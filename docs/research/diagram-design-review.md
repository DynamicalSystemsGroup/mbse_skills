# Diagram-design review

Reviewed 2026-10-10 against the locally installed `diagram-design` skill at
`/home/rohan/.codex/skills/diagram-design/`, whose frontmatter declares version
2.6 and MIT licensing. This is an inspection of that installed copy, not a
claim about an upstream release. No implementation was copied or installed.

## What we can adopt

| Capability | Current collection | Proposed addition |
| --- | --- | --- |
| Output contract | Audience, purpose and source mapping are requested. | Record format, destination dimensions, detail level and audience before layout; define readable slide/document type sizes. |
| Fidelity ledger | Omissions and source mappings are required in prose. | Record source/drawn element counts, merged instances, collapsed groups and omitted relationships with reasons and source identifiers. |
| Geometry review | Visual review is required; the Excalidraw checker checks structure. | Check label collisions, connector attachment/separation, unrelated-node crossings and legend placement. Split overview/detail views when density exceeds readable capacity. |
| Accessible SVG | Our plot has a title, description, role and ARIA references. | Use diagram-prefixed IDs, validate references, retain color-independent meaning and require static/reduced-motion fallbacks for animated outputs. |
| Import adapters | Mermaid/DOT authoring and native Excalidraw scenes exist. | Add bounded Mermaid and Draw.io extraction into a shared representation with nodes, relationships, groups and provenance; treat imported labels and links as untrusted input. |
| Semantic patterns | Diagram families explain engineering authoring criteria. | Add reusable patterns for capacity bottlenecks, lifecycle gates, evidence provenance and paired verification outcomes, independently of layout choice. |
| Type-specific examples | All ten automobile-table diagram families have guidance, but formal examples and tested exports remain incomplete. | Add reviewed sequence activation/guard/fragment examples and state transition examples, with explicit renderer limitations. |
| Project style | No project-selected visualization profile. | Offer optional project-local tokens and profiles, while preserving engineering shape and relationship semantics. |

The useful architectural pattern is progressive disclosure: a short entry
skill selects an output contract, semantic pattern and type reference; scripts
perform deterministic extraction or validation. We already separate skills,
references and scripts, so this strengthens existing extensions rather than
requiring another core skill.

## What needs tailoring

- Do not automatically delete supposedly obvious edges, low-degree nodes or
  cross-cutting infrastructure. In MBSE these can represent interfaces,
  constraints, assumptions or trace links. Aggregation must retain a mapping
  back to the model and disclose what the view hides.
- Treat node budgets, fonts, colors and orthogonal routing as presentation
  defaults, not engineering validity rules. Dense formal views may need a
  different renderer or several linked views.
- Keep SysML/UML semantic checks separate from SVG/HTML checks. A polished
  sequence rendering does not establish formal UML conformance, and support
  for many visual types does not establish SysML model validation.
- Preserve our verification outcomes, including unsupported, undecided and
  not-run, when adopting comparison patterns. A generic pass/fail palette
  would lose evidence distinctions.
- Prefer optional local style profiles over a mandatory branding question.
  External fonts also need an offline fallback.

## Observed helper results

Two installed helpers were exercised against existing examples. Neither test
generated a new diagram or ran a native Mermaid renderer.

1. `scripts/self_check.py` checked an HTML wrapper containing our unmodified
   `examples/visualization/rover-energy.svg`. It exited 1 with:
   `svg 1 title/desc IDs must be diagram-prefixed, never bare`.
   Our standalone SVG uses `title` and `desc` as IDs. Prefixing them would
   prevent collisions when multiple SVGs are embedded in one document; this
   finding does not mean the standalone SVG is invalid.
2. `scripts/mermaid_extract.py examples/visualization/rover-energy.mmd --json`
   exited 2 with `mermaid_extract: malformed edge at line 2`. That line is
   `accTitle`, which is supported by [Mermaid's accessibility syntax](https://mermaid.js.org/config/accessibility.html).
   The extractor therefore needs compatibility work before reuse. Its failure
   does not establish that the Mermaid source is invalid.

Local command receipts and outputs are retained in the ignored
`.local/diagram-design-study/` directory. The inspected markup checker does
not establish geometric correctness or visual readability. Geometry/motion
verifiers mentioned as repository-only were not present among the installed
scripts, so we have not evaluated them.

## Suggested implementation order

1. Extend the visualization view contract with output sizing and a fidelity
   ledger; prefix SVG accessibility IDs and add a focused regression check.
2. Add type-specific examples and a measurable geometry review checklist.
3. Prototype import adapters, starting with our existing Mermaid examples
   and accessibility metadata, before considering implementation reuse.
4. Add optional project style profiles and engineering semantic patterns.

These are proposals. Current skills and renderers were not changed by this
review. Verify full source provenance and licensing before vendoring code;
the installed frontmatter alone is not a complete upstream provenance record.

## Subsequent implementation

After this review, the collection added the output/fidelity contract, manual
geometry criteria, semantic patterns, optional project-style guidance and
bounded sequence/state examples. Original stdlib helpers implement static SVG
accessibility checking and a narrow Mermaid/uncompressed-Draw.io importer.
The plot helper now prefixes accessibility IDs; the original reviewed plot
is preserved alongside a newly generated accessible example. See the
[example check record](../../examples/visualization/extension-checks.json).
There is no automated text-collision detector or general-purpose import/parser,
and no installed external implementation was vendored.
