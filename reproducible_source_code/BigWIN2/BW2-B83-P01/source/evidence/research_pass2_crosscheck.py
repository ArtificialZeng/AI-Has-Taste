#!/usr/bin/env python3
"""Independent pass-2 cross-check of the finite degree reduction.

Unlike the two earlier programs, this program performs an unpruned traversal of
all nondecreasing 17-multisets from {1,...,9} using the standard-library
``combinations_with_replacement`` iterator.  NetworkX's independently exposed
Erdos--Gallai and Havel--Hakimi tests are required to agree.  Exact integer
arithmetic then checks the deficiency certificates used in the proof dossier.
"""

from hashlib import sha256
from itertools import combinations_with_replacement
from math import comb

import networkx as nx


N = 17
TARGET = 123
MAX_EDGES = 36
SOURCE_SHA256 = "66dca795135d1d39b33ac000c548a361beb67db39de0cf00381572244e2790f7"


def lemma_5_3(degrees):
    total = sum(comb(d - 1, 2) for d in degrees)
    return all(
        comb(N - d, 2) >= total - comb(d - 1, 2) for d in degrees
    )


with open("source.md", "rb") as source_file:
    assert sha256(source_file.read()).hexdigest() == SOURCE_SHA256

examined = 0
arithmetic = []
for increasing in combinations_with_replacement(range(1, 10), N):
    examined += 1
    if not 5 <= increasing[-1] <= 9:
        continue
    if sum(comb(d, 2) for d in increasing) != TARGET:
        continue
    degree_sum = sum(increasing)
    if degree_sum % 2 or degree_sum // 2 > MAX_EDGES:
        continue
    arithmetic.append(tuple(reversed(increasing)))

arithmetic.sort(reverse=True)
graphical_eg = [
    degrees
    for degrees in arithmetic
    if nx.is_graphical(degrees, method="eg")
]
graphical_hh = [
    degrees
    for degrees in arithmetic
    if nx.is_graphical(degrees, method="hh")
]
assert graphical_eg == graphical_hh
survivors = [degrees for degrees in graphical_eg if lemma_5_3(degrees)]

expected = [
    (5,) * 12 + (2,) * 3 + (1,) * 2,
    (5,) * 11 + (4,) * 2 + (2,) + (1,) * 3,
    (5,) * 11 + (4,) + (3,) + (2,) * 4,
    (5,) * 11 + (3,) * 4 + (2,) + (1,),
    (5,) * 10 + (4,) * 3 + (3,) + (2,) * 2 + (1,),
    (5,) * 9 + (4,) * 5 + (3,) + (1,) * 2,
    (5,) * 9 + (4,) * 3 + (3,) * 5,
    (5,) * 8 + (4,) * 6 + (3,) * 2 + (2,),
]

assert examined == comb(25, 17)
assert len(arithmetic) == 1368
assert len(graphical_eg) == 1356
assert survivors == expected

print(
    "method=unpruned-combinations-with-replacement "
    f"networkx={nx.__version__} arithmetic=integer"
)
print(f"examined={examined}")
print(f"arithmetic={len(arithmetic)}")
print(f"graphical_eg=graphical_hh={len(graphical_eg)}")
print(f"lemma_5_3_survivors={len(survivors)}")

for index, degrees in enumerate(survivors, 1):
    high = sum(d == 5 for d in degrees)
    low_degree_sum = sum(d for d in degrees if d < 5)
    supply = sum(d * (5 - d) for d in degrees if d < 5)
    edge_count = sum(degrees) // 2
    assert sum(comb(d, 2) for d in degrees) == TARGET

    if index <= 6:
        assert supply < 4 * high
        certificate = f"S={supply}<4h={4 * high}"
    elif index == 7:
        leave_sum_upper = supply - 4 * high
        assert leave_sum_upper == 6 < high
        certificate = f"R_H<=S-4h={leave_sum_upper}<h={high}"
    else:
        # Odd degree at every high vertex gives R_H >= h.  Since
        # R_H=S-C-4h, the low--low deficiency cost satisfies C<=2.
        cost_upper = supply - 5 * high
        assert (high, low_degree_sum, supply, cost_upper) == (8, 32, 42, 2)
        for q in (0, 1):
            cost = 2 * q
            high_low_edges = low_degree_sum - 2 * q
            high_edges = (5 * high - high_low_edges) // 2
            leave_sum = supply - cost - 4 * high
            triangle_lower = (5 * high - leave_sum + 1) // 2
            triangle_upper = 2 * high_edges + q
            assert high_edges == 4 + q
            assert triangle_lower == 15 + q
            assert triangle_upper == 8 + 3 * q
            assert triangle_lower > triangle_upper
        certificate = "C=2q,q={0,1}: T_H>=15+q>8+3q>=T_H"

    print(
        f"case={index} edges={edge_count} h={high} degrees={degrees} "
        f"certificate={certificate}"
    )

print("STATUS VERIFIED")
