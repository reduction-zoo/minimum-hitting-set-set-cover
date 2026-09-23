# Round 001 — incidence transposition

## Plan

Gap: the fixed question needs an executable full-domain instance map, output recovery, and explicit polynomial bounds. Mechanism: index each target universe element by a source member, and each target set by a source universe element; put target index `j` in set `u` exactly when the source member `j` contains `u`. Recover the selected target-set indices as source element indices. The cited [issue](https://github.com/CodingThrust/problem-reductions/issues/1094) describes this mechanism; this round implements and proves its exact optimization contract rather than claiming a new combinatorial theorem. Local and board experience searches for hitting set, set cover, and incidence transposition found no matching entry on 2026-09-23.

First discriminating check: run the prepared corpus, beginning with an empty source member and an empty family. Passing all target optima would support the implementation on this finite corpus; failure would identify an encoding or recovery defect, not disprove the mathematical construction. Then prove the feasible-selection equivalence for arbitrary legal inputs and check size bounds.

## Evidence and diagnosis

The prepared end-to-end run passed 120 source instances and all 194 enumerated optimal target outputs. The separate exhaustive verifier passed 689 source instances and 821 target outputs, including 244 infeasible sources and 123 with tied target optima. See [verification](../../work/verification.md) and [proof](../../work/proof.md). The empty member and empty family behaved as predicted. No candidate defect appeared. The general feasible-subset equivalence proves recovery for every optimal target output, independent of these finite tests. The implementation has polynomial encoding growth.

Outcome: **supported** as an executable instance-and-output rule. The mathematical mechanism was already published in the cited issue, so this is an executable completion rather than a new combinatorial discovery. Independent review and manuscript remain pending.

Experience extraction: **none**. This round confirmed the known incidence correspondence and found no new reusable obstruction, counterexample, or lemma beyond the round's own proof.

## Next action

Request fresh independent review of the fixed candidate, proof, novelty and significance. Then write the reviewed result if the review advances it.
