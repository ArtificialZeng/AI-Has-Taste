#!/usr/bin/env python3
"""Diamond decompositions of the differences between the solutions found by rdp.

B(i) follows Beluhov (arXiv:2308.08798, Sec. 4): on the N x N vertex grid with
1-based coordinates (x to the right, y upwards), D(i) is the rectangle with
corners (1/2, i+1/2), (i+1/2, 1/2), (N-i+1/2, N+1/2), (N+1/2, N-i+1/2), and
B(i) is the set of grid edges inside D(i), 1 <= i <= N-1.
Our edges: ('h', r, c) = (r,c)-(r,c+1), ('v', r, c) = (r,c)-(r+1,c), r = row from
the top (0-based), c = column (0-based).  So x = c + 1, y = m + 1 - r.
"""
import json
import itertools
from kernel_count import is_totally_even


def diamond(m, i):
    N = m + 1
    B = set()
    for r in range(m + 1):
        for c in range(m + 1):
            for e in (('h', r, c), ('v', r, c)):
                if e[0] == 'h' and c >= m:
                    continue
                if e[0] == 'v' and r >= m:
                    continue
                if e[0] == 'h':
                    mx, my = c + 1.5, m + 1 - r
                else:
                    mx, my = c + 1, m + 1 - r - 0.5
                if i + 1 <= mx + my <= 2 * N - i + 1 and -i <= mx - my <= i:
                    B.add(e)
    return frozenset(B)


def decompose(E, D):
    for k in range(len(D) + 1):
        for comb in itertools.combinations(range(len(D)), k):
            X = frozenset()
            for j in comb:
                X = X ^ D[j]
            if X == E:
                return [j + 1 for j in comb]
    return None


def fmt(dec):
    return '0' if not dec else '+'.join(f'B{i}' for i in dec)


if __name__ == '__main__':
    data = json.load(open('solutions.json'))
    for name in ['a_13x13_claim5', 'b_12x12_claim6', 'c_13x13_claim6', 'd_knuth6x6_claim4']:
        d = data[name]
        m = len(d['rows'])
        D = [diamond(m, i) for i in range(1, m + 1)]
        assert all(is_totally_even(m, m, B) for B in D)
        # each B(i) meets the lower side exactly in the edge below cell column i-1
        for i, B in enumerate(D, 1):
            assert {e for e in B if e[0] == 'h' and e[1] == m} == {('h', m, i - 1)}
        sols = [frozenset(tuple(e) for e in s) for s in d['solutions']]
        print(f'== {name}')
        for b, base in enumerate(sols):
            decs = [decompose(base ^ s, D) for s in sols]
            print(f'  base = solution {b + 1}: differences = {{' + ', '.join(fmt(x) for x in decs) + '}')
