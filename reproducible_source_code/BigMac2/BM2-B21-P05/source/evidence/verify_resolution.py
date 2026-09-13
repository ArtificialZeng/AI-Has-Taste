#!/usr/bin/env python3
"""Exact finite checks for the H(3,3) majority C-coloring claim.

The program uses only integer tuple comparisons.  It exhausts every subset of
the 27 vertices having size at most five and separately verifies an explicit
four-class partition.
"""

from itertools import combinations, product
from math import comb


VALUES = (1, 2, 3)
VERTICES = tuple(product(VALUES, repeat=3))


def adjacent(x, y):
    """Return whether x and y differ in exactly one coordinate."""
    return sum(a != b for a, b in zip(x, y)) == 1


NEIGHBORS = {
    v: frozenset(w for w in VERTICES if adjacent(v, w)) for v in VERTICES
}


def induced_degrees(vertices):
    vertex_set = frozenset(vertices)
    return tuple(len(NEIGHBORS[v] & vertex_set) for v in vertices)


def exhaustive_small_set_check():
    total_checked = 0
    rows = []
    witnesses = []
    for size in range(1, 6):
        checked = 0
        qualifying = 0
        max_min_degree = -1
        max_edges = -1
        for subset in combinations(VERTICES, size):
            degrees = induced_degrees(subset)
            minimum = min(degrees)
            edges = sum(degrees) // 2
            checked += 1
            max_min_degree = max(max_min_degree, minimum)
            max_edges = max(max_edges, edges)
            if minimum >= 3:
                qualifying += 1
                witnesses.append(subset)
        assert checked == comb(27, size)
        total_checked += checked
        rows.append((size, checked, qualifying, max_min_degree, max_edges))

    assert total_checked == sum(comb(27, size) for size in range(1, 6))
    assert not witnesses
    return total_checked, rows


def explicit_four_classes():
    # One K_3 square K_3 plane, followed by three K_2 square K_3 prisms.
    classes = [
        frozenset((1, b, c) for b in VALUES for c in VALUES),
        *(
            frozenset((a, b, c) for a in (2, 3) for c in VALUES)
            for b in VALUES
        ),
    ]

    assert len(classes) == 4
    assert all(classes)
    assert all(classes[i].isdisjoint(classes[j])
               for i in range(4) for j in range(i + 1, 4))
    assert frozenset().union(*classes) == frozenset(VERTICES)

    degree_multisets = []
    for color_class in classes:
        degrees = induced_degrees(tuple(sorted(color_class)))
        assert min(degrees) >= 3
        degree_multisets.append(tuple(sorted(degrees)))
    return classes, degree_multisets


def main():
    assert len(VERTICES) == 27
    assert all(len(NEIGHBORS[v]) == 6 for v in VERTICES)

    total_checked, rows = exhaustive_small_set_check()
    classes, degree_multisets = explicit_four_classes()

    print("graph: H(3,3)")
    print("vertices: 27")
    print("degree of every ambient vertex: 6")
    print("small-subset exhaustive enumeration")
    print("size checked qualifying_delta_ge_3 max_min_degree max_edges")
    for row in rows:
        print(*row)
    print(f"total subsets checked: {total_checked}")
    print("qualifying subsets of sizes 1..5: 0")
    print("explicit partition class sizes:", [len(c) for c in classes])
    print("explicit partition induced degree multisets:")
    for index, degrees in enumerate(degree_multisets, start=1):
        print(f"  class {index}:", list(degrees))
    print("partition covers every vertex exactly once: yes")
    print("all four induced minimum degrees are at least 3: yes")
    print("RESULT: exact finite checks passed")


if __name__ == "__main__":
    main()
