#!/usr/bin/env python3
"""Independent exact verifier for mac01-p15, using reduced recurrence."""

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
        if type(value[key]) is not int:
            raise ValueError(f"{key} must be an integer")
    if value["schema_version"] != 1 or value["n"] != 31862:
        raise ValueError("unsupported witness")
    if value["p"] != 179 or value["expected_h"] != 179:
        raise ValueError("witness does not address the frozen endpoint")
    if value["claim"] != EXPECTED_CLAIM:
        raise ValueError("claim text does not bind the frozen endpoint")
    return value, raw


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} WITNESS.json", file=sys.stderr)
        return 2
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    witness_path = pathlib.Path(sys.argv[1])
    witness, raw = load_witness(witness_path)
    n = int(witness["n"])

    # If H_{k-1}=u/v in lowest terms, reduce (ku+v)/(kv) at every step.
    numerator, denominator = 0, 1
    for k in range(1, n + 1):
        numerator = k * numerator + denominator
        denominator *= k
        cancellation = math.gcd(numerator, denominator)
        numerator //= cancellation
        denominator //= cancellation

    if math.gcd(numerator, denominator) != 1:
        raise AssertionError("recurrence did not maintain lowest terms")
    computed_h = math.gcd(numerator, math.factorial(n))
    if computed_h != witness["expected_h"]:
        raise AssertionError(f"computed h(n)={computed_h}, expected {witness['expected_h']}")
    if numerator % 179 != 0 or numerator % (179 * 179) == 0:
        raise AssertionError("the numerator does not have 179-adic valuation one")
    if denominator % 179 == 0:
        raise AssertionError("the reduced denominator is unexpectedly divisible by 179")

    result = {
        "status": "PASS",
        "algorithm": "stepwise-reduced-recurrence",
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
