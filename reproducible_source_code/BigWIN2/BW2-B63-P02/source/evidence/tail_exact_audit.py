#!/usr/bin/env python3
"""Symbolic/exact audit for the identities in tail_proof.md."""

from math import comb

import sympy as sp


r = sp.symbols("r", integer=True, positive=True)
j = sp.symbols("j", integer=True, nonnegative=True)
n = 4 * r + 2

v = sp.binomial(n, 2 * r)
degree = sp.binomial(2 * r, r) * sp.binomial(2 * r + 2, r)
m4 = sp.binomial(n, 4) - sp.binomial(n, 3)
theta2 = -(2 * r**2 + 1) / ((2 * r - 1) * (2 * r + 2) * (2 * r + 1))
q = sp.combsimp(v / degree / (m4 * theta2**2))


def normalized_eberlein_fixed(index: int):
    """For fixed index, terms above index vanish identically."""
    eigenvalue = sum(
        (-1) ** ell
        * sp.binomial(index, ell)
        * sp.binomial(2 * r - index, r - ell)
        * sp.binomial(2 * r + 2 - index, r - ell)
        for ell in range(index + 1)
    )
    return sp.factor(sp.combsimp(eigenvalue / degree))


theta = [normalized_eberlein_fixed(index) for index in range(4)]
assert theta[0] == 1
assert sp.factor(theta[1] - 1 / (2 * (r + 1))) == 0
assert sp.factor(theta[2] - theta2) == 0
assert sp.factor(
    theta[3] - theta[2] - (r - 1) / (2 * (r + 1) * (2 * r + 1))
) == 0

q_claimed = (
    6
    * (2 * r - 1) ** 2
    * sp.binomial(4 * r, 2 * r)
    * sp.factorial(r - 1)
    * sp.factorial(r + 2)
    / (
        (4 * r - 5)
        * (2 * r**2 + 1) ** 2
        * sp.binomial(2 * r, r)
        * sp.factorial(2 * r)
    )
)
assert sp.factor(sp.combsimp(q - q_claimed)) == 0

q_ratio_claimed = (
    r
    * (r + 3)
    * (4 * r - 5)
    * (4 * r + 1)
    * (4 * r + 3)
    * (2 * r**2 + 1) ** 2
    / (
        2
        * (r + 1)
        * (2 * r - 1) ** 2
        * (2 * r + 1)
        * (4 * r - 1)
        * (2 * r**2 + 4 * r + 3) ** 2
    )
)
assert sp.factor(sp.combsimp(q.subs(r, r + 1) / q) - q_ratio_claimed) == 0
assert q.subs(r, 3) == sp.Rational(330, 361)

p = (
    384 * r**8
    + 2032 * r**7
    + 1276 * r**6
    + 76 * r**5
    - 236 * r**4
    + 136 * r**3
    + 439 * r**2
    + 87 * r
    - 18
)
denominator = sp.denom(q_ratio_claimed)
assert sp.factor((1 - q_ratio_claimed) * denominator - p) == 0

m = lambda x: sp.binomial(n, x) - sp.binomial(n, x - 1)
m_ratio_claimed = (4 * r + 1 - 2 * j) * (4 * r + 3 - j) / (
    (j + 1) * (4 * r + 3 - 2 * j)
)
assert sp.factor(sp.combsimp(m(j + 1) / m(j)) - m_ratio_claimed) == 0
assert sp.factor(
    3 * (4 * r - 2) * (4 * r - 1) - 5 * (2 * r + 3) * (4 * r - 5)
) == 8 * r**2 - 46 * r + 81


def eberlein(rr: int, jj: int) -> int:
    def c(a: int, b: int) -> int:
        return comb(a, b) if 0 <= b <= a else 0

    return sum(
        (-1) ** ell
        * c(jj, ell)
        * c(2 * rr - jj, rr - ell)
        * c(2 * rr + 2 - jj, rr - ell)
        for ell in range(rr + 1)
    )


assert [eberlein(2, jj) for jj in range(5)] == [90, 15, -9, -6, 6]
print("all symbolic identities and the r=2 exact spectrum verified")
