#!/usr/bin/env python3
"""Exact certificate for the 4,774-factor / 19,927-digit deduction."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [p for p in range(2, limit + 1) if sieve[p]]


def integer_digest(value: int) -> str:
    return hashlib.sha256(
        value.to_bytes((value.bit_length() + 7) // 8, "big")
    ).hexdigest()


def digit_certificate(values: list[int], expected_digits: int) -> dict[str, object]:
    product = 1
    for value in values:
        product *= value
    assert 10 ** (expected_digits - 1) <= product < 10**expected_digits
    return {
        "factor_count": len(values),
        "first_prime": values[0],
        "last_prime": values[-1],
        "decimal_digits": expected_digits,
        "product_bit_length": product.bit_length(),
        "product_sha256_binary": integer_digest(product),
    }


def main() -> None:
    primes = primes_up_to(50_000)
    odd_primes = primes[1:]
    first_eight_sum = sum(
        (Fraction(1, p) for p in odd_primes[:8]), Fraction()
    )
    assert odd_primes[:8] == [3, 5, 7, 11, 13, 17, 19, 23]
    assert first_eight_sum == Fraction(111_429_982, 111_546_435)
    assert first_eight_sum < 1

    value_one_primes = odd_primes[1 : 1 + 4_774]
    value_ge_two_primes = odd_primes[:4_779]
    assert value_one_primes[-1] == 46_171
    assert value_ge_two_primes[-1] == 46_199

    a_one = digit_certificate(value_one_primes, 19_927)
    a_ge_two = digit_certificate(value_ge_two_primes, 19_946)
    assert a_one["product_sha256_binary"] == (
        "486c2ff49e48a4a25c49910183e99b8989a1eb9e0a61a5352fff3b9c610e3a09"
    )
    assert a_ge_two["product_sha256_binary"] == (
        "d2b8cbd8813e4e4219e121175e2c86ac0b084efb4c28e070ebe52e220f33e029"
    )
    output = {
        "schema_version": 1,
        "exact_first_eight_odd_prime_reciprocal_sum": {
            "numerator": first_eight_sum.numerator,
            "denominator": first_eight_sum.denominator,
            "gap_numerator": (1 - first_eight_sum).numerator,
            "gap_denominator": (1 - first_eight_sum).denominator,
        },
        "a_equals_one_case": a_one,
        "a_at_least_two_case": a_ge_two,
        "universal_conclusion": {
            "distinct_prime_factors_at_least": 4_774,
            "decimal_digits_at_least": 19_927,
        },
    }
    certificate_path = (
        Path(__file__).resolve().parents[1]
        / "experiments"
        / "improved_bound_certificate.json"
    )
    assert output == json.loads(certificate_path.read_text(encoding="utf-8"))
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
