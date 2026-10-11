# First task: develop a reviewable requirement

Use a small rover energy-budget scenario to try the skills with Markdown and tables. This walkthrough asks your agent to produce proposed engineering artifacts; it does not require a SysML engine. Native client invocation remains an untested compatibility gate in the collection's recorded evidence. If your client does not discover copied skills, use its documented discovery mechanism or ask it to read the installed `SKILL.md` directly.

## 1. Install in your target project

Choose a new teaching project or an existing project where local documentation edits are appropriate. From that project, with Node.js/npm available:

```bash
npx skills@1.7.0 add DynamicalSystemsGroup/mbse_skills --agent codex --skill '*' --copy
```

This installs editable skills in `.agents/skills`; it does not configure the engineering project. Review the copied files. For other clients or a plugin route, follow [distribution and onboarding](distribution.md). Keep one installation route per client to avoid duplicate discovery.

## 2. Set the project conventions

If the project's practice is unresolved, setup first asks what the team follows and offers supported choices. For this engine-free teaching task, you can choose tailored core practices. Choose the bounded OOSEM adaptation when you specifically want its scenario-to-allocation workflow, or keep your existing process. Setup records missing methodology coverage rather than claiming to supply it. Methodology selection stays separate from the Markdown/tables choice below.

Copy this prompt into your agent in the target project:

```text
Use setup-mbse-skills to configure this project for a teaching rover
energy-budget task. Read existing project instructions and preserve
existing conventions. Use Markdown and tables; keep tools unconfigured.

Use these proposed assumptions from the collection's rover example:
- Traverse distance: 2000 m.
- Constant speed: 1 m/s.
- Constant aggregate power: 100 W.
- Required remaining energy: at least 20% of initial usable capacity.
- Candidate usable battery capacities: 180, 270 and 360 kJ.

Scope the rover as the system, with terrain and operator outside it.
Record requirement IDs, assumption IDs, source/decision status and
evidence locations in the project conventions. Keep all assumptions
and choices proposed; stakeholder owner and acceptance remain open.
Identify one requirement to develop next with mbse-requirements.
```

These inputs come from [the retained teaching scenario](../examples/team-onboarding/scenario.json). They exclude variable terrain/load, temperature, losses, aging and physical mission validation.

Expected setup output: project-owned conventions, normally `docs/mbse-project.md`, with the boundary, artifact locations, selected practices, unresolved decisions and one concrete next task. An established project's locations may differ. An explicitly new project can use [the portable starter](../skills/setup-mbse-skills/assets/project-template/README.md); its empty templates become useful only after project choices are recorded.

## 3. Develop the requirement and check plan

Then ask:

```text
Use mbse-requirements, mbse-constraint-reasoning and mbse-verification
with the recorded project conventions. Develop a proposed measurable
requirement for the 2000 m traverse and 20% reserve. Retain the source
need and assumptions, show units and exact arithmetic, and compare
the three listed battery capacities.

Write a requirements table, an assumptions/decision record and a
verification plan in the agreed document locations. Trace the need,
requirement, assumptions and planned check with mbse-traceability.
Keep a planned check distinct from an executed observation. Report
what stakeholder review or physical validation remains open.
```

## 4. Review the result

The default starter uses ordinary editable files; these are expected destinations, not a promise that every client produces identical filenames:

| File | Review for |
| --- | --- |
| `docs/mbse-project.md` | Boundary, conventions, selected skills and next task |
| `docs/needs.md` | Proposed source need and unresolved stakeholder authority |
| `docs/requirements.md` | Stable ID, condition, measurable threshold, units and proposed status |
| `docs/decisions.md` | Assumptions, candidate comparison, rationale and open decisions |
| `docs/verification.md` | Planned observation, method, evidence location and scope |
| `traceability.json` or a project-owned trace table | Need-to-requirement and requirement-to-check relationships |

Use the JSON trace format only when adopting [the graph contract](../skills/mbse-traceability/references/graph-contract.md). A Markdown table is sufficient for this first task.

Independent arithmetic gives a traversal time of 2000 s and modeled consumption of 200 kJ. To retain 20%, usable capacity must be at least `200 / 0.8 = 250 kJ`. Of the three listed candidates, 270 kJ is the smallest feasible one under the proposed assumptions. This finite comparison is not a global battery optimum or a validated rover design.

Completion means the requirement is reviewable, its assumptions and source status are explicit, the arithmetic is checkable, and its verification and trace relationships are recorded. Review and reconcile agent output against these criteria; record unresolved matters rather than treating generated text as approved. Use [the engineering review questions](engineering-principles.md) to examine traceability, auditability and communication as well as the numerical result.

## Next: inspect a retained example or add SysML

To inspect complete artifacts without relying on agent invocation, use a full collection checkout and the [onboarding acceptance example](../examples/team-onboarding/README.md):

```bash
just onboarding-demo .local/first-task-review
```

Run this from the collection root with its development environment configured, and choose a fresh destination. The runner rejects a populated destination. It creates requirements, a trace graph, derived reports and change-impact evidence using retained native observations; it does not run an agent or create fresh engine results by default.

For a follow-on task, change the mission to 3 km and ask `mbse-traceability` which requirements, assumptions, decisions and evidence need review. Under the same power and speed assumptions, the modeled capacity threshold becomes 375 kJ, so none of the original candidates suffices. Historical results stay attached to their original inputs.

When you want model-backed checks, select `mbse-sysml-modeling` and `mbse-model-tdd`, inspect an existing local engine profile and follow [engine setup](development.md#configure-and-run-engines). Keep modeled outcomes, native engine evidence and stakeholder decisions distinct. Browse [Awesome SysML v2 & MBSE](https://github.com/DynamicalSystemsGroup/awesome-sysmlv2-mbse) to discover tooling; installing this collection does not install those tools.
