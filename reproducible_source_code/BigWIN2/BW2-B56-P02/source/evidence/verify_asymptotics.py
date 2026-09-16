#!/usr/bin/env python3
"""Exact SymPy checks for the four Example 6 asymptotics.

This script uses only rational/symbolic arithmetic.  Decimal values printed at
the end are orientation aids and are not used by any assertion.
"""

import sympy as sp

d, z = sp.symbols("d z", positive=True)
Q = sp.Rational

X1 = sp.Matrix([[-Q(1, 9), 1 / d, 0],
                [0, 1 / (3 + d), 0],
                [0, 0, -Q(1, 13)]])
X2 = sp.Matrix([[-Q(1, 9), 1 / d, -Q(1, 19)],
                [-Q(1, 6), 1 / (3 + d), -Q(1, 16)],
                [-Q(1, 3), 1 / (6 + d), -Q(1, 13)]])
X3 = sp.Matrix([[-Q(1, 9), 0, -Q(1, 19)],
                [-Q(1, 6), 1 / (3 + d), -Q(1, 16)],
                [-Q(1, 3), 1 / (6 + d), -Q(1, 13)]])
X4 = sp.diag(-Q(1, 9), 1 / (3 + d), -Q(1, 13))


def gram_coefficients(X):
    """Return S1,S2,S3 in det(zI-X^T X)=z^3-S1*z^2+S2*z-S3."""
    G = X.T * X
    s1 = sp.factor(sp.trace(G))
    s2 = sp.factor(sum(G.extract([i, j], [i, j]).det()
                       for i, j in [(0, 1), (0, 2), (1, 2)]))
    s3 = sp.factor(G.det())
    assert sp.factor((z * sp.eye(3) - G).det()
                     - (z**3 - s1 * z**2 + s2 * z - s3)) == 0
    return s1, s2, s3


coeffs = [gram_coefficients(X) for X in (X1, X2, X3, X4)]

# The finite eigenvalues in case 2 converge to those of D^T D.
D = sp.Matrix([[-Q(1, 6), -Q(1, 16)],
               [-Q(1, 3), -Q(1, 13)]])
Dpoly = sp.factor((z * sp.eye(2) - D.T * D).det())
assert sp.factor(Dpoly - (z**2 - Q(57905, 389376) * z
                          + Q(25, 389376))) == 0
mu_minus = Q(57905, 778752) - 5 * sp.sqrt(132562057) / 778752
assert sp.factor(Dpoly.subs(z, mu_minus)) == 0
assert mu_minus > 0

# Case 3 limiting Gram polynomial and exact rational root isolation.
X30 = X3.subs(d, 0)
P3 = 45542974464 * z**3 - 13786630308 * z**2 + 429202697 * z - 330625
assert sp.factor((z * sp.eye(3) - X30.T * X30).det()
                 - P3 / 45542974464) == 0
root_intervals = [(Q(1, 1300), Q(1, 1200)),
                  (Q(1, 30), Q(1, 29)),
                  (Q(1, 4), Q(1, 3))]
assert [sp.Poly(P3, z).count_roots(a, b) for a, b in root_intervals] == [1, 1, 1]
assert sp.discriminant(P3, z) > 0

# Exact determinant/full-rank checks.
expected_dets = [1 / (117 * (d + 3)),
                 5 * (d + 9) * (d + 19) / (5928 * d * (d + 3) * (d + 6)),
                 -5 * (17 * d + 115) / (11856 * (d + 3) * (d + 6)),
                 1 / (117 * (d + 3))]
for X, det_expected in zip((X1, X2, X3, X4), expected_dets):
    assert sp.factor(X.det() - det_expected) == 0

print("All exact symbolic assertions passed.")
for i, (s1, s2, s3) in enumerate(coeffs, 1):
    print(f"case {i}: S1={s1}; S2={s2}; S3={s3}")
print("case 2 K =", sp.sqrt(1 / mu_minus), "~=", sp.N(sp.sqrt(1 / mu_minus), 15))
roots3 = sorted(sp.nroots(P3), key=lambda w: float(sp.re(w)))
print("case 3 limiting squared singular values ~=", roots3)
print("case 3 K ~=", sp.N(sp.sqrt(roots3[-1] / roots3[0]), 15))
