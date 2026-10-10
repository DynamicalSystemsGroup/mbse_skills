import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/mbse-model-tdd/scripts'))
from normalize_capture import convert, normalize, validate_report, verify_retained


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


starter = load('test_starter', ROOT / 'skills/setup-mbse-skills/scripts/init_project.py')
trace = load('test_trace', ROOT / 'skills/mbse-traceability/scripts/trace_check.py')
demo = load('test_onboarding_demo', ROOT / 'scripts/onboarding_demo.py')


class OnboardingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_starter_repeat_and_preflight_preserve_project(self):
        project = self.root / 'project'
        starter.initialize(project)
        self.assertEqual(starter.initialize(project)['created'], 0)
        (project / 'README.md').write_text('User-owned content')
        (project / 'docs/glossary.md').unlink()
        with self.assertRaisesRegex(ValueError, 'existing project content'):
            starter.initialize(project)
        self.assertEqual((project / 'README.md').read_text(), 'User-owned content')
        self.assertFalse((project / 'docs/glossary.md').exists())

    def test_starter_rejects_symlink_escape(self):
        project = self.root / 'project'
        project.mkdir()
        outside = self.root / 'outside'
        outside.mkdir()
        (project / 'docs').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'escaping'):
            starter.initialize(project)
        self.assertEqual(list(outside.iterdir()), [])

    def test_end_to_end_retained_evidence_and_change(self):
        result = demo.run(self.root / 'project')
        self.assertEqual(result['normalized_records'], 40)
        self.assertEqual(result['selected_capacity_j'], 270000)
        self.assertEqual(result['changed_remaining_fraction'], '-1/9')
        self.assertTrue(result['stale_assumption_detected'])
        self.assertIn('not_run', result['changed_engine_check'])
        with self.assertRaisesRegex(ValueError, 'fresh destination'):
            demo.run(self.root / 'project')

    def graph(self):
        (self.root / 'source.md').write_text('original obligation')
        sha = hashlib.sha256((self.root / 'source.md').read_bytes()).hexdigest()
        nodes = [{'id': i, 'kind': kind, 'status': 'proposed', 'title': i, 'path': 'source.md', 'sha256': sha}
                 for i, kind in [('N', 'need'), ('R', 'requirement'), ('V', 'verification'), ('E', 'evidence')]]
        nodes[1]['acceptance'] = 'observable criterion'
        nodes[3]['status'] = 'observed'
        edges = [{'source': a, 'target': b, 'relation': r, 'rationale': 'explicit dependency'} for a, b, r in [('R', 'N', 'derives_from'), ('V', 'R', 'verifies'), ('E', 'V', 'evidence_for')]]
        return {'schema_version': 1, 'nodes': nodes, 'edges': edges}

    def test_requirement_change_requires_check_and_evidence_review(self):
        graph = self.graph()
        result = trace.inspect(graph, self.root, ['R'])
        self.assertEqual(result['review_required'], ['E', 'R', 'V'])
        self.assertTrue(result['recorded_coverage_complete'])
        graph['nodes'][1]['acceptance'] = None
        self.assertFalse(trace.inspect(graph, self.root)['recorded_coverage_complete'])

    def test_historical_and_planned_evidence_do_not_cover_current_claim(self):
        graph = self.graph()
        graph['nodes'][3]['status'] = 'historical'
        self.assertFalse(trace.inspect(graph, self.root)['recorded_coverage_complete'])
        graph['nodes'][3]['status'] = 'proposed'
        self.assertFalse(trace.inspect(graph, self.root)['recorded_coverage_complete'])
        graph['nodes'][3]['status'] = 'observed'
        graph['nodes'][2]['status'] = 'historical'
        self.assertFalse(trace.inspect(graph, self.root)['recorded_coverage_complete'])

    def test_stale_shared_file_and_empty_graph_are_not_coverage_proof(self):
        graph = self.graph()
        (self.root / 'source.md').write_text('changed obligation')
        result = trace.inspect(graph, self.root)
        self.assertFalse(result['fresh'])
        self.assertEqual(len(result['stale']), 4)
        self.assertFalse(trace.inspect({'schema_version': 1, 'nodes': [], 'edges': []}, self.root)['recorded_coverage_complete'])

    def test_trace_cycles_unknown_changes_and_external_paths_fail(self):
        graph = self.graph()
        with self.assertRaisesRegex(ValueError, 'unknown changed'):
            trace.inspect(graph, self.root, ['missing'])
        graph['edges'].append({'source': 'N', 'target': 'E', 'relation': 'depends_on', 'rationale': 'cycle'})
        with self.assertRaisesRegex(ValueError, 'cycle'):
            trace.inspect(graph, self.root)
        graph = self.graph()
        graph['nodes'][0]['path'] = '../outside.md'
        with self.assertRaisesRegex(ValueError, 'outside project'):
            trace.inspect(graph, self.root)

    def native(self):
        return json.loads((ROOT / 'examples/rover/evidence/cli.json').read_text())

    def test_native_disagreement_unknown_and_skipped_remain_distinct(self):
        report = normalize(self.native(), 'evidence/cli.json', 'a' * 64)
        rows = {(r['engine'], r['case'], r['operation']): r for r in report['records']}
        self.assertEqual(rows['opensysml', 'unknown', 'verify']['outcome'], 'unavailable')
        self.assertEqual(rows['toolkit', 'unknown', 'verify']['outcome'], 'undecided')
        self.assertEqual(rows['opensysml', 'unresolved', 'validate']['outcome'], 'rejected')
        self.assertEqual(rows['toolkit', 'unresolved', 'validate']['outcome'], 'accepted')
        self.assertEqual(rows['opensysml', 'syntax-error', 'verify']['outcome'], 'not_run')
        self.assertEqual(rows['toolkit', 'green', 'verify']['subject_scope']['kind'], 'file-eligible-checks')

    def test_tampered_outcomes_and_incomplete_satisfaction_fail(self):
        native = self.native()
        native['runs'][0]['verification']['outcome'] = 'holds'
        with self.assertRaisesRegex(ValueError, 'disagrees'):
            normalize(native, 'cli.json', 'a' * 64)
        report = normalize(self.native(), 'cli.json', 'a' * 64)
        row = report['records'][1]
        row['measurement'] = 'timeout'
        row['outcome'] = 'satisfied'
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            validate_report(report)

    def test_unsupported_requires_capability_evidence(self):
        report = normalize(self.native(), 'cli.json', 'a' * 64)
        row = report['records'][1]
        row['outcome'] = 'unsupported'
        with self.assertRaisesRegex(ValueError, 'capability evidence'):
            validate_report(report)
        row['capability_evidence'] = {'type': 'synthetic test only', 'statement': 'operation explicitly unsupported'}
        validate_report(report)
        row['measurement'] = 'not-run'
        validate_report(report)
        row['measurement'] = 'timeout'
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            validate_report(report)

    def test_conversion_retains_native_hash_and_preserves_output(self):
        path = self.root / 'cli.json'
        path.write_text(json.dumps(self.native()))
        output = self.root / 'report.json'
        report = convert(path, output, self.root)
        self.assertEqual(report['source']['sha256'], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(verify_retained(report, self.root)['records_replayed'], 40)
        before = output.read_bytes()
        with self.assertRaises(FileExistsError):
            convert(path, output, self.root)
        self.assertEqual(output.read_bytes(), before)

    def test_native_replay_rejects_plausible_report_forgery_and_source_change(self):
        path = self.root / 'cli.json'
        path.write_text(json.dumps(self.native()))
        report = convert(path, self.root / 'report.json', self.root)
        forged = copy.deepcopy(report)
        forged['records'][1]['outcome'] = 'satisfied'
        validate_report(forged)  # Shape alone cannot establish an observation.
        with self.assertRaisesRegex(ValueError, 'native interpretation'):
            verify_retained(forged, self.root)
        path.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'source identity'):
            verify_retained(report, self.root)
