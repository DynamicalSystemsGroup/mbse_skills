# Reviewable visualization examples

These examples explain the proposed rover teaching slice. They are authored views, not generated SysML diagrams, a complete architecture or physical validation.

- [Mermaid source](rover-energy.mmd) and [Graphviz DOT source](rover-energy.dot): same small energy-flow and analytical-input topology. Native renderers were unavailable and were not run.
- [Excalidraw scene](rover-energy.excalidraw): editable native document with ten live elements, separate text/shapes and reciprocal arrow bindings. Starter structural check passed; editor import/export and sketch visual review were not run.
- [SVG plot](rover-energy.svg) and [plot receipt](rover-energy.receipt.json): exact finite-energy summary, capacity in kJ, reserve in percent and the supplied 20% threshold. Generated without extra Python dependencies and rasterized with the existing librsvg tool for visual inspection. Labels and legend were inspected after one label-placement repair.
- [Source mapping](source-map.json) and [review record](review.json): input/artifact identities, meanings, proposed status and actual checks.

The plot source is the retained [rover summary](../rover/evidence/summary.json), and the explanatory artifact source is the [OOSEM walkthrough](../rover/oosem-walkthrough.md). The smallest feasible listed capacity is 270 kJ; the analytical minimum under the assumptions is 250 kJ. Negative reserve is a budget deficit rather than measured negative battery energy. The plot does not assert an uncertainty band or untested intermediate candidate.

The later [accessible SVG](rover-energy-accessible.svg) and its
[generation receipt](rover-energy-accessible.receipt.json) use figure-prefixed
accessibility IDs. The original SVG/review are preserved as historical evidence.
The [extension check record](extension-checks.json) records actual static checks,
Mermaid extraction and rasterized plot inspection. The [imported view](rover-view.json)
preserves four nodes, three edges and accessibility metadata; its
[fidelity ledger](rover-view-ledger.json) reconciles that selected diagram slice,
not the complete rover architecture. Sequence/state examples in the skill
remain unrendered, and geometry checking remains manual.

From the repository root, `just visual-demo .local/visualization-demo/energy.svg` runs the scene check and generates a fresh plot/receipt. Choose another output path for a repeat. Mermaid `mmdc`, Graphviz `dot`, an Excalidraw editor, Matplotlib and Vega-Lite remain optional and separately configured. Existing tools/skills can be used via the extension references; no packages or global skills were installed.
