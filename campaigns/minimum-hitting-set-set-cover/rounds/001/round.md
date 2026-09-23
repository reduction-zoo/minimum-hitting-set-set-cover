# Round 001 — incidence transposition

## Plan

Gap: the fixed question needs an executable full-domain instance map, output recovery, and explicit polynomial bounds. Mechanism: index each target universe element by a source member, and each target set by a source universe element; put target index `j` in set `u` exactly when the source member `j` contains `u`. Recover the selected target-set indices as source element indices. The cited [issue](https://github.com/CodingThrust/problem-reductions/issues/1094) describes this mechanism; this round implements and proves its exact optimization contract rather than claiming a new combinatorial theorem. Local and board experience searches for hitting set, set cover, and incidence transposition found no matching entry on 2026-09-23.

First discriminating check: run the prepared corpus, beginning with an empty source member and an empty family. Passing all target optima would support the implementation on this finite corpus; failure would identify an encoding or recovery defect, not disprove the mathematical construction. Then prove the feasible-selection equivalence for arbitrary legal inputs and check size bounds.

## Evidence and diagnosis

Pending.

## Next action

Implement F and G, run the prepared candidate suite, and verify independently.
