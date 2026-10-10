---
name: mbse-model-tdd
description: Develop test-first checks for SysML v2 model changes, collect pinned engine and LSP evidence, and investigate differing or unavailable results.
license: MIT
---

# MBSE Model TDD

Verify an explicitly stated property, with observable failure and success where appropriate.

1. Specify inputs, the expected property, its source/rationale, and the observation that can establish it. Distinguish project acceptance criteria from standard obligations. Freeze the baseline model and engine/library identities.
2. Run the original case. Preserve the failing or unavailable result. If there is no failure, describe what the proposed test actually adds; do not manufacture a red result.
3. Make the smallest model change, rerun the same check, and run relevant prior cases and boundary controls.
4. Compare native observations only where the operations and contexts are comparable. Read [engine evidence](references/engine-evidence.md) for outcome distinctions, capture requirements and the helper interfaces.
5. For LSP, capture initialization capabilities, exact document bytes/version, diagnostic exchanges, restoration and shutdown. Establish that diagnostics correspond to the revision under discussion. For unversioned diagnostics, preserve the edit-session observations as weak evidence and corroborate each text in a fresh single-version session; report that edit correlation remains unproven.
6. Explain disagreements as investigation leads. Check versions, libraries, measurement paths, semantics and unsupported operations before naming a defect. Retain raw evidence and identify the exact claim each check supports.

For local OpenSysML/Toolkit checks, use [engine_check.py](scripts/engine_check.py) with an explicit profile and case manifest. For a valid–invalid–restored LSP exchange, use [lsp_check.py](scripts/lsp_check.py) with an explicit valid model. These helpers require matching configured binaries and libraries; they do not download engines or prove conformance.

Deliver the baseline, changed model, expected outcomes, native captures, and a bounded verification statement. Successful process exit, absent diagnostics or an empty check list cannot independently establish a requirement result.

For normalized comparison reports, read [the verification contract](references/verification-contract.md) and use `scripts/normalize_capture.py` on retained CLI captures. Preserve native output and property scope; a normalized satisfied result is still a bounded model observation.
