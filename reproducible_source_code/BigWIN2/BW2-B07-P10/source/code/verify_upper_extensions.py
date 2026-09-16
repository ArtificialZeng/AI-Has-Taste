#!/usr/bin/env python3
"""Kruskal--Katona upper bound for one-point maximal extensions."""

import json
import pathlib
import sys


def colex_cliques(n: int, complement_edges: int) -> int:
    a = 0
    while a < n and (a + 1) * a // 2 <= complement_edges:
        a += 1
    if a == n:
        return 1 << n
    b = complement_edges - a * (a - 1) // 2
    if not 0 <= b < a:
        raise ValueError("invalid binomial representation")
    return (1 << a) + (1 << b) + (n - a - 1)


def main(path: str) -> None:
    raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    histogram = raw.get("u16_by_number_of_strict_relations")
    if raw.get("target_n") != 17 or not isinstance(histogram, list) or len(histogram) != 121:
        raise SystemExit("VERIFY FAILED: malformed relation histogram")
    if any(type(v) is not int or v < 0 for v in histogram):
        raise SystemExit("VERIFY FAILED: histogram entries must be nonnegative integers")
    if sum(histogram) != 4483130665195087:
        raise SystemExit("VERIFY FAILED: relation histogram does not sum to U(16)")
    upper = 0
    for relations, number_of_posets in enumerate(histogram):
        complement_edges = 120 - relations
        upper += number_of_posets * colex_cliques(16, complement_edges)
    if upper != raw.get("expected", {}).get("upper_bound_u17"):
        raise SystemExit(f"VERIFY FAILED: upper bound mismatch: {upper}")
    print(f"VERIFY PASSED: U(17) <= {upper}; Table 59 sum and colex formula exact")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("VERIFY FAILED: usage: verify_upper_extensions.py CERTIFICATE.json")
    main(sys.argv[1])
