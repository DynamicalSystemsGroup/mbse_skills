"""Evidence-preserving visualization checks, independent of optional renderers."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result
scene = module('scene_check', 'skills/mbse-excalidraw/scripts/scene_check.py')
plot = module('plot_energy', 'skills/mbse-engineering-plots/scripts/plot_energy.py')

class VisualizationTests(unittest.TestCase):
    def setUp(self):
        self.scene = json.loads((ROOT / 'examples/visualization/rover-energy.excalidraw').read_text())
        self.summary = json.loads((ROOT / 'examples/rover/evidence/summary.json').read_text())

    def test_binding_survives_geometry_change_but_deleted_target_fails(self):
        self.assertEqual(scene.check_scene(self.scene)['live_elements'], 10)
        self.scene['elements'][2]['x'] += 50
        scene.check_scene(self.scene)
        self.scene['elements'][2]['isDeleted'] = True
        with self.assertRaisesRegex(ValueError, 'missing|deleted'):
            scene.check_scene(self.scene)

    def test_duplicate_ids_nonfinite_geometry_and_nonreciprocal_binding_fail(self):
        for defect in ('duplicate', 'nonfinite', 'binding'):
            candidate = copy.deepcopy(self.scene)
            if defect == 'duplicate':
                candidate['elements'].append(candidate['elements'][0])
            elif defect == 'nonfinite':
                candidate['elements'][0]['x'] = float('nan')
            else:
                candidate['elements'][2]['boundElements'] = []
            with self.assertRaises(ValueError):
                scene.check_scene(candidate)

    def test_remaining_arithmetic_and_selection_are_checked(self):
        points, _, selected = plot.prepare(self.summary, '0.2')
        self.assertEqual(selected, 270000)
        self.assertEqual([point['status'] for point in points], ['infeasible', 'feasible', 'feasible'])
        self.summary['candidates'][1]['remaining_fraction'] = '1/3'
        with self.assertRaisesRegex(ValueError, 'arithmetic'):
            plot.prepare(self.summary, '0.2')
        self.summary['candidates'][1]['remaining_fraction'] = '7/27'
        self.summary['selected_capacity_joules'] = 360000
        with self.assertRaisesRegex(ValueError, 'smallest'):
            plot.prepare(self.summary, '0.2')

    def test_unknown_and_conflicting_evidence_do_not_become_feasible(self):
        self.summary['selected_capacity_joules'] = None
        self.summary['candidates'][1]['engine_verdicts']['toolkit'] = 'undecided'
        points, _, _ = plot.prepare(self.summary, '0.2')
        self.assertEqual(points[1]['status'], 'inconclusive')
        self.summary['candidates'][1]['engine_verdicts']['toolkit'] = 'violated'
        points, _, _ = plot.prepare(self.summary, '0.2')
        self.assertEqual(points[1]['status'], 'conflict')

    def test_svg_escapes_labels_and_preserves_existing_output(self):
        self.summary['candidates'][0]['case'] = '<untrusted & case>'
        points, reserve, selected = plot.prepare(self.summary, '0.2')
        svg = plot.render(points, reserve, selected)
        ET.fromstring(svg)
        self.assertIn('&lt;untrusted &amp; case&gt;', svg)
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / 'input.json', Path(directory) / 'plot.svg'
            source.write_text(json.dumps(self.summary))
            plot.generate(source, output, '0.2')
            original = output.read_bytes()
            with self.assertRaises(FileExistsError):
                plot.generate(source, output, '0.2')
            self.assertEqual(output.read_bytes(), original)

    def test_unsupported_scene_is_not_partially_certified(self):
        self.scene['elements'][0]['type'] = 'image'
        with self.assertRaisesRegex(ValueError, 'unsupported'):
            scene.check_scene(self.scene)

if __name__ == '__main__':
    unittest.main()
