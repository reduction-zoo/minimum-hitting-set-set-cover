# Campaign state

Budget: 20 rounds. Used: 2. Remaining: 18. Distinct mechanisms: 2.
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

Capability probe (2026-09-23, local macOS): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at `/opt/homebrew/bin/z3`; Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; CP-SAT executable absent; cvc5 and MiniSat absent. Z3 Python binding 4.16.0.0 locked in `uv.lock` for Prepare. Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.0 and Lake 5.0.0 at `/opt/homebrew/bin`; Mathlib project/cache not found locally (pending if formalization requested). External `sci-brain:how-to-technical-writing` skill available at `/Users/xiweipan/.codex/plugins/cache/sci-brain/sci-brain/0.5.0/skills/how-to-technical-writing/SKILL.md`.
Prepare: [120 fixed cases and independent oracles](work/preparation.md), committed as `4f4eee4`.
Current claim: [initial review](reviews/initial/review.md) requires sparse-universe repair; the first map fails polynomial size under the decimal universe-size encoding. The finite [prepared and independent checks](work/verification.md) still support the incidence correspondence. Mathematical novelty is limited by the cited existing issue and Cygan et al. 2015.
Next action: execute round 002's targeted failing test, repair, and focused re-review.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Incidence transpose with exact-optimum recovery | Empty member and empty family, then all prepared optima | Supported | [round](rounds/001/round.md) |
| 002 | Active-element transpose to avoid sparse-universe expansion | Large sparse universe, selected nonzero index, empty family/member | In progress | [round](rounds/002/round.md) |
