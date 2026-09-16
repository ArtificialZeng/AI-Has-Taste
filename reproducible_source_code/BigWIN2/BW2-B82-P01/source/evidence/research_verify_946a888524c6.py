#!/usr/bin/env python3
"""Exact independent check of every reduced slice in the E(8,4) proof.

This is corroboration, not a substitute for the symbolic proof.  It uses
Python integers and finite sets only; there is no randomness or floating point.
"""

from itertools import combinations
from math import gcd


G = tuple(range(10))


def convolution_value(A, D, x):
    return sum(((x - a) % 10) in D for a in A)


def reconstructed_column(A, D, x):
    return frozenset(a for a in A if ((x - a) % 10) in D)


counts = {"impossible": 0, "generating": 0, "antipodal": 0}
valid_pair_count = 0

for A_tuple in combinations(G, 8):
    A = frozenset(A_tuple)
    B = tuple(x for x in G if x not in A)
    difference = B[1] - B[0]
    order = 10 // gcd(10, difference)
    target = {frozenset(c) for c in combinations(A_tuple, 4)}

    valid_templates = []
    accessible = set()
    for D_tuple in combinations(G, 5):
        D = frozenset(D_tuple)
        if all(convolution_value(A, D, x) == 4 for x in G):
            columns = tuple(reconstructed_column(A, D, x) for x in G)
            assert all(len(column) == 4 for column in columns)
            valid_templates.append(D)
            accessible.update(columns)

    if order % 2:
        case = "impossible"
        assert len(valid_templates) == 0
        assert len(accessible) == 0
    elif difference == 5:
        case = "antipodal"
        assert len(valid_templates) == 32
        assert len(accessible) == 16
    else:
        case = "generating"
        assert difference % 2 == 1
        assert len(valid_templates) == 2
        assert len(accessible) == 2

    assert len(target) == 70
    assert not target <= accessible
    counts[case] += 1
    valid_pair_count += len(valid_templates)

assert counts == {"impossible": 20, "generating": 20, "antipodal": 5}
assert valid_pair_count == 200

print("tested_pairs=11340")
print("complements: impossible=20 generating=20 antipodal=5")
print("valid_slice_pairs=200")
print("all_70_columns_accessible_for_some_A=no")
