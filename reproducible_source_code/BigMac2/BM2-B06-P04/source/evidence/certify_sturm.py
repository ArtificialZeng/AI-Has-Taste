#!/usr/bin/env python3
"""Exact arithmetic certificate for the pass-2 Sturm comparison.

This does not certify modularity (that is the mathematical argument in
``research_pass2.md``).  It independently records every finite arithmetic
quantity used after modularity has been established: the common-group index,
Sturm bound, eta cusp orders, the A5 Gram data, and the coefficient comparison
through the bound.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

from enumerate_series import charged_coefficients, multiply_truncated, three_core_coefficients


def psi(max_degree: int, scale: int = 1) -> list[int]:
    out = [0] * (max_degree + 1)
    r = 0
    while scale * r * (r + 1) // 2 <= max_degree:
        out[scale * r * (r + 1) // 2] = 1
        r += 1
    return out


def dilate(series: list[int], scale: int, max_degree: int) -> list[int]:
    out = [0] * (max_degree + 1)
    for n, value in enumerate(series):
        if scale * n <= max_degree:
            out[scale * n] = value
    return out


def eta_square_cusp_orders() -> dict[str, str]:
    """Ligozat orders for (eta(6z)^3 eta(18z)^2 eta(36z)^2/eta(3z)^2)^2."""
    level = 36
    exponents = {3: -4, 6: 6, 18: 4, 36: 4}
    answer: dict[str, str] = {}
    for c in (1, 2, 3, 4, 6, 9, 12, 18, 36):
        order = Fraction(level, 24) * sum(
            Fraction(math.gcd(c, d) ** 2 * r, math.gcd(c, level // c) * c * d)
            for d, r in exponents.items()
        )
        answer[str(c)] = str(order)
    return answer


def main() -> None:
    # Shimura's elementary-theta realization uses matrix 36*(I_5+J_5),
    # modulus 216, and initially c == 0 (mod 432), b == 0 (mod 2).
    # Integer exponents give T-invariance, extending the result to Gamma_0(432).
    theta_level = 432
    gamma0_index = theta_level * Fraction(3, 2) * Fraction(4, 3)
    common_index = gamma0_index
    sturm_bound = 5 * common_index // 12
    assert gamma0_index == 864 and common_index == 864 and sturm_bound == 360

    # q^5 C(q^3) only uses C_n with 3n+5 <= B.
    charged_bound = (sturm_bound - 5) // 3
    charged, radius, core_count = charged_coefficients(charged_bound, 1)
    c3_q2 = dilate(three_core_coefficients(charged_bound // 2), 2, charged_bound)
    product = multiply_truncated(
        multiply_truncated(psi(charged_bound), psi(charged_bound), charged_bound),
        multiply_truncated(c3_q2, psi(charged_bound, 6), charged_bound),
        charged_bound,
    )
    mismatches = [n for n in range(charged_bound + 1) if charged[n] != product[n]]
    transformed_charged = [0] * (sturm_bound + 1)
    transformed_product = [0] * (sturm_bound + 1)
    for n in range(charged_bound + 1):
        transformed_charged[3 * n + 5] = charged[n]
        transformed_product[3 * n + 5] = product[n]
    square_charged = multiply_truncated(transformed_charged, transformed_charged, sturm_bound)
    square_product = multiply_truncated(transformed_product, transformed_product, sturm_bound)
    square_mismatches = [
        n for n in range(sturm_bound + 1) if square_charged[n] != square_product[n]
    ]

    # In the basis e_i-e_6, the A5 Gram matrix is I_5+J_5, with determinant 6
    # and inverse I_5-J_5/6.  Six times its inverse is integral.
    six_gram_inverse = [
        [5 if i == j else -1 for j in range(5)] for i in range(5)
    ]

    result = {
        "theta_coset_group": "Gamma_0(432)",
        "theta_character": "Kronecker(12,d)",
        "theta_square_character": "Kronecker(-4,d)",
        "eta_square_group": "Gamma_0(36)",
        "eta_square_character": "Kronecker(-4,d)",
        "common_group": "Gamma_0(432)",
        "a5_gram_determinant": 6,
        "a5_level": 6,
        "six_times_a5_gram_inverse": six_gram_inverse,
        "shimura_elementary_theta_matrix_scale": 36,
        "shimura_elementary_theta_modulus": 216,
        "shimura_c_divisibility": 432,
        "eta_exponent_sums": {
            "sum_delta_r_delta": 240,
            "sum_36_over_delta_r_delta": 0,
        },
        "eta_square_cusp_orders_by_denominator_c": eta_square_cusp_orders(),
        "gamma0_432_index": int(gamma0_index),
        "common_group_index": int(common_index),
        "integral_weight_after_squaring": 5,
        "sturm_bound": int(sturm_bound),
        "charged_degree_required": int(charged_bound),
        "enumeration_box_radius": radius,
        "six_core_vectors_after_size_cut": core_count,
        "coefficient_mismatches_through_required_degree": mismatches,
        "square_coefficient_mismatches_through_sturm_bound": square_mismatches,
        "largest_checked_exponent_after_q5_and_q_to_q3": 3 * charged_bound + 5,
        "coefficient_at_sturm_bound_is_structurally_zero": sturm_bound % 3 != 2,
        "all_coefficients_compared_through_q_exponent": int(sturm_bound),
        "all_eta_square_cusp_orders_nonnegative": all(
            Fraction(x) >= 0 for x in eta_square_cusp_orders().values()
        ),
    }
    output = Path(__file__).with_name("sturm_certificate.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
