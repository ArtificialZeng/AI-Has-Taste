#!/usr/bin/env python3
"""Exact symbolic checks for the endpoint audit in arXiv:2609.04833v1.

Here A = alpha + 2 and h = p - A.  The script checks the rational
simplification of the upper bound G and the log-Gamma form of the exact
left-hand side L of condition (3.38).  It is evidence, not a formal proof;
the accompanying Markdown artifact supplies the analytic derivation.
"""

import sympy as sp


A, h, b = sp.symbols("A h b", positive=True)
p = A + h

G = (
    (p * (b + 1) - A)
    / (p - A)
    * 2
    * (1 - (A / p) ** 2)
    / (A / p + 2 * (p - A))
)
G_rational = (
    2
    * (A * b + (b + 1) * h)
    * (2 * A + h)
    / ((A + h) * (A + 2 * A * h + 2 * h**2))
)

assert sp.factor(G - G_rational) == 0
G_difference = sp.factor(G_rational - 4 * b)

# With x=A/(A+h), use 2h*B(x,2h)
# = Gamma(x) Gamma(1+2h) / Gamma(x+2h).
x = A / (A + h)
Phi = sp.loggamma(x) + sp.loggamma(1 + 2 * h) - sp.loggamma(x + 2 * h)
L = (A * b + (b + 1) * h) / h**2 * (1 - sp.exp(-Phi))

phi_coefficient = sp.simplify(sp.limit(Phi / h**2, h, 0, dir="+"))
L_limit = sp.simplify(sp.limit(L, h, 0, dir="+"))

assert sp.simplify(sp.limit(G, h, 0, dir="+") - 4 * b) == 0
assert sp.simplify(phi_coefficient - sp.pi**2 / (3 * A)) == 0
assert sp.simplify(L_limit - sp.pi**2 * b / 3) == 0

print("G - G_rational =", sp.factor(G - G_rational))
print("G_rational =", G_rational)
print("G - 4*b =", G_difference)
print("limit_(h->0+) G =", sp.limit(G, h, 0, dir="+"))
print("limit_(h->0+) Phi/h^2 =", phi_coefficient)
print("limit_(h->0+) L =", L_limit)

