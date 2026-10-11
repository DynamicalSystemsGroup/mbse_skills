# Development, visualization and engine checks

For installation into an engineering project, use [the first-task walkthrough](first-task.md). This page is for a full repository checkout and deliberately configured local tools.

## Development and checks

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/); [just](https://just.systems/) supplies shortcuts. There are no Python package dependencies. From this repository root:

```bash
uv sync --locked --offline
just check
```

Without just, run the three commands in its `check` recipe: `uv run --locked --offline python scripts/check_repository.py`, `uv run --locked --offline python scripts/check_distribution.py`, and `uv run --locked --offline python -m unittest discover -s tests -v`.

The repository check validates the simple metadata format used here, UI description bounds, resources and local links. It is not a general YAML parser or an agent-behavior test. See [contributing](../CONTRIBUTING.md) for baseline/assisted artifact evaluation and source review.

## Visualization tools

The visualization extensions reuse available tools or external skills while keeping engineering source mapping and evidence in this collection. See the [existing-skill search](research/visualization-skill-discovery.md) for Mermaid, UML/PlantUML, Excalidraw and Archify candidates; none was installed or vendored. [Archify-inspired principles](research/visualization-inspiration.md) explain our view and review contracts.

The [output contract](../skills/mbse-diagramming/references/view-contract.md) adds destination sizing, fidelity ledgers, geometry review and optional project styles. [Semantic patterns](../skills/mbse-diagramming/references/semantic-patterns.md) and [behavior examples](../skills/mbse-diagramming/references/behavior-examples.md) support authoring. The [import contract](../skills/mbse-diagramming/references/import-contract.md) documents a bounded Mermaid-flowchart/uncompressed-Draw.io extractor; unsupported constructs fail explicitly. The static SVG checker validates accessibility markup, not geometry or model semantics:

```bash
python3 skills/mbse-diagramming/scripts/import_view.py examples/visualization/rover-energy.mmd --format mermaid
python3 skills/mbse-diagramming/scripts/svg_check.py examples/visualization/rover-energy-accessible.svg
```

The [diagram-family coverage](../skills/mbse-diagramming/references/diagram-families.md) distinguishes authoring criteria from formal notation and tested exports. The [visualization example](../examples/visualization/README.md) contains Mermaid/DOT sources, a native Excalidraw scene and a reviewed SVG trade-study plot. Native Mermaid/Graphviz rendering and Excalidraw editor import/export have not been exercised here. Matplotlib and Vega-Lite are optional existing-environment branches, not dependencies. The limited plot helper and scene structural checker use only Python's stdlib:

```bash
just visual-demo .local/visualization-demo/energy.svg
```

Choose a fresh output path for a rerun; the plot helper preserves existing exports and receipts. The generated plot does not execute engines or validate a physical rover.

## Configure and run engines

Use existing, deliberately selected local executables and a library directory. Configuration records byte hashes; it does not download or certify tools. Follow your team's context and dependency policies before dependency or remote operations; inspect Git status and use `ctxcheck` if your environment provides it. No global installs are needed.

```bash
just configure /path/to/sysml /path/to/sysmlv2 /path/to/sysml-lsp /path/to/sysml.library
just demo .local/engines.json
```

The equivalent commands are `uv run --locked --offline python scripts/configure_engines.py` with its four named path arguments, and `uv run --locked --offline python scripts/rover_demo.py --profile .local/engines.json`. Inspect `--help` for options.

The tested contracts are OpenSysML source revision `714c459fe5dcce1affb62fd98309b63626dfa311` and Toolkit 0.10.0. Other versions need calibration before their output is interpreted. OpenSysML uses bundled libraries; Toolkit uses the explicit external library. Commands run without a shell and exclude ambient model/library settings and credentials. Hash mismatches stop execution rather than silently replacing a tool.

Reports are written to `.local/rover-demo/`: native CLI results, LSP transcripts and the finite comparison summary. The LSP transcript contains the model text. Keep confidential project captures in an appropriate local location. See the [rover example](../examples/rover/README.md), [verification record](verification.md), and [evaluation method](../evaluations/README.md).

## Research and scope

- [Inspiration comparison](research/inspiration-comparison.md): seven sources, mechanisms, dependencies and adoption decisions.
- [Mechanism principles](research/skill-collection-principles.md): skills, scripts, hooks, LSP, MCP and plugins.
- [MBSE source map](research/mbse-source-map.md): OMG, INCOSE, NASA, SEBoK and implementation evidence.
- [Diagram-design review](research/diagram-design-review.md): visualization gaps, adoption priorities and observed helper limitations.
- [SysML v2 views, features and requirements](research/sysml-v2-features-diagrams-requirements.md): clause-linked inventory, requirements semantics, limitations and reviewed NotebookLM findings.
- [Adaptive interview techniques](research/adaptive-discovery-interviews.md): open-to-specific questioning, choice bias and stakeholder elicitation.
- [Starter specifications](starter-specifications.md): triggers, outputs and controls.
- [Source revisions and licenses](../references/sources.json).

Study clones under `references/repos/` are ignored and inactive. To recreate one, use its recorded upstream/revision after checking context; do not refresh an existing checkout blindly. OpenSysML's study checkout is reused from the nearby standards-research workspace.
