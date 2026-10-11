"""Check portable plugin packaging; optionally sync version from pyproject.toml."""
import argparse
import json
from pathlib import Path
import re
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    version = tomllib.loads((root / "pyproject.toml").read_text())["project"]["version"]
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text())
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("release version must be major.minor.patch")
    if plugin.get("name") != "mbse-skills" or plugin.get("version") != version:
        raise ValueError("plugin identity/version differs from project; run sync-version")
    if plugin.get("license") != "MIT" or not plugin.get("author", {}).get("name"):
        raise ValueError("missing distribution license or author")
    if set(plugin) - {"name", "version", "description", "author", "license", "keywords", "repository", "homepage"}:
        raise ValueError("unexpected plugin fields: review component/URL changes explicitly")
    entries = marketplace.get("plugins", [])
    if marketplace.get("name") != "mbse-skills-community" or len(entries) != 1:
        raise ValueError("unexpected marketplace identity or plugin count")
    if entries[0].get("name") != plugin["name"] or entries[0].get("source") != "./":
        raise ValueError("marketplace must resolve this repository root")
    catalog = json.loads((root / "skills/catalog.json").read_text())
    folders = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if folders != {s["name"] for s in catalog["skills"]} or "setup-mbse-skills" not in folders:
        raise ValueError("default skills scan and catalog disagree")
    if f"## [{version}]" not in (root / "CHANGELOG.md").read_text():
        raise ValueError("missing changelog entry for release version")
    return {"plugin": plugin["name"], "version": version, "skills": len(folders)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync-version", action="store_true")
    args = parser.parse_args()
    if args.sync_version:
        path = ROOT / ".claude-plugin/plugin.json"
        plugin = json.loads(path.read_text())
        plugin["version"] = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
        path.write_text(json.dumps(plugin, indent=2) + "\n")
    print(json.dumps(check()))
