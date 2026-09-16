#!/usr/bin/env python3
"""Exact coefficient certificate for the double-twist positivity formula."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict


# Laurent polynomials in x,y, serialized as exponent-pair -> integer.
def add(*polys):
    out = defaultdict(int)
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] += coefficient
    return {m: c for m, c in out.items() if c}


def mul(left, right):
    out = defaultdict(int)
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            out[(i + k, j + ell)] += a * b
    return {m: c for m, c in out.items() if c}


ONE = {(0, 0): 1}


def monomial(i, j, coefficient=1):
    return {(i, j): coefficient}


def A(n, sign=1):
    if n < 0:
        raise ValueError("n must be nonnegative")
    return {(sign * k, sign * k): 1 for k in range(n)}


def E(n, sign=1):
    if n < 0:
        raise ValueError("n must be nonnegative")
    return {(sign * k, sign * k): 2 * (n - k) - 1 for k in range(n)}


def H(sign=1):
    return {(0, 0): 1, (sign, 0): 1, (0, sign): 1,
            (sign, sign): 1}


def double_twist_positive(p, q):
    """Return LG(D(p,q);-x,-y) in the Kohli D-notation."""
    if p < 1 or q < 1:
        raise ValueError("p and q must be positive")
    delta_E_p_minus = add(monomial(-(p - 1), -(p - 1)),
                          {m: 2 * c for m, c in A(p - 1, -1).items()})
    term1 = mul(A(q, 1), mul(H(-1), delta_E_p_minus))
    term2 = mul(H(1), mul(E(q, 1), mul(H(-1), E(p, -1))))
    term3 = add(ONE, mul(H(1), A(q, 1)))
    return add(term1, term2, term3)


def assert_nonnegative(poly):
    assert poly
    assert all(isinstance(c, int) and c >= 0 for c in poly.values())


def figure_eight_expected():
    return {
        (1, 1): 2, (1, 0): 3, (1, -1): 1,
        (0, 1): 3, (0, 0): 7, (0, -1): 3,
        (-1, 1): 1, (-1, 0): 3, (-1, -1): 2,
    }


def verify(p, q):
    result = double_twist_positive(p, q)
    assert_nonnegative(A(q, 1))
    assert_nonnegative(E(q, 1))
    assert_nonnegative(H(1))
    assert_nonnegative(A(p, -1))
    assert_nonnegative(E(p, -1))
    assert_nonnegative(H(-1))
    assert_nonnegative(result)

    # The two finite-sum identities used in the proof.
    if p >= 1:
        delta_e = add(E(p, -1),
                      {m: -c for m, c in E(p - 1, -1).items()})
        expected_delta = add(monomial(-(p - 1), -(p - 1)),
                             {m: 2 * c for m, c in A(p - 1, -1).items()})
        assert delta_e == expected_delta
    if q >= 1:
        delta_a = add(A(q, 1),
                      {m: -c for m, c in A(q - 1, 1).items()})
        assert delta_a == monomial(q - 1, q - 1)

    if (p, q) == (1, 1):
        assert result == figure_eight_expected()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int, nargs="?", default=1)
    parser.add_argument("q", type=int, nargs="?", default=1)
    args = parser.parse_args()
    result = verify(args.p, args.q)
    print(json.dumps({
        "status": "CERTIFIED",
        "family": "Kohli D(p,q) double-twist knot",
        "p": args.p,
        "q": args.q,
        "term_count": len(result),
        "minimum_coefficient": min(result.values()),
        "terms": [[i, j, c] for (i, j), c in sorted(result.items())],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
