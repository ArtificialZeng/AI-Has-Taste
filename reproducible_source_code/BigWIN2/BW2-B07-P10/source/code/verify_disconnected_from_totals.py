#!/usr/bin/env python3
"""Re-derive connected counts and D(17) from U(0),...,U(16)."""

import json
import math
import pathlib
import sys


def partitions(total: int, largest: int, prefix: tuple[int, ...] = ()):
    if total == 0:
        yield prefix
    else:
        for part in range(min(total, largest), 0, -1):
            yield from partitions(total - part, part, prefix + (part,))


def disconnected(n: int, connected: dict[int, int]) -> int:
    ans = 0
    for lam in partitions(n, n):
        if len(lam) < 2:
            continue
        mult: dict[int, int] = {}
        for size in lam:
            mult[size] = mult.get(size, 0) + 1
        term = 1
        for size, copies in mult.items():
            term *= math.comb(connected[size] + copies - 1, copies)
        ans += term
    return ans


def main(path: str) -> None:
    try:
        raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
        u = {int(k): v for k, v in raw["unlabeled_counts"].items()}
        claimed_c = {int(k): v for k, v in raw["connected_unlabeled_counts"].items()}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f"VERIFY FAILED: malformed certificate: {exc}")
    if set(u) != set(range(17)) or u[0] != 1:
        raise SystemExit("VERIFY FAILED: U table must contain exactly 0..16")
    c: dict[int, int] = {}
    for n in range(1, 17):
        c[n] = u[n] - disconnected(n, c)
    if c != claimed_c:
        raise SystemExit(f"VERIFY FAILED: inverse transform mismatch: {c!r}")
    d17 = disconnected(17, c)
    if d17 != raw.get("claimed_disconnected_total"):
        raise SystemExit(f"VERIFY FAILED: D(17) mismatch: {d17}")
    print(f"VERIFY PASSED: inverse transform recovered C(1..16) and D(17)={d17}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("VERIFY FAILED: usage: verify_disconnected_from_totals.py CERTIFICATE.json")
    main(sys.argv[1])
