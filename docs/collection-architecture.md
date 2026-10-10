# Collection architecture

## Boundaries

Core practices define the engineering questions and evidence contracts independently of representation. Methodology extensions choose and tailor an established workflow. Language/tool extensions express artifacts and execute supported operations. Visualization extensions create reviewable views of those artifacts or engineering datasets without becoming the authoritative model. A method can span categories: OPM combines methodology and language, so future packaging must state those dependencies rather than force an artificial separation.

Keep skill folders flat and self-contained for copying. `skills/catalog.json` is the authoritative membership and prerequisite record; `scripts/check_repository.py` checks coverage, known prerequisites, cycles and the rule that core cannot depend on an extension. It is not a client plugin manifest. `requires` is a composition prerequisite, not executable dependency installation. Engines and libraries are separately configured resources.

A user can apply core requirements review to a Markdown document with no language extension. An OOSEM-oriented project composes core practices and optionally SysML. SysML authoring can also support another methodology; selecting SysML does not select OOSEM.

## Current coverage

Nine core skills cover project setup, traceability/change impact, discovery, requirements, architecture/interfaces, verification and validation, constraint reasoning, standards and literature research. Risk, configuration management, lifecycle tailoring, integration, safety and specialty engineering are not yet dedicated core workflows. Model syntax checking and constraint execution are particular evidence paths, not substitutes for those practices.

The OOSEM skill is a bounded adaptation of the public historical survey with original artifact conventions. It does not reproduce the detailed tutorial or implement newer OOSEM v2 work. Its first walkthrough assesses only a rover energy-budget slice.

SysML v2/KerML modeling and `mbse-model-tdd` form the initial language/tool extension. The latter retains its existing name and bundled helpers for compatibility. Generic test-first evidence planning now lives in core `mbse-verification`; CLI/LSP mechanics live in the extension. The standards skill now appraises standards generally; specific OMG artifacts and clause pointers live in the modeling extension.

Three visualization extensions add diagramming, editable sketches and plots. They remain optional, have no mandatory renderer packages, and can hand tool mechanics to existing Mermaid/UML/Excalidraw skills. [Discovery findings](research/visualization-skill-discovery.md) record selected candidates and limits. A visualization's mapping and shape checks do not verify its underlying engineering claim. Core independence now also applies to the `visualization` catalog layer.

## Methodology candidates

| Candidate | Current status | Work needed before implementation |
| --- | --- | --- |
| Harmony | Research candidate | Authoritative edition, workflow/artifacts, access terms and a bounded example |
| RUP SE | Research candidate | Distinguish historical process descriptions from currently obtainable guidance |
| State Analysis | Research candidate | Source-specific physical-state, estimation and control-objective semantics and example |
| Vitech MBSE | Research candidate | Method edition and distinction between transferable practices and tool coupling |
| OPM | Research candidate | Method/language boundary, ISO 19450 edition and accessible source coverage |

The [2007 INCOSE survey](https://www.omg.org/sysml/MBSE_Methodology_Survey_RevA.pdf) identifies historical candidates; it is not a current recommendation or a detailed implementation guide. [NASA JPL's State Analysis description](https://www.jpl.nasa.gov/work-with-us/technology-system/mds/system-engineering/) and [ISO 19450:2024](https://www.iso.org/standard/84612.html) are useful first-party entrypoints for those candidates, not evidence of implemented skills here.

## Extension acceptance

Before calling a new extension implemented, identify a concrete task, source edition and access boundaries; document its inputs, workflow, outputs and completion criteria; distinguish method rules from our tailoring; include a reviewed end-to-end artifact and its limitations; check activation against an unrelated task; and run relevant repository checks. Empirical agent improvement needs retained baseline/assisted runs, not merely this structural checklist.

The original evaluation concerns the six-skill starter. Visualization and [workflow evaluations](../evaluations/workflow/results.md) cover later bounded tasks with retained input/skill identities; none establishes general improvement or effects of each individual skill.

## Distribution and onboarding

`setup-mbse-skills` is a core onboarding skill: it records project-owned conventions without requiring a language, engine or renderer. The single skills-only plugin wraps all portable folders through standard client discovery. Logical extensions remain optional in use; separate installable extension packages are not implemented. See [distribution](distribution.md) for installation and release boundaries.
