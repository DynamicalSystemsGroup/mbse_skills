---
name: mbse-sysml-modeling
description: Author, explain or revise SysML v2 textual models with relevant KerML foundations, typed quantities and explicit engine portability limits.
license: MIT
---

# SysML v2 Modeling

Build the smallest model that answers the user's engineering question.

1. Establish purpose, boundary, requirements, assumptions and vocabulary from the supplied brief. Clarify unresolved choices that change model meaning.
2. Pin the SysML/KerML baseline and library configuration. Read [modeling foundations](references/foundations.md) for concept distinctions, source pointers and a small typed example. Treat engine documentation as engine-specific guidance.
3. Choose declarations and relationships that express the intended semantics. Explain definition versus usage, feature typing, specialization/redefinition and namespace/import decisions when they affect this model. Use typed quantities and explicit units for physical properties.
4. Before changing behavior, state the expected property and retain the original model. Establish a failing check for a requested fix where the tool supports it.
5. Run language diagnostics against the actual model revision, then the relevant constraint or execution check. Capture the operation and library configuration. Keep unsupported observations and non-normative extensions visible.
6. Explain the change in engineering terms, with source-linked language claims and evidence limits. Inspect the resulting textual model directly; a rendered diagram alone does not establish its semantics.

Deliver model files, a brief rationale, test inputs/results, and unresolved limitations. LSP diagnostics, constraint satisfaction, engineering verification, and stakeholder validation answer different questions.

For exact OMG artifacts and clause navigation, read [language source selection](references/source-selection.md). General standards appraisal is a core practice; these pointers are specific to this extension.
