#!/usr/bin/env python3
"""Validate rdp.Counter against brute force on small grids.

Brute force: enumerate every simple cycle of the (m+1)x(n+1) grid graph by DFS
(each cycle once: rooted at its smallest vertex, one orientation), compute its
signature, and group.  Then for every signature, rdp must return exactly the
group size; for random clue diagrams it must return the group size (usually 0).
"""
import random
import sys
from collections import Counter as Multiset
from rdp import Counter, check_solution


def cycles(m, n):
    V = [(r, c) for r in range(m + 1) for c in range(n + 1)]
    idx = {v: i for i, v in enumerate(V)}

    def nb(v):
        r, c = v
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            x, y = r + dr, c + dc
            if 0 <= x <= m and 0 <= y <= n:
                yield (x, y)

    out = []
    for s in V:
        si = idx[s]
        path = [s]
        onp = {s}

        def dfs(v):
            for w in nb(v):
                if idx[w] < si:
                    continue
                if w == s and len(path) >= 4:
                    if idx[path[1]] < idx[path[-1]]:
                        out.append(list(path))
                    continue
                if w in onp:
                    continue
                path.append(w)
                onp.add(w)
                dfs(w)
                path.pop()
                onp.discard(w)
        dfs(s)
    return out


def edges_of(cyc):
    E = set()
    for i in range(len(cyc)):
        a, b = cyc[i], cyc[(i + 1) % len(cyc)]
        a, b = min(a, b), max(a, b)
        if a[0] == b[0]:
            E.add(('h', a[0], a[1]))
        else:
            E.add(('v', a[0], a[1]))
    return frozenset(E)


def signature(E, m, n):
    rows = []
    for r in range(m):
        s = ''
        for c in range(n):
            s += str((('h', r, c) in E) + (('h', r + 1, c) in E) + (('v', r, c) in E) + (('v', r, c + 1) in E))
        rows.append(s)
    return tuple(rows)


def main():
    random.seed(1)
    for (m, n) in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 3), (2, 5), (3, 4), (4, 4), (3, 5), (5, 3)]:
        cyc = cycles(m, n)
        groups = {}
        for cy in cyc:
            E = edges_of(cy)
            groups.setdefault(signature(E, m, n), set()).add(E)
        dist = Multiset(len(g) for g in groups.values())
        bad = 0
        for sig, g in groups.items():
            C = Counter(sig)
            cnt = C.count()
            if cnt != len(g):
                bad += 1
                print('MISMATCH', m, n, sig, cnt, len(g))
            elif len(g) > 1:
                sols = set(C.solutions())
                if sols != g or not all(check_solution(sig, s)[0] for s in sols):
                    bad += 1
                    print('SOLUTION SET MISMATCH', sig)
        # random diagrams (clue 2 weighted, to get some nonzero counts)
        for _ in range(300):
            sig = tuple(''.join(random.choice('0122223') for _ in range(n)) for _ in range(m))
            cnt = Counter(sig).count()
            if cnt != len(groups.get(sig, ())):
                bad += 1
                print('RANDOM MISMATCH', sig, cnt)
        print(f'{m}x{n}: cycles={len(cyc)} signatures={len(groups)} multiplicity distribution={dict(sorted(dist.items()))} mismatches={bad}')
        sys.stdout.flush()


if __name__ == '__main__':
    main()
