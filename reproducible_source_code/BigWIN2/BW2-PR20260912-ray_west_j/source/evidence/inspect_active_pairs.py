"""Explore the adjacent gaps counted by Ray--West Cor. 8.6.

This is an insertion/synonymity implementation, not an intrinsic formula.
Coordinates are one-based original grid coordinates as in the primary paper.
"""
from itertools import combinations, permutations
from collections import defaultdict


def active_pairs(beta):
    m = len(beta)
    n = m+2
    groups = defaultdict(list)
    for a, b in combinations(range(n), 2):
        c = (a+1, b)
        keep = [i for i in range(n) if i not in (a, b)]
        for x, y in combinations(range(1, n+1), 2):
            r = (x, y-1)
            values = [v for v in range(1, n+1) if v not in (x, y)]
            for rho in ((0, 1), (1, 0)):
                if any(any(0 <= col < m and beta[col] == r[rho[t]]
                           for col in (c[t]-2, c[t]-1)) for t in (0, 1)):
                    continue
                p = [0]*n
                for pos, v in zip(keep, beta):
                    p[pos] = values[v-1]
                p[a], p[b] = (x, y) if rho == (0, 1) else (y, x)
                groups[tuple(p)].append((r, c, rho))
    matches = []
    counted_left = set()
    for ambient, triples in groups.items():
        triples.sort()
        for t, u in combinations(triples, 2):
            r, c, rho = t
            s, d, sigma = u
            if r[1] < s[0] and (c[1] < d[0] or d[1] < c[0]):
                # Cor. 8.6 counts active lefthand triples, not all choices
                # of a synonymous righthand triple. E.g. 2143 has a chain
                # of three active triples giving three synonymity pairs.
                if t in counted_left:
                    continue
                counted_left.add(t)
                gap = c[1]-1 if c[1] < d[0] else c[0]-3
                assert 0 <= gap < m-1
                matches.append({'gap_zero_based': gap, 'left': t, 'right': u,
                                'ambient': ambient})
    gaps = [x['gap_zero_based'] for x in matches]
    assert len(set(gaps)) == len(gaps), (beta, matches)
    return matches


if __name__ == '__main__':
    import json
    import sys
    beta = tuple(map(int, sys.argv[1].split(',')))
    print(json.dumps(active_pairs(beta), indent=2))
