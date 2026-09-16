#!/usr/bin/env python3
"""Independent integer-partition verifier for disconnected 17-posets."""

import json
import pathlib
import sys


def choose(n: int, k: int) -> int:
    if k < 0 or n < k:
        return 0
    k = min(k, n - k)
    ans = 1
    for j in range(1, k + 1):
        ans = ans * (n - k + j) // j
    return ans


def partitions(total: int, largest: int, prefix: tuple[int, ...] = ()):
    if total == 0:
        yield prefix
        return
    for part in range(min(total, largest), 0, -1):
        yield from partitions(total - part, part, prefix + (part,))


def main(path: str) -> None:
    try:
        raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
        n = raw["target_n"]
        c = {int(k): v for k, v in raw["connected_unlabeled_counts"].items()}
        claimed = {int(k): v for k, v in raw["claimed_by_components"].items()}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f"VERIFY FAILED: malformed certificate: {exc}")
    if n != 17 or set(c) != set(range(1, 17)):
        raise SystemExit("VERIFY FAILED: incomplete domain")
    totals = {m: 0 for m in range(2, n + 1)}
    for lam in partitions(n, n):
        m = len(lam)
        if m < 2:
            continue
        multiplicities: dict[int, int] = {}
        for part in lam:
            multiplicities[part] = multiplicities.get(part, 0) + 1
        ways = 1
        for size, multiplicity in multiplicities.items():
            ways *= choose(c[size] + multiplicity - 1, multiplicity)
        totals[m] += ways
    if totals != claimed:
        raise SystemExit(f"VERIFY FAILED: component vector mismatch: {totals!r}")
    total = sum(totals.values())
    if total != raw.get("claimed_disconnected_total"):
        raise SystemExit(f"VERIFY FAILED: total mismatch: {total}")
    print(f"VERIFY PASSED: D(17)={total}; enumerated integer partitions independently")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("VERIFY FAILED: usage: verify_disconnected_partitions.py CERTIFICATE.json")
    main(sys.argv[1])
