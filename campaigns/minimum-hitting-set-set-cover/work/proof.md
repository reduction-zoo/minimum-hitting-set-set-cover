# Incidence-transpose rule and proof

## Domains and maps

Let a legal source instance be an explicit universe `U={0,...,n-1}` and indexed family `C=(C_0,...,C_{m-1})`, with each `C_j⊆U`. The source output is either a minimum-cardinality set of element indices meeting every `C_j`, or `NO-SOLUTION` when none exists. Let a legal target instance be an explicit universe and indexed family of unit-cost subsets; repeated and empty sets are permitted. Its valid outputs are exactly its minimum-cardinality covering subfamilies, or `NO-SOLUTION` when none exists. The JSON encodings are fixed in [contract.md](contract.md).

`F` makes target universe `V={0,...,m-1}` and one indexed target set `D_u={j∈V:u∈C_j}` for each `u∈U`. `G` maps any selected target-set indices directly to the same source element indices; it maps target `NO-SOLUTION` to source `NO-SOLUTION`. The implementation is [algorithm.py](algorithm.py). Both operations use only the current input and are deterministic.

## Correctness

For every index subset `H⊆U` and each `j∈V`, `j` is covered by the target sets indexed by `H` if and only if there is a `u∈H` with `j∈D_u`, if and only if there is a `u∈H∩C_j`. Consequently `H` covers `V` exactly when it hits every `C_j`. The two instances therefore have the same feasible index subsets and the same cardinality for each such subset. If either is infeasible, both are, so `NO-SOLUTION` is valid on both sides. If feasible, their minimum cardinalities coincide and **every** optimal target index subset is an optimal source hitting set. This proves `G(x,y)∈S_A(x)` for every legal source `x` and every valid target output `y∈S_B(F(x))`, including all ties.

The equivalence covers the boundaries without exceptions. An empty source member gives a target universe element in no target set and infeasibility. An empty source family gives an empty target universe, whose empty selection is optimal even when the source universe contains unused elements. A source element absent from all members gives an empty indexed target set. Repeated source members become distinct target universe elements with equal incidence; repeated or empty target sets remain legal. The empty source universe is covered by the same argument.

## Runtime and encoding size

Let `L` be the source JSON encoding length and `r=Σ_j |C_j|`. We have `n,m,r≤L` up to fixed encoding constants. Parsing the source and building the member sets takes `O(L+r)` expected time with Python hash sets; the nested scan performs `nm` membership operations, so expected runtime is `O(L+nm)`. A deterministic polynomial implementation may instead use a Boolean incidence matrix or sort each member; then construction takes `O(L+nm+r log(n+1))` worst-case time. The mathematical map is independent of the data structure. It emits exactly `r` incidences, `n` indexed target sets and `m` target universe elements. With decimal indices, output length is `O(L+(n+m+r) log(L+1))`, hence polynomial. The implemented Python set operations on bounded integer indices also have polynomial worst-case bit complexity because integer hashing and equality are deterministic and bounded by input bit length; the nested scan remains at most `nm` lookups.

Let `T=|y|`. Recovery parses the source wrapper and target output and copies either the special answer or the selected index list. Its runtime and output length are `O(L+T)` and `O(T)` respectively (up to JSON serialization overhead polynomial in bit length). It does not call either solver or use state from the forward process. The dominant target instance overhead is incidence transposition; the number of incidences is preserved exactly. No optional compression is needed for the declared result.

## Prior result and scope

The [existing reduction issue](https://github.com/CodingThrust/problem-reductions/issues/1094) states the same incidence-transpose construction, cardinality correspondence and corner-case idea. The argument above reconstructs that proof against this campaign's exact output contract and executable encodings. It is not a new combinatorial theorem. The question's cited Garey–Johnson book supplies the classic problem definitions; the issue, rather than an unverified theorem attribution to that book, is the direct prior description of this rule.
