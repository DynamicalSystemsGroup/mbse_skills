"""Check a bounded static SVG accessibility contract, not rendered geometry."""
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def check(raw):
    if len(raw) > 1024 * 1024:
        raise ValueError('SVG exceeds 1 MiB')
    if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
        raise ValueError('DTD/entities unsupported')
    root = ET.fromstring(raw)
    ns = '{http://www.w3.org/2000/svg}'
    if root.tag != ns + 'svg' or root.get('role') != 'img':
        raise ValueError('expected standalone SVG with role="img"')
    ids = {}
    for element in root.iter():
        key = element.get('id')
        if key:
            if key in ids:
                raise ValueError(f'duplicate ID: {key}')
            ids[key] = element
        if element.tag in {ns + tag for tag in ('script', 'foreignObject', 'animate', 'animateMotion', 'animateTransform', 'set', 'style')}:
            raise ValueError('active/animated/styled content outside static checker scope')
        if any(name.lower().startswith('on') for name in element.attrib):
            raise ValueError('event handler unsupported')
        for name, value in element.attrib.items():
            if name.rsplit('}', 1)[-1] == 'href':
                if not value.startswith('#'):
                    raise ValueError('external reference unsupported')
                if value[1:] not in {item.get('id') for item in root.iter()}:
                    raise ValueError('unresolved local reference')
    references = root.get('aria-labelledby', '').split()
    if len(references) != 2 or len(set(references)) != 2:
        raise ValueError('aria-labelledby must name distinct title and description')
    for key, tag in zip(references, ('title', 'desc')):
        target = ids.get(key)
        if target is None or target.tag != ns + tag or target not in list(root):
            raise ValueError('unresolved or misplaced accessibility reference')
        if not key.endswith('-' + tag) or not key[:-len(tag)-1]:
            raise ValueError('accessibility IDs must be diagram-prefixed')
        if not ''.join(target.itertext()).strip():
            raise ValueError('empty accessibility text')
    if list(root)[0].tag != ns + 'title':
        raise ValueError('title must be first child')
    return {'static_svg_accessibility': 'passed', 'geometry': 'not-run',
            'visual_review': 'not-run', 'model_semantics': 'not-run'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('svg', type=Path)
    args = parser.parse_args()
    try:
        with args.svg.open('rb') as stream:
            result = check(stream.read(1024 * 1024 + 1))
        print(json.dumps(result))
    except (OSError, ValueError, ET.ParseError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
