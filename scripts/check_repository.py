"""Validate this collection's simple metadata, resources and local links."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check_catalog(catalog, names):
    entries = catalog.get('skills', [])
    indexed = {entry['name']: entry for entry in entries}
    errors = []
    if catalog.get('schema_version') != 1:
        errors.append('unsupported catalog schema')
    if len(indexed) != len(entries) or set(indexed) != set(names):
        errors.append('catalog must list each skill exactly once')
    for name, entry in indexed.items():
        if entry.get('layer') not in ('core', 'methodology', 'language-tool', 'visualization'):
            errors.append(f'{name}: invalid layer')
        dependencies = entry.get('requires', [])
        if not isinstance(dependencies, list) or any(not isinstance(d, str) for d in dependencies):
            errors.append(f'{name}: invalid prerequisites')
            continue
        for dependency in dependencies:
            if dependency not in indexed:
                errors.append(f'{name}: missing prerequisite {dependency}')
            elif entry.get('layer') == 'core' and indexed[dependency].get('layer') != 'core':
                errors.append(f'{name}: core cannot require an extension')
    visiting, visited = set(), set()
    def visit(name):
        if name in visiting:
            errors.append(f'{name}: prerequisite cycle')
            return
        if name in visited:
            return
        visiting.add(name)
        dependencies = indexed[name].get('requires', [])
        if isinstance(dependencies, list):
            for dependency in dependencies:
                if isinstance(dependency, str) and dependency in indexed:
                    visit(dependency)
        visiting.remove(name)
        visited.add(name)
    for name in indexed:
        visit(name)
    return errors


def check(root=ROOT):
    errors = []
    skills = sorted((root / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills found')
    catalog = json.loads((root / 'skills/catalog.json').read_text())
    errors.extend(check_catalog(catalog, [file.parent.name for file in skills]))
    for file in skills:
        text = file.read_text()
        parts = text.split('---', 2)
        if not text.startswith('---\n') or len(parts) != 3:
            errors.append(f'{file}: missing frontmatter')
            continue
        metadata = {}
        for line in parts[1].strip().splitlines():
            if ':' not in line:
                errors.append(f'{file}: invalid metadata line')
                continue
            key, value = line.split(':', 1)
            if key in metadata:
                errors.append(f'{file}: duplicate field {key}')
            metadata[key] = value.strip()
        name = metadata.get('name', '')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name != file.parent.name or len(name) > 64:
            errors.append(f'{file}: invalid name')
        description = metadata.get('description', '')
        if not description or len(description) > 1024:
            errors.append(f'{file}: invalid description')
        if metadata.get('license') != 'Apache-2.0':
            errors.append(f'{file}: expected original Apache-2.0 material')
        if len(text.splitlines()) >= 500 or re.search(r'\bTODO\b|\[INSERT|\[TODO', text):
            errors.append(f'{file}: excessive length or unfinished scaffold')
        ui = file.parent / 'agents/openai.yaml'
        if not ui.exists():
            errors.append(f'{file}: missing UI metadata')
        else:
            ui_text = ui.read_text()
            match = re.search(r'  short_description: "([^"\n]+)"', ui_text)
            if not match or not 25 <= len(match[1]) <= 64:
                errors.append(f'{ui}: invalid short description')
    links = 0
    markdown = [root / 'README.md', root / 'NOTICE.md', root / 'CONTRIBUTING.md', root / 'AGENTS.md']
    for directory in ('docs', 'skills', 'examples', 'evaluations'):
        markdown.extend((root / directory).rglob('*.md'))
    for file in markdown:
        if not file.exists():
            errors.append(f'{file}: missing document')
            continue
        text = file.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith('#'):
                continue
            path = (file.parent / target.split('#')[0]).resolve()
            if not path.exists():
                errors.append(f'{file}: broken link {target}')
            links += 1
    manifest = json.loads((root / 'references/sources.json').read_text())
    for entry in manifest['repositories']:
        if not re.fullmatch('[0-9a-f]{40}', entry['commit']):
            errors.append('invalid source commit')
    if errors:
        raise ValueError('\n'.join(errors))
    return {'skills': len(skills), 'local_links': links, 'source_records': len(manifest['repositories'])}

if __name__ == '__main__':
    try:
        print(json.dumps(check()))
    except (ValueError, OSError, KeyError) as error:
        sys.exit(str(error))
