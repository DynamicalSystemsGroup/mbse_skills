# Contributing

Use [issues](https://github.com/DynamicalSystemsGroup/mbse_skills/issues) for reproducible bugs and scoped proposals, and [discussions](https://github.com/DynamicalSystemsGroup/mbse_skills/discussions) for questions and design exploration. Follow the [conduct policy](CODE_OF_CONDUCT.md), [governance](GOVERNANCE.md) and [security reporting guidance](SECURITY.md).

Fork the repository and open a focused pull request from a topic branch. Explain the problem, resulting behavior, evidence and limitations using the PR template. Prefer clear Conventional Commit titles; keep unrelated changes separate. Contributions are accepted under the repository's Apache-2.0 license only when you have the right to contribute the material; retain third-party notices and restrictions.

Start with a concrete recurring task or an observed agent failure. Include inputs, expected behavior, actual behavior and why existing skills do not already cover it.

Classify the skill in `skills/catalog.json` as core, methodology, language/tool or visualization and declare composition prerequisites. Core must not require extensions. Research candidates have no discoverable skill entrypoint until implemented.

Use a focused standard skill folder with discriminating metadata, concise instructions and conditionally loaded references. Define the trigger, required inputs, expected artifacts, important failure modes and completion condition. Keep source facts separate from original project conventions. Mechanical constraints belong in a reusable check when one is practical.

Before adopting a source, record its exact revision or document edition, authority, location, license/access restrictions and the claim supported. Preserve attribution and file notices for adapted material. The collection's Apache-2.0 license does not override another work's terms.

For significant changes, retain a baseline task run and a skill-assisted run with the same request, input bytes and engine identities. Evaluate the output model and evidence against the rubric, not the agent's claim that it complied. Test intended activation and an unrelated request. Report single-run evidence as exploratory; do not call it a benchmark.

Run `just check`. For engine or model changes, run the configured example and relevant negative cases. Review native streams and warnings. An expectation calibration that matches an engine's limitation is not proof that the engine is correct.

Update the README when commands, installation, compatibility or common operations change. Do not commit, push, publish or deploy without the user's explicit authorization.

For distribution changes, follow [installation and releases](docs/distribution.md). Keep the plugin thin: portable skill folders are the authoritative content. `just check` includes version/marketplace checks. Record native client compatibility separately from these structural checks.
