#!/usr/bin/env python3
"""Independent exact verifier using five projective evaluations."""

from __future__ import annotations

import json

import sympy as sp
from sympy.polys.matrices import DomainMatrix


A, S, u, v = sp.symbols("A S u v")
BASE = [(1, 0), (0, A), (-1, 0), (0, -A)]
POINTS = [0, 1, -1, sp.I, -sp.I]


def distance(i: int, j: int) -> sp.Expr:
    if {i, j} == {0, 2}:
        return sp.Integer(2)
    if {i, j} == {1, 3}:
        return 2 * A
    return S


def pair(i: int, j: int) -> tuple[sp.Expr, sp.Expr]:
    if i < 4 and j < 4:
        xi, yi = BASE[i]
        xj, yj = BASE[j]
        return -distance(i, j), xj-xi + sp.I*(yj-yi)
    if i < 4:
        xi, yi = BASE[i]
        return -(u if yi == 0 else A*v), -xi-sp.I*yi
    xj, yj = BASE[j]
    return -(1/u if yj == 0 else A/v), xj+sp.I*yj


def determinant_from_values() -> tuple[sp.Expr, sp.Expr]:
    values = sp.zeros(5)
    vandermonde = sp.Matrix([[t**k for k in range(5)] for t in POINTS])
    for row, t in enumerate(POINTS):
        for i in range(5):
            value = sp.Integer(1)
            for j in range(5):
                if i != j:
                    c0, c1 = pair(i, j)
                    value *= c0 + c1*t
            if i == 4:
                value = sp.cancel(u**2*v**2*value)
            values[row, i] = sp.expand(value)
    numerator = DomainMatrix.from_Matrix(values).det().as_expr()
    return sp.cancel(numerator / vandermonde.det()), vandermonde.det()


def claimed() -> sp.Expr:
    p = (
        A**3*u*v + A**3*v + A**2*S*u*v + A**2*S*u + A**2*S*v
        + A**2*S + A**2*u*v + A**2*u + A*S**2*u + A*S**2
        + 2*A*S*u + 2*A*S*v + A*u*v + A*v + S**2*v + S**2
        + S*u*v + S*u + S*v + S + u*v + u
    )
    g = (u+v)*(u-v)**2
    q = (
        A**4*(u+v) + 2*A**3*S*(v+1) + A**2*S**2*(2*u**3*v**3+g+2)
        + 2*A**2*S*(u+1) + 2*A**2*(u+v)
        + 2*A*S**3*(u**3*v**3+u**3*v**2) + 2*A*S*(v+1)
        + S**4*(u**3*v**2+u**2*v**3)
        + 2*S**3*(u**3*v**3+u**2*v**3) + 2*S**2*u**3*v**3
        + S**2*(g+2) + 2*S*(u+1) + u+v
    )
    return sp.expand(2**7*sp.I*A**6*S*p*q)


def main() -> None:
    determinant, vandermonde = determinant_from_values()
    difference = sp.expand(determinant - claimed())
    payload = {
        "certificate_id": "AS-C1-5-RHOMBPYR-20260830",
        "method": "direct products at five projective evaluation points; divide by Vandermonde determinant",
        "evaluation_points": [str(t) for t in POINTS],
        "vandermonde_determinant": str(vandermonde),
        "cleared_column_factor": "u^2*v^2",
        "identity_verified": difference == 0,
    }
    print(json.dumps(payload, indent=2))
    if difference != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
