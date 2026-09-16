#!/usr/bin/env python3
"""Cross-check CoverSearch against literal subset enumeration for n <= 12."""

from itertools import combinations
from exact_cover_verify import CoverSearch, collision_edges_by_four_subsets


def literal_f(n):
    best = 0
    for mask in range(1 << n):
        if mask.bit_count() <= best:
            continue
        vals = [i + 1 for i in range(n) if mask >> i & 1]
        products = [a * b for a, b in combinations(vals, 2)]
        if len(products) == len(set(products)):
            best = len(vals)
    return best


for n in range(1, 13):
    edges = collision_edges_by_four_subsets(n)
    expected = literal_f(n)
    if n - expected - 1 >= 0:
        search = CoverSearch(edges, n)
        rejected = not search.exists((1 << len(edges)) - 1, (1 << n) - 1,
                                     n - expected - 1)
        assert rejected, (n, expected)
    if expected < n:
        search2 = CoverSearch(edges, n)
        accepted = search2.exists((1 << len(edges)) - 1, (1 << n) - 1,
                                  n - expected)
        assert accepted, (n, expected)
    print(f"n={n}: F(n)={expected}, cross-check PASS")
print("SMALL CROSS-CHECK VERIFIED")
