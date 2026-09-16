#!/usr/bin/env python3
"""Exact next-degree coefficient family from the triangular trace formula.

No floating point arithmetic. This is the producer, not a fresh referee.
Run from the project root: python3 evidence/research_next_degree.py
"""
from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json

JOB = 'primary-20260914-antiprism-total-positivity-research-dee875af8862'


def triangular_derivative(size):
    a, e, f = {}, {}, {}
    for r in range(1, size + 1):
        for ell in range(1, r + 1):
            a[r, ell] = sum(
                ((-1)**(r+h)*comb(ell, h)*Q(h, ell)**r
                 for h in range(ell + 1)), Q(0))/factorial(r)
            e[r, ell] = sum(
                ((-1)**(r+h)*comb(ell, h)*r*Q(h, ell)**(r-1)
                 * (Q(h, ell)-Q(h+1, ell+1))
                 for h in range(ell + 1)), Q(0))/factorial(r)
    for r in range(1, size + 1):
        for ell in range(1, r + 1):
            f[r, ell] = (e[r, ell]-sum(a[r, j]*f[j, ell]
                                      for j in range(ell, r)))/a[r, r]
    return f


def normalized(k, m, f):
    return Q(k*(k+1)*(2*k+1), 6) + sum(
        ((-1)**(i-ell+1)
         * Q(ell*(ell+1)*comb(k-ell, i-ell),
             (i-ell)*comb(i, i-ell))*f[i, ell]
         for i in range(2, m+1) for ell in range(1, i)), Q(0))


def scalar(k):
    return Q(prod(factorial(r) for r in range(1, k+1)),
             prod(ell**ell for ell in range(1, k+1)))


def main():
    f = triangular_derivative(32)
    search = []
    for k in range(2, 33):
        vals = [(m, normalized(k, m, f)) for m in range(1, k+1)]
        negatives = [(m, str(v)) for m, v in vals if v < 0]
        search.append({'k': k, 'm_tested': [1, k],
                       'negative_m_and_normalized_values': negatives})
    witnesses = []
    for k, m in [(22, 9), (25, 7), (76, 5)]:
        value = normalized(k, m, f)
        assert value < 0
        powers = [k*(k+1)//2-1, 0, m]+[0]*(m-1)+[1]*(k-m)
        assert len(powers) == k+2 and sum(powers[2:]) == k
        witnesses.append({'k': k, 'm': m, 'monomial_powers_a_n_z': powers,
                          'positive_normalizing_scalar': str(scalar(k)),
                          'normalized_coefficient': str(value),
                          'exact_coefficient': str(scalar(k)*value)})
    # This finite cross-check does not prove the symbolic quartic identity;
    # the accompanying proof derives it from the displayed 5 by 5 table.
    for k in range(5, 101):
        quartic = -Q(125*k**4-9555*k**3+17736*k**2-346478*k+858264,
                     20736)
        assert normalized(k, 5, f) == quartic
    out = {
        'proposer_job_id': JOB,
        'scope': 'coefficients of the frozen auxiliary R_k only; original TN unresolved',
        'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        'arithmetic': 'standard-library integers and Fraction',
        'F_i_l_at_a1_n0_through_9': [
            {'i': i, 'l': ell, 'value': str(f[i, ell])}
            for i in range(1, 10) for ell in range(1, i+1)],
        'targeted_search': search,
        'search_limit': 'Only a^(K-1)*z1^m*z_(m+1)*...*z_k, 2<=k<=32, 1<=m<=k. No minimality claim among all coefficients.',
        'witnesses': witnesses,
        'm5_symbolic_formula': '-(125*k^4-9555*k^3+17736*k^2-346478*k+858264)/20736',
        'm5_finite_formula_checks_k': [5, 100],
        'scope_of_verification': 'Producer calculation in the research context; direct determinant verifier is separate.'
    }
    dest = Path('evidence/research_next_degree.json')
    temp = dest.with_suffix('.json.tmp')
    temp.write_text(json.dumps(out, indent=2)+'\n')
    temp.replace(dest)
    print(json.dumps({'witnesses': [{key: w[key] for key in
        ['k', 'm', 'normalized_coefficient']} for w in witnesses],
        'targeted_search_first_negative_k': next(r['k'] for r in search
            if r['negative_m_and_normalized_values'])}))


if __name__ == '__main__':
    main()
