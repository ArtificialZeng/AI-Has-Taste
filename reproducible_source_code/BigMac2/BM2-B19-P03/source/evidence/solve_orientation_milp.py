#!/usr/bin/env python3
"""Seek an exact feasible orientation via SciPy/HiGHS mixed-integer solving.

The solver is used only to discover a candidate.  A rounded candidate is
written solely after exact integer replay of every constraint in the supplied
incidence file; publication evidence must additionally replay the graph and
cycle census independently.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("instance", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--time", type=float, default=300.0)
    args = ap.parse_args()
    tokens = [int(x) for x in args.instance.read_text().split()]
    it = iter(tokens)
    vertices, constraints = next(it), next(it)
    rows: list[int] = []
    cols: list[int] = []
    data: list[int] = []
    lower: list[float] = []
    upper: list[float] = []

    # Exactly one of the three choices at each vertex.
    for v in range(vertices):
        row = len(lower)
        for typ in range(3):
            rows.append(row); cols.append(3 * v + typ); data.append(1)
        lower.append(1.0); upper.append(1.0)

    parsed: list[tuple[int, list[tuple[int, int]]]] = []
    for _ in range(constraints):
        required, length = next(it), next(it)
        items = [(next(it), next(it)) for _ in range(length)]
        parsed.append((required, items))
        row = len(lower)
        for v, typ in items:
            rows.append(row); cols.append(3 * v + typ); data.append(1)
        lower.append(float(required)); upper.append(np.inf)
    try:
        next(it)
        raise RuntimeError("trailing instance tokens")
    except StopIteration:
        pass

    matrix = coo_matrix((data, (rows, cols)), shape=(len(lower), 3 * vertices)).tocsr()
    result = milp(
        c=np.zeros(3 * vertices),
        integrality=np.ones(3 * vertices),
        bounds=Bounds(np.zeros(3 * vertices), np.ones(3 * vertices)),
        constraints=LinearConstraint(matrix, np.array(lower), np.array(upper)),
        options={"time_limit": args.time, "presolve": True, "disp": True},
    )
    print(json.dumps({
        "success": bool(result.success),
        "status": int(result.status),
        "message": str(result.message),
        "has_incumbent": result.x is not None,
    }, sort_keys=True))
    if result.x is None:
        return
    rounded = np.rint(result.x).astype(int)
    choices: list[int] = []
    for v in range(vertices):
        selected = [t for t in range(3) if rounded[3 * v + t] == 1]
        if len(selected) != 1:
            raise RuntimeError(f"rounded incumbent is not one-hot at vertex {v}")
        choices.append(selected[0])
    margins = []
    for required, items in parsed:
        count = sum(choices[v] == typ for v, typ in items)
        if count < required:
            raise RuntimeError("rounded incumbent fails an exact constraint")
        margins.append(count - required)
    payload = {
        "schema": "orientation-choice-candidate-v1",
        "instance": args.instance.as_posix(),
        "instance_sha256": hashlib.sha256(args.instance.read_bytes()).hexdigest(),
        "choices": choices,
        "choices_sha256": hashlib.sha256(bytes(choices)).hexdigest(),
        "exact_replay": {
            "vertices": vertices,
            "constraints": constraints,
            "minimum_margin": min(margins),
            "tight_constraints": sum(x == 0 for x in margins),
        },
        "solver_status": int(result.status),
        "solver_message": str(result.message),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in payload.items() if k != "choices"}, sort_keys=True))


if __name__ == "__main__":
    main()
