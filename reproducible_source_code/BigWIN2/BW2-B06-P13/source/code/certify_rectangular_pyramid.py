#!/usr/bin/env python3
"""Exact coefficient-expansion certificate for the rectangular-pyramid identity."""

from __future__ import annotations

import json

import sympy as sp
from sympy.polys.matrices import DomainMatrix


A, S, w = sp.symbols("A S w")
BASE = [(1, A), (-1, A), (-1, -A), (1, -A)]


def linear_factor(i: int, j: int) -> tuple[sp.Expr, sp.Expr]:
    """Coefficients of U,V; the apex column is later cleared by w^4."""
    if i < 4 and j < 4:
        dx = BASE[j][0] - BASE[i][0]
        dy = BASE[j][1] - BASE[i][1]
        distance = 2 * A if dx == 0 else (sp.Integer(2) if dy == 0 else 2 * S)
        return -distance, dx + sp.I * dy
    if i < 4 and j == 4:
        x, y = BASE[i]
        return -w * S, -x - sp.I * y
    if i == 4 and j < 4:
        x, y = BASE[j]
        return -S / w, x + sp.I * y
    raise ValueError("diagonal pair")


def coefficient_matrix_with_cleared_apex() -> sp.Matrix:
    matrix = sp.zeros(5)
    for i in range(5):
        coefficients = [sp.Integer(1)]
        for j in range(5):
            if i == j:
                continue
            f0, f1 = linear_factor(i, j)
            updated = [sp.Integer(0)] * (len(coefficients) + 1)
            for k, value in enumerate(coefficients):
                updated[k] += value * f0
                updated[k + 1] += value * f1
            coefficients = [sp.expand(value) for value in updated]
        if i == 4:
            coefficients = [sp.expand(w**4 * value) for value in coefficients]
        for k, value in enumerate(coefficients):
            matrix[k, i] = value
    return matrix


def target() -> sp.Expr:
    e = w**6 + w**5 + w + 1
    q = (
        (A**4 + 1) * (w**3 + 1) ** 2
        + S * e * (A**3 + A**2 + A + 1)
        + 2 * (w**5 + w) * (A**3 + A)
        + 2 * A**2 * (w**3 - 1) ** 2
    )
    return (
        -2**16
        * A**4
        * S**5
        * (A**2 + A * S + S + 1)
        * (S * (1 + w**2) + 2 * w * (A + 1))
        * q
    )


def quotient_remainder(expression: sp.Expr) -> sp.Expr:
    relation = sp.Poly(S**2 - A**2 - 1, S)
    return sp.Poly(sp.expand(expression), S).rem(relation).as_expr()


def main() -> None:
    matrix = coefficient_matrix_with_cleared_apex()
    domain_matrix = DomainMatrix.from_Matrix(matrix)
    determinant = domain_matrix.det().as_expr()
    difference = sp.expand(quotient_remainder(determinant) - quotient_remainder(target()))
    result = {
        "certificate_id": "AS-C1-5-RECTPYR-20260830",
        "method": "binary-form coefficient convolution and exact domain-matrix determinant",
        "ring": str(domain_matrix.domain),
        "raw_determinant_terms": len(sp.Poly(determinant, A, S, w).terms()),
        "quotient_relation": "S^2-A^2-1",
        "identity_verified": difference == 0,
    }
    print(json.dumps(result, indent=2))
    if difference != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
