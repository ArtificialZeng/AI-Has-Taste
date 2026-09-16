#!/usr/bin/env python3
"""Exact, deterministic experiments for OEIS A182510 (Python signed XOR)."""
import argparse
import json
import platform
import time


def iterate(limit: int):
    prevprev, prev = 0, 1
    zeros = [0]
    max_bits = 1
    for n in range(2, limit + 1):
        prevprev, prev = prev, (prev ^ n) - prevprev
        max_bits = max(max_bits, abs(prev).bit_length())
        if prev == 0:
            zeros.append(n)
    return zeros, prev, max_bits


def modular_period(k: int):
    modulus = 1 << k
    period = 3 * modulus
    prevprev, prev = 0, 1
    zero_residues = [0]
    for n in range(2, period + 2):
        prevprev, prev = prev, ((prev ^ n) - prevprev) % modulus
        if n < period and prev == 0:
            zero_residues.append(n)
    return period, (prevprev, prev), zero_residues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=10_000_000)
    ap.add_argument("--max-k", type=int, default=22)
    ap.add_argument("--output")
    args = ap.parse_args()
    started = time.time()
    zeros, last, max_bits = iterate(args.limit)
    modular = []
    for k in range(1, args.max_k + 1):
        period, end_state, residues = modular_period(k)
        modular.append({"k": k, "modulus": 1 << k, "tested_period": period,
                        "end_state": list(end_state), "period_test_passed": end_state == (0, 1),
                        "zero_residue_count": len(residues), "zero_residues": residues})
    result = {"semantics": "Python arbitrary-precision signed integer XOR",
              "limit_inclusive": args.limit, "zeros": zeros, "last_value": last,
              "maximum_absolute_bit_length": max_bits, "modular_tests": modular,
              "python": platform.python_version(), "elapsed_seconds": time.time() - started}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
