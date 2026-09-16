#!/usr/bin/env python3
"""Exact finite sanity checks for win-00087-p01 triage; not a proof."""

from itertools import combinations


def tournament(n, mask):
    out = [set() for _ in range(n)]
    for bit, (a, b) in enumerate(combinations(range(n), 2)):
        if (mask >> bit) & 1:
            out[a].add(b)
        else:
            out[b].add(a)
    return out


def h_edges(out):
    n = len(out)
    ans = set()
    for a, b in combinations(range(n), 2):
        rest = set(range(n)) - {a, b}
        if rest <= out[a] or rest <= out[b]:
            ans.add(frozenset((a, b)))
    return ans


def star_or_exact_triangle(edges):
    if not edges:
        return True
    common = set.intersection(*(set(e) for e in edges))
    if common:
        return True
    vertices = set().union(*(set(e) for e in edges))
    return len(vertices) == 3 and len(edges) == 3


def check_structural_lemma(max_n=6):
    counts = {}
    for n in range(3, max_n + 1):
        total = 1 << (n * (n - 1) // 2)
        for mask in range(total):
            assert star_or_exact_triangle(h_edges(tournament(n, mask)))
        counts[n] = total
    return counts


def block_tournament(blocks, active):
    n = sum(map(len, blocks))
    owner = {v: j for j, block in enumerate(blocks) for v in block}
    out = [set() for _ in range(n)]
    cyclic = set()
    if len(blocks[active]) == 3:
        a, b, c = blocks[active]
        cyclic = {(a, b), (b, c), (c, a)}
    for a, b in combinations(range(n), 2):
        if owner[a] == active and owner[b] != active:
            winner = a
        elif owner[b] == active and owner[a] != active:
            winner = b
        elif (a, b) in cyclic:
            winner = a
        elif (b, a) in cyclic:
            winner = b
        else:
            winner = a
        loser = b if winner == a else a
        out[winner].add(loser)
    return out


def check_upper_construction(first_k=3, last_k=12):
    checked = {}
    for k in range(first_k, last_k + 1):
        blocks = [list(range(3)), list(range(3, 6))]
        blocks.extend([[v] for v in range(6, k + 3)])
        family = [block_tournament(blocks, j) for j in range(k - 1)]
        n = k + 3
        for u_tuple in combinations(range(n), k):
            u = set(u_tuple)
            assert any(
                any(v not in u and u <= out[v] for v in range(n))
                for out in family
            )
        checked[k] = len(list(combinations(range(n), k)))
    return checked


def check_cover_inequality(limit=100):
    for q in range(3, limit + 1):
        assert q * (q - 1) // 2 > 3 * (q - 3)


if __name__ == "__main__":
    structural = check_structural_lemma()
    upper = check_upper_construction()
    check_cover_inequality()
    print("structural tournaments checked:", structural)
    print("upper-construction k-subsets checked:", upper)
    print("cover inequality checked for 3 <= q <= 100")
