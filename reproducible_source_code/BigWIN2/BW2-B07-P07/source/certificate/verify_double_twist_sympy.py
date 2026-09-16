#!/usr/bin/env python3
"""Independent symbolic audit of the double-twist proof identities."""

from __future__ import annotations

import argparse

import sympy as sp


x, y = sp.symbols("x y")


def A(n, u):
    return sum((u ** k for k in range(n)), sp.Integer(0))


def E(n, u):
    return sum(((2 * (n - k) - 1) * u ** k for k in range(n)), sp.Integer(0))


def a_values(n, t0, t1):
    u = t0 * t1
    a1 = sp.cancel((u ** n - 1) / (u - 1))
    a2 = sp.cancel(
        2 * n * (t0 - 1) * (t1 - 1) / (u - 1)
        - a1 * ((u + 1) * (t0 - 1) * (t1 - 1) / (u - 1) + 1)
    )
    a3 = sp.cancel((t0 - 1) * (t1 - 1) * a1 + 1)
    return a1, a2, a3


def positive_formula(p, q):
    u = x * y
    hp = (1 + x) * (1 + y)
    hm = (1 + x ** -1) * (1 + y ** -1)
    return sp.expand(
        A(q, u) * hm * (u ** (-(p - 1)) + 2 * A(p - 1, u ** -1))
        + hp * E(q, u) * hm * E(p, u ** -1)
        + 1 + hp * A(q, u)
    )


def verify(p, q, max_identity_n):
    u = x * y
    hp = (1 + x) * (1 + y)

    # Direct, independent comparison with the rational a_i definitions.
    for n in range(1, max_identity_n + 1):
        a1, a2, a3 = a_values(n, -x, -y)
        assert sp.cancel(a1 - A(n, u)) == 0
        assert sp.cancel(-a2 - (A(n, u) + hp * E(n, u))) == 0
        assert sp.cancel(a3 - (1 + hp * A(n, u))) == 0
        assert sp.expand(E(n, u) - E(n - 1, u)
                         - u ** (n - 1) - 2 * A(n - 1, u)) == 0

    # Reconstruct Kohli's one-block and two-block recurrences directly.
    def L1(n):
        ta1, ta2, _ = a_values(n, -x ** -1, -y ** -1)
        return sp.cancel(ta1 + ta2)

    aq1, aq2, aq3 = a_values(q, -x, -y)
    recurrence = sp.cancel(aq1 * L1(p - 1) + aq2 * L1(p) + aq3)
    closed = positive_formula(p, q)
    assert sp.cancel(recurrence - closed) == 0

    terms = sp.Poly(sp.expand(closed * x ** p * y ** p), x, y).terms()
    # Multiplication by a monomial clears negative exponents without changing
    # coefficients.  All coefficients must be exact nonnegative integers.
    assert all(coefficient.is_Integer and coefficient >= 0
               for _, coefficient in terms)

    if (p, q) == (1, 1):
        expected = (2 * x * y + 3 * x + x / y + 3 * y + 7 + 3 / y
                    + y / x + 3 / x + 2 / (x * y))
        assert sp.cancel(closed - expected) == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int, nargs="?", default=2)
    parser.add_argument("q", type=int, nargs="?", default=3)
    parser.add_argument("--max-identity-n", type=int, default=12)
    args = parser.parse_args()
    if args.p < 1 or args.q < 1 or args.max_identity_n < 1:
        parser.error("all parameters must be positive")
    verify(args.p, args.q, args.max_identity_n)
    print("INDEPENDENT_DOUBLE_TWIST_SYMBOLIC_AUDIT_OK",
          f"p={args.p}", f"q={args.q}",
          f"identity_n=1..{args.max_identity_n}")


if __name__ == "__main__":
    main()
