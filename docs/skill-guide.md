# Choose a skill by task

Start with the engineering result you need. For a new project, use [the first-task walkthrough](first-task.md); for an established project, supply its existing artifacts and conventions.

Across tasks, apply [the engineering principles](engineering-principles.md): explicit assumptions, traceable obligations, inspectable evidence, clear communication and accountable decisions.

| Your task | Start with | Expected reviewable output |
| --- | --- | --- |
| Configure a project | [setup-mbse-skills](../skills/setup-mbse-skills/SKILL.md) | Project conventions, open choices and one next task |
| Clarify a need or system boundary | [mbse-discovery](../skills/mbse-discovery/SKILL.md) | Scope, stakeholders, assumptions and open questions |
| Stress-test an engineering plan | [mbse-grill-me](../skills/mbse-grill-me/SKILL.md) | An adaptive interview and reviewable brief |
| Develop or review requirements | [mbse-requirements](../skills/mbse-requirements/SKILL.md) | Requirements table, source traces and issue list |
| Develop architecture and interfaces | [mbse-architecture](../skills/mbse-architecture/SKILL.md) | Responsibilities, alternatives and interface contracts |
| Plan verification and validation | [mbse-verification](../skills/mbse-verification/SKILL.md) | Checks, evidence plan and validation gaps |
| Assess the impact of a change | [mbse-traceability](../skills/mbse-traceability/SKILL.md) | Trace relationships, stale evidence and required reviews |
| Examine budgets and constraints | [mbse-constraint-reasoning](../skills/mbse-constraint-reasoning/SKILL.md) | Assumptions, calculations and feasibility boundaries |
| Investigate a standard | [mbse-standards-research](../skills/mbse-standards-research/SKILL.md) | Artifact/clause references and interpretation limits |
| Investigate research literature | [mbse-literature-research](../skills/mbse-literature-research/SKILL.md) | Source appraisal and supported findings |
| Apply the bounded OOSEM adaptation | [mbse-oosem](../skills/mbse-oosem/SKILL.md) | A method-oriented artifact sequence with tailoring stated |
| Author or review SysML v2/KerML | [mbse-sysml-modeling](../skills/mbse-sysml-modeling/SKILL.md) | Model artifacts with language-source grounding |
| Exercise model checks with an engine | [mbse-model-tdd](../skills/mbse-model-tdd/SKILL.md) | Red/green checks and version-bound native evidence |
| Explain architecture or behavior visually | [mbse-diagramming](../skills/mbse-diagramming/SKILL.md) | A source-mapped view and fidelity/review record |
| Create an editable sketch | [mbse-excalidraw](../skills/mbse-excalidraw/SKILL.md) | A native scene with engineering source mapping |
| Plot engineering results | [mbse-engineering-plots](../skills/mbse-engineering-plots/SKILL.md) | A plot with units, assumptions and provenance |

## Skills and agents

A skill supplies a procedure, references and optional helpers to your chosen agent. This collection contains skills, not separate autonomous engineering agents. Per-skill `agents/openai.yaml` files supply UI metadata; they do not define a reviewer or orchestrator. The setup skill records project conventions, while [the catalog](../skills/catalog.json) records composition prerequisites. Neither launches agents nor installs tools.

Compose skills around a concrete task: discovery establishes the need; requirements makes obligations reviewable; verification plans observations; traceability records dependencies. Select methodology, language and visualization extensions when the task needs them.

## Core and extensions

| Layer | Skills |
| --- | --- |
| Core | [Project setup](../skills/setup-mbse-skills/SKILL.md), [Discovery](../skills/mbse-discovery/SKILL.md), [Grill me](../skills/mbse-grill-me/SKILL.md), [requirements](../skills/mbse-requirements/SKILL.md), [architecture](../skills/mbse-architecture/SKILL.md), [verification and validation](../skills/mbse-verification/SKILL.md), [traceability/change impact](../skills/mbse-traceability/SKILL.md), [constraint reasoning](../skills/mbse-constraint-reasoning/SKILL.md), [standards research](../skills/mbse-standards-research/SKILL.md), [literature research](../skills/mbse-literature-research/SKILL.md) |
| Methodology | [OOSEM starter adaptation](../skills/mbse-oosem/SKILL.md) |
| Language/tool | [SysML v2/KerML modeling](../skills/mbse-sysml-modeling/SKILL.md), [SysML engine-backed model TDD](../skills/mbse-model-tdd/SKILL.md) |
| Visualization | [Diagramming](../skills/mbse-diagramming/SKILL.md), [Excalidraw sketches](../skills/mbse-excalidraw/SKILL.md), [engineering plots](../skills/mbse-engineering-plots/SKILL.md) |

The checked [catalog](../skills/catalog.json) records layer membership and composition prerequisites. Flat skill folders preserve portable client discovery and existing helper paths; layer membership does not require nested installation folders. The catalog is metadata, not a runtime router or installer. Its `requires` entries name core practices needed for the composed workflow; read those entrypoints when applying that workflow, or explicitly identify unavailable practices. No downloads are implied.

Harmony, RUP SE, State Analysis, Vitech MBSE and OPM are **research candidates**, not implemented skills. Read [collection architecture](collection-architecture.md) for boundaries, current coverage and extension acceptance criteria.

Use `mbse-grill-me` when you want an interactive engineering interview or plan stress-test. It starts open-ended, adapts one main question at a time, and offers potential answers later when useful. There is no total question cap; it stops at a useful brief or when you pause. Precise edits and factual lookups do not need an interview. See the [technique comparison](research/adaptive-discovery-interviews.md) for sources and transfer limits.

Each folder has a standard `SKILL.md`, focused references where needed and UI metadata. Engine/LSP helpers remain bundled with the SysML model-TDD extension. Plugin packaging is available; no router, hook, MCP server or tool installation runs automatically.

The [OOSEM-oriented rover walkthrough](../examples/rover/oosem-walkthrough.md) connects a proposed need to requirements, logical responsibilities, allocation and existing SysML evidence. It is a bounded teaching example, not a complete OOSEM implementation, conformance certification or physically validated rover design.
