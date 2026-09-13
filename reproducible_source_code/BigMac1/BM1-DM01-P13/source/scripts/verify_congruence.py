#!/usr/bin/env python3
"""Exact modular checks for DM01-13.

The main evaluator follows C(2(k+1),k+1)=C(2k,k)*2(2k+1)/(k+1),
storing the p-adic valuation separately from the unit.  It therefore never
divides by a nonunit modulo p^e.  A second evaluator uses Python's exact
``math.comb`` and is intended for small cross-checks.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from pathlib import Path


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (
                (limit - q * q) // q + 1
            )
    return [q for q in range(2, limit + 1) if sieve[q]]


def strip_p(x: int, p: int) -> tuple[int, int]:
    valuation = 0
    while x % p == 0:
        x //= p
        valuation += 1
    return x, valuation


def sum_by_p_adic_recurrence(p: int, n: int, exponent: int = 3) -> int:
    modulus = p**exponent
    valuation = 0
    unit = 1
    total = 0
    for k in range(n + 1):
        if 3 * valuation < exponent:
            total = (total + pow(unit, 3, modulus) * p ** (3 * valuation)) % modulus
        if k == n:
            break
        numerator, vn = strip_p(2 * (2 * k + 1), p)
        denominator, vd = strip_p(k + 1, p)
        valuation += vn - vd
        if valuation < 0:
            raise ArithmeticError(f"negative valuation at p={p}, k={k}")
        unit = unit * numerator * pow(denominator, -1, modulus) % modulus
    return total


def sum_by_exact_comb(p: int, n: int, exponent: int = 3) -> int:
    modulus = p**exponent
    return sum(pow(math.comb(2 * k, k), 3, modulus) for k in range(n + 1)) % modulus


def check_prime(p: int, exact_crosscheck: bool) -> dict[str, object]:
    residues: dict[str, int] = {}
    for exponent in (3, 4):
        residues[f"mod_p^{exponent}"] = sum_by_p_adic_recurrence(
            p, p * p, exponent
        )
    target = (8 + p * p) % (p**3)
    row: dict[str, object] = {
        "p": p,
        "p_mod_7": p % 7,
        "A_p2_mod_p3": residues["mod_p^3"],
        "target_mod_p3": target,
        "holds": residues["mod_p^3"] == target,
        "A_p2_mod_p4": residues["mod_p^4"],
        "quotient_mod_p": ((residues["mod_p^4"] - 8 - p * p) // (p**3)) % p
        if (residues["mod_p^4"] - 8 - p * p) % (p**3) == 0
        else None,
    }
    if exact_crosscheck:
        independent = sum_by_exact_comb(p, p * p, 4)
        row["exact_comb_mod_p4"] = independent
        row["crosscheck_ok"] = independent == residues["mod_p^4"]
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=101)
    parser.add_argument("--crosscheck-limit", type=int, default=19)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    selected = [p for p in primes_through(args.limit) if p % 7 in (3, 5, 6)]
    rows = [check_prime(p, p <= args.crosscheck_limit) for p in selected]
    payload = {
        "problem_id": "mac01-p13",
        "algorithm": "p-adic unit/valuation central-binomial recurrence",
        "independent_algorithm": "Python exact math.comb for declared small range",
        "python": sys.version,
        "platform": platform.platform(),
        "limit": args.limit,
        "eligible_primes": len(rows),
        "all_hold": all(bool(row["holds"]) for row in rows),
        "all_crosschecks_hold": all(
            bool(row.get("crosscheck_ok", True)) for row in rows
        ),
        "rows": rows,
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0 if payload["all_hold"] and payload["all_crosschecks_hold"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
