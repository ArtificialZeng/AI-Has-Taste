#!/usr/bin/env python3
"""Bounded exact validation. Run from the project root with Python 3."""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time

MAX_D = 16
S = [[0] * (MAX_D + 1) for _ in range(MAX_D + 1)]
S[0][0] = 1
for n in range(1, MAX_D + 1):
    for k in range(1, n + 1):
        S[n][k] = S[n-1][k-1] + k*S[n-1][k]

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

def transpose(a):
    return list(map(list, zip(*a)))

def direct(d):
    local = [[C(r, a)*sum(factorial(l)**2*S[a][l]*S[r-a][l]
                         for l in range(min(a, r-a)+1))
              for a in range(r+1)] for r in range(d+1)]
    return [[sum(C(j,s)*C(d-j,d-r-s)*local[r][i-s]
                 for r in range(d+1) for s in range(i+1) if 0 <= i-s <= r)
             for j in range(d+1)] for i in range(d+1)]

def from_faces(d):
    q = [[C(k,i)*sum(factorial(l)*S[i][l]*l**(k-i) for l in range(i+1))
          if i <= k else 0 for k in range(d+1)] for i in range(d+1)]
    b = [[(-1)**(i-k)*C(d-k,d-i) if k <= i else 0
          for k in range(d+1)] for i in range(d+1)]
    bi = [[C(d-j,d-k) if j <= k else 0
           for j in range(d+1)] for k in range(d+1)]
    assert multiply(b, bi) == [[int(i == j) for j in range(d+1)] for i in range(d+1)]
    return multiply(multiply(b, q), bi)

def determinant(a):
    """Integer Bareiss determinant, with explicit row swaps and exact divisions."""
    a = [row[:] for row in a]
    n = len(a)
    prev = sign = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k+1,n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot - a[i][k]*a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

def all_minors(a):
    n = len(a)
    counts = []
    for k in range(1,n+1):
        signs = {'negative':0, 'zero':0, 'positive':0}
        for rows in combinations(range(n),k):
            for cols in combinations(range(n),k):
                det = determinant([[a[i][j] for j in cols] for i in rows])
                signs['positive' if det > 0 else 'zero' if det == 0 else 'negative'] += 1
                if det < 0:
                    return {'negative_witness':{'rows':rows,'cols':cols,'det':det},'partial_counts':counts}
        assert sum(signs.values()) == comb(n,k)**2
        counts.append({'order':k, **signs})
    return {'total':sum(sum(c[s] for s in ('negative','zero','positive')) for c in counts),
            'counts':counts}

def ne(a):
    """No-swap adjacent-row elimination; do not invent multipliers at bad pivots."""
    start = [[Fraction(x) for x in row] for row in a]
    b = [row[:] for row in start]
    ops = []
    n = len(b)
    for j in range(n-1):
        for i in range(n-1,j,-1):
            target, pivot = b[i][j], b[i-1][j]
            if target == 0:
                continue
            if pivot == 0:
                return {'failure':'nonzero target above zero denominator','column':j,'row':i}
            m = target/pivot
            ops.append((i,j,m))
            b[i] = [x-m*y for x,y in zip(b[i],b[i-1])]
    assert all(b[i][j] == 0 for i in range(n) for j in range(i))
    restored = [row[:] for row in b]
    for i,j,m in reversed(ops):
        restored[i] = [x+m*y for x,y in zip(restored[i],restored[i-1])]
    assert restored == start
    return b, ops

def factor_check(a):
    first = ne(transpose(a))
    if isinstance(first,dict):
        return first
    u, lower = first
    second = ne(transpose(u))
    if isinstance(second,dict):
        return second
    diagonal, upper = second
    assert all(x == 0 for i,row in enumerate(diagonal) for j,x in enumerate(row) if i != j)
    good = all(m >= 0 for i,j,m in lower+upper) and all(diagonal[i][i] > 0 for i in range(len(a)))
    return {'nonnegative_factors':good, 'both_reconstructions_exact':True,
            'orientation':'H_d transpose = lower elementary factors * positive diagonal * upper elementary factors',
            'lower_operations':[[i,j,str(m)] for i,j,m in lower],
            'upper_transposed_operations':[[i,j,str(m)] for i,j,m in upper],
            'diagonal':[str(diagonal[i][i]) for i in range(len(a))]}

def main():
    started = time.monotonic()
    out = {'job_id':'primary-20260914-antiprism-total-positivity-triage-f5eff4f77594',
           'arithmetic':'Python integers and fractions.Fraction; no floating-point mathematical tests',
           'source_sha256':hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
           'definition_comparison':[], 'all_minors':{}, 'factorizations':{}, 'small_matrices':{}}
    previous = None
    for d in range(MAX_D+1):
        h = direct(d)
        assert h == from_faces(d), ('formula mismatch',d)
        assert h[0] == [1]+[0]*d and h[-1] == [0]*d+[1]
        if d:
            for j in range(1,d+1):
                for i in range(d+1):
                    term1 = previous[i-1][j-1] if i >= 1 else 0
                    term2 = previous[i][j-1] if i < d else 0
                    assert h[i][j] == h[i][j-1] + term1 - term2
        out['definition_comparison'].append({'d':d,'equal':True,'boundary_rows':True,'recurrence_21':bool(d)})
        if d <= 5:
            out['small_matrices'][str(d)] = h
        if 1 <= d <= 8:
            out['all_minors'][str(d)] = all_minors(h)
        if d:
            out['factorizations'][str(d)] = factor_check(h)
        previous = h
        # Durable incremental result; replacing a complete JSON file atomically.
        out['elapsed_seconds'] = round(time.monotonic()-started,3)
        target = Path('evidence/triage_exact.json')
        tmp = target.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(out,indent=2)+'\n')
        tmp.replace(target)
        print(json.dumps({'d':d,'definitions_equal':True,
                          'all_minors':out['all_minors'].get(str(d),{}).get('total'),
                          'factor_nonnegative':out['factorizations'].get(str(d),{}).get('nonnegative_factors')}),flush=True)
    print('elapsed_seconds',out['elapsed_seconds'])

if __name__ == '__main__':
    main()
