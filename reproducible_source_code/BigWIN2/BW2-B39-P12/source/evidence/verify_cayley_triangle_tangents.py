#!/usr/bin/env python3
"""Independent stdlib/Fraction check of the Cayley-triangle tangent certificate.

This checker deliberately does not import SymPy or either search script.  It
enumerates the permutation anchors and edge choices afresh, and computes only
the quadratic Taylor coefficients needed for the local-isolation conclusion.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


N = 7
EDGES = tuple((i, j) for i in range(N) for j in range(i + 1, N))


def zero_matrix() -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(N)] for _ in range(N)]


def add(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[left[i][j] + right[i][j] for j in range(N)] for i in range(N)]


def scale(scalar: Fraction, matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[scalar * matrix[i][j] for j in range(N)] for i in range(N)]


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    output = zero_matrix()
    for i in range(N):
        for k in range(N):
            if left[i][k] == 0:
                continue
            for j in range(N):
                output[i][j] += left[i][k] * right[k][j]
    return output


def permutation_matrix(permutation: tuple[int, ...]) -> list[list[Fraction]]:
    matrix = zero_matrix()
    for i, j in enumerate(permutation):
        matrix[i][j] = Fraction(1)
    return matrix


def skew_edge(edge: tuple[int, int]) -> list[list[Fraction]]:
    matrix = zero_matrix()
    i, j = edge
    matrix[i][j] = Fraction(1)
    matrix[j][i] = Fraction(-1)
    return matrix


def cycles(permutation: tuple[int, ...]) -> list[list[int]]:
    seen: set[int] = set()
    output = []
    for start in range(N):
        if start in seen:
            continue
        cycle = []
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cycle.append(cursor)
            cursor = permutation[cursor]
        output.append(cycle)
    return output


def anchors() -> list[tuple[int, ...]]:
    output = []
    for permutation in itertools.permutations(range(N)):
        fixed = sum(permutation[i] == i for i in range(N))
        anti = sum(permutation[i] == N - 1 - i for i in range(N))
        if fixed == anti == 1 and sorted(map(len, cycles(permutation))) == [1, 3, 3]:
            output.append(permutation)
    return output


def selected_sum(
    matrix: list[list[Fraction]], positions: list[tuple[int, int]]
) -> Fraction:
    return sum((matrix[i][j] for i, j in positions), Fraction(0))


def square_coefficient(
    p_matrix: list[list[Fraction]],
    linear: list[list[Fraction]],
    second: list[list[Fraction]],
    positions: list[tuple[int, int]],
) -> Fraction:
    return sum((linear[i][j] ** 2 for i, j in positions), Fraction(0)) + 2 * sum(
        (p_matrix[i][j] * second[i][j] for i, j in positions), Fraction(0)
    )


def cross_coefficient(
    p_matrix: list[list[Fraction]],
    left_linear: list[list[Fraction]],
    right_linear: list[list[Fraction]],
    cross_second: list[list[Fraction]],
    positions: list[tuple[int, int]],
) -> Fraction:
    return 2 * sum(
        (left_linear[i][j] * right_linear[i][j] for i, j in positions), Fraction(0)
    ) + 2 * sum(
        (p_matrix[i][j] * cross_second[i][j] for i, j in positions), Fraction(0)
    )


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    permutations = anchors()
    diagonal_positions = [(i, i) for i in range(N)]
    anti_positions = [(i, N - 1 - i) for i in range(N)]
    ay_counts: Counter[Fraction] = Counter()
    failures = []
    family_count = 0

    for permutation_index, permutation in enumerate(permutations):
        p_matrix = permutation_matrix(permutation)
        identity_plus_p = zero_matrix()
        for i in range(N):
            identity_plus_p[i][i] = Fraction(1)
        identity_plus_p = add(identity_plus_p, p_matrix)
        b_matrix = scale(Fraction(1, 2), identity_plus_p)

        edge_matrices = {edge: skew_edge(edge) for edge in EDGES}
        right_b = {edge: multiply(edge_matrices[edge], b_matrix) for edge in EDGES}
        b_edge_b = {
            edge: multiply(b_matrix, right_b[edge]) for edge in EDGES
        }
        linear = {edge: scale(Fraction(-2), b_edge_b[edge]) for edge in EDGES}
        second_square = {
            edge: scale(
                Fraction(2), multiply(b_edge_b[edge], right_b[edge])
            )
            for edge in EDGES
        }

        d_square = {
            edge: square_coefficient(
                p_matrix, linear[edge], second_square[edge], diagonal_positions
            )
            for edge in EDGES
        }
        a_square = {
            edge: square_coefficient(
                p_matrix, linear[edge], second_square[edge], anti_positions
            )
            for edge in EDGES
        }

        cycle_list = cycles(permutation)
        singleton = next(cycle[0] for cycle in cycle_list if len(cycle) == 1)
        triples = sorted((cycle for cycle in cycle_list if len(cycle) == 3), key=min)
        first_cycle, second_cycle = triples
        for first_vertex in first_cycle:
            for middle_vertices in itertools.product(first_cycle, second_cycle):
                for third_vertex in second_cycle:
                    active = (
                        tuple(sorted((singleton, first_vertex))),
                        tuple(sorted(middle_vertices)),
                        tuple(sorted((singleton, third_vertex))),
                    )
                    d_cross = []
                    for left_index, right_index in ((0, 1), (0, 2), (1, 2)):
                        left_edge = active[left_index]
                        right_edge = active[right_index]
                        cross_second = scale(
                            Fraction(2),
                            add(
                                multiply(b_edge_b[left_edge], right_b[right_edge]),
                                multiply(b_edge_b[right_edge], right_b[left_edge]),
                            ),
                        )
                        d_cross.append(
                            cross_coefficient(
                                p_matrix,
                                linear[left_edge],
                                linear[right_edge],
                                cross_second,
                                diagonal_positions,
                            )
                        )
                    d_coefficients = (
                        d_square[active[0]],
                        d_square[active[1]],
                        d_square[active[2]],
                        d_cross[0],
                        d_cross[1],
                        d_cross[2],
                    )
                    ay = a_square[active[1]]
                    ay_counts[ay] += 1
                    family_count += 1
                    if d_coefficients != (
                        Fraction(-2),
                        Fraction(0),
                        Fraction(-2),
                        Fraction(0),
                        Fraction(0),
                        Fraction(0),
                    ) or ay == 0:
                        failures.append(
                            {
                                "permutation_index": permutation_index,
                                "active_edges_zero_based": [list(edge) for edge in active],
                                "diagonal_coefficients": list(map(fstr, d_coefficients)),
                                "antidiagonal_y_squared_coefficient": fstr(ay),
                            }
                        )

    result = {
        "schema": "win-00039-p12/fraction-tangent-check/v1",
        "implementation": "Python standard library fractions.Fraction; no SymPy imports",
        "permutation_count": len(permutations),
        "edge_choices_per_permutation": 81,
        "family_count": family_count,
        "diagonal_quadratic_in_every_family": "-2*x^2-2*z^2",
        "antidiagonal_y_squared_coefficient_counts": {
            fstr(value): count for value, count in sorted(ay_counts.items())
        },
        "failed_certificate_count": len(failures),
        "failures": failures,
    }
    if len(permutations) != 112 or family_count != 9072 or failures:
        raise AssertionError("independent tangent certificate failed")
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: result[key] for key in (
        "permutation_count", "family_count", "failed_certificate_count"
    )}, sort_keys=True))


if __name__ == "__main__":
    main()
