#!/usr/bin/env python3
"""Exact replay of the overlap-poset and moment proof for pattern 21435.

This script is supplementary verification, not the mathematical proof.  It
constructs transitive closures from the defining inequalities, checks the
closed-form moments against direct multiset-word enumeration for every ordered
positive content through N=9, and prints the two critical distributions.  It
uses only integer arithmetic.
"""

from collections import Counter
from math import comb, factorial


# Local positions in increasing VALUE order for a 21435 occurrence.
VALUE_CHAIN = (1, 0, 3, 2, 4)


def relations(starts):
    edges = set()
    for start in starts:
        chain = tuple(start + x for x in VALUE_CHAIN)
        edges.update(zip(chain, chain[1:]))
    return edges


def closure(starts):
    vertices = set()
    for s in starts:
        vertices.update(range(s, s + 5))
    reach = {(u, v): False for u in vertices for v in vertices}
    for u, v in relations(starts):
        reach[u, v] = True
    for k in vertices:
        for i in vertices:
            for j in vertices:
                reach[i, j] = reach[i, j] or (reach[i, k] and reach[k, j])
    acyclic = all(not reach[v, v] for v in vertices)
    comparable = {
        frozenset((u, v))
        for u in vertices
        for v in vertices
        if u != v and (reach[u, v] or reach[v, u])
    }
    return tuple(sorted(vertices)), reach, acyclic, comparable


def unique_chain_order(starts):
    vertices, reach, acyclic, comparable = closure(starts)
    if not acyclic or len(comparable) != comb(len(vertices), 2):
        return None
    return tuple(sorted(vertices, key=lambda v: sum(reach[u, v] for u in vertices)))


def partitions(n, ceiling=None):
    if n == 0:
        yield ()
        return
    ceiling = n if ceiling is None else min(ceiling, n)
    for first in range(ceiling, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def coordinate_orders(parts):
    counts = Counter(parts)
    out = [0] * len(parts)

    def rec(i):
        if i == len(out):
            yield tuple(out)
            return
        for value in sorted(counts):
            if counts[value]:
                counts[value] -= 1
                out[i] = value
                yield from rec(i + 1)
                counts[value] += 1

    yield from rec(0)


def elementary(alpha, k):
    coeff = [1] + [0] * k
    for value in alpha:
        for j in range(k, 0, -1):
            coeff[j] += value * coeff[j - 1]
    return coeff[k]


def q_shift4(alpha):
    if len(alpha) == 9 and all(x == 1 for x in alpha):
        return 5
    if len(alpha) == 8 and sorted(alpha) == [1] * 7 + [2]:
        return int(alpha.index(2) + 1 <= 4)
    return 0


def predicted_moments(alpha):
    n = sum(alpha)
    den = 1
    for x in alpha:
        den *= factorial(x)
    b1 = 0
    if n >= 5:
        b1 = (n - 4) * factorial(n - 5) * elementary(alpha, 5) // den
    b2 = 0
    if n >= 7:
        c2 = factorial(n - 7) * elementary(alpha, 7) // den
        b2 += (n - 6) * c2
    if n == 9:
        b2 += q_shift4(alpha)
    return b1, b2


def direct_distribution(alpha):
    remaining = list(alpha)
    word = []
    dist = Counter()

    def rec(c):
        if len(word) == sum(alpha):
            dist[c] += 1
            return
        for j, left in enumerate(remaining):
            if not left:
                continue
            remaining[j] -= 1
            word.append(j + 1)
            added = 0
            if len(word) >= 5:
                a, b, c0, d, e = word[-5:]
                added = int(b < a < d < c0 < e)
            rec(c + added)
            word.pop()
            remaining[j] += 1

    rec(0)
    degree = max(dist, default=0)
    return tuple(dist[j] for j in range(degree + 1))


def main():
    overlap = {}
    for shift in range(1, 5):
        vertices, _, acyclic, comparable = closure((0, shift))
        overlap[shift] = {
            "acyclic": acyclic,
            "vertices": len(vertices),
            "comparable_pairs": len(comparable),
            "chain_order": unique_chain_order((0, shift)),
        }
    print("two_occurrence_overlaps", overlap)
    print("triple_chain", unique_chain_order((0, 2, 4)))

    tested_contents = 0
    tested_words = 0
    max_occurrence_repeated = 0
    critical = {}
    for n in range(1, 10):
        for parts in partitions(n):
            for alpha in coordinate_orders(parts):
                poly = direct_distribution(alpha)
                tested_contents += 1
                tested_words += sum(poly)
                b1 = sum(j * count for j, count in enumerate(poly))
                b2 = sum(comb(j, 2) * count for j, count in enumerate(poly))
                assert (b1, b2) == predicted_moments(alpha), (alpha, poly)
                if any(x > 1 for x in alpha):
                    max_occurrence_repeated = max(
                        max_occurrence_repeated, len(poly) - 1
                    )
                if n == 9 and sorted(alpha) == [1] * 7 + [2]:
                    critical[alpha.index(2) + 1] = poly

    print("checked", {"ordered_contents": tested_contents, "words": tested_words})
    print("max_occurrence_for_repeated_content", max_occurrence_repeated)
    print("critical_rank_polynomials", dict(sorted(critical.items())))


if __name__ == "__main__":
    main()
