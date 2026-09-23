"""Independent subprocess check of sparse, long-integer recovery."""

import itertools
import json
from pathlib import Path
import subprocess
import sys

sys.set_int_max_str_digits(0)
ALGORITHM = Path(__file__).resolve().parents[2] / "work/algorithm.py"


def run(value, extract=False):
    result = subprocess.run(
        [sys.executable, str(ALGORITHM)] + (["--extract"] if extract else []),
        input=json.dumps(value), text=True, capture_output=True, check=True,
    )
    return json.loads(result.stdout), len(result.stdout)


def target_optima(instance):
    count = len(instance["sets"])
    assert count <= 3
    for size in range(count + 1):
        answers = []
        for selected in itertools.combinations(range(count), size):
            valid = all(any(j in instance["sets"][i] for i in selected)
                        for j in range(instance["universe_size"]))
            if valid:
                answers.append({"selected": list(selected)})
        if answers:
            return answers
    return ["NO-SOLUTION"]


def main():
    n = 10 ** 5000
    cases = [
        ({"universe_size": n, "sets": [[n - 2, n - 1], [n - 1], [17, n - 2]]},
         [{"selected": [17, n - 1]}, {"selected": [n - 2, n - 1]}]),
        ({"universe_size": n, "sets": []}, [{"selected": []}]),
        ({"universe_size": n, "sets": [[]]}, ["NO-SOLUTION"]),
    ]
    checked = 0
    for source, expected in cases:
        target, length = run(source)
        assert length < len(json.dumps(source))
        assert target["universe_size"] == len(source["sets"])
        assert all(len(set(member)) == len(member) and
                   all(0 <= j < target["universe_size"] for j in member)
                   for member in target["sets"])
        answers = target_optima(target)
        recovered = [run({"source": source, "target_solution": answer}, True)[0]
                     for answer in answers]
        assert sorted(recovered, key=str) == sorted(expected, key=str)
        checked += len(answers)
    print(f"review sparse check passed: {len(cases)} sources, {checked} target optima")


if __name__ == "__main__":
    main()
