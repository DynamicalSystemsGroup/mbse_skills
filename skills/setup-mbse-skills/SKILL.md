---
name: setup-mbse-skills
description: Configure project conventions for this MBSE skill collection when onboarding a team or changing its modeling, evidence or verification workflow.
license: MIT
---

# Set up MBSE skills for a project

Read the target project's instructions, README and existing engineering conventions before writing. Treat the current checkout as the target only when the request identifies it; installation into a plugin cache is not a project configuration location.

For an explicitly requested new project, the bundled [starter](assets/project-template/README.md) supplies conventions, empty requirements/glossary and evidence locations. Run `python scripts/init_project.py /new/project` relative to the installed skill folder. It creates ordinary editable files, preserves unrelated files and rejects conflicting existing content before copying. An unchanged rerun creates nothing. For an established project, tailor its existing conventions directly instead of imposing this template. The starter is intentionally incomplete and requires project decisions.

Discover the project's system scope, stakeholder terminology, existing artifacts and desired first task. Reuse stated choices. Ask only for missing choices that materially affect setup: document location, authoritative model representation, requirement IDs and evidence storage. Record unresolved choices as unresolved rather than inventing agreement.

Create or update a short project-owned Markdown configuration at the established documentation location (default `docs/mbse-project.md`). Include:

- System boundary, stakeholders and project vocabulary, with proposed terms distinguished from agreed ones.
- Authoritative requirements/model locations, identifiers, traceability conventions and decision records.
- Selected practices: core skills, any chosen methodology, language/tool and visualization extensions. Core works without SysML. A catalog prerequisite describes workflow composition, not an installed dependency.
- Verification expectations: acceptance criteria, evidence locations, distinction between model/engine checks and stakeholder validation, and unsupported outcomes.
- Existing tool identities and executable/library paths when relevant. Otherwise record tools as unconfigured; install nothing as part of onboarding. Keep credentials and confidential captures outside shared configuration.
- One concrete next task, its inputs, expected artifacts and completion check.

Preserve unrelated content and established workflows. Add a concise pointer in the project's existing agent instructions only when it helps future MBSE tasks reach this configuration. If no instruction file exists, the configuration itself is sufficient. Make local reversible edits within the requested scope; setup does not authorize remote changes, publication or stakeholder approval.

Finish by reporting files changed, choices retained, unresolved decisions and the next task. For a repeat run, reconcile the existing configuration rather than appending duplicate sections. Completion means usable project conventions and an actionable first task; it does not mean engines are installed, models are verified or requirements are approved.
