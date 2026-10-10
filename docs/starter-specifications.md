# Starter skills and adopted patterns

These specifications turn the [inspiration comparison](research/inspiration-comparison.md) into bounded tasks. Each folder is usable through its own entrypoint; helpers needed by a skill are bundled in that folder. No plugin or global hook is needed.

| Skill | Input | Output and completion criterion | Principal failure/control |
| --- | --- | --- | --- |
| mbse-discovery | User goal, project context, existing vocabulary | Brief naming purpose, boundary, requirements, assumptions and open decisions | Ambiguity stays visible; requirement versus objective in the rover case |
| mbse-standards-research | Bounded standards question and edition | Identified authoritative artifact/clause, original interpretation and project applicability limits | Inaccessible or contradictory source; exact artifacts and clause pointers |
| mbse-sysml-modeling | Brief, model files, baseline and libraries | Revised model, semantic rationale and evidence | Typed quantities, imports, invalid syntax and source/engine distinction |
| mbse-model-tdd | Expected property, models and pinned tools | Actual red/green/control captures and bounded verdict | Empty checks, unknown values, stale diagnostics and engine disagreement |
| mbse-constraint-reasoning | Inputs, domains, constraints, candidates and objective | Feasibility comparison, scoped choice and limitations | Unit mismatch, reserve boundary, unknown constraints and finite-set optimum |
| mbse-literature-research | Research question and candidate references | Verified citation/provenance, synthesis and gaps | Unidentified paper, version confusion, unsupported institutional claims |

Adopt small composition and active vocabulary refinement from Matt Pocock; baseline/intervention testing and fresh evidence from Superpowers; structured domain distinctions, reproducible checks and explicit uncertainty from pstack; citation and uncertainty discipline from scientific skills; independent specification/evidence review from Trail of Bits. Adapt engine guidance from OpenSysML to a tool-neutral workflow. Treat CAD descriptions as conceptual inspiration because its inspected repository has no executable skill implementation.

Leave client-specific model routing, autonomous shipping, paid-service coupling, global bootstrap hooks and a duplicated evidence platform outside the starter. The [mechanism study](research/skill-collection-principles.md) explains skills, references, scripts, hooks, LSP, MCP and plugin responsibilities.

The starter's constraints are original engineering equations. Normative source pointers support language explanations, not an institutional certification of this example. First-party engine help and captures establish only operations actually exercised.

## Core/extension revision

Layer membership and composition prerequisites are recorded in the [catalog](../skills/catalog.json); see [architecture](collection-architecture.md). The original six-skill table above remains the initial task set, with standards research now generalized.

| Added skill | Input | Output and completion criterion | Principal control |
| --- | --- | --- | --- |
| mbse-requirements | Needs, scenarios and source obligations | Identified measurable requirements, derivation/allocation traces and open issues | Proposed thresholds stay distinct from approved requirements |
| mbse-architecture | Scenarios, boundary and requirements | Logical responsibilities, candidate allocations, interfaces and rationale | Logical function stays distinct from physical realization |
| mbse-verification | Requirement/property, conditions and criterion | Verification matrix, native evidence or planned observations, scoped verdict | Model checks stay distinct from physical and stakeholder validation |
| mbse-oosem | Selected method/edition, mission context and artifacts | Linked needs-to-evidence argument with tailoring and unresolved relationships | Historical adaptation stays distinct from complete OOSEM or OOSEM v2 |

## Visualization extensions

| Skill | Input | Output and completion criterion | Principal control |
| --- | --- | --- | --- |
| mbse-diagramming | Engineering artifacts, question, audience and selected notation | Editable diagram source, source mapping, available render and scoped check record | Energy/control/allocation/trace arrows retain distinct meanings; layout edits preserve topology |
| mbse-excalidraw | Existing scene or source-backed sketch brief | Native editable scene, mapped elements, basic structural check and actual editor/export status | Binding reciprocity, stable IDs, preserved user edits and no false import-validation claim |
| mbse-engineering-plots | Engineering dataset, units, assumptions and decision criterion | Reproducible figure, source/data identity and bounded interpretation | Missing/conflicting outcomes, supplied thresholds and finite-set selection remain explicit |

Existing tool skills are selected through [discovery findings](research/visualization-skill-discovery.md); no external renderer or skill is installed by activating these extensions.

## Team workflow additions

| Skill/resource | Input | Output and completion criterion | Principal control |
| --- | --- | --- | --- |
| setup-mbse-skills and bundled starter | New or established project conventions | Project-owned configuration and actionable first task | Preserve user content; unconfigured tools/undecided thresholds stay open |
| mbse-traceability | Requirements/design artifacts and explicit dependencies | Coverage gaps, artifact identities and reverse change impact | Historical evidence does not cover a revised claim; no inferred satisfaction |
| Shared vocabulary reference | Source editions and project terminology | Operational distinctions with project interpretations | No invented institutional equivalence or stakeholder agreement |
| Model report contract | Retained calibrated CLI captures | Normalized operation/outcome/scope with native identity and replay | Empty checks, unsupported operations and interrupted measurements remain distinct |

The [onboarding acceptance example](../examples/team-onboarding/README.md) and [workflow evaluation](../evaluations/workflow/results.md) supply bounded evidence for these additions.
