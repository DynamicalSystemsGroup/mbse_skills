# Diagram import contract

Use [import_view.py](../scripts/import_view.py) to extract a deliberately small
structural subset into JSON before redrawing. It reads at most 1 MiB, records
source/helper hashes and preserves raw labels as inert strings. It executes no
links, callbacks or imported styles. Renderers must escape labels themselves.

Supported inputs:

- Mermaid `flowchart`/`graph` with direction, quoted rectangular node labels,
  single simple edges `-->` or `-.->` with optional `|label|`, isolated nodes,
  line comments and single-line `accTitle`/`accDescr` metadata. Metadata is
  retained, not treated as an edge. Each statement occupies its own line.
- Uncompressed Draw.io `mxGraphModel`, either directly or inside one
  `mxfile/diagram`. Vertex cells, edge endpoints/labels and parent groups are
  retained. Cell styles and geometry are not imported; raw XML is retained as
  the source authority. HTML labels remain raw strings, not executable markup.

Unsupported constructs fail the whole extraction with a diagnostic; no partial
representation is certified. This includes compressed/multi-page Draw.io,
embedded PNG/SVG, Mermaid sequence/state diagrams, subgraphs, chained edges,
HTML directives, multiline metadata and richer shapes. Use an existing native
tool for those inputs and record its version/export instead of stripping
content until this helper accepts it. This subset is not a general Mermaid
parser, a Draw.io round-trip editor or formal UML/SysML interchange.

The output representation contains nodes, edges, accessibility metadata and
provenance. Edges record source/target, label and line style; nodes record IDs,
labels and group ownership. Stable edge IDs are extraction-local and tied to
the source hash, not authoritative model relationship IDs. Compare topology
and labels before styling, and build the [fidelity ledger](view-contract.md)
for any subsequent aggregation. An extracted group is ownership information,
not automatically a subsystem or a SysML package.

Example from the repository root:

```bash
python3 skills/mbse-diagramming/scripts/import_view.py examples/visualization/rover-energy.mmd --format mermaid > .local/rover-view.json
```

The command prints JSON; choose a new output path to preserve earlier evidence.
