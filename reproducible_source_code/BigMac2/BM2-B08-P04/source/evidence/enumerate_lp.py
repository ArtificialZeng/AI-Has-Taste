#!/usr/bin/env python3
"""Exact exhaustive checker using rational convex-feasibility vertices.

For generators a_1,...,a_m and a lattice exponent u, Newton membership is

    exists lambda >= 0: sum(lambda)=1 and sum(lambda_i a_i) <= u.

The feasible set is a rational polytope inside the (m-1)-simplex.  If it is
nonempty it has a vertex.  At a vertex, the sum equation together with m-1
linearly independent active inequalities determines lambda.  This program
enumerates every possible set of m-1 active inequalities and solves the
resulting square systems over fractions.Fraction.  Thus every membership
decision is exact; no floating-point solver is used.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


Exponent = tuple[int, int, int]
Generators = tuple[Exponent, ...]


def solve_square(matrix: list[list[int]], rhs: list[int]) -> list[Fraction] | None:
    """Return the unique exact solution, or None when the matrix is singular."""

    n = len(matrix)
    augmented = [
        [Fraction(entry) for entry in row] + [Fraction(value)]
        for row, value in zip(matrix, rhs, strict=True)
    ]
    rank = 0
    for column in range(n):
        pivot = next(
            (row for row in range(rank, n) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        augmented[rank], augmented[pivot] = augmented[pivot], augmented[rank]
        pivot_value = augmented[rank][column]
        augmented[rank] = [entry / pivot_value for entry in augmented[rank]]
        for row in range(n):
            if row == rank or augmented[row][column] == 0:
                continue
            multiplier = augmented[row][column]
            augmented[row] = [
                entry - multiplier * pivot_entry
                for entry, pivot_entry in zip(
                    augmented[row], augmented[rank], strict=True
                )
            ]
        rank += 1
    if rank != n:
        return None
    return [augmented[row][-1] for row in range(n)]


def in_integral_closure(generators: Generators, exponent: Exponent) -> bool:
    """Decide exponent membership in conv(generators)+R^3_+ exactly."""

    generator_count = len(generators)
    # First m inequalities are lambda_i >= 0 (activated as lambda_i=0).
    # Last three are sum_i lambda_i*a_{i,k} <= exponent_k.
    possible_active: list[tuple[list[int], int]] = []
    for index in range(generator_count):
        possible_active.append(
            ([int(other == index) for other in range(generator_count)], 0)
        )
    for coordinate in range(3):
        possible_active.append(
            ([g[coordinate] for g in generators], exponent[coordinate])
        )

    for active_indices in combinations(
        range(generator_count + 3), generator_count - 1
    ):
        matrix = [[1] * generator_count]
        rhs = [1]
        for active_index in active_indices:
            row, value = possible_active[active_index]
            matrix.append(row)
            rhs.append(value)
        lambdas = solve_square(matrix, rhs)
        if lambdas is None or any(value < 0 for value in lambdas):
            continue
        if any(
            sum(
                lambdas[index] * generators[index][coordinate]
                for index in range(generator_count)
            )
            > exponent[coordinate]
            for coordinate in range(3)
        ):
            continue
        return True
    return False


def in_monomial_ideal(generators: Generators, exponent: Exponent) -> bool:
    return any(
        all(generator[k] <= exponent[k] for k in range(3))
        for generator in generators
    )


def admissible_ideals() -> list[Generators]:
    """Enumerate all labeled ideals in the finite parameterization."""

    ideals: list[Generators] = []
    for a, b, c in product(range(1, 5), repeat=3):
        pure: Generators = ((a, 0, 0), (0, b, 0), (0, 0, c))
        ideals.append(pure)
        for r in range(a):
            for s in range(b):
                for t in range(c):
                    mixed = (r, s, t)
                    if sum(mixed) > 4:
                        continue
                    if sum(coordinate > 0 for coordinate in mixed) < 2:
                        continue
                    ideals.append(pure + (mixed,))
    assert len(ideals) == 517
    assert len(set(ideals)) == len(ideals)
    return ideals


def grid_points(bounds: Exponent):
    """The standard box plus its one-step upper boundary."""

    return product(*(range(bound + 1) for bound in bounds))


def inner_box_points(bounds: Exponent):
    return product(*(range(bound) for bound in bounds))


def analyze(generators: Generators) -> dict[str, object]:
    bounds = (generators[0][0], generators[1][1], generators[2][2])
    points = list(grid_points(bounds))
    direct = {point: in_monomial_ideal(generators, point) for point in points}
    closed = {point: in_integral_closure(generators, point) for point in points}
    assert all(not direct[point] or closed[point] for point in points)

    def socle(membership: dict[Exponent, bool]) -> list[Exponent]:
        answer: list[Exponent] = []
        for point in inner_box_points(bounds):
            if membership[point]:
                continue
            if all(
                membership[
                    tuple(point[k] + int(k == coordinate) for k in range(3))
                ]
                for coordinate in range(3)
            ):
                answer.append(point)
        assert answer
        return answer

    socle_i = socle(direct)
    socle_closed = socle(closed)
    v_i = min(map(sum, socle_i))
    v_closed = min(map(sum, socle_closed))
    return {
        "generators": [list(generator) for generator in generators],
        "bounds": list(bounds),
        "grid_order": "lexicographic product(range(a+1),range(b+1),range(c+1))",
        "ideal_membership_bits": "".join("1" if direct[p] else "0" for p in points),
        "closure_membership_bits": "".join("1" if closed[p] else "0" for p in points),
        "socle_I": [list(point) for point in socle_i],
        "socle_closure": [list(point) for point in socle_closed],
        "v_I": v_i,
        "v_closure": v_closed,
    }


def build_payload() -> dict[str, object]:
    ideals = admissible_ideals()
    records = [analyze(generators) for generators in ideals]
    differences = Counter(
        record["v_closure"] - record["v_I"]  # type: ignore[operator]
        for record in records
    )
    control_generators: Generators = (
        (2, 0, 0),
        (0, 2, 0),
        (0, 0, 5),
        (1, 1, 1),
    )
    control = analyze(control_generators)
    assert (control["v_I"], control["v_closure"]) == (2, 3)
    assert all(record["v_closure"] <= record["v_I"] for record in records)
    return {
        "method": "exact-rational-active-set-vertex-feasibility",
        "arithmetic": "fractions.Fraction only; no floating point",
        "labeled_ideal_count": len(records),
        "three_generator_count": sum(len(generators) == 3 for generators in ideals),
        "four_generator_count": sum(len(generators) == 4 for generators in ideals),
        "expanded_grid_point_count": sum(
            (record["bounds"][0] + 1)  # type: ignore[index,operator]
            * (record["bounds"][1] + 1)  # type: ignore[index,operator]
            * (record["bounds"][2] + 1)  # type: ignore[index,operator]
            for record in records
        ),
        "standard_box_point_count": sum(
            record["bounds"][0]  # type: ignore[index]
            * record["bounds"][1]  # type: ignore[index]
            * record["bounds"][2]  # type: ignore[index]
            for record in records
        ),
        "v_closure_minus_v_I_distribution": {
            str(key): differences[key] for key in sorted(differences)
        },
        "violating_count": sum(
            record["v_closure"] > record["v_I"] for record in records
        ),
        "degree_five_positive_control": control,
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: value for key, value in payload.items() if key != "records"},
            ensure_ascii=False,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
