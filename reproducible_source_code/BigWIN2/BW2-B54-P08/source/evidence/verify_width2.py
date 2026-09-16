#!/usr/bin/env python3
"""Independent small-order audit of enumerate_width2.py.

This script does not use the two-chain generator to define its comparison
domain.  It enumerates every subset of the forward pairs i<j, retains exactly
the transitive relations, filters width exactly two, and canonicalizes under
all n! permutations.  It then compares the resulting canonical set with the
two-chain generator.  A generic ideal-subset DP recomputes extension counts and
rank sums, while explicit DFS over all maximal cover paths recomputes the chain
predicate.  The exhaustive audit is intentionally bounded to n<=6.
"""

from __future__ import annotations

import itertools
import json

import numpy as np

from enumerate_width2 import presentations, test_one


def forward_relations(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for bits in range(1 << len(pairs)):
        below = [0] * n
        for k, (i, j) in enumerate(pairs):
            if bits >> k & 1:
                below[j] |= 1 << i
        transitive = True
        for k in range(n):
            for j in range(n):
                if below[k] >> j & 1 and below[j] & ~below[k]:
                    transitive = False
                    break
            if not transitive:
                break
        if transitive:
            yield tuple(below)


def width_two(below):
    n = len(below)
    def comparable(x, y):
        return bool((below[y] >> x & 1) or (below[x] >> y & 1))
    if all(comparable(x, y) for x in range(n) for y in range(x + 1, n)):
        return False
    for x, y, z in itertools.combinations(range(n), 3):
        if not comparable(x, y) and not comparable(x, z) and not comparable(y, z):
            return False
    return True


def relabel(below, p):
    """p[new_label]=old_label."""
    n = len(below)
    rows = []
    for y in range(n):
        row = 0
        for x in range(n):
            if below[p[y]] >> p[x] & 1:
                row |= 1 << x
        rows.append(row)
    return tuple(rows)


def canonical(below):
    return min(relabel(below, p) for p in itertools.permutations(range(len(below))))


def chain_relation(a, b, L, U):
    below = [0] * (a + b)
    for i in range(a):
        below[i] = (1 << i) - 1
        below[i] |= sum(1 << (a + j) for j in range(L[i]))
    for j in range(b):
        below[a + j] = ((1 << j) - 1) << a
        below[a + j] |= sum(1 << i for i in range(a) if U[i] <= j)
    return tuple(below)


def generic_ranks(below):
    n = len(below)
    full = (1 << n) - 1
    prefix = [0] * (1 << n)
    prefix[0] = 1
    for mask in range(1 << n):
        for x in range(n):
            if not (mask >> x & 1) and below[x] & ~mask == 0:
                prefix[mask | 1 << x] += prefix[mask]
    suffix = [0] * (1 << n)
    suffix[full] = 1
    for mask in range(full - 1, -1, -1):
        suffix[mask] = sum(
            suffix[mask | 1 << x] for x in range(n)
            if not (mask >> x & 1) and below[x] & ~mask == 0
        )
    sums = [0] * n
    for mask in range(1 << n):
        rank = mask.bit_count() + 1
        for x in range(n):
            if not (mask >> x & 1) and below[x] & ~mask == 0:
                sums[x] += prefix[mask] * suffix[mask | 1 << x] * rank
    return prefix[full], sums


def explicit_qualifies(below, extensions, sums):
    n = len(below)
    above = [0] * n
    for y in range(n):
        for x in range(n):
            if below[y] >> x & 1:
                above[x] |= 1 << y
    covers = [[] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if above[x] >> y & 1 and above[x] & below[y] == 0:
                covers[x].append(y)
    maximal_chains = []
    def dfs(path):
        x = path[-1]
        if above[x] == 0:
            maximal_chains.append(tuple(path))
        else:
            for y in covers[x]:
                dfs(path + [y])
    for x in range(n):
        if below[x] == 0:
            dfs([x])
    four_e = 4 * extensions
    for chain in maximal_chains:
        values = [0] + [sums[x] for x in chain] + [(n + 1) * extensions]
        if max(values[i + 1] - values[i] for i in range(len(values) - 1)) <= four_e:
            return False
    return True


def main():
    rows = []
    for n in range(2, 7):
        brute = {canonical(r) for r in forward_relations(n) if width_two(r)}
        by_chains = set()
        comparisons = 0
        for a in range(1, n // 2 + 1):
            b = n - a
            for L, U in presentations(a, b):
                relation = chain_relation(a, b, L, U)
                if not width_two(relation):
                    continue
                by_chains.add(canonical(relation))
                generic_e, generic_s = generic_ranks(relation)
                w, q, lattice_e, lattice_s = test_one(
                    np.asarray(L, np.int8), np.asarray(U, np.int8), a, b
                )
                assert w
                assert generic_e == int(lattice_e)
                assert generic_s == [int(x) for x in lattice_s[:n]]
                assert explicit_qualifies(relation, generic_e, generic_s) == bool(q)
                comparisons += 1
        assert brute == by_chains
        rows.append({
            "n": n, "unlabeled_width_two": len(brute),
            "two_chain_presentations_checked": comparisons,
            "canonical_sets_equal": True,
            "rank_and_chain_tests_equal": True,
        })
    print(json.dumps({"format": "width2-independent-audit-v1", "orders": rows}, sort_keys=True))


if __name__ == "__main__":
    main()
