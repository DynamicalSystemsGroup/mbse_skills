# Shared engineering vocabulary

These are original working distinctions for the collection, not quotations or universal institutional definitions. Retain an adopted standard's own definition and edition beside the project meaning when they differ. A shared word does not imply shared scope.

| Term | Working meaning | Common confusion to resolve |
| --- | --- | --- |
| Stakeholder need | Desired outcome in an identified stakeholder context | A proposed need is not stakeholder agreement |
| Requirement | Stated obligation with source, responsible system, conditions and acceptance criterion | A design preference or unresolved threshold is not an agreed obligation |
| Constraint | Restriction on allowable values or behavior | A model predicate may encode a requirement, assumption or design restriction |
| Objective | Criterion for comparing alternatives | An optimization objective is not a mandatory threshold |
| Assumption | Condition accepted for a particular analysis, with consequences if false | A computed answer does not establish that its assumptions hold |
| System boundary | Chosen scope separating the system of interest from its environment | Organizational responsibility and physical enclosure may differ |
| Logical responsibility | Behavior or capability the system must provide, before selecting realization | A physical component name alone does not specify required behavior |
| Allocation | Assignment of responsibility or resource budget to a realization | Allocation does not prove satisfaction or derive every lower-level requirement |
| Interface | Defined exchange between endpoints, with semantics and conditions | A drawn arrow alone leaves ownership and compatibility unresolved |
| Derivation | Reasoned development of an obligation from parent needs/requirements | Copying text or allocating it is not derivation rationale |
| Realization | Proposed or selected implementation of a logical responsibility | Naming an implementation does not establish its adequacy |
| Satisfaction | Claim that a design meets an obligation under stated conditions | A SysML satisfaction relationship is an asserted relationship, not executable proof by itself |
| Verification | Establishing whether specified obligations/properties are met using suitable observations | Parser acceptance addresses notation; it does not test the physical mission |
| Validation | Establishing suitability for intended use in stakeholder context | Engine APIs sometimes call parsing/model checks validation; label those model-validation |
| Evidence | Retained observation and identities supporting a bounded claim | A green badge, trace link or agent statement alone is insufficient |
| Traceability | Explicit relationships among source needs, obligations, design and evidence | Link coverage is not semantic correctness |
| Baseline | Identified configuration used as a reference for change/control | A baseline is not necessarily approved; record its decision status |
| Decision | Choice with alternatives, rationale, owner and status | An agent proposal is not an accepted team decision |
| Risk | Uncertainty with consequences for objectives | A known failure and an unquantified concern need different treatment |
| Margin / reserve | Explicitly defined allowance relative to an identified quantity | 20% of initial capacity differs from 20% of mission demand |

NASA's online Systems Engineering Handbook [system design, §§4.1–4.4](https://www.nasa.gov/reference/4-0-system-design-processes/) treats stakeholder expectations, requirements, logical decomposition and design solution definition as related processes. Its [product realization, §§5.3–5.4](https://www.nasa.gov/reference/5-0-product-realization/) distinguishes verification against specified requirements and validation for intended use. Those sources support the distinction, not every authored definition above. Accessed 2026-10-10; record a controlled document edition before contractual use.

For OMG/SysML/KerML terms, consult the exact adopted specification through the language extension. For INCOSE, ISO/IEC/IEEE or a particular methodology, record the authoritative edition and access rights rather than asserting equivalence from this table. Standards can use different definitions; preserve the source wording or a bounded paraphrase and explain the project's interpretation.

A project glossary records `term`, `working meaning`, `source + edition/clause`, `project interpretation`, `owner/status`, and unresolved differences. Use proposed/open status until the appropriate owner decides. A general vocabulary entry is not a requirement approval.

Example: “retain at least 20% of initial usable capacity after the 2 km mission” is the proposed requirement. `remaining >= reserve` is its modeled condition under stated assumptions. “choose the smallest battery among these three options” is the finite-set objective. A clean parser result addresses notation, not energy adequacy.
