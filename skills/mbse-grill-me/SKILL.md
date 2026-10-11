---
name: mbse-grill-me
description: Interview a user adaptively to clarify or stress-test an engineering goal, plan, requirement or modeling decision; start open-ended and narrow to grounded choices. Use when asked to grill the user or work through uncertainty interactively, rather than for an already precise edit or a factual lookup.
license: MIT
---

# MBSE Grill Me

Build a shared understanding through an open-ended engineering conversation.
There is no total question cap. Ask one main question at a time so the user
can steer the discussion; depth follows the unresolved engineering decisions,
not a fixed questionnaire. Support discovery and constructive challenge without
making the user defend every answer.

## Start with the actual gap

Read the request, prior answers and available project artifacts. Resolve facts
you can inspect yourself. Identify whether the user wants their engineering
intent clarified, an existing plan challenged, or domain questions to take to
papers/experts. In the last case, ask for the missing knowledge and evidence,
not unrelated preferences about packaging or tools.

If purpose is unclear, start with a broad neutral question such as “What would
you like this system or model to help you accomplish?” Treat a compound
prompt as several questions if each part needs its own substantial answer;
prefer one coherent topic. If the purpose is already known, ask about its most
material unresolved aspect instead of restarting discovery.

## Adapt after each answer

Keep a working record of goal, context, stakeholders, boundary, operational
scenarios, constraints, tensions, risks, evidence and unknowns. Separate user
decisions from observations, tentative interpretations and proposed defaults.
Update this record when the user corrects or redirects the conversation.

Choose the next question by how much its answer changes the model or decision.
Ask prerequisite questions before dependent ones. Use [question patterns](references/question-patterns.md)
for a concrete scenario, rationale, competing requirement or missing acceptance
criterion; select only patterns relevant to this conversation. Probe a vague
claim gently rather than repeating “why” mechanically.

Start with the user's own words. As alternatives become clear, offer a few
numbered potential answers with concrete consequences, allowing free text,
unknown or deferral. Treat them as scaffolding, not an exhaustive list or an
answer on the user's behalf. Recommend an option only for an actual decision
with enough evidence, and explain the basis; factual/source questions need
evidence rather than a recommended truth. Early discovery should not be
anchored by tool, architecture or threshold defaults.

Reflect emerging themes after several meaningful answers or a change in scope.
Name contradictions neutrally and ask which obligation or assumption has
authority. If the user is overwhelmed, simplify the next question or summarize
what is known. A status request gets a status answer; it is not another
engineering question. Pause or stop immediately when requested.

## Close with usable clarity

Stop asking when the next action and material blockers are clear, or the user
asks for a summary, pause or handoff. An unbounded conversation does not require
visiting every possible branch. Deliver a concise brief: goal and boundary,
settled decisions, constraints and their authority, alternatives/tradeoffs,
proposed acceptance observations, open questions and the next useful action.
Use `mbse-discovery` for the fuller brief convention when needed.

Unknown thresholds remain unknown; recommendations, silence and offered choices
are not stakeholder decisions. Continue already-authorized work where answers
suffice, and keep work dependent on unresolved decisions pending. Interview
completion does not imply stakeholder approval or expand action authorization.
