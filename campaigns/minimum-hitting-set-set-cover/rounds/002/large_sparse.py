"""End-to-end sparse-universe cases whose decimal n is much larger than incidence data."""

import itertools
import json
from pathlib import Path
import subprocess
import sys


sys.set_int_max_str_digits(0)
CANDIDATE = Path(__file__).resolve().parents[2] / "work/algorithm.py"


def run(value, extract=False):
    result = subprocess.run(
        [sys.executable, str(CANDIDATE)] + (["--extract"] if extract else []),
        input=json.dumps(value), text=True, capture_output=True, check=True,
    )
    return json.loads(result.stdout), len(result.stdout)


def target_answers(target):
    assert type(target["universe_size"]) is int
    assert target["universe_size"] >= 0
    assert all(len(set(s)) == len(s) and all(type(j) is int and 0 <= j < target["universe_size"] for j in s) for s in target["sets"])
    count = len(target["sets"])
    assert count <= 4, "sparse source must produce a compact target"
    for size in range(count + 1):
        answers = [
            {"selected": list(choice)}
            for choice in itertools.combinations(range(count), size)
            if all(any(j in target["sets"][i] for i in choice) for j in range(target["universe_size"]))
        ]
        if answers:
            return answers
    return ["NO-SOLUTION"]


def main():
    huge = 10 ** 5000
    cases = [
        ({"universe_size": 100000, "sets": [[99999]]}, {"selected": [99999]}),
        ({"universe_size": huge, "sets": [[huge - 1]]}, {"selected": [huge - 1]}),
        ({"universe_size": huge, "sets": []}, {"selected": []}),
        ({"universe_size": huge, "sets": [[]]}, "NO-SOLUTION"),
    ]
    outputs = 0
    for source, expected in cases:
        target, length = run(source)
        assert length <= 3 * len(json.dumps(source)), "target expansion exceeds sparse-input bound"
        for answer in target_answers(target):
            recovered, _ = run({"source": source, "target_solution": answer}, True)
            assert recovered == expected, (source, target, answer, recovered)
            outputs += 1
    print(f"large sparse check passed: {len(cases)} source instances, {outputs} target outputs")


if __name__ == "__main__":
    main()
