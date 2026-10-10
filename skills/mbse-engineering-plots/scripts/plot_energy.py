"""Render a finite energy-budget summary as a reproducible standalone SVG."""
import argparse
from fractions import Fraction
import hashlib
from html import escape
import json
import math
from pathlib import Path
import platform

VERDICTS = {'holds', 'violated', 'undecided', 'unavailable', 'unsupported', 'not-run'}


def prepare(summary, reserve):
    reserve = Fraction(reserve)
    if not 0 < reserve < 1:
        raise ValueError('reserve must be between zero and one')
    used = Fraction(summary['reference']['used_energy_joules'])
    if used < 0:
        raise ValueError('used energy must be nonnegative')
    candidates = summary['candidates']
    if not isinstance(candidates, list) or not 1 <= len(candidates) <= 32:
        raise ValueError('expected 1..32 candidates')
    result, seen = [], set()
    for candidate in candidates:
        case = candidate['case']
        if not isinstance(case, str) or not case or len(case) > 40 or case in seen:
            raise ValueError('case IDs must be unique nonempty strings of at most 40 characters')
        seen.add(case)
        capacity = candidate['capacity_joules']
        if type(capacity) is not int or capacity <= 0:
            raise ValueError(f'{case}: capacity must be a positive integer in joules')
        remaining = Fraction(candidate['remaining_fraction'])
        if remaining != (capacity - used) / capacity:
            raise ValueError(f'{case}: remaining fraction disagrees with energy arithmetic')
        verdicts = candidate['engine_verdicts']
        if not isinstance(verdicts, dict) or not verdicts or any(
            not isinstance(key, str) or not isinstance(value, str) or value not in VERDICTS
            for key, value in verdicts.items()
        ):
            raise ValueError(f'{case}: expected named engine outcomes')
        math_feasible = remaining >= reserve
        states = set(verdicts.values())
        conflict = ('holds' in states and not math_feasible) or ('violated' in states and math_feasible)
        if conflict:
            status = 'conflict'
        elif states == {'holds'} and math_feasible:
            status = 'feasible'
        elif states == {'violated'} and not math_feasible:
            status = 'infeasible'
        else:
            status = 'inconclusive'
        if not all(math.isfinite(float(value)) for value in (capacity, remaining, reserve)):
            raise ValueError(f'{case}: value exceeds plotting range')
        result.append({'case': case, 'capacity_joules': capacity, 'remaining_fraction': str(remaining),
                       'engine_verdicts': verdicts, 'status': status})
    selected = summary.get('selected_capacity_joules')
    if selected is not None:
        feasible = [point['capacity_joules'] for point in result if point['status'] == 'feasible']
        if type(selected) is not int or not feasible or selected != min(feasible):
            raise ValueError('selected capacity is not the smallest supported feasible listed capacity')
        if sum(point['capacity_joules'] == selected and point['status'] == 'feasible' for point in result) != 1:
            raise ValueError('selected capacity does not identify a unique feasible candidate')
    return result, reserve, selected


def render(points, reserve, selected):
    identity = json.dumps({'points': points, 'reserve': str(reserve), 'selected': selected}, sort_keys=True)
    prefix = 'energy-' + hashlib.sha256(identity.encode()).hexdigest()[:16]
    capacities = [point['capacity_joules'] / 1000 for point in points]
    percentages = [float(Fraction(point['remaining_fraction'])) * 100 for point in points]
    threshold = float(reserve) * 100
    xmin, xmax = min(capacities), max(capacities)
    xpad = max((xmax - xmin) * .15, xmax * .1, 1)
    xmin, xmax = max(0, xmin - xpad), xmax + xpad
    ymin, ymax = min(0, *percentages), max(threshold, *percentages)
    ypad = max((ymax - ymin) * .18, 5)
    ymin, ymax = ymin - ypad, ymax + ypad
    xp = lambda value: 120 + (value - xmin) / (xmax - xmin) * 750
    yp = lambda value: 450 - (value - ymin) / (ymax - ymin) * 300
    choice = f'{selected / 1000:g} kJ selected from listed candidates' if selected is not None else 'No selection asserted'
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" role="img" aria-labelledby="{prefix}-title {prefix}-desc">',
           f'<title id="{prefix}-title">Finite energy trade study</title>',
           f'<desc id="{prefix}-desc">Candidate capacities and modeled remaining energy. Threshold is supplied by the caller. Negative reserve is an idealized budget deficit. Engine results are not physical validation.</desc>',
           '<rect width="1000" height="640" fill="#ffffff"/>',
           '<g font-family="sans-serif" fill="#172536">',
           '<text x="70" y="48" font-size="25" font-weight="bold">Finite energy trade study</text>',
           f'<text x="70" y="78" font-size="16">{escape(choice)}</text>',
           '<text x="70" y="103" font-size="14">Analytical budget under constant inputs; no physical validation or uncertainty band</text>']
    for tick in range(5):
        x = xmin + (xmax - xmin) * tick / 4
        y = ymin + (ymax - ymin) * tick / 4
        svg += [f'<line x1="120" y1="{yp(y):.3f}" x2="870" y2="{yp(y):.3f}" stroke="#dbe2e8"/>',
                f'<text x="105" y="{yp(y)+5:.3f}" text-anchor="end" font-size="14">{y:.1f}</text>',
                f'<text x="{xp(x):.3f}" y="477" text-anchor="middle" font-size="14">{x:.1f}</text>']
    svg += ['<path d="M120 150 V450 H870" fill="none" stroke="#506070"/>',
            '<text x="495" y="516" text-anchor="middle" font-size="17">Usable capacity (kJ)</text>',
            '<text transform="translate(35 300) rotate(-90)" text-anchor="middle" font-size="17">Remaining energy (%)</text>',
            f'<line x1="120" y1="{yp(threshold):.3f}" x2="870" y2="{yp(threshold):.3f}" stroke="#506070" stroke-dasharray="7 5"/>',
            f'<text x="870" y="{yp(threshold)-9:.3f}" text-anchor="end" font-size="14">Supplied reserve: {threshold:g}%</text>']
    colors = {'feasible': '#167260', 'infeasible': '#b23844', 'inconclusive': '#946c10', 'conflict': '#7954a1'}
    for point, capacity, percentage in zip(points, capacities, percentages):
        x, y, status = xp(capacity), yp(percentage), point['status']
        value_y = y + 25
        if abs(value_y - yp(threshold)) < 14:
            value_y += 18
        title = escape(f"{point['case']}: {point['remaining_fraction']}; {point['engine_verdicts']}")
        svg.append(f'<g fill="{colors[status]}"><title>{title}</title>')
        if status == 'feasible':
            svg.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="7"/>')
        elif status == 'infeasible':
            svg.append(f'<path d="M{x-7:.3f},{y-7:.3f} l14,14 m-14,0 l14,-14" fill="none" stroke="{colors[status]}" stroke-width="3"/>')
        else:
            svg.append(f'<path d="M{x:.3f},{y-9:.3f} l9,9 -9,9 -9,-9 Z"/>')
        svg += [f'<text x="{x:.3f}" y="{y-18:.3f}" text-anchor="middle" font-size="15" font-weight="bold">{escape(point["case"])}</text>',
                f'<text x="{x:.3f}" y="{value_y:.3f}" text-anchor="middle" font-size="14">{percentage:.2f}% — {status}</text>', '</g>']
    svg += ['<text x="70" y="561" font-size="14">Circle: feasible • Cross: infeasible • Diamond: inconclusive/conflicting evidence</text>',
            '<text x="70" y="588" font-size="14">Discrete candidates only. Missing results are not success. Negative values indicate budget deficit.</text>',
            '<text x="70" y="615" font-size="14">Retain the adjacent receipt for exact values, source identity and plotting assumptions.</text>', '</g></svg>']
    return '\n'.join(svg) + '\n'


def generate(source, output, reserve):
    source, output = Path(source), Path(output)
    receipt = output.with_suffix('.receipt.json')
    raw = source.read_bytes()
    points, reserve, selected = prepare(json.loads(raw), reserve)
    rendered = render(points, reserve, selected).encode()
    record = {'source_file': source.name, 'source_sha256': hashlib.sha256(raw).hexdigest(),
              'svg_sha256': hashlib.sha256(rendered).hexdigest(),
              'helper_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python_version': platform.python_version(), 'reserve_supplied': str(reserve),
              'selected_capacity_joules': selected, 'points': points,
              'checks': {'arithmetic': 'passed', 'svg_generation': 'passed', 'visual_review': 'not run'},
              'limits': ['supplied threshold not independently verified against model source',
                         'finite candidates only; no engine execution or physical validation',
                         'no uncertainty data or collision check']}
    if output.exists() or receipt.exists():
        raise FileExistsError('preserve existing output/receipt; choose new paths')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('xb') as stream:
        stream.write(rendered)
    with receipt.open('x') as stream:
        stream.write(json.dumps(record, indent=2) + '\n')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('summary', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--reserve', required=True, help='explicit fractional reserve, e.g. 0.2')
    args = parser.parse_args()
    try:
        record = generate(args.summary, args.output, args.reserve)
        print(json.dumps({'output': str(args.output), 'source_sha256': record['source_sha256'], 'points': len(record['points'])}))
    except (OSError, ValueError, KeyError, TypeError, OverflowError, ZeroDivisionError) as error:
        parser.exit(1, f'{error}\n')

if __name__ == '__main__':
    main()
