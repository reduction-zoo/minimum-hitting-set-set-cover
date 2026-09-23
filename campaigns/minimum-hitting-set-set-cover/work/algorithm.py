"""Incidence transpose: minimum hitting set to minimum set cover."""

import json
import sys

sys.set_int_max_str_digits(0)


def forward(source):
    members = [set(member) for member in source["sets"]]
    active = sorted(set().union(*members))
    return {
        "universe_size": len(members),
        "sets": [[j for j, member in enumerate(members) if u in member]
                 for u in active],
    }


def extract(payload):
    solution = payload["target_solution"]
    if solution == "NO-SOLUTION":
        return solution
    active = sorted(set().union(*(set(member) for member in payload["source"]["sets"])))
    return {"selected": [active[i] for i in solution["selected"]]}


if __name__ == "__main__":
    try:
        value = json.load(sys.stdin)
        print(json.dumps(extract(value) if sys.argv[1:] == ["--extract"] else forward(value)))
    except (KeyError, TypeError, ValueError, IndexError) as error:
        print(f"invalid input: {error}", file=sys.stderr)
        sys.exit(1)
