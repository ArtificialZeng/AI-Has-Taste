#!/usr/bin/env python3
"""Exact polynomial certificate for the three-row Neville flag minor.

See research-pivots.md for the infinite-domain argument. The polynomial
identity and sign certificate use exact arithmetic, and are additionally
checked against the original definition and independent face-vector sums.
"""
from fractions import Fraction
from math import comb, factorial
import json
from pathlib import Path
import sympy as s
import triage_exact as prior

x, y, a, n = s.symbols('x y a n')
j = a+3
u, v, w = s.symbols('u v w')
base = {1: u, 2: v, 3: w}
polys = {
    1: {1: x+y},
    2: {1: -(x+y)*(x+3*y)/2, 2: (x+y)**2},
    3: {1: (x+y)*(x*x+5*x*y+7*y*y)/6,
        2: -(x+y)**2*(x+2*y), 3: (x+y)**3},
}


def falling(z, k):
    return s.prod(z-r for r in range(k))


def entry(r, shift):
    ans = 0
    for ell, poly in polys[r].items():
        factor = base[ell]*s.Rational(ell, ell+1)**shift
        ans += factor*sum(c*falling(j+shift, px)*falling(n-shift, py)
                          /s.Integer(ell)**px/s.Integer(ell+1)**py
                          for (px, py), c in s.Poly(poly, x, y).terms())
    return s.expand(ans)


def main():
    z, c = s.symbols('z c')
    egf_row3 = s.series(s.exp(z*x)/(1-(s.exp(z*(x+y))-1)*(c-1)),
                        z, 0, 4).removeO().coeff(z, 3)
    assert s.expand(egf_row3-sum(poly*c**ell for ell, poly in polys[3].items())+y**3/6) == 0
    matrix = s.Matrix([[entry(r, shift) for shift in (-2, -1, 0)] for r in (1, 2, 3)])
    det = s.Poly(s.expand(matrix.det(method='domain-ge')), u, v, w)
    group_polys = dict(det.terms())
    groups = []
    for powers, coeff in det.terms():
        p = s.Poly(coeff, a, n)
        signs = {'positive': 0, 'zero': 0, 'negative': 0}
        for c in p.coeffs():
            signs['positive' if c > 0 else 'negative' if c < 0 else 'zero'] += 1
        groups.append({'base_powers_u_v_w': list(powers),
                       'polynomial_factored': str(s.factor(coeff)),
                       'coefficients': [[list(m), str(c)] for m, c in p.terms()],
                       'monomial_coefficient_signs_in_j_minus_3_and_d_minus_j': signs})
    positive_polys = {str(p): s.Poly(group_polys[p], a, n)
                      for p in ((3, 0, 0), (2, 0, 1), (1, 2, 0), (1, 1, 1))}
    positive_polys['repair_P210_plus_2P120'] = s.Poly(
        group_polys[(2, 1, 0)]+2*group_polys[(1, 2, 0)], a, n)
    certificate = {}
    for label, poly in positive_polys.items():
        assert all(c > 0 for c in poly.coeffs())
        assert poly.eval({a: 0, n: 0}) > 0
        certificate[label] = {'polynomial_factored': str(s.factor(poly.as_expr())),
                              'coefficients': [[list(m), str(c)] for m, c in poly.terms()],
                              'all_listed_coefficients_positive': True,
                              'constant_term_positive': True}
    repaired = (u**3*group_polys[(3, 0, 0)]
                + u**2*w*group_polys[(2, 0, 1)]
                + u*v*w*group_polys[(1, 1, 1)]
                + u**2*v*positive_polys['repair_P210_plus_2P120'].as_expr()
                + u*v*(v-2*u)*group_polys[(1, 2, 0)])
    assert s.expand(det.as_expr()-repaired) == 0
    out = {'job_id': 'primary-20260914-antiprism-total-positivity-research-7e4c6a3e5254',
           'scope': 'det H_d[{1,2,3},{j-2,j-1,j}], d>=4, 3<=j<=d',
           'variables': {'a': 'j-3', 'n': 'd-j',
                         'u': '2^(d-j)', 'v': '2^j 3^(d-j)', 'w': '3^j 4^(d-j)'},
           'egf_third_row_identity_checked': True,
           'groups': groups, 'positive_coefficient_certificate': certificate,
           'repair_identity_checked': True,
           'infinite_sign_argument': 'a,n>=0; u,v,w>0; v/u=2^j*(3/2)^n>=8; all repaired groups positive',
           'direct_definition_checks': [], 'independent_face_checks': []}

    terms = [(powers, s.Poly(coeff, a, n).terms()) for powers, coeff in det.terms()]
    def flag_formula(dim, col):
        av, nv = col-3, dim-col
        bases = (2**nv, 2**col*3**nv, 3**col*4**nv)
        value = Fraction(0)
        for powers, poly_terms in terms:
            pvalue = sum(Fraction(int(c.p), int(c.q))*av**m[0]*nv**m[1]
                         for m, c in poly_terms)
            value += pvalue*int(s.prod(base**power for base, power in zip(bases, powers)))
        assert value.denominator == 1
        return value.numerator

    for dim in range(4, 17):
        h = prior.direct(dim)
        vals = []
        for col in range(3, dim+1):
            exact = prior.determinant([[h[r][c] for c in range(col-2, col+1)]
                                       for r in (1, 2, 3)])
            assert exact == flag_formula(dim, col) and exact > 0
            vals.append(str(exact))
        out['direct_definition_checks'].append({'d': dim, 'flags_j_3_through_d': vals})

    st = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 3, 1]]
    for dim in list(range(17, 33))+[64, 128]:
        rows = [[] for _ in range(4)]
        q = [[(comb(r, k)*sum(factorial(ell)*st[k][ell]*ell**(r-k)
                              for ell in range(k+1))) if r >= k else 0
               for r in range(dim+1)] for k in range(4)]
        for col in range(dim+1):
            face = [sum(q[k][r]*comb(dim-col, r-col) for r in range(col, dim+1))
                    for k in range(4)]
            for r in (1, 2, 3):
                rows[r].append(sum((-1)**(r-k)*comb(dim-k, r-k)*face[k]
                                   for k in range(r+1)))
        for col in range(3, dim+1):
            exact = prior.determinant([[rows[r][c] for c in range(col-2, col+1)]
                                       for r in (1, 2, 3)])
            assert exact == flag_formula(dim, col) and exact > 0
        out['independent_face_checks'].append({'d': dim, 'all_flags_j_3_through_d': True})
    path = Path('evidence/research_third_flag.json')
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({'groups': len(groups), 'positive_repaired_groups': len(certificate),
                      'repair_identity_checked': True, 'direct_d': [4, 16],
                      'independent_face_d': [17, 32, 64, 128]}))


if __name__ == '__main__':
    main()
