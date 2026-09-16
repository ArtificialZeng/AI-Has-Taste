#!/usr/bin/env python3
"""Exact finite test of the frozen compensation invariant, research pass 1.

Run: python3 evidence/research_recurrence.py
No floating point is used for a mathematical decision. Integer packing performs
ordinary convolution: the base exceeds the sum of all product coefficients,
so no coefficient can carry into the next base digit.
"""
import hashlib
import json
import math
from pathlib import Path

from triage_recurrence import direct, shift_add

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-binary-subsum-shape-research-f5d9991a30d8'
LIMIT = 512


def convolution(p, q):
    bound = sum(p) * sum(q)
    width = max(1, (bound.bit_length() + 7) // 8)
    pp = int.from_bytes(b''.join(c.to_bytes(width, 'little') for c in p), 'little')
    qq = int.from_bytes(b''.join(c.to_bytes(width, 'little') for c in q), 'little')
    size = len(p) + len(q) - 1
    raw = (pp * qq).to_bytes(width * size, 'little')
    return [int.from_bytes(raw[i*width:(i+1)*width], 'little') for i in range(size)]


def turan(p, j):
    return p[j] * p[j] - p[j-1] * p[j+1]


def digest(p):
    return hashlib.sha256(json.dumps(p, separators=(',', ':')).encode()).hexdigest()


def build(limit):
    polys = [[1], [1]]
    for n in range(2, limit+1):
        if n % 2:
            polys.append(polys[-1])
            continue
        lifted = [0] * (2 * len(polys[n//2]) - 1)
        lifted[::2] = polys[n//2]
        a = convolution(lifted, [math.comb(n, j) for j in range(n+1)])
        b = polys[n-2][:]
        w = 2
        while n % w == 0:
            b = b + [0] * w
            # Descending order prevents reusing newly changed coefficients.
            for j in range(len(b)-1, w-1, -1):
                b[j] += b[j-w]
            w *= 2
        assert len(a) == len(b)
        p = [u+v for u, v in zip(a, b)]
        polys.append(p)
        yield n, a, b, p, polys


def main():
    source_sha = hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
    assert source_sha == '13e46a8af8569069d5eeadd7da3bb949452eccaa5e9472a43ebadec7f5231fdb'
    keys = ['total', 'A', 'B', 'mixed', 'compensation']
    first_target_failure = None
    first_original_failure = None
    rows = []
    independent_a_checks = []
    check_a_at = set(range(2, 34, 2)) | {130, 256, 512}
    for n, a, b, p, polys in build(LIMIT):
        degree = sum((1 << k) * (n // (1 << k)) for k in range(1, n.bit_length()))
        assert len(p) == degree+1
        assert p == p[::-1] and a == a[::-1] and b == b[::-1]
        assert min(p) > 0 and min(a) > 0 and min(b) >= 0
        if n in check_a_at:
            alt = [0] * (2 * len(polys[n//2]) - 1)
            alt[::2] = polys[n//2]
            for _ in range(n):
                alt = shift_add(alt, 1)
            assert alt == a, n
            independent_a_checks.append(n)
        counts = {key: 0 for key in keys}
        zeros = {key: 0 for key in keys}
        for j in range(1, len(p)-1):
            ta, tb, tn = turan(a, j), turan(b, j), turan(p, j)
            mixed = 2*a[j]*b[j]-a[j-1]*b[j+1]-b[j-1]*a[j+1]
            assert tn == ta+tb+mixed
            vals = dict(total=tn, A=ta, B=tb, mixed=mixed, compensation=tn-ta)
            for key, val in vals.items():
                counts[key] += val < 0
                zeros[key] += val == 0
            witness = None
            if n >= 130 and (ta < 0 or tn-ta < 0) and first_target_failure is None:
                witness = dict(n=n, j=j, A=a[j-1:j+2], B=b[j-1:j+2],
                               N=p[j-1:j+2], values=vals)
                first_target_failure = witness
            if n >= 6 and tn < 0 and first_original_failure is None:
                first_original_failure = witness or dict(n=n, j=j, A=a[j-1:j+2],
                    B=b[j-1:j+2], N=p[j-1:j+2], values=vals)
        rows.append(dict(n=n, degree=degree, internal_indices=degree-1,
                         negative_counts=counts, zero_counts=zeros, N_sha256=digest(p)))
        if n % 64 == 0:
            print('Completed every internal coefficient through n =', n, flush=True)
    direct_checks = []
    for n in range(17):
        assert direct(n) == polys[n], n
        direct_checks.append(n)
    target_rows = [row for row in rows if row['n'] >= 130]
    report = dict(job_id=JOB, source_sha256=source_sha,
        arithmetic='Exact arbitrary-precision integers; exhaustive internal coefficients',
        recurrence_even_n=[2, LIMIT], target_even_n=[130, LIMIT],
        target_polynomial_count=len(target_rows),
        target_internal_index_count=sum(row['internal_indices'] for row in target_rows),
        independent_pascal_A_checks=independent_a_checks,
        direct_partition_checks=direct_checks,
        first_target_invariant_failure=first_target_failure,
        first_original_counterexample=first_original_failure,
        failed_even_n={key:[r['n'] for r in rows if r['negative_counts'][key]] for key in keys},
        rows=rows,
        limitation='Finite evidence only. The infinite invariant and original remain unproved.')
    out = ROOT/'evidence/research_recurrence.json'
    temp = out.with_suffix('.tmp')
    temp.write_text(json.dumps(report, indent=2)+'\n')
    temp.replace(out)
    print(json.dumps({k:v for k,v in report.items() if k != 'rows'}, indent=2))


if __name__ == '__main__':
    main()
