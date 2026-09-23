"""Incidence transpose: minimum hitting set to minimum set cover."""

import json
import sys


def forward(source):
    members = [set(member) for member in source["sets"]]
    return {
        "universe_size": len(members),
        "sets": [[j for j, member in enumerate(members) if u in member]
                 for u in range(source["universe_size"])],
    }


def extract(payload):
    solution = payload["target_solution"]
    if solution == "NO-SOLUTION":
        return solution
    return {"selected": solution["selected"]}


if __name__ == "__main__":
    try:
        value = json.load(sys.stdin)
        print(json.dumps(extract(value) if sys.argv[1:] == ["--extract"] else forward(value)))
    except (KeyError, TypeError, ValueError, IndexError) as error:
        print(f"invalid input: {error}", file=sys.stderr)
        sys.exit(1)
