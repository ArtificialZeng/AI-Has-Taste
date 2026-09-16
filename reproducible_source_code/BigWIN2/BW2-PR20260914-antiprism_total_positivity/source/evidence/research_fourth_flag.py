#!/usr/bin/env python3
"""Exact expansion of the fourth antiprism flag; run from project root."""
import json
import time
from itertools import permutations
from pathlib import Path
import sympy as S
from sympy.functions.combinatorial.numbers import stirling

JOB = 'primary-20260914-antiprism-total-positivity-research-1f8d7876bdf3'
x, y, a, n, c = S.symbols('x y a n c')
b = S.symbols('u v w t')


def falling(z, k):
    return S.prod(z-i for i in range(k))


def row_polys(r):
    # [z^r] exp(z*x)/(1-(exp(z*(x+y))-1)*(c-1)).
    row = S.expand(sum(x**s/S.factorial(s) * (x+y)**(r-s)/S.factorial(r-s)
                       * sum(S.factorial(m)*stirling(r-s, m, kind=2)*(c-1)**m
                             for m in range(r-s+1)) for s in range(r+1)))
    return {ell: S.Poly(row.coeff(c, ell), x, y) for ell in range(r+1)}


def entry(r, shift, polys):
    return S.Poly(sum(b[ell-1]*S.Rational(ell, ell+1)**shift
                      * sum(coef*falling(a+4+shift, px)*falling(n-shift, py)
                            /S.Integer(ell)**px/S.Integer(ell+1)**py
                            for (px, py), coef in polys[r][ell].terms())
                      for ell in range(1, r+1)), a, n, *b)


def serialize(poly):
    return [[list(m), str(coef)] for m, coef in poly.terms()]


def save(data):
    dest = Path('evidence/research_fourth_flag.json')
    tmp = dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(dest)


def main():
    start = time.monotonic()
    polys = {r: row_polys(r) for r in range(1, 5)}
    for r in polys:
        assert polys[r][0].as_expr() == (-y)**r/S.factorial(r)
    print('row polynomials ready', flush=True)
    matrix = [[entry(r, shift, polys) for shift in (-3, -2, -1, 0)] for r in range(1, 5)]
    # Fraction-free polynomial products avoid rational-function simplification.
    det = S.Poly(0, a, n, *b)
    for perm in permutations(range(4)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        term = S.Poly(sign, a, n, *b)
        for i in range(4):
            term *= matrix[i][perm[i]]
        det += term
    print('determinant expanded', len(det.terms()), round(time.monotonic()-start, 2), flush=True)
    groups = S.Poly(det.as_expr(), *b)
    data = {'job_id': JOB, 'scope': 'det H_d[{1,2,3,4},{j-3,j-2,j-1,j}], d>=5, 4<=j<=d',
            'variables': {'a':'j-4', 'n':'d-j', 'b_l':'l^j*(l+1)^n, l=1,2,3,4'},
            'row_polynomials': {str(r): {str(ell): serialize(poly) for ell, poly in p.items()}
                                for r, p in polys.items()},
            'groups': [], 'certificate_status': 'expansion only, no sign conclusion yet'}
    for powers, expr in groups.terms():
        poly = S.Poly(expr, a, n)
        pos = sum(bool(coef > 0) for coef in poly.coeffs())
        neg = sum(bool(coef < 0) for coef in poly.coeffs())
        data['groups'].append({'powers': list(powers), 'coefficients': serialize(poly),
                               'positive_coefficients': int(pos), 'negative_coefficients': int(neg),
                               'constant': str(poly.eval({a:0,n:0}))})
        print(powers, 'degree', poly.total_degree(), 'pos', pos, 'neg', neg,
              'constant', poly.eval({a:0,n:0}), flush=True)
    V, W, T = S.symbols('V W T')
    transformed = S.Poly(S.expand(det.as_expr().subs(b[3], S.Rational(256,81)*b[2]+T)
                                  .subs(b[2], S.Rational(81,16)*b[1]+W)
                                  .subs(b[1], 16*b[0]+V)), a, n, b[0], V, W, T)
    assert all(coef > 0 for coef in transformed.coeffs())
    assert transformed.coeff_monomial(b[0]**4) > 0
    data['ratio_substitution'] = {
        'variables':['a','n','u','V','W','T'],
        'relations':['v=16u+V','w=81v/16+W','t=256w/81+T'],
        'coefficients':serialize(transformed),
        'coefficient_count':len(transformed.terms()),
        'all_listed_coefficients_positive':True,
        'u_fourth_coefficient':str(transformed.coeff_monomial(b[0]**4)),
    }
    data['certificate_status'] = 'exact positive coefficient certificate; independent verification separate'
    data['elapsed_seconds'] = time.monotonic()-start
    save(data)


if __name__ == '__main__':
    main()
