"""Independent exhaustive end-to-end verification over small set systems."""

import argparse
import itertools
import json
from pathlib import Path
import subprocess
import sys


def selections(count):
    for size in range(count + 1):
        for chosen in itertools.combinations(range(count), size):
            yield chosen


def valid_choices(instance, role):
    n, family = instance["universe_size"], instance["sets"]
    count = n if role == "source" else len(family)
    feasible = []
    for chosen in selections(count):
        if role == "source":
            works = all(set(member).intersection(chosen) for member in family)
        else:
            covered = set().union(*(family[i] for i in chosen)) if chosen else set()
            works = len(covered) == n
        if works:
            if feasible and len(chosen) > len(feasible[0]):
                break
            feasible.append(chosen)
    return feasible


def run(candidate, payload, extract=False):
    proc = subprocess.run(
        [sys.executable, str(candidate)] + (["--extract"] if extract else []),
        input=json.dumps(payload), text=True, capture_output=True, check=True,
    )
    return json.loads(proc.stdout)


def main(candidate):
    instances = outputs = infeasible = tied = 0
    for n in range(4):
        possible = [list(s) for size in range(n + 1) for s in itertools.combinations(range(n), size)]
        for m in range(4):
            for family in itertools.product(possible, repeat=m):
                source = {"universe_size": n, "sets": list(family)}
                source_best = valid_choices(source, "source")
                target = run(candidate, source)
                assert isinstance(target, dict) and type(target.get("universe_size")) is int
                assert target["universe_size"] >= 0 and all(
                    isinstance(member, list) and len(member) == len(set(member))
                    and all(type(j) is int and 0 <= j < target["universe_size"] for j in member)
                    for member in target["sets"]
                )
                target_best = valid_choices(target, "target")
                target_outputs = [{"selected": list(s)} for s in target_best] if target_best else ["NO-SOLUTION"]
                for answer in target_outputs:
                    recovered = run(candidate, {"source": source, "target_solution": answer}, True)
                    expected = [{"selected": list(s)} for s in source_best] if source_best else ["NO-SOLUTION"]
                    assert recovered in expected, (source, target, answer, recovered, expected)
                    outputs += 1
                instances += 1
                infeasible += not source_best
                tied += len(target_best) > 1
    print(f"verified {instances} source instances, {outputs} target outputs, {infeasible} infeasible sources, {tied} instances with target ties")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True, type=Path)
    main(parser.parse_args().candidate.resolve())
