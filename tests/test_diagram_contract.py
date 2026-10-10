"""Check preservation, bounded failures and embeddable accessibility IDs."""
from test_visualization import module, ROOT
import json
import unittest
import xml.etree.ElementTree as ET

plot = module('plot_contract', 'skills/mbse-engineering-plots/scripts/plot_energy.py')
svg = module('svg_contract', 'skills/mbse-diagramming/scripts/svg_check.py')
importer = module('import_contract', 'skills/mbse-diagramming/scripts/import_view.py')


class DiagramContractTests(unittest.TestCase):
    def test_figure_ids_are_reproducible_and_distinct(self):
        summary = json.loads((ROOT / 'examples/rover/evidence/summary.json').read_text())
        points, reserve, selected = plot.prepare(summary, '0.2')
        first = plot.render(points, reserve, selected)
        self.assertEqual(first, plot.render(points, reserve, selected))
        self.assertEqual(svg.check(first.encode())['geometry'], 'not-run')
        second = plot.render(points, reserve, None)
        ids = lambda text: {e.get('id') for e in ET.fromstring(text).iter() if e.get('id')}
        self.assertFalse(ids(first) & ids(second))
        with self.assertRaises(ValueError):
            svg.check(first.replace(ET.fromstring(first)[0].get('id'), 'missing', 1).encode())

    def test_active_content_and_duplicate_ids_fail(self):
        raw = '<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="view-title view-desc"><title id="view-title">View</title><desc id="view-desc">Details</desc></svg>'
        svg.check(raw.encode())
        for content in ('<script/>', '<animate/>', '<path onclick="run()"/>',
                        '<use href="https://example.org/image.svg"/>', '<g id="view-title"/>'):
            with self.assertRaises(ValueError):
                svg.check(raw.replace('</svg>', content + '</svg>').encode())

    def test_actual_mermaid_topology_and_accessibility_survive(self):
        result = importer.extract((ROOT / 'examples/visualization/rover-energy.mmd').read_bytes(), 'mermaid')
        self.assertEqual(result['counts'], {'nodes': 4, 'edges': 3})
        self.assertEqual([(e['source'], e['target']) for e in result['edges']],
                         [('battery', 'load'), ('scenario', 'load'), ('load', 'budget')])
        self.assertEqual(result['accessibility']['accTitle'], 'Proposed rover energy-flow slice')
        self.assertEqual(result['edges'][1]['line_style'], 'dashed')
        self.assertEqual(result['edges'][1]['label'], 'scenario assumption')
        self.assertEqual(result['edges'][1]['raw_label'], '"scenario assumption"')

    def test_unsupported_mermaid_and_conflicting_labels_fail(self):
        for content in ('subgraph group\nA\nend', 'A --> B --> C', 'click A callback',
                        'accDescr {\nmultiline\n}', 'A["one"]\nA["two"]', 'end'):
            with self.assertRaises(ValueError):
                importer.extract(('flowchart LR\n' + content).encode(), 'mermaid')
        result = importer.extract(b'flowchart LR\nA --> B\nA["later label"]', 'mermaid')
        self.assertEqual(result['nodes'][0]['label'], 'later label')

    def test_drawio_groups_and_dangling_compressed_cycles(self):
        raw = b'<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="g" vertex="1" parent="1" value="Group"/><mxCell id="a" vertex="1" parent="g" value="A"/><mxCell id="b" vertex="1" parent="1" value="B"/><mxCell id="e" edge="1" source="a" target="b" value="energy" parent="1"/></root></mxGraphModel>'
        result = importer.extract(raw, 'drawio')
        self.assertEqual(result['counts'], {'nodes': 3, 'edges': 1})
        self.assertEqual(result['nodes'][1]['parent'], 'g')
        self.assertEqual(result['edges'][0]['label'], 'energy')
        wrapped = b'<mxfile><diagram>' + raw + b'</diagram></mxfile>'
        self.assertEqual(importer.extract(wrapped, 'drawio')['nodes'], result['nodes'])
        for invalid in (raw.replace(b'target="b"', b'target="missing"'),
                        raw.replace(b'id="g" vertex="1" parent="1"', b'id="g" vertex="1" parent="a"'),
                        b'<mxfile><diagram>compressed-content</diagram></mxfile>',
                        b'<!DOCTYPE root><mxGraphModel><root/></mxGraphModel>'):
            with self.assertRaises(ValueError):
                importer.extract(invalid, 'drawio')

    def test_import_size_is_bounded(self):
        with self.assertRaisesRegex(ValueError, '1 MiB'):
            importer.extract(b' ' * (1024 * 1024 + 1), 'mermaid')


if __name__ == '__main__':
    unittest.main()
