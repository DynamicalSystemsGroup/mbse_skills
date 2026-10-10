"""Extract a bounded Mermaid flowchart or uncompressed Draw.io structural view."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

NODE = r'([A-Za-z_][A-Za-z0-9_]*)(?:\["([^"\n]*)"\])?'
EDGE = re.compile(NODE + r'\s*(-->|-\.->)(?:\|([^|\n]*)\|)?\s*' + NODE)


def mermaid(text):
    nodes, edges, metadata = {}, [], {}
    declared = set()
    lines = text.splitlines()
    first = next((i for i, line in enumerate(lines) if line.strip() and not line.strip().startswith('%%')), None)
    if first is None or not re.fullmatch(r'(flowchart|graph)\s+(LR|RL|TB|TD|BT)', lines[first].strip()):
        raise ValueError('expected flowchart/graph direction header')
    def node(key, label):
        if key not in nodes:
            nodes[key] = {'id': key, 'label': key, 'parent': None}
        if label is not None:
            if key in declared and nodes[key]['label'] != label:
                raise ValueError(f'conflicting node label: {key}')
            nodes[key]['label'] = label
            declared.add(key)
    for number, line in enumerate(lines[first+1:], first+2):
        line = line.strip()
        if not line or line.startswith('%%'):
            continue
        if line in {'end', 'subgraph'}:
            raise ValueError(f'unsupported Mermaid statement at line {number}')
        meta = re.fullmatch(r'(accTitle|accDescr):\s*(.+)', line)
        if meta:
            if meta[1] in metadata:
                raise ValueError('duplicate accessibility metadata')
            metadata[meta[1]] = meta[2]
            continue
        match = EDGE.fullmatch(line)
        if match:
            source, slabel, arrow, label, target, tlabel = match.groups()
            node(source, slabel)
            node(target, tlabel)
            raw_label = label or ''
            if label and label.startswith('"') and label.endswith('"'):
                label = label[1:-1]
            edges.append({'id': f'edge-{len(edges)+1}', 'source': source, 'target': target,
                          'label': label or '', 'raw_label': raw_label,
                          'line_style': 'dashed' if arrow == '-.->' else 'solid'})
        else:
            match = re.fullmatch(NODE, line)
            if not match:
                raise ValueError(f'unsupported Mermaid statement at line {number}')
            node(*match.groups())
    return list(nodes.values()), edges, metadata


def drawio(text):
    if '<!DOCTYPE' in text.upper() or '<!ENTITY' in text.upper():
        raise ValueError('DTD/entities unsupported')
    root = ET.fromstring(text)
    if root.tag == 'mxfile':
        pages = list(root)
        if len(pages) != 1 or pages[0].tag != 'diagram' or len(pages[0]) != 1:
            raise ValueError('expected one uncompressed Draw.io page')
        root = pages[0][0]
    if root.tag != 'mxGraphModel' or len(root) != 1 or root[0].tag != 'root':
        raise ValueError('expected uncompressed mxGraphModel/root')
    cells = list(root[0])
    if any(cell.tag != 'mxCell' for cell in cells):
        raise ValueError('unsupported Draw.io object wrapper')
    ids = [cell.get('id') for cell in cells]
    if any(not key for key in ids) or len(set(ids)) != len(ids):
        raise ValueError('missing/duplicate cell ID')
    nodes, edges = [], []
    vertices = {cell.get('id') for cell in cells if cell.get('vertex') == '1'}
    parents = {}
    for cell in cells:
        key, parent = cell.get('id'), cell.get('parent')
        if parent is not None and parent not in ids:
            raise ValueError('unknown parent cell')
        parents[key] = parent
        if any(child.tag != 'mxGeometry' for child in cell):
            raise ValueError('unsupported cell child')
        if cell.get('vertex') == '1' and cell.get('edge') == '1':
            raise ValueError('cell cannot be vertex and edge')
        if cell.get('vertex') == '1':
            nodes.append({'id': key, 'label': cell.get('value', ''),
                          'parent': parent if parent in vertices else None})
        elif cell.get('edge') == '1':
            source, target = cell.get('source'), cell.get('target')
            if source not in vertices or target not in vertices:
                raise ValueError('edge endpoint missing or unsupported')
            edges.append({'id': key, 'source': source, 'target': target,
                          'label': cell.get('value', ''), 'line_style': 'unknown'})
        elif cell.get('value') or cell.get('source') or cell.get('target'):
            raise ValueError('unsupported non-vertex content')
    for key in ids:
        seen, cursor = set(), key
        while cursor is not None:
            if cursor in seen:
                raise ValueError('cyclic parent ownership')
            seen.add(cursor)
            cursor = parents[cursor]
    return nodes, edges, {}


def extract(raw, format):
    if len(raw) > 1024 * 1024:
        raise ValueError('input exceeds 1 MiB')
    text = raw.decode('utf-8')
    nodes, edges, metadata = {'mermaid': mermaid, 'drawio': drawio}[format](text)
    if len(nodes) > 1000 or len(edges) > 2000:
        raise ValueError('view exceeds node/edge budget')
    return {'schema_version': 1, 'format': format,
            'source_sha256': hashlib.sha256(raw).hexdigest(),
            'helper_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'nodes': nodes, 'edges': edges, 'accessibility': metadata,
            'counts': {'nodes': len(nodes), 'edges': len(edges)},
            'limits': ['structural subset only; no renderer or semantic validation',
                       'labels are inert strings; escape before rendering',
                       'source styles/geometry not retained; source bytes remain authoritative']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--format', required=True, choices=('mermaid', 'drawio'))
    args = parser.parse_args()
    try:
        with args.source.open('rb') as stream:
            raw = stream.read(1024 * 1024 + 1)
        print(json.dumps(extract(raw, args.format), indent=2))
    except (OSError, ValueError, ET.ParseError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
