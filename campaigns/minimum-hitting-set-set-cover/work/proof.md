# Incidence-transpose rule and proof

## Domains and maps

Let a legal source instance be an explicit universe `U={0,...,n-1}` and indexed family `C=(C_0,...,C_{m-1})`, with each `C_j⊆U`. The source output is either a minimum-cardinality set of element indices meeting every `C_j`, or `NO-SOLUTION` when none exists. Let a legal target instance be an explicit universe and indexed family of unit-cost subsets; repeated and empty sets are permitted. Its valid outputs are exactly its minimum-cardinality covering subfamilies, or `NO-SOLUTION` when none exists. The JSON encodings are fixed in [contract.md](contract.md).

Let `A=⋃_j C_j` be the sorted list `(a_0,...,a_{q-1})` of source elements occurring in at least one member. `F` makes target universe `V={0,...,m-1}` and one indexed target set `D_i={j∈V:a_i∈C_j}` for each `i<q`. `G` maps a selected target-set index `i` to source element `a_i`, reconstructing `A` from the source input; it maps target `NO-SOLUTION` to source `NO-SOLUTION`. The implementation is [algorithm.py](algorithm.py). Both operations use only the current input and are deterministic.

## Correctness

For every target index subset `I⊆{0,...,q-1}`, write `H_I={a_i:i∈I}`. For each `j∈V`, `j` is covered by the target sets indexed by `I` if and only if there is an `i∈I` with `j∈D_i`, if and only if `H_I∩C_j` is nonempty. Thus `I` covers `V` exactly when `H_I` hits every source member, and `|I|=|H_I|` because the active elements are distinct.

Every source hitting set `H` can be replaced by `H∩A` without losing feasibility, since each `C_j⊆A`. If `H` is optimal, it contains no unused element: otherwise `H∩A` would be smaller. Hence target and source feasibility agree, including the infeasible case; their minimum cardinalities agree; and **every** optimal target output recovers an optimal source hitting set. Target `NO-SOLUTION` maps to source `NO-SOLUTION` exactly when both are infeasible. This proves `G(x,y)∈S_A(x)` for every legal source `x` and every valid target output `y∈S_B(F(x))`, including all ties.

The equivalence covers the boundaries without exceptions. An empty source member gives a target universe element in no target set and infeasibility. An empty source family gives an empty active list and target universe, whose empty selection is optimal. A source element absent from all members is omitted, as no optimum uses it. Repeated source members become distinct target universe elements with equal incidence; empty target sets are allowed, though this construction creates no such set for active elements. The empty source universe is covered by the same argument.

## Runtime and encoding size

Let `L` be the source JSON encoding length, `r=Σ_j |C_j|`, `q=|A|`, and `m` the number of members. The decimal value of `n` may be exponential in `L`, but `m,r,q≤L` up to constants. Parsing each written integer, deduplicating and sorting the `r` incidences, and scanning the `qm` active-element/member pairs take polynomial time in `L`; each integer comparison, hash, and JSON conversion costs polynomial time in its at most `L` digits. A coarse worst-case bit bound is `O(L^4)`, which also covers Python's built-in sort and hash-table operations. The output has `m` universe elements, `q` indexed sets and exactly `r` incidences. Every emitted index is at most `m`, so its decimal length is `O(log(L+1))`; target JSON length is `O((m+q+r)log(L+1))`, hence polynomial in `L`. The CLI disables Python's default decimal-digit limit to admit legal integers of arbitrary finite length, subject only to available memory.

Let `T=|y|`. Recovery parses the source and target output, rebuilds sorted `A` from at most `r≤L` written incidences, and replaces each selected target index with its source element. This is polynomial in `L+T`; a coarse worst-case bit bound is `O((L+T)^4)`. Its JSON output has at most `q` selected elements, each with at most `L` digits, so its length is `O(L^2+T)`. It does not call either solver or use state from the forward process. The dominant target instance overhead is the written incidence count, preserved exactly; the numeric universe size is never expanded.

## Prior result and scope

The [existing reduction issue](https://github.com/CodingThrust/problem-reductions/issues/1094) states the same incidence-transpose construction, cardinality correspondence and corner-case idea. The argument above reconstructs that proof against this campaign's exact output contract and executable encodings. It is not a new combinatorial theorem. The question's cited Garey–Johnson book supplies the classic problem definitions; the issue, rather than an unverified theorem attribution to that book, is the direct prior description of this rule.
