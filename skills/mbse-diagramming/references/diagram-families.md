# Diagram families: coverage and authoring criteria

The user-supplied automobile table uses familiar SysML v1 diagram-family names. Its publication/edition is unidentified; it is task context, not normative authority. [OMG SysML 1.7](https://www.omg.org/spec/SysML/1.7) and [SysML 2.0](https://www.omg.org/spec/SysML/2.0) are separate specifications. Select the required language/version before claiming formal notation. The guidance below is original engineering view-design advice; it is not a substitute for the adopted specification.

## Current coverage

| Requested family | Collection guidance | Formal notation/examples |
| --- | --- | --- |
| Package | Organization/view ownership criteria below | No dedicated formal template or native validation |
| Requirement | Requirements and traceability practices; criteria below | No formal requirement-diagram template |
| Block definition | Logical/type/hierarchy criteria below | Informal topology only; no SysML v1 BDD exporter |
| Internal block | Parts/interfaces/connection criteria below | Source-linked informal example; no formal IBD exporter |
| Use case | Actor/boundary/goal criteria below | No dedicated rendered example |
| Sequence | Ordering/message criteria plus Mermaid syntax reference | No native sequence rendering tested |
| Activity | Flow/decision/concurrency criteria plus Mermaid flowchart reference | No formal activity-notation example |
| State machine | State/transition criteria plus Mermaid state syntax reference | No native state rendering tested |
| Parametric | Constraint reasoning and engineering plots; criteria below | No formal parametric-diagram template or solver |
| Timing (the table labels it outside SysML) | Time-axis/event criteria below | No dedicated timing renderer/example |

Mermaid, Graphviz and editable sketches can communicate these concerns with an explicit legend. A generic flowchart/class shape is not automatically a formal SysML diagram. Full formal-family support requires edition-specific notation references, a suitable renderer/modeling engine, source/model mapping, and tested examples. Existing tool-skills remain optional handoffs.

## Select and author the relevant family

- **Package / organization view:** show namespaces, package ownership and intentionally exposed dependencies/imports. Separate containment from dependency arrows. Identify whether a viewpoint is a stakeholder perspective or a package containing view artifacts; visual nesting alone does not establish either.
- **Requirement view:** show stable IDs, obligation text/acceptance and source/status. Distinguish derivation, refinement, allocation, satisfaction claims and verification links. Include check/evidence identities in a companion trace matrix when the diagram would become unreadable. A relationship labeled satisfaction records a claim; retain its supporting observation separately.
- **Block definition / type or hierarchy view:** identify definitions, specialization and part/composition relationships with multiplicity and role names where material. Distinguish a type from its occurrences. Do not interpret all hierarchy arrows as inheritance or containment. An analysis context should identify assumptions, quantities and relevant participants rather than only component names.
- **Internal block / internal structure view:** choose one enclosing context, show part occurrences, ports/interface endpoints and connectors. Name the exchanged information, energy or material and direction/units where applicable. Check producer/consumer responsibilities and distinguish an external context boundary from a subsystem's internal structure.
- **Use case / stakeholder interaction view:** show actors outside the selected system boundary and goals/services inside it. State scope, success condition and exceptions in a companion scenario. Keep implementation steps in a behavior view; avoid making every internal function a stakeholder use case.
- **Sequence / interaction view:** identify participants/occurrences and the triggering scenario. Preserve message sender/receiver, ordering, guards and alternatives. Distinguish calls, replies and physical/information exchanges. Show concurrency and timing constraints only when supported by the source; vertical placement alone is not a quantitative time axis.
- **Activity / behavior-flow view:** identify inputs/outputs, actions, control and object flows, decision guards and parallel branches. Distinguish branching from concurrency and their merge/join conditions. Trace actions to responsibilities and show exceptional outcomes relevant to the requested decision. A Mermaid flowchart is an explanatory rendering unless formal semantics are established separately.
- **State machine / lifecycle view:** identify the state-owning system, initial/terminal conditions, states, triggers, guards and effects. Check event coverage, unreachable states and competing transitions against the supplied behavior. State names should represent conditions rather than simply repeat an activity sequence. Mark unmodeled faults or recovery explicitly.
- **Parametric / analysis view:** identify quantities, units, equation/constraint definitions and bindings to the actual design parameters. Separate known inputs, solved values, constraints and optimization objectives. Record assumptions and solver/engine scope; independently check dimensions and numerical boundaries. A plotted feasible region is an analytical view, not proof that a formal parametric model was executed.
- **Timing / performance timeline:** use a labeled time axis with units and origin, state/value tracks, events and intervals. Distinguish measured samples, model predictions and illustrative timing. Record precision, interpolation and clock assumptions; sequence order does not establish duration. Missing temporal data remains open.

All families use the entrypoint's common source mapping, editable-source retention and separate structural/render/visual checks. Select only the families needed to answer the engineering question; a complete design is not established by producing every diagram type.
