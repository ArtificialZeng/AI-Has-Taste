#!/usr/bin/env python3
"""Independent exact audit of [q^5] prod_m (1-q^(2m))^8/(1-q^m)^16.

This implementation is intentionally separate from triage_b5.py: it uses sparse
dictionaries, a local multiplicative binomial routine, and records every
nonzero term in every truncated convolution.
"""

DEGREE = 5


def choose(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    value = 1
    for i in range(1, k + 1):
        numerator = n - k + i
        assert (value * numerator) % i == 0
        value = value * numerator // i
    return value


def numerator_factor(m):
    """(1-q^(2m))^8 modulo q^6, as an exponent: coefficient dictionary."""
    return {
        2 * m * j: (-1 if j % 2 else 1) * choose(8, j)
        for j in range(0, DEGREE // (2 * m) + 1)
    }


def denominator_factor(m):
    """(1-q^m)^(-16) modulo q^6, using the negative-binomial formula."""
    return {
        m * j: choose(15 + j, 15)
        for j in range(0, DEGREE // m + 1)
    }


def convolve(left, right):
    """Multiply modulo q^6 and retain the complete nonzero-term ledger."""
    result = {}
    ledger = {degree: [] for degree in range(DEGREE + 1)}
    for degree in range(DEGREE + 1):
        total = 0
        for left_degree in sorted(left):
            right_degree = degree - left_degree
            if right_degree in right:
                term = left[left_degree] * right[right_degree]
                ledger[degree].append(
                    (left_degree, left[left_degree], right_degree,
                     right[right_degree], term)
                )
                total += term
        if total:
            result[degree] = total
    return result, ledger


def dense(poly):
    return [poly.get(degree, 0) for degree in range(DEGREE + 1)]


def format_poly(poly):
    return "[" + ", ".join(str(x) for x in dense(poly)) + "]"


product = {0: 1}
steps = []
for m in range(1, DEGREE + 1):
    for label, factor in (
        (f"N_{m}=(1-q^{2*m})^8", numerator_factor(m)),
        (f"D_{m}=(1-q^{m})^-16", denominator_factor(m)),
    ):
        product, ledger = convolve(product, factor)
        steps.append((label, factor, dict(product), ledger))

expected_factors = {
    "N_1=(1-q^2)^8": [1, 0, -8, 0, 28, 0],
    "D_1=(1-q^1)^-16": [1, 16, 136, 816, 3876, 15504],
    "N_2=(1-q^4)^8": [1, 0, 0, 0, -8, 0],
    "D_2=(1-q^2)^-16": [1, 0, 16, 0, 136, 0],
    "N_3=(1-q^6)^8": [1, 0, 0, 0, 0, 0],
    "D_3=(1-q^3)^-16": [1, 0, 0, 16, 0, 0],
    "N_4=(1-q^8)^8": [1, 0, 0, 0, 0, 0],
    "D_4=(1-q^4)^-16": [1, 0, 0, 0, 16, 0],
    "N_5=(1-q^10)^8": [1, 0, 0, 0, 0, 0],
    "D_5=(1-q^5)^-16": [1, 0, 0, 0, 0, 16],
}
for label, factor, _, _ in steps:
    assert dense(factor) == expected_factors[label]

assert dense(product) == [1, 16, 144, 960, 5264, 25056]
assert product[5] % 5 == 1

print("All polynomials are coefficient vectors in degrees 0,...,5.")
for label, factor, partial, ledger in steps:
    print(f"\n{label}: factor={format_poly(factor)}; partial={format_poly(partial)}")
    for degree in range(DEGREE + 1):
        terms = ledger[degree]
        rendered = " + ".join(
            f"({a}@q^{i})*({b}@q^{j})={term}"
            for i, a, j, b, term in terms
        )
        print(f"  q^{degree}: {rendered or 'no nonzero terms'}"
              f" -> {partial.get(degree, 0)}")

print("\nFinal b(5) =", product[5])
print("Final b(5) mod 5 =", product[5] % 5)
