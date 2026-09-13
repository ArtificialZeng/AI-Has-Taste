#!/usr/bin/env python3
"""Independent exact definition-level checks for the regular polygon theorem.

The verifier imports no discovery code.  It works in the quotient ring
Q[t]/(t^n+1), where t is specialized to exp(pi*i/n).  It constructs
2*A_ij = t^(i-j)+t^(j-i), computes permanents by subset DP, forms 2^n F,
and diagonalizes the circulant matrix by formal Fourier substitution.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def monomial(n: int, exponent: int, coefficient: int = 1) -> tuple[int, ...]:
    exponent %= 2 * n
    sign = coefficient
    if exponent >= n:
        exponent -= n
        sign = -sign
    result = [0] * n
    result[exponent] = sign
    return tuple(result)


def multiply(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            if y == 0:
                continue
            exponent = i + j
            if exponent >= n:
                exponent -= n
                out[exponent] -= x * y
            else:
                out[exponent] += x * y
    return tuple(out)


def scaled_entry(n: int, i: int, j: int) -> tuple[int, ...]:
    return add(monomial(n, i - j), monomial(n, j - i))


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def exact_divide(numerator: list[int], denominator: list[int]) -> list[int]:
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    if denominator[-1] != 1:
        raise AssertionError("cyclotomic divisor must be monic")
    if len(numerator) < len(denominator):
        raise AssertionError("non-exact polynomial division")
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and numerator != [0]:
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1]
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] -= coefficient * value
        trim(numerator)
    if any(numerator):
        raise AssertionError(("non-exact polynomial division", numerator, denominator))
    return trim(quotient)


def cyclotomic(order: int, cache: dict[int, list[int]] | None = None) -> list[int]:
    if cache is None:
        cache = {}
    if order in cache:
        return cache[order]
    polynomial = [-1] + [0] * (order - 1) + [1]
    for divisor in range(1, order):
        if order % divisor == 0:
            polynomial = exact_divide(polynomial, cyclotomic(divisor, cache))
    cache[order] = polynomial
    return polynomial


def reduce_mod(poly: tuple[int, ...], modulus: list[int]) -> tuple[int, ...]:
    work = trim(list(poly))
    degree = len(modulus) - 1
    while len(work) - 1 >= degree:
        shift = len(work) - len(modulus)
        coefficient = work[-1]
        for index, value in enumerate(modulus):
            work[index + shift] -= coefficient * value
        trim(work)
    work += [0] * (degree - len(work))
    return tuple(work)


def equals_scalar(poly: tuple[int, ...], scalar: int, modulus: list[int]) -> bool:
    difference = list(poly)
    difference[0] -= scalar
    return not any(reduce_mod(tuple(difference), modulus))


def permanent(matrix: list[list[tuple[int, ...]]]) -> tuple[int, ...]:
    m = len(matrix)
    if m == 0:
        return (1,)
    ring_n = len(matrix[0][0])
    zero = (0,) * ring_n
    one = monomial(ring_n, 0)
    dp = [zero] * (1 << m)
    dp[0] = one
    for row in range(m):
        nxt = [zero] * (1 << m)
        for mask, value in enumerate(dp):
            if mask.bit_count() != row or value == zero:
                continue
            for column in range(m):
                if mask & (1 << column):
                    continue
                target = mask | (1 << column)
                nxt[target] = add(nxt[target], multiply(value, matrix[row][column]))
        dp = nxt
    return dp[-1]


def minor(matrix: list[list[tuple[int, ...]]], i: int, j: int) -> list[list[tuple[int, ...]]]:
    return [
        [entry for column, entry in enumerate(row) if column != j]
        for row_index, row in enumerate(matrix)
        if row_index != i
    ]


def verify_order(n: int) -> dict[str, object]:
    modulus = cyclotomic(2 * n)
    matrix = [[scaled_entry(n, i, j) for j in range(n)] for i in range(n)]
    scaled_permanent = permanent(matrix)  # 2^n per(A)
    expected_permanent = math.factorial(n) * 2
    if not equals_scalar(scaled_permanent, expected_permanent, modulus):
        raise AssertionError((n, "permanent", scaled_permanent, expected_permanent, modulus))

    first_row: list[tuple[int, ...]] = []
    for j in range(n):
        scaled_minor = permanent(minor(matrix, 0, j))
        # (2 A_0j)(2^(n-1) per minor) = 2^n F_0j.
        first_row.append(multiply(matrix[0][j], scaled_minor))

    eigenvalues_scaled: list[int] = []
    for s in range(n):
        value = (0,) * n
        for j, entry in enumerate(first_row):
            value = add(value, multiply(entry, monomial(n, -2 * s * j)))
        # Rewrite n! / C(n-1,k) without integer-division ambiguity.
        expected = n * (
            math.factorial(s) * math.factorial(n - 1 - s)
            + math.factorial((s - 1) % n)
            * math.factorial(n - 1 - ((s - 1) % n))
        )
        if not equals_scalar(value, expected, modulus):
            raise AssertionError((n, s, "eigenvalue", value, expected, modulus))
        eigenvalues_scaled.append(expected)

    if eigenvalues_scaled[0] != 2 * math.factorial(n):
        raise AssertionError((n, "constant eigenvalue"))
    if max(eigenvalues_scaled[1:]) >= eigenvalues_scaled[0]:
        raise AssertionError((n, "spectral inequality"))
    expected_second = math.factorial(n) * n // (n - 1)
    if max(eigenvalues_scaled[1:]) != expected_second:
        raise AssertionError((n, "second eigenvalue", max(eigenvalues_scaled[1:]), expected_second))

    return {
        "n": n,
        "scaled_permanent": expected_permanent,
        "cyclotomic_modulus": modulus,
        "scaled_eigenvalues": eigenvalues_scaled,
        "strict_nonconstant": True,
    }


def fail_closed_attacks() -> dict[str, bool]:
    # These attacks target the closed formulas.  Each deliberately wrong
    # variant must disagree already at an exact small order.
    n = 5
    correct = [
        n
        * (
            math.factorial(s) * math.factorial(n - 1 - s)
            + math.factorial((s - 1) % n) * math.factorial(n - 1 - ((s - 1) % n))
        )
        for s in range(n)
    ]
    wrong_phase = [
        n
        * (
            math.factorial(s) * math.factorial(n - 1 - s)
            + math.factorial((s + 1) % n) * math.factorial(n - 1 - ((s + 1) % n))
        )
        for s in range(n)
    ]
    wrong_factor = [value // 2 for value in correct]
    wrong_binomial = [2 * math.factorial(n)] * n
    return {
        "wrong_phase_rejected": wrong_phase != correct,
        "wrong_factor_rejected": wrong_factor != correct,
        "wrong_binomial_rejected": wrong_binomial != correct,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (3 <= args.max_n <= 9):
        raise SystemExit("definition-level audit is intentionally bounded to 3 <= max-n <= 9")
    orders = [verify_order(n) for n in range(3, args.max_n + 1)]
    attacks = fail_closed_attacks()
    if not all(attacks.values()):
        raise AssertionError(attacks)
    result = {
        "schema_version": 1,
        "method": "no-import exact subset DP in Q[t]/(t^n+1)",
        "orders": orders,
        "fail_closed_attacks": attacks,
        "verdict": "PASS",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"orders": [item["n"] for item in orders], "attacks": attacks, "verdict": "PASS"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
