# Diagram tool contracts

Consult only the branch selected for this task. Documentation reviewed 2026-10-10; live documentation can change and is not a pinned tool installation.

## Mermaid

Use [flowchart syntax](https://mermaid.js.org/syntax/flowchart.html), [sequence syntax](https://mermaid.js.org/syntax/sequenceDiagram.html) or [state syntax](https://mermaid.js.org/syntax/stateDiagram.html) according to the view. Stable IDs should be separate from quoted human labels. Reserved words, special characters and labels need the renderer's documented escaping; do not interpolate arbitrary source text into syntax unchecked.

An existing [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) can render `mmdc -i view.mmd -o view.svg`. Record the CLI/library versions from the selected installation. A Markdown host's ability to display Mermaid does not prove it supports the same syntax or exports. Keep external links, callbacks and HTML labels out unless the requested use needs them and the host permits them.

## Graphviz

The official [DOT language](https://graphviz.org/doc/info/lang.html) distinguishes directed graphs (`digraph` with `->`) from undirected ones. Label edges rather than inferring meaning from direction alone. Use quoted strings for labels and consult the documented escaping rules. Clusters group nodes visually; their meaning must be named in a legend.

With an existing installation, `dot -Tsvg view.dot -o view.svg` renders an SVG; `dot -V` reports its version. See [command syntax](https://graphviz.org/doc/info/command.html). A successful parse does not establish the source-to-view mapping.

## Optional Archify handoff

If Archify is already available and the user wants an explorable standalone HTML view, read that installation's `SKILL.md` and the selected mode schema. Convert meaning and topology into its typed candidate; preserve source evidence and exact version. Run its supported `finalize` contract and retain the artifact-bound receipt. A plain Mermaid/DOT render is not an Archify finalization.

Archify is an optional separately installed tool, not a catalog prerequisite or bundled dependency. This collection has no automatic install, update check or copied HTML runtime. An explanatory drawing is not an automatic SysML diagram export, round-trip editor or interchange implementation.

## Companion evidence convention

Record view purpose, authoritative inputs and hashes, stable node/edge-to-source mapping, status (proposed/observed/accepted with authority), aggregation and omissions, tool versions/commands, output hashes and separate structural/render/visual-review outcomes. Source hashing identifies bytes; it does not verify their truth or endorsement. Layout-only edits should preserve IDs, endpoints, labels and mapping.

## UML and PlantUML handoff

When the request requires UML notation, identify the selected diagram family and preserve its relationship semantics, multiplicities, guards and ordering. An informal component map should be labeled explanatory rather than formal UML. Use the official [UML specification page](https://www.omg.org/spec/UML) for exact language claims and [PlantUML CLI documentation](https://plantuml.com/command-line) for operations supported by the chosen local version.

If a Mermaid, UML or PlantUML skill is already available, read its entrypoint and the relevant resources for syntax/rendering instead of reimplementing its general tooling. Inspected candidates include `softaworks/agent-toolkit` Mermaid, `SpillwaveSolutions/plantuml`, and the UML skill in `openai/plugins`' build-web-data-visualization package. They have different dependencies, scopes and licensing evidence; select deliberately and keep the MBSE source/evidence contract here. The OpenAI entrypoint relies on companion package resources and should not be copied alone. No native PlantUML runtime was tested for this starter.

Preserve authoritative source and evidence when an external skill suggests deleting intermediate files. Its installation examples do not authorize global installs or dependency changes. A tool's class/sequence shapes do not by themselves establish UML or SysML semantic conformance.
