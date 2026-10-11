# MBSE skills ecosystem map

[Interactive HTML](ecosystem-bubbles.html) · [Static SVG](ecosystem-bubbles.svg)

The map uses the same pastel category-bubble layout as the companion awesome catalog. Human responsibility sits at the center; surrounding groups organize discovery/research, requirements/design, checks/traceability, models/communication, methodology profiles, proposed agent roles and method candidates.

## Meaning and coverage

There are 30 entries: 16 actual skills, three profile conventions, three human-review concepts, two illustrative agent roles and six unimplemented methodology candidates. Solid outlines represent skills and project conventions. Dashed outlines distinguish proposed roles and method candidates; the viewer also states each entry's availability in text.

Placement is a browsing choice. The catalog's core, methodology, language/tool and visualization layers remain authoritative. The map does not establish dependencies, agent orchestration, method compliance, qualification or engineering acceptance. Equal circle sizes are decorative. Profiles are Markdown conventions, not executable packages. No specialist agents are shipped.

The viewer supports category zoom, keyboard activation, Escape to reset zoom, search, kind/availability filters and a full-map SVG export. An accessible linked directory and the static map remain available without JavaScript. Download the standalone HTML and open it locally; GitHub does not execute HTML viewers. There are no external runtime dependencies.

## Sources and regeneration

- [Skill catalog](../../skills/catalog.json): membership, authoritative layers and composition prerequisites.
- Each skill's `SKILL.md`: descriptions and portable instructions, linked by the viewer.
- [Concept notes](ecosystem-concepts.json): profiles, human-review conventions, illustrative roles and unimplemented candidates, with source links.
- [Generator](../../scripts/build-ecosystem-map.py): primary placements and circle geometry.
- [Viewer template](../../scripts/templates/ecosystem-map.html): interaction and presentation.

From the repository root:

```bash
just ecosystem-map
```

Or run `uv run --locked --offline python scripts/build-ecosystem-map.py`. Update source files rather than editing generated HTML/SVG. The generator checks unique coverage, candidate membership, local source targets, circle containment and sibling spacing. A renamed or added skill needs a corresponding browsing placement. Core/extension reclassification still follows the catalog rules.

## Recorded presentation checks

- Generation covered all 16 skills and 14 concepts in eight groups; geometry and source-target checks passed.
- Browser checks passed for category zoom, keyboard selection, Escape reset, proposed-role and unimplemented-method filters, search, empty results, full-map export from a filtered/zoomed view, and the no-JavaScript directory.
- Desktop and mobile views had no horizontal overflow; overview, zoom and mobile captures were inspected. No runtime exceptions were observed.
- The generated static SVG passed the diagram-design static self-check. The custom viewer is checked separately in a browser; it is not a motion-controller template.

These checks concern the map's navigation and presentation, not native skill invocation or agent behavior. Human review is required before adopting changed engineering obligations, decisions or adequacy claims.
