# Clean-project onboarding acceptance example

This teaching task connects a proposed need to requirements, architecture, model results and change impact. It uses the repository's actual retained rover CLI observations rather than inventing new tool output. No stakeholder accepted the scenario and no physical rover was tested.

For the methodology-aware setup interview, see [practice-selection acceptance cases](practice-selection-cases.md). The scripted runner below does not conduct that interview or evaluate agent behavior.

From the collection root, choose a fresh ignored destination:

```bash
just onboarding-demo .local/team-onboarding
```

The runner copies the portable starter, applies the [scenario](scenario.json), copies the rover model cases and native capture, normalizes results, builds a trace graph with file hashes and checks recorded requirement coverage. The created project contains editable needs/requirements/architecture/decision/glossary documents, models, evidence and traceability. The runner independently checks exact arithmetic and checks every native record's model hash against the copied model.

The report distinguishes the red 180 kJ candidate (violated), green 270 kJ (satisfied), and 250 kJ boundary. It also changes the mission from 2 km to 3 km in a separate model: the green candidate no longer meets the 20% reserve criterion under the same assumptions. The dependency graph identifies the model, verification, historical evidence and decision as requiring review when A-01 changes. It deliberately mutates a temporary copy of the original assumption file to verify that stale identities are rejected.

Without a profile this is a retained-evidence and independent-analysis acceptance test, not a new engine run. Add `--profile .local/engines.json` to the Python command to execute the changed model with already configured engines and retain fresh native/normalized evidence. The runner checks executable/library identities through the existing calibrated helper. No tool installs occur.

A repeat run rejects the populated destination to preserve it. The low-level starter copier itself is idempotent for an unchanged starter. Native plugin discovery/onboarding inside a client remains a separate manual gate because the development environment has no Claude CLI; see [distribution](../../docs/distribution.md). This test exercises portable resources and authored conventions, not a simulated claim of client support.

## Retained checks

[Native changed-model capture](evidence/changed-cli.json), [normalized report](evidence/changed-model-report.json), [changed model](evidence/changed-mission.sysml), [case manifest](evidence/changed-cases.json) and [live-run summary](evidence/onboarding-result.json) retain the configured 3 km check. Both calibrated engines accepted model validation and reported the modeled reserve condition violated. Original executable/library identities are inside the native capture; the normalized report is a derived interpretation and retains its adapter byte identity. Native commands contain capture-time local paths, not portable setup instructions.

[Codex marketplace discovery](evidence/codex-marketplace-discovery.json) records a separate native client listing through temporary local source overrides. The plugin was listed as available/uninstalled; no user configuration, plugin installation or skill invocation was changed. [Workflow evaluation](../../evaluations/workflow/results.md) tests project configuration and engineering judgments on isolated copies.

The [artifact receipt](evidence/receipt.json) binds retained outputs and current helpers and records native replay/model/manifest checks. Current helper identities can postdate the native run; a derived normalization/replay is not a fresh engine observation.
