# Round 002 — sparse-universe encoding repair

## Plan

The [initial review](../../reviews/initial/review.md) found that the first map expands a decimal-encoded `universe_size` and fails for long integers. That refutes the claimed polynomial bound and full-domain execution, while leaving the feasible-subset argument on its tested domain intact. Mechanism: index target sets only by source elements occurring in at least one member. Recover original indices through the sorted active-element list reconstructed from the source. An optimal hitting set cannot contain an unused element, so cardinality and all-optima recovery should hold. Disable Python's decimal digit cap in the CLI so legal long integers can be parsed.

First discriminating check: [large_sparse.py](large_sparse.py) runs F and G in fresh processes on sparse source systems with a 100,000-element or 5,001-digit universe, including empty family and empty member. It should reject any output that expands in proportion to the numeric universe size and require the selected original source index. This test is fixed before the repair. Passing it plus the previous suites supports the implementation but leaves the general bound to proof review. No relevant local or board experience entry was found; the reviewer finding is the direct prior evidence.

## Evidence and diagnosis

Pending.

## Next action

Run the new check against the old implementation to establish the failure, repair F/G and proof, then rerun affected checks and seek focused re-review.
