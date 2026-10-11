# Practice selection during onboarding

Use this reference after learning the team's existing practice, or when the user asks to see methodology choices. The table describes this collection's support, not the maturity or value of the methodologies themselves.

| Path | What changes in the project | Available support |
| --- | --- | --- |
| Tailored core systems engineering practices | Compose discovery, requirements, architecture, verification and traceability around the team's task | Available, without requiring a named methodology, SysML or engines |
| OOSEM-oriented workflow | Link mission/stakeholder scenarios to black-box requirements, logical responsibilities, allocations, alternatives and evidence | Bounded historical adaptation in `mbse-oosem`; not complete OOSEM or OOSEM v2 |
| Existing team process | Preserve its artifact names, stage/review conventions and authorities; map applicable core skills to those artifacts | Available as project tailoring; method-specific coverage depends on supplied sources and actual skills |

Present these as numbered choices after the broad question. Recommend core practices only when the user has no existing preference; explain that it offers an engine-free starting point. Include keeping the methodology unresolved as a valid outcome. Preserve the user's own description if it does not fit a listed path.

ICONIX/Rosenberg-inspired development, Harmony, RUP SE, State Analysis, Vitech MBSE and OPM have no implemented methodology skill in this collection. If asked about them, explain that status and record the requested method, source/edition and coverage gap. Offer mapping existing core skills to the supplied process as limited tailoring; proceed on that path only when the user selects it. A source link or a configured method name does not establish implementation or compliance.

## Map the selection to project conventions

- **Core:** select the practices needed for the first task. A small first task might combine requirements, constraint reasoning and verification; expand only for an actual need.
- **OOSEM:** identify `mbse-oosem` and its composition prerequisites: discovery, requirements, architecture, constraint reasoning and verification. Record unavailable skills instead of fetching them. Read the installed OOSEM entrypoint and source-basis reference before method-specific tailoring.
- **Existing process:** preserve its names, sequence, review authorities and authoritative artifacts. Map each selected skill to a concrete artifact or activity; list unmatched activities as gaps. Distinguish sourced method rules from the team's tailoring.

Then establish representation, visualization and tools separately. Markdown/tables is an available first-task representation. SysML modeling and engine-backed TDD are optional extensions; the latter requires deliberately configured engines. Installation is a separate operation.

Record the following in the project's conventions, adapting to an existing format:

```text
Practice/process: <team selection or unresolved>
Selection status and authority: <who selected it; distinguish from approval>
Source/edition: <when relevant; unknown if not established>
Tailoring and artifact/review mapping: <retained conventions and changes>
Selected skills and missing prerequisites: <actual available names and gaps>
Representation and visualization: <separate choices or unresolved>
Tools and evidence: <actual configuration and storage conventions>
Agent roles: <existing roles or proposed responsibilities; no generated agents>
Human review gates: <responsible reviewers, artifacts and decisions requiring review>
Review record: <actual reviewer, artifact revision, disposition and conditions; open if absent>
First task: <inputs, expected artifacts and completion check>
```

Apply selected skills through this configuration and the project's normal agent instruction pointer. Editing shared skill procedures is unnecessary for ordinary project choices. If a user explicitly requests deeper customization, preserve portable helpers/references and record the changed procedure and its evaluation needs. On a repeat setup, retain prior selections unless the user changes them; record the effect of a process change on existing artifacts and evidence.
