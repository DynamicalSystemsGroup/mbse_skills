# Model verification report contract, version 1

This original interchange convention sits above engine-specific native output. Preserve native output as the evidence of record. Normalizing a result does not establish standards conformance, physical adequacy or stakeholder acceptance.

Every report has `schema_version: 1`, `source` (project-relative native capture path and exact SHA-256), `adapter_sha256`, and `records`. Each record has a unique `id`, engine name and executable hash, case ID, model hash, `operation`, `outcome`, `measurement`, nonempty `reason`, `native_pointer`, `subject_scope`, `diagnostics_pointer`, and configuration hashes (`profile_sha256`, `manifest_sha256`, `library_sha256`). The capture retains commands, timestamps, versions and stdout/stderr; the report points to them rather than replacing them.

| Dimension | Values and meaning |
| --- | --- |
| Operation | `validate`: the configured model validation policy; `verify`: a modeled condition check |
| Validation outcome | `accepted`, `rejected`, `unsupported`, `unavailable`, `not_run` |
| Verification outcome | `satisfied`, `violated`, `undecided`, `unsupported`, `unavailable`, `not_run` |
| Measurement | `completed`, `timeout`, `output-limit`, `launch-failed`, `not-run` |
| Scope | `model-validation`, `named-checks` (explicit native subject list), `file-eligible-checks` (Toolkit aggregate; no fabricated subject identity) |

`unsupported` requires an explicit capability statement or native unsupported-feature observation. A timeout, unknown output format, absent check or unresolved value is not automatically unsupported. `unavailable` means the capture cannot establish a result; retain the cause. `undecided` is a completed modeled check with an explicit undecided result. `not_run` records a deliberate skip and its reason. Timeouts and other interrupted measurements carry unavailable outcomes. An operation deliberately not attempted may be not_run, or unsupported with explicit capability evidence; it cannot carry accepted/satisfied/violated/undecided.

Syntax failures, unresolved references and other model diagnostics remain in native validation output. The current adapters do not reliably categorize each finding across engines, so `rejected` alone does not distinguish parsing from name resolution. Retain the diagnostic pointer and inspect the native message/code. LSP diagnostics have their separate capture contract and cannot be converted to constraint satisfaction.

The current `normalize_capture.py` converts the two calibrated CLI capture contracts from `engine_check.py`; it recomputes interpretation from native streams, rejecting a stored outcome that disagrees. It emits explicit skipped verification records after unsuccessful validation, preserving engine-specific differences. It does not run engines, validate model/engine bytes against today's machine, or invent unsupported capabilities. Different engines disagreeing means a comparison conflict to investigate, not majority-vote satisfaction. Do not compare results without equivalent property scope and assumptions.

```bash
python scripts/normalize_capture.py /project/evidence/cli.json /project/evidence/model-report.json --root /project
```

Input must lie inside the root; output must be a fresh project-relative destination inside it. The helper validates its emitted record invariants and refuses to overwrite any output. `validate_report` checks record shape only. Consumers of the two current calibrated adapters can call `verify_retained(report, project_root)` to verify the native source hash and replay the interpretation; it rejects plausible fabricated verdicts even when their schema is valid. Historical adapter hashes are retained, while replay uses the current calibrated interpretation. This replay is not a generic validator for future adapters or unsupported-feature reports. Hashes identify bytes, not correctness. For future adapters, use the same invariants and add native calibration tests before reporting supported operation semantics.
