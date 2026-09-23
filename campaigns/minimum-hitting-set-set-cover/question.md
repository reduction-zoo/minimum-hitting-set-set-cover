# Fixed question

```json
{
  "source": "Minimum Hitting Set",
  "target": "Minimum Set Cover",
  "category": "Construction open",
  "summary": "This direct solver route connects two standard covering interfaces while preserving exact optima and infeasible instances.",
  "source_definition": "Given an explicit universe and family of subsets, return a smallest set of universe elements meeting every member, or NO-SOLUTION if no hitting set exists.",
  "target_definition": "Given an explicit universe and indexed family of subsets with unit costs, return a smallest subfamily covering the universe, or NO-SOLUTION if the universe cannot be covered. Repeated sets and empty sets are permitted.",
  "required_result": "Give deterministic polynomial-time F and G such that every valid target output decodes to a valid source output. For the stated optimization endpoints, valid outputs are globally optimal solutions, including all ties. For the thresholded feasibility endpoints, include NO-SOLUTION exactly when infeasible. Prove polynomial runtime and encoding-size bounds and implement the complete rule.",
  "acceptance": "Deliver executable instance construction and output recovery, a general proof covering all legal inputs and target outputs, and worst-case polynomial time and encoding-size bounds. Cite the actual proof used, or identify a newly derived argument. Check small positive and negative instances with independent solvers; finite tests alone do not establish correctness.",
  "importance": "This direct solver route connects two standard covering interfaces while preserving exact optima and infeasible instances.",
  "difficulty": "Low mathematical difficulty: incidence transposition gives a direct correspondence of feasible selections and their cardinalities. Implementation must preserve empty families, empty members, repeated sets and objective values without narrowing the legal domain.",
  "openness": "The incidence-transpose construction and recovery are already described in the cited source. The remaining task is a correct executable rule with objective encodings covering the full declared source domain; no new combinatorial theorem is claimed.",
  "literature_checked": "2026-09-18",
  "coverage": "Import inventory review of the cited sources. Primary proofs have not been independently re-audited; availability of a complete reconstruction elsewhere remains unassessed.",
  "references": [
    {
      "title": "Problem-Reductions: Minimum Hitting Set \u2192 Minimum Set Cover",
      "url": "https://github.com/CodingThrust/problem-reductions/issues/1094",
      "note": "Issue and review discussion checked on 2026-09-18. The exact endpoint semantics and remaining deliverable are stated in this record."
    }
  ],
  "solutions": [],
  "equation": ""
}
```
