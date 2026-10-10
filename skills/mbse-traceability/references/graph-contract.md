# Optional trace graph, version 1

This is an original project convention, not a SysML interchange format or an institutional methodology.

The graph contains `schema_version: 1`, `nodes` and `edges`. Every node has a unique stable `id`, `kind`, `status`, `title`, project-relative `path` and the file's exact `sha256`. Kinds are `need`, `assumption`, `requirement`, `architecture`, `decision`, `model`, `verification`, `evidence`. Statuses are `proposed`, `accepted`, `open`, `observed`, `historical`; status is supplied by the author, never certified by the checker. Requirements additionally carry `acceptance` (a nonempty criterion, or null for an unresolved obligation).

An edge has `source`, `target`, `relation` and nonempty `rationale`. **Source depends on target.** Relations: `derives_from`, `depends_on`, `allocated_from`, `realizes`, `verifies`, `evidence_for`, `informs`. Relationship types describe meaning but all use the same dependency direction. `V-01 verifies R-01` means V-01 depends on R-01. `E-01 evidence_for V-01` means E-01 depends on V-01. An accepted decision's supporting evidence may be a dependency of the decision; avoid introducing cycles by linking the exact prior design revision rather than an artifact that already depends on that decision.

Paths must resolve to files inside the supplied project root. Several nodes may address different concepts in one file. Hashes bind the entire file, not a semantic element; editing that file therefore makes all such nodes stale. The acyclic graph describes the recorded derivation at a particular revision; represent iteration through revised artifacts rather than cyclic dependencies.

The checker validates identities, paths, link endpoints and dependency cycles. It reports each requirement's recorded path to a need, direct verification link, and linked evidence; these are coverage indicators, not semantic proof. Historical checks/evidence do not count toward current coverage; evidence must have observed/accepted status. Historical requirements remain visible but do not contribute to the current completeness flag. Confirm that every in-scope requirement in the authoritative documents is represented: the checker cannot extract missing nodes from prose. Missing acceptance, missing need/verification/evidence and stale hashes fail `--require-covered`. Without that flag, coverage gaps are reported and valid incomplete starter graphs remain inspectable. Malformed graphs and stale hashes always fail. An empty graph has no coverage and cannot pass `--require-covered`.

```bash
python scripts/trace_check.py /project/traceability.json --root /project --require-covered
python scripts/trace_check.py /project/traceability.json --root /project --changed R-01
```

`--changed` accepts repeated known IDs. Changed nodes and their reverse-transitive dependents are listed as `review_required`, including old evidence that may need rerunning. The command reports impacts but does not mark any artifact approved or overwrite graph/results. An unknown changed ID fails. The checker never creates hashes to make a stale graph pass; review changed artifacts and explicitly revise the graph.
