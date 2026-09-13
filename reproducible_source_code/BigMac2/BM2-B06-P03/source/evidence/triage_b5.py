#!/usr/bin/env python3
"""Exact triage computation of [q^5] f_2^8/f_1^16; no external packages."""

from math import comb

DEGREE = 5


def multiply(left, right):
    out = [0] * (DEGREE + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= DEGREE:
                out[i + j] += a * b
    return out


def original_euler_product():
    coeff = [1] + [0] * DEGREE
    for m in range(1, DEGREE + 1):
        numerator = [0] * (DEGREE + 1)
        denominator_inverse = [0] * (DEGREE + 1)
        for j in range(9):
            if 2 * m * j <= DEGREE:
                numerator[2 * m * j] = (-1) ** j * comb(8, j)
        for j in range(DEGREE // m + 1):
            denominator_inverse[m * j] = comb(j + 15, 15)
        coeff = multiply(coeff, numerator)
        coeff = multiply(coeff, denominator_inverse)
    return coeff


def cancelled_euler_product():
    coeff = [1] + [0] * DEGREE
    for m in range(1, DEGREE + 1):
        factor = [0] * (DEGREE + 1)
        for total in range(DEGREE // m + 1):
            factor[m * total] = sum(
                comb(8, j) * comb(total - j + 7, 7)
                for j in range(min(8, total) + 1)
            )
        coeff = multiply(coeff, factor)
    return coeff


first = original_euler_product()
second = cancelled_euler_product()
assert first == second
assert first == [1, 16, 144, 960, 5264, 25056]
print("coefficients q^0..q^5:", first)
print("b(5) =", first[5])
print("b(5) mod 5 =", first[5] % 5)
