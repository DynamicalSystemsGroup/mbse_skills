# Local verification record

Verification date: 10 October 2026. This records local starter checks and bounded teaching-model observations. It does not supply stakeholder validation, accepted research results or complete SysML conformance evidence.

## Tool identities

| Artifact | Identity |
| --- | --- |
| OpenSysML CLI | Source `714c459fe5dcce1affb62fd98309b63626dfa311`; SHA-256 `8a7bdc975c4ddcb72a51bc9e8d98624bd565d47a3b0eea9d66b8ba989e347b7e` |
| OpenSysML LSP | Same isolated source; Go 1.25.11; SHA-256 `b9b1bcd9249131e8049614f62a3d636ba85984f3790c44dba2e7457545195238` |
| Toolkit CLI/LSP | 0.10.0; SHA-256 `2f03096cdd2814c7ae03390d3759027a34c42588deac1f39d0ef8c5205af7a88` |
| Toolkit library | SysML-v2-Release checkout `fb97b754f29588b8e9c7a35f370880cd15eb29e7`; exact content inventory identity retained in profile |

OpenSysML CLI was reused from the existing pinned research build. LSP was built locally from that isolated source using its private Go toolchain and cached module/build directories with `GOTOOLCHAIN=local`, `GOPROXY=off`, `CGO_ENABLED=0`, and `go build -trimpath -o PATH ./cmd/sysml-lsp`. The maintained source checkout was unchanged. No dependency installation, engine upgrade or global installation occurred.

## Model and LSP observations

Twenty case/engine combinations cover original failure, corrected design, exact reserve boundary, just below the boundary, shorter mission, larger battery, missing capacity, unresolved import, wrong physical unit and invalid syntax. Expected outcomes include calibration differences; matching them does not mean all models are valid.

The original 180000 J/2 km design violates the reserve condition. The 270000 J design holds in both engines; 250000 J holds exactly and 249999 J violates. Independent rational arithmetic gives 200000 J usage and a 250000 J boundary. Among the three listed candidate capacities, 270000 J is the minimum with observed satisfaction in both tools.

Both LSP sessions exercise initialization, valid text, invalid edit, restored text, close, shutdown and exit. Toolkit reports document versions. This OpenSysML build omits them; the edit publications are weak evidence, so each text is additionally checked in a fresh single-version session. Edit-to-publication correlation remains unproven for that session. Diagnostic smoke checks do not execute the energy condition.

The [example](../examples/rover/README.md) describes missing-value, import and dimensional differences. Toolkit uses an external library and OpenSysML uses bundled libraries, so these are bounded operational comparisons with differing contexts.

## Checks and limits

Unit tests cover verdict interpretation, malformed/empty outputs, unknown outcomes, executable identity mismatch, output bounds, missing executable, timeout and LSP framing. Skill validation checks metadata/resources and the bundled skill-creator validator is run separately. All 13 tests passed. Added regression tests reproduce descendant-held pipes, blocked LSP writes, stderr overflow and stale unversioned publications. The independent review confirmed the fixes. Final artifact hashes are recorded in the evidence receipt.

Independent baseline and skill-assisted artifact runs are assessed against the [evaluation rubric](../evaluations/README.md); these are exploratory runs, not a performance benchmark. Installation/automatic discovery in other clients, optional plugins/hooks/MCP, solver behavior, remote infrastructure and physical validation are not tested.

## Final commands and retained evidence

- `just check`: six skill metadata/resource checks, 44 local links, seven source records and all 13 unit/regression tests passed before this evidence index was added.
- The bundled skill-creator `quick_validate.py` passed for all six folders, using the existing system Python/YAML installation; no dependency was added.
- `just demo`: all 20 case/engine expectations, both diagnostic workflows and the finite candidate comparison matched.
- `scripts/rover_demo.py --output examples/rover/evidence` retained the final native streams/transcripts; their recorded helper hashes match current source bytes.
- `scripts/configure_engines.py` reproduced the existing executable/library identities into a separate local profile.
- Whitespace checks covered 55 new text artifacts. Git has no commits or remote; study clones, caches and local evaluation artifacts are ignored.

Retained evidence: [CLI captures](../examples/rover/evidence/cli.json), [LSP captures](../examples/rover/evidence/lsp.json), [comparison summary](../examples/rover/evidence/summary.json), and [artifact hashes](../examples/rover/evidence/receipt.json). The [exploratory evaluation result](../evaluations/results.md) records the baseline/assisted comparison and its limitations.

## Core/extension revision — 2026-10-10

The collection now has ten skills: seven core practices, one historical OOSEM starter adaptation and two SysML language/tool skills. The catalog checker replaces the fixed six-skill count with catalog coverage and prerequisite validation. Three new regression tests cover exact catalog membership, cycles/missing prerequisites and core independence from extensions.

`just check` passed all 16 tests and checked all ten skill folders, resources, local links and seven repository-source records. Bundled `quick_validate.py` was also run for all ten folders. The [layering review](../evaluations/layering-review.md) records authored routing/artifact review and its limitations; the [OOSEM walkthrough](../examples/rover/oosem-walkthrough.md) uses the retained original rover captures. Engine helpers and model bytes were not changed, and no new engine capture or paired agent evaluation was run for this revision. Earlier six-skill evaluation and capture hashes remain historical evidence, not checksums of the current revised skills.

## Visualization extensions and skill discovery — 2026-10-10

Added three optional visualization adapters, making thirteen skills. Archify's installed instructions/authoring/evidence/delivery references informed original conventions; no renderer implementation was copied. Searched existing Mermaid, UML/PlantUML, Excalidraw and Graphviz skills, inspected seven repository revisions and selected helpers, and retained the [discovery report](research/visualization-skill-discovery.md) and byte identities. Cached `npx --offline skills find` queried the directory with offline package resolution and no project dependency change. No third-party skill, renderer or production dependency was installed or vendored.

`just check` passed all 22 tests, including six new visualization regressions and core independence from the visualization layer. The bundled skill-creator validator passed all thirteen folders. `just visual-demo` exercised the scene checker and fresh SVG/receipt generation. The example has ten live scene elements and three plotted candidates. The SVG was rasterized with existing librsvg and visually inspected after one label-placement repair; helper-generated “visual review not run” remains separate from the author's [artifact-bound review](../examples/visualization/review.json).

The [exploratory pair](../evaluations/visualization-results.md) retained separate baseline/assisted artifacts and input identities. Both preserved the main engineering semantics and arithmetic; no clear semantic improvement was demonstrated. Parent checks passed both basic scene structures and inspected both plots. Native Mermaid/Graphviz rendering, PlantUML runtime, Excalidraw editor import/export, browser gates, Matplotlib/Vega-Lite execution and the later external-skill handoff branches were not tested. Existing engine captures and model bytes remain unchanged; no engine or physical experiment was rerun for visualization work.

## Plugin packaging change

Local distribution checks passed for version 0.1.0, marketplace root resolution and catalog coverage of 14 skills. `just check` passed all 26 unit tests; four new distribution tests exercise version drift, wrong marketplace sources and missing skill coverage. The setup skill passed skill-creator metadata validation. No Claude CLI is available, so native plugin validation, installation/discovery, setup behavior in a fresh client, and cross-client compatibility were not tested. The GitHub Actions workflow has been authored but not run on GitHub; no tag or release was created.

## Team workflow additions

The clean-project acceptance runner copies 11 starter files, confirms an unchanged starter rerun creates zero files, normalizes 40 actual retained CLI operation records, checks model hashes/exact arithmetic and complete recorded coverage for the original R-01. A temporary changed assumption is detected as stale and reverse impact includes R-01, L-01, M-01, V-01, E-01/E-02 and D-01. The configured live branch executed the 3 km model on both engines: model validation accepted, reserve condition violated. The native capture, model, manifest and derived report are retained in the team-onboarding example. This is bounded model evidence, not intended-use or physical validation.

The current verification contract preserves outcomes and operation scope, explicitly skipped operations, native pointers and hashes. Native replay rejects schema-valid fabricated outcomes. Unit cases cover historical/planned evidence not counting toward current requirement coverage, stale shared files, cycles, path escape, source tampering and initializer preservation. [Workflow evaluation](../evaluations/workflow/results.md) retains one paired behavioral run and post-run artifact checks. Diagram-family guidance now documents every family in the user-supplied table, but formal notation templates/native renders for all families are not implemented.

Codex CLI 0.162.1 discovered mbse-skills@mbse-skills-community with invocation-only local marketplace configuration. This supersedes the earlier blanket statement that no native client is available: Claude remains unavailable; native marketplace discovery passed, plugin installation/skill invocation remain untested. Hosted GitHub Actions execution, other client compatibility and automatic skill routing are not tested.

Final local checks for this change: `just check` passed 15 skill/resource checks and all 38 unit tests; skill-creator validation passed for setup/traceability entrypoints. The final portable acceptance run passed with a fresh destination. The retained changed capture replay, manifest/model identities and native marketplace manifest identities match the [artifact receipt](../examples/team-onboarding/evidence/receipt.json). Current native-client limits remain as stated above.
