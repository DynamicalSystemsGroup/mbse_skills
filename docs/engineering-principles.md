# Engineering principles and review questions

This collection is guided by the discipline of mission-critical systems engineering. Its purpose is to help people produce inspectable engineering artifacts: explicit obligations, traceable decisions, reproducible observations and communication that supports review. These are design goals for the workflows, not a claim that the collection or a resulting system has achieved a reliability target or safety qualification.

## Reliability and assurance

State the system boundary, operating conditions, measurable obligations and assumptions before interpreting a result. Examine boundary conditions, conflicting constraints and the consequences of unsupported checks. Preserve failed, inconclusive and unavailable observations with their actual meanings.

Review questions: What obligation was checked? Under which conditions? Which failure cases were considered? What uncertainty or untested behavior could change the decision?

Start with [requirements](../skills/mbse-requirements/SKILL.md), [constraint reasoning](../skills/mbse-constraint-reasoning/SKILL.md) and [verification](../skills/mbse-verification/SKILL.md). Reliability analysis, hazard analysis, fault tolerance and safety assurance require additional project-specific methods and evidence; dedicated workflows for them are not implemented here.

## Traceability and change control

Give needs, requirements, assumptions, responsibilities, checks and decisions stable identities. Record the meaning and source of each relationship. On a change, identify affected artifacts and reviews, and retain historical evidence against its original inputs. File hashes help detect stale identities; engineering review determines the significance of a change.

Review questions: Where did this obligation come from? What realizes it? Which check addresses it? What must be reconsidered when an assumption changes? Which dependencies are missing from the recorded graph?

Use [traceability](../skills/mbse-traceability/SKILL.md) and the optional [graph contract](../skills/mbse-traceability/references/graph-contract.md). A connected graph alone does not establish satisfaction or complete coverage.

## Auditability and reproducibility

Keep source statements, interpretations, native observations and engineering decisions distinguishable. Retain the inputs, artifact revisions, commands, tool identities and scope needed to inspect an observation. Record who made a decision when that authority is known; leave unresolved authority visible. Protect confidential evidence using the project's storage and access conventions.

Review questions: Can someone find the original observation and its inputs? Can they identify the exact tool and model? Is the reported outcome a native result or a derived interpretation? What changed since the observation?

Use [standards research](../skills/mbse-standards-research/SKILL.md), [verification](../skills/mbse-verification/SKILL.md) and, for configured SysML checks, [model TDD](../skills/mbse-model-tdd/SKILL.md). The [verification record](verification.md) shows bounded engine observations and their limits.

## Clear engineering communication

Communicate the claim, its basis and its limits in terms the intended reviewer can assess. Show units, interfaces, system boundaries and assumptions. Bind diagrams and plots to their sources; record any simplifications or omitted behavior. State open questions and needed decisions alongside the result.

Review questions: Who needs to understand or act on this artifact? Can they distinguish proposed choices from agreed ones? Does the view preserve the relevant semantics? Are the uncertainty and next decision clear?

Use [architecture](../skills/mbse-architecture/SKILL.md), [diagramming](../skills/mbse-diagramming/SKILL.md) and [engineering plots](../skills/mbse-engineering-plots/SKILL.md). Presentation quality and diagram structure checks do not establish engineering correctness.

## Verification, validation and human accountability

Identify how evidence addresses a stated obligation and separately how intended use will be assessed. Record decisions and acceptance through the project's actual engineering authorities. An agent can draft, calculate, inspect and assemble evidence; generated artifacts remain proposed until the applicable review is recorded.

Review questions: Is this language validation, a modeled engineering check, an implementation test or intended-use validation? What decision can the available evidence support? Who is responsible for that decision, and has it actually been made?

The [first-task walkthrough](first-task.md) deliberately separates proposed requirements, arithmetic, planned observations, retained engine results and stakeholder acceptance. The [collection architecture](collection-architecture.md) records uncovered practices; the [evaluation method](../evaluations/README.md) explains the limited scope of observed skill evaluations.
