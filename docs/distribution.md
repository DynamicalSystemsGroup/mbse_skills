# Distribution and project onboarding

The repository is both a portable skill library and a skills-only plugin. The plugin uses the default `skills/` directory; `.claude-plugin/plugin.json` adds identity/version metadata and `marketplace.json` points to the repository root. The catalog supplies logical layers and workflow prerequisites, not plugin dependencies. One plugin currently includes all layers; installing it does not require SysML engines or renderers.

## Local Claude Code use

From your target engineering project, load a reviewed checkout:

```bash
claude --plugin-dir /absolute/path/to/mbse_skills
```

Alternatively, add the checkout as a local marketplace and install the plugin:

```text
/plugin marketplace add /absolute/path/to/mbse_skills
/plugin install mbse-skills@mbse-skills-community
```

Then invoke `/mbse-skills:setup-mbse-skills` in the target project. It creates project-owned conventions, preserves existing workflows and identifies a first task. Re-run it when conventions change. Choose either plugin installation or copied skills for a given client, to avoid duplicate discovery.

These commands follow [Claude Code's plugin reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces). The Claude CLI is unavailable in the development environment: native manifest validation, installation and discovery are not yet tested. Before claiming client support, run `claude plugin validate /absolute/path/to/mbse_skills` and verify setup skill invocation in an isolated project.

## Editable skills with npx

From the engineering project where you want the skills, run:

```bash
npx skills@1.7.0 add DynamicalSystemsGroup/mbse_skills --list
npx skills@1.7.0 add DynamicalSystemsGroup/mbse_skills --agent codex --skill '*' --copy
```

The second command installs all 16 skills into project-local `.agents/skills` for the Codex target. Omit `--agent codex` to choose a client interactively; other targets have not been tested here. Omit `--skill '*'` to choose individual skills, including `setup-mbse-skills` and the selected workflow's catalog prerequisites. The installer does not interpret `skills/catalog.json` or resolve those prerequisites for you. Choose copied skills or a plugin for a given client to avoid duplicate discovery.

This uses Vercel's [Skills installer](https://github.com/vercel-labs/skills), not an npm package published by this project. Node.js/npm are needed for installation; no repository clone or Python environment is required. There is no packaged `uvx` installer for this collection; uv is for our Python helpers and repository checks. Version 1.7.0 is the tested installer. The newer 1.7.2 was rejected by the development machine's npm release-age policy; that policy was preserved. Unpinned `npx skills@latest` behavior has not been tested.

The [installation receipt](../examples/team-onboarding/evidence/npx-skills-installation.json) records successful discovery and copying from public GitHub, plus a fresh local-source copy test with the bundled Apache license/notices. Remote installation matched 73 source files; the local packaging test matched 105. The new license/notice files reach GitHub when these additions are pushed. Installation/file integrity is verified; native client loading and invocation remain untested. A full repository checkout is still needed for collection-level examples and checks.

After installation, ask the agent to use `setup-mbse-skills` in your project. `--copy` creates editable project files; review local changes before replacing them during an update. Each folder carries its helpers, references, license and notice.

## Other clients and manual copies

Copy selected complete skill folders into the client's documented project-local skills directory. Include `setup-mbse-skills` and any catalog prerequisites needed by your chosen workflow. Helpers and references travel with each folder. Invoke the setup entrypoint using that client's supported syntax, or ask the agent to read it directly.

Matt Pocock's packaging is inspiration, not evidence of compatibility with our plugin. Codex CLI 0.162.1 successfully listed this marketplace/plugin using invocation-only local source overrides; the retained [discovery record](../examples/team-onboarding/evidence/codex-marketplace-discovery.json) identifies the manifests and command. This establishes native marketplace discovery, not installation or skill invocation. Codex, Copilot, Gemini and other clients require separate installation/invocation checks; broad cross-client plugin support is not claimed. The local source override fields follow [official OpenAI configuration documentation](https://developers.openai.com/codex/config-reference).

## Public hosting and releases

The confirmed host is [DynamicalSystemsGroup/mbse_skills](https://github.com/DynamicalSystemsGroup/mbse_skills). It is an independent collection; hosting does not imply OpenMBEE organizational endorsement. The manifest links to this repository. The repository contents are published on `main`; the GitHub marketplace source is `DynamicalSystemsGroup/mbse_skills`; installation from that source remains untested.

`pyproject.toml` is the authoritative version. For a release:

1. Review licenses/notices, source provenance and examples for confidential material. Keep ignored research clones, local profiles, binaries and evaluation scratch output out of publication.
2. Add the release notes to `CHANGELOG.md`, update the project version and regenerate the uv lock with uv when necessary. Run `just sync-version` to update the plugin version.
3. Run `just check`, native client validation and a clean-project onboarding smoke test. Record client versions, discovered skills and skipped checks. Re-run affected model/visual checks only where relevant.
4. Review and commit explicit paths under the team's Git policy. When publication and tagging are authorized, use `v<major>.<minor>.<patch>` matching the project version. CI checks tag/version consistency; it does not create a release or publish anything.

The dependency-free Python CI runs repository/distribution checks, unit tests and a fresh retained-evidence onboarding acceptance run on pushes and pull requests. It does not install engines, exercise native clients, prove standards conformance or evaluate agent behavior. Changesets is intentionally omitted: this collection has one versioned distribution and no npm package; a changelog and version-sync command cover the present need.

Contributions follow [CONTRIBUTING.md](../CONTRIBUTING.md). Report privately any sensitive findings to the maintainers through [GitHub private vulnerability reporting](../SECURITY.md) rather than including secrets in public issues. There is no established security response service or support SLA.
