"""Exact verification for the partition-jump proof dossier (standard library).

Run from the project root: python3 evidence/research_check.py
This is not a formal proof checker. The infinite theorem is in research-proof.md.
"""
from collections import Counter
from itertools import combinations, zip_longest
from math import isqrt
from pathlib import Path
import json


def partitions(n, least=1):
    if n == 0:
        yield ()
        return
    for first in range(least, n + 1):
        for tail in partitions(n - first, first):
            yield tail + (first,)


def moves(lam):
    counts = Counter(lam)
    for p in counts:
        for q in [0] + list(counts):
            if p == q and counts[p] < 2:
                continue
            c = counts.copy()
            c[p] -= 1
            if q:
                c[q] -= 1
            if p > 1:
                c[p - 1] += 1
            c[q + 1] += 1
            assert all(v >= 0 for v in c.values())
            mu = tuple(sorted((x for x, m in c.items() for _ in range(m)),
                              reverse=True))
            if mu != lam:
                yield p, q, mu


def neighbors(lam):
    return {mu for _, _, mu in moves(lam)}


def gap_count(support):
    sizes = sorted(support, reverse=True)
    return sum(x - y > 1 for x, y in zip(sizes, sizes[1:] + [0]))


def invariants(lam):
    c = Counter(lam)
    sizes = sorted(c, reverse=True)
    r = len(sizes)
    a = [int(c[x] == 1) for x in sizes]
    b = [int(x - y == 1) for x, y in zip(sizes, sizes[1:] + [0])]
    A = gap_count(c)
    B = sum(m >= 2 for m in c.values())
    capacity = max([r + 1 - u - v for u, v in zip(a, b)] +
                   [r - u - v for u, v in zip(a + [0], [0] + b)])
    staircase = lam == tuple(range(r, 0, -1))
    H = any(x >= 2 and m >= 2 and x - 1 not in c for x, m in c.items())
    epsilon = -1 if staircase else (1 if H else 0)
    assert capacity == r + epsilon
    return {'r': r, 'epsilon': epsilon, 'A': A, 'B': B,
            'degree': r * (r - 1) + A + B, 'delta': capacity}


def l1_adjacent(lam, mu):
    return sum(abs(a - b) for a, b in zip_longest(lam, mu, fillvalue=0)) == 2


def clique_by_subsets(vs, adj):
    """Reject every larger subset before returning a maximum clique."""
    vs = sorted(vs)
    tested = 0
    for size in range(len(vs), -1, -1):
        for subset in combinations(vs, size):
            tested += 1
            if all(w in adj[v] for v, w in combinations(subset, 2)):
                return subset, tested
    raise AssertionError('empty clique must exist')


def direct_dimension(lam):
    ns = neighbors(lam)
    adj = {v: {w for w in ns if w != v and l1_adjacent(v, w)} for v in ns}
    return len(clique_by_subsets(ns, adj)[0])


def run(max_n=30):
    output = {'arithmetic': 'exact integers and finite sets',
              'finite_direct_clique_range': [2, 13],
              'expanded_formula_and_edge_range': [2, max_n],
              'finite_graphs': [], 'expanded_rows': [], 'transfer_categories': {},
              'failures': []}
    categories = Counter()
    total_vertices = total_edges = subset_tests = 0
    for n in range(2, max_n + 1):
        vertices = sorted(partitions(n))
        assert len(vertices) == len(set(vertices))
        assert all(sum(v) == n and tuple(sorted(v, reverse=True)) == v
                   for v in vertices)
        inv = {v: invariants(v) for v in vertices}
        adj = {v: neighbors(v) for v in vertices}
        all_vertices = set(vertices)
        assert all(adj[v] <= all_vertices for v in vertices)
        assert all(v in adj[w] for v in vertices for w in adj[v])
        assert all(len(adj[v]) == inv[v]['degree'] for v in vertices)
        if n <= 13:
            pair_adj = {v: set() for v in vertices}
            for v, w in combinations(vertices, 2):
                if l1_adjacent(v, w):
                    pair_adj[v].add(w)
                    pair_adj[w].add(v)
            assert pair_adj == adj
            records = []
            for v in vertices:
                clique, tested = clique_by_subsets(pair_adj[v], pair_adj)
                subset_tests += tested
                assert len(clique) == inv[v]['delta']
                records.append({'partition': v, 'degree': len(adj[v]),
                                'delta': len(clique), 'clique_neighbors': clique})
            output['finite_graphs'].append({'n': n, 'vertex_records': records})
        edges = [(v, w) for v in vertices for w in adj[v] if v < w]
        for v, w in edges:
            left, right = sorted((v, w), key=lambda z: inv[z]['r'])
            a, b = inv[left], inv[right]
            k = b['r'] - a['r']
            assert 0 <= k <= 2
            if k == 0:
                assert a['epsilon'] != -1 and b['epsilon'] != -1
            if k == 1:
                assert a['epsilon'] != -1
            if k == 2:
                assert a['epsilon'] == 1
            jump = b['delta'] - a['delta']
            assert abs(jump) <= 2
            equality = (k == 1 and a['epsilon'] == 0 and b['epsilon'] == 1 or
                        k == 2 and a['epsilon'] == b['epsilon'] == 1)
            assert (abs(jump) == 2) == equality
            assert abs(b['A'] - a['A']) <= 4
            assert abs(b['B'] - a['B']) <= 4
            baseline = b['r'] * (b['r'] - 1) - a['r'] * (a['r'] - 1)
            assert abs(b['degree'] - a['degree'] - baseline) <= 8
        for v in vertices:
            for p, q, w in moves(v):
                categories['all_legal_size_descriptions'] += 1
                categories['equal_donor_recipient'] += p == q
                categories['new_row'] += q == 0
                categories['vanished_unit_donor'] += p == 1
                categories['coincident_output_sizes'] += p - 1 == q + 1
                if inv[w]['r'] - inv[v]['r'] == 2:
                    categories['support_increase_two'] += 1
                    assert p > 1 and p - 1 not in v
                    assert Counter(v)[p] >= (3 if p == q else 2)
                if inv[v]['epsilon'] == -1:
                    assert inv[w]['r'] < inv[v]['r']
        Dd = max(abs(inv[v]['degree'] - inv[w]['degree']) for v, w in edges)
        Dc = max(abs(inv[v]['delta'] - inv[w]['delta']) for v, w in edges)
        expected = 0 if n <= 3 else (2 if n == 11 or n >= 14 else 1)
        assert Dc == expected
        s = (isqrt(8 * n + 1) - 1) // 2
        if n >= 10:
            assert 4 * s - 8 <= Dd <= 4 * s + 2
        output['expanded_rows'].append({'n': n, 'vertices': len(vertices),
                                       'edges': len(edges), 'D_d': Dd, 'D_delta': Dc})
        total_vertices += len(vertices)
        total_edges += len(edges)

    degree_tests = 0
    for s in range(4, 21):
        for q in range(s + 1):
            mu = (s + q,) + tuple(range(s - 1, 0, -1))
            lam = (s + q,) + tuple(range(s - 1, 3, -1)) + (3, 3)
            assert sum(mu) == sum(lam) == s * (s + 1) // 2 + q
            assert mu in neighbors(lam)
            assert len(neighbors(mu)) - len(neighbors(lam)) == 4 * s - 8
            degree_tests += 1

    dimension_pairs = [((4, 4, 3), (4, 4, 2, 1)),
                       ((5, 5, 4), (5, 5, 3, 1))]
    ks = list(range(4, 101)) + [1000, 10**6, 10**12]
    for k in ks:
        dimension_pairs.append((tuple(sorted((k, 4, 4, 3), reverse=True)),
                                tuple(sorted((k, 4, 4, 2, 1), reverse=True))))
    for lam, mu in dimension_pairs:
        assert sum(lam) == sum(mu) and mu in neighbors(lam)
        assert direct_dimension(mu) - direct_dimension(lam) == 2

    gap_tests = 0
    for mask in range(1 << 10):
        support = {i + 1 for i in range(10) if mask & (1 << i)}
        for x in range(1, 12):
            if x not in support:
                assert abs(gap_count(support | {x}) - gap_count(support)) <= 1
                gap_tests += 1

    output['transfer_categories'] = dict(categories)
    output['coverage'] = {'expanded_vertices': total_vertices,
                          'expanded_undirected_edges': total_edges,
                          'small_vertices': sum(len(g['vertex_records'])
                                                for g in output['finite_graphs']),
                          'small_clique_subsets_tested': subset_tests,
                          'degree_family_all_q_tests': degree_tests,
                          'degree_family_s_range': [4, 20],
                          'dimension_family_tests': len(dimension_pairs),
                          'dimension_k_values': ks,
                          'support_insertion_checks': gap_tests}
    dest = Path('evidence/research_check.json')
    temp = dest.with_suffix('.json.tmp')
    temp.write_text(json.dumps(output, indent=2) + '\n')
    temp.replace(dest)
    print(json.dumps({'coverage': output['coverage'], 'failures': [],
                      'output': str(dest)}, indent=2))


if __name__ == '__main__':
    run()
