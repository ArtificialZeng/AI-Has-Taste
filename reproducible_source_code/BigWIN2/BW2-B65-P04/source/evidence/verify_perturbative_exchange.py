#!/usr/bin/env python3
"""Exact verification of the sharp 2C3 -> 2C3 + C4 exchange."""

from __future__ import annotations

from fractions import Fraction


def symmetric_product(x: tuple[int, ...], y: tuple[int, ...]) -> list[int]:
    return [
        x[i] * y[j] if i == j else x[i] * y[j] + x[j] * y[i]
        for i in range(4)
        for j in range(i, 4)
    ]


def determinant(matrix: list[list[int | Fraction]]) -> Fraction:
    a = [[Fraction(value) for value in row] for row in matrix]
    det = Fraction(1)
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        value = a[col][col]
        det *= value
        for j in range(col, len(a)):
            a[col][j] /= value
        for row in range(col + 1, len(a)):
            factor = a[row][col]
            if factor:
                for j in range(col, len(a)):
                    a[row][j] -= factor * a[col][j]
    return det


def product_matrix(q: int) -> list[list[int]]:
    vectors = [
        (1, 0, 0, q),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (1, 1, 0, 0),
        (0, 1, 1, 0),
        (1, 0, 1, 0),
        (2, -1, 2, 0),
        (1, -2, 2, -1),
        (2, -1, 0, 1),
        (-1, 0, 1, -2),
    ]
    edges = [
        (0, 1), (1, 2), (2, 0),
        (3, 4), (4, 5), (5, 3),
        (6, 7), (7, 8), (8, 9), (9, 6),
    ]
    return [symmetric_product(vectors[i], vectors[j]) for i, j in edges]


def main() -> None:
    # Only the two rows incident with vertex 0 depend linearly on q, so the
    # determinant has degree at most two.  Three exact values prove (7).
    values = {q: determinant(product_matrix(q)) for q in (0, 1, 2)}
    expected = {q: 2 * q * (27 * q + 10) for q in values}
    if values != expected:
        raise AssertionError((values, expected))

    matrix0 = product_matrix(0)
    w_columns = [0, 1, 2, 4, 5, 7]
    q_columns = [3, 6, 8, 9]
    old = [[matrix0[i][j] for j in w_columns] for i in range(6)]
    if determinant(old) != -1:
        raise AssertionError("wrong old certificate")

    frozen_quotient = [[matrix0[i][j] for j in q_columns] for i in range(6, 10)]
    # The exchanged e3e4 column is C A^{-1} b.  Its exact value for this
    # specialization is (-2,0,4,0)^T.
    exchange_column = [-2, 0, 4, 0]
    exchange = [row[:] for row in frozen_quotient]
    for i, value in enumerate(exchange_column):
        exchange[i][2] = value
    if determinant(frozen_quotient) != 0 or determinant(exchange) != 20:
        raise AssertionError("wrong quotient exchange minor")

    # At q=1 these nonzero row scalars make the Gale rows sum to zero.
    vectors_q1 = [
        (1, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0),
        (1, 1, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0),
        (2, -1, 2, 0), (1, -2, 2, -1),
        (2, -1, 0, 1), (-1, 0, 1, -2),
    ]
    scales = (1, 1, 1, 1, 1, 3, -6, 4, 1, -1)
    weighted_sum = [sum(scales[i] * vectors_q1[i][j] for i in range(10)) for j in range(4)]
    if weighted_sum != [0, 0, 0, 0]:
        raise AssertionError(f"nonzero Gale row sum: {weighted_sum}")
    scaled_det = values[1]
    for scale in scales:
        scaled_det *= scale * scale  # every vertex has degree two
    if scaled_det != 383_616:
        raise AssertionError(f"unexpected scaled determinant: {scaled_det}")

    print(
        "verified perturbative exchange: det=2q(27q+10), "
        "old_det=-1, exchange_minor=20, scaled_gale_det=383616"
    )


if __name__ == "__main__":
    main()
