"""Copy the portable starter into a new project, preserving existing files."""
import argparse
import json
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[1] / 'assets/project-template'


def initialize(destination, template=TEMPLATE):
    destination = Path(destination).resolve()
    template = Path(template).resolve()
    if destination == template or destination.is_relative_to(template):
        raise ValueError('destination cannot be inside the bundled template')
    files = sorted(p for p in template.rglob('*') if p.is_file())
    pending = []
    for source in files:
        target = destination / source.relative_to(template)
        if not target.resolve().is_relative_to(destination):
            raise ValueError('destination contains a path escaping the project')
        if target.exists():
            if not target.is_file() or target.read_bytes() != source.read_bytes():
                raise ValueError(f'existing project content differs: {target.relative_to(destination)}; configure it manually')
        else:
            for parent in target.parents:
                if parent == destination.parent:
                    break
                if parent.exists() and not parent.is_dir():
                    raise ValueError('destination parent is not a directory')
            pending.append((source, target))
    for source, target in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(source.read_bytes())
    return {'destination': str(destination), 'created': len(pending), 'template_files': len(files)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination')
    args = parser.parse_args()
    try:
        print(json.dumps(initialize(args.destination)))
    except (OSError, ValueError) as error:
        parser.exit(2, str(error) + '\n')
