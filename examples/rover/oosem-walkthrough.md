# OOSEM-oriented rover energy slice

This is an authored desk walkthrough using the [OOSEM starter adaptation](../../skills/mbse-oosem/SKILL.md), not a new agent benchmark or a complete method application. IDs and traces below are original collection conventions. All needs, requirements and allocations are proposed teaching assumptions; no stakeholder approval is recorded.

## Scenario and need

`N-01`: a mission planner needs a rover to complete a 2 km traverse and retain energy for subsequent activity. The illustrative system boundary is the rover; terrain, operator and future tasks lie outside it. The current illustrative 180 kJ candidate cannot meet the proposed budget. A real as-is enterprise assessment, stakeholder interviews and validation of the reserve threshold have not been performed.

`S-01`: traverse 2000 m at a constant 1 m/s while drawing a constant 100 W, starting with full usable battery capacity. Temperature, slopes, losses, aging and other loads are excluded; those exclusions need engineering review before real use.

## Requirements, logical responsibilities and allocation

| ID | Proposed artifact | Trace |
| --- | --- | --- |
| R-01 | Under S-01, complete the 2000 m traverse with remaining usable energy at least 20% of initial usable capacity | N-01, S-01 |
| L-01 | Provide mobility over the traverse | R-01 |
| L-02 | Supply the energy needed by mobility | R-01, L-01 |
| L-03 | Estimate remaining energy for mission decisions | N-01; no estimator requirement or implementation yet |
| A-01 | Allocate energy supply to a candidate battery; assume the 100 W aggregate load covers mobility | L-01, L-02 |
| I-01 | Energy exchange from battery to aggregate load, measured in joules; simplified fixed power in watts | A-01, L-02 → L-01 |

This logical/allocated sketch is prose, not an implemented subsystem or behavior model. Battery limits, electrical interfaces, estimator error and fault behavior are unresolved. L-03 makes that gap visible; the existing arithmetic model does not implement an onboard estimator.

## Alternatives and decision

`C-01` 180000 J, `C-02` 270000 J and `C-03` 360000 J are the finite candidate set. Under S-01, duration is 2000 s and used energy is 200000 J. For capacity C, `(C - 200000) / C >= 0.2` requires C >= 250000 J.

`D-01`: propose C-02 because it is the smallest feasible capacity among the three listed candidates. This is not a global optimum, a mass/cost optimum or an accepted procurement decision. Minimum feasible analytical capacity is 250000 J; at 270000 J reserve is 7/27, approximately 25.93%.

## Representation and evidence

The [green SysML model](green.sysml) expresses the typed calculation and constraint. It does not encode this full need/requirement/allocation table as SysML requirement, satisfaction or verification-case elements.

| Claim | Method and retained observation | Scope |
| --- | --- | --- |
| E-01: baseline violates modeled R-01 condition | [CLI captures](evidence/cli.json), red case on both engines | Modeled constant-input condition |
| E-02: C-02 meets modeled condition | Same capture, green case on both engines | Constraint result, not mission validation |
| E-03: analytical threshold | Independent equation above plus boundary/below-boundary cases in the CLI capture | Stated assumptions and numerical boundary |
| E-04: choose smallest listed feasible capacity | [Finite trade-study summary](evidence/summary.json) | Listed candidates only |
| E-05: editor diagnostics for selected text | [LSP capture](evidence/lsp.json) | Language diagnostics; unversioned edit correlation limits remain |

The [capture receipt](evidence/receipt.json) identifies retained artifacts and helper hashes. These existing captures predate this walkthrough; no new architecture or physical experiment was run. See the [verification record](../../docs/verification.md) for engine and LSP limitations.

R-01 → L-01/L-02 → A-01 → C-02/D-01 → E-01/E-02/E-03 is a bounded trace argument. Need validation, realistic power characterization, interface design and physical mission testing remain open. Changes to S-01 require reassessment of the requirements, allocation and evidence.
