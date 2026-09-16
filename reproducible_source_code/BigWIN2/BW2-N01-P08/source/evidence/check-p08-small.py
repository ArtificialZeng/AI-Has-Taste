#!/usr/bin/env python3
"""Bounded exact intake test for the literal user N/E orientation.

Count words by dynamic programming, independently enumerate tiny cases, and
isolate real roots using exact rational Sturm routines. No floating fit or seed.
Print JSON only; never edit a queue or assert a general theorem.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from math import comb
import json
import platform
import sympy as sp


def counts(m, n):
    # State (east, north, trailing north capped at two, NE count, NNE count).
    states = {(0, 0, 0, 0, 0): 1}
    for _ in range((m + 1) * n):
        nxt = defaultdict(int)
        for (e, h, last, k, j), value in states.items():
            if h < m * n:
                nxt[e, h+1, min(2, last+1), k, j] += value
            if e < n and h >= m * (e+1):
                nxt[e+1, h, 0, k+(last>0), j+(last==2)] += value
        states = nxt
    result = defaultdict(Counter)
    for (e, h, last, k, j), value in states.items():
        assert (e, h) == (n, m*n)
        result[k][j] += value
    return result


def enumerate_words(m, n):
    result = defaultdict(Counter)
    def visit(word, e, h):
        if (e, h) == (n, m*n):
            k = sum(word[i:i+2] == 'NE' for i in range(len(word)-1))
            j = sum(word[i:i+3] == 'NNE' for i in range(len(word)-2))
            result[k][j] += 1
            return
        if h < m*n:
            visit(word+'N', e, h+1)
        if e < n and h >= m*(e+1):
            visit(word+'E', e+1, h)
    visit('', 0, 0)
    return result


if __name__ == '__main__':
    t = sp.Symbol('t')
    rows = []
    failures = []
    for m in range(2, 5):
        for n in range(1, 9):
            data = counts(m, n)
            if n <= 4:
                assert data == enumerate_words(m, n), (m, n, 'independent enumeration')
            assert sum(sum(c.values()) for c in data.values()) == comb((m+1)*n, n)//(m*n+1)
            for k in range(1, n+1):
                coefficients = [data[k][j] for j in range(max(data[k])+1)]
                total = sum(coefficients)
                expected = Fraction(comb(n,k)*comb(m*n,k-1), n)
                assert total == expected, (m,n,k,'Fuss-Narayana consistency')
                poly = sp.Poly(sum(c*t**j for j,c in enumerate(coefficients)), t, domain=sp.ZZ)
                intervals = poly.intervals()
                real_multiplicity = sum(mult for _, mult in intervals)
                row = dict(m=m,n=n,k=k,coefficients_ascending=coefficients,
                           degree=int(poly.degree()),real_root_multiplicity=real_multiplicity,
                           all_roots_real=real_multiplicity==poly.degree())
                rows.append(row)
                if not row['all_roots_real']:
                    failures.append(row)
    print(json.dumps(dict(python=platform.python_version(),sympy=sp.__version__,
        domain='exact integers and rationals',randomness='none',
        scope={'m':[2,4],'n':[1,8],'k':'all 1..n'},
        independent_word_enumeration_n=[1,4],root_method='sympy Poly.intervals over ZZ; multiplicities sum to degree',
        tested_polynomials=len(rows),failures=failures,rows=rows,
        conclusion='bounded observation only, not an all-parameter proof')))
