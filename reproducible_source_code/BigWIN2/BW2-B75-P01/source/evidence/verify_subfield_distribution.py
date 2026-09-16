#!/usr/bin/env python3
"""Exact small-field check of the reduced fibre-count formulation.

Elements of GF(2^m) are bit-polynomials modulo the printed irreducible
polynomial.  No external finite-field package is used.
"""

from collections import Counter


def degree(a):
    return a.bit_length() - 1


def poly_mod(a, modulus):
    md = degree(modulus)
    while degree(a) >= md:
        a ^= modulus << (degree(a) - md)
    return a


def poly_gcd(a, b):
    while b:
        a, b = b, poly_mod(a, b)
    return a


def multiply(a, b, modulus, m):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << m):
            a ^= modulus
    return result


def square(a, modulus, m):
    return multiply(a, a, modulus, m)


def power(a, exponent, modulus, m):
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus, m)
        a = square(a, modulus, m)
        exponent >>= 1
    return result


def is_irreducible(modulus, m):
    x = poly_mod(2, modulus)
    x_power = x
    for i in range(1, m + 1):
        x_power = square(x_power, modulus, m)
        if i <= m // 2 and poly_gcd(x_power ^ x, modulus) != 1:
            return False
    return x_power == x


def first_irreducible(m):
    for low_bits in range(1, 1 << m, 2):
        modulus = (1 << m) | low_bits
        if is_irreducible(modulus, m):
            return modulus
    raise RuntimeError(f"no irreducible polynomial found in degree {m}")


def absolute_trace(a, modulus, m):
    value = 0
    conjugate = a
    for _ in range(m):
        value ^= conjugate
        conjugate = square(conjugate, modulus, m)
    assert value in (0, 1)
    return value


def check(m, c_previous_2, c_previous_1):
    q = 1 << m
    modulus = first_irreducible(m)
    fibres = Counter()
    for y in range(1, q):
        inverse = power(y, q - 2, modulus, m)
        if absolute_trace(inverse, modulus, m) == 1:
            y2 = square(y, modulus, m)
            y3 = multiply(y2, y, modulus, m)
            a = y3 ^ y2 ^ 1
            fibres[a] += 1
    distribution = Counter(fibres.get(a, 0) for a in range(q))
    if m == 1:
        c = 1
    elif m == 2:
        c = -3
    else:
        c = c_previous_1 - 2 * c_previous_2
    d = -2 + (-1) ** m + c
    predicted = {0: (5 * q + d) // 8, 1: (q - d) // 4, 2: (q + d) // 8}
    observed = {k: distribution[k] for k in (0, 1, 2)}
    assert sum(fibres.values()) == q // 2
    assert max(distribution) <= 2
    assert observed == predicted
    print(
        f"m={m:2d} modulus=0x{modulus:x} c={c:6d} d={d:6d} "
        f"fibres(0,1,2)=({observed[0]},{observed[1]},{observed[2]}) OK"
    )
    return c


def main():
    c_values = []
    for m in range(1, 16):
        c = check(
            m,
            c_values[-2] if len(c_values) >= 2 else None,
            c_values[-1] if c_values else None,
        )
        c_values.append(c)


if __name__ == "__main__":
    main()
