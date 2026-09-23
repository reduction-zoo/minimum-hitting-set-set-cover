# Round 002 — sparse-universe encoding repair

## Plan

The [initial review](../../reviews/initial/review.md) found that the first map expands a decimal-encoded `universe_size` and fails for long integers. That refutes the claimed polynomial bound and full-domain execution, while leaving the feasible-subset argument on its tested domain intact. Mechanism: index target sets only by source elements occurring in at least one member. Recover original indices through the sorted active-element list reconstructed from the source. An optimal hitting set cannot contain an unused element, so cardinality and all-optima recovery should hold. Disable Python's decimal digit cap in the CLI so legal long integers can be parsed.

First discriminating check: [large_sparse.py](large_sparse.py) runs F and G in fresh processes on sparse source systems with a 100,000-element or 5,001-digit universe, including empty family and empty member. It should reject any output that expands in proportion to the numeric universe size and require the selected original source index. This test is fixed before the repair. Passing it plus the previous suites supports the implementation but leaves the general bound to proof review. No relevant local or board experience entry was found; the reviewer finding is the direct prior evidence.

## Evidence and diagnosis

The new test failed on the old candidate at its first 100,000-element sparse case: target output was too long. The independent review had also measured failure to parse a legal 4,301-digit integer. The cause was enumeration of the numeric universe size and Python's default integer digit cap. The repaired map enumerates only the active support and reconstructs it in recovery; it disables the digit cap in the CLI. The targeted check now passes 4 source instances and 4 target outputs, including three 5,001-digit-universe inputs. The prepared suite still passes 120 instances and 194 target outputs; the separate exhaustive verifier still passes 689 and 821. See [verification](../../work/verification.md) and [repaired proof](../../work/proof.md). These checks support the change on finite inputs; the new proof supplies the input-length bound.

Outcome: **supported**, pending focused independent re-review. The old polynomial-size claim was refuted; no conclusion drawn from the old finite suite is used to support that asymptotic claim.

Experience extraction: [active support for succinct universes](../../../../research/experience/active-support-for-succinct-universe.md) created as a reusable lemma and size-audit reminder. Its proposed promotion to the board's local collection remains pending without editing the board.

## Next action

Request focused re-review of the map, recovery, bound, and long-integer behavior. If advanced, draft and inspect the manuscript.
