---
name: mbse-traceability
description: Build requirements-to-evidence traces and assess change impact across needs, assumptions, architecture, model artifacts and verification results.
license: MIT
---

# Requirements to evidence and change impact

Read the project's conventions and authoritative artifacts. Preserve stable IDs and decision status. A trace link records a stated relationship; it is not proof that the design satisfies a requirement.

1. Identify the need, measurable obligation, assumptions, architecture responsibilities, model representation and planned verification. Keep missing acceptance criteria and conflicts open. Core traceability works with prose and tables; SysML is optional.
2. Give each artifact a stable ID and identify its source/revision. Link dependents to their inputs with an explicit relationship and rationale. Distinguish derivation, allocation, realization, verification and evidence support.
3. Attach each result to its actual check, input/configuration identities and native evidence. Record the scope of the observation. An analysis under assumptions may address a modeled requirement; it does not establish stakeholder validation or physical adequacy.
4. For a change, traverse recorded dependencies back to affected requirements, decisions, models, checks and evidence. Inspect the changed meaning and propose required reviews or reruns. Treat unrecorded dependencies as a limitation. A hash change identifies stale artifact identity, not the engineering significance of the change.
5. Deliver the trace matrix/graph, coverage gaps, evidence freshness and a change-impact report. Represent every in-scope changed/new requirement in the graph or explicitly state why it is excluded. Keep historical checks and evidence tied to their original requirement/input revision rather than counting them toward current coverage. Retain prior evidence as historical; regenerate affected checks before using it for a revised claim.

For the optional JSON graph and bounded structural checker, read [the graph contract](references/graph-contract.md). Run `scripts/trace_check.py` relative to the installed skill folder, with the target project as the explicit root. The helper does not inspect requirement quality, extract model semantics, infer missing links or execute engines.
