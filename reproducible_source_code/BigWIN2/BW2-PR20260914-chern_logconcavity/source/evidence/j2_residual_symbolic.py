#!/usr/bin/env python3
"""Symbolic Abel certificate search for the lower-mode recurrence residual.

All expressions use exact SymPy polynomials. Coefficients p_i represent
twice the Newton coefficient, so each quadratic prefix is divided by 4.
"""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
k, r, X, Y = s.symbols('k r X Y')


def add(*terms):
    out = defaultdict(lambda: s.S.Zero)
    for weight, shift, data in terms:
        for i, c in data.items():
            out[i + shift] += weight * c
    return {i: s.expand(c) for i, c in out.items() if s.expand(c) != 0}


@lru_cache(None)
def reduced(offset, depth):
    if depth == 0:
        return {offset: s.S.One}
    return add((r + offset - 1, 0, reduced(offset - 1, depth - 1)),
               (r + offset - 1, 0, reduced(offset - 2, depth - 1)))


@lru_cache(None)
def times(factors, offset, depth):
    if not factors:
        return add((1, 0, reduced(offset, depth)),
                   (1, 0, reduced(offset + 1, depth)))
    return add((r + offset + factors[-1], 0, times(factors[:-1], offset, depth)),
               (r + offset, 0, times(factors[:-1], offset - 1, depth)))


def j2(drop):
    return add((k * (k + 1), 0, times((), 0, drop)),
               (-2 * k, 0, times((0, 2 - k), 0, drop - 1)),
               (1, 0, times((0, 0, 3 - k, 2 - k), 0, drop - 2)))


def substitute(data, dk=0, dr=0):
    return {i: s.expand(c.subs({k: k + dk, r: r + dr}, simultaneous=True))
            for i, c in data.items()}


def multiply(a, b):
    out = defaultdict(lambda: s.S.Zero)
    for i, x in a.items():
        for j, y in b.items():
            out[tuple(sorted((i, j)))] += x * y
    return out


def minor(data):
    center = multiply(data, data)
    left = add((1, -1, substitute(data, dr=-1)))
    right = add((1, 1, substitute(data, dr=1)))
    adjacent = multiply(left, right)
    return {pair: s.expand(center.get(pair, 0) - adjacent.get(pair, 0))
            for pair in center.keys() | adjacent.keys()}


def main():
    previous = substitute(j2(2), dk=-1)
    g = add((r + 1, 0, previous), (r, -1, substitute(previous, dr=-1)))
    residual = add((1, 1, substitute(j2(3), dr=1)), (-1, 0, g))

    # Cross-check against a direct expansion of the four lower-mode terms.
    # j1 = d(d+2-n)S_{n-1} - (n+1)S_n.
    direct = add(
        (2, 0, times((2-k, 0, 3-k), 0, 1)),
        (-2*k, 0, times((2-k,), 0, 2)),
        (1, 0, times((3-k, 2-k), 0, 1)),
        (2, 0, times((1, 3-k, 0, 4-k), 0, 0)),
        (-2*(k-1), 0, times((1, 3-k), 0, 1)),
        (1, 0, times((1, 4-k, 3-k), 0, 0)),
    )
    assert not add((1, 0, residual), (-1, 0, direct))
    q = minor(residual)
    groups = defaultdict(list)
    for pair, c in q.items():
        if c != 0:
            groups[sum(pair)].append(pair)
    prefixes = []
    for trace, pairs in sorted(groups.items()):
        pairs.sort(key=lambda z: z[1] - z[0])
        w = s.S.Zero
        for a, b in pairs:
            w = s.expand(w + q[a, b])
            expr = s.Poly(w.subs({k: X + Y + b - a + 4,
                                 r: 2*X + Y + b - 2*a + 2}, simultaneous=True) / 4, X, Y)
            bad = [{'monomial': list(m), 'coefficient': str(c)}
                   for m, c in expr.terms() if c < 0]
            prefixes.append({'trace': trace, 'pair': [a, b],
                             'prefix_kr': str(w / 4),
                             'support_substitution': {'k': str(X+Y+b-a+4), 'r': str(2*X+Y+b-2*a+2)},
                             'terms': [{'monomial': list(m), 'coefficient': str(c)} for m, c in expr.terms()],
                             'negative_coefficients': bad})
    report = {'job_id': 'primary-20260914-chern-logconcavity-research-5a27c3ef60f2',
              'kind': 'exact symbolic sufficient-certificate test for an auxiliary sequence',
              'scope': 'R_k = Delta A_{k,2} - (x+1)A_{k-1,2}, common defect k-3',
              'independent_symbolic_residual_identity': True,
              'twice_residual_expansion': {str(i): str(c) for i, c in sorted(residual.items())},
              'prefix_count': len(prefixes),
              'prefixes_with_negative_coefficients': sum(bool(p['negative_coefficients']) for p in prefixes),
              'prefixes': prefixes}
    (ROOT / 'j2-residual-symbolic.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'prefixes'}, indent=2))


if __name__ == '__main__':
    main()
