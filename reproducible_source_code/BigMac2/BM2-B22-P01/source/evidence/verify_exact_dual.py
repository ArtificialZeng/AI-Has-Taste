#!/usr/bin/env python3
"""Exact audit of the proposed N=2 queried-gradient PEP certificate.

All identities are checked in Q(a), where the actual radical a=1+beta is the
root of a^4-8a^3+10a^2-a-1 in (1.281,1.282).  Positivity is proved by rational
interval bounds; no floating-point comparison is used.
"""

import json
import sympy as sp


a = sp.symbols("a", real=True)
c = 1 / (a + 2)
rho = c**2
q = sp.Rational
star = -1
ids = (star, 0, 1, 2)

# Exact radical identification and a rational enclosure.
alpha_radical = 1 + (sp.sqrt(5) - 1) / (1 + sp.sqrt(7 + 2 * sp.sqrt(5)))
minimal = a**4 - 8*a**3 + 10*a**2 - a - 1
assert sp.simplify(minimal.subs(a, alpha_radical)) == 0
s_lo, s_hi = q(559, 250), q(2237, 1000)
r_lo, r_hi = q(3387, 1000), q(847, 250)
assert s_lo**2 < 5 < s_hi**2
assert r_lo**2 < 7 + 2*s_lo
assert 7 + 2*s_hi < r_hi**2
assert (s_lo - 1)/(1 + r_hi) > q(281, 1000)
assert (s_hi - 1)/(1 + r_lo) < q(282, 1000)
lo, hi = q(1281, 1000), q(641, 500)

# Coordinate vectors in the ordered Gram family (x0,g0,g1,g2).
zero = sp.zeros(4, 1)
x = {
    star: zero,
    0: sp.Matrix([1, 0, 0, 0]),
    1: sp.Matrix([1, -1, 0, 0]),
    2: sp.Matrix([1, -1, -a, 0]),
}
g = {
    star: zero,
    0: sp.Matrix([0, 1, 0, 0]),
    1: sp.Matrix([0, 0, 1, 0]),
    2: sp.Matrix([0, 0, 0, 1]),
}


def sym_outer(u, v):
    return (u*v.T + v*u.T) / 2


def interpolation_matrix(i, j):
    """Gram coefficient in h_ij=f_i-f_j-<g_j,x_i-x_j>-|g_i-g_j|^2/2."""
    return -sym_outer(g[j], x[i]-x[j]) - sym_outer(g[i]-g[j], g[i]-g[j])/2


# The ten displayed multipliers are nonzero; the omitted (0,*) and (1,*)
# multipliers are exactly zero.  All twelve ordered inequalities are nevertheless
# present in the coefficient audit below.
lam = {edge: sp.Integer(0) for edge in ((i, j) for i in ids for j in ids if i != j)}
lam.update({
    (0, 1): (399*a**2 - 201*a + 2) / (500*(a+2)),
    (0, 2): (996 - 456*a - 227*a**2) / (500*(a+2)),
    (1, 0): (172*a**2 - 485*a + 342) / (500*(a+2)),
    (1, 2): (227*a + 229) / 500,
    (2, 0): q(2, 25),
    (2, 1): q(153, 250),
    (star, 0): (144 - 53*a) / (125*(a+2)),
    (star, 1): q(93, 500),
    (star, 2): q(119, 500),
    (2, star): 2 / (a+2),
})
mu = (q(1, 1000), q(1, 1000), q(499, 500))
assert sum(mu) == 1

# Exact nonnegativity from 1.281<a<1.282.  The only close polynomial is
# lambda_(1,0); it is decreasing on the enclosure and remains >2.9/(500(a+2)).
assert 399*lo**2 - 201*lo + 2 > 0
assert 798*lo - 201 > 0
assert 996 - 456*hi - 227*hi**2 == q(9582013, 250000) > 0
assert 344*hi - 485 < 0
assert 172*hi**2 - 485*hi + 342 == q(91129, 31250) > 0
assert 144 - 53*hi == q(38027, 500) > 0
assert all(m > 0 for m in mu)

# Function-value coefficients cancel (flow conservation).
flow = [sp.Integer(0)] * 3
for (i, j), value in lam.items():
    if i != star:
        flow[i] += value
    if j != star:
        flow[j] -= value
assert all(sp.cancel(value) == 0 for value in flow)

# Form the exact dual slack.  This simultaneously checks every Gram coefficient
# in the full PEP, including the FGM recurrence encoded in x[1] and x[2].
S = sp.zeros(4)
S[0, 0] = rho
for k, value in enumerate(mu):
    S[k+1, k+1] -= value
for edge, value in lam.items():
    S -= value * interpolation_matrix(*edge)
S = S.applyfunc(sp.cancel)

w = sp.Matrix([1, c, c, c])
assert all(sp.cancel(value) == 0 for value in S*w)
B = S[1:4, 1:4]
assert sp.cancel((sp.ones(1, 3)*B*sp.ones(3, 1))[0] - 1) == 0

# Sylvester minors of B.  Reduce their numerators with the exact minimal
# polynomial and prove the two nontrivial signs by outward rational bounds.
d1 = sp.factor(B[:1, :1].det())
d2 = sp.factor(B[:2, :2].det())
d3 = sp.factor(B.det())
assert sp.cancel(d1 - (46 - 17*a)/(40*(a+2))) == 0

n2 = sp.cancel(d2 * 1_000_000*(a+2)**2)
n3 = sp.cancel(d3 * 200_000_000*(a+2)**2)
r2 = sp.rem(sp.Poly(n2, a), sp.Poly(minimal, a)).as_expr()
r3 = sp.rem(sp.Poly(n3, a), sp.Poly(minimal, a)).as_expr()
assert sp.expand(r2 - (-227450*a**3 + 701517*a**2 - 1522068*a + 1768420)) == 0
assert sp.expand(r3 - (4682448*a**3 + 24778142*a**2 - 115934851*a + 124473901)) == 0
r2_lower = -227450*hi**3 + 701517*lo**2 - 1522068*hi + 1768420
r3_lower = 4682448*lo**3 + 24778142*lo**2 - 115934851*hi + 124473901
assert r2_lower == q(2445271097527, 5000000) > 0
assert r3_lower == q(205845508080081, 7812500) > 0
assert 46 - 17*hi > 0

# The exact lower witness: x1=1-c is still in the saturated projection region,
# and the second FGM queried point is exactly c.
assert lo > 0  # hence a>0 and c=1/(a+2)<1/2
assert sp.cancel(1 - c - a*c - c) == 0

print(json.dumps({
    "certificate": "exact",
    "field_polynomial": str(minimal),
    "alpha_interval": [str(lo), str(hi)],
    "interpolation_inequalities": len(lam),
    "positive_multipliers": 13,
    "zero_interpolation_multipliers": 2,
    "slack_rank": 3,
    "psd_test": "three exact positive Sylvester minors on w-perp",
    "objective": "1/(a+2)^2=c_2^2",
}, sort_keys=True))
