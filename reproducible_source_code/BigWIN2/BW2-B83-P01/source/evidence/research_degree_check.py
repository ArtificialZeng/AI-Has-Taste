#!/usr/bin/env python3
"""Independent exact check of the degree reduction used in the order-17 proof.

This deliberately does not import the triage program.  It enumerates degree
multiplicities rather than nonincreasing tuples and uses Havel--Hakimi rather
than Erdos--Gallai for graphicality.  All arithmetic is integral.
"""

from math import comb


N = 17
TARGET = 123
MAX_DEGREE = 9
MAX_EDGES = 36


def havel_hakimi(degrees):
    """Return whether ``degrees`` is graphical, by Havel--Hakimi."""
    work = sorted(degrees, reverse=True)
    while work and work[0]:
        d = work.pop(0)
        if d > len(work):
            return False
        for i in range(d):
            work[i] -= 1
            if work[i] < 0:
                return False
        work.sort(reverse=True)
    return True


def lemma_5_3(degrees):
    """The necessary inequality in source Lemma 5.3, for every vertex."""
    total = sum(comb(d - 1, 2) for d in degrees)
    return all(
        comb(N - d, 2) >= total - comb(d - 1, 2) for d in degrees
    )


arithmetic = []


def enumerate_multiplicities(d, vertices_left, target_left, counts):
    """Enumerate all count vectors (n_1,...,n_9) meeting the two sums."""
    if d == MAX_DEGREE:
        count = vertices_left
        if target_left == count * comb(d, 2):
            candidate = counts + [count]
            degrees = tuple(
                degree
                for degree in range(MAX_DEGREE, 0, -1)
                for _ in range(candidate[degree - 1])
            )
            if (
                degrees
                and 5 <= degrees[0] <= MAX_DEGREE
                and sum(degrees) % 2 == 0
                and sum(degrees) // 2 <= MAX_EDGES
            ):
                arithmetic.append(degrees)
        return

    value = comb(d, 2)
    for count in range(vertices_left + 1):
        used = count * value
        if used > target_left:
            break
        enumerate_multiplicities(
            d + 1,
            vertices_left - count,
            target_left - used,
            counts + [count],
        )


enumerate_multiplicities(1, N, TARGET, [])
arithmetic.sort(reverse=True)
graphical = [degrees for degrees in arithmetic if havel_hakimi(degrees)]
survivors = [degrees for degrees in graphical if lemma_5_3(degrees)]

expected = [
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 1, 1),
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 2, 1, 1, 1),
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 2, 2, 2),
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 2, 1),
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 2, 1),
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 1, 1),
    (5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3),
    (5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 2),
]

assert len(arithmetic) == 1368
assert len(graphical) == 1356
assert survivors == expected

print("method=multiplicity-DFS graphicality=Havel-Hakimi arithmetic=integer")
print(f"arithmetic={len(arithmetic)}")
print(f"graphical={len(graphical)}")
print(f"lemma_5_3_survivors={len(survivors)}")

for index, degrees in enumerate(survivors, 1):
    high = sum(d == 5 for d in degrees)
    supply = sum(d * (5 - d) for d in degrees if d < 5)
    edge_count = sum(degrees) // 2
    assert sum(comb(d, 2) for d in degrees) == TARGET
    if index <= 6:
        assert supply < 4 * high
        certificate = f"supply={supply}<4|H|={4 * high}"
    elif index == 7:
        assert (high, supply) == (9, 42)
        certificate = "sum_leave_degrees_on_H=6-C<=6<|H|=9"
    else:
        assert (high, supply) == (8, 42)
        # If C is the low--low deficiency cost, odd-degree parity gives
        # 8 <= 10-C, hence C<=2.  The minimum edge cost is two and equality
        # occurs only on a 4--4 edge, so q=e(L) is 0 or 1 and C=2q.
        for q in (0, 1):
            lower_triangle_incidence = 15 + q
            upper_triangle_incidence = 8 + 3 * q
            assert lower_triangle_incidence > upper_triangle_incidence
        certificate = "C=2q,q_in_{0,1}: 15+q>8+3q"
    print(
        f"case={index} edges={edge_count} high={high} "
        f"degrees={degrees} certificate={certificate}"
    )

print("STATUS VERIFIED")
