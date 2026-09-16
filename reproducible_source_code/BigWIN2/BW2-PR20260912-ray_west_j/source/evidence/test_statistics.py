"""Exact bounded triage experiment; run with python3 evidence/test_statistics.py.

For every ambient permutation, delete two positions and deduplicate its patterns.
This counts superpermutations, not embeddings. No fitted formula is a proof.
"""
from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
P3 = list(permutations(range(1, 4)))


def standardize(p):
    ranks = {v: i + 1 for i, v in enumerate(sorted(p))}
    return tuple(ranks[v] for v in p)


def upper_counts(m):
    n = m + 2
    deletions = [(a, b, tuple(i for i in range(n) if i != a and i != b))
                 for a, b in combinations(range(n), 2)]
    result = Counter()
    for p in permutations(range(1, n + 1)):
        patterns = set()
        for a, b, keep in deletions:
            x, y = p[a], p[b]
            patterns.add(tuple(p[i] - (x < p[i]) - (y < p[i]) for i in keep))
        result.update(patterns)
    return result


def features(p):
    m = len(p)
    invp = tuple(p.index(v) + 1 for v in range(1, m + 1))
    inv = sum(p[a] > p[b] for a, b in combinations(range(m), 2))
    pc = Counter(standardize(t) for t in combinations(p, 3))
    des = lambda q: tuple(i + 1 for i in range(len(q) - 1) if q[i] > q[i + 1])
    d, di = des(p), des(invp)
    bonds = tuple(sum(p[i + 1] - p[i] == sign for i in range(m - 1))
                  for sign in (1, -1))
    small = (m, inv) + tuple(pc[q] for q in P3)
    std = (m, inv, len(d), sum(d), len(di), sum(di)) + bonds
    return {'classical_le3': small,
            'standard_and_bonds': std,
            'classical_le3_and_standard_and_bonds': small + std[2:]}


def direct_g2(beta):
    """Independent insertion oracle, with no ambient-permutation loop."""
    n = len(beta) + 2
    result = set()
    for positions in combinations(range(n), len(beta)):
        missing_positions = [i for i in range(n) if i not in positions]
        for values in combinations(range(1, n + 1), len(beta)):
            missing_values = [v for v in range(1, n + 1) if v not in values]
            for rest in permutations(missing_values):
                p = [0] * n
                for pos, v in zip(positions, beta):
                    p[pos] = values[v - 1]
                for pos, v in zip(missing_positions, rest):
                    p[pos] = v
                result.add(tuple(p))
    return len(result)


def main():
    rows, histograms, collisions, tables = [], {}, {}, {}
    for m in range(1, 8):
        counts = upper_counts(m)
        base = (m**4 + 2*m**3 + m*m + 4*m + 4) // 2
        seen = {}
        histograms[m] = dict(sorted(Counter(base - g for g in counts.values()).items()))
        tables[m] = {p: base-g for p, g in counts.items()}
        for p in sorted(counts):
            g, j = counts[p], base - counts[p]
            assert 0 <= j <= m - 1
            rows.append({'beta': list(p), 'g2': g, 'j': j})
            for name, f in features(p).items():
                key = (name, f)
                if key in seen and seen[key][1] != j and name not in collisions:
                    q, jq = seen[key]
                    collisions[name] = {'beta': list(q), 'gamma': list(p),
                                        'j_beta': jq, 'j_gamma': j,
                                        'shared_features': list(f)}
                seen.setdefault(key, (p, j))
        print('m=', m, 'j histogram=', histograms[m], flush=True)
        (OUT / 'exact-counts.json').write_text(json.dumps(rows, indent=2) + '\n')
    calibration = {}
    for p, expected in [((1,), 0), ((2,4,1,3),2),
                        ((1,2,3,4,5),4), ((1,4,5,2,3),3),
                        ((1,4,2,5,3),2), ((4,1,2,5,3),1),
                        ((2,5,3,1,4),0)]:
        got = tables[len(p)][p]
        assert got == expected
        calibration[''.join(map(str, p))] = got
    for c in collisions.values():
        for key in ('beta', 'gamma'):
            p = tuple(c[key]); m = len(p)
            g = direct_g2(p)
            assert (m**4+2*m**3+m*m+4*m+4)//2-g == c['j_'+key]
            c['independent_g2_'+key] = g
    report = {'job_id': 'primary-20260912-ray-west-j-triage-b0b8b2bcc0bf',
              'coverage': 'All beta in S_m for 1<=m<=7; all ambient S_(m+2)',
              'feature_definitions': {
                  'classical_le3': '[m, inversions, #123, #132, #213, #231, #312, #321]',
                  'standard_and_bonds': '[m, inversions, descents, major index, inverse descents, inverse major index, increasing bonds, decreasing bonds]',
                  'classical_le3_and_standard_and_bonds': 'classical_le3 followed by standard_and_bonds with m and inversions omitted',
                  'bond': 'adjacent positions with value difference +1 or -1'},
              'histograms': histograms, 'calibration_j': calibration,
              'collisions': collisions,
              'status': 'Exact finite observations; no universal positive formula or novelty claim'}
    (OUT / 'statistics-test.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
