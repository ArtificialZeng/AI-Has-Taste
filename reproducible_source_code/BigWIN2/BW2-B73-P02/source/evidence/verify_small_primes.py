#!/usr/bin/env python3
"""Exact replay of equations (4)--(5) and affine point counts for four rows."""

WITNESSES = (
    (5, 1, 1, 8, 2, 3),
    (7, 0, 1, 11, 3, 4),
    (11, 1, 3, 17, 5, 6),
    (13, 0, 4, 20, 6, 7),
)


def truncated_subtraction(x, y):
    return max(x - y, 0)


def equation_4(p, a, b):
    """Return (extracted base-2^(p^2) digit, r), using the printed integer term."""
    w = p * p
    base = (1 << (3 * w)) + (a % p) * (1 << w) + (b % p)
    digit = (base ** (p // 2) // (1 << (w * (p - 1)))) % (1 << w)
    return digit, digit % p


def coefficient_x_p_minus_1(p, a, b):
    """Independently expand (x^3+a*x+b)^floor(p/2) over the integers."""
    coefficients = [1]
    factor = [b % p, a % p, 0, 1]
    for _ in range(p // 2):
        product = [0] * (len(coefficients) + 3)
        for i, left in enumerate(coefficients):
            for j, right in enumerate(factor):
                product[i + j] += left * right
        coefficients = product
    return coefficients[p - 1]


def equation_5(p, r):
    indicator = truncated_subtraction(
        1, truncated_subtraction(4 * p + 1, r * r)
    )
    return truncated_subtraction(p, r) + p * indicator


def affine_point_count(p, a, b):
    return sum(
        (y * y - (x * x * x + a * x + b)) % p == 0
        for x in range(p)
        for y in range(p)
    )


def main():
    print("p A B disc digit coeff r N_direct Nhat row_ok")
    all_ok = True
    for p, a, b, expected_n, expected_r, expected_nhat in WITNESSES:
        digit, r = equation_4(p, a, b)
        coefficient = coefficient_x_p_minus_1(p, a, b)
        direct_n = affine_point_count(p, a, b)
        nhat = equation_5(p, r)
        discriminant = (4 * a**3 + 27 * b**2) % p
        row_ok = (
            discriminant != 0
            and digit == coefficient
            and direct_n == expected_n
            and r == expected_r
            and nhat == expected_nhat
            and direct_n != nhat
        )
        all_ok &= row_ok
        print(
            p, a, b, discriminant, digit, coefficient, r,
            direct_n, nhat, str(row_ok).lower()
        )
    print(f"all_rows_ok={str(all_ok).lower()}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
