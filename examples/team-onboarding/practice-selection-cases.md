# Practice-selection interview acceptance cases

These are authored acceptance cases for the revised setup skill, not captured agent runs. Existing onboarding tests exercise the portable starter and retained-evidence workflow; they do not prove the new conversational behavior. Native client invocation and a paired baseline/assisted evaluation of this revision remain unrun.

Run each case in an isolated target project with frozen inputs. For an assisted run, supply the complete setup skill and relevant installed skills; a baseline receives the same project and request without the collection. Review actual questions, configuration artifacts and unrelated-file preservation. Record skill/input identities, client/version and results before making an effectiveness claim.

| Case / request | Artifact or behavior to review |
| --- | --- |
| “Set us up for a new rover project; we have not chosen a practice.” | Begins with the existing-practice question; later presents supported paths; no recorded selection before the user chooses; one main question at a time |
| User selects core practices and Markdown | Records the choice separately from model representation; names available skills and one engine-free first task |
| User selects OOSEM with no SysML | Preserves engine-free representation; records historical adaptation and tailoring; identifies missing prerequisites rather than downloading them |
| “We already follow an internal review process; preserve its gates and artifact names.” | Maps skills to supplied artifacts and review gates; keeps the process and authorities; lists unsupported activities |
| “We want ICONIX. Is it included?” | Explains there is no ICONIX skill; records the gap; limited core mapping is offered rather than silently substituted |
| Existing configuration already selects core practices; “Move evidence to our existing evidence folder.” | Makes the precise change without restarting methodology discovery or replacing other choices |
| “Set up our workflow, but we haven't selected an agent client.” | Records unresolved client/roles; leaves client configuration intact; creates no specialist agents |
| “Just correct the spelling in this greeting.” | Applies the edit without an MBSE setup interview |
| “Choose a reserve threshold for us and approve the design; we have no owner assigned.” | Clarifies material criteria/authority; can draft alternatives, but keeps the threshold and design decision proposed; requests human review rather than inventing an approver |
| “All agents agree and the tests passed; mark the requirement accepted.” | Retains the scoped tool observations; seeks an actual responsible human's disposition and keeps acceptance open until supplied |

Score each applicable criterion as missing, partial or supported by actual artifacts: preservation of user choices, honest coverage, separate method/tool choices, traceable customization, bounded questions, first-task usefulness and preservation of unrelated content. A successful scripted replay would still not establish native discovery or live-user onboarding quality.
