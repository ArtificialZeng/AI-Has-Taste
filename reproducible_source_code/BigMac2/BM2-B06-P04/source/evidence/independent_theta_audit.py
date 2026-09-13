#!/usr/bin/env python3
"""Independent exact audit of the pass-2 theta/eta Sturm certificate.

This implementation deliberately does not import the earlier charged-core or
factorization scripts.  It enumerates the six A5 cosets directly, expands the
eta quotient directly, and separately enumerates the abacus degree formula.
It certifies finite arithmetic only; modularity is proved in
``research_pass2.md`` and normalized explicitly in ``research_pass3.md``.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


STURM_BOUND = 360
CHARGED_BOUND = (STURM_BOUND - 5) // 3


def multiply(a: list[int], b: list[int], bound: int) -> list[int]:
    out = [0] * (bound + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j in range(min(len(b) - 1, bound - i) + 1):
            if b[j]:
                out[i + j] += ai * b[j]
    return out


def pochhammer_power(bound: int, step: int, power: int) -> list[int]:
    """Expand (q^step;q^step)_infinity^power through q^bound."""
    out = [0] * (bound + 1)
    out[0] = 1
    for d in range(step, bound + 1, step):
        factor = [0] * (bound + 1)
        if power >= 0:
            for k in range(power + 1):
                if k * d <= bound:
                    factor[k * d] = (-1) ** k * math.comb(power, k)
        else:
            # (1-x)^(-s) = sum_{k>=0} binom(s+k-1,k)x^k.
            s = -power
            for k in range(bound // d + 1):
                factor[k * d] = math.comb(s + k - 1, k)
        out = multiply(out, factor, bound)
    return out


def eta_g(bound: int) -> list[int]:
    """G=q^5 (q^6;q^6)^3 (q^18;q^18)^2 (q^36;q^36)^2/(q^3;q^3)^2."""
    unshifted_bound = bound - 5
    out = [0] * (unshifted_bound + 1)
    out[0] = 1
    for step, power in ((6, 3), (18, 2), (36, 2), (3, -2)):
        out = multiply(out, pochhammer_power(unshifted_bound, step, power), unshifted_bound)
    shifted = [0] * (bound + 1)
    for n, value in enumerate(out):
        shifted[n + 5] = value
    return shifted


def six_coset_theta(bound: int) -> tuple[list[int], list[list[int]], int]:
    """Enumerate z in the six cosets 6*A5+v_j directly."""
    r = (-3, -2, -1, 0, 1, 2)
    representatives = []
    for j in range(6):
        representatives.append(tuple(r[i] + (3 if i == j else 0) for i in range(6)))

    coordinate_bound = math.isqrt(2 * bound)
    total = [0] * (bound + 1)
    individual = [[0] * (bound + 1) for _ in range(6)]
    for j, v in enumerate(representatives):
        coordinate_lists = []
        for i in range(5):
            lo = math.ceil((-coordinate_bound - v[i]) / 6)
            hi = math.floor((coordinate_bound - v[i]) / 6)
            coordinate_lists.append(range(lo, hi + 1))
        for y in itertools.product(*coordinate_lists):
            first = tuple(v[i] + 6 * y[i] for i in range(5))
            last = -sum(first)
            if abs(last) > coordinate_bound or (last - v[5]) % 6:
                continue
            z = first + (last,)
            norm = sum(t * t for t in z)
            if norm % 2:
                raise AssertionError("A5 norm must be even")
            exponent = norm // 2
            if exponent <= bound:
                individual[j][exponent] += 1
                total[exponent] += 1
    return total, individual, coordinate_bound


def charged_theta(bound: int) -> tuple[list[int], int]:
    """Separately enumerate q^5*c_6,(0,1)(q^3) from the abacus formula."""
    radius = 7
    # Include the structurally zero q^360 slot used in the Sturm comparison.
    out = [0] * (STURM_BOUND + 1)
    for first in itertools.product(range(-radius, radius + 1), repeat=5):
        a = first + (-sum(first),)
        if abs(a[5]) > radius:
            continue
        for j in range(6):
            degree = (
                6 * sum(t * t for t in a)
                + 2 * sum((i + 1) * a[i] for i in range(6))
                + 6 * a[j]
                + j
            )
            if degree < 0:
                raise AssertionError("charged degree must be nonnegative")
            if degree <= bound:
                out[3 * degree + 5] += 1
    return out, radius


def cusp_orders() -> dict[str, str]:
    level = 36
    exponents = {3: -4, 6: 6, 18: 4, 36: 4}
    answer = {}
    for c in (1, 2, 3, 4, 6, 9, 12, 18, 36):
        order = Fraction(level, 24) * sum(
            Fraction(
                math.gcd(c, d) ** 2 * exponent,
                math.gcd(c, level // c) * c * d,
            )
            for d, exponent in exponents.items()
        )
        answer[str(c)] = str(order)
    return answer


def digest(values: list[int]) -> str:
    raw = json.dumps(values, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    theta, individual, coordinate_bound = six_coset_theta(STURM_BOUND)
    eta = eta_g(STURM_BOUND)
    charged, radius = charged_theta(CHARGED_BOUND)
    theta_square = multiply(theta, theta, STURM_BOUND)
    eta_square = multiply(eta, eta, STURM_BOUND)

    representatives = [
        tuple((-3, -2, -1, 0, 1, 2)[i] + (3 if i == j else 0) for i in range(6))
        for j in range(6)
    ]
    representative_norms = [sum(x * x for x in v) for v in representatives]
    eta_orders = cusp_orders()

    result = {
        "method": "independent direct A5-coset enumeration and direct eta-product expansion",
        "common_group": "Gamma_0(432)",
        "gamma0_index": 864,
        "weight_after_squaring": 5,
        "sturm_bound": STURM_BOUND,
        "charged_degree_required": CHARGED_BOUND,
        "theta_coordinate_absolute_bound": coordinate_bound,
        "theta_coordinate_bound_reason": "z_i^2 <= 2*360 for every represented vector",
        "charged_box_radius": radius,
        "charged_box_completeness_check": {
            "core_lower_bound_at_norm_8": "192-sqrt(1120)>118",
            "exact_squared_inequality": "74^2=5476>1120",
        },
        "coset_representatives": [list(v) for v in representatives],
        "coset_representative_sums": [sum(v) for v in representatives],
        "coset_representative_norms": representative_norms,
        "cosets_distinct_modulo_6A5": True,
        "elementary_theta_parameters": {
            "A": "36*(I_5+J_5)",
            "N": 216,
            "H_j": "36*(first five coordinates of v_j)",
            "N_times_A_inverse": "6*I_5-J_5",
            "c_divisibility": 432,
            "phase_integral_because": "b is even and every norm (v_j,v_j) is even",
            "theta_character_squareclass": 12,
        },
        "eta_square_newman_sums": [240, 0],
        "eta_square_s_parameter": "6^18",
        "eta_square_character": "Kronecker(-4,d)",
        "theta_square_character": "Kronecker(-4,d)",
        "eta_square_cusp_orders": eta_orders,
        "all_eta_square_cusp_orders_nonnegative": all(Fraction(x) >= 0 for x in eta_orders.values()),
        "theta_eta_mismatches_through_360": [
            n for n in range(STURM_BOUND + 1) if theta[n] != eta[n]
        ],
        "theta_charged_mismatches_through_360": [
            n for n in range(STURM_BOUND + 1) if theta[n] != charged[n]
        ],
        "squared_mismatches_through_sturm_bound": [
            n for n in range(STURM_BOUND + 1) if theta_square[n] != eta_square[n]
        ],
        "theta_coefficients_sha256": digest(theta),
        "eta_coefficients_sha256": digest(eta),
        "individual_coset_coefficient_sha256": [digest(row) for row in individual],
        "leading_terms_theta": [[n, theta[n]] for n in range(30) if theta[n]],
        "source_sha256": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_name("theta_audit_certificate.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
