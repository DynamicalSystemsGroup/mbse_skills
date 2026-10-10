# Skill collection principles and MBSE application

Historical initial discovery pass. For the implemented starter and current checks, see the [repository README](../../README.md) and [verification record](../verification.md).

Study date: 10 October 2026. Initial comparison of three cloned collections, with representative skills, manifests, hooks, and playbooks inspected. This is source analysis, not an exhaustive audit or behavioral evaluation. Exact revisions and clone locations are in [sources.json](../../references/sources.json). Recommendations below are our design hypotheses, not institutional requirements.

## Goal and first workflow

Rohan's goal is an MBSE collection that combines SysML v2 and KerML knowledge with engineering practices, vocabulary, and paper/repository research. His first concrete workflow is to help build a SysML v2 model, verify it using OpenSysML, sysml-toolkit and other engines through LSP, understand and discuss constraints, explore optimization, and use TDD.

The first slice should therefore connect engineering intent, a small executable/checkable model, expected outcomes, actual engine evidence, and review. The application domain, first model, acceptance criteria, and supported engine revisions remain open. This study supports the workspace's existing SysML v2 research effort; it does not authorize deployment or upstream contributions.

## What the collections teach

### Matt Pocock: composition and shared meaning

The [README](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/README.md) favors small, adaptable, composable skills. [Domain modeling](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md) actively resolves terminology and records decisions, while distinguishing that work from simply reading a glossary. [Scope](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/SCOPE.md) asks for observed failures and rejects creating a new skill where existing ones compose. [Research](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/research/SKILL.md) requires primary sources and persisted findings.

MBSE application: make “explain specialization,” “review a requirement,” and “research a language rule” focused tasks with explicit outputs. A vocabulary reference is supporting knowledge; resolving competing meanings in a model is a procedure. Preserve the distinction between the project's terminology and a term's standard-defined meaning.

Limitation: the current [plugin manifest](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/.claude-plugin/plugin.json) distributes a selected set, while the repository also contains experimental and frozen miscellaneous skills. Clone contents and installed plugin contents are not interchangeable. The miscellaneous Git guardrail skill is an illustrative hook example, not a recommendation to install that frozen skill.

### Superpowers: staged work and behavioral tests

[Writing skills](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-skills/SKILL.md) applies a baseline/failure, minimal intervention, re-test cycle to agent behavior. It distinguishes reusable procedures from session narratives and suggests automating mechanical constraints. [Verification before completion](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md) requires fresh evidence before claiming success.

The [SessionStart hook configuration](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/hooks/hooks.json) and [handler](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/hooks/session-start) demonstrate a separate role: bootstrap guidance at session lifecycle events. The workflow skills carry the procedures; the hook helps make them available. Upstream overview: [Superpowers](https://github.com/obra/superpowers).

MBSE application: test whether a skill prevents an observed mistake, such as using SysML v1 notation in a v2 task, treating missing diagnostics as proof of correctness, or inventing a standard clause. Evaluate resulting models and evidence, not an agent's statement that it followed the skill.

Tradeoff: mandatory stages can impose overhead on small tasks. Keep rigor proportional to the claim and task, while retaining evidence requirements. Software TDD does not supply stakeholder validation or a complete engineering method.

### Original pstack: structure, evidence, and routed playbooks

The original [pstack README](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/README.md) and [Poteto Mode](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/poteto-mode/SKILL.md) route tasks into playbooks and situational skills. [Model the Domain](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/principle-model-the-domain/SKILL.md) puts domain invariants into structures. [Prove It Works](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/principle-prove-it-works/SKILL.md) checks actual artifacts and favors reproducible checks. [Encode Lessons in Structure](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) moves repeated corrections into mechanisms when possible.

[Why](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/why/SKILL.md) discovers evidence sources through available MCPs. Its [epistemics reference](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/why/references/epistemics.md) separates explicit evidence, supported interpretations, inference, speculation, and unknowns. The [evaluation playbook](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/skills/poteto-mode/playbooks/eval.md) uses blinded outputs and observable behavior.

MBSE application: represent requirements, model elements, constraint assumptions, verification cases, runs, and review decisions distinctly. Turn repeated checks into scripts; retain uncertainty in source interpretation. Use capabilities discovered from tools rather than assuming all engines expose the same operations.

Tradeoff: original pstack uses Cursor-specific modes, model routing, agent APIs, and companion skills. Its [manifest](https://github.com/cursor/plugins/blob/d73344bee8cf22e53b9d5f4cf5749d38ba38c174/pstack/.cursor-plugin/plugin.json) lists skills and agents. Learn from its mechanisms; do not assume its entire workflow is portable or appropriate for engineering decisions.

## Choosing the mechanism

These components work together. The table is a proposed decision rule for our collection.

| Mechanism | Use when | MBSE example |
| --- | --- | --- |
| Skill | A recurring task needs reasoning, source selection, or ordered professional practice. | Elicit model scope; author/review a model; formulate verification cases; explain a constraint. |
| Reference | Knowledge supports several tasks without being a procedure itself. | Versioned syntax notes, concept glossary, clause index, engine capability notes. |
| Script/CLI | A specified operation can be repeated and its result checked mechanically. | Run pinned engines, preserve diagnostics, compare expected outcomes, check evidence metadata. |
| Hook | An action belongs at a known agent lifecycle event and should run without the agent choosing it. | Invoke a quick local checker after relevant edits, or check required evidence before completion. |
| LSP | An editor/client needs language-service requests and diagnostics. | Send document revisions, resolve symbols, collect diagnostics tied to the exact document version. |
| MCP | Agents need a standardized interface to tools or data across clients. | Expose model repository queries, engine operations, or a research service when a CLI is insufficient. |
| Plugin | A tested collection needs distribution with client-specific integration. | Bundle portable skills and optional adapters/hooks for a supported agent client. |
| Repository instructions | A rule applies throughout one project rather than to a selected task. | Source baseline, evidence paths, library configuration, local review and permission conventions. |

The [Agent Skills specification](https://agentskills.io/specification) supports instructions with optional scripts, references, and assets, loaded progressively. Keep task instructions concise and read deeper resources when needed. A script may sit inside a skill; it does not need to become a separate skill.

[Claude Code hooks](https://code.claude.com/docs/en/hooks) respond to lifecycle events and can return event-dependent decisions. Hook behavior is client-specific, and hooks can themselves use probabilistic handlers. Use deterministic checks where a repeatable invariant matters; enforce critical rules in the underlying tool/CI as well.

[MCP](https://modelcontextprotocol.io/docs/getting-started/intro) connects AI clients to external tools and data. It supplies access, not engineering judgment or a proof of correctness. [Cursor plugins](https://cursor.com/docs/plugins) package components for distribution. Packaging should follow tested workflows and known compatibility needs.

LSP is a distinct protocol from MCP. The inspected [OpenSysML language server documentation](https://opensysml.org/reference/lsp/) describes LSP plus tool-specific extensions, and [sysml-toolkit's README](https://github.com/Open-MBEE/sysml-toolkit/blob/main/README.md) describes a CLI and language server with syntax/semantic capabilities. These are maintainer claims; neither engine was installed or exercised in this pass. Record initialization capabilities, library configuration, supported methods, and limitations before depending on them.

## Proposed first model-building loop

1. Establish system boundary, purpose, stakeholder needs, assumptions, units, and the questions the model must answer. Capture unresolved terms and distinguish engineering requirements from implementation choices.
2. Select the normative SysML/KerML baseline, libraries, and pinned engines. Create a capability matrix for parsing, semantic diagnostics, evaluation, execution, constraint solving, and optimization. Mark unsupported and untested capabilities explicitly.
3. Write a small verification case before changing the model: inputs, expected property, source of the expectation, and how failure will be observed. Establish the failing baseline when using TDD.
4. Build the smallest model change that addresses the case. Explain notation and semantics with clause references and examples. Collect LSP results against the actual document revision; use CLI/API execution where LSP lacks the needed operation.
5. Re-run the case and relevant previous cases. Save raw engine results before normalizing comparisons. Engine disagreement is an investigation trigger, not an automatic majority verdict on the standard.
6. For constraints, state variables, domains, units, assumptions, and feasible conditions. For optimization, additionally state objective, direction, bounds, solver, tolerances, and termination criteria. A feasible result does not by itself establish optimality. Record unsupported/unknown outcomes separately from false constraints.
7. Present the model, evidence, unresolved differences, and limitations for review. Keep tool acceptance, normative interpretation, engineering verification, stakeholder validation, and reviewer approval distinguishable.

Candidate skill boundaries are intent/vocabulary discovery, standards lookup, SysML/KerML authoring, model TDD and engine comparison, constraint/trade-study reasoning, and literature/repository research. Start with one representative task; do not freeze this inventory yet. The [MBSE source map](mbse-source-map.md) identifies authority and access boundaries.

## Evaluation and next evidence

Compare baseline agent behavior with skill-assisted behavior on the same bounded cases. Include valid and invalid models, ambiguous requests, library/version mismatches, unsupported engine features, contradictory diagnostics, infeasible constraints, and claims lacking evidence. Grade source correctness, model semantics, expected outcomes, reproducibility, and honest limitations. Include tasks where the skill should stay inactive.

First milestone: one small model built with an explicit expected result, a demonstrated failing-to-passing check, reproducible engine evidence, and a clear explanation of what was verified. Before execution, identify existing local tools and read their project instructions. Before installing dependencies, follow the user's dependency approval rules.

## Checks and limitations of this pass

Three shallow clones completed and their identities, clean working trees, and license-file presence were recorded. Representative source files and primary documentation were inspected. No upstream installation scripts, hooks, engine builds, software tests, or agent behavior evaluations ran. No commits, pushes, deployments, or MBSE conformance claims were made. MIT license files are retained in the source checkouts; attribution and notices must accompany any later copied/adapted material.
