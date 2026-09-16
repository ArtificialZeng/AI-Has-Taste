#!/usr/bin/env python3
"""Dependency-free exact sanity checks for the frozen F_2^5 instance."""

from itertools import combinations


def span(vectors):
    """Return the F_2-span of bit-vector integers."""
    result = {0}
    for vector in vectors:
        result |= {entry ^ vector for entry in tuple(result)}
    return frozenset(result)


subspaces = tuple(
    {span(triple) for triple in combinations(range(1, 32), 3)
     if len(span(triple)) == 8}
)
star = tuple(subspace for subspace in subspaces if 1 in subspace)

intersection_size_distribution = {1: 0, 2: 0, 4: 0, 8: 0}
for first in subspaces:
    for second in subspaces:
        pair_intersection = first & second
        for third in subspaces:
            intersection_size_distribution[len(pair_intersection & third)] += 1

e1, e2, e3, e4, e5 = 1, 2, 4, 8, 16
zero_intersection_example = (
    span((e1, e2, e3)),
    span((e1, e4, e5)),
    span((e2, e3, e4)),
)

assert len(subspaces) == 155
assert len(star) == 35
assert len(star) ** 3 == 42875
assert sum(intersection_size_distribution.values()) == 155 ** 3
assert intersection_size_distribution[1] == 2499840
assert set.intersection(*(set(space) for space in zero_intersection_example)) == {0}

print("three_subspaces", len(subspaces))
print("star_size", len(star))
print("star_product", len(star) ** 3)
print("ordered_triple_intersection_sizes", intersection_size_distribution)
print("zero_intersection_example_bases", ((1, 2, 4), (1, 8, 16), (2, 4, 8)))
