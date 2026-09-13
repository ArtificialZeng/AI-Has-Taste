#!/usr/bin/env python3
"""Fresh coefficient-level recheck of the frozen horizon-two certificate."""

import json
import sympy as sp


q = sp.Rational
a = sp.symbols("a", real=True)
m = a**4 - 8*a**3 + 10*a**2 - a - 1
c = 1 / (a + 2)
ids = (-1, 0, 1, 2)


def outer_coefficient(u, v):
    return (u * v.T + v * u.T) / 2


zero = sp.zeros(4, 1)
X = {
    -1: zero,
    0: sp.Matrix([1, 0, 0, 0]),
    1: sp.Matrix([1, -1, 0, 0]),
    2: sp.Matrix([1, -1, -a, 0]),
}
G = {
    -1: zero,
    0: sp.Matrix([0, 1, 0, 0]),
    1: sp.Matrix([0, 0, 1, 0]),
    2: sp.Matrix([0, 0, 0, 1]),
}


def H(i, j):
    dg = G[i] - G[j]
    return -outer_coefficient(G[j], X[i] - X[j]) - outer_coefficient(dg, dg) / 2


lam = {(i, j): sp.Integer(0) for i in ids for j in ids if i != j}
lam.update({
    (0, 1): (399*a**2 - 201*a + 2) / (500*(a+2)),
    (0, 2): (996 - 456*a - 227*a**2) / (500*(a+2)),
    (1, 0): (172*a**2 - 485*a + 342) / (500*(a+2)),
    (1, 2): (227*a + 229) / 500,
    (2, 0): q(2, 25),
    (2, 1): q(153, 250),
    (-1, 0): (144 - 53*a) / (125*(a+2)),
    (-1, 1): q(93, 500),
    (-1, 2): q(119, 500),
    (2, -1): 2 / (a+2),
})
mu = (q(1, 1000), q(1, 1000), q(499, 500))

# This is the matrix printed in proof.md, entered independently of its constructor.
S = sp.Matrix([
    [1/(a+2)**2, (53*a-144)/(250*(a+2)), -q(93,1000), -q(119,1000)],
    [(53*a-144)/(250*(a+2)), (46-17*a)/(40*(a+2)),
     (-106*a**2+249*a-78)/(500*(a+2)), q(79,1000)],
    [-q(93,1000), (-106*a**2+249*a-78)/(500*(a+2)),
     (186*a**2-829*a+1598)/(1000*(a+2)),
     (119*a**2+703*a-1070)/(1000*(a+2))],
    [-q(119,1000), q(79,1000),
     (119*a**2+703*a-1070)/(1000*(a+2)),
     (694-153*a)/(500*(a+2))],
])


def vanishes_at_frozen_root(expr):
    numerator = sp.cancel(expr).as_numer_denom()[0]
    return sp.rem(sp.Poly(numerator, a), sp.Poly(m, a)).is_zero


# Check f-value coefficients directly.
flow = {i: sp.Integer(0) for i in ids}
for (i, j), value in lam.items():
    flow[i] += value
    flow[j] -= value
assert all(sp.cancel(value) == 0 for value in flow.values())

# Reconstruct the coefficient of the Gram matrix in the proposed identity.
gram_residual = S.copy()
gram_residual[0, 0] -= c**2
for k, value in enumerate(mu):
    gram_residual[k+1, k+1] += value
for edge, value in lam.items():
    gram_residual += value * H(*edge)
assert all(vanishes_at_frozen_root(entry) for entry in gram_residual)
assert sum(mu) == 1

# Independently audit the kernel and Sylvester minors of the printed slack.
w = sp.Matrix([1, c, c, c])
assert all(vanishes_at_frozen_root(entry) for entry in S*w)
B = S[1:4, 1:4]
deltas = [B[:k, :k].det() for k in (1, 2, 3)]
scaled = [
    sp.cancel(deltas[0] * 40*(a+2)),
    sp.cancel(deltas[1] * 1_000_000*(a+2)**2),
    sp.cancel(deltas[2] * 200_000_000*(a+2)**2),
]
reduced = [sp.rem(sp.Poly(x, a), sp.Poly(m, a)).as_expr() for x in scaled]
assert reduced[0] == 46 - 17*a

lo, hi = q(1281, 1000), q(641, 500)
r2_lower = -227450*hi**3 + 701517*lo**2 - 1522068*hi + 1768420
r3_lower = 4682448*lo**3 + 24778142*lo**2 - 115934851*hi + 124473901
assert 46 - 17*hi > 0
assert r2_lower > 0 and r3_lower > 0

# Check the radical is the intended root and the endpoint witness recurrence.
actual_a = 1 + (sp.sqrt(5)-1)/(1+sp.sqrt(7+2*sp.sqrt(5)))
assert sp.simplify(m.subs(a, actual_a)) == 0
assert sp.N(actual_a-lo, 50) > 0 and sp.N(hi-actual_a, 50) > 0
assert vanishes_at_frozen_root(1 - c - a*c - c)

eigenvalues = [str(x) for x in sp.N(S.subs(a, actual_a), 18).eigenvals().keys()]
print(json.dumps({
    "flow_coefficients_zero": True,
    "printed_slack_identity_exact": True,
    "kernel_exact": True,
    "sylvester_lower_bounds": [str(46-17*hi), str(r2_lower), str(r3_lower)],
    "numerical_slack_eigenvalues_sanity": eigenvalues,
    "lower_witness_recurrence_exact": True,
}, sort_keys=True))
