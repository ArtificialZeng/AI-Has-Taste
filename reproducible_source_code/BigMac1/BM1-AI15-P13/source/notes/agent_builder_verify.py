#!/usr/bin/env python3
"""Exact rational verifier for the Builder's scalar SM--IR certificate.

This does not use host floating point.  It implements unbounded-exponent,
precision-p, radix-2 round-to-nearest/ties-to-even arithmetic with Fraction.
The certificate values are far from IEEE exponent limits, so this is also the
relevant IEEE-754 result for any format whose normal range contains 2**p.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def pow2(e: int) -> Fraction:
    return Fraction(1 << e, 1) if e >= 0 else Fraction(1, 1 << (-e))


def floor_log2_pos(x: Fraction) -> int:
    assert x > 0
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < pow2(e):
        e -= 1
    assert pow2(e) <= x < pow2(e + 1)
    return e


def round_nearest_even_integer(q: Fraction) -> int:
    assert q >= 0
    lo = q.numerator // q.denominator
    rem = q.numerator - lo * q.denominator
    twice = 2 * rem
    if twice < q.denominator:
        return lo
    if twice > q.denominator:
        return lo + 1
    return lo if lo % 2 == 0 else lo + 1


def rn(x: Fraction, precision: int) -> Fraction:
    """Round x to a normal radix-2 precision-p value, with unbounded exponents."""
    assert precision >= 2
    if x == 0:
        return Fraction(0)
    sign = -1 if x < 0 else 1
    ax = abs(x)
    exponent = floor_log2_pos(ax)
    spacing = pow2(exponent - (precision - 1))
    significand_integer = round_nearest_even_integer(ax / spacing)
    return sign * significand_integer * spacing


def add(x: Fraction, y: Fraction, p: int) -> Fraction:
    return rn(x + y, p)


def sub(x: Fraction, y: Fraction, p: int) -> Fraction:
    return rn(x - y, p)


def mul(x: Fraction, y: Fraction, p: int) -> Fraction:
    return rn(x * y, p)


def div(x: Fraction, y: Fraction, p: int) -> Fraction:
    assert y != 0
    return rn(x / y, p)


def verify_scalar(precision: int, steps: int) -> None:
    p = precision
    a = Fraction(1)
    u = Fraction(1)
    v = Fraction(1 << p)
    b = Fraction(1)
    bmat = a + u * v  # mathematical B, not rounded

    assert rn(v + 1, p) == v
    assert bmat == v + 1
    # Every nonzero scalar matrix has spectral condition number one.
    kappa_a = Fraction(1)
    kappa_b = Fraction(1)

    y = div(b, a, p)
    z = div(u, a, p)
    alpha = mul(v, y, p)
    vz = mul(v, z, p)
    beta_hat = add(Fraction(1), vz, p)
    theta = div(alpha, beta_hat, p)
    theta_z = mul(theta, z, p)
    x = sub(y, theta_z, p)

    assert (y, z, alpha, vz, beta_hat, theta, x) == (
        Fraction(1),
        Fraction(1),
        v,
        v,
        v,
        Fraction(1),
        Fraction(0),
    )

    for _ in range(steps):
        # Paper's separated residual: b - A*x - (v*x)*u.
        p1 = sub(b, mul(a, x, p), p)
        p2 = mul(mul(v, x, p), u, p)
        residual_hat = sub(p1, p2, p)

        y_r = div(residual_hat, a, p)
        alpha_r = mul(v, y_r, p)
        theta_r = div(alpha_r, beta_hat, p)
        correction_term = mul(theta_r, z, p)
        # Algorithm 2, Step 5, evaluated left to right.
        w = sub(add(x, y_r, p), correction_term, p)

        assert residual_hat == 1
        assert y_r == 1
        assert alpha_r == v
        assert theta_r == 1
        assert correction_term == 1
        assert w == 0
        x = w

    true_residual = b - bmat * x
    eta = abs(true_residual) / (abs(bmat) * abs(x) + abs(b))
    assert x == 0
    assert eta == 1
    assert kappa_a == 1 and kappa_b == 1

    print(
        "CERTIFIED_SCALAR",
        f"p={p}",
        f"steps={steps}",
        f"B={bmat}",
        f"beta_hat={beta_hat}",
        f"x={x}",
        f"eta={eta}",
        f"kappa_A={kappa_a}",
        f"kappa_B={kappa_b}",
    )


def dot(x: tuple[Fraction, ...], y: tuple[Fraction, ...], p: int) -> Fraction:
    assert len(x) == len(y) and len(x) > 0
    total = mul(x[0], y[0], p)
    for xi, yi in zip(x[1:], y[1:]):
        total = add(total, mul(xi, yi, p), p)
    return total


def diagonal_matvec(
    diagonal: tuple[Fraction, ...], x: tuple[Fraction, ...], p: int
) -> tuple[Fraction, ...]:
    assert len(diagonal) == len(x)
    return tuple(mul(ai, xi, p) for ai, xi in zip(diagonal, x))


def diagonal_solve(
    diagonal: tuple[Fraction, ...], rhs: tuple[Fraction, ...], p: int
) -> tuple[Fraction, ...]:
    assert len(diagonal) == len(rhs)
    return tuple(div(ri, ai, p) for ai, ri in zip(diagonal, rhs))


def vector_add(
    x: tuple[Fraction, ...], y: tuple[Fraction, ...], p: int
) -> tuple[Fraction, ...]:
    return tuple(add(xi, yi, p) for xi, yi in zip(x, y))


def vector_sub(
    x: tuple[Fraction, ...], y: tuple[Fraction, ...], p: int
) -> tuple[Fraction, ...]:
    return tuple(sub(xi, yi, p) for xi, yi in zip(x, y))


def scalar_vector_mul(
    alpha: Fraction, x: tuple[Fraction, ...], p: int
) -> tuple[Fraction, ...]:
    return tuple(mul(alpha, xi, p) for xi in x)


def verify_two_by_two(precision: int, steps: int) -> None:
    p = precision
    assert p >= 4
    m = p // 2
    scale = Fraction(1 << m)
    huge = Fraction(1 << p)
    zero = Fraction(0)
    one = Fraction(1)

    diagonal_a = (one, scale)
    u = (one, zero)
    v = (huge, zero)
    b = (one, zero)
    # Exact mathematical B; its first diagonal entry is deliberately not a
    # floating-point number.
    diagonal_b = (huge + one, scale)
    kappa_a = scale
    kappa_b = (huge + one) / scale

    y = diagonal_solve(diagonal_a, b, p)
    z = diagonal_solve(diagonal_a, u, p)
    alpha = dot(v, y, p)
    vz = dot(v, z, p)
    beta_hat = add(one, vz, p)
    theta = div(alpha, beta_hat, p)
    x = vector_sub(y, scalar_vector_mul(theta, z, p), p)

    assert y == (one, zero)
    assert z == (one, zero)
    assert alpha == huge and vz == huge and beta_hat == huge
    assert theta == one and x == (zero, zero)

    for _ in range(steps):
        # b - A*x - (v^T*x)u, with every operation rounded at precision p.
        p1 = vector_sub(b, diagonal_matvec(diagonal_a, x, p), p)
        p2 = scalar_vector_mul(dot(v, x, p), u, p)
        residual_hat = vector_sub(p1, p2, p)

        y_r = diagonal_solve(diagonal_a, residual_hat, p)
        alpha_r = dot(v, y_r, p)
        theta_r = div(alpha_r, beta_hat, p)
        correction_term = scalar_vector_mul(theta_r, z, p)
        w = vector_sub(vector_add(x, y_r, p), correction_term, p)

        assert residual_hat == (one, zero)
        assert y_r == (one, zero)
        assert alpha_r == huge and theta_r == one
        assert correction_term == (one, zero)
        assert w == (zero, zero)
        x = w

    # Since x=0 and ||b||_2=1, both standard relative backward errors equal 1.
    eta = one
    assert x == (zero, zero) and eta == one
    assert kappa_a == (1 << m)
    assert kappa_b == Fraction((1 << p) + 1, 1 << m)
    assert Fraction(1, 1 << p) * kappa_a <= Fraction(1, 4)
    assert Fraction(1, 1 << p) * kappa_b < Fraction(1, 2)

    print(
        "CERTIFIED_2X2",
        f"p={p}",
        f"steps={steps}",
        f"A_diag=(1,{scale})",
        f"B_diag=({huge + 1},{scale})",
        f"beta_hat={beta_hat}",
        f"x={x}",
        f"eta={eta}",
        f"kappa_A={kappa_a}",
        f"kappa_B={kappa_b}",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=53)
    parser.add_argument("--steps", type=int, default=100)
    args = parser.parse_args()
    assert args.steps >= 0
    verify_scalar(args.precision, args.steps)
    verify_two_by_two(args.precision, args.steps)


if __name__ == "__main__":
    main()
