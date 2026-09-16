#!/usr/bin/env python3
"""Exact test of j=2 Abel certificates after lowering the common defect.

Run: python3 evidence/j2_reduced_prefix.py --drop 3 --kmin 5 --kmax 32
The coefficient expansion uses 2*B; reported prefixes divide by 4.
The data file from the defining product is checked, never overwritten.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
JOB = 'primary-20260914-chern-logconcavity-research-5a27c3ef60f2'


@lru_cache(None)
def D(n, h):
    if n == h == 0:
        return 1
    if h <= 0 or n < h + 1 or n > 2 * h:
        return 0
    return (n - 1) * (D(n - 1, h - 1) + D(n - 2, h - 1))


@lru_cache(None)
def multiplied(factors, r, h):
    """Newton coefficient of prod(d+a)*S_h, in unreduced D(n,h)."""
    if r < 0:
        return {}
    if not factors:
        return {r: 1, r + 1: 1}
    out = defaultdict(int)
    for n, c in multiplied(factors[:-1], r, h).items():
        out[n] += (r + factors[-1]) * c
    for n, c in multiplied(factors[:-1], r - 1, h).items():
        out[n] += r * c
    return dict(out)


@lru_cache(None)
def reduce_defect(n, h, target):
    if h == target:
        return {n: 1}
    out = defaultdict(int)
    for step in (1, 2):
        for q, c in reduce_defect(n - step, h - 1, target).items():
            out[q] += (n - 1) * c
    return dict(out)


@lru_cache(None)
def expansion(k, r, drop):
    """Return p_i in 2*B_{k,2,r}=sum_i p_i D(r+i,k-drop)."""
    out = defaultdict(int)
    for weight, factors, h in (
        (k * (k + 1), (), k),
        (-2 * k, (0, 2 - k), k - 1),
        (1, (0, 0, 3 - k, 2 - k), k - 2),
    ):
        for n, c in multiplied(factors, r, h).items():
            for q, v in reduce_defect(n, h, k - drop).items():
                out[q - r] += weight * c * v
    return {i: c for i, c in out.items() if c}


def quadratic(k, r, drop):
    p, left, right = [expansion(k, t, drop) for t in (r, r - 1, r + 1)]
    q = defaultdict(int)
    for a, x in p.items():
        for b, y in p.items():
            q[tuple(sorted((a, b)))] += x * y
    for a, x in left.items():
        for b, y in right.items():
            q[tuple(sorted((a - 1, b + 1)))] -= x * y
    return dict(q)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--drop', type=int, default=3)
    ap.add_argument('--kmin', type=int, default=5)
    ap.add_argument('--kmax', type=int, default=32)
    args = ap.parse_args()
    assert 2 <= args.drop < args.kmin <= args.kmax <= 32
    rows = {(row['k'], row['j']): row['B'] for row in
            json.loads((ROOT / 'exact-coefficients.json').read_text())}
    checks = minors = active = 0
    negatives = []
    per_k = []
    first_details = None
    for k in range(args.kmin, args.kmax + 1):
        target = k - args.drop
        bs = rows[k, 2]
        for r, b in enumerate(bs):
            got = sum(c * D(r + i, target)
                      for i, c in expansion(k, r, args.drop).items())
            assert got == 2 * b, (k, r, got, 2 * b)
            checks += 1
        negative_before = len(negatives)
        active_before = active
        for r in range(k - 1, 2 * k + 1):
            q = quadratic(k, r, args.drop)
            groups = defaultdict(list)
            for pair in q:
                groups[sum(pair)].append(pair)
            actual = bs[r] ** 2 - bs[r - 1] * (bs[r + 1] if r < 2 * k else 0)
            got = sum(c * D(r + a, target) * D(r + b, target)
                      for (a, b), c in q.items())
            assert got == 4 * actual and actual > 0
            minors += 1
            abel_total = 0
            for trace, pairs in sorted(groups.items()):
                pairs.sort(key=lambda z: z[1] - z[0])
                w = 0
                records = []
                for i, (a, b) in enumerate(pairs):
                    w += q[a, b]
                    u = D(r + a, target) * D(r + b, target)
                    v = (D(r + pairs[i + 1][0], target)
                         * D(r + pairs[i + 1][1], target)) if i + 1 < len(pairs) else 0
                    assert u >= v
                    abel_total += w * (u - v)
                    records.append({'pair': [a, b], 'coefficient': str(Fraction(q[a, b], 4)),
                                    'prefix': str(Fraction(w, 4)), 'U': u, 'next_U': v})
                    if u > v:
                        active += 1
                        if w < 0:
                            witness = {'k': k, 'r': r, 'trace': trace, 'pair': [a, b],
                                       'prefix': str(Fraction(w, 4)),
                                       'positive_Abel_difference': u - v,
                                       'actual_minor': actual}
                            negatives.append(witness)
                            if first_details is None:
                                first_details = {**witness, 'target_defect': target,
                                                 'B_triple': bs[r - 1:r + 2],
                                                 'twice_B_expansion': expansion(k, r, args.drop),
                                                 'trace_records': records.copy()}
                if (first_details is not None and first_details['k'] == k
                        and first_details['r'] == r and first_details['trace'] == trace):
                    first_details['trace_records'] = records
            assert abel_total == 4 * actual
        per_k.append({'k': k, 'active_prefixes': active - active_before,
                      'negative_active_prefixes': len(negatives) - negative_before})
    report = {'job_id': JOB,
              'kind': 'exact finite test of a named sufficient certificate; original unresolved',
              'scope': {'j': 2, 'k': [args.kmin, args.kmax],
                        'r': 'all k-1 <= r <= 2k', 'common_defect': f'k-{args.drop}'},
              'expansion_value_checks': checks, 'quadratic_and_Abel_identity_checks': minors,
              'active_prefix_checks': active, 'negative_active_prefixes': len(negatives),
              'certificate_rejected': bool(negatives), 'per_k': per_k,
              'first_negative': first_details,
              'all_negative_prefixes': negatives,
              'coefficient_input_sha256': hashlib.sha256((ROOT / 'exact-coefficients.json').read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256((ROOT.parent / 'source.md').read_bytes()).hexdigest()}
    out = ROOT / f'j2-defect-kminus{args.drop}.json'
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: val for key, val in report.items()
                      if key not in ('all_negative_prefixes', 'per_k')}, indent=2))


if __name__ == '__main__':
    main()
