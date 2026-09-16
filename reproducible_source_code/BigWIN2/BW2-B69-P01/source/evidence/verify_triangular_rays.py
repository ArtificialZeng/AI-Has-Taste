#!/usr/bin/env python3
"""Exact support test for the 18 triangular rays of BR_Q(4,3).

The variables are ordered (a_11,a_12,a_13,a_21,...,a_43).  Every
polynomial is represented by a dictionary from 12-tuples of exponents to
nonnegative Python integers, so no floating-point arithmetic is used.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


H4 = tuple(weak_compositions(4, 3))
H2 = tuple(weak_compositions(2, 3))
H4_INDEX = {alpha: pos for pos, alpha in enumerate(H4)}


def add(*vectors):
    return tuple(sum(entries) for entries in zip(*vectors))


def unit(i: int):
    return tuple(int(i == j) for j in range(3))


def coefficient_polynomial(alpha):
    """Return the ordinary coefficient P_alpha as an exact sparse dict."""
    polynomial = defaultdict(int)
    for assignment in itertools.product(range(3), repeat=4):
        counts = tuple(assignment.count(i) for i in range(3))
        if counts != alpha:
            continue
        monomial = [0] * 12
        for row, column in enumerate(assignment):
            monomial[3 * row + column] += 1
        polynomial[tuple(monomial)] += 1
    return dict(polynomial)


P = {alpha: coefficient_polynomial(alpha) for alpha in H4}


def multiply(left, right):
    product = defaultdict(int)
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                a + b for a, b in zip(left_monomial, right_monomial)
            )
            product[monomial] += left_coefficient * right_coefficient
    return dict(product)


def alpha_label(alpha):
    return "".join(str(entry) for entry in alpha)


def monomial_label(monomial):
    factors = []
    for row in range(4):
        for column in range(3):
            exponent = monomial[3 * row + column]
            if exponent:
                label = f"a{row + 1}{column + 1}"
                factors.append(label if exponent == 1 else f"{label}^{exponent}")
    return "*".join(factors) if factors else "1"


def main():
    rays = []
    seen = set()
    for beta in H2:
        for i in range(3):
            j, k = tuple(column for column in range(3) if column != i)
            positive = (add(beta, unit(i), unit(i)), add(beta, unit(j), unit(k)))
            negative = (add(beta, unit(i), unit(j)), add(beta, unit(i), unit(k)))

            gamma = [0] * len(H4)
            for alpha in positive:
                gamma[H4_INDEX[alpha]] += 1
            for alpha in negative:
                gamma[H4_INDEX[alpha]] -= 1
            gamma = tuple(gamma)

            assert gamma not in seen
            seen.add(gamma)
            assert sum(gamma) == 0
            assert all(
                sum(gamma[pos] * H4[pos][coordinate] for pos in range(len(H4)))
                == 0
                for coordinate in range(3)
            )
            assert math.gcd(*(abs(entry) for entry in gamma)) == 1

            numerator = multiply(P[positive[0]], P[positive[1]])
            denominator = multiply(P[negative[0]], P[negative[1]])
            missing = sorted(set(numerator) - set(denominator))
            coefficient_violations_at_c1 = sorted(
                monomial
                for monomial, coefficient in numerator.items()
                if coefficient > denominator.get(monomial, 0)
            )
            maximum_ratio = max(
                (
                    numerator[monomial],
                    denominator[monomial],
                    monomial,
                )
                for monomial in numerator
                if monomial in denominator
            ) if numerator else None

            rays.append(
                {
                    "ray": f"beta={alpha_label(beta)},i={i + 1}",
                    "positive_indices": [alpha_label(alpha) for alpha in positive],
                    "negative_indices": [alpha_label(alpha) for alpha in negative],
                    "gamma_in_H4_order": list(gamma),
                    "balanced": True,
                    "ambient_lattice_gcd": 1,
                    "numerator_terms": len(numerator),
                    "denominator_terms": len(denominator),
                    "missing_denominator_monomials": len(missing),
                    "first_missing": (
                        {
                            "monomial": monomial_label(missing[0]),
                            "exponents": list(missing[0]),
                            "numerator_coefficient": numerator[missing[0]],
                            "denominator_coefficient": 0,
                        }
                        if missing
                        else None
                    ),
                    "c_equals_1_coefficient_violations": len(
                        coefficient_violations_at_c1
                    ),
                }
            )

    assert len(rays) == 18
    result = {
        "arithmetic": "exact nonnegative integers",
        "H4_order": [alpha_label(alpha) for alpha in H4],
        "ray_count": len(rays),
        "distinct_ray_count": len(seen),
        "all_balanced": all(ray["balanced"] for ray in rays),
        "all_ambient_primitive": all(
            ray["ambient_lattice_gcd"] == 1 for ray in rays
        ),
        "rays_with_missing_denominator_monomials": sum(
            ray["missing_denominator_monomials"] > 0 for ray in rays
        ),
        "rays_passing_support_containment": sum(
            ray["missing_denominator_monomials"] == 0 for ray in rays
        ),
        "rays_passing_c_equals_1": sum(
            ray["c_equals_1_coefficient_violations"] == 0 for ray in rays
        ),
        "rays": rays,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
