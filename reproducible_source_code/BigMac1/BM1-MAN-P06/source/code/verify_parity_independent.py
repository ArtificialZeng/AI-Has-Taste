#!/usr/bin/env python3
"""Second derivation using affine-dependence cofactor signs."""

from __future__ import annotations

import itertools


def sign(value: int) -> int:
    return (value > 0) - (value < 0)


def determinant(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def main() -> None:
    grid = tuple(itertools.product(range(-2, 3), repeat=2))
    checked = 0
    for points in itertools.combinations(grid, 4):
        a, b, c, d = points
        chis = (
            determinant(a, b, c),
            determinant(a, b, d),
            determinant(a, c, d),
            determinant(b, c, d),
        )
        if 0 in chis:
            continue
        # Cofactors give an affine dependence with coefficient signs
        # (-chi_bcd, chi_acd, -chi_abd, chi_abc).
        coefficient_signs = (
            -sign(chis[3]),
            sign(chis[2]),
            -sign(chis[1]),
            sign(chis[0]),
        )
        positives = sum(value > 0 for value in coefficient_signs)
        convex_by_radon = positives == 2
        convex_by_product = sign(chis[0] * chis[1] * chis[2] * chis[3]) == 1
        assert convex_by_radon == convex_by_product
        checked += 1
    print(f"verified_affine_cofactor_quadruples={checked}")
    print("verified_radon_partition_parity_equivalence")


if __name__ == "__main__":
    main()
