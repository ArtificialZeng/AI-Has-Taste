#!/usr/bin/env python3
"""Independent exact verifier using FLINT characteristic polynomials/Sturm.

This deliberately does not import the discovery census implementation.
It parses graph6 independently, forms M=Q-2I over Z, computes its integer
characteristic polynomial, square-free factors it, and applies Sturm's theorem
to every factor with its multiplicity.
"""

import argparse, hashlib, json, platform
from collections import Counter
from flint import fmpq_poly, fmpz_mat


def parse(raw):
    s = raw.strip(); n = s[0] - 63
    bits = [(ch - 63 >> shift) & 1 for ch in s[1:] for shift in range(5, -1, -1)]
    edges = []; k = 0
    for high in range(1, n):
        for low in range(high):
            if bits[k]: edges.append((low, high))
            k += 1
    return s.decode(), n, edges


def variations(signs):
    signs = [x for x in signs if x]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sign_at(poly, where):
    if where == 0:
        v = poly[0]
    else:
        v = poly.leading_coefficient()
        if where < 0 and poly.degree() % 2: v = -v
    return (v > 0) - (v < 0)


def sturm_distinct(poly, side):
    p = fmpq_poly(poly); seq = [p, p.derivative()]
    while seq[-1]:
        rem = divmod(seq[-2], seq[-1])[1]
        if not rem: break
        seq.append(-rem)
    at_zero = variations([sign_at(p, 0) for p in seq])
    at_inf = variations([sign_at(p, side) for p in seq])
    return (at_zero - at_inf) if side > 0 else (at_inf - at_zero)


def inertia_charpoly(mat):
    poly = fmpz_mat(mat).charpoly()
    positive = negative = zero = 0
    _, factors = poly.factor_squarefree()
    for factor, multiplicity in factors:
        if factor.degree() == 1 and factor[0] == 0:
            zero += multiplicity
        else:
            positive += multiplicity * sturm_distinct(factor, 1)
            negative += multiplicity * sturm_distinct(factor, -1)
    if positive + zero + negative != len(mat):
        raise AssertionError((poly, positive, zero, negative))
    return positive, zero, negative, str(poly)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--input', required=True)
    ap.add_argument('--census', required=True); ap.add_argument('--log', required=True)
    a = ap.parse_args(); expected = json.load(open(a.census, encoding='utf-8'))
    digest = hashlib.sha256(); totals = Counter(); count = 0; equality = []
    for raw in open(a.input, 'rb'):
        if not raw.strip() or raw.startswith(b'>>'): continue
        digest.update(raw); g6, n, edges = parse(raw); count += 1
        mat = [[0] * n for _ in range(n)]; deg = [0] * n
        for u, v in edges:
            mat[u][v] = mat[v][u] = 1; deg[u] += 1; deg[v] += 1
        for i in range(n): mat[i][i] = deg[i] - 2
        p, z, q, charpoly = inertia_charpoly(mat)
        m = len(edges); c = m - n + 1; sig = p - q - c + 1
        slack = c + 1 - 2 * sig
        totals['violation' if slack < 0 else 'equality' if slack == 0 else 'strict'] += 1
        if slack == 0:
            equality.append({'graph6': g6, 'm': m, 'c': c,
                             'inertia_Q_minus_2': [p,z,q],
                             'line_graph_signature': sig,
                             'charpoly_Q_minus_2': charpoly})
    checks = {
      'input_sha256_matches': digest.hexdigest() == expected['input_sha256'],
      'graph_count_matches': count == expected['graph_count'],
      'totals_match': dict(totals) == expected['totals'],
      'no_violations': totals['violation'] == 0,
    }
    out = {'verifier': 'python-flint charpoly + square-free factorization + Sturm',
           'python': platform.python_version(), 'flint': __import__('flint').__version__,
           'checks': checks, 'graph_count': count, 'totals': dict(totals),
           'input_sha256': digest.hexdigest(), 'equality_certificates': equality}
    with open(a.log, 'w', encoding='utf-8') as f: json.dump(out, f, indent=2, sort_keys=True); f.write('\n')
    if not all(checks.values()): raise SystemExit('FAIL ' + json.dumps(checks))
    print('PASS ' + json.dumps({'graph_count':count, 'totals':dict(totals), 'equality':len(equality)}))


if __name__ == '__main__': main()
