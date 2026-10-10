"""Run the bounded rover checks and finite candidate comparison."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'skills/mbse-model-tdd/scripts'))
from engine_check import run_suite
from lsp_check import run as run_lsp


def reference(distance=2000, speed=1, power=100, reserve=Fraction(1, 5)):
    duration = Fraction(distance, speed)
    used = power * duration
    boundary = used / (1 - reserve)
    return {'duration_seconds': str(duration), 'used_energy_joules': str(used),
            'boundary_capacity_joules': str(boundary)}


def demo(profile, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    cli = run_suite(profile, 'examples/rover/cases.json', output / 'cli.json')
    lsp = run_lsp(profile, output / 'lsp.json', 'examples/rover/green.sysml')
    rows = []
    for case, capacity in [('red', 180000), ('green', 270000), ('large', 360000)]:
        verdicts = {r['engine']: r.get('verification', {}).get('outcome', 'unavailable')
                    for r in cli['runs'] if r['case'] == case}
        rows.append({'case': case, 'capacity_joules': capacity,
                     'remaining_fraction': str(Fraction(capacity - 200000, capacity)),
                     'engine_verdicts': verdicts,
                     'feasible_in_both_observations': all(v == 'holds' for v in verdicts.values()) and len(verdicts) == 2})
    feasible = [r for r in rows if r['feasible_in_both_observations']]
    selected = min(feasible, key=lambda r: r['capacity_joules'])['capacity_joules'] if feasible else None
    result = {'reference': reference(), 'objective': 'minimum capacity in the explicitly listed finite candidate set',
              'candidates': rows, 'selected_capacity_joules': selected,
              'expectations_met': cli['expectations_met'] and lsp['expectations_met'] and selected == 270000,
              'limits': ['constant power/speed and usable capacity; no physical validation',
                        'Toolkit uses configured external library; OpenSysML uses bundled libraries',
                        'LSP diagnostics do not execute the energy constraint',
                        'OpenSysML diagnostics lack server document versions in this build']}
    (output / 'summary.json').write_text(json.dumps(result, indent=2) + '\n')
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--output', default='.local/rover-demo')
    args = parser.parse_args()
    try:
        result = demo(args.profile, args.output)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(2, str(error) + '\n')
    print(json.dumps({'expectations_met': result['expectations_met'], 'selected_capacity_joules': result['selected_capacity_joules'], 'output': args.output}))
    raise SystemExit(0 if result['expectations_met'] else 1)
