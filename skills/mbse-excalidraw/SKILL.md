---
name: mbse-excalidraw
description: Create or revise editable Excalidraw engineering sketches with stable artifact mapping, meaningful arrows and explicit proposal status; retain the scene and review its exports.
license: Apache-2.0
---

# MBSE Excalidraw Sketches

Use an editable sketch for collaborative exploration of system boundaries, responsibilities, interfaces or alternatives. Preserve the difference between a discussion artifact and an authoritative engineering model.

1. Identify the source artifacts, revision, audience and question. Name proposed versus observed content and unresolved decisions before drawing.
2. Read [scene contract](references/scene-contract.md). Prefer the available editor or supported skeleton API when authoring; when writing native JSON directly, use the selected editor's documented fields and report import compatibility only after actually testing it.
3. Create stable element IDs and a companion element-to-artifact mapping. Use separate editable text and shapes; bind arrows to their endpoints where supported. Label exchange or trace semantics and show boundary ownership explicitly.
4. For an edit, preserve unrelated elements, IDs, bindings and user layout. Compare endpoints and labels after rearranging; an arrow that happens to touch a shape is weaker than a retained binding.
5. Save the native `.excalidraw` scene. Run the bundled [scene_check.py](scripts/scene_check.py) for the starter structural subset, then open/import in the selected editor when available. Check labels, endpoint bindings and the intended view; export SVG or PNG if requested or needed for review.
6. Deliver the editable scene, source mapping, assumptions and a check record that separates structural validation, actual editor import, export and visual inspection. Retain native source alongside an image.

Completion requires mapped material shapes/arrows and disclosed uncertainty. A structural pass is not full Excalidraw schema validation, import proof, or SysML model validation. Static preview pictures cannot establish editability or editor binding behavior.

For output sizing, fidelity ledgers and geometry review, use the diagramming
extension's [output contract](../mbse-diagramming/references/view-contract.md).
Keep source IDs and bindings through aggregation; show hidden relationships
in the ledger or a detail view instead of silently removing them for layout.
