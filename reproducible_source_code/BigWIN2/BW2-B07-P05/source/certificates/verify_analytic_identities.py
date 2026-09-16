#!/usr/bin/env python3
"""Exact symbolic audit of the human full-family proof identities."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    X, Y, Z, T, A = sp.symbols("X Y Z T A")
    f = 12 * Z**3 - 27 * Z**2 + 20 * Z - 4
    P = X * (1 - X - Y)
    Q = Y * (1 - 2 * Z)
    R = Z * (1 - X + Y) - Y
    L = T / (1 - 2 * Z)
    U = 1 - (T + (1 - Z) * L) / Z
    vertex = (1 - L) / 2
    N = T * (4 - 7 * Z) + 2 * Z**2 - Z
    H = (6 * Z - 4) * T + 2 * Z**3 - 5 * Z**2 + 2 * Z
    h = (2 * Z**3 - 5 * Z**2 + 2 * Z) / (4 - 6 * Z)

    assert sp.factor(vertex - U - N / (2 * Z * (1 - 2 * Z))) == 0
    assert sp.factor(U * (1 - U - L) - T - T * H / (Z**2 * (1 - 2 * Z))) == 0
    assert sp.factor(sp.diff(h, Z) + f / (2 * (3 * Z - 2)**2)) == 0
    assert f.subs(Z, sp.Rational(31, 100)) == -sp.Rational(4651, 125000)
    assert f.subs(Z, sp.Rational(8, 25)) == sp.Rational(444, 15625)

    z = sp.CRootOf(f, 0)
    x = z / 2
    y = (1 - z) * (1 - 2 * z)
    t0 = (5 * z**2 - 4 * z**3) / 4
    assert sp.Rational(31, 100) < z < sp.Rational(8, 25)
    assert sp.Rational(9, 100) < t0 < sp.Rational(1, 10)
    assert 0 < x < y < z < sp.Rational(1, 2)

    def reduce_at_root(expression):
        numerator, denominator = sp.fraction(sp.together(expression.xreplace({z: Z})))
        reduced = sp.rem(sp.Poly(numerator, Z), sp.Poly(f, Z)).as_expr()
        return sp.factor(reduced / denominator)

    for expression in (
        P.subs({X: x, Y: y, Z: z}) - t0,
        Q.subs({X: x, Y: y, Z: z}) - t0,
        R.subs({X: x, Y: y, Z: z}) - t0,
        h.xreplace({Z: z}) - t0,
        L.subs({T: t0, Z: z}) - y,
        U.subs({T: t0, Z: z}) - x,
    ):
        assert reduce_at_root(expression) == 0

    resultant = sp.factor(sp.resultant(f, 8 * A - (5 * Z**2 - 4 * Z**3), Z))
    assert sp.expand(resultant - 256 * (3456 * A**3 - 1764 * A**2 + 268 * A - 9)) == 0

    def configuration(a, b, c):
        return [
            (a, 0), (1 - b, 0), (0, a), (1, b), (1 - c, c),
            (c, 1 - c), (0, 1 - b), (1, 1 - a), (b, 1), (1 - a, 1)
        ]

    base = sorted(map(str, configuration(X, Y, Z)))
    involution_xy = sorted(map(str, configuration(1 - Y, 1 - X, Z)))
    involution_z = sorted(map(str, configuration(X, Y, 1 - Z)))
    assert base == involution_xy == involution_z

    print(json.dumps({
        "status": "PASS",
        "implementation": "sympy-exact-analytic-identity-audit",
        "identities_checked": 6,
        "root_and_order_checks": 5,
        "parameter_involutions_checked": 2,
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }, sort_keys=True))


if __name__ == "__main__":
    main()
