#!/usr/bin/env python3
"""Exact bivariate Euler-product verifier for disconnected 17-posets."""

import json
import math
import pathlib
import sys


def fail(message: str) -> None:
    raise SystemExit(f"VERIFY FAILED: {message}")


def main(path: str) -> None:
    raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    n = raw.get("target_n")
    counts_raw = raw.get("connected_unlabeled_counts")
    claimed_raw = raw.get("claimed_by_components")
    if n != 17 or not isinstance(counts_raw, dict) or not isinstance(claimed_raw, dict):
        fail("malformed top-level certificate")
    c = {int(k): v for k, v in counts_raw.items()}
    claimed = {int(k): v for k, v in claimed_raw.items()}
    if set(c) != set(range(1, n)) or any(type(v) is not int or v < 0 for v in c.values()):
        fail("connected counts must be nonnegative integers for every size 1..16")

    # dp[size][components] is the coefficient after multiplying factors
    # (1-y*x^k)^(-C(k)).
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for k in range(1, n):
        nxt = [[0] * (n + 1) for _ in range(n + 1)]
        for size in range(n + 1):
            for components in range(n + 1):
                base = dp[size][components]
                if not base:
                    continue
                for multiplicity in range((n - size) // k + 1):
                    ways = math.comb(c[k] + multiplicity - 1, multiplicity)
                    nxt[size + k * multiplicity][components + multiplicity] += base * ways
        dp = nxt

    got = {m: dp[n][m] for m in range(2, n + 1)}
    if got != claimed:
        fail(f"component vector mismatch: got {got!r}")
    total = sum(got.values())
    if total != raw.get("claimed_disconnected_total"):
        fail(f"total mismatch: got {total}")
    print(f"VERIFY PASSED: D(17)={total}; component strata 2..17 exact")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        fail("usage: verify_disconnected_euler.py CERTIFICATE.json")
    main(sys.argv[1])
