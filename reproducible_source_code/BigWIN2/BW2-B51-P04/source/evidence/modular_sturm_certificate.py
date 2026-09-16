#!/usr/bin/env python3
"""Exact Sturm-bound replay for the first congruence in Conjecture 7.1.

All coefficient arithmetic is performed in F_5.  The modular-form proof in
``resolution_proof.md`` reduces the infinite assertion to equality through
degree 180 between

    U_5(q^25 f_5^120 F(q))  and  q^5 f_1^120,

where F=f_4^8/(f_1^16 f_2^8).  Since E_4^2 is 1 modulo 5, this is exactly
the coefficient check required for the weight-60 Sturm comparison.
"""

MODULUS = 5
STURM_BOUND = 180


def multiply_euler_power(coeff: list[int], step: int, exponent: int) -> None:
    """Multiply coeff by product_m (1-q^(step*m))^exponent, in place."""
    limit = len(coeff) - 1
    for degree in range(step, limit + 1, step):
        if exponent >= 0:
            for _ in range(exponent):
                for n in range(limit, degree - 1, -1):
                    coeff[n] = (coeff[n] - coeff[n - degree]) % MODULUS
        else:
            for _ in range(-exponent):
                for n in range(degree, limit + 1):
                    coeff[n] = (coeff[n] + coeff[n - degree]) % MODULUS


def shifted_eta_quotient(limit: int, shift: int,
                         exponents: dict[int, int]) -> list[int]:
    """Return q^shift times the indicated f_j product through q^limit."""
    if shift > limit:
        return [0] * (limit + 1)
    body = [1] + [0] * (limit - shift)
    for step, exponent in sorted(exponents.items()):
        multiply_euler_power(body, step, exponent)
    return [0] * shift + body


def main() -> None:
    # A(z)=eta(4z)^8 eta(5z)^120/(eta(z)^16 eta(2z)^8)
    #     =q^25 f_4^8 f_5^120/(f_1^16 f_2^8).
    a = shifted_eta_quotient(
        5 * STURM_BOUND,
        shift=25,
        exponents={1: -16, 2: -8, 4: 8, 5: 120},
    )
    u5_a = [a[5 * n] for n in range(STURM_BOUND + 1)]

    # Delta(z)^5=eta(z)^120=q^5 f_1^120.
    delta5 = shifted_eta_quotient(
        STURM_BOUND, shift=5, exponents={1: 120}
    )

    failures = [
        (n, u5_a[n], delta5[n])
        for n in range(STURM_BOUND + 1)
        if u5_a[n] != delta5[n]
    ]
    print(f"modulus={MODULUS}")
    print("level=20")
    print("comparison_weight=60")
    print("index_gamma0=36")
    print(f"sturm_bound={STURM_BOUND}")
    print(f"checked_coefficients=0..{STURM_BOUND}")
    print(f"failures={failures}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
