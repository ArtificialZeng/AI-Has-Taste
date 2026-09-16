#!/usr/bin/env python3
"""Exact triage diagnostics; no universal theorem is certified by this run."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 128

def add(p, q):
    r = [0] * max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    return r

def shift_add(p, w):
    r = p[:] + [0] * w
    for i, c in enumerate(p):
        r[i+w] += c
    return r

def convolution(p, q):
    r = [0] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r

def multiplicities(n, k):
    if k == 0:
        yield [n]
    else:
        for m in range(n//(1 << k)+1):
            for rest in multiplicities(n-m*(1 << k), k-1):
                yield rest+[m]

def direct(n):
    if n == 0:
        return [1]
    r = [0]
    for mults in multiplicities(n, n.bit_length()-1):
        p = [1]
        for k, m in enumerate(mults):
            w = 1 << k
            e = n//w-m
            factor = [0] * (e*w+1)
            for j in range(e+1):
                factor[w*j] = math.comb(e, j)
            p = convolution(p, factor)
        r = add(r, p)
    return r

def turan(p, j):
    return p[j]**2-p[j-1]*p[j+1]

def main():
    polys = [[1], [1]]
    failures = {k: [] for k in ['total', 'A', 'B', 'mixed', 'sync_left',
                                 'sync_right', 'LA_plus_mixed', 'LB_plus_mixed']}
    first = {}
    rows = []
    for n in range(2, LIMIT+1):
        if n % 2:
            polys.append(polys[-1][:])
            continue
        a = [0] * (2*len(polys[n//2])-1)
        a[::2] = polys[n//2]
        for _ in range(n):
            a = shift_add(a, 1)
        b = polys[n-2][:]
        w = 2
        while n % w == 0:
            b = shift_add(b, w)
            w *= 2
        p = add(a, b)
        polys.append(p)
        assert len(a) == len(b) == len(p)
        assert p == p[::-1] and min(p) > 0
        assert len(p)-1 == sum((1 << k)*(n//(1 << k)) for k in range(1,n.bit_length()))
        counts = {key: 0 for key in failures}
        for j in range(1, len(p)-1):
            la, lb = turan(a, j), turan(b, j)
            left = a[j]*b[j]-a[j-1]*b[j+1]
            right = a[j]*b[j]-b[j-1]*a[j+1]
            mixed = left+right
            vals = dict(total=turan(p,j), A=la, B=lb, mixed=mixed,
                        sync_left=left, sync_right=right,
                        LA_plus_mixed=la+mixed, LB_plus_mixed=lb+mixed)
            assert vals['total'] == la+lb+mixed
            for key, val in vals.items():
                if val < 0:
                    counts[key] += 1
                    if n >= 6 and key not in first:
                        first[key] = dict(n=n, j=j, a=a[j-1:j+2], b=b[j-1:j+2],
                                          total=p[j-1:j+2], values=vals)
        for key, count in counts.items():
            if count:
                failures[key].append(n)
        rows.append(dict(n=n, degree=len(p)-1, failed_index_counts=counts))
    direct_checks = []
    for n in range(17):
        assert direct(n) == polys[n], n
        direct_checks.append(n)
    report = dict(job_id='primary-20260913-binary-subsum-shape-triage-b98ea643b894',
                  arithmetic='Exact Python integers; no randomness or floating point',
                  recurrence_even_n=[2,LIMIT], direct_partition_checks=direct_checks,
                  definitions=dict(A='(1+x)^n N_(n/2)(x^2)',
                    B='product_(i=1)^v2(n) (1+x^(2^i)) N_(n-2)(x)',
                    mixed='2*a_j*b_j-a_(j-1)*b_(j+1)-b_(j-1)*a_(j+1)',
                    LA='a_j^2-a_(j-1)*a_(j+1)', LB='b_j^2-b_(j-1)*b_(j+1)'),
                  failed_even_n=failures, first_failures_n_ge_6=first,
                  small_polynomials={str(n):polys[n] for n in [2,4,6,8]},
                  rows=rows,
                  limitation='Finite method diagnostics only; neither a proof nor a new paper result.')
    (ROOT/'evidence/triage_recurrence.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ['failed_even_n','first_failures_n_ge_6','small_polynomials']},indent=2))

if __name__ == '__main__':
    main()
