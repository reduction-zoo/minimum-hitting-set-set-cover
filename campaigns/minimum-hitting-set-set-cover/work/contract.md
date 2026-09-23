# Executable contract

The source and target instances use the same JSON shape: `{"universe_size": n, "sets": [[...], ...]}`. Here `n` is a nonnegative integer, and each inner list contains distinct integers in `[0,n)`. Its order is immaterial. The outer list is indexed and may contain repeated or empty sets. An empty universe and family are legal.

A solution is `{"selected": [i,...]}` with distinct, in-range indices, or the JSON string `"NO-SOLUTION"`. For the source, selected indices denote universe elements and must meet every source set. For the target, they denote indexed target sets and must cover every target element. A selected solution is valid only if its cardinality is globally minimum. `NO-SOLUTION` is valid exactly when no feasible selection exists. Empty selection is optimal when the constraint family is empty or the target universe is empty.

`algorithm.py` reads one source instance on stdin and emits one target instance on stdout. `algorithm.py --extract` reads `{"source": ..., "target_solution": ...}` and emits one source solution. Both modes are deterministic, run in fresh processes, and emit only JSON on stdout. Execution errors exit nonzero with diagnostics on stderr. The maps may assume legal inputs and valid target outputs under the reduction contract.
