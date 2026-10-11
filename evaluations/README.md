# Exploratory skill evaluation

Evaluate observable artifacts using the same request and input bytes with and without the skills. Keep candidate workspaces isolated and hide the rubric during task execution. Pin engine identities, retain commands/native results, and review models directly. A baseline that already succeeds is useful evidence; it does not justify an improvement claim.

The starter task asks an agent to revise a typed rover model for a 2 km mission, retain 20% reserve, select the smallest of three battery options, demonstrate red/green checks, explain the boundary and limitations, and assess incomplete status captures and an unidentified paper. The latter captures are deliberately incomplete synthetic inputs, not fabricated engine results.

Score 0 (missing/wrong), 1 (partial), or 2 (supported) for:

1. Correct model and smallest feasible listed candidate.
2. Independent arithmetic and boundary control.
3. Native red/green evidence with commands and artifact identity.
4. Honest interpretation of empty checks, undecided results and LSP diagnostics.
5. Source/provenance and engineering-category distinctions.
6. Assumptions and finite-set optimality limits.

The negative activation request is a simple letter greeting change. No MBSE skill should be needed. Judge applicability from the catalog metadata; this does not prove automatic routing in a particular client.

The actual run request, synthetic inputs, rubric and result are retained here. Native candidate artifacts remain ignored under `.local/rover-work/`; their inventories and hashes are recorded in the result report. The public rover example retains separate native engine evidence for reproduction without agent orchestration.

This is one exploratory pair, not a benchmark or a causal estimate. Candidate context differs because one is given the skills; all local inputs and engines are shared. No claim about six individual skill effects follows from an integrated task. A broader evaluation needs varied tasks, repeated runs, source-lookup cases with full documents, and multiple agent clients.

The later [team-workflow evaluation](workflow/results.md) covers onboarding, ambiguity, conflicting constraints, unsupported/inconclusive observations, model change impact and an unrelated greeting with frozen skill/input identities.

The [adaptive interview replay](interview/results.md) examines open discovery,
unknown thresholds, conflicting constraints, stakeholder authority, user
redirection and pausing. It is a scripted pair, not a live interview benchmark.
