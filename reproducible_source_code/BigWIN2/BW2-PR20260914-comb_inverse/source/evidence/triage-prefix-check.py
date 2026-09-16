#!/usr/bin/env python3
"""Deterministic exact checks for the comb prefix reduction; Python stdlib only.

Run from project root: python3 evidence/triage-prefix-check.py
Output: evidence/triage-prefix-check.json (atomic replacement).
Finite checks do not certify an all-n identity or independent mathematical review.
"""
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timezone
from math import comb
from pathlib import Path

JOB = 'primary-20260914-comb-inverse-triage-109258fe42b6'

def vectors(d, budget, prefix=()):
    if not d:
        yield prefix
        return
    for a in range(budget + 1):
        yield from vectors(d - 1, budget - a, prefix + (a,))

def lower_ideals(n):
    # Bottom-to-top spine labels: r_i=2*i, s_i=2*i+1.
    pred = []
    for i in range(n):
        spine = sum(1 << (2*j) for j in range(i + 1))
        pred.extend([spine, spine | (1 << (2*i + 1))])
    return [tuple(j for j in range(2*n) if mask >> j & 1)
            for mask in range(1, 1 << (2*n))
            if all(not (mask >> j & 1) or mask & p == p
                   for j, p in enumerate(pred))]

def prefix_member(v):
    total = 0
    for i in range(len(v)//2):
        total += v[2*i] + max(v[2*i + 1] - 1, 0)
        if total > i + 1:
            return False
    return True

def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}

def mul(a, b):
    out = defaultdict(int)
    for i, u in a.items():
        for j, v in b.items():
            out[i+j] += u*v
    return {k: v for k, v in out.items() if v}

def series_mul(a, b, bound):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            if i+j <= bound:
                out[i+j] = add(out.get(i+j, {}), mul(u, v))
    return {k: v for k, v in out.items() if v}

def main():
    max_n = 12
    state = {(0, 0): 1}
    hs = [[1]]
    for n in range(1, max_n + 1):
        nxt = defaultdict(int)
        for (height, support), count in state.items():
            for cost in range(height + 2):
                weights = [(0, 1), (1, 1)] if cost == 0 else [(1, 2), (2, cost)]
                for degree, multiplicity in weights:
                    nxt[height + 1 - cost, support + degree] += count * multiplicity
        state = nxt
        h = [0] * (2*n + 1)
        for (_, support), count in state.items():
            h[support] += count
        hs.append(h)

    brute = []
    for n in range(6):
        ideals = lower_ideals(n)
        h = [0] * (2*n + 1)
        checked = 0
        for v in vectors(2*n, 2*n):
            checked += 1
            direct = all(sum(v[j] for j in ideal) <= len(ideal) for ideal in ideals)
            assert direct == prefix_member(v), (n, v)
            if direct:
                h[sum(a > 0 for a in v)] += 1
        assert checked == comb(4*n, 2*n)
        assert h == hs[n], (n, h, hs[n])
        brute.append({'n': n, 'ambient_vectors': checked,
                      'nonempty_ideals': len(ideals), 'coefficients': h})

    bound = max_n + 1
    f = {n+1: {j-n: v for j, v in enumerate(h) if v} for n, h in enumerate(hs)}
    power = {0: {0: 1}}
    composition = {}
    rs = {}
    for m in range(1, bound + 1):
        power = series_mul(power, f, bound)
        extra = mul({j: comb(m, j) for j in range(m+1)}, {j: 1 for j in range(m-1)})
        r = add({0: 1}, {j+1-m: v for j, v in extra.items()})
        r = {j: (-1)**(m-1)*v for j, v in r.items()}
        rs[m] = r
        for degree, p in power.items():
            composition[degree] = add(composition.get(degree, {}), mul(r, p))
    composition = {k: v for k, v in composition.items() if v}
    assert composition == {1: {0: 1}}, composition

    # Independently check the claimed rational expression for R by multiplication.
    denominator = {0: {0: 1}}
    for slope in [{0: 1}, {0: 1, 1: 1}, {-1: 1, 0: 1}]:
        denominator = series_mul(denominator, {0: {0: 1}, 1: slope}, bound)
    rational_residual = series_mul(rs, denominator, bound)
    assert rational_residual == {1: {0: 1}}, rational_residual

    result = {
        'job_id': JOB, 'observed_at_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        'arithmetic': 'exact integers and finite Laurent polynomials; no randomness',
        'brute_force': brute, 'ambient_vectors_total': sum(c['ambient_vectors'] for c in brute),
        'all_ideal_vs_prefix_checks_passed': True,
        'prefix_dp_coefficients_n_0_through_12': hs,
        'composition_checked_through_x_degree': bound,
        'R_of_F_residual': composition,
        'R_times_three_factor_denominator_residual': rational_residual,
        'uniform_proof': False, 'fresh_referee': False,
        'scope': 'The brute-force comparison is independent of the earlier intake implementation; this is the same triage context, not a fresh review.'
    }
    target = Path('evidence/triage-prefix-check.json')
    temporary = target.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(target)
    print(json.dumps({'output': str(target), 'brute_vectors': result['ambient_vectors_total'],
                      'checks_passed': True, 'composition_degree': bound,
                      'h_6': hs[6], 'h_12_at_1': sum(hs[12])}))

if __name__ == '__main__':
    main()
