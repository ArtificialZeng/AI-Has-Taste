#!/usr/bin/env python3
"""Standard-library verification of the third-flag polynomial certificate.

Exact interpolation: both polynomials have separate degree bounds
(6,6,3,2,1) in (a,n,u,v,w). Their equality on the full product grid of
sizes (7,7,4,3,2) therefore proves their polynomial identity. This is a
separate arithmetic implementation, not a fresh mathematical referee.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

# Coefficients of x^p y^q multiplying exp(ell*x+(ell+1)*y) in [z^r]G.
# The ell=0 terms vanish in all columns used here, which have j>=1.
ROW = {
    (1, 1): [(1, 0, F(1)), (0, 1, F(1))],
    (2, 1): [(2, 0, F(-1, 2)), (1, 1, F(-2)), (0, 2, F(-3, 2))],
    (2, 2): [(2, 0, F(1)), (1, 1, F(2)), (0, 2, F(1))],
    (3, 1): [(3, 0, F(1, 6)), (2, 1, F(1)), (1, 2, F(2)), (0, 3, F(7, 6))],
    (3, 2): [(3, 0, F(-1)), (2, 1, F(-4)), (1, 2, F(-5)), (0, 3, F(-2))],
    (3, 3): [(3, 0, F(1)), (2, 1, F(3)), (1, 2, F(3)), (0, 3, F(1))],
}


def fall(v, k):
    ans = 1
    for i in range(k):
        ans *= v-i
    return ans


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def polynomial(rows):
    out = {tuple(m): F(c) for m, c in rows}
    assert len(out) == len(rows)
    assert all(0 <= a <= 6 and 0 <= n <= 6 for a, n in out)
    return out


def main():
    path = Path('evidence/research_third_flag.json')
    data = json.loads(path.read_text())
    groups = {tuple(g['base_powers_u_v_w']): polynomial(g['coefficients'])
              for g in data['groups']}
    assert set(groups) == {(3, 0, 0), (2, 1, 0), (2, 0, 1), (1, 2, 0), (1, 1, 1)}
    assert all(p <= 3 and q <= 2 and r <= 1 for p, q, r in groups)
    checks = 0
    for av, nv in product(range(7), repeat=2):
        matrix_coeff = []
        for row in range(1, 4):
            entries = []
            for shift in (-2, -1, 0):
                entries.append({ell: F(ell, ell+1)**shift
                                *sum(c*fall(av+3+shift, px)*fall(nv-shift, py)
                                     /ell**px/(ell+1)**py for px, py, c in ROW[row, ell])
                                for ell in range(1, row+1)})
            matrix_coeff.append(entries)
        group_values = {p: sum(c*av**m[0]*nv**m[1] for m, c in poly.items())
                        for p, poly in groups.items()}
        for uv, vv, wv in product(range(4), range(3), range(2)):
            bases = {1: uv, 2: vv, 3: wv}
            matrix = [[sum(bases[ell]*c for ell, c in entry.items())
                       for entry in row] for row in matrix_coeff]
            rhs = sum(value*uv**p*vv**q*wv**r for (p, q, r), value in group_values.items())
            assert det3(matrix) == rhs
            checks += 1
    assert checks == 7*7*4*3*2
    positive = data['positive_coefficient_certificate']
    for p in ((3, 0, 0), (2, 0, 1), (1, 2, 0), (1, 1, 1)):
        assert polynomial(positive[str(p)]['coefficients']) == groups[p]
    repair = polynomial(positive['repair_P210_plus_2P120']['coefficients'])
    keys = groups[2, 1, 0].keys() | groups[1, 2, 0].keys()
    expected = {key: groups[2, 1, 0].get(key, F(0))+2*groups[1, 2, 0].get(key, F(0))
                for key in keys}
    expected = {key: value for key, value in expected.items() if value}
    assert repair == expected
    for c in positive.values():
        poly = polynomial(c['coefficients'])
        assert all(v > 0 for v in poly.values()) and poly[0, 0] > 0
    result = {'job_id': data['job_id'], 'arithmetic': 'standard-library Fraction',
              'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'separate_degree_bounds_a_n_u_v_w': [6, 6, 3, 2, 1],
              'grid_sizes': [7, 7, 4, 3, 2], 'grid_points_checked': checks,
              'polynomial_identity_by_exact_interpolation': True,
              'coefficient_repair_identity': True,
              'all_five_repaired_groups_have_positive_coefficients_and_constant': True,
              'review_scope': 'independent arithmetic implementation, same research context'}
    dest = Path('evidence/verify_third_flag.json')
    tmp = dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(result, indent=2)+'\n')
    tmp.replace(dest)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
