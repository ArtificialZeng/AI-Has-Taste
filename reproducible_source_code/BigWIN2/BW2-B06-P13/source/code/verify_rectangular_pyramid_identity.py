#!/usr/bin/env python3
"""Independent exact verifier based on direct values at five projective points."""

from __future__ import annotations

import json

import sympy as sp
from sympy.polys.matrices import DomainMatrix


A, S, w = sp.symbols("A S w")
BASE = [(1, A), (-1, A), (-1, -A), (1, -A)]
EVALUATION_POINTS = [0, 1, -1, sp.I, -sp.I]


def factor_coefficients(i: int, j: int) -> tuple[sp.Expr, sp.Expr]:
    if i < 4 and j < 4:
        dx = BASE[j][0] - BASE[i][0]
        dy = BASE[j][1] - BASE[i][1]
        if dx == 0:
            distance = 2 * A
        elif dy == 0:
            distance = sp.Integer(2)
        else:
            distance = 2 * S
        return -distance, dx + sp.I * dy
    if i < 4:
        x, y = BASE[i]
        return -w * S, -x - sp.I * y
    x, y = BASE[j]
    return -S / w, x + sp.I * y


def value_determinant() -> tuple[sp.Expr, sp.Expr]:
    values = sp.zeros(5)
    vandermonde = sp.Matrix([[t**k for k in range(5)] for t in EVALUATION_POINTS])
    for row, t in enumerate(EVALUATION_POINTS):
        for i in range(5):
            value = sp.Integer(1)
            for j in range(5):
                if i != j:
                    f0, f1 = factor_coefficients(i, j)
                    value *= f0 + f1 * t
            if i == 4:
                value *= w**4
            values[row, i] = sp.expand(value)
    numerator = DomainMatrix.from_Matrix(values).det().as_expr()
    return sp.cancel(numerator / vandermonde.det()), vandermonde.det()


def claimed_factorization() -> sp.Expr:
    e = w**6 + w**5 + w + 1
    q = ((A**4 + 1) * (w**3 + 1) ** 2
         + S * e * (A**3 + A**2 + A + 1)
         + 2 * (w**5 + w) * (A**3 + A)
         + 2 * A**2 * (w**3 - 1) ** 2)
    return (-2**16 * A**4 * S**5 * (A**2 + A*S + S + 1)
            * (S * (1 + w**2) + 2*w*(A + 1)) * q)


def reduce_relation(expression: sp.Expr) -> sp.Expr:
    return sp.Poly(sp.expand(expression), S).rem(sp.Poly(S**2-A**2-1, S)).as_expr()


def main() -> None:
    determinant, vandermonde = value_determinant()
    difference = sp.expand(reduce_relation(determinant) - reduce_relation(claimed_factorization()))
    payload = {
        "certificate_id": "AS-C1-5-RECTPYR-20260830",
        "method": "direct products at five projective evaluation points; divide by Vandermonde determinant",
        "evaluation_points": [str(value) for value in EVALUATION_POINTS],
        "vandermonde_determinant": str(vandermonde),
        "quotient_relation": "S^2-A^2-1",
        "identity_verified": difference == 0,
    }
    print(json.dumps(payload, indent=2))
    if difference != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
