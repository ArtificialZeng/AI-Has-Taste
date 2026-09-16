#!/usr/bin/env python3
"""Verify the two-black-square factorial formulas against the exact census.

The formulas use 1-based coordinates.  A negative factorial term is interpreted
as absent; this convention only handles small dimensions in which the
corresponding block-matching case is impossible.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


Square = tuple[int, int]
Configuration = tuple[Square, Square]


def fact_or_zero(value: int) -> int:
    return math.factorial(value) if value >= 0 else 0


def interval_profile(n: int, low: int, high: int) -> tuple[int, int, int, int]:
    """Return (I4, I_remove_low_right, I_remove_high_left, I2)."""
    a = low - 1
    b = high - low - 1
    c = n - high
    i2 = a * c
    i4 = i2 * (a * b + a * c - a + b * b + b * c - 3 * b - c + 1)
    return i4, i2 * (a + b - 1), i2 * (b + c - 1), i2


def formula_count(n: int, black: Configuration) -> int:
    """Evaluate the exhaustive case formula for a pair of black squares."""
    (r1, c1), (r2, c2) = black

    if r1 == r2 or c1 == c2:
        if c1 == c2:
            return formula_count(n, tuple(sorted(((c1, r1), (c2, r2)))))
        row = r1
        low, high = sorted((c1, c2))
        if row in (1, n):
            special = {(1, 2), (1, n), (n - 1, n)}
            if (low, high) in special:
                return math.factorial(n) - 2 * math.factorial(n - 1)
            return 0
        if 1 < low < high < n and high > low + 1:
            return (
                (low - 1)
                * (high - low - 1)
                * (n - high)
                * (row - 1)
                * (row - 2)
                * (n - row)
                * (n - row - 1)
                * fact_or_zero(n - 5)
            )
        return 0

    interior_columns = sum(1 < col < n for _, col in black)
    interior_rows = sum(1 < row < n for row, _ in black)
    if interior_columns != interior_rows:
        return 0

    if interior_columns == 0:
        return math.factorial(n) - 2 * math.factorial(n - 1) + math.factorial(n - 2)

    if interior_columns == 1:
        corners = [
            square
            for square in black
            if square[0] in (1, n) and square[1] in (1, n)
        ]
        if corners:
            corner_row, corner_col = corners[0]
            row, col = next(
                square for square in black if 1 < square[0] < n and 1 < square[1] < n
            )
            near_col = col - 1 if corner_col == 1 else n - col
            far_col = n - col if corner_col == 1 else col - 1
            near_row = row - 1 if corner_row == 1 else n - row
            far_row = n - row if corner_row == 1 else row - 1
            unrestricted = (
                (col - 1)
                * (n - col)
                * (row - 1)
                * (n - row)
                * fact_or_zero(n - 3)
            )
            forbidden = (
                (near_col - 1)
                * far_col
                * (near_row - 1)
                * far_row
                * fact_or_zero(n - 4)
            )
            return unrestricted - forbidden

        boundary_row, interior_col = next(square for square in black if square[0] in (1, n))
        interior_row, boundary_col = next(square for square in black if square[1] in (1, n))
        col = interior_col if boundary_col == 1 else n + 1 - interior_col
        row = interior_row if boundary_row == 1 else n + 1 - interior_row
        return (n - col) * (n - row) * (
            (col - 2) * (row - 2) * fact_or_zero(n - 3) + math.factorial(n - 2)
        )

    low_row, high_row = sorted((r1, r2))
    low_col, high_col = sorted((c1, c2))
    row_i4, row_u, row_v, row_i2 = interval_profile(n, low_row, high_row)
    col_i4, col_u, col_v, col_i2 = interval_profile(n, low_col, high_col)
    low_row_col = c1 if r1 < r2 else c2
    parallel = low_row_col == low_col
    if parallel:
        one_cross_edge = col_u * row_v + col_v * row_u
    else:
        one_cross_edge = col_u * row_u + col_v * row_v
    return (
        col_i4 * row_i4 * fact_or_zero(n - 6)
        + one_cross_edge * fact_or_zero(n - 5)
        + col_i2 * row_i2 * fact_or_zero(n - 4)
    )


def verify_census(path: Path) -> tuple[int, int]:
    data = json.loads(path.read_text())
    checked_orbits = 0
    checked_configurations = 0
    for result in data["results"]:
        n = result["n"]
        for record in result["orbit_records"]:
            black = tuple(tuple(square) for square in record["representative"])
            actual = formula_count(n, black)
            assert actual == record["count"], (n, black, actual, record["count"])
            checked_orbits += 1
            checked_configurations += record["orbit_size"]
        assert checked_configurations >= sum(
            item["configurations"] for item in data["results"] if item["n"] <= n
        )
    return checked_orbits, checked_configurations


def scan_maxima(min_n: int, max_n: int) -> list[dict[str, object]]:
    """Scan all pairs via the formulas; this is finite evidence, not a proof."""
    output = []
    for n in range(min_n, max_n + 1):
        maximum = -1
        maximizers: list[Configuration] = []
        squares = itertools.product(range(1, n + 1), repeat=2)
        for pair in itertools.combinations(squares, 2):
            value = formula_count(n, pair)
            if value > maximum:
                maximum = value
                maximizers = [pair]
            elif value == maximum:
                maximizers.append(pair)
        output.append(
            {
                "n": n,
                "maximum": maximum,
                "maximizing_configurations": [list(map(list, pair)) for pair in maximizers],
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--census", type=Path, default=Path("evidence/census_n3_n8.json"))
    parser.add_argument("--scan-min-n", type=int)
    parser.add_argument("--scan-max-n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    orbits, configurations = verify_census(args.census)
    print(f"formula verification: {orbits} orbits, {configurations} configurations")
    if args.scan_min_n is not None or args.scan_max_n is not None:
        assert args.scan_min_n is not None and args.scan_max_n is not None and args.output
        scan = scan_maxima(args.scan_min_n, args.scan_max_n)
        args.output.write_text(json.dumps(scan, indent=2) + "\n")
        for item in scan:
            print(
                f"n={item['n']} maximum={item['maximum']} "
                f"maximizing_configurations={len(item['maximizing_configurations'])}"
            )


if __name__ == "__main__":
    main()
