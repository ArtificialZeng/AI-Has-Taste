#!/usr/bin/env python3
"""Exact checks for the Gale-dual extension obstruction note."""

from __future__ import annotations

from fractions import Fraction


def symmetric_product(x: tuple[int, ...], y: tuple[int, ...]) -> list[int]:
    """Coordinates in lexicographic upper-triangular order."""
    ans: list[int] = []
    for i in range(len(x)):
        for j in range(i, len(x)):
            if i == j:
                ans.append(x[i] * y[i])
            else:
                ans.append(x[i] * y[j] + x[j] * y[i])
    return ans


def determinant(matrix: list[list[int]]) -> int:
    """Compute the determinant by exact rational elimination."""
    a = [[Fraction(value) for value in row] for row in matrix]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        value = a[col][col]
        det *= value
        for j in range(col, n):
            a[col][j] /= value
        for row in range(col + 1, n):
            factor = a[row][col]
            if factor:
                for j in range(col, n):
                    a[row][j] -= factor * a[col][j]
    if det.denominator != 1:
        raise AssertionError("integer matrix unexpectedly had nonintegral determinant")
    return det.numerator


def cycle_edges(starts_and_lengths: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [
        (start + i, start + (i + 1) % length)
        for start, length in starts_and_lengths
        for i in range(length)
    ]


def main() -> None:
    # The two frozen triangles span Sym^2(Q^3).
    old = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 0),
        (0, 1, 1),
        (1, 0, 1),
    ]
    old_matrix = [
        symmetric_product(old[u], old[v])
        for u, v in cycle_edges([(0, 3), (3, 3)])
    ]
    old_det = determinant(old_matrix)
    if old_det == 0:
        raise AssertionError("the frozen two-triangle certificate is singular")

    # A replacement placement makes 2 C3 union C4 a basis of Sym^2(Q^4).
    replacement = [
        (2, -1, 1, -2),
        (-1, 2, 2, 0),
        (1, 0, 2, 2),
        (0, -1, 1, 1),
        (0, 1, 0, -2),
        (-2, -1, -1, 1),
        (1, 2, -2, -1),
        (-1, -1, 2, -2),
        (0, 1, 1, 1),
        (0, 2, 1, 2),
    ]
    replacement_matrix = [
        symmetric_product(replacement[u], replacement[v])
        for u, v in cycle_edges([(0, 3), (3, 3), (6, 4)])
    ]
    replacement_det = determinant(replacement_matrix)
    if replacement_det != -3_616_140:
        raise AssertionError(f"unexpected replacement determinant: {replacement_det}")

    print(
        "verified exact Gale certificates: "
        f"two_triangle_det={old_det}, replacement_det={replacement_det}"
    )


if __name__ == "__main__":
    main()
