#!/usr/bin/env python3
"""Exact, exhaustive checks. No floating point or third-party packages.

Run from PROJECT_DIR: python3 evidence/verify_exact.py
Writes evidence/exact_checks.json deterministically.
"""
import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def cycle_lengths(q):
    seen = set()
    lengths = []
    for i in range(len(q)):
        if i in seen:
            continue
        j, k = i, 0
        while j not in seen:
            seen.add(j)
            k += 1
            j = q[j]
        lengths.append(k)
    return lengths

def det_leibniz(a):
    n = len(a)
    ans = 0
    for q in itertools.permutations(range(n)):
        if all(a[i][q[i]] for i in range(n)):
            inv = sum(q[i] > q[j] for i in range(n) for j in range(i+1,n))
            ans += (-1)**inv
    return ans

def coefficients(nmax, odd):
    # n f_n = (1/2) sum_{k allowed, k<=n} f_{n-k}, f_0=1.
    a = [F(1)]
    for n in range(1, nmax+1):
        a.append(sum((a[n-k] for k in range(2,n+1)
                      if not odd or k % 2), F(0))/(2*n))
    return a

def matrices(n):
    # Each row is one unordered column pair. Pruning only discards
    # partial assignments with a column sum >2 or impossible to fill.
    pairs = list(itertools.combinations(range(n),2))
    cols, rows = [0]*n, []
    def visit():
        if len(rows) == n:
            if cols == [2]*n:
                yield [[int(j in pair) for j in range(n)] for pair in rows]
            return
        for x,y in pairs:
            if cols[x] == 2 or cols[y] == 2:
                continue
            cols[x] += 1
            cols[y] += 1
            rows.append((x,y))
            remaining = n-len(rows)
            if all(c+remaining >= 2 for c in cols):
                yield from visit()
            rows.pop()
            cols[x] -= 1
            cols[y] -= 1
    yield from visit()

def main():
    d, h = coefficients(30,False), coefficients(30,True)
    records = []
    for n in range(2,10):
        total, good, derangements = 0, 0, 0
        for q in itertools.permutations(range(n)):
            lengths = cycle_lengths(q)
            if 1 in lengths:
                continue
            derangements += 1
            weight = 2**(n-len(lengths))
            total += weight
            if all(k % 2 for k in lengths):
                good += weight
        assert F(total, 2**n*math.factorial(n)) == d[n]
        assert F(good, 2**n*math.factorial(n)) == h[n]
        row = dict(n=n, permutations_visited=math.factorial(n),
                   derangements=derangements, scaled_weight_total=total,
                   scaled_weight_invertible=good, probability=str(h[n]/d[n]),
                   coefficient_D=str(d[n]), coefficient_H=str(h[n]))
        if n <= 5:
            hist = Counter()
            for a in matrices(n):
                assert all(sum(r)==2 for r in a)
                assert all(sum(a[i][j] for i in range(n))==2 for j in range(n))
                hist[det_leibniz(a)] += 1
            count = sum(hist.values())
            count_good = count-hist[0]
            assert F(count_good,count) == h[n]/d[n]
            assert count == math.factorial(n)**2*d[n]
            assert count_good == math.factorial(n)**2*h[n]
            row.update(matrix_total=count,matrix_invertible=count_good,
                       determinant_histogram=dict(sorted(hist.items())))
        records.append(row)
    # Cycle-block determinant verification, independently using Leibniz.
    blocks = []
    for n in range(2,9):
        a = [[int(j==i)+int(j==(i+1)%n) for j in range(n)] for i in range(n)]
        actual = det_leibniz(a)
        assert actual == 1-(-1)**n
        blocks.append(dict(length=n,determinant=actual))
    payload = dict(status="all exact assertions passed",
                   source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
                   coverage="All permutations for 2<=N<=9; all matrices for 2<=N<=5; cycle blocks 2<=N<=8.",
                   weight_scaling="Integer weight 2^(N-c); common scaling cancels.",
                   records=records,cycle_blocks=blocks,
                   coefficient_probabilities_to_30={str(n):str(h[n]/d[n]) for n in range(2,31)})
    (ROOT/'evidence/exact_checks.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({"status":payload['status'],"records":records},indent=2))

if __name__ == '__main__':
    main()
