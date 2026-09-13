#!/usr/bin/env python3
"""Exact verifier for the mac01-p15 witness, using an LCM numerator sum."""

from __future__ import annotations

import hashlib
import json
import math
import pathlib
import sys


EXPECTED_KEYS = {"schema_version", "n", "p", "expected_h", "claim"}
EXPECTED_CLAIM = (
    "For the reduced harmonic number H_n=U_n/V_n, gcd(U_n,n!)=179."
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def integer_sha256(value: int) -> str:
    return sha256_bytes(str(value).encode("ascii"))


def reject_duplicate_object(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    """Build a JSON object while rejecting every repeated member name."""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def load_witness(path: pathlib.Path) -> tuple[dict[str, object], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw, object_pairs_hook=reject_duplicate_object)
    if not isinstance(value, dict) or set(value) != EXPECTED_KEYS:
        raise ValueError("witness must be an object with exactly the expected keys")
    for key in ("schema_version", "n", "p", "expected_h"):
        if type(value[key]) is not int:  # bool is deliberately rejected
            raise ValueError(f"{key} must be an integer")
    if value["schema_version"] != 1:
        raise ValueError("unsupported witness schema")
    if value["claim"] != EXPECTED_CLAIM:
        raise ValueError("claim text does not bind the frozen endpoint")
    if value["n"] != value["p"] * (value["p"] - 1):
        raise ValueError("this certificate expects n=p(p-1)")
    if value["p"] != 179 or value["expected_h"] != 179:
        raise ValueError("witness does not address the frozen endpoint")
    return value, raw


def primes_up_to(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(n) + 1):
        if sieve[q]:
            sieve[q * q : n + 1 : q] = b"\x00" * (((n - q * q) // q) + 1)
    return [q for q in range(2, n + 1) if sieve[q]]


def lcm_one_to_n(n: int) -> int:
    result = 1
    for q in primes_up_to(n):
        power = q
        while power * q <= n:
            power *= q
        result *= power
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} WITNESS.json", file=sys.stderr)
        return 2
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    witness_path = pathlib.Path(sys.argv[1])
    witness, raw = load_witness(witness_path)
    n = int(witness["n"])

    denominator_common = lcm_one_to_n(n)
    numerator_common = sum(denominator_common // k for k in range(1, n + 1))
    cancellation = math.gcd(numerator_common, denominator_common)
    numerator = numerator_common // cancellation
    denominator = denominator_common // cancellation
    factorial_n = math.factorial(n)
    computed_h = math.gcd(numerator, factorial_n)

    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("reduction failed")
    if numerator_common * denominator != numerator * denominator_common:
        raise AssertionError("reduced fraction is not the harmonic sum")
    if computed_h != witness["expected_h"]:
        raise AssertionError(f"computed h(n)={computed_h}, expected {witness['expected_h']}")
    if numerator % 179 != 0 or numerator % (179 * 179) == 0:
        raise AssertionError("the numerator does not have 179-adic valuation one")
    if denominator % 179 == 0:
        raise AssertionError("the reduced denominator is unexpectedly divisible by 179")

    result = {
        "status": "PASS",
        "algorithm": "lcm-sum-then-reduce",
        "n": n,
        "computed_h": computed_h,
        "numerator_bits": numerator.bit_length(),
        "denominator_bits": denominator.bit_length(),
        "numerator_mod_179_squared": numerator % (179 * 179),
        "denominator_mod_179": denominator % 179,
        "numerator_sha256_decimal": integer_sha256(numerator),
        "denominator_sha256_decimal": integer_sha256(denominator),
        "input_sha256": sha256_bytes(raw),
        "code_sha256": sha256_bytes(pathlib.Path(__file__).read_bytes()),
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
