#!/usr/bin/env python3
"""Finite test of the direct j=2 analogue of the source's Abel certificate.

This tests a specific sufficient certificate, not the original conjecture.
Uses equation (3.3) and the fixed-point-free permutation recurrence.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
import json
from pathlib import Path


@lru_cache(None)
def D(n, h):
    if n == h == 0:
        return 1
    if n <= 0 or h <= 0:
        return 0
    return (n - 1) * (D(n - 1, h - 1) + D(n - 2, h - 1))


def expansion(k, r):
    target = k - 2

    @lru_cache(None)
    def reduce(n, h):
        if h == target:
            return {n: 1}
        out = defaultdict(int)
        for step in [1, 2]:
            for idx, val in reduce(n - step, h - 1).items():
                out[idx] += (n - 1) * val
        return dict(out)

    def times(factors, n, h):
        if not factors:
            out = defaultdict(int)
            for idx in [n, n + 1]:
                for q, val in reduce(idx, h).items():
                    out[q] += val
            return out
        out = defaultdict(int)
        for q, val in times(factors[:-1], n, h).items():
            out[q] += (n + factors[-1]) * val
        for q, val in times(factors[:-1], n - 1, h).items():
            out[q] += n * val
        return out

    # A_{k,2}=k(k+1)/2 S_k-k*d*(d+2-k)*S_{k-1}
    #          +d^2*(d+3-k)*(d+2-k)/2*S_{k-2}, S_h=A_{h,0}.
    out = defaultdict(Fraction)
    for weight, factors, h in [
        (Fraction(k * (k + 1), 2), (), k),
        (-k, (0, 2 - k), k - 1),
        (Fraction(1, 2), (0, 0, 3 - k, 2 - k), k - 2)
    ]:
        for q, val in times(factors, r, h).items():
            out[q - r] += weight * val
    return {idx: val for idx, val in out.items() if val}


root = Path(__file__).resolve().parent
rows = json.loads((root / 'exact-coefficients.json').read_text())
checks = 0
for row in rows:
    if row['j'] != 2:
        continue
    k = row['k']
    for r, b in enumerate(row['B']):
        p = expansion(k, r)
        assert sum(val * D(r + idx, k - 2) for idx, val in p.items()) == b
        checks += 1

negative = []
prefix_count = 0
for k in range(4, 33):
    for r in range(k - 1, 2 * k + 1):
        p, left, right = [expansion(k, x) for x in (r, r - 1, r + 1)]
        q = defaultdict(Fraction)
        for a, x in p.items():
            for b, y in p.items():
                q[tuple(sorted((a, b)))] += x * y
        for a, x in left.items():
            for b, y in right.items():
                q[tuple(sorted((a - 1, b + 1)))] -= x * y
        groups = defaultdict(list)
        for pair in q:
            groups[sum(pair)].append(pair)
        for trace, pairs in groups.items():
            pairs.sort(key=lambda z: z[1] - z[0])
            w = Fraction(0)
            for i, (a, b) in enumerate(pairs):
                w += q[a, b]
                u = D(r + a, k - 2) * D(r + b, k - 2)
                v = (D(r + pairs[i + 1][0], k - 2)
                     * D(r + pairs[i + 1][1], k - 2)) if i + 1 < len(pairs) else 0
                assert u >= v
                if u > v:
                    prefix_count += 1
                    if w < 0:
                        negative.append({'k': k, 'r': r, 'trace': trace, 'pair': [a, b],
                                         'prefix': str(w), 'positive_Abel_difference': u - v})

report = {
    'kind': 'finite sufficient-certificate probe; no theorem or disproof claimed',
    'scope': 'j=2, 4<=k<=32, k-1<=r<=2k',
    'expansion_value_checks': checks,
    'active_prefix_checks': prefix_count,
    'negative_prefix_count': len(negative),
    'first_negative_prefixes': negative[:5],
    'common_defect': 'K=k-2',
    'method': 'source (3.3), defect recurrence, direct trace grouping and Abel prefixes'
}
(root / 'j2-prefix-probe.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
