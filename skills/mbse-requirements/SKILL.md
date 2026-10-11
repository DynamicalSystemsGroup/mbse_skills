---
name: mbse-requirements
description: Develop or review measurable system requirements, derivation, allocation and traceability independently of a modeling language.
license: Apache-2.0
---

# MBSE Requirements

## Clarification and human review

Engineers retain responsibility for engineering decisions. Clarify unresolved requirement thresholds, operating conditions or stakeholder authority when they could change the result; reuse established answers. Keep dependent conclusions pending while continuing authorized drafting or investigation. Present changed engineering artifacts as proposed or awaiting review, preserving existing source and approval status. Request the responsible human's review before adopting changed obligations, design decisions or adequacy claims. Report the artifact revision, evidence scope, open questions and decision needed; record acceptance only when actually supplied by an identified authority. A passing tool check, silence or agent agreement is not human acceptance.


Turn needs into reviewable obligations without deciding an architecture prematurely.

1. Identify the system boundary, stakeholder need, operating scenario and source authority. Label missing stakeholder decisions as open; mark agent-created examples as proposed.
2. Assign stable IDs. State the responsible system, observable behavior, conditions, threshold, units and tolerances where applicable. Separate obligations from objectives, assumptions and design choices.
3. Review each statement for ambiguity, conflicting conditions, missing quantities, feasibility and verification approach. Explain corrections against the intended need; preserve the original source text separately.
4. Trace each requirement to its need or parent and record derivation rationale. Distinguish allocating responsibility from deriving a new obligation. Record interface responsibilities on both sides of the boundary.
5. Identify the observation and method that could establish compliance, and the scenario or stakeholder review needed to validate relevance. Record owner and decision status when available.

Deliver a requirements table, trace relationships and an issue list. Every obligation has a source or explicit proposed status and a planned verification observation. Unresolved thresholds remain open, not invented defaults. Use the [review reference](references/review.md) when examining quality or traceability.
