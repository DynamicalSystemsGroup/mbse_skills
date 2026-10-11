---
name: mbse-engineering-plots
description: Visualize engineering constraints, finite trade studies, sensitivity or verification data with explicit units, uncertainty and provenance; use reproducible plots rather than decorative charts.
license: Apache-2.0
---

# MBSE Engineering Plots

Choose a figure that answers a bounded engineering question and exposes the assumptions behind the data.

1. Identify the decision, source dataset and its byte/revision identity. Separate measured, simulated, analytically derived and illustrative values. Retain missing/undecided outcomes explicitly.
2. Define axes, units, transformations, parameter bounds and acceptance boundary before drawing. Identify the feasible region, candidate set and objective separately; explain whether uncertainty is measured, modeled or absent.
3. Use the project's existing plotting tools. Read [plot tools](references/tools.md) for Matplotlib, Vega-Lite and the bundled zero-dependency finite-energy example helper. Use static standalone artifacts for exportable engineering figures; interactivity is optional for exploration.
4. Validate the data-to-plot mapping independently: sample values, unit conversions, thresholds, extrema and uncertainty bands. Preserve categorical outcomes and avoid connecting discrete candidates with a line that implies unmodeled designs are validated.
5. Generate the plot with readable labels and a legend whose meaning is also conveyed through text or shape. Inspect the actual export for clipping, scale distortion and missing data; retain native code/specification and source data.
6. Deliver the figure, reproducible command, source/tool identities and bounded conclusions. State whether only the listed alternatives were compared, which assumptions affect feasibility and which checks were not run.

The bundled [plot_energy.py](scripts/plot_energy.py) renders an SVG and an artifact receipt from the collection's finite-energy summary format. It cross-checks modeled reserve arithmetic, preserves inconclusive engine outcomes and explicitly labels the reserve threshold as supplied. It does not execute engines, solve an optimization problem or validate a physical system. Use another existing plotting tool for different datasets.

For destination sizing, accessibility, project styles and aggregation records,
use the diagramming extension's [output contract](../mbse-diagramming/references/view-contract.md).
The helper uses deterministic figure-prefixed accessibility IDs; embedding the
same figure twice requires an additional instance prefix and updated ARIA
references. A markup check does not replace inspecting the rendered figure.
