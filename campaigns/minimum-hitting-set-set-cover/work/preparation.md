# Preparation, 2026-09-23

The fixed corpus has 120 distinct legal source instances: 12 hand-designed edge cases and 108 random cases from recorded integer seeds. `generate_cases.py` regenerates each random source from its seed and records the Z3 optimum. Source universe sizes range from 0 to 7 and family sizes from 0 to 8. There are 77 feasible and 43 infeasible sources. The edge cases include empty universe and family, empty member, repeated members, unused elements, forced choices, and tied optima.

`check.py` independently encodes each source set as an OR over selected elements and each target universe element as an OR over target sets containing it. It minimizes the sum of Boolean selections using Z3 Python 4.16.0.0 (`sat` supplies a witness and exact cardinality; `unsat` means no solution; any other status fails). The checker validates each witness against the problem definition, separately from its Z3 constraints. For all 120 source cases, an exhaustive subset search also agrees with Z3's optimum. Hand-computed source and target examples check empty and infeasible cases. Deliberately invalid, duplicate-index, suboptimal and false no-solution outputs are rejected. The `--candidate` mode will run both candidate commands as separate subprocesses, solve the actual target, enumerate all target optima at the small corpus sizes, and validate every recovered source output against the source optimum.

From the repository root:

```sh
uv sync --locked
uv run python campaigns/minimum-hitting-set-set-cover/work/check.py --self-test
```

Observed: `Preparation corpus passed: 120 distinct cases, 108 random, 12 edge` and `self-test passed: 120 source cases; Z3 4.16.0`. The corpus is finite and contains no instance with more than seven source elements or eight source sets. The source labels are independently checked by exhaustive enumeration on these finite instances; this provides no proof for unbounded inputs. The first generator run failed because Z3's Python API treats an empty integer sum as a Python integer. The oracle now includes a Z3 zero term, preserving the empty-universe semantics. No expectation changed.
