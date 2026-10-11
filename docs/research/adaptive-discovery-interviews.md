# Adaptive discovery interviews

Reviewed 2026-10-11. This is an original synthesis for a conversational MBSE skill, not a validated interview instrument. The user superseded the initial 6–10 question preference with open-ended questioning without a total cap. One main question at a time and purposeful stopping are our conversational design choices, not a source-established optimum.

## Techniques and adaptations

| Technique | Source guidance | Proposed adaptation and limit |
|---|---|---|
| Semi-structured interviewing | GOV.UK recommends a topic guide with starters and possible follow-ups, general questions first, neutral prompts, concrete stories, and flexibility. | Ask one broad question first; choose subsequent questions from the answer. Keep a small topic backlog instead of sending a questionnaire. |
| Five Whys | IDEO.org Design Kit follows a broad behavioral question with successive probes into motivations and assumptions. | Probe one important rationale selectively. Do not spend five turns on every topic or mistake the speaker's explanation for demonstrated root cause. |
| Questionnaire design | Pew describes wording, response-option and order effects; advises clear single-concept questions, concrete language, and reasonably complete, non-overlapping choices. Earlier choices can prime later open answers. | Elicit free context before offering options. Later options scaffold decisions; include another answer and uncertainty. Recommendations are advisory, never the recorded stakeholder answer. |
| Stakeholder expectations elicitation | NASA §4.1 covers stakeholders, intended use, needs/goals/objectives, operational scenarios, constraints, assumptions, decision authority, success measures and source traceability. | Select the unresolved engineering topics relevant to this task. Record stakeholder statements separately from assumptions and proposed requirements; preserve conflicts and absent stakeholder voices. |

Sources: [GOV.UK: Using in-depth interviews](https://www.gov.uk/service-manual/user-research/using-in-depth-interviews), [IDEO.org Design Kit: The Five Whys](https://www.designkit.org/methods/the-five-whys.html), [Pew: Writing Survey Questions](https://www.pewresearch.org/writing-survey-questions/), [NASA: Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/).

GOV.UK's interview guidance addresses human research sessions. Pew's findings concern surveys, not agent conversations. NASA's process is broader than an interview. Applying these ideas to an adaptive agent skill is our interpretation; source authority does not demonstrate the resulting skill's effectiveness.

## Comparison with the installed grilling skill

The local `/home/rohan/.agents/skills/grilling/SKILL.md` organizes decisions as a dependency tree and asks only questions whose prerequisites are settled. This is useful for avoiding premature dependent questions. It also separates discoverable facts from stakeholder decisions.

Its unbounded completion rule, whole-frontier question batches, recommendations attached to every question, and blanket confirmation gate do not fit this request. Our adaptation should prioritize consequential uncertainties, stop when sufficiently clear or when the user pauses, without requiring every branch to be exhausted, and retain unresolved items explicitly. An initial open question should not immediately receive a recommended answer. No implementation or text has been copied from the installed skill; its upstream identity and license are unverified.

## Proposed procedure

1. Review available context and state a short interview purpose. Do not ask users to repeat facts already supplied or discoverable in authorized local sources.
2. Ask one open question about the desired outcome or a concrete operating situation.
3. Reflect the answer briefly; select the next consequential unknown. Dependencies determine readiness, but do not expose the entire frontier at once.
4. After several meaningful answers, move to targeted questions with a few plausible options. Distinguish neutral elicitation from an explicitly labeled recommendation with a rationale.
5. Keep one main question in each turn and adapt follow-ups to the answer. Avoid hiding a questionnaire inside a multi-part prompt. There is no total question cap; stop when the next engineering task is sufficiently clear or the user asks to pause. Summarize unresolved items instead of pursuing exhaustive certainty.
6. Return a concise record of goal, stakeholders, scope, success criteria, constraints, decisions, assumptions, conflicts and unknowns, plus the appropriate next engineering task. Unknown is a valid outcome, not permission to invent a threshold.

This procedure is a collection design proposal. Conversation evaluation should check adaptation, burden, leading choices, purposeful stopping and the resulting engineering record before claiming effectiveness.

The collection now implements these conventions in [mbse-grill-me](../../skills/mbse-grill-me/SKILL.md).
An [exploratory scripted replay](../../evaluations/interview/results.md) checks
bounded scenarios and records its limits; it does not establish live-user
effectiveness or a preferred interview length.

## Provenance

See [interview-methods.json](../../references/interview-methods.json). Pages were inspected through the web reader; no complete retrieved-page byte hashes or source snapshots were retained. Only original short summaries and source links are included. No source code or question lists are vendored.
