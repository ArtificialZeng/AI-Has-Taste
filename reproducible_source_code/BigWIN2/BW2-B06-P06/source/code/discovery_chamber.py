#!/usr/bin/env python3
"""Floating-point discovery for the exact chamber-dual reduction.

This program is diagnostic only.  A separate exact serializer and verifier
must certify any decisive finite result.
"""

from __future__ import annotations

import argparse
import itertools
import json
import platform
import sys
from fractions import Fraction

import numpy as np
import scipy
from scipy.optimize import linprog


def ball_rows_fraction(n: int) -> list[list[list[Fraction]]]:
    """Rows mapping edge differences d to centered-ball averages of z.

    Vertices are zero based, z[0]=0, and z[j]=sum(d[:j]).
    Duplicate balls are omitted (there are eccentricity+1 distinct balls).
    """
    rows: list[list[list[Fraction]]] = []
    for i in range(n):
        vertex_rows: list[list[Fraction]] = []
        for radius in range(max(i, n - 1 - i) + 1):
            left = max(0, i - radius)
            right = min(n - 1, i + radius)
            size = right - left + 1
            row = []
            for edge in range(n - 1):
                count = max(0, right - max(left, edge + 1) + 1)
                row.append(Fraction(count, size))
            if not vertex_rows or row != vertex_rows[-1]:
                vertex_rows.append(row)
        rows.append(vertex_rows)
    return rows


def sign_coefficients(signs: tuple[int, ...]) -> tuple[int, ...]:
    n = len(signs) + 1
    return (signs[0],) + tuple(
        signs[i] - signs[i - 1] for i in range(1, n - 1)
    ) + (-signs[-1],)


def solve_dual_float(
    rows_q: list[list[list[Fraction]]],
    coeffs: tuple[int, ...],
    positive_radii: tuple[int, ...],
) -> tuple[float, np.ndarray]:
    """Solve the dual Chebyshev LP for one chamber."""
    n = len(rows_q)
    positive = [i for i, c in enumerate(coeffs) if c > 0]
    negative = [i for i, c in enumerate(coeffs) if c < 0]
    rows = [[np.array([float(x) for x in row]) for row in rs] for rs in rows_q]

    p = np.zeros(n - 1)
    for i, radius in zip(positive, positive_radii):
        p += coeffs[i] * rows[i][radius]

    offsets: dict[int, tuple[int, int]] = {}
    cursor = 0
    for i in negative:
        offsets[i] = (cursor, cursor + len(rows[i]))
        cursor += len(rows[i])
    t_index = cursor
    variables = cursor + 1

    a_eq = np.zeros((len(negative), variables))
    b_eq = np.zeros(len(negative))
    for eq, i in enumerate(negative):
        start, stop = offsets[i]
        a_eq[eq, start:stop] = 1.0
        b_eq[eq] = -coeffs[i]

    a_ub = np.zeros((2 * (n - 1), variables))
    b_ub = np.zeros(2 * (n - 1))
    for edge in range(n - 1):
        for i in negative:
            start, stop = offsets[i]
            column = np.array([row[edge] for row in rows[i]])
            a_ub[2 * edge, start:stop] = -column
            a_ub[2 * edge + 1, start:stop] = column
        a_ub[2 * edge, t_index] = -1.0
        a_ub[2 * edge + 1, t_index] = -1.0
        b_ub[2 * edge] = -p[edge]
        b_ub[2 * edge + 1] = p[edge]

    objective = np.zeros(variables)
    objective[t_index] = 1.0
    result = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, None)] * variables,
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.fun), result.x


def enumerate_all(n: int) -> dict[str, object]:
    rows = ball_rows_fraction(n)
    best = -1.0
    best_record: dict[str, object] | None = None
    chambers = 0
    for signs in itertools.product((-1, 1), repeat=n - 1):
        coeffs = sign_coefficients(signs)
        positive = [i for i, c in enumerate(coeffs) if c > 0]
        radius_ranges = [range(len(rows[i])) for i in positive]
        for radii in itertools.product(*radius_ranges):
            value, _ = solve_dual_float(rows, coeffs, radii)
            chambers += 1
            if value > best:
                best = value
                best_record = {
                    "signs": signs,
                    "coefficients": coeffs,
                    "positive_vertices": positive,
                    "positive_radii": radii,
                    "value": value,
                }
    return {
        "n": n,
        "chambers": chambers,
        "maximum": best,
        "conjectured": 1.0 - 1.0 / n,
        "best_record": best_record,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
    }


def maximal_direct(x: np.ndarray) -> np.ndarray:
    n = len(x)
    answer = np.empty(n)
    for i in range(n):
        averages = []
        for radius in range(max(i, n - 1 - i) + 1):
            left = max(0, i - radius)
            right = min(n, i + radius + 1)
            averages.append(float(np.mean(x[left:right])))
        answer[i] = max(averages)
    return answer


def randomized_reduction_test(n: int, trials: int, seed: int) -> dict[str, object]:
    rng = np.random.default_rng(seed)
    rows = ball_rows_fraction(n)
    largest_gap = 0.0
    for _ in range(trials):
        z = rng.normal(size=n)
        z -= z[0]
        y_direct = maximal_direct(z)
        d = np.diff(z)
        y_rows = np.array([
            max(float(sum(a * Fraction.from_float(float(v)) for a, v in zip(row, d)))
                for row in vertex_rows)
            for vertex_rows in rows
        ])
        largest_gap = max(largest_gap, float(np.max(np.abs(y_direct - y_rows))))
    return {"n": n, "trials": trials, "seed": seed, "largest_gap": largest_gap}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--random-tests", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260830)
    args = parser.parse_args()
    payload = {
        "reduction_test": randomized_reduction_test(args.n, args.random_tests, args.seed),
        "enumeration": enumerate_all(args.n),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
