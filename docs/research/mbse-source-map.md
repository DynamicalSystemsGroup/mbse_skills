# MBSE source map for agent skills

Historical initial discovery pass. For the implemented starter and current checks, see the [repository README](../../README.md) and [verification record](../verification.md).

Discovery date: 10 October 2026. This is a first source map, not a completed standards review, skill implementation, certification scheme, or institutional endorsement. Public landing pages, repository READMEs, and selected document passages were inspected; no models or tools were executed.

## Sources and their authority

| Source | Observed status and useful material | Appropriate role in the collection |
| --- | --- | --- |
| [OMG SysML 2.0](https://www.omg.org/spec/SysML/2.0/About-SysML) | Formal version adopted September 2025. OMG separates normative language/transformation documents and machine-readable artifacts from its informative vehicle example. | Language rules, abstract/concrete syntax, semantics, libraries, and transformation claims must cite a pinned normative artifact and clause. Examples illustrate rules; they do not establish them. |
| [OMG KerML 1.0](https://www.omg.org/spec/KerML/1.0/About-KerML) | Formal version adopted September 2025. Normative artifacts include the specification, abstract-syntax XMI, semantic/data-type/function libraries, and JSON representations. | Foundational modeling vocabulary and semantics, with explicit links from SysML concepts to their KerML basis. |
| [OMG Systems Modeling API and Services 1.0](https://www.omg.org/spec/SystemsModelingAPI/About-SystemsModelingAPI) | Formal version adopted September 2025. Normative API PIM, OpenAPI/JSON artifacts, OSLC shapes and vocabularies are distinguished from the informative cookbook. | Repository/service operations, representations, and interoperability contracts; keep these separate from language authoring. |
| [INCOSE Systems Engineering Handbook](https://www.incose.org/resources-publications/technical-publications/se-handbook/) | Current landing page presents the fifth edition and describes elaboration of ISO/IEC/IEEE 15288:2023 life-cycle processes. Full handbook is offered for purchase. | Practice and process framing. The public description does not supply the handbook's detailed procedures or the ISO standard text. |
| [INCOSE Competency Framework](https://www.incose.org/resources-publications/publish-with-incose/competency-framework/) | Landing page labels a second edition and describes 37 competencies in a tailorable framework. | Coverage map for technical and professional abilities; adapt task expectations to context rather than copying human proficiency grades into agent claims. |
| [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) | Public chapters span fundamentals, NASA life cycle, system design, product realization, and technical management. | An accessible foundation for procedural examples, artifact review, and lifecycle reasoning, qualified by NASA context. |
| [SEBoK](https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_%28SEBoK%29) | Landing page identifies version 2.14, released 18 May 2026, and stewardship by INCOSE, IEEE Systems Council, and Stevens. It points to literature rather than containing all underlying knowledge. | Vocabulary, orientation, competing perspectives, and reference discovery. Follow material claims to the cited original literature or standards. |

NASA explicitly calls its handbook general guidance and a companion to implementing NPR 7123.1 and Center directives. It also calls for formality and documentation to vary with project type, size, and complexity. A NASA-derived checklist is therefore guidance unless the user's project actually adopts the relevant requirements. [NASA introduction](https://www.nasa.gov/reference/1-0-introduction/).

SEBoK acknowledges alternative approaches and differing terminology; its glossary can retain multiple definitions. A domain vocabulary skill should identify the source and project meaning of a term, preserving disagreement rather than manufacturing one universal definition. [SEBoK structure](https://sebokwiki.org/wiki/Structure_of_the_SEBoK).

## Implementation evidence and reusable examples

| First-party repository | What its maintainers describe | How to use it |
| --- | --- | --- |
| [Systems-Modeling/SysML-v2-Release](https://github.com/Systems-Modeling/SysML-v2-Release) | Incremental specification documents, example models, model library, and user installation instructions; maintained by the OMG Systems Modeling Community Reference Implementation Working Group. | Start with examples, libraries, and release identity. Pin a tag/commit before using files as fixtures. An incremental release may differ from the selected formal standard. |
| [Systems-Modeling/SysML-v2-Pilot-Implementation](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) | Pilot textual notation and visualization implementation, including Xtext projects and tests. | Inspect syntax handling and implementation behavior; execute reproducible parser/semantic tests only in a later authorized task. |
| [Systems-Modeling/SysML-v2-API-Services](https://github.com/Systems-Modeling/SysML-v2-API-Services) | Proof-of-concept pilot REST/HTTP implementation and cookbook reference. | Study API examples and implementation-specific behavior; do not assume its current README or deployed service matches the chosen normative revision. |

Proposed evidence rule: a successful parse, valid JSON schema, SHACL result, rendered diagram, or successful API request supports only the property actually checked. It does not independently establish language conformance, adequate engineering content, stakeholder validation, or certification. Retain standard revision/clause, implementation version, input, expected result, actual result, and limitations; human judgments require a named reviewer decision. This rule also follows the workspace's recorded direction (local parent-workspace document `../docs/workspace-direction.md`, outside this repository).

## Candidate task families, not committed scope

These are proposed slices to evaluate with concrete tasks before deciding the skill inventory:

1. **Domain and stakeholder discovery:** capture system boundary, mission, stakeholders, concerns, assumptions, unresolved terminology, and conflicting needs. Preserve stakeholder ownership of decisions.
2. **Requirements reasoning:** distinguish need, requirement, rationale, acceptance condition, and verification evidence; review ambiguity and traceability using the applicable source and project rules.
3. **SysML v2 authoring/review:** produce or explain small models and diagnose errors using normative clauses, library imports, and a pinned implementation.
4. **KerML foundations:** explain typing, specialization, membership, features, relationships, and semantic foundations through grounded examples; resolve precise claims against the specification.
5. **Architecture and lifecycle reasoning:** compare alternatives, record decision criteria and uncertainty, and examine interfaces and allocation using the selected engineering method.
6. **Verification, validation, and evidence:** distinguish model checking, implementation testing, engineering verification, stakeholder validation, and review approval.
7. **Research and vocabulary maintenance:** locate standards, papers, implementations, and case studies; record identity, scope, authority, versions, and contradictory evidence.

The INCOSE 2018 framework explicitly distinguishes domain knowledge and tool-specific supporting skills from broader competence. It also covers communication, ethics/professionalism, team dynamics, and facilitation. This supports keeping engineering judgment and communication in scope alongside modeling syntax. Its human competence levels are not evidence that an agent has professional competence. [2018 framework, sections on supporting skills and professional competencies](https://www.incose.org/docs/default-source/professional-development-portal/isecf.pdf).

## Paper lookup and evidence discipline

A useful first lookup is [Wheaton and Herber, *Digital requirements engineering with an INCOSE-derived SysML meta-model*, arXiv:2410.21288v2](https://arxiv.org/abs/2410.21288v2). The authors describe an INCOSE-derived SysML profile applied to two NASA JPL architecture models. The arXiv record labels it a journal preprint, last revised 4 December 2025. This is a requirements/MBSE case study; it is not evidence of SysML v2 conformance or blanket institutional approval.

Proposed lookup workflow: search source institutions, authors, publication venues, and cited references; verify bibliographic identity at the publisher or author record; distinguish preprint from published version; inspect full text before evaluating methods/results; confirm any linked code repository belongs to the paper; retain DOI/arXiv version, publication status, study context, limitations, and the exact claim supported. Search discovery and citation counts are not technical validation. Do not infer a paper's language version from the word “SysML” alone.

## Access, reuse, and unresolved issues

- **OMG:** public availability does not make specifications an unrestricted redistribution corpus. The KerML PDF's front matter includes specific use/copy conditions. Prefer original summaries, clause references, and official links; assess the exact artifact's terms before bundling its text. [KerML terms, PDF page 5](https://www.omg.org/spec/KerML/1.0/PDF).
- **INCOSE:** do not reconstruct inaccessible handbook content from search snippets. The inspected public competency PDF identifies itself as July 2018, first edition, despite the landing page advertising a second edition. Its copyright section restricts derivative/commercial reuse and separately addresses extracts and images. Obtain and inspect the intended edition and applicable permissions before adapting competency tables. [2018 framework, copyright on PDF page 3](https://www.incose.org/docs/default-source/professional-development-portal/isecf.pdf).
- **Repositories:** the three Systems-Modeling repositories display EPL-2.0 licensing. Review the actual LICENSE and individual file notices at the selected revision before copying code or examples; repository licensing does not automatically replace specification document notices. [Release](https://github.com/Systems-Modeling/SysML-v2-Release), [pilot](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation), [API services](https://github.com/Systems-Modeling/SysML-v2-API-Services).
- **SEBoK:** current content and references were verified, but redistribution terms were not successfully established in this pass. Keep links and original summaries until the applicable copyright terms are inspected.
- **Workflow clarified during this study:** Rohan selected SysML v2 model building, TDD, verification across OpenSysML, sysml-toolkit and other engines via LSP, and discussion of constraints and optimization. See the [collection principles and proposed loop](skill-collection-principles.md). Target users, intended autonomy, application domain, first model, engine revisions, chosen methods, offline needs, and access to licensed references remain undecided. ISO/IEC/IEEE standards and other domain standards need separate primary-source review before inclusion.

Recommended design hypothesis: use skills to guide source selection, engineering reasoning, and review; use scripts for deterministic extraction and checks; introduce model/research service adapters only when actual tasks require them. Keep source authority and tool behavior visible in every workflow. This hypothesis needs evaluation against the skill-framework study and concrete user tasks.
