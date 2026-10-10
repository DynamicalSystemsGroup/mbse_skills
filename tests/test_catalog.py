"""Protect language-independent core and resolvable workflow composition."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('repository_check', Path(__file__).resolve().parents[1] / 'scripts/check_repository.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class CatalogTests(unittest.TestCase):
    def catalog(self, entries):
        return {'schema_version': 1, 'skills': entries}

    def test_core_cannot_require_tool_or_visualization_extension(self):
        for layer in ('language-tool', 'visualization'):
            with self.subTest(layer=layer):
                entries = [
                    {'name': 'requirements', 'layer': 'core', 'requires': ['extension']},
                    {'name': 'extension', 'layer': layer, 'requires': []},
                ]
                self.assertIn('requirements: core cannot require an extension', checker.check_catalog(self.catalog(entries), ['requirements', 'extension']))
                entries[0]['requires'] = []
                entries[1]['requires'] = ['requirements']
                self.assertEqual(checker.check_catalog(self.catalog(entries), ['requirements', 'extension']), [])

    def test_missing_prerequisite_and_cycle_are_rejected(self):
        entries = [{'name': 'oosem', 'layer': 'methodology', 'requires': ['absent']}]
        self.assertIn('oosem: missing prerequisite absent', checker.check_catalog(self.catalog(entries), ['oosem']))
        entries = [
            {'name': 'a', 'layer': 'core', 'requires': ['b']},
            {'name': 'b', 'layer': 'core', 'requires': ['a']},
        ]
        self.assertTrue(any('cycle' in error for error in checker.check_catalog(self.catalog(entries), ['a', 'b'])))

    def test_catalog_covers_each_portable_folder_once(self):
        entry = {'name': 'a', 'layer': 'core', 'requires': []}
        for entries, names in [([entry], ['a', 'b']), ([entry, entry], ['a'])]:
            self.assertIn('catalog must list each skill exactly once', checker.check_catalog(self.catalog(entries), names))

if __name__ == '__main__':
    unittest.main()
