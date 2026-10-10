"""Build and verify a clean teaching project from portable MBSE resources."""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/mbse-model-tdd/scripts'))
from engine_check import run_suite
from normalize_capture import convert, validate_report, verify_retained


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


starter = load('starter', ROOT / 'skills/setup-mbse-skills/scripts/init_project.py')
traces = load('traces', ROOT / 'skills/mbse-traceability/scripts/trace_check.py')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(destination, profile=None):
    destination = Path(destination).resolve()
    if destination.exists() and any(destination.iterdir()):
        raise ValueError('choose a fresh destination; existing project is preserved')
    initialized = starter.initialize(destination)
    repeated = starter.initialize(destination)
    assert repeated['created'] == 0, 'unchanged starter should be idempotent'
    scenario = json.loads((ROOT / 'examples/team-onboarding/scenario.json').read_text())
    (destination / 'scenario.json').write_text(json.dumps(scenario, indent=2) + '\n')
    used = Fraction(scenario['distance_m'], scenario['speed_m_per_s']) * scenario['power_w']
    reserve = Fraction(scenario['reserve_fraction'])
    threshold = used / (1 - reserve)
    candidates = scenario['candidate_capacities_j']
    selected = min(c for c in candidates if Fraction(c - used, c) >= reserve)
    assert selected == scenario['selected_capacity_j'] == 270000
    docs = {
        'needs.md': '# Proposed teaching need\n\nN-01: A mission planner needs the rover to complete the 2 km traverse with energy retained for subsequent activity. No stakeholder approval is recorded.\n',
        'requirements.md': '# Proposed requirements\n\nR-01: Under A-01, the rover shall complete the 2000 m traverse with remaining usable energy >=20% of initial usable battery capacity. Proposed; stakeholder owner unresolved. Verification: V-01 modeled energy analysis. Intended-use validation remains open.\n',
        'architecture.md': '# Proposed logical architecture\n\nL-01: Provide mobility. L-02: Supply energy to mobility. Allocate energy supply to a candidate battery; assume 100 W covers the aggregate load. The interface exchanges energy in joules at fixed power in watts. Detailed electrical interfaces and failure behavior remain open.\n',
        'decisions.md': f'# Proposed decision\n\nD-01: Select {selected} J as the smallest feasible capacity among the listed {candidates} J candidates under A-01. Analytical threshold is {threshold} J. This is not a global mass/cost optimum or an accepted procurement decision. Depend on R-01, A-01 and E-01/E-02.\n',
        'verification.md': '# Verification matrix\n\nV-01 checks modeled R-01 under A-01. E-01 selects green constraint records from model-report.json for both engines. E-02 retains the native finite-set summary and exact arithmetic. Native model-validation does not establish constraint satisfaction. Toolkit verifies all eligible file conditions; this teaching model has one constraint. Physical mission validation and reserve suitability are not run.\n',
        'glossary.md': '# Teaching project glossary\n\nReserve means remaining energy divided by initial usable capacity, not mission demand. Model-validation means a configured tool acceptance check; validation of intended use requires stakeholder evidence. These meanings are proposed conventions, not institutional definitions or owner approval.\n',
        'mbse-project.md': '# Teaching project conventions\n\nBoundary: rover; terrain/operator outside. All needs, requirements, assumptions and decisions are proposed. IDs and trace links are collection conventions. Authoritative obligations: requirements.md; scenario: ../scenario.json; models: ../models/. Trace source depends on target.\n\nSelected core practices: discovery, requirements, architecture, verification, traceability and constraint reasoning. Extension: SysML model-TDD. Existing native observations are retained, not represented as fresh runs. Tool paths stay in the separate local profile.\n\nEvidence: ../evidence/; verification.md describes scope. Next task: review changed 3 km assumptions, reevaluate R-01 and rerun affected checks before relying on historical evidence. Physical validation and stakeholder acceptance remain open.\n',
    }
    for name, text in docs.items():
        (destination / 'docs' / name).write_text(text)
    (destination / 'README.md').write_text('# Rover teaching project\n\nRead [project conventions](docs/mbse-project.md), [requirements](docs/requirements.md) and [verification scope](docs/verification.md). All engineering decisions are proposed. The project retains actual native model observations; these do not establish physical adequacy or stakeholder acceptance. `evidence/onboarding-result.json` records which checks this run executed.\n')
    (destination / 'evidence/README.md').write_text('# Teaching evidence\n\n`cli.json` and `summary.json` are retained historical rover observations, copied without changes. `model-report.json` normalizes their operation outcomes and points to native evidence. `change-impact.json` reports recorded dependencies requiring review. If an explicit existing engine profile was supplied, `changed-cli.json` retains fresh changed-mission checks. Consult `onboarding-result.json` for actual run scope. No physical or stakeholder validation was performed.\n')
    models = destination / 'models'
    models.mkdir()
    for source in (ROOT / 'examples/rover').glob('*.sysml'):
        shutil.copyfile(source, models / source.name)
    evidence = destination / 'evidence'
    shutil.copyfile(ROOT / 'examples/rover/evidence/cli.json', evidence / 'cli.json')
    shutil.copyfile(ROOT / 'examples/rover/evidence/summary.json', evidence / 'summary.json')
    normalized = convert(evidence / 'cli.json', evidence / 'model-report.json', destination)
    validate_report(normalized)
    verify_retained(normalized, destination)
    for record in normalized['records']:
        assert record['model_sha256'] == sha(models / (record['case'] + '.sysml')), 'captured model identity differs'
    verdicts = {(r['engine'], r['case'], r['operation']): r['outcome'] for r in normalized['records']}
    for engine in ('opensysml', 'toolkit'):
        assert verdicts[engine, 'red', 'verify'] == 'violated'
        assert verdicts[engine, 'green', 'verify'] == 'satisfied'
        assert verdicts[engine, 'boundary', 'verify'] == 'satisfied'
        assert verdicts[engine, 'below-boundary', 'verify'] == 'violated'
    nodes = []
    def node(identity, kind, path, title, status='proposed', **extras):
        nodes.append({'id': identity, 'kind': kind, 'status': status, 'path': path,
                      'sha256': sha(destination / path), 'title': title, **extras})
    node('N-01', 'need', 'docs/needs.md', 'Mission need')
    node('A-01', 'assumption', 'scenario.json', 'Constant-input mission assumptions')
    node('R-01', 'requirement', 'docs/requirements.md', 'Mission reserve', acceptance='remaining usable energy / initial usable capacity >= 1/5 after 2000 m under A-01')
    node('L-01', 'architecture', 'docs/architecture.md', 'Logical mobility and energy responsibility')
    node('M-01', 'model', 'models/green.sysml', '270 kJ modeled candidate')
    node('V-01', 'verification', 'docs/verification.md', 'Modeled reserve check')
    node('E-01', 'evidence', 'evidence/model-report.json', 'Retained green modeled-condition results', 'observed', record_ids=['opensysml:green:verify', 'toolkit:green:verify'])
    node('E-02', 'evidence', 'evidence/summary.json', 'Retained finite candidate comparison', 'observed')
    node('D-01', 'decision', 'docs/decisions.md', 'Proposed finite-set choice')
    pairs = [
        ('R-01', 'N-01', 'derives_from'), ('R-01', 'A-01', 'depends_on'),
        ('L-01', 'R-01', 'allocated_from'), ('M-01', 'R-01', 'realizes'),
        ('M-01', 'L-01', 'depends_on'), ('M-01', 'A-01', 'depends_on'),
        ('V-01', 'R-01', 'verifies'), ('V-01', 'M-01', 'depends_on'),
        ('E-01', 'V-01', 'evidence_for'), ('E-01', 'M-01', 'depends_on'),
        ('E-02', 'V-01', 'evidence_for'), ('E-02', 'A-01', 'depends_on'),
        ('D-01', 'R-01', 'depends_on'), ('D-01', 'E-01', 'depends_on'), ('D-01', 'E-02', 'depends_on'),
    ]
    graph = {'schema_version': 1, 'nodes': nodes,
             'edges': [{'source': a, 'target': b, 'relation': r, 'rationale': 'Recorded teaching dependency; inspect referenced artifact for scope.'} for a, b, r in pairs]}
    (destination / 'traceability.json').write_text(json.dumps(graph, indent=2) + '\n')
    trace = traces.inspect(graph, destination, ['A-01'])
    assert trace['fresh'] and trace['recorded_coverage_complete']
    expected_impact = {'A-01', 'R-01', 'L-01', 'M-01', 'V-01', 'E-01', 'E-02', 'D-01'}
    assert set(trace['review_required']) == expected_impact
    (evidence / 'change-impact.json').write_text(json.dumps(trace, indent=2) + '\n')
    with tempfile.TemporaryDirectory() as scratch:
        stale_project = Path(scratch) / 'project'
        shutil.copytree(destination, stale_project)
        (stale_project / 'scenario.json').write_text('{"distance_m":3000}\n')
        stale = traces.inspect(graph, stale_project)
        assert not stale['fresh'] and stale['stale'][0]['id'] == 'A-01'
        assert set(stale['review_required']) == expected_impact
    changed_used = Fraction(scenario['changed_distance_m'], scenario['speed_m_per_s']) * scenario['power_w']
    changed_remaining = Fraction(selected - changed_used, selected)
    assert changed_remaining < reserve
    change_model = (models / 'green.sysml').read_text().replace('distance : LengthValue = 2000 [m]', 'distance : LengthValue = 3000 [m]')
    assert change_model != (models / 'green.sysml').read_text()
    (models / 'changed-mission.sysml').write_text(change_model)
    live_status = 'not_run: no profile supplied; changed result is independent arithmetic only'
    if profile:
        manifest = {'subject': 'Rover::energyReserve', 'cases': [{'id': 'changed-mission', 'model': 'models/changed-mission.sysml', 'expected_validation': 'valid', 'expected_verification': 'violated'}]}
        manifest_path = destination / 'changed-cases.json'
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
        live = run_suite(profile, manifest_path, evidence / 'changed-cli.json')
        assert live['expectations_met'], 'changed model engine expectations did not match'
        convert(evidence / 'changed-cli.json', evidence / 'changed-model-report.json', destination)
        live_status = 'both configured engines accepted model validation and reported changed modeled condition violated'
    result = {'starter': initialized, 'starter_repeat_created': repeated['created'], 'normalized_records': len(normalized['records']),
              'recorded_trace_coverage_complete': trace['recorded_coverage_complete'], 'stale_assumption_detected': True,
              'change_review_required': trace['review_required'], 'used_energy_j': str(used), 'boundary_j': str(threshold),
              'selected_capacity_j': selected, 'changed_remaining_fraction': str(changed_remaining), 'changed_engine_check': live_status,
              'client_plugin_discovery': 'separate gate; see retained native marketplace discovery record',
              'limits': ['teaching assumptions and decisions are proposed', 'retained observations predate onboarding', 'no physical or intended-use validation']}
    (evidence / 'onboarding-result.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination')
    parser.add_argument('--profile')
    args = parser.parse_args()
    try:
        print(json.dumps(run(args.destination, args.profile), indent=2))
    except (OSError, ValueError, KeyError, AssertionError) as error:
        parser.exit(2, str(error) + '\n')
