# Security policy

This is an early-stage collection of agent instructions and local helpers. No supported-release matrix or security response SLA is established. Reports against the current default branch are welcome; do not assume historical versions receive fixes.

## Report privately

Use [GitHub private vulnerability reporting](https://github.com/DynamicalSystemsGroup/mbse_skills/security/advisories/new). Include the affected revision, a minimal reproduction with synthetic inputs, observed impact and any proposed mitigation. Do not include credentials, confidential models or real customer data. If the form is unavailable, seek a private maintainer contact before disclosing sensitive details publicly.

Relevant findings include unexpected command execution, path traversal, overwriting project files, unsafe imports, credential exposure and instructions that cause unauthorized actions. Report ordinary bugs through an issue with sanitized evidence.

Maintainers will assess reports and coordinate remediation and disclosure as capacity permits. Reporters should allow that coordination before public disclosure; no fixed response or remediation deadline is promised.

## Use safely

Review skills and helpers before allowing an agent to use them. Run external engines only after inspecting their configuration; keep private captures and credentials outside Git. The collection's checks do not certify a model, an engine or an agent's behavior.
