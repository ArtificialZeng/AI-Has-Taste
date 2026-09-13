#!/usr/bin/env python3
"""Dependency-free exact checks for the finite claims in evidence/proof.md."""

from collections import Counter
from fractions import Fraction
from itertools import combinations


N = 5
edge_families = {
    h: {tuple(sorted((x, (x + h) % N))) for x in range(N)}
    for h in (1, 2)
}
assert all(len(edges) == N for edges in edge_families.values())

cut_signatures = []
for mask in range(1, 2**N - 1):
    subset = {x for x in range(N) if (mask >> x) & 1}
    counts = tuple(
        sum((x in subset) != (y in subset) for x, y in edge_families[h])
        for h in (1, 2)
    )
    cut_signatures.append((min(len(subset), N - len(subset)), counts))

expected_cuts = {(1, (2, 2)), (2, (2, 4)), (2, (4, 2))}
assert set(cut_signatures) == expected_cuts
assert Counter(cut_signatures) == Counter({signature: 10 for signature in expected_cuts})

triangle_signatures = []
for triple in combinations(range(N), 3):
    kinds = []
    for x, y in combinations(triple, 2):
        kinds.append(1 if (y - x) % N in (1, 4) else 2)
    triangle_signatures.append(tuple(sorted(kinds)))

assert Counter(triangle_signatures) == Counter({(1, 1, 2): 5, (1, 2, 2): 5})


def averaged_cut_distances(subset):
    return tuple(
        Fraction(
            sum((c in subset) != ((c + h) % N in subset) for c in range(N)),
            N,
        )
        for h in (1, 2)
    )


assert averaged_cut_distances({0, 1}) == (Fraction(2, 5), Fraction(4, 5))
assert averaged_cut_distances({0, 2}) == (Fraction(4, 5), Fraction(2, 5))

print("30 nontrivial subsets: exact cut signatures and multiplicities verified")
print("10 vertex triples: exact two triangle signatures verified")
print("endpoint translation-averaged cut distances verified over Q")
