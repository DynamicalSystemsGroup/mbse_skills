# MBSE agent skills

[![Repository checks](https://github.com/DynamicalSystemsGroup/mbse_skills/actions/workflows/checks.yml/badge.svg?branch=main)](https://github.com/DynamicalSystemsGroup/mbse_skills/actions/workflows/checks.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-2563eb?style=flat)](LICENSE)
[![Status: early draft](https://img.shields.io/badge/status-early%20draft-f59e0b?style=flat)](docs/share-readiness.md)
[![Python: 3.11+](https://img.shields.io/badge/python-3.11%2B-3776ab?style=flat&logo=python&logoColor=white)](pyproject.toml)
[![SysML v2: partial coverage](https://img.shields.io/badge/SysML%20v2-partial%20coverage-0f766e?style=flat)](docs/collection-architecture.md)

A portable collection of systems engineering practices with optional methodology, modeling-language and tool extensions. The core can be used with prose, tables or a project's chosen modeling representation; it does not require SysML or an engine.

## About

Hosted by [Dynamical Systems Group](https://github.com/DynamicalSystemsGroup/mbse_skills), this independent project welcomes OpenMBEE and other teams building agent-assisted engineering workflows. Version 0.1.0 is an early draft: coverage and client support are bounded by the documented evidence, and no institutional endorsement or complete SysML conformance is claimed.

For collaboration, start with [contributing](CONTRIBUTING.md), [governance](GOVERNANCE.md), [community conduct](CODE_OF_CONDUCT.md) and [security reporting](SECURITY.md). Use GitHub issues for bugs/proposals and discussions for questions.

## Core and extensions

| Layer | Skills |
| --- | --- |
| Core | [Project setup](skills/setup-mbse-skills/SKILL.md), [Discovery](skills/mbse-discovery/SKILL.md), [Grill me](skills/mbse-grill-me/SKILL.md), [requirements](skills/mbse-requirements/SKILL.md), [architecture](skills/mbse-architecture/SKILL.md), [verification and validation](skills/mbse-verification/SKILL.md), [traceability/change impact](skills/mbse-traceability/SKILL.md), [constraint reasoning](skills/mbse-constraint-reasoning/SKILL.md), [standards research](skills/mbse-standards-research/SKILL.md), [literature research](skills/mbse-literature-research/SKILL.md) |
| Methodology | [OOSEM starter adaptation](skills/mbse-oosem/SKILL.md) |
| Language/tool | [SysML v2/KerML modeling](skills/mbse-sysml-modeling/SKILL.md), [SysML engine-backed model TDD](skills/mbse-model-tdd/SKILL.md) |
| Visualization | [Diagramming](skills/mbse-diagramming/SKILL.md), [Excalidraw sketches](skills/mbse-excalidraw/SKILL.md), [engineering plots](skills/mbse-engineering-plots/SKILL.md) |

The checked [catalog](skills/catalog.json) records layer membership and composition prerequisites. Flat skill folders preserve portable client discovery and existing helper paths; layer membership does not require nested installation folders. The catalog is metadata, not a runtime router or installer. Its `requires` entries name core practices needed for the composed workflow; read those entrypoints when applying that workflow, or explicitly identify unavailable practices. No downloads are implied.

Harmony, RUP SE, State Analysis, Vitech MBSE and OPM are **research candidates**, not implemented skills. Read [collection architecture](docs/collection-architecture.md) for boundaries, current coverage and extension acceptance criteria.

Use `mbse-grill-me` when you want an interactive engineering interview or plan stress-test. It starts open-ended, adapts one main question at a time, and offers potential answers later when useful. There is no total question cap; it stops at a useful brief or when you pause. Precise edits and factual lookups do not need an interview. See the [technique comparison](docs/research/adaptive-discovery-interviews.md) for sources and transfer limits.

Each folder has a standard `SKILL.md`, focused references where needed and UI metadata. Engine/LSP helpers remain bundled with the SysML model-TDD extension. Plugin packaging is available; no router, hook, MCP server or tool installation runs automatically.

The [OOSEM-oriented rover walkthrough](examples/rover/oosem-walkthrough.md) connects a proposed need to requirements, logical responsibilities, allocation and existing SysML evidence. It is a bounded teaching example, not a complete OOSEM implementation, conformance certification or physically validated rover design.

## Use with an agent

For plugin use, load this reviewed checkout in Claude Code with `claude --plugin-dir /absolute/path/to/mbse_skills`, then invoke `/mbse-skills:setup-mbse-skills` in your engineering project. The setup skill records project conventions and an actionable first task. See [installation and releases](docs/distribution.md) for local marketplace installation, editable skills, compatibility limits and the publication checklist. Codex CLI marketplace discovery has passed; installation and skill invocation remain untested.


Point the agent to the relevant entrypoint, for example: “Use `skills/mbse-model-tdd/SKILL.md` to establish a failing check, revise my model and retain the evidence.” For discovery through your client's normal skill mechanism, copy or symlink the selected complete skill folders into that client's project-local skills directory. Keep an existing installation intact and avoid installing the same skill twice. Check the client's current discovery conventions; compatibility across all clients has not been tested.

A full repository checkout is needed for the included example and development checks; individual skill folders supply their own reasoning references and required helpers. Standards and engines remain separately accessed resources. The collection does not bundle standards PDFs or engine binaries.

## Start a team project

The setup skill carries an editable starter with needs, requirements, architecture, decisions, glossary and evidence conventions. For a fresh project, use its bundled `scripts/init_project.py`; established projects keep their own conventions. Read the [clean-project acceptance example](examples/team-onboarding/README.md) to exercise the complete flow:

```bash
just onboarding-demo .local/team-onboarding
```

This builds a project from the starter, verifies retained model/evidence identities, checks requirement trace coverage and reports change impact. An optional existing engine profile exercises the changed model; the default run makes no new engine observations. The [shared vocabulary](skills/mbse-discovery/references/vocabulary.md), [trace graph contract](skills/mbse-traceability/references/graph-contract.md) and [model verification report contract](skills/mbse-model-tdd/references/verification-contract.md) define their boundaries.

## Development and checks

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/); [just](https://just.systems/) supplies shortcuts. There are no Python package dependencies. From this repository root:

```bash
uv sync --locked --offline
just check
```

Without just, run the three commands in its `check` recipe: `uv run --locked --offline python scripts/check_repository.py`, `uv run --locked --offline python scripts/check_distribution.py`, and `uv run --locked --offline python -m unittest discover -s tests -v`.

The repository check validates the simple metadata format used here, UI description bounds, resources and local links. It is not a general YAML parser or an agent-behavior test. See [contributing](CONTRIBUTING.md) for baseline/assisted artifact evaluation and source review.

## Visualization tools

The visualization extensions reuse available tools or external skills while keeping engineering source mapping and evidence in this collection. See the [existing-skill search](docs/research/visualization-skill-discovery.md) for Mermaid, UML/PlantUML, Excalidraw and Archify candidates; none was installed or vendored. [Archify-inspired principles](docs/research/visualization-inspiration.md) explain our view and review contracts.

The [output contract](skills/mbse-diagramming/references/view-contract.md) adds destination sizing, fidelity ledgers, geometry review and optional project styles. [Semantic patterns](skills/mbse-diagramming/references/semantic-patterns.md) and [behavior examples](skills/mbse-diagramming/references/behavior-examples.md) support authoring. The [import contract](skills/mbse-diagramming/references/import-contract.md) documents a bounded Mermaid-flowchart/uncompressed-Draw.io extractor; unsupported constructs fail explicitly. The static SVG checker validates accessibility markup, not geometry or model semantics:

```bash
python3 skills/mbse-diagramming/scripts/import_view.py examples/visualization/rover-energy.mmd --format mermaid
python3 skills/mbse-diagramming/scripts/svg_check.py examples/visualization/rover-energy-accessible.svg
```

The [diagram-family coverage](skills/mbse-diagramming/references/diagram-families.md) distinguishes authoring criteria from formal notation and tested exports. The [visualization example](examples/visualization/README.md) contains Mermaid/DOT sources, a native Excalidraw scene and a reviewed SVG trade-study plot. Native Mermaid/Graphviz rendering and Excalidraw editor import/export have not been exercised here. Matplotlib and Vega-Lite are optional existing-environment branches, not dependencies. The limited plot helper and scene structural checker use only Python's stdlib:

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

Reports are written to `.local/rover-demo/`: native CLI results, LSP transcripts and the finite comparison summary. The LSP transcript contains the model text. Keep confidential project captures in an appropriate local location. See the [rover example](examples/rover/README.md), [verification record](docs/verification.md), and [evaluation method](evaluations/README.md).

## Research and scope

- [Inspiration comparison](docs/research/inspiration-comparison.md): seven sources, mechanisms, dependencies and adoption decisions.
- [Mechanism principles](docs/research/skill-collection-principles.md): skills, scripts, hooks, LSP, MCP and plugins.
- [MBSE source map](docs/research/mbse-source-map.md): OMG, INCOSE, NASA, SEBoK and implementation evidence.
- [Diagram-design review](docs/research/diagram-design-review.md): visualization gaps, adoption priorities and observed helper limitations.
- [SysML v2 views, features and requirements](docs/research/sysml-v2-features-diagrams-requirements.md): clause-linked inventory, requirements semantics, limitations and reviewed NotebookLM findings.
- [Adaptive interview techniques](docs/research/adaptive-discovery-interviews.md): open-to-specific questioning, choice bias and stakeholder elicitation.
- [Starter specifications](docs/starter-specifications.md): triggers, outputs and controls.
- [Source revisions and licenses](references/sources.json).

Study clones under `references/repos/` are ignored and inactive. To recreate one, use its recorded upstream/revision after checking context; do not refresh an existing checkout blindly. OpenSysML's study checkout is reused from the nearby standards-research workspace.

This is an independent Git repository named `mbse-skills` in the existing `mbse_skills` directory. Version 0.1.0 is an unpublished draft suitable for early community review; see the [sharing readiness record](docs/share-readiness.md) for checks and remaining limits. Apache-2.0 covers original material; [notices](NOTICE.md) explain third-party boundaries. The skills-only plugin is packaged locally. Verified client compatibility, automatic hooks, MCP integrations, additional engines and solver integration remain future work.
