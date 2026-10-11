"""Build the skills atlas from catalog metadata, skill descriptions and concepts."""

from pathlib import Path
import html
import json
import math
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/diagrams"

# Browsing groups do not change the catalog's authoritative layer assignments.
GROUPS = [
    ("humans", "Human responsibility", "#deeae5", [("review-authority", "Engineer"), ("clarifications", "Clarify unknowns"), ("review-record", "Review record")]),
    ("discovery", "Discovery & research", "#deebf5", [("setup-mbse-skills", "Project setup"), ("mbse-discovery", "Discovery"), ("mbse-grill-me", "Interview"), ("mbse-standards-research", "Standards"), ("mbse-literature-research", "Literature")]),
    ("design", "Requirements & design", "#f5e4cf", [("mbse-requirements", "Requirements"), ("mbse-architecture", "Architecture"), ("mbse-constraint-reasoning", "Constraint reasoning")]),
    ("evidence", "Checks & traceability", "#e4e3f3", [("mbse-verification", "Verification"), ("mbse-traceability", "Traceability"), ("mbse-model-tdd", "Model TDD")]),
    ("views", "Models & communication", "#f2dfe3", [("mbse-sysml-modeling", "SysML modeling"), ("mbse-diagramming", "Diagramming"), ("mbse-excalidraw", "Editable sketches"), ("mbse-engineering-plots", "Engineering plots")]),
    ("profiles", "Methodology profiles", "#dfedde", [("profile-core", "Tailored core"), ("profile-oosem", "OOSEM profile"), ("profile-existing", "Team process"), ("mbse-oosem", "OOSEM skill")]),
    ("agents", "Proposed agent roles", "#f1e8c9", [("requirements-reviewer", "Req. review"), ("evidence-reviewer", "Evidence review")]),
    ("candidates", "Method candidates", "#dcecef", [("candidate-iconix", "ICONIX"), ("candidate-harmony", "Harmony"), ("candidate-rup-se", "RUP SE"), ("candidate-state-analysis", "State Analysis"), ("candidate-vitech-mbse", "Vitech"), ("candidate-opm", "OPM")]),
]


def build():
    catalog = json.loads((ROOT / "skills/catalog.json").read_text())
    records = {}
    for entry in catalog["skills"]:
        name = entry["name"]
        text = (ROOT / "skills" / name / "SKILL.md").read_text()
        description = re.search(r"^description: (.+)$", text, re.M).group(1)
        records[name] = {
            "id": name, "name": name, "purpose": description,
            "tasks": "Skill; catalog layer: " + entry["layer"],
            "interfaces": "Composition prerequisites: " + (", ".join(entry["requires"]) or "none declared"),
            "license": "Apache-2.0; native agent invocation remains unevaluated",
            "limits": "Authored practice, not engineering approval. Material unknowns need clarification; changed obligations, decisions and adequacy claims need responsible human review.",
            "notes": "../../skills/" + name + "/SKILL.md", "upstream": "", "access": "skill",
        }
    concepts = json.loads((OUT / "ecosystem-concepts.json").read_text())
    for record in concepts:
        assert record["id"] not in records
        records[record["id"]] = dict(record, upstream="")
    assert {r["name"] for r in catalog["skills"]} == {r["id"] for r in records.values() if r["access"] == "skill"}
    candidate_names = {r["name"] for r in concepts if r["access"] == "candidate"}
    assert candidate_names == set(catalog["research_candidates"]) | {"ICONIX"}, "Candidate concepts must match catalog plus documented ICONIX gap"
    for record in records.values():
        assert (OUT / record["notes"].split("#")[0]).resolve().exists(), record["notes"]
    nodes, groups, svg, assigned = [], [], [], []
    svg.append('<svg id="ecosystem-map" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1320 1320" role="img" aria-labelledby="ecosystem-map-title ecosystem-map-desc">')
    svg.append('<title id="ecosystem-map-title">MBSE skills, profiles and human review</title><desc id="ecosystem-map-desc">Sixteen skills and fourteen related concepts in eight groups. Human responsibility is central. Profile conventions, proposed agent roles and unimplemented methodology candidates are distinct from skills.</desc>')
    svg.append('<style>text{font-family:system-ui,sans-serif;fill:#26332f;text-anchor:middle;pointer-events:none}.category-title{font-size:20px;font-weight:650}.category-count{font-size:13px;fill:#596861}.tool-label{font-size:14px;font-weight:550}.tool-circle{fill:#ffffff;fill-opacity:.88;stroke:#ffffff;stroke-width:2}.access-proposed .tool-circle{stroke:#8b7352;stroke-dasharray:4 3}.access-candidate .tool-circle{stroke:#8b7352;stroke-dasharray:2 4}.access-guidance .tool-circle{stroke:#285f49}.access-profile .tool-circle{stroke:#587c66}.category-ring{stroke:#ffffff;stroke-width:2}</style>')
    svg.append('<circle class="ecosystem-boundary" cx="660" cy="660" r="630" fill="#f7f4e8"/>')
    for index, (gid, label, color, members) in enumerate(GROUPS):
        if index == 0:
            cx, cy = 660, 660
        else:
            angle = -math.pi / 2 + (index - 1) * 2 * math.pi / 7
            cx, cy = round(660 + 414 * math.cos(angle), 2), round(660 + 414 * math.sin(angle), 2)
        group = {"id": gid, "name": label, "color": color, "x": cx, "y": cy, "r": 176, "count": len(members)}
        groups.append(group)
        svg.append(f'<g class="category" data-category="{gid}" tabindex="0" role="button" aria-label="Explore {html.escape(label)}">')
        svg.append(f'<circle class="category-ring" cx="{cx}" cy="{cy}" r="176" fill="{color}"/>')
        svg.append(f'<text class="category-title" x="{cx}" y="{cy-144}">{html.escape(label)}</text><text class="category-count" x="{cx}" y="{cy-124}">{len(members)} entries</text>')
        count = len(members)
        for j, (name, short) in enumerate(members):
            record = dict(records[name], group=gid, short=short)
            if count == 7 and j == 6:
                dx, dy = 0, 24
            elif count == 2:
                dx, dy = (-60 if j == 0 else 60), 20
            else:
                ring_count = 6 if count == 7 else count
                angle = -math.pi / 2 + j * 2 * math.pi / ring_count
                radius = 100 if count >= 6 else 92 if count == 5 else 80
                dx, dy = radius * math.cos(angle), radius * math.sin(angle) + 24
            record.update(x=round(cx+dx, 2), y=round(cy+dy, 2), r=44)
            nodes.append(record); assigned.append(name)
            x,y = record["x"],record["y"]
            svg.append(f'<g class="resource access-{record["access"]}" data-resource="{record["id"]}" tabindex="0" role="button" aria-label="{html.escape(record["name"])}">')
            svg.append(f'<title>{html.escape(record["name"])}</title><circle class="tool-circle" cx="{x}" cy="{y}" r="44"/>')
            wrapped = textwrap.wrap(short, width=12, break_long_words=False)
            svg.append(f'<text class="tool-label" x="{x}" y="{y-(len(wrapped)-1)*8+5}">')
            for k, line in enumerate(wrapped):
                svg.append(f'<tspan x="{x}" dy="{0 if k==0 else 16}">{html.escape(line)}</tspan>')
            svg.append('</text></g>')
        svg.append('</g>')
    svg.append('</svg>')
    assert len(assigned) == len(set(assigned)) and set(assigned) == set(records), "Primary placement must cover every catalog entry exactly once"
    for group in groups:
        children = [n for n in nodes if n["group"] == group["id"]]
        for i,a in enumerate(children):
            assert math.hypot(a["x"]-group["x"],a["y"]-group["y"])+a["r"] <= group["r"], a["name"]
            for b in children[i+1:]:
                assert math.hypot(a["x"]-b["x"],a["y"]-b["y"]) >= a["r"]+b["r"]+4, (a["name"],b["name"])
    for i,a in enumerate(groups):
        for b in groups[i+1:]:
            assert math.hypot(a["x"]-b["x"],a["y"]-b["y"]) >= a["r"]+b["r"]+4
    svg_text = "\n".join(svg)
    nav = ''.join(f'<button class="category-nav" data-group="{g["id"]}"><span class="swatch" style="background:{g["color"]}"></span><span>{html.escape(g["name"])}</span><span class="nav-count">{g["count"]}</span></button>' for g in groups)
    listing = ''.join(f'<li data-list-resource="{n["id"]}"><a href="{n["notes"]}" data-resource-link="{n["id"]}">{html.escape(n["name"])}</a></li>' for n in sorted(nodes,key=lambda n:n['name'].lower()))
    data = json.dumps({"groups":groups,"resources":nodes},ensure_ascii=False).replace('</','<\\/')
    template = (ROOT / "scripts/templates/ecosystem-map.html").read_text()
    for marker,content in {"__SVG__":svg_text,"__NAV__":nav,"__LIST__":listing,"__DATA__":data,"__COUNT__":str(len(nodes))}.items():
        template=template.replace(marker,content)
    OUT.mkdir(exist_ok=True)
    (OUT / "ecosystem-bubbles.html").write_text(template)
    (OUT / "ecosystem-bubbles.svg").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+svg_text+'\n')
    print(f'Built {len(nodes)} entries (16 skills) in {len(groups)} groups; unique placement, containment and spacing verified.')


if __name__ == "__main__":
    build()
