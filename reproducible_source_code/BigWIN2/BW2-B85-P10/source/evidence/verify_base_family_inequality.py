#!/usr/bin/env python3
"""Exact symbolic audit of the T(p,0,q) discriminant proof."""

import json

import sympy as sp


p, q, r, s = sp.symbols("p q r s")


def expanded(expr):
    return sp.expand(sp.expand_func(expr))


def h(t):
    return (
        sp.binomial(p + q, t)
        + sp.binomial(p, t - 1)
        + sp.binomial(q, t - 1)
        + (1 if t == 2 else 0)
    )


ell2_pq = expanded(h(1) + h(2))
ell3_pq = expanded(h(2) + h(3))
ell4_pq = expanded(h(3) + h(4))

r_pq = p + q
s_pq = p * q
ell2 = (r**2 + 3 * r + 6) / 2
ell3_minus_one = sp.binomial(r + 2, 3) - s
ell4 = sp.binomial(r + 2, 4) - r * s / 2

assert sp.simplify(ell2_pq - ell2.subs({r: r_pq})) == 0
assert sp.simplify(ell3_pq - 1 - ell3_minus_one.subs({r: r_pq, s: s_pq})) == 0
assert sp.simplify(ell4_pq - ell4.subs({r: r_pq, s: s_pq})) == 0

delta = expanded(ell3_minus_one**2 - ell2 * ell4)
discriminant = sp.factor(sp.discriminant(delta, s))
expected = -r * (r**2 + 3 * r + 6) * (r**3 + 7 * r**2 + 2 * r + 8) / 48
assert sp.simplify(discriminant - expected) == 0
assert sp.Poly(delta, s).LC() == 1

print(
    json.dumps(
        {
            "arithmetic": "exact symbolic",
            "delta": str(sp.factor(delta)),
            "discriminant_in_s": str(discriminant),
            "leading_coefficient_in_s": "1",
            "status": "all symbolic identities verified",
        },
        indent=2,
        sort_keys=True,
    )
)
