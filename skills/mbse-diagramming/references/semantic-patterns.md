# Engineering semantic patterns

Select a pattern by the question the view answers, then choose its layout.
These are explanatory conventions, not a replacement for a methodology.

| Question | Pattern and required content |
| --- | --- |
| Where does demand exceed capacity? | Show producers, queue/resource, consumer and capacity/demand units. Label overflow or rejected work, distinguishing modeled limits from observations. |
| What authorizes progression? | Show lifecycle stages with entry inputs, exit criteria, decision authority and resulting evidence. Mark pending gates explicitly. |
| Where did a requirement come from? | Link raw need, interpretation, proposed requirement and acceptance criterion. Preserve source IDs, unresolved ambiguity and stakeholder authority. |
| Why do two verification results differ? | Align the same input/model identity and check scope, then show each operation and the first observed divergence. Preserve unsupported, undecided, unavailable and not-run independently of violations. |
| What crosses an ownership boundary? | Name owners, interface, exchanged item, direction and permitted/forbidden interactions with source references. A drawn boundary is not evidence of enforcement. |

For paired engine views, differing tool capability is not automatically a
model defect. Separate a native diagnostic from an interpretation, and expose
missing operations rather than inventing equivalent results. For stage gates,
a check passing does not authorize approval; show the actual decision record.
