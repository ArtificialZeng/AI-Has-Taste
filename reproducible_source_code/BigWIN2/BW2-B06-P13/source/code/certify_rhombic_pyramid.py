#!/usr/bin/env python3
"""Exact coefficient-expansion certificate for the rhombic-pyramid identity."""

from __future__ import annotations

import json

import sympy as sp
from sympy.polys.matrices import DomainMatrix


A, S, u, v = sp.symbols("A S u v")
BASE = [(1, 0), (0, A), (-1, 0), (0, -A)]


def base_distance(i: int, j: int) -> sp.Expr:
    if {i, j} == {0, 2}:
        return sp.Integer(2)
    if {i, j} == {1, 3}:
        return 2 * A
    return S


def linear_factor(i: int, j: int) -> tuple[sp.Expr, sp.Expr]:
    if i < 4 and j < 4:
        x_i, y_i = BASE[i]
        x_j, y_j = BASE[j]
        return -base_distance(i, j), x_j - x_i + sp.I * (y_j - y_i)
    if i < 4:
        x_i, y_i = BASE[i]
        return (-(u if y_i == 0 else A * v), -x_i - sp.I * y_i)
    x_j, y_j = BASE[j]
    return (-(1 / u if y_j == 0 else A / v), x_j + sp.I * y_j)


def coefficient_matrix() -> sp.Matrix:
    matrix = sp.zeros(5)
    for i in range(5):
        coefficients = [sp.Integer(1)]
        for j in range(5):
            if i == j:
                continue
            f0, f1 = linear_factor(i, j)
            updated = [sp.Integer(0)] * (len(coefficients) + 1)
            for k, value in enumerate(coefficients):
                updated[k] += f0 * value
                updated[k + 1] += f1 * value
            coefficients = [sp.expand(value) for value in updated]
        if i == 4:
            coefficients = [sp.cancel(u**2 * v**2 * value) for value in coefficients]
        for k, value in enumerate(coefficients):
            matrix[k, i] = value
    return matrix


def positive_factors() -> tuple[sp.Expr, sp.Expr]:
    p = (
        A**3*u*v + A**3*v + A**2*S*u*v + A**2*S*u + A**2*S*v
        + A**2*S + A**2*u*v + A**2*u + A*S**2*u + A*S**2
        + 2*A*S*u + 2*A*S*v + A*u*v + A*v + S**2*v + S**2
        + S*u*v + S*u + S*v + S + u*v + u
    )
    square_group = (u + v) * (u - v)**2
    q = (
        A**4*(u + v) + 2*A**3*S*(v + 1)
        + A**2*S**2*(2*u**3*v**3 + square_group + 2)
        + 2*A**2*S*(u + 1) + 2*A**2*(u + v)
        + 2*A*S**3*(u**3*v**3 + u**3*v**2) + 2*A*S*(v + 1)
        + S**4*(u**3*v**2 + u**2*v**3)
        + 2*S**3*(u**3*v**3 + u**2*v**3) + 2*S**2*u**3*v**3
        + S**2*(square_group + 2) + 2*S*(u + 1) + u + v
    )
    return sp.expand(p), sp.expand(q)


def main() -> None:
    determinant = DomainMatrix.from_Matrix(coefficient_matrix()).det().as_expr()
    p, q = positive_factors()
    target = 2**7 * sp.I * A**6 * S * p * q
    difference = sp.expand(determinant - target)
    payload = {
        "certificate_id": "AS-C1-5-RHOMBPYR-20260830",
        "method": "binary-form coefficient convolution and exact domain-matrix determinant",
        "ring": str(DomainMatrix.from_Matrix(coefficient_matrix()).domain),
        "cleared_column_factor": "u^2*v^2",
        "raw_determinant_terms": len(sp.Poly(determinant, A, S, u, v).terms()),
        "identity_verified": difference == 0,
    }
    print(json.dumps(payload, indent=2))
    if difference != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
