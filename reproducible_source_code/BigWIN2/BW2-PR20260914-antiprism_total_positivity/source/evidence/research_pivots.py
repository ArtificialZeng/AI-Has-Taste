#!/usr/bin/env python3
"""Exact checks for research-pivots.md; run from the project root.

Finite verification supplements the proof; no infinite sign is inferred from
the tested dimensions. Python 3 and SymPy are used without floating point.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time
import sympy as sp
import triage_exact as prior

JOB = 'primary-20260914-antiprism-total-positivity-research-7e4c6a3e5254'


def delta_formula(d, j):
    if j == 1:
        return d*(d-1)*((d+1)*(F(2)**(d-2)-2)*F(3)**(d-3)
                       + F(2)**(2*d-5) + d*F(2)**(d-4))
    t, n = d+j, d-j
    return (F(2)**(d-4)*F(3)**(n-2)
            *((t+2*d-2)*t*(t-1)+d*(d+1)*(t-4))
            + F(2)**(2*n-3)*(t*(t-1)-2*d))


def low_rows(d, j):
    n = d-j
    h1 = (d+j)*F(2)**(n-1)-d*(j == 0)
    h2 = (F(2)**(j-2)*F(3)**(n-2)*((2*d+j)**2-4*d-5*j)
          + F(2)**(n-3)*((d+j)**2-(d+3*j)-4*(d-1)*(d+j))
          + comb(d, 2)*(j == 0))
    return h1, h2


def face_rows(d):
    """Only the first two rows, independently via the source's B Q B^-1.

    q_1(r)=r and q_2(r)=C(r,2)*(2^(r-1)+1) for r>=2.
    Their invalid lower-index cases are set to zero explicitly.
    """
    out = []
    for j in range(d+1):
        t1 = sum(r*comb(d-j, r-j) for r in range(j, d+1))
        t2 = sum(comb(r, 2)*(2**(r-1)+1)*comb(d-j, r-j)
                 for r in range(max(2, j), d+1))
        out.append((t1-d*(j == 0),
                    t2-(d-1)*t1+comb(d, 2)*(j == 0)))
    return out


def save(out):
    path = Path('evidence/research_pivots.json')
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2)+'\n')
    tmp.replace(path)


def main():
    started = time.monotonic()
    out = {'job_id': JOB,
           'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
           'arithmetic': 'exact integers, rational fractions and SymPy identities',
           'direct_definition_checks': [], 'independent_face_row_checks': [],
           'symbolic_checks': {}, 'boundary_examples': {}}

    # Exact expansion of the bivariate exponential generating function.
    x, y, z, c = sp.symbols('x y z c')
    w = x+y
    expansion = sp.series(sp.exp(z*x)/(1-(sp.exp(z*w)-1)*(c-1)), z, 0, 3).removeO()
    assert sp.expand(expansion.coeff(z, 1)-(w*c-y)) == 0
    assert sp.expand(expansion.coeff(z, 2)-(w*w*c*c-w*(x+3*y)*c/2+y*y/2)) == 0
    out['symbolic_checks']['egf_coefficients_through_row_2'] = True

    d, j, e = sp.symbols('d j e')
    def ratio(k, ek):
        return ek*(3*d+k-5+d*(d+1)/(d+k))/18+(k-3*d+1+2*d/(d+k))/4
    t = d+j
    diff = e*(t+2*d-2+d*(d+1)*(t-4)/(t*(t-1)))/54+(1-2*d/(t*(t-1)))/4
    assert sp.factor(ratio(j, 4*e/3)-ratio(j-1, e)-diff) == 0
    out['symbolic_checks']['ratio_difference_identity'] = True

    for dim in range(3, 17):
        h = prior.direct(dim)
        assert h == prior.from_faces(dim)
        for col in range(dim+1):
            assert low_rows(dim, col) == (h[1][col], h[2][col])
        deltas = []
        for col in range(1, dim+1):
            exact = h[1][col-1]*h[2][col]-h[1][col]*h[2][col-1]
            assert exact == delta_formula(dim, col) and exact > 0
            deltas.append(str(exact))
        for a, b in combinations(range(dim+1), 2):
            assert h[1][a]*h[2][b]-h[1][b]*h[2][a] > 0
            assert h[dim-2][a]*h[dim-1][b]-h[dim-2][b]*h[dim-1][a] > 0
        out['direct_definition_checks'].append(
            {'d': dim, 'both_low_rows_match': True, 'deltas': deltas,
             'all_column_pair_checks_per_row_pair': comb(dim+1, 2),
             'reflected_pair_also_checked': True})
        save(out)

    # Held-out dimensions use an integer face-vector sum, not the formula
    # delta_formula itself. This is a finite computational check, not a referee.
    for dim in list(range(17, 65))+[96, 128, 192, 256]:
        rows = face_rows(dim)
        for col, row in enumerate(rows):
            assert low_rows(dim, col) == row
        for col in range(1, dim+1):
            a, b = rows[col-1], rows[col]
            exact = a[0]*b[1]-b[0]*a[1]
            assert exact == delta_formula(dim, col) and exact > 0
        out['independent_face_row_checks'].append({'d': dim, 'all_columns': True,
                                                  'all_adjacent_minors': True})
        save(out)

    for dim in (3, 4, 16, 64, 256):
        out['boundary_examples'][str(dim)] = {
            str(col): str(delta_formula(dim, col)) for col in (1, 2, dim)}

    # Test a concrete neighboring route: factoring through the known
    # barycentric transform cannot leave a TN residual even in d=3.
    dim = 3
    b = sp.Matrix([[(-1)**(i-k)*prior.C(dim-k, dim-i) if k <= i else 0
                    for k in range(dim+1)] for i in range(dim+1)])
    r = sp.Matrix([[factorial(i)*prior.S[k][i] for k in range(dim+1)]
                    for i in range(dim+1)])
    hb = b*r*b.inv()
    ha = sp.Matrix(prior.direct(dim))
    left, right = hb.inv()*ha, ha*hb.inv()
    assert left[1, 3] == right[1, 3] == -sp.Rational(1, 6)
    assert hb*left == ha and right*hb == ha
    out['barycentric_residual_counterexample'] = {
        'd': dim, 'barycentric_H': [list(map(str, hb.row(i))) for i in range(dim+1)],
        'antiprism_H': [list(map(str, ha.row(i))) for i in range(dim+1)],
        'left_residual': [list(map(str, left.row(i))) for i in range(dim+1)],
        'right_residual': [list(map(str, right.row(i))) for i in range(dim+1)],
        'negative_entry': {'row': 1, 'column': 3, 'value': '-1/6'},
        'both_factor_identities_exact': True,
        'scope': 'only a single unmodified barycentric factor on either side'}
    out['elapsed_seconds'] = round(time.monotonic()-started, 3)
    save(out)
    print(json.dumps({'direct_d': [3, 16], 'face_d': [17, 64, 96, 128, 192, 256],
                      'symbolic_checks': out['symbolic_checks'],
                      'negative_barycentric_residual_entry': '-1/6',
                      'elapsed_seconds': out['elapsed_seconds']}))


if __name__ == '__main__':
    main()
