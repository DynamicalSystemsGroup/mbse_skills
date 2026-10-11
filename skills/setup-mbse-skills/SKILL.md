---
name: setup-mbse-skills
description: Configure project conventions for this MBSE skill collection when onboarding a team or changing its modeling, evidence or verification workflow.
license: Apache-2.0
---

# Set up MBSE skills for a project

## Clarification and human review

Engineers retain responsibility for engineering decisions. Clarify unresolved process selection, review authority or evidence conventions when they could change the result; reuse established answers. Keep dependent conclusions pending while continuing authorized drafting or investigation. Present changed engineering artifacts as proposed or awaiting review, preserving existing source and approval status. Request the responsible human's review before adopting changed obligations, design decisions or adequacy claims. Report the artifact revision, evidence scope, open questions and decision needed; record acceptance only when actually supplied by an identified authority. A passing tool check, silence or agent agreement is not human acceptance.


Read the target project's instructions, README and existing engineering conventions before writing. Treat the current checkout as the target only when the request identifies it; installation into a plugin cache is not a project configuration location.

For an explicitly requested new project, the bundled [starter](assets/project-template/README.md) supplies conventions, empty requirements/glossary and evidence locations. Run `python scripts/init_project.py /new/project` relative to the installed skill folder. It creates ordinary editable files, preserves unrelated files and rejects conflicting existing content before copying. An unchanged rerun creates nothing. For an established project, tailor its existing conventions directly instead of imposing this template. The starter is intentionally incomplete and requires project decisions.

Discover the project's system scope, stakeholder terminology, existing artifacts and desired first task. Reuse stated choices. Ask only for missing choices that materially affect setup: document location, authoritative model representation, requirement IDs and evidence storage. Record unresolved choices as unresolved rather than inventing agreement.

## Choose the engineering practice

When methodology or team practice is unresolved, begin with one broad question: “What engineering practice or methodology does your team follow today, and what would you like to keep or change?” Use an already stated choice rather than asking again. Read [practice selection](references/practice-selection.md) when presenting options or mapping a selected practice to skills.

After learning the team's context, present the available paths with their coverage limits: tailored core practices, the bounded OOSEM adaptation, or the team's existing process. Show other methodologies as unimplemented candidates, not ready-made installations. Let the user select or leave the choice open. Core practices are the suggested starting point when the team has no preference; record a selection only after the user chooses it.

Ask one main question at a time for unresolved choices. Resolve methodology separately from modeling representation and tools: choosing SysML does not choose OOSEM, and choosing OOSEM does not require SysML. If the user asks only for a precise configuration change, apply that change using the established choices without restarting the interview.

## Record and apply the choices

Create or update a short project-owned Markdown configuration at the established documentation location (default `docs/mbse-project.md`). Include:

- System boundary, stakeholders and project vocabulary, with proposed terms distinguished from agreed ones.
- Authoritative requirements/model locations, identifiers, traceability conventions and decision records.
- Selected practices: methodology/team process, source edition when relevant, selection status, tailoring, selected skill names and coverage gaps; language/tool and visualization choices remain separate. Core works without SysML. A catalog prerequisite describes workflow composition, not an installed dependency.
- Verification expectations: acceptance criteria, evidence locations, distinction between model/engine checks and stakeholder validation, and unsupported outcomes.
- Existing tool identities and executable/library paths when relevant. Otherwise record tools as unconfigured; install nothing as part of onboarding. Keep credentials and confidential captures outside shared configuration.
- One concrete next task, its inputs, expected artifacts and completion check.

Make the configuration the source of project customization. Identify relevant installed skills and unavailable prerequisites; an absent skill or engine remains unavailable until separately supplied. Preserve existing agent roles and client configuration. Optional roles can be recorded as proposed responsibilities, with their inputs, outputs and review authority, but this collection supplies no specialist agent definitions. Explain that skill UI metadata is not an executable agent. Create client-specific agent files only under a separate explicit request with a supported format and validation plan.

Preserve unrelated content and established workflows. Add a concise pointer in the project's existing agent instructions only when it helps future MBSE tasks reach this configuration. If no instruction file exists, the configuration itself is sufficient. Make local reversible edits within the requested scope; setup does not authorize remote changes, publication or stakeholder approval.

Finish by reporting files changed, the selected practice and tailoring, choices retained, unavailable capabilities, unresolved decisions and the next task. For a repeat run, reconcile the existing configuration rather than appending duplicate sections; a methodology change also identifies artifacts and reviews affected by the change. Completion means usable project conventions and an actionable first task; it does not mean engines are installed, models are verified or requirements are approved.
