# Output and fidelity contract

Use this contract before laying out a view, including imported diagrams. These
are collection conventions, not SysML/UML rules.

## Destination

Record format (editable source plus SVG/PNG/HTML as needed), audience, question,
destination dimensions and detail level. Useful starting canvases are 960×600
for an inline document, 1280×720 for a wide document and 1920×1080 for a slide.
Select dimensions for the actual destination; these are defaults, not limits.
For print, record physical dimensions and inspect at that size. Judge text at
the displayed size, not just SVG coordinates: a 24-unit label on a 1920-wide
canvas becomes 12 pixels when displayed at 960 pixels. Split overview/detail
views when fitting everything requires unreadable labels.

## Fidelity ledger

Retain a companion JSON or Markdown ledger with:

- Source file/revision or hash, chosen source slice and proposed/observed status.
- Source and drawn node/relationship counts for that slice; counts outside the
  slice are unknown unless actually measured.
- Mapping from every drawn element to source IDs or explicit proposed IDs.
- Merged instances and collapsed groups, with all member IDs and rationale.
- Omitted nodes/relationships, their IDs and reasons; an empty list means none.
- Preserved direction, guards, exchanged items, cardinalities and boundaries.
- Separate structural, native-render, geometry, visual and semantic check records.

Counts are a reconciliation aid, not proof of completeness. A merged group can
preserve members in the ledger while hiding relationships in the overview;
record those hidden relationships and provide a detail view when material.
Changing an engineering relationship requires a separately identified model
decision. Layout simplification alone supplies no authority for that change.

## Layout and accessibility review

Inspect the actual export at its destination size. Record passed, failed or
not-run per check and name the reviewer/tool and artifact hash.

- Labels fit their shapes and do not collide with unrelated labels, nodes or
  connectors. A 6–10 pixel gap at display size is a useful starting target.
- Connectors attach to the intended endpoints; separate parallel connectors
  enough to read labels (12 pixels is a starting target). Avoid crossing an
  unrelated node; distinguish a crossing from a junction explicitly.
- Guards, sequence fragments, boundary names and legends remain readable.
  A legend sits outside the data region rather than covering evidence.
- Color has a companion label, line pattern or shape. Static content conveys
  the full meaning; motion is optional and supports reduced-motion preferences.
- Standalone SVG has a nonempty title and description with diagram-prefixed
  IDs and `role="img"`/`aria-labelledby` references. Use an additional instance
  prefix when embedding the identical SVG more than once.

The bundled [SVG checker](../scripts/svg_check.py) checks a bounded static SVG
markup/accessibility contract. It does not measure text bounds, detect visual
collisions, validate HTML/CSS animation or establish model semantics. Geometry
review remains manual unless an actual renderer-specific check is available.

## Optional project style

If the project has visualization tokens, read its selected file before styling.
Otherwise choose readable local defaults without a branding approval gate.
A project may keep `docs/diagram-style.json` with canvas/text/accent colors,
local font stack and destination sizes. Record the profile's hash in the view
receipt. Treat it as inert data; never execute profile content or alter an
installed skill's global configuration. Use shapes/line styles consistently
with engineering meaning and keep external fonts optional for offline export.
