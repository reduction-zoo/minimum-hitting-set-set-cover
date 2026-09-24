# Minimum Hitting Set → Minimum Set Cover

**Status:** `ready_for_expert_review` · **Research model:** `GPT-6 (exact variant/version unavailable)` · **Submitted:** 2026-09-23

The public campaign supplies deterministic polynomial-time construction and recovery for the fixed exact optimization endpoints. Every globally optimal target output recovers a globally optimal source hitting set, including all ties; NO-SOLUTION corresponds exactly to infeasibility.

## Construction

Create one target-universe element per source member and one target set per source element that occurs in a member. A target set contains the indices of members containing its source element. Recovery rebuilds the sorted list of those active elements and maps selected target-set indices back to source indices. Omitting unused elements keeps the construction polynomial even when the source universe size is a compactly encoded, large decimal integer. The incidence duality is known prior work; the archive supplies the executable rule and its encoding-aware bound.

## Evidence

- **Mathematical correctness and recovery: Written proof; independent agent review advanced.** The proof covers every target optimum, ties, empty and repeated members, and infeasibility. The focused reviewer accepted the repair of an initial sparse-universe size gap. Human expert acceptance remains pending. ([evidence](campaigns/minimum-hitting-set-set-cover/reviews/followup/review.md))
- **Construction and recovery complexity: Written polynomial bounds.** Both maps have polynomial worst-case bit time and output length in the written JSON encodings. The bounds were independently reviewed; they are not formally certified or claimed optimal. ([evidence](campaigns/minimum-hitting-set-set-cover/work/proof.md))
- **Executable verification: Finite checks passed.** The prepared suite checked 120 source instances and 194 target outputs; an independent exhaustive verifier checked 689 small source instances and 821 outputs. Sparse regressions checked 5,001-digit universe values, and the reviewer checked alternate optimal recoveries. These checks supplement rather than replace the general proof. ([evidence](campaigns/minimum-hitting-set-set-cover/work/verification.md))
- **Formal certification and maintainer acceptance: Pending / not performed.** No Lean certification, human expert acceptance, or upstream integration is recorded. The executable contract defines exact optimization outputs; no separate thresholded CLI is specified. ([evidence](campaigns/minimum-hitting-set-set-cover/state.md))

## Reproduce

Run from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/minimum-hitting-set-set-cover/work/check.py --self-test
uv run --locked python campaigns/minimum-hitting-set-set-cover/work/check.py --candidate campaigns/minimum-hitting-set-set-cover/work/algorithm.py
uv run --locked python campaigns/minimum-hitting-set-set-cover/work/verify.py --candidate campaigns/minimum-hitting-set-set-cover/work/algorithm.py
uv run --locked python campaigns/minimum-hitting-set-set-cover/rounds/002/large_sparse.py
uv run --locked python campaigns/minimum-hitting-set-set-cover/reviews/followup/check_sparse.py
```

The finite checks execute construction and recovery. The unbounded claim rests on the written proof.

## Artifacts

- [Fixed question](campaigns/minimum-hitting-set-set-cover/question.md)
- [Campaign state](campaigns/minimum-hitting-set-set-cover/state.md)
- [Manuscript](campaigns/minimum-hitting-set-set-cover/work/manuscript.pdf)
- [Construction and recovery](campaigns/minimum-hitting-set-set-cover/work/algorithm.py)
- [General proof](campaigns/minimum-hitting-set-set-cover/work/proof.md)
- [Independent review](campaigns/minimum-hitting-set-set-cover/reviews/followup/review.md)
- [Verification evidence](campaigns/minimum-hitting-set-set-cover/work/verification.md)

## Scope

The registered independent agent review advanced the exact optimization result to expert review. The board records it as a submitted solution. The incidence theorem is established prior work, and the separately mentioned thresholded feasibility interface has no executable endpoint definition in the fixed question. No human certification or publication priority claim is made.
