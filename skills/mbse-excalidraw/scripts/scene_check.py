"""Check a bounded, editable basic Excalidraw scene; not the full native schema."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def check_scene(scene):
    if scene.get('type') != 'excalidraw' or scene.get('version') != 2:
        raise ValueError('expected Excalidraw document format version 2')
    if not isinstance(scene.get('appState'), dict) or not isinstance(scene.get('files'), dict):
        raise ValueError('appState and files must be objects')
    elements = scene.get('elements')
    if not isinstance(elements, list):
        raise ValueError('elements must be a list')
    indexed = {}
    for element in elements:
        if not isinstance(element, dict):
            raise ValueError('element must be an object')
        identity = element.get('id')
        if not isinstance(identity, str) or not identity or identity in indexed:
            raise ValueError('element IDs must be unique nonempty strings')
        indexed[identity] = element
    live = {key: value for key, value in indexed.items() if not value.get('isDeleted', False)}
    supported = {'rectangle', 'ellipse', 'diamond', 'text', 'arrow'}
    for identity, element in live.items():
        kind = element.get('type')
        if kind not in supported:
            raise ValueError(f'{identity}: unsupported live element type {kind}')
        for field in ('x', 'y', 'width', 'height', 'angle'):
            if not finite(element.get(field)):
                raise ValueError(f'{identity}: {field} must be finite')
        if element['width'] < 0 or element['height'] < 0:
            raise ValueError(f'{identity}: negative size')
        references = element.get('boundElements') or []
        if not isinstance(references, list):
            raise ValueError(f'{identity}: invalid boundElements')
        seen = set()
        for binding in references:
            if not isinstance(binding, dict):
                raise ValueError(f'{identity}: invalid bound element')
            target = binding.get('id')
            if not isinstance(target, str) or target not in live or target in seen:
                raise ValueError(f'{identity}: missing, deleted or duplicate bound element')
            seen.add(target)
            if binding.get('type') != live[target]['type']:
                raise ValueError(f'{identity}: bound element type mismatch')
            partner = live[target]
            if partner['type'] == 'text':
                if partner.get('containerId') != identity:
                    raise ValueError(f'{identity}: text container is not reciprocal')
            elif partner['type'] == 'arrow':
                endpoints = [partner.get(key) or {} for key in ('startBinding', 'endBinding')]
                if identity not in [endpoint.get('elementId') for endpoint in endpoints]:
                    raise ValueError(f'{identity}: arrow binding is not reciprocal')
            else:
                raise ValueError(f'{identity}: unsupported bound element relationship')
        if kind == 'text':
            if not isinstance(element.get('text'), str):
                raise ValueError(f'{identity}: text must be a string')
            container = element.get('containerId')
            if container is not None:
                if container not in live or live[container]['type'] not in {'rectangle', 'ellipse', 'diamond'}:
                    raise ValueError(f'{identity}: missing or unsupported text container')
                if {'id': identity, 'type': 'text'} not in (live[container].get('boundElements') or []):
                    raise ValueError(f'{identity}: text binding is not reciprocal')
        if kind == 'arrow':
            points = element.get('points')
            if not isinstance(points, list) or len(points) < 2 or any(
                not isinstance(point, list) or len(point) != 2 or not all(finite(v) for v in point)
                for point in points
            ):
                raise ValueError(f'{identity}: arrow needs finite point pairs')
            for key in ('startBinding', 'endBinding'):
                binding = element.get(key)
                if binding is None:
                    continue
                if not isinstance(binding, dict):
                    raise ValueError(f'{identity}: invalid {key}')
                target = binding.get('elementId')
                if not isinstance(target, str) or target not in live or live[target]['type'] not in {'rectangle', 'ellipse', 'diamond'}:
                    raise ValueError(f'{identity}: missing, deleted or unsupported arrow target')
                if {'id': identity, 'type': 'arrow'} not in (live[target].get('boundElements') or []):
                    raise ValueError(f'{identity}: arrow binding is not reciprocal')
    return {'live_elements': len(live), 'scope': 'basic structural subset; editor import and visual review not run'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scene', type=Path)
    args = parser.parse_args()
    try:
        raw = args.scene.read_bytes()
        result = check_scene(json.loads(raw))
        result['scene_sha256'] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(result))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        parser.exit(1, f'{error}\n')

if __name__ == '__main__':
    main()
