"""Independent Z3 oracles and observable-output checks for both problems."""

import argparse
import itertools
import json
from pathlib import Path
import subprocess
import sys

import z3


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def legal(instance):
    n = instance["universe_size"]
    return type(n) is int and n >= 0 and all(
        len(set(s)) == len(s) and all(type(i) is int and 0 <= i < n for i in s)
        for s in instance["sets"]
    )


def feasible(instance, chosen, role):
    n, sets = instance["universe_size"], instance["sets"]
    limit = n if role == "source" else len(sets)
    if not isinstance(chosen, list) or any(type(i) is not int or i < 0 or i >= limit for i in chosen) or len(set(chosen)) != len(chosen):
        return False
    if role == "source":
        return all(any(i in chosen for i in s) for s in sets)
    return all(any(u in sets[i] for i in chosen) for u in range(n))


def optimum(instance, role):
    assert legal(instance)
    n, sets = instance["universe_size"], instance["sets"]
    count = n if role == "source" else len(sets)
    variables = [z3.Bool(f"v_{i}") for i in range(count)]
    solver = z3.Optimize()
    if role == "source":
        for member in sets:
            solver.add(z3.Or([variables[i] for i in member]))
    else:
        for u in range(n):
            solver.add(z3.Or([variables[i] for i, s in enumerate(sets) if u in s]))
    solver.minimize(z3.Sum([z3.If(v, 1, 0) for v in variables] + [z3.IntVal(0)]))
    result = solver.check()
    if result == z3.unsat:
        return None
    if result != z3.sat:
        raise RuntimeError(f"inconclusive Z3 result: {result}")
    selected = [i for i, v in enumerate(variables) if z3.is_true(solver.model().eval(v))]
    assert feasible(instance, selected, role)
    return len(selected)


def source_optimum(instance):
    return optimum(instance, "source")


def target_optimum(instance):
    return optimum(instance, "target")


def valid_output(instance, output, role, expected=None):
    if expected is None:
        expected = optimum(instance, role)
    if expected is None:
        return output == "NO-SOLUTION"
    return type(output) is dict and set(output) == {"selected"} and feasible(instance, output["selected"], role) and len(output["selected"]) == expected


def all_valid_outputs(instance, role, expected):
    if expected is None:
        return ["NO-SOLUTION"]
    count = instance["universe_size"] if role == "source" else len(instance["sets"])
    return [{"selected": list(choice)} for choice in itertools.combinations(range(count), expected) if feasible(instance, list(choice), role)]


def exhaustive_optimum(instance, role):
    count = instance["universe_size"] if role == "source" else len(instance["sets"])
    for size in range(count + 1):
        if any(feasible(instance, list(choice), role) for choice in itertools.combinations(range(count), size)):
            return size
    return None


def run_candidate(candidate, payload, extract=False):
    command = [sys.executable, str(candidate)] + (["--extract"] if extract else [])
    result = subprocess.run(command, input=json.dumps(payload), text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def self_test():
    subprocess.run([sys.executable, str(ROOT / "research/validate_preparation.py"), str(HERE / "cases.json")], check=True)
    from generate_cases import EDGES, random_case

    cases = json.loads((HERE / "cases.json").read_text())
    assert [c["source"] for c in cases[:len(EDGES)]] == EDGES
    for case in cases:
        source = case["source"]
        if case["kind"] == "random":
            assert source == random_case(case["seed"])
        assert legal(source)
        expected = source_optimum(source)
        assert case["expected"] == expected
        assert exhaustive_optimum(source, "source") == expected
        outputs = all_valid_outputs(source, "source", expected)
        assert outputs and all(valid_output(source, y, "source", expected) for y in outputs)
        if expected is None:
            assert not valid_output(source, {"selected": []}, "source", expected)
        else:
            assert not valid_output(source, "NO-SOLUTION", "source", expected)
            assert not valid_output(source, {"selected": list(range(source["universe_size"]))}, "source", expected) or expected == source["universe_size"]
            assert not valid_output(source, {"selected": [-1]}, "source", expected)
    source_examples = [({"universe_size": 0, "sets": []}, 0), ({"universe_size": 0, "sets": [[]]}, None), ({"universe_size": 2, "sets": [[0], [1]]}, 2), ({"universe_size": 2, "sets": [[0, 1]]}, 1)]
    target_examples = [({"universe_size": 0, "sets": [[]]}, 0), ({"universe_size": 1, "sets": [[]]}, None), ({"universe_size": 2, "sets": [[0], [1]]}, 2), ({"universe_size": 2, "sets": [[0, 1]]}, 1)]
    for instance, expected in source_examples:
        assert source_optimum(instance) == expected
    for instance, expected in target_examples:
        assert target_optimum(instance) == expected
        assert exhaustive_optimum(instance, "target") == expected
        if expected is None:
            assert not valid_output(instance, {"selected": []}, "target", expected)
        else:
            assert not valid_output(instance, "NO-SOLUTION", "target", expected)
            assert not valid_output(instance, {"selected": [-1]}, "target", expected)
    assert not valid_output({"universe_size": 2, "sets": [[0, 1], [0, 1]]}, {"selected": [0, 1]}, "target", 1)
    assert not valid_output({"universe_size": 2, "sets": [[0, 1]]}, {"selected": [0, 0]}, "source", 1)
    print(f"self-test passed: {len(cases)} source cases; Z3 {z3.get_version_string()}")


def candidate_test(candidate):
    cases = json.loads((HERE / "cases.json").read_text())
    output_count = 0
    for case in cases:
        source = case["source"]
        target = run_candidate(candidate, source)
        assert legal(target), (source, target)
        target_best = target_optimum(target)
        for target_output in all_valid_outputs(target, "target", target_best):
            assert valid_output(target, target_output, "target", target_best)
            recovered = run_candidate(candidate, {"source": source, "target_solution": target_output}, True)
            assert valid_output(source, recovered, "source", case["expected"]), (source, target, target_output, recovered)
            output_count += 1
    print(f"candidate passed: {len(cases)} source instances, {output_count} target outputs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test", action="store_true")
    group.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    self_test() if args.self_test else candidate_test(args.candidate.resolve())
