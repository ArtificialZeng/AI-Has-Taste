#!/usr/bin/env python3
"""Exact-certificate exhaustion for periods with one high junction.

The only non-exact step is using HiGHS to discover a dual vector.  Every
reported lower bound is then reconstructed over Q and checked using
fractions.Fraction.  Failure to reconstruct aborts the run.
"""

from fractions import Fraction
from itertools import combinations, permutations, product

import numpy as np
from scipy.optimize import linprog


LAYERS = 13
TARGET = Fraction(39, 8)


def maximal_patterns(left, right):
    """Coordinatewise-maximal anchored patterns with no other high edge."""
    answer = []
    for tail in product(range(1, 5), repeat=11):
        counts = (left, right) + tail
        if not all(counts[i] + counts[i + 1] <= 6 for i in range(1, 12)):
            continue
        if counts[12] + counts[0] > 6:
            continue
        if not all(
            counts[i] == 4
            or counts[i - 1] + counts[i] == 6
            or counts[i] + counts[(i + 1) % LAYERS] == 6
            for i in range(2, LAYERS)
        ):
            continue
        answer.append(counts)
    return answer


def reflect_44(counts):
    """Reflection fixing the unoriented edge {0,1} and swapping its ends."""
    return tuple(counts[(1 - i) % LAYERS] for i in range(LAYERS))


def missing_edge_representatives(kind):
    # Vertex labels 0,...,left+right-1, first layer followed by second.
    if kind == "34":
        return (
            ((0, 1),),             # inside the 3-layer
            ((3, 4),),             # inside the 4-layer
            ((0, 3),),             # crossing the junction
        )
    # The ten S_4 x S_4 orbits of two disjoint edges or a triangle.
    return (
        ((0, 1), (0, 2), (1, 2)),
        ((0, 1), (0, 4), (1, 4)),
        ((0, 1), (2, 3)),
        ((0, 1), (2, 4)),
        ((0, 1), (4, 5)),
        ((0, 4), (0, 5), (4, 5)),
        ((0, 4), (1, 5)),
        ((0, 4), (5, 6)),
        ((4, 5), (4, 6), (5, 6)),
        ((4, 5), (6, 7)),
    )


def canonical_missing(missing, left, right):
    images = []
    for pleft in permutations(range(left)):
        for raw_right in permutations(range(right)):
            permutation = pleft + tuple(left + x for x in raw_right)
            images.append(
                tuple(sorted(tuple(sorted((permutation[u], permutation[v])))
                             for u, v in missing))
            )
    return min(images)


def check_topology_classes():
    edges34 = tuple(combinations(range(7), 2))
    classes34 = {
        canonical_missing((edge,), 3, 4) for edge in edges34
    }
    expected34 = {
        canonical_missing(missing, 3, 4)
        for missing in missing_edge_representatives("34")
    }
    assert classes34 == expected34 and len(classes34) == 3

    edges44 = tuple(combinations(range(8), 2))
    minimal44 = []
    minimal44.extend(
        (first, second)
        for first, second in combinations(edges44, 2)
        if len(set(first + second)) == 4
    )
    minimal44.extend(
        triple for triple in combinations(edges44, 3)
        if len(set().union(*map(set, triple))) == 3
    )
    classes44 = {
        canonical_missing(missing, 4, 4) for missing in minimal44
    }
    expected44 = {
        canonical_missing(missing, 4, 4)
        for missing in missing_edge_representatives("44")
    }
    assert len(minimal44) == 266
    assert classes44 == expected44 and len(classes44) == 10


def adjacency(counts, missing):
    starts = np.cumsum((0,) + counts)
    n = int(starts[-1])
    layer = []
    for i, count in enumerate(counts):
        layer.extend((i,) * count)
    missing = {tuple(sorted(edge)) for edge in missing}
    matrix = np.zeros((n, n), dtype=np.int8)
    for u, v in combinations(range(n), 2):
        gap = (layer[u] - layer[v]) % LAYERS
        if layer[u] == layer[v] or gap in (1, LAYERS - 1):
            if (u, v) not in missing:
                matrix[u, v] = matrix[v, u] = 1
    return matrix


def exact_dual_certificate(matrix):
    """Return an exact feasible dual of value at least 39/8."""
    n = len(matrix)
    result = linprog(
        np.ones(n), A_ub=-matrix, b_ub=-np.ones(n), bounds=(0, None),
        method="highs",
    )
    assert result.success
    discovered = -result.ineqlin.marginals
    # HiGHS solutions here have small rational coordinates.  The exact tests
    # below, rather than the denominator cap, decide whether reconstruction is
    # valid.
    dual = tuple(Fraction(float(x)).limit_denominator(1_000_000) for x in discovered)
    assert all(x >= 0 for x in dual)
    for v in range(n):
        assert sum(dual[u] * int(matrix[u, v]) for u in range(n)) <= 1
    value = sum(dual)
    assert value >= TARGET
    return value, dual


def run():
    check_topology_classes()
    patterns34 = maximal_patterns(3, 4)
    raw44 = maximal_patterns(4, 4)
    patterns44 = sorted(
        counts for counts in raw44 if counts <= reflect_44(counts)
    )
    assert len(patterns34) == 60
    assert len(raw44) == 51
    assert len(patterns44) == 30

    total_lps = 0
    weakest = None
    weakest_data = None
    denominators = set()
    for kind, patterns in (("34", patterns34), ("44", patterns44)):
        misses = missing_edge_representatives(kind)
        for counts in patterns:
            for missing in misses:
                value, dual = exact_dual_certificate(adjacency(counts, missing))
                total_lps += 1
                denominators.update(x.denominator for x in dual)
                if weakest is None or value < weakest:
                    weakest = value
                    weakest_data = (kind, counts, missing, dual)

    assert total_lps == 60 * 3 + 30 * 10 == 480
    print("anchored maximal 3+4 patterns:", len(patterns34))
    print("anchored maximal 4+4 patterns before reflection:", len(raw44))
    print("dihedral representatives of maximal 4+4 patterns:", len(patterns44))
    print("junction topology classes: 3 for 3+4; 10 for 4+4")
    print("exact dual certificates checked:", total_lps)
    print("weakest certified dual value:", weakest)
    print("distinct dual coordinate denominators:", len(denominators))
    print("largest dual coordinate denominator:", max(denominators))
    kind, counts, missing, dual = weakest_data
    print("one weakest case kind:", kind)
    print("one weakest count pattern:", " ".join(map(str, counts)))
    print("one weakest missing-edge set:", " ".join(f"{u}-{v}" for u, v in missing))
    print("one exact dual:", " ".join(map(str, dual)))


if __name__ == "__main__":
    run()
