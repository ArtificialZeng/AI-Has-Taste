#!/usr/bin/env python3
"""Fail-closed verifier for a finite A071532 parity claim.

Only Python integer arithmetic is used.  The primary evaluator maintains 3**k
incrementally.  A deliberately separate evaluator uses modular exponentiation
for a small prefix: floor(3**k/2**k) mod 2 is bit k of 3**k.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

REQUIRED = {
    "schema",
    "endpoint",
    "crosscheck_endpoint",
    "claimed_final_sum",
    "claimed_min_sum_after_2",
    "claimed_min_indices_after_2",
    "claimed_first_nonpositive_after_2",
    "trace_sha256",
}


def die(message: str) -> "None":
    raise SystemExit("FAIL: " + message)


def load_claim(path: Path) -> dict:
    try:
        raw = path.read_bytes()
        value = json.loads(raw)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        die(f"cannot parse claim: {exc}")
    if not isinstance(value, dict) or set(value) != REQUIRED:
        die("claim must be an object with exactly the required fields")
    if value["schema"] != "a071532-finite-v1":
        die("unsupported schema")
    for key in ("endpoint", "crosscheck_endpoint", "claimed_final_sum",
                "claimed_min_sum_after_2"):
        if type(value[key]) is not int:
            die(f"{key} must be an integer (not bool)")
    if not (3 <= value["crosscheck_endpoint"] <= value["endpoint"] <= 2_000_000):
        die("invalid or excessive endpoints")
    indices = value["claimed_min_indices_after_2"]
    if (not isinstance(indices, list) or not indices or
            any(type(x) is not int or x < 3 or x > value["endpoint"] for x in indices) or
            indices != sorted(set(indices))):
        die("invalid minimum-index list")
    first = value["claimed_first_nonpositive_after_2"]
    if first is not None and (type(first) is not int or not 3 <= first <= value["endpoint"]):
        die("invalid first-nonpositive field")
    digest = value["trace_sha256"]
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        die("trace_sha256 must be 64 lowercase hexadecimal characters")
    return value


def primary(endpoint: int) -> tuple[int, int, list[int], int | None, str]:
    power = 1
    total = 0
    minimum = None
    minimum_indices: list[int] = []
    first_nonpositive = None
    trace = hashlib.sha256()
    for k in range(1, endpoint + 1):
        power *= 3
        bit = (power >> k) & 1
        total += 1 if bit else -1
        trace.update(f"{k},{bit},{total}\n".encode("ascii"))
        if k > 2:
            if minimum is None or total < minimum:
                minimum, minimum_indices = total, [k]
            elif total == minimum:
                minimum_indices.append(k)
            if total <= 0 and first_nonpositive is None:
                first_nonpositive = k
    assert minimum is not None
    return total, minimum, minimum_indices, first_nonpositive, trace.hexdigest()


def independent_prefix(endpoint: int) -> None:
    total = 0
    for k in range(1, endpoint + 1):
        # This residue contains exactly bits 0,...,k of 3**k.
        residue = pow(3, k, 1 << (k + 1))
        bit = (residue >> k) & 1
        total += 1 if bit else -1
        # A local direct quotient check makes the bit identity executable.
        direct_bit = ((3 ** k) // (2 ** k)) % 2
        if bit != direct_bit:
            die(f"independent evaluator disagreement at k={k}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("claim", type=Path)
    args = parser.parse_args()
    claim_raw = args.claim.read_bytes() if args.claim.is_file() else die("claim is not a file")
    claim = load_claim(args.claim)
    independent_prefix(claim["crosscheck_endpoint"])
    actual = primary(claim["endpoint"])
    expected = (
        claim["claimed_final_sum"], claim["claimed_min_sum_after_2"],
        claim["claimed_min_indices_after_2"],
        claim["claimed_first_nonpositive_after_2"], claim["trace_sha256"],
    )
    if actual != expected:
        die(f"recomputed tuple differs: {actual!r}")
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(claim_raw).hexdigest()
    print("PASS a071532-finite-v1")
    print(f"endpoint={claim['endpoint']} crosscheck_endpoint={claim['crosscheck_endpoint']}")
    print(f"final_sum={actual[0]} min_after_2={actual[1]} min_indices={actual[2]}")
    print(f"first_nonpositive_after_2={actual[3]}")
    print(f"trace_sha256={actual[4]}")
    print(f"input_sha256={input_hash}")
    print(f"verifier_sha256={code_hash}")
    print(f"python={platform.python_version()} implementation={platform.python_implementation()}")


if __name__ == "__main__":
    main()
