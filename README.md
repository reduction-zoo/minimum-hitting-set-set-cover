# Minimum Hitting Set → Minimum Set Cover

Independent research campaign. A deterministic polynomial-time JSON reduction from exact Minimum Hitting Set to exact Minimum Set Cover is implemented and independently reviewed. The incidence duality is known; the result here is a full-domain executable adapter with a size bound that respects the compact decimal universe encoding. Status: `ready_for_expert_review` (agent assessment, not human certification).

[State](campaigns/minimum-hitting-set-set-cover/state.md) · [Question](campaigns/minimum-hitting-set-set-cover/question.md) · [Proof](campaigns/minimum-hitting-set-set-cover/work/proof.md) · [Reviewed paper](campaigns/minimum-hitting-set-set-cover/work/manuscript.pdf) · [Review](campaigns/minimum-hitting-set-set-cover/reviews/followup/review.md)

Reproduce from this repository root:

```sh
uv sync --locked
uv run python campaigns/minimum-hitting-set-set-cover/work/check.py --self-test
uv run python campaigns/minimum-hitting-set-set-cover/work/check.py --candidate campaigns/minimum-hitting-set-set-cover/work/algorithm.py
uv run python campaigns/minimum-hitting-set-set-cover/work/verify.py --candidate campaigns/minimum-hitting-set-set-cover/work/algorithm.py
uv run python campaigns/minimum-hitting-set-set-cover/rounds/002/large_sparse.py
uv run python campaigns/minimum-hitting-set-set-cover/reviews/followup/check_sparse.py
```

The executable contract defines exact optimization outputs. A same-threshold feasibility equivalence follows from the proof, but no thresholded CLI is defined by the fixed endpoint descriptions. No large-instance target solver performance was measured.

Board source commit: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.
