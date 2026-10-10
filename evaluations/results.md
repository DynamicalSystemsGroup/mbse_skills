# Initial artifact comparison

Date: 10 October 2026. One independent baseline run and one skill-assisted run completed the identical [request](request.md) using unchanged local input bytes and the same engine profile. The candidates were isolated from each other's outputs. A separate reviewer inspected artifacts under labels A and B without reading the skills or parent conversation. These controls support an exploratory comparison; they do not establish a benchmark or causal performance gain.

| Criterion (0–2) | Baseline A | Assisted B |
| --- | --- | --- |
| Correct model and smallest feasible candidate | 2 | 2 |
| Independent boundary calculation | 2 | 2 |
| Native red/green checks and reproducible identities | 1 | 2 |
| Honest empty/undecided/LSP interpretation | 2 | 2 |
| Source/provenance and engineering categories | 1 | 2 |
| Assumptions and scoped optimality | 2 | 2 |
| Total | 10/12 | 12/12 |

Both chose 270000 J correctly and demonstrated native failure for the original design and satisfaction for the changed design. Assisted B retained per-model hashes, additional boundary controls, library identity and explicit normative clause references. Baseline A did not retain changed-model hashes beside its captures and left the library digest unverified. The selected model bytes were identical in the two outputs.

The reviewer recomputed model hashes and checked native capture contents. It did not independently verify executable/library bytes, rerun engines, verify the OMG passage, or reproduce the reported literature searches. The parent separately inspected the relevant official PDF passages and artifact identities. No claim that the unidentified paper exists or supports the model was accepted.

The independent helper review discovered capture defects after the candidate runs: descendant-held pipes could exceed a timeout, and stale unversioned LSP publications could falsely look like successful edit restoration. Those bugs were fixed, four regression cases added, and the helper fixes independently reviewed. The original candidate captures remain unchanged. Their earlier unversioned LSP restoration observations are weak evidence. A separate post-review LSP run of B's model corroborated each text in fresh sessions; the final public example captures use the revised helpers.

The grader found no MBSE skill applicable to the unrelated greeting-edit request based on the six frontmatter descriptions. This is catalog-level review, not a measured automatic-routing test in another client.

[Artifact inventory](artifact-inventory.json) retains task-input, skill/reference and candidate-output hashes. Full candidate native artifacts remain in ignored `.local/rover-work/output-a` and `output-b`; caches are excluded from the inventory. The exact pre-review helper source bytes were not independently frozen before the candidate runs. For a reproducible current tool demonstration, use the retained [rover evidence](../examples/rover/evidence/summary.json), its raw CLI/LSP captures and the current helper hashes.

Next evaluations should independently exercise standards lookup, vocabulary ambiguity and literature search, expand task variety and repeat runs. This integrated pair supports retaining the starter for further use; it does not establish six separate skill improvements.
