#!/usr/bin/env python3
"""Exact discovery audit at and just beyond the adjacent-X certificate edge.

This is a falsification aid, not a proof of a continuum.  It reconstructs the
raw Hermitian gate and evaluates an exact rational corner grid at X=1/31 and
X=1/30.  A negative value would be a genuine exact candidate after legality
checks; absence of one is reported only as a finite exact search result.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

from itertools import product

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic


def main():
    R = sp.Rational
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    X, M, omega, nu = sp.symbols("X M omega nu", real=True)
    A = 1 + M
    y0 = R(12, 25) / A + nu
    wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
    Y = S * y0
    W = S * (wc + omega)
    Zmap = 3 * X - X**2 - Y**2 + W
    xmap = -R(1, 5) + X
    ymap = R(3, 5) + Y
    gate = quartic.as_expr()

    records = []
    for sv, xv, mv, ov, nv in product(
        (R(1, 20000), R(1, 10000)),
        (R(1, 31), R(1, 30)),
        (-R(1, 1000), R(1, 1000)),
        (-R(1, 100), R(1, 100)),
        (-R(1, 100), R(1, 100)),
    ):
        substitutions = {S: sv, X: xv, M: mv, omega: ov, nu: nv}
        zv = sp.factor(Zmap.subs(substitutions))
        xv_raw = xmap.subs(substitutions)
        yv_raw = ymap.subs(substitutions)
        lv = sp.factor(A.subs(substitutions) / sv)
        danger = sp.factor(1 - xv_raw**2 - yv_raw**2 - zv)
        determinant = sp.factor(R(5, 9) * sv * zv)
        if not (lv > 0 and 0 < zv < R(1, 8) and danger > 0 and determinant > 0):
            raise AssertionError(("illegal exact node", substitutions))
        value = sp.factor(gate.subs({
            S: sv,
            Z: zv,
            x: xv_raw,
            y: yv_raw,
            lam: lv,
        }))
        records.append(((sv, xv, mv, ov, nv), value))

    negatives = [item for item in records if item[1] < 0]
    minimum = min(records, key=lambda item: item[1])
    print("EXACT_LEGAL_NODES", len(records))
    print("EXACT_NEGATIVE_NODES", len(negatives))
    print("EXACT_MINIMUM", minimum)
    print("STATUS finite exact falsification search only; continuum sign at X=1/30 open")
    if negatives:
        raise AssertionError(("exact legal negative candidate", negatives[0]))


if __name__ == "__main__":
    main()
