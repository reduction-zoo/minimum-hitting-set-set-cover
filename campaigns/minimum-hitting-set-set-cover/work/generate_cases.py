"""Fixed source corpus, derived without reference to any reduction."""

import json
import random
from pathlib import Path


EDGES = [
    {"universe_size": 0, "sets": []},
    {"universe_size": 1, "sets": []},
    {"universe_size": 0, "sets": [[]]},
    {"universe_size": 1, "sets": [[]]},
    {"universe_size": 1, "sets": [[0]]},
    {"universe_size": 2, "sets": [[0], [1]]},
    {"universe_size": 2, "sets": [[0, 1]]},
    {"universe_size": 2, "sets": [[0], [0]]},
    {"universe_size": 3, "sets": [[0], [1], [2]]},
    {"universe_size": 3, "sets": [[0, 1], [1, 2]]},
    {"universe_size": 3, "sets": [[0, 1], [0, 1]]},
    {"universe_size": 4, "sets": [[0], [1, 2], [1, 2]]},
]


def random_case(seed):
    rng = random.Random(seed)
    n = rng.randrange(1, 8)
    m = rng.randrange(1, 9)
    return {
        "universe_size": n,
        "sets": [[u for u in range(n) if rng.randrange(2)] for _ in range(m)],
    }


def main():
    from check import source_optimum

    cases = [{"source": source, "kind": "edge"} for source in EDGES]
    seen = {json.dumps(source, sort_keys=True) for source in EDGES}
    seed = 0
    while len(cases) < 120:
        source = random_case(seed)
        key = json.dumps(source, sort_keys=True)
        if key not in seen:
            cases.append({"source": source, "kind": "random", "seed": seed})
            seen.add(key)
        seed += 1
    for case in cases:
        case["expected"] = source_optimum(case["source"])
    Path(__file__).with_name("cases.json").write_text(json.dumps(cases, indent=2) + "\n")


if __name__ == "__main__":
    main()
