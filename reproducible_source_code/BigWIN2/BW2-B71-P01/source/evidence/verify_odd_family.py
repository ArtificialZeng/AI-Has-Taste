#!/usr/bin/env python3
"""Exact checks for the all-one odd-length Q-polynomial family.

All calculations are over QQ.  No numerical root approximations are used.
The script compares the three-state tangle transfer with the Chebyshev closed
form and then counts real roots of the canonically monomial-cleared polynomial
by a Sturm sequence.
"""

from __future__ import annotations

import sympy as sp


x = sp.Symbol("x")
u = (x + 1) / 2

# In the ordered relative-skein basis (1,e,g), the positive all-one
# continued-fraction step is: reciprocal-with-sign rotation, then multiply by
# g.  Rotation swaps 1 and e and fixes g; g^2=-1+x*e+x*g.
A = sp.Matrix([[0, 0, -1], [1, 0, x], [0, 1, x]])
v1 = sp.Matrix([0, 0, 1])
delta = 2 / x - 1
closure = sp.Matrix([[delta, 1, 1]])


def transfer_q(j: int) -> sp.Expr:
    """Q of C(1^j), from the exact relative-skein transfer."""
    assert j >= 1
    return sp.cancel((closure * (A ** (j - 1)) * v1)[0])


def trig_numerator(n: int) -> sp.Poly:
    """H_n=x(x+3) Q_{C(1^(2n+1))}, expressed with Chebyshev T."""
    m = 2 * n + 2
    expr = 2 * (u - sp.chebyshevt(2, u) + 2 * sp.chebyshevt(m, u))
    return sp.Poly(sp.expand(expr), x, domain=sp.QQ)


def canonical_from_closed_form(n: int) -> sp.Poly:
    """The canonical P_n after removal of the sole possible x^{-1}."""
    H = trig_numerator(n)
    divisor = sp.Poly(x + 3, x, domain=sp.QQ)
    if n % 3 != 2:  # knot case: H has the additional factor x
        divisor *= sp.Poly(x, x, domain=sp.QQ)
    quotient, remainder = sp.div(H, divisor, domain=sp.QQ)
    assert remainder.is_zero
    assert quotient.domain == sp.QQ
    assert all(c.q == 1 for c in quotient.all_coeffs())
    assert quotient.eval(0) != 0
    return quotient


def canonical_from_transfer(n: int) -> sp.Poly:
    q = sp.expand(transfer_q(2 * n + 1))
    terms = sp.Add.make_args(q)
    exponents = [term.as_powers_dict().get(x, 0) for term in terms]
    emin = min(exponents)
    assert emin in (sp.Integer(-1), sp.Integer(0))
    expected = -1 if n % 3 == 2 else 0
    assert emin == expected
    p = sp.Poly(sp.expand(q * x ** (-emin)), x, domain=sp.QQ)
    assert all(c.q == 1 for c in p.all_coeffs())
    assert p.eval(0) != 0
    return p


def sign_at_infinity(poly: sp.Poly, positive: bool) -> int:
    lc_sign = int(sp.sign(poly.LC()))
    if positive or poly.degree() % 2 == 0:
        return lc_sign
    return -lc_sign


def variations(signs: list[int]) -> int:
    signs = [s for s in signs if s]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm_real_count(poly: sp.Poly) -> tuple[int, int]:
    """Return (distinct real roots, Sturm chain length), exactly."""
    chain = [sp.Poly(f, x, domain=sp.QQ) for f in sp.sturm(poly.as_expr(), x)]
    at_minus = [sign_at_infinity(f, False) for f in chain]
    at_plus = [sign_at_infinity(f, True) for f in chain]
    return variations(at_minus) - variations(at_plus), len(chain)


def main() -> None:
    charpoly = sp.factor(A.charpoly().as_expr())
    charpoly2 = sp.factor((A**2).charpoly().as_expr())

    # Independently known smallest-link values, also derived by the transfer.
    expected = {
        1: 1,
        2: 2 * x + 1 - 2 / x,
        3: 2 * x**2 + 2 * x - 3,
        4: 2 * x**3 + 4 * x**2 - 2 * x - 3,
    }
    for j, value in expected.items():
        assert sp.cancel(transfer_q(j) - value) == 0

    print("exact_arithmetic=QQ")
    print(f"charpoly_A={charpoly}")
    print(f"charpoly_A2={charpoly2}")
    print("initial_q1=1")
    print("initial_q2=2*x + 1 - 2/x")
    print("initial_q3=2*x^2 + 2*x - 3")
    print("columns=n,components,canonical_degree,sturm_real_roots,squarefree,chain_length")

    for n in range(1, 21):
        q = transfer_q(2 * n + 1)
        H = trig_numerator(n).as_expr()
        assert sp.cancel(q - H / (x * (x + 3))) == 0

        p_transfer = canonical_from_transfer(n)
        p_closed = canonical_from_closed_form(n)
        assert p_transfer == p_closed

        squarefree = sp.gcd(p_transfer, p_transfer.diff()).degree() == 0
        real_count, chain_length = sturm_real_count(p_transfer)
        assert squarefree
        assert real_count == p_transfer.degree()

        components = 2 if n % 3 == 2 else 1
        print(
            f"{n},{components},{p_transfer.degree()},"
            f"{real_count},{str(squarefree).lower()},{chain_length}"
        )


if __name__ == "__main__":
    main()
