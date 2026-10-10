# Rover energy workflow

Original teaching example inspired by the nearby practical MBSE course. The engineering requirement is: retain at least 20% usable battery energy after a 2 km mission. The objective is: choose the smallest feasible battery from 180000, 270000 and 360000 J. The model represents the acceptance condition as a constraint; it does not yet implement a complete SysML requirement/satisfaction/verification-case structure.

Assumptions: constant speed 1 m/s, constant power 100 W, full initial charge and usable capacity. Terrain, acceleration, temperature, uncertainty and battery ageing are omitted. Physical adequacy and stakeholder validation remain separate questions.

Independent arithmetic: duration = 2000 s, used energy = 200000 J, and reserve boundary capacity = 200000 / 0.8 = 250000 J. The original 180000 J design fails. The 270000 J design leaves 7/27 (about 25.926%) reserve and is the smallest feasible listed candidate; 360000 J leaves 4/9. At 1000 m, 180000 J leaves 4/9 reserve.

Read red.sysml before green.sysml, then the boundary and negative cases. `cases.json` records expected outcomes by operation/engine. Run from the repository root:

```bash
just demo .local/engines.json
```

The demo runs ten cases per engine, then both LSP diagnostic sessions and a finite candidate comparison. Reports go to `.local/rover-demo/`. Exit zero means the declared observations matched, including the negative calibration cases; it does not mean every model was accepted or every check held.

Observed differences in the pinned tools:

- Missing capacity: OpenSysML cannot make the check; Toolkit reports undecided.
- Unresolved import: OpenSysML rejects the model. Toolkit's check reports a warning and its constraint operation returns satisfied. That result does not resolve the missing dependency.
- Energy assigned a length unit: OpenSysML rejects it during validation; Toolkit accepts the validation operation but reports undecided during the constraint operation.
- Invalid syntax: both validation operations reject it.
- Both report violation just below 250000 J and satisfaction at the exact boundary.

Toolkit uses the configured external library; OpenSysML uses bundled libraries. Diagnostic policies and library contexts differ. OpenSysML LSP diagnostics in this build omit the document version; Toolkit includes it. The helper records the unversioned edit observations and independently checks each text in fresh sessions. It does not assert server-version correlation for OpenSysML edits.

For the retained run and exact artifact identities, read [verification record](../../docs/verification.md). Native reports are retained alongside the summary in the example evidence directory after final verification. These are local example observations, not accepted research results or a general engine ranking.
