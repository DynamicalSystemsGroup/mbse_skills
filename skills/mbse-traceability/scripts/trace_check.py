"""Validate an explicit trace dependency graph and report bounded change impact."""
import argparse
import hashlib
import json
from pathlib import Path
import re

KINDS = {'need', 'assumption', 'requirement', 'architecture', 'decision', 'model', 'verification', 'evidence'}
STATUSES = {'proposed', 'accepted', 'open', 'observed', 'historical'}
RELATIONS = {'derives_from', 'depends_on', 'allocated_from', 'realizes', 'verifies', 'evidence_for', 'informs'}


def inspect(graph, root, changed=()):
    root = Path(root).resolve()
    if graph.get('schema_version') != 1 or not isinstance(graph.get('nodes'), list) or not isinstance(graph.get('edges'), list):
        raise ValueError('unsupported or malformed trace graph')
    nodes, dependencies, reverse, stale = {}, {}, {}, []
    for node in graph['nodes']:
        identity = node.get('id')
        if not isinstance(identity, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', identity) or identity in nodes:
            raise ValueError('invalid or duplicate node ID')
        if node.get('kind') not in KINDS or node.get('status') not in STATUSES or not isinstance(node.get('title'), str) or not node['title'].strip():
            raise ValueError(f'{identity}: invalid kind, status or title')
        if node['kind'] == 'requirement' and (('acceptance' not in node) or (node['acceptance'] is not None and (not isinstance(node['acceptance'], str) or not node['acceptance'].strip()))):
            raise ValueError(f'{identity}: acceptance must be a criterion or null')
        relative = node.get('path')
        digest = node.get('sha256')
        if not isinstance(relative, str) or not relative or Path(relative).is_absolute() or not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest):
            raise ValueError(f'{identity}: invalid artifact path/hash')
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f'{identity}: artifact missing or outside project')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            stale.append({'id': identity, 'recorded_sha256': digest, 'actual_sha256': actual})
        nodes[identity] = node
        dependencies[identity], reverse[identity] = set(), set()
    seen = set()
    for edge in graph['edges']:
        source, target = edge.get('source'), edge.get('target')
        relation = edge.get('relation')
        if source not in nodes or target not in nodes or relation not in RELATIONS or source == target:
            raise ValueError('invalid trace endpoint or relationship')
        if not isinstance(edge.get('rationale'), str) or not edge['rationale'].strip():
            raise ValueError('trace rationale missing')
        signature = (source, target, relation)
        if signature in seen:
            raise ValueError('duplicate trace relationship')
        seen.add(signature)
        dependencies[source].add(target)
        reverse[target].add(source)
    visited, active = set(), set()
    def visit(identity):
        if identity in active:
            raise ValueError('trace dependency cycle')
        if identity in visited:
            return
        active.add(identity)
        for target in dependencies[identity]:
            visit(target)
        active.remove(identity)
        visited.add(identity)
    for identity in nodes:
        visit(identity)
    def closure(start, adjacency):
        found, pending = set(), list(start)
        while pending:
            identity = pending.pop()
            if identity not in found:
                found.add(identity)
                pending.extend(adjacency[identity])
        return found
    coverage = []
    for identity, node in nodes.items():
        if node['kind'] != 'requirement':
            continue
        needs = sorted(i for i in closure([identity], dependencies) if nodes[i]['kind'] == 'need')
        checks = sorted(e['source'] for e in graph['edges'] if e['target'] == identity and e['relation'] == 'verifies' and nodes[e['source']]['kind'] == 'verification' and nodes[e['source']]['status'] != 'historical')
        evidence = sorted({e['source'] for e in graph['edges'] if e['target'] in checks and e['relation'] == 'evidence_for' and nodes[e['source']]['kind'] == 'evidence' and nodes[e['source']]['status'] in {'observed', 'accepted'}})
        gaps = [label for label, value in [('acceptance', node['acceptance']), ('need', needs), ('verification', checks), ('evidence', evidence)] if not value]
        coverage.append({'requirement': identity, 'status': node['status'], 'needs': needs, 'verification': checks, 'evidence': evidence, 'gaps': gaps})
    changed = set(changed)
    if changed - nodes.keys():
        raise ValueError('unknown changed IDs: ' + ', '.join(sorted(changed - nodes.keys())))
    affected = closure(changed | {s['id'] for s in stale}, reverse)
    current = [c for c in coverage if c['status'] != 'historical']
    return {'schema_version': 1, 'nodes': len(nodes), 'fresh': not stale, 'stale': stale, 'coverage': coverage,
            'recorded_coverage_complete': bool(current) and all(not c['gaps'] for c in current),
            'review_required': sorted(affected), 'limits': ['recorded dependencies only', 'file identity, not semantic freshness', 'no satisfaction or approval certification']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph')
    parser.add_argument('--root', required=True)
    parser.add_argument('--changed', action='append', default=[])
    parser.add_argument('--require-covered', action='store_true')
    args = parser.parse_args()
    try:
        result = inspect(json.loads(Path(args.graph).read_text()), args.root, args.changed)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + '\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['fresh'] and (not args.require_covered or result['recorded_coverage_complete']) else 1)
