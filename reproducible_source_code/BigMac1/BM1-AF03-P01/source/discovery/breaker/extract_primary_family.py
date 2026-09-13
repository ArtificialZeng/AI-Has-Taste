#!/usr/bin/env python3
"""Extract primary x_E values from a CaDiCaL competition witness."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("witness", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.n not in (8, 9, 10):
        raise SystemExit("n must be in {8,9,10}")
    lines = args.witness.read_text(encoding="ascii").splitlines()
    status_lines = [line for line in lines if line.startswith("s ")]
    if status_lines != ["s SATISFIABLE"]:
        raise SystemExit(f"expected exactly one SAT status, got {status_lines!r}")
    tokens: list[int] = []
    for line in lines:
        if line.startswith("v "):
            try:
                tokens.extend(int(token) for token in line.split()[1:])
            except ValueError as exc:
                raise SystemExit(f"noninteger witness token: {exc}") from exc
    if not tokens or tokens[-1] != 0 or 0 in tokens[:-1]:
        raise SystemExit("witness must contain one final zero")
    assignments: dict[int, bool] = {}
    for literal in tokens[:-1]:
        variable = abs(literal)
        if variable in assignments:
            raise SystemExit(f"duplicate assignment for variable {variable}")
        assignments[variable] = literal > 0
    edges = list(itertools.combinations(range(1, args.n + 1), 4))
    missing = [variable for variable in range(1, len(edges) + 1) if variable not in assignments]
    if missing:
        raise SystemExit(f"primary assignments missing, starting with {missing[:5]}")
    family = [
        list(edge)
        for variable, edge in enumerate(edges, 1)
        if assignments[variable]
    ]
    args.output.write_text(
        json.dumps({"n": args.n, "family": family}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"n": args.n, "family_size": len(family)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
