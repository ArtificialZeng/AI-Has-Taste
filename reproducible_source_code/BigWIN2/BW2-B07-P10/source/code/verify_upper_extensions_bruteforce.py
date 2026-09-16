#!/usr/bin/env python3
"""Independent 2^16-subset check of every colex clique count."""

import json
import pathlib
import sys


def colex_edges(n: int):
    pairs = [(i, j) for j in range(n) for i in range(j)]
    return pairs  # pair colex order for 2-subsets


def clique_count(n: int, edge_count: int) -> int:
    adjacency = [0] * n
    for i, j in colex_edges(n)[:edge_count]:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    total = 0
    for subset in range(1 << n):
        vertices = subset
        ok = True
        while vertices:
            bit = vertices & -vertices
            vertices ^= bit
            v = bit.bit_length() - 1
            if vertices & ~adjacency[v]:
                ok = False
                break
        total += ok
    return total


def main(path: str) -> None:
    raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    hist = raw.get("u16_by_number_of_strict_relations")
    if not isinstance(hist, list) or len(hist) != 121:
        raise SystemExit("VERIFY FAILED: malformed histogram")
    upper = sum(hist[q] * clique_count(16, 120 - q) for q in range(121))
    expected = raw.get("expected", {}).get("upper_bound_u17")
    if upper != expected:
        raise SystemExit(f"VERIFY FAILED: brute upper {upper}, expected {expected}")
    print(f"VERIFY PASSED: brute colex subsets independently give U(17) <= {upper}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("VERIFY FAILED: usage: verify_upper_extensions_bruteforce.py CERTIFICATE.json")
    main(sys.argv[1])
