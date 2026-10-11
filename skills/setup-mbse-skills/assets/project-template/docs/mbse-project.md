# Project conventions

System boundary, stakeholders and intended use: open; establish these before deriving obligations.

Authoritative needs and requirements: [needs](needs.md) and [requirements](requirements.md). IDs: N-xx, R-xx, A-xx for assumptions, L-xx for logical responsibilities, D-xx for decisions, V-xx for checks, E-xx for evidence. These IDs are starter conventions, not a standards requirement.

Architecture and decisions: [architecture](architecture.md), [decisions](decisions.md). Project terminology: [glossary](glossary.md). Trace dependencies: [traceability.json](../traceability.json); source is the dependent, target is its input.

Selected practices: discovery, requirements, architecture, verification and traceability. Methodology, modeling representation and visualization: open. Engines: unconfigured. No dependency or engine installation is implied.

Practice selection: unresolved. Start by asking what process the team follows; offer tailored core practices, the bounded OOSEM adaptation or preserving an existing team process. Record the selected path, selector, source/edition when relevant, tailoring, artifact/review mapping and missing capabilities. Keep representation and tool choices separate. These initial skill names are starter suggestions, not an agreed methodology.

Agent roles and review authority: unresolved. Preserve existing client configuration; this starter supplies no specialist agents. Record proposed responsibilities separately from appointed engineering authorities.

Human review: engineers retain responsibility. Clarify material unknowns before relying on dependent conclusions. Identify the responsible reviewer for changed requirements, design decisions and adequacy claims; keep them proposed/awaiting review until actual acceptance is recorded. Review handoff: artifact/revision, proposed decision, evidence scope, open questions and requested disposition. Record reviewer, decision, scope/revision and conditions when supplied; silence or passing checks are not acceptance.

Evidence: [evidence conventions](../evidence/README.md). Keep secrets and confidential native captures outside shared/public artifacts. Verification addresses the specified property; stakeholder validation and physical adequacy need their own evidence.

Next task: identify a stakeholder need and operating scenario; propose one observable obligation with units/conditions, source/status, and a planned check. Completion: a reviewable requirement plus unresolved decisions and an identified verification method, not stakeholder approval.
