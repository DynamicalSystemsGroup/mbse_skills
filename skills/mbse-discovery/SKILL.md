---
name: mbse-discovery
description: Clarify system boundaries, stakeholder needs, requirements and vocabulary before authoring or reviewing an engineering model.
license: Apache-2.0
---

# MBSE Discovery

## Clarification and human review

Engineers retain responsibility for engineering decisions. Clarify unresolved system boundary, stakeholder intent or conflicting sources of authority when they could change the result; reuse established answers. Keep dependent conclusions pending while continuing authorized drafting or investigation. Present changed engineering artifacts as proposed or awaiting review, preserving existing source and approval status. Request the responsible human's review before adopting changed obligations, design decisions or adequacy claims. Report the artifact revision, evidence scope, open questions and decision needed; record acceptance only when actually supplied by an identified authority. A passing tool check, silence or agent agreement is not human acceptance.


Turn an engineering request into a modeling brief that makes its intended use and open decisions explicit.

1. Read the existing project brief and vocabulary. Ask one broad question if the purpose or system boundary is unclear; resolve observable facts from available artifacts.
2. Record stakeholders and their concerns, system-of-interest, operating environment, lifecycle stage, interfaces, and the decisions the model should support.
3. Separate stakeholder needs, measurable engineering requirements, design choices, and modeling assumptions. Attach acceptance conditions and an owner/source to each requirement when available.
4. Resolve overloaded terms by naming the source definition and the project meaning. Preserve competing meanings until the user resolves them. Read [vocabulary](references/vocabulary.md) when these distinctions matter.
5. Deliver a concise brief with settled facts, alternatives, assumptions, and open questions. Do not turn an unresolved preference into a requirement. For a model change, name the property to check and how its result affects a decision.

A useful brief lets the next modeler identify inputs, outputs, expected properties, and decisions that still belong to stakeholders. It does not imply stakeholder approval.

When the user wants an interactive interview or a plan stress-test, compose
with `mbse-grill-me`. It adapts from open questions to specific choices without
a total question cap; ordinary artifact-based discovery need not become an
interview.
