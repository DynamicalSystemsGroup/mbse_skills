# SysML v2 feature, view and requirements source review

Reviewed 2026-10-10. This note independently inspects the official document text retained locally; it does not use NotebookLM's generated answers. It is a source map for future skills, not an assertion that the current collection covers the language completely. No engines or renderers were run.

## Baseline and evidence limits

- [SysML 2.0 language](https://www.omg.org/spec/SysML/2.0/Language/PDF), OMG **formal/2026-03-02**, March 2026.
- [KerML 1.0](https://www.omg.org/spec/KerML/1.0/PDF), OMG **formal/2026-03-01**, March 2026.
- [Systems Modeling API and Services 1.0](https://www.omg.org/spec/SystemsModelingAPI/1.0/PDF), OMG **formal/2026-03-04**, March 2026.

Source clause numbers below refer to these exact artifacts. The local extracts contain NotebookLM image URLs, text wrapping and occasional spelling anomalies. They support clause navigation and semantic review; example syntax should be checked against the original artifact and official library files before adoption. The archive/member hashes are retained in `.local/notebooklm-sysml/library-extraction-manifest.json`; this review does not certify all extracted members or their engine compatibility. Standards text is not copied into this note.

SysML §6.2 distinguishes informative chapter-7 overviews from normative
abstract-syntax/notation descriptions; chapter 8 defines the metamodel and
chapter 9 the libraries. Do not classify all of chapter 7 as informative.
For requirements implementation rules, also consult §8.3.21 and §8.4.17;
verification cases use §8.3.24 and §8.4.20. A usage guide alone does not replace
the applicable syntax, well-formedness and semantics clauses.

## Confirmed standard views

SysML §9.2.20.1, Table 34, lists **eight standard view definitions**. These are supported by graphical-notation conformance; user-defined views are also permitted. They are not eight mutually exclusive kinds of engineering model.

| Standard view | Intended content | Source |
| --- | --- | --- |
| General View (`gv`) | General model elements and relationships; filtering can produce package, definition/usage, requirement, and viewpoint views | §9.2.20.2.3; §8.2.3.5 |
| Interconnection View (`iv`) | Features, nested features, connections and boundary features | §9.2.20.2.6; §8.2.3.11 |
| Action Flow View (`afv`) | Actions, parameters, flows, bindings, control nodes and structures | §9.2.20.2.1; §8.2.3.17 |
| State Transition View (`stv`) | States, entry/do/exit actions, transitions, triggers and guards | §9.2.20.2.8; §8.2.3.18 |
| Sequence View (`sv`) | Event ordering on feature lifelines, messages and successions | §9.2.20.2.7; §8.2.3.9 |
| Geometry View (`gev`) | Spatial items, frames and two/three-dimensional presentation | §9.2.20.2.4 |
| Grid View (`grv`) | Rectangular arrangement of elements and relationships, including tables and matrices | §9.2.20.2.5 |
| Browser View (`bv`) | Expandable model membership hierarchy | §9.2.20.2.2 |

§7.26.5 explains compartments and diagrams as view usages. A requirement view is explicitly an example of a filtered General View, rather than a separately listed ninth standard view. Views expose selected model content and render it; a diagram's appearance does not by itself establish model semantics.

Our interpretation for the earlier automobile table: package, requirement and definition views route primarily to General View; internal connectivity to Interconnection View; activity to Action Flow View; state machine to State Transition View; interactions to Sequence View. This is a purpose-oriented migration guide, **not a normative one-to-one mapping from v1 diagram kinds**. Use cases and constraint/analysis content need element-specific notation and appropriate filtered views. The v1 labels “block definition” and “parametric diagram” should not be presented as the complete v2 view taxonomy.

Extraction anomaly: §9.2.20.2.5's GridView description names GeometryView while discussing tabular/matrix specializations. Resolve this against the original artifact/library before copying that sentence or interpreting it as a hierarchy rule.

## Feature inventory to expand into skill references

The following is a high-level inventory, not a grammar-production audit. SysML chapter 7 provides a practical organizing spine; chapter 8 supplies concrete syntax, abstract syntax and semantics.

| Area | SysML clauses |
| --- | --- |
| Elements, relationships, dependencies, comments and documentation | §§7.2–7.4 |
| Namespaces, packages, ownership, aliases, imports and filtering | §7.5 |
| Definitions/usages, references, feature chains, variations/variants and specialization | §7.6 |
| Attributes, enumerations, occurrences and individuals | §§7.7–7.9 |
| Items, parts, ports and conjugation | §§7.10–7.12 |
| Connections, bindings, values, successions, interfaces and allocations | §§7.13–7.15 |
| Flows/messages; actions, control nodes, event acceptance, assignments and loops | §§7.16–7.17 |
| States, transitions and exhibiting state behavior | §7.18 |
| Calculations, constraints and assertions | §§7.19–7.20 |
| Requirements and concerns | §7.21 |
| Cases, analysis/trade studies, verification and use cases | §§7.22–7.25 |
| Views, viewpoints and renderings | §7.26 |
| Metadata, semantic metadata and user-defined keywords | §7.27 |

KerML chapter 7 adds the underlying root, core and kernel concepts, including types, features, relationships, expressions and metaclasses. KerML chapter 9 covers semantic/data/function libraries; chapter 10 covers interchange and JSON serialization. SysML chapter 9 covers the Systems Model Library (§9.2) and domain libraries: metadata (§9.3), analysis (§9.4), cause/effect (§9.5), requirement derivation (§9.6), geometry (§9.7), and quantities and units (§9.8). Individual package/member coverage still needs an inventory of the actual artifacts.

API §7.2 defines six service groups: projects, element navigation, project-data versioning, queries, external relationships, and project usage. §8 defines REST/HTTP and OSLC mappings. Annex A supplies conformance test cases; Annex B supplies examples/cookbook material. An API query or successful request alone is not verification of an engineering requirement.

## Requirements: independently checked semantic distinctions

| Feature | Confirmed meaning | Clause |
| --- | --- | --- |
| Definition versus usage | A reusable requirement definition is a constraint definition; a contextual requirement usage is a constraint usage defined by one requirement definition | §§7.21.1–7.21.2 |
| Text and identification | Documentation provides informal requirement text; a declared short name is considered the requirement ID | §7.21.2 |
| Subject | The entity constrained by the requirement; satisfaction must conform to its subject definition. Omitted explicit subject uses the general Anything baseline | §7.21.1 |
| Actors and stakeholders | Actors supply external roles relevant to satisfaction; stakeholders represent concern-bearing roles | §7.21.1 |
| Concerns | Specialized requirements for stakeholder concerns, which requirements may frame | §§7.21.1, 7.21.3 |
| Assumptions and required constraints | Effective logic is an implication: when all assumptions hold, all required constraints must hold | §7.21.2 |
| Decomposition | Nested composite requirements are required constraints; referenced requirements can also be required constraints | §7.21.1 |
| Satisfaction assertion | A satisfy requirement usage binds its subject to a satisfying feature and is an assert constraint usage; negated satisfaction is supported | §7.21.4 |
| Verification case | Objective identifies requirements using `verify`; result is a verdict with pass, fail, inconclusive or error | §7.24.2 |
| Verification method metadata | The library supplies inspect, analyze, demo and test method classifications | §7.24.2; §9.2.17 |
| Derivation | A domain library supplies derivation connections and semantic metadata; it is not merely an informal label | §§9.6.2–9.6.3 |
| Ordinary versus semantic metadata | Ordinary metadata describes annotated elements. SemanticMetadata specializations can impose implicit specialization through their base type | §§7.27.2–7.27.3 |

## Limitations and recommended skill guardrails

These are our engineering interpretations, separated from the source statements above.

- **False assumptions:** implication can hold when an assumption is false. Report assumption applicability separately from required-constraint evaluation; do not translate a vacuous result into operational success.
- **Satisfaction versus evidence:** a `satisfy` declaration makes an assertion. It is not retained measurement, solver execution or stakeholder acceptance evidence.
- **Text versus executable checks:** informal shall statements are valid modeling content, but an agent must identify which properties actually have evaluable constraints and inputs.
- **Derivation versus justification:** a modeled derivation connection records a relationship. Retain its engineering rationale, source identities and change impact separately.
- **Verdict versus engine status:** standard verification verdicts differ from adapter statuses such as unsupported, unavailable or not-run. Preserve native output and avoid fabricated verdict mappings.
- **View versus model:** enforce source-element mapping and a fidelity ledger for filtered/aggregated diagrams; sketches do not become normative SysML by resembling notation.
- **Libraries and metadata:** packaging in a library and applying metadata are compatible choices. Semantic metadata needs stronger review than descriptive annotations because it can alter specialization.
- **Standard versus implementation:** no claim here establishes parser, graphical renderer, solver, LSP or API implementation support. Engine versions, operations and tested constructs need their own evidence matrix.

Next references should each include usage decisions, an original worked example, common mistakes, source clauses, and separately recorded verification status. Requirements deserve the first complete path: stakeholder concern → reusable definition → contextual subject/assumptions → required constraints → derivation/allocation → satisfaction assertion → verification objective/method/verdict → traceable evidence → requirement view/table.

Remaining work: grammar-level completeness audit; clause-linked worked examples for every listed feature; independent review of extracted syntax/library identifiers; exact v1 transformation mappings; tool support evidence; and agreed requirement-quality criteria beyond language semantics.

## NotebookLM queries and review

Two fresh queries were run against a source-scoped NotebookLM notebook:
one on views/features/libraries and one
on requirements/limitations/API evidence. They were restricted to formal
SysML, KerML, API and library sources as appropriate; supporting tool pages
were excluded. Original questions, responses and citation mappings remain in
ignored `.local/notebooklm-sysml/diagrams-features-query.json` and
`.local/notebooklm-sysml/requirements-query.json`. This document's core findings
were independently checked before those answers were read.

Useful findings agree with the primary review above. Generated material is
not adopted as model or API fixtures:

- Numerous generated clause strings were replaced by `[suspicious link removed]`.
  Clause pointers in this note were recovered from the actual source text.
- The diagrams response labels the whole of chapter 7 informative, which is
  too broad under §6.2. Its v1-to-v2 mappings are interpretations, not verified
  transformation rules.
- The generated requirements example references a battery `capacity` feature
  that it never declares. Its syntax/conformance claims are untested.
- Its REST walkthrough uses `main` as a branch identifier and `REQ_BAT_01` as
  an element identifier. API §7.2.2 and §7.2.3 use UUIDs for these operations;
  a human name or requirement short ID is not interchangeable with that UUID.
- A modeled verification case is a specification of a process, not evidence
  that a test was executed. Missing inputs do not imply one universal solver
  outcome. The notebook supplies no evidence of particular commercial-tool
  capabilities.

Consequently this is a checked research inventory, not complete feature
coverage, a validated generated model or a tool-support assessment. The next
skill-writing work should begin with the requirements path and retain these
distinctions as explicit example-review criteria.
