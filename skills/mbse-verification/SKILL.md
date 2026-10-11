---
name: mbse-verification
description: Plan and assess verification and validation evidence for requirements or model changes, including test-first checks, independently of engines or modeling languages.
license: Apache-2.0
---

# MBSE Verification and Validation

## Clarification and human review

Engineers retain responsibility for engineering decisions. Clarify unresolved acceptance criteria, observation scope or interpretation of inconclusive results when they could change the result; reuse established answers. Keep dependent conclusions pending while continuing authorized drafting or investigation. Present changed engineering artifacts as proposed or awaiting review, preserving existing source and approval status. Request the responsible human's review before adopting changed obligations, design decisions or adequacy claims. Report the artifact revision, evidence scope, open questions and decision needed; record acceptance only when actually supplied by an identified authority. A passing tool check, silence or agent agreement is not human acceptance.


Connect a claim to the observation that can actually establish it.

1. Name the requirement or model property, revision, conditions and acceptance criterion. Separate verification of an obligation from validation against intended stakeholder use.
2. Choose analysis, inspection, demonstration or test according to the claim. Specify inputs, expected observations, tolerances, evidence identity and known limits before running the check.
3. For test-first changes, retain a genuine failing baseline when available, make the bounded change and rerun comparable checks plus relevant boundary/negative controls. If no failure exists, state what the new check adds.
4. Preserve raw observations and configuration identities. Separate satisfied, violated, undecided, unsupported and not run. Diagnose whether an observation is about syntax, model consistency, a modeled constraint or the physical system.
5. Trace results to requirements, revisions and assumptions. State validation gaps and necessary stakeholder or physical evidence separately from computed results.

Deliver a verification matrix and a bounded conclusion for each claim. A clean model or passing software check does not establish physical adequacy. Engine operations belong in the chosen language/tool extension; this skill requires none. Read the [evidence reference](references/evidence.md) when selecting evidence or reporting uncertainty.

When the task includes requirements-to-evidence links or change impact, use the available traceability practice to record dependencies and stale evidence. The observation method and semantic claim still require engineering review.
