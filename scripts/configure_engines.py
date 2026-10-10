"""Record explicit existing engine/library paths and hashes; install nothing."""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'skills/mbse-model-tdd/scripts'))
from engine_check import file_hash, library_hash

parser = argparse.ArgumentParser(description=__doc__)
for option in ('opensysml', 'toolkit', 'opensysml-lsp', 'library'):
    parser.add_argument('--' + option, required=True)
parser.add_argument('--output', default='.local/engines.json')
args = parser.parse_args()
try:
    engines = {}
    for name in ('opensysml', 'toolkit', 'opensysml-lsp'):
        path = Path(getattr(args, name.replace('-', '_'))).expanduser().resolve(strict=True)
        engines[name] = {'executable': str(path), 'sha256': file_hash(path)}
    library = Path(args.library).expanduser().resolve(strict=True)
    profile = {'engines': engines, 'library': str(library), 'library_sha256': library_hash(library)}
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(profile, indent=2) + '\n')
except (OSError, ValueError) as error:
    parser.exit(2, str(error) + '\n')
print(f'Profile written: {output}. Inspect versions before running checks.')
