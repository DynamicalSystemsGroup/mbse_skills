# Existing visualization skills

Reviewed 2026-10-10 with the find-skills workflow. Checked the skills.sh leaderboard, searched Mermaid, PlantUML, Excalidraw and Graphviz using the already cached CLI (`npx --offline skills find ...`), then inspected primary GitHub entrypoints, root license presence and selected helper imports/operations. Offline package resolution did not prevent the CLI querying its remote directory. No skills or renderers were installed.

The [candidate manifest](../../references/visualization-skill-candidates.json) records exact source commits, inspected byte hashes and GitHub metadata. The [Archify source record](../../references/visualization-sources.json) instead identifies installed release 3.0.1 by bytes; its frontmatter reports 3.0. Those identities should not be conflated.

## Findings

| Candidate | Useful capability | Evidence and adoption decision |
| --- | --- | --- |
| [Softaworks Mermaid](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/mermaid-diagrams/SKILL.md) | Concise syntax/type guidance with conditionally loaded references | MIT root license inspected; preferred syntax-authoring handoff candidate. Its global-install example is not our setup policy. |
| [Spillwave Mermaid](https://github.com/SpillwaveSolutions/design-doc-mermaid/blob/c36d83503d2ba9c1e51638dc2d8a34758a377dea/SKILL.md) | Larger hierarchy of guides, document extraction and image conversion | Selected Python converter inspected; uses existing `mmdc` or `npx`. No root license found at the inspected revision, so no source copying or default vendoring selected. |
| [Spillwave PlantUML](https://github.com/SpillwaveSolutions/plantuml/blob/8aa811cf672dd895a970e81065b8f7e7cee52ded/SKILL.md) | UML/non-UML guides, conversion and Markdown processing | Converter inspected; Java/JAR and some Graphviz-dependent layouts are separate runtime needs. Current description emphasizes types Mermaid does not readily cover. No root license found; reference candidate, not vendored implementation. |
| [OpenAI UML visualization](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/build-web-data-visualization/skills/uml-and-software-architecture-visualization/SKILL.md) | Formal UML versus explanatory-view selection, formats and rendering choices | Entry point inspected; depends on sibling skills and package references. Keep as a package-level reference candidate, not a standalone copied file. Package license terms were not established by this review. |
| [GitHub Excalidraw generator](https://github.com/github/awesome-copilot/blob/82701c24b99488536ca399ff4789a458b7a05db7/skills/excalidraw-diagram-generator/SKILL.md) | Native editable scenes, icon and arrow helpers | MIT root license and arrow helper inspected. Preferred external sketch-authoring handoff candidate; still needs actual editor import/export checks. |
| [Cole Medin Excalidraw](https://github.com/coleam00/excalidraw-diagram-skill/blob/8646fcc9f74f38539c6cdb4c969723336a96ddcd/SKILL.md) | Evidence-rich visual explanation and native scene instructions | A corresponding skill is already installed locally; upstream entrypoint inspected. No root license found in the inspected tree; no copying selected. |
| [Beautiful Mermaid](https://github.com/intellectronica/agent-skills/blob/9b0e00ad1b941165e2506545bbfddafa34cf2cb8/skills/beautiful-mermaid/SKILL.md) | SVG generation with optional PNG/browser workflow | CC0 root declaration and TypeScript renderer inspected. Separate library/runtime and agent-browser requirements; the renderer can install a missing library, and cleanup guidance removes source files, so MBSE handoff must explicitly retain our authoritative source/evidence. Not a default dependency. |
| [Archify](https://github.com/tt-a1i/archify) | Typed views, standalone HTML and layered delivery evidence | Installed skill/references/license inspected. Primary inspiration and optional existing-tool handoff; runtime not copied into this collection. |

The directory reported approximately 68.7K Mermaid-design-doc installs, 5K Softaworks Mermaid installs, 31K GitHub Excalidraw installs and 204 Spillwave PlantUML installs. These are a search-time observation, not endorsements or a runtime test. The skills.sh page and CLI differed slightly for Spillwave's count. Exact GitHub star observations are in the manifest; smaller PlantUML adoption and missing root-license evidence warrant further evaluation before choosing it as a distributed dependency.

## Integration choice

Keep our three visualization skills as MBSE adapters: source-to-view identity, engineering arrow meaning, proposal/observation status, units, constraints, uncertainty and honest evidence. Reach the chosen already-available external skill for syntax, rendering or layout. Do not recreate a general Mermaid/PlantUML/Excalidraw renderer. The two bundled helpers cover narrower checks not provided by the inspected generic entrypoints: a conservative editable-binding check and arithmetic/evidence preservation for the finite-energy summary.

UML is a modeling language; PlantUML is a source/rendering tool. Mermaid includes UML-like families but cannot be assumed to provide complete UML semantics or model interchange. For exact language rules use the [OMG UML version page](https://www.omg.org/spec/UML) and the relevant clause. None of these tool skills establishes SysML v2 round-trip support.

A future installation should select one skill, inspect its complete resources and dependencies, pin a revision, and use the target client's normal mechanism. Example discovery-provided commands (not executed):

```bash
npx skills add softaworks/agent-toolkit --skill mermaid-diagrams
npx skills add github/awesome-copilot --skill excalidraw-diagram-generator
```

No global flags, bootstrap hooks or automatic package downloads are added to this repository. Further runtime testing, complete helper audit and package-specific license review remain open. Broad descriptions and large guide collections are discovery aids, not measured MBSE capability.
