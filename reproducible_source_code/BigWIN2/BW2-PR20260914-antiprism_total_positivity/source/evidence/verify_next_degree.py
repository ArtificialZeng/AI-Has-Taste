#!/usr/bin/env python3
"""Independent exact extraction from the defining determinant.

Uses a Stirling recurrence for the two needed T coefficients, followed by
integer Bareiss determinants. Does not import the producer or use A^-1 E,
the Vandermonde differentiation matrix, or the normalized family formula.
This checks arithmetic in the same research context, not a fresh referee.
"""
from fractions import Fraction
from math import comb, factorial, lcm, prod
from pathlib import Path
import hashlib
import json
import time

JOB = 'primary-20260914-antiprism-total-positivity-research-dee875af8862'


def determinant(matrix):
    a = [list(row) for row in matrix]
    size = len(a)
    previous, sign = 1, 1
    for p in range(size-1):
        if a[p][p] == 0:
            swap = next((q for q in range(p+1, size) if a[q][p]), None)
            if swap is None:
                return 0
            a[p], a[swap] = a[swap], a[p]
            sign = -sign
        pivot = a[p][p]
        for i in range(p+1, size):
            for j in range(p+1, size):
                num = a[i][j]*pivot-a[i][p]*a[p][j]
                assert num % previous == 0
                a[i][j] = num//previous
        previous = pivot
    return sign*a[-1][-1]


def coefficient(k, m):
    # [x^r]T_(r,l)=(-1)^(r-l)*l!*S(r,l)/r!.
    # [x^(r-1)y]T_(r,l) follows by differentiating the generating
    # expression exp(-t*y)*(1-exp(-t*(x+y)))^l at y=0.
    stir = [[0]*(k+1) for _ in range(k+1)]
    stir[0][0] = 1
    for r in range(1, k+1):
        for ell in range(1, r+1):
            stir[r][ell] = stir[r-1][ell-1]+ell*stir[r-1][ell]
    lead, sub = [], []
    scale = 1
    for r in range(1, k+1):
        row_l, row_n = [], []
        for s in range(1-k, 1):
            vl, vn = Fraction(0), Fraction(0)
            for ell in (range(1, r+1) if r <= m else [r]):
                tx = Fraction((-1)**(r-ell)*factorial(ell)*stir[r][ell],
                              factorial(r))
                txy = r*tx - Fraction((-1 if (r-1-ell) % 2 else 1)*factorial(ell)
                                     *stir[r-1][ell], factorial(r-1))
                base = ell**k*Fraction(ell, ell+1)**s
                vl += base*tx/ell**r
                vn += base*(tx*Fraction(r*(k+s)-comb(r, 2), ell**r)
                            -txy*Fraction(s, ell**(r-1)*(ell+1)))
            row_l.append(vl)
            row_n.append(vn)
        den = lcm(*(c.denominator for c in row_l+row_n))
        lead.append([int(c*den) for c in row_l])
        sub.append([int(c*den) for c in row_n])
        scale *= den
    top = Fraction(determinant(lead), scale)
    terms = []
    for r in range(k):
        replaced = [row[:] for row in lead]
        replaced[r] = sub[r]
        terms.append(determinant(replaced))
    return top, Fraction(sum(terms), scale), terms, scale


def verify_quartic():
    # A self-contained exact verification of the finite table in the proof.
    table = [
        [Fraction(1, 2)],
        [Fraction(1), Fraction(2, 3)],
        [Fraction(9, 8), Fraction(9, 8), Fraction(3, 4)],
        [Fraction(4, 3), Fraction(8, 9), Fraction(32, 27), Fraction(4, 5)],
        [Fraction(625, 432), Fraction(3125, 3456), Fraction(3125, 3888),
         Fraction(625, 512), Fraction(5, 6)]
    ]
    st = [[0]*6 for _ in range(6)]
    st[0][0] = 1
    for r in range(1, 6):
        for ell in range(1, r+1):
            st[r][ell] = st[r-1][ell-1]+ell*st[r-1][ell]
    for r in range(1, 6):
        for ell in range(1, r+1):
            lhs = sum(Fraction((-1)**(r-j)*factorial(j)*st[r][j],
                               factorial(r)*j**r)*table[j-1][ell-1]
                      for j in range(ell, r+1))
            rhs = Fraction((-1)**(r-ell)*factorial(ell-1)*st[r-1][ell-1],
                           (ell+1)*factorial(r-1)*ell**(r-1))
            assert lhs == rhs
    # Coefficients in ascending powers of the formal indeterminate k.
    poly = [Fraction(0), Fraction(1, 6), Fraction(1, 2), Fraction(1, 3), Fraction(0)]
    for i in range(2, 6):
        for ell in range(1, i):
            term = [Fraction(1)]
            for h in range(i-ell):
                nxt = [Fraction(0)]*(len(term)+1)
                for j, val in enumerate(term):
                    nxt[j] -= (ell+h)*val
                    nxt[j+1] += val
                term = nxt
            prefactor = Fraction((-1)**(i-ell+1)*ell*(ell+1),
                                 (i-ell)*comb(i, i-ell)*factorial(i-ell))*table[i-1][ell-1]
            for j, val in enumerate(term):
                poly[j] += prefactor*val
    expected = [Fraction(-858264, 20736), Fraction(346478, 20736),
                Fraction(-17736, 20736), Fraction(9555, 20736), Fraction(-125, 20736)]
    assert poly == expected
    negative_poly = [-20736*c for c in poly]
    shifted = [sum(negative_poly[j]*comb(j, h)*76**(j-h)
                   for j in range(h, 5)) for h in range(5)]
    assert shifted == [52825392, 56268354, 2171196, 28445, 125]
    assert all(c > 0 for c in shifted)
    return {'table_identity_A_times_F_equals_E': True,
            'S_k_5_coefficients_ascending': [str(c) for c in poly],
            'minus_20736_S_at_76_plus_t_coefficients_ascending': [str(c) for c in shifted],
            'interpretation': 'Exact polynomial identities; positivity of the shifted polynomial proves negativity for every integer k>=76.'}


def main():
    start = time.monotonic()
    source = Path('evidence/research_next_degree.json')
    data = json.loads(source.read_text())
    quartic = verify_quartic()
    checks = []
    # The smaller positive cases check signs and monomial selection against
    # complete certificates from the previous pass.
    for k, m in [(5, 5), (6, 3), (6, 6), (22, 9), (25, 7)]:
        top, value, numerators, denominator = coefficient(k, m)
        scalar = Fraction(prod(factorial(r) for r in range(1, k+1)),
                          prod(ell**ell for ell in range(1, k+1)))
        assert top == scalar
        if k <= 6:
            prior = json.loads(Path(f'evidence/research_flag_order_{k}.json').read_text())
            mon = [k*(k+1)//2-1, 0, m]+[0]*(m-1)+[1]*(k-m)
            expected = next(Fraction(c) for powers, c in prior['coefficients'] if powers == mon)
        else:
            expected = Fraction(next(w['exact_coefficient'] for w in data['witnesses']
                                     if w['k'] == k and w['m'] == m))
            assert value < 0
        assert value == expected
        checks.append({'k': k, 'm': m, 'leading_coefficient': str(top),
                       'next_coefficient': str(value),
                       'normalized_next_coefficient': str(value/top),
                       'cleared_denominator': str(denominator),
                       'row_replacement_determinants': [str(v) for v in numerators],
                       'agrees_with_certificate': True})
        print('verified', k, m, str(value/top), flush=True)
    result = {'proposer_job_id': JOB,
              'producer_certificate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'arithmetic': 'standard-library Fraction; row denominators cleared; integer Bareiss',
              'checks': checks,
              'uniform_quartic_check': quartic,
              'elapsed_seconds': time.monotonic()-start,
              'scope': 'exact coefficients from the defining determinant; same-context arithmetic check, not a fresh referee'}
    dest = Path('evidence/verify_next_degree.json')
    temp = dest.with_suffix('.json.tmp')
    temp.write_text(json.dumps(result, indent=2)+'\n')
    temp.replace(dest)


if __name__ == '__main__':
    main()
