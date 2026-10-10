import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("distribution", ROOT / "scripts/check_distribution.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("pyproject.toml", "CHANGELOG.md"):
            shutil.copy(ROOT / name, self.root / name)
        shutil.copytree(ROOT / ".claude-plugin", self.root / ".claude-plugin")
        shutil.copytree(ROOT / "skills", self.root / "skills", ignore=shutil.ignore_patterns("__pycache__"))

    def test_current_distribution(self):
        self.assertEqual(module.check(self.root)["skills"], 15)

    def test_version_drift_is_rejected(self):
        path = self.root / ".claude-plugin/plugin.json"
        data = json.loads(path.read_text())
        data["version"] = "9.0.0"
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "version"):
            module.check(self.root)

    def test_external_marketplace_source_is_rejected(self):
        path = self.root / ".claude-plugin/marketplace.json"
        data = json.loads(path.read_text())
        data["plugins"][0]["source"] = "../another-repository"
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "repository root"):
            module.check(self.root)

    def test_missing_portable_skill_is_rejected(self):
        shutil.rmtree(self.root / "skills/setup-mbse-skills")
        with self.assertRaisesRegex(ValueError, "catalog"):
            module.check(self.root)
