#!/usr/bin/env python3
"""Adversarial finite checks for the owner-context two-level proof candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ortools.sat.python import cp_model

from block_allocation import canonical_two_level_allocation, two_level_rho
from cds_search import cells, corner_rho


def fixed_quota_coloring_exists(a: int, p: int, b: int, q: int) -> bool:
    shape = (a,) * p + (b,) * q
    target, quotas = canonical_two_level_allocation(a, p, b, q)
    board = cells(shape)
    model = cp_model.CpModel()
    variables: dict[tuple[int, int, int], cp_model.IntVar] = {}
    for i, j in board:
        for color in range(len(target)):
            variables[i, j, color] = model.new_bool_var(f"x_{i}_{j}_{color}")
        model.add_exactly_one(variables[i, j, color] for color in range(len(target)))
    for i, row_length in enumerate(shape):
        for color in range(len(target)):
            model.add_at_most_one(
                variables[i, j, color] for j in range(row_length)
            )
    for j in range(a):
        incident_rows = [i for i, row_length in enumerate(shape) if j < row_length]
        for color in range(len(target)):
            model.add_at_most_one(
                variables[i, j, color] for i in incident_rows
            )
    for color, (top_left, top_right, bottom_left) in enumerate(quotas):
        model.add(
            sum(variables[i, j, color] for i in range(p) for j in range(b))
            == top_left
        )
        model.add(
            sum(variables[i, j, color] for i in range(p) for j in range(b, a))
            == top_right
        )
        model.add(
            sum(
                variables[i, j, color]
                for i in range(p, p + q)
                for j in range(b)
            )
            == bottom_left
        )
    for attempt in range(3):
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 5.0
        solver.parameters.num_search_workers = 1
        solver.parameters.random_seed = 3402002 + attempt
        status = solver.solve(model)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return True
        if status == cp_model.INFEASIBLE:
            return False
    return False


def main() -> int:
    formula_cases = formula_prefixes = quota_cases = cell_cases = 0
    for a in range(2, 13):
        for b in range(1, a):
            for p in range(1, 9):
                for q in range(1, 9):
                    shape = (a,) * p + (b,) * q
                    canonical_two_level_allocation(a, p, b, q)
                    quota_cases += 1
                    for k in range(max(a, p + q) + 1):
                        if two_level_rho(a, p, b, q, k) != corner_rho(shape, k):
                            raise AssertionError(
                                f"six-line formula failed for {(a, p, b, q)}, k={k}"
                            )
                        formula_prefixes += 1
                    formula_cases += 1
    for a in range(2, 8):
        for b in range(1, a):
            for p in range(1, 6):
                for q in range(1, 6):
                    if not fixed_quota_coloring_exists(a, p, b, q):
                        raise AssertionError(
                            f"fixed-quota lift failed for {(a, p, b, q)}"
                        )
                    cell_cases += 1
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(
        json.dumps(
            {
                "status": "verified",
                "six_line_parameter_cases": formula_cases,
                "six_line_prefix_equalities": formula_prefixes,
                "canonical_quota_cases": quota_cases,
                "fixed_quota_cell_colorings": cell_cases,
                "script_sha256": script_hash,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
