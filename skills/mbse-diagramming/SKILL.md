---
name: mbse-diagramming
description: Create or review source-linked engineering architecture, workflow, sequence or state diagrams in Mermaid, Graphviz or an available UML/PlantUML tool skill; preserve semantics and report actual rendering checks.
license: Apache-2.0
---

# MBSE Diagramming

## Clarification and human review

Engineers retain responsibility for engineering decisions. Clarify unresolved relationship semantics, source authority or omitted critical behavior when they could change the result; reuse established answers. Keep dependent conclusions pending while continuing authorized drafting or investigation. Present changed engineering artifacts as proposed or awaiting review, preserving existing source and approval status. Request the responsible human's review before adopting changed obligations, design decisions or adequacy claims. Report the artifact revision, evidence scope, open questions and decision needed; record acceptance only when actually supplied by an identified authority. A passing tool check, silence or agent agreement is not human acceptance.


Create an explanatory view of supplied engineering artifacts, retaining their authority and uncertainty. This extension expresses an architecture or behavior; it does not choose a methodology or establish model validity.

1. Identify the audience, question and view: components/interfaces, workflow, sequence or state transitions. Read the relevant source slice and record its file/revision or byte identity. Distinguish proposed designs from observed implementation; keep unresolved facts visible. Use the [output and fidelity contract](references/view-contract.md) to set destination size/detail and preserve a reconciliation ledger.
2. List the responsibilities and relationships needed to answer the question. Preserve direction, exchanged item, guard, ordering, ownership and boundary meaning. Keep stable artifact IDs in labels or a companion mapping. State omitted details and aggregation explicitly.
3. Choose Mermaid for compact text diagrams in docs, Graphviz DOT for graph-oriented views, or an available UML/PlantUML skill for explicitly requested notation. Reuse its selected syntax/rendering resources while retaining this engineering evidence contract. For a named SysML/UML diagram family, read [family coverage and authoring criteria](references/diagram-families.md) before selecting notation. Read [tool contracts](references/tools.md) for syntax pointers, local rendering and an optional Archify handoff. Use conservative syntax compatible with the selected renderer.
4. Author the editable source and source mapping before styling. Label each relationship by what it actually means: energy transfer, allocation, dependency, control or traceability are distinct. A drawn arrow is not a SysML relationship or proof of satisfaction.
   For imported Mermaid/Draw.io, read [import limits](references/import-contract.md) before extraction. For bottlenecks, stage gates, provenance or paired verification views, select a [semantic pattern](references/semantic-patterns.md). For sequence/state authoring, consult the [bounded examples](references/behavior-examples.md).
5. Run the available native renderer; retain exact version, command, source hash and output hash. Inspect the rendered view for readable labels, edge direction, missing topology, crossings and boundaries. If the renderer is unavailable, deliver source with rendering explicitly not run.
6. Repair layout without changing agreed relationships or evidence. If a semantic change is needed, identify and review it separately. Deliver editable source, mapping, legend/assumptions, available exports and a check record.

Completion requires every material node and relationship to have an identified source or proposed status, and each check to report passed, failed or not run with its scope. Distinguish source/topology inspection, native rendering, browser checks and visual review. These are original collection conventions inspired by Archify; this extension does not reproduce its renderer or claim its quality gates.
