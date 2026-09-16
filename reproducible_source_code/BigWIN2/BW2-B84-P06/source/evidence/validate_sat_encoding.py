#!/usr/bin/env python3
"""Planted-instance cross-checks for systematic_sat_search.py.

The fixed matrix is Equation (3)'s 11-column G', with its four non-normalized
parity columns scaled by 2 and its parity columns reordered to satisfy the
CNF's justified row-1 convention.  An independent kernel-word enumeration
computes the exact nontrivial packing number for every target.  Single-target
CNFs must be SAT exactly when that packing number is at least three.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path

from pysat.solvers import Solver

from systematic_sat_search import K, N, P, build_encoding


FIXED_A = [
    [1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
]


def kernel_supports() -> list[set[int]]:
    supports = [set() for _ in range(N)]
    # One representative of every projective direction in F_3^5.
    directions = [
        x
        for x in product(range(P), repeat=5)
        if x != (0,) * 5 and next(value for value in x if value) == 1
    ]
    for x in directions:
        left = [
            -sum(FIXED_A[row][col] * x[col] for col in range(5)) % P
            for row in range(K)
        ]
        word = left + list(x)
        support = sum((value != 0) << col for col, value in enumerate(word))
        for target, value in enumerate(word):
            if value:
                supports[target].add(support ^ (1 << target))
    return supports


def packing_number(masks: set[int]) -> int:
    ordered = sorted(masks, key=lambda mask: (mask.bit_count(), mask))
    minimal: list[int] = []
    for mask in ordered:
        if not any(previous & mask == previous for previous in minimal):
            minimal.append(mask)
    states = {0: 0}
    for mask in minimal:
        for used, count in list(states.items()):
            if not used & mask:
                states[used | mask] = max(states.get(used | mask, 0), count + 1)
    return max(states.values(), default=0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    exact_packings = [packing_number(masks) for masks in kernel_supports()]
    cnf_statuses = []
    for target in range(N):
        enc, _, _ = build_encoding(active_targets=(target,), fixed_a=FIXED_A)
        with Solver(name=args.solver, bootstrap_with=enc.cnf.clauses) as solver:
            cnf_statuses.append("SAT" if solver.solve() else "UNSAT")
    expected_statuses = ["SAT" if packing >= 3 else "UNSAT" for packing in exact_packings]
    accepted = exact_packings == [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
    accepted = accepted and cnf_statuses == expected_statuses
    report = {
        "provenance": "win-00084-p06-research-3dd502da7309",
        "fixed_matrix": "normalized and reordered Equation (3) G' with one parity copy",
        "fixed_a_rows_mod_3": FIXED_A,
        "independent_kernel_max_nontrivial_packings": exact_packings,
        "single_target_cnf_statuses": cnf_statuses,
        "expected_single_target_statuses": expected_statuses,
        "solver": args.solver,
        "accepted": accepted,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    raise SystemExit(0 if accepted else 1)


if __name__ == "__main__":
    main()
