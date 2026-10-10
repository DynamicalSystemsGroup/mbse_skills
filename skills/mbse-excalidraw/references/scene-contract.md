# Excalidraw scene contract

The official [JSON-format documentation](https://docs.excalidraw.com/docs/codebase/json-schema), reviewed 2026-10-10, describes `.excalidraw` files with `type`, `version`, `source`, `elements`, `appState` and `files`. The starter uses document format version 2. That is a document format, not a pinned editor release.

Prefer an editor-created scene or the selected installation's supported conversion API. Its [export utilities](https://docs.excalidraw.com/docs/@excalidraw/excalidraw/api/utils/export) provide SVG and canvas exports. No API package is installed by this skill. Use a deliberately selected local/self-hosted editor for sensitive material; uploading a scene is a separate action requiring appropriate authorization.

For a hand-authored basic scene, retain the common element geometry/style fields, unique IDs and deletion state. Text needs its text/font/alignment fields; arrows need points and endpoint bindings when the intended attachment is editable. Containers and their bound text/arrows should reference each other consistently. Keep images and their file payloads together if the requested scene uses them; the bundled checker does not support image payload validation.

Run `python /path/to/scene_check.py scene.excalidraw`. The stdlib helper checks only a bounded starter subset: format version, IDs, finite geometry, arrow points, existing live binding targets, reciprocal bound-element references, and text-container reciprocity. It deliberately rejects live element types outside rectangle, ellipse, diamond, text and arrow, rather than presenting a partial check as full validation. Deleted elements are retained but excluded from live bindings. It is not a geometry/collision checker or native editor renderer.

Our evidence convention records input hashes, material element-to-source mapping and status, source/editor version when known, and native import/export/inspection results separately. Converting from Mermaid or another view requires a semantic comparison; stable syntax does not guarantee equivalent topology.

## Existing skill handoff

An already-available `github/awesome-copilot` Excalidraw generator or `coleam00/excalidraw-diagram-skill` can author scenes or provide layout guidance. Read the selected skill and only its relevant resources; preserve project artifact IDs, source mapping and native scene despite any differing presentation defaults. This extension adds the engineering/evidence contract and basic structural check, not another full editor. No third-party skill or helper is bundled or installed.
