#!/usr/bin/env python3
"""Exact benchmark checks for the classical D5 and E6 kissing codes."""

from itertools import combinations, product


def rank_rational(matrix):
    from fractions import Fraction

    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                scale = a[r][col]
                a[r] = [x - scale * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def main():
    d5 = set()
    for i, j in combinations(range(5), 2):
        for a, b in product((-1, 1), repeat=2):
            v = [0] * 5
            v[i], v[j] = a, b
            d5.add(tuple(v))
    assert len(d5) == 40
    assert {sum(x * x for x in v) for v in d5} == {2}
    assert max(sum(x * y for x, y in zip(u, v)) for u in d5 for v in d5 if u != v) == 1
    assert rank_rational(list(d5)) == 5

    # E8 roots, scaled by two so all arithmetic is integral.
    e8 = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            v = [0] * 8
            v[i], v[j] = a, b
            e8.add(tuple(v))
    for signs in product((-1, 1), repeat=8):
        if sum(x == -1 for x in signs) % 2 == 0:
            e8.add(signs)
    assert len(e8) == 240
    a = (-2, -2, 0, 0, 0, 0, 0, 0)
    b = (0, 2, -2, 0, 0, 0, 0, 0)
    e6 = {
        r
        for r in e8
        if sum(x * y for x, y in zip(r, a)) == 0
        and sum(x * y for x, y in zip(r, b)) == 0
    }
    assert len(e6) == 72
    assert {sum(x * x for x in r) for r in e6} == {8}
    assert max(sum(x * y for x, y in zip(u, v)) for u in e6 for v in e6 if u != v) == 4
    assert rank_rational(list(e6)) == 6
    print("VERIFIED: D5 gives 40 kissing points in rank 5")
    print("VERIFIED: E6 gives 72 kissing points in rank 6")


if __name__ == "__main__":
    main()
