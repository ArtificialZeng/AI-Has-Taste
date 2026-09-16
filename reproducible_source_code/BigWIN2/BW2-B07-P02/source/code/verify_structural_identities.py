#!/usr/bin/env python3
"""Exact low-degree cross-check of the structural factorization."""

from argparse import ArgumentParser
from fractions import Fraction
from math import factorial


def multiply(left, right, limit):
    out = [Fraction(0) for _ in range(limit + 1)]
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right[: limit - i + 1]):
            if y:
                out[i + j] += x * y
    return out


def exponential_from_log(log_coeff, limit):
    out = [Fraction(0) for _ in range(limit + 1)]
    out[0] = 1
    for n in range(1, limit + 1):
        out[n] = sum(
            (m * log_coeff[m] * out[n - m] for m in range(1, n + 1)),
            Fraction(0),
        ) / n
    return out


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()
    limit = args.limit

    q = [Fraction(0) for _ in range(limit + 1)]
    q[0] = Fraction(1)
    for k in range(1, limit + 1):
        for n in range(limit, k - 1, -1):
            q[n] += q[n - k] / k
    f_direct = [q[n] - (q[n - 1] if n else 0) for n in range(limit + 1)]

    w_log = [Fraction(0) for _ in range(limit // 2 + 1)]
    for n in range(2, len(w_log)):
        w_log[n] = Fraction(-1, 2 * n * n)
    w = exponential_from_log(w_log, len(w_log) - 1)
    assert w[0] == 1 and w[1] == 0
    assert all(w[n] < 0 for n in range(2, len(w)))
    assert all(-w[n] <= Fraction(1, 2 * n * n) for n in range(2, len(w)))

    r_log = [Fraction(0) for _ in range(limit + 1)]
    for exponent in range(3, limit + 1):
        sign = 1 if exponent % 2 else -1
        for base in range(2, limit // exponent + 1):
            r_log[exponent * base] += Fraction(
                sign, exponent * base**exponent
            )
    k_series = exponential_from_log(r_log, limit)

    b = [Fraction(0) for _ in range(limit + 1)]
    b[0] = 1
    b[1] = 0
    for n in range(2, limit + 1):
        b[n] = Fraction(((-1) ** n) * (1 - n), factorial(n))
    j = multiply(b, k_series, limit)

    w_of_z2 = [Fraction(0) for _ in range(limit + 1)]
    for n, value in enumerate(w):
        if 2 * n <= limit:
            w_of_z2[2 * n] = value
    f_factored = multiply(w_of_z2, j, limit)
    assert f_factored == f_direct

    print(f"exact_factorization_checked_through={limit}")
    print("difference_indexing=PASS")
    print("W_sign_and_upper_bound=PASS")
    print("factorization_F_equals_W_z2_times_J=PASS")
    print("status=PASS")


if __name__ == "__main__":
    main()
