# Plot tools and evidence

Documentation reviewed 2026-10-10. Tool installation and dependency changes remain separate from skill activation.

## Matplotlib

Use an existing project environment for publication/export-oriented figures. The [official quick start](https://matplotlib.org/stable/users/explain/quick_start.html) explains Figure/Axes and plotting; [savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html) describes exports. Retain the plotting code, data, library version, units and transformations. Choose the actual export format and inspect it; a notebook display is not a check of the saved figure.

## Vega-Lite

Use the official [view specification](https://vega.github.io/vega-lite/docs/spec.html) for a declarative view when an existing compatible renderer is available. Record its `$schema` version and runtime identity. Bundle data for portable captures; remote data and a CDN runtime make a view network-dependent. This skill installs or embeds no runtime and does not claim offline interactivity.

## Bundled finite-energy SVG helper

`python /path/to/plot_energy.py summary.json output.svg --reserve 0.2`

Input follows the rover summary contract: `reference.used_energy_joules`, 1–32 `candidates` with unique `case` (at most 40 characters), positive integer `capacity_joules`, exact rational `remaining_fraction`, and nonempty `engine_verdicts`. Each fraction must match `(capacity - used_energy) / capacity`. The helper checks that a supplied `selected_capacity_joules` is the unique smallest feasible listed candidate with all engine verdicts `holds`. It accepts inconclusive engine outcomes as uncertain evidence and preserves definitive disagreement with arithmetic as `conflict`, rather than marking either as success. The reserve threshold is an explicit caller input, not independently recovered from model source.

SVG output uses capacity in kJ and remaining energy in percent, includes negative analytical values when present, shows the supplied threshold and uses both labels and shapes for verdicts. No uncertainty band is drawn without uncertainty data. A receipt records input/output/helper SHA-256, exact plotted values, reserve and Python version. Existing output or receipt paths are preserved; choose new paths for revised artifacts.

This helper is a limited energy-budget plotter using Python's stdlib, not a general plotting package. For a depleted battery the negative reserve is an idealized budget deficit, not a physical negative energy measurement. Plot arithmetic checks do not validate the source data or engine semantics.
