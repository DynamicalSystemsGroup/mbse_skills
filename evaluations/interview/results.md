# Adaptive interview exploratory replay

Run 2026-10-11. A fresh baseline agent received the [raw request](request.json)
without skills. A separate fresh agent received the same bytes and
`mbse-grill-me` plus its question-pattern reference. Each produced a seven-turn
scripted replay and an unrelated spelling correction. No real user questions,
external operations, model executions or client installations occurred.
The [inventory](artifact-inventory.json) binds inputs, outputs and skill bytes.

Reviewed the actual [baseline](baseline.json) and [assisted](assisted.json)
responses, not just agent completion messages:

| Observation | Baseline | Assisted |
| --- | --- | --- |
| Undefined reserve | Preserves missing threshold; initial prompt asks about acceptance and purpose of reserve | Preserves missing threshold; initial prompt asks for an operating scenario |
| Conflict in supplied numbers | Computes 300 kJ demand versus 270 kJ capacity | Same correct calculation; asks who can resolve the conflict |
| Stakeholder authority | Preserves mission-lead ownership and does not invent a threshold | Same; asks whether constraints can be revised or must be reported as fixed |
| Later 20% criterion | Computes 216 kJ spend limit and 375 kJ required capacity; no unauthorized relaxation | Same; closes this slice with an infeasibility finding without another approval gate |
| User redirects to source knowledge | Switches to source passages rather than packaging choices | Same; later asks about missing derivation rules and accepts not-found |
| Pause | Summarizes facts and unknowns without further questioning | Same |
| Unrelated spelling edit | Correct sentence, no interview | Same |

Both succeeded on the main evidence/authority distinctions. The assisted
response demonstrates scenario-first pacing, a contextual later choice and
purposeful stopping in this fixture. That is not evidence of general superiority.

All future user turns were visible in a single fixture, although agents were
instructed to use only the accumulated context. This is weaker than an isolated
live interview and cannot exclude lookahead. The baseline's first response
names a mission lead before that role is supplied; that is an unsupported
role inference in that response, not proof of an underlying general defect.
No long interview, live user burden, response-option bias, repeated trials,
automatic skill selection or no-cap continuation was tested. A total question
cap is absent from the authored skill; this is an instruction property, not an
observed long-dialogue result. Results are one exploratory pair.
