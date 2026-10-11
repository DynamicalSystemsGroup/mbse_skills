---
name: mbse-constraint-reasoning
description: Explain engineering constraints and evaluate feasible design alternatives against explicit objectives, units, bounds and uncertainty.
license: Apache-2.0
---

# MBSE Constraint Reasoning

## Clarification and human review

Engineers retain responsibility for engineering decisions. Clarify unresolved units, thresholds, uncertainty bounds or the objective when they could change the result; reuse established answers. Keep dependent conclusions pending while continuing authorized drafting or investigation. Present changed engineering artifacts as proposed or awaiting review, preserving existing source and approval status. Request the responsible human's review before adopting changed obligations, design decisions or adequacy claims. Report the artifact revision, evidence scope, open questions and decision needed; record acceptance only when actually supplied by an identified authority. A passing tool check, silence or agent agreement is not human acceptance.


Make the decision problem explicit before computing a result.

1. Record decision variables, given inputs, domains, units, assumptions, constraints and the objective with its direction. Distinguish a requirement threshold from a design variable and an objective.
2. Check dimensional consistency and identify unbound values. Read [trade-study reasoning](references/trade-study.md) for feasibility, boundary and optimization distinctions.
3. Establish an independently calculated control or simple boundary result. Preserve the rationale for acceptance conditions and numerical tolerances.
4. Evaluate the stated candidate set or configured solver through supported operations. Report native satisfied, violated, undecided and unavailable outcomes distinctly. Discuss conflicting results rather than choosing the convenient one.
5. State the chosen candidate, feasibility evidence, objective comparison, sensitivity and omitted effects. An optimum in a finite candidate set is scoped to that set. Solver evidence needs domains, bounds, tolerances, termination status and the exact claim it establishes.

Deliver alternatives, assumptions, calculations and decision limitations. If several feasible candidates tie, report the tie and the additional decision criterion needed. An unknown constraint is not a false constraint or a feasible design.
