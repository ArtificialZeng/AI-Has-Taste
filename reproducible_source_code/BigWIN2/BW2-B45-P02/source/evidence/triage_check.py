#!/usr/bin/env python3
"""Exact, reproducible triage checks; requires SymPy."""
import sympy as sp

a, r, s, t, x = sp.symbols("a r s t x")


def cubic(rr, ss, tt, xx):
    return (
        rr * ss * tt
        + (rr * (ss + tt) + ss * tt + (ss + tt) / a) * xx
        + (rr + ((a + 1) * (ss + tt) + 2) / a) * xx**2
        + (a + 2) / a * xx**3
    )


R = cubic(r, s, t, x)
assert sp.factor(R.subs(x, -1) - (r - 1) * (s - 1) * (t - 1)) == 0
assert sp.factor(-cubic(r, s, t, -1 - x) - cubic(1-r, 1-s, 1-t, x)) == 0

grid = [sp.Rational(j, 4) for j in range(5)]
agrid = [sp.Rational(1, 10), sp.Rational(1, 4), sp.Rational(1, 2),
         sp.Rational(1), sp.Rational(2), sp.Rational(4), sp.Rational(10)]
checked = 0
for aa in agrid:
    for rr in grid:
        for ss in grid:
            for tt in grid:
                D = sp.discriminant(R.subs({a: aa, r: rr, s: ss, t: tt}), x)
                assert D >= 0
                checked += 1
print(f"symbolic identities verified; exact grid points with discriminant >= 0: {checked}")

