#!/usr/bin/env python3
"""Exact checks for the proposed two-step theorem, not an infinite proof.

Run from PROJECT_DIR: python3 evidence/two_step_checks.py
Uses Python integer arithmetic and SymPy only for polynomial identities.
This implementation does not import the earlier triage checker.
"""
import hashlib
import json
from math import comb
from pathlib import Path

import sympy as sp


def plus(p, q):
    return tuple((p[k] if k < len(p) else 0) +
                 (q[k] if k < len(q) else 0)
                 for k in range(max(len(p), len(q))))


def times(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            r[i+j] += pi*qj
    while len(r) > 1 and not r[-1]:
        r.pop()
    return tuple(r)


def mode(p):
    return p.index(max(p))


def support(p):
    nz = [i for i, pi in enumerate(p) if pi]
    assert nz and all(p[i] > 0 for i in range(nz[0], nz[-1]+1))
    return nz[0], nz[-1]


def log_concave(p):
    support(p)
    return all(p[k]*p[k] >= p[k-1]*p[k+1]
               for k in range(1, len(p)-1))


def lr(p, q, full=False):
    """Checks support endpoints and either every or every adjacent minor.

    For interval supports with ordered endpoints, adjacent minors imply
    all minors by multiplying ratios on the common positive support.
    The separate full check tests all minors without using that implication.
    """
    pl, ph = support(p)
    ql, qh = support(q)
    assert pl <= ql and ph <= qh, (p, q)
    size = max(len(p), len(q))
    p = p + (0,)*(size-len(p))
    q = q + (0,)*(size-len(q))
    checked = 0
    if full:
        for i in range(size):
            for j in range(i+1, size):
                assert p[i]*q[j] >= p[j]*q[i], (i, j, p, q)
                checked += 1
    else:
        for i in range(size-1):
            assert p[i]*q[i+1] >= p[i+1]*q[i], (i, p, q)
            checked += 1
    return checked


def direct_f(n, ell):
    """Closed binomial expansion, independently of the recurrence.

    F_n=sum_j binom(n-1-j,j) x^j
        (1+s*x)^(n-1-2j) (1+t*x)^(n-1-j).
    """
    if n == 0:
        return (0,)
    s, t = ell-2, ell-1
    out = [0]*(2*n-1)
    for j in range((n-1)//2+1):
        h, v = n-1-2*j, n-1-j
        count = comb(v, j)
        for u in range(h+1):
            left = count*comb(h, u)*s**u
            for w in range(v+1):
                out[j+u+w] += left*comb(v, w)*t**w
    return tuple(out)


def symbolic_checks():
    x, s, t, y = sp.symbols('x s t y')
    a = (1+s*x)*(1+t*x)
    b = x*(1+t*x)
    ry = 1+(2*s+t+4*y)*x+(s*s+2*s*t)*x*x+s*s*t*x**3
    identities = {
        'factorization': a*a+4*y*b-(1+t*x)*ry,
        'first_cubic_minor': (2*s+t+4*y)**2-(s*s+2*s*t)-
            (3*s*s+2*s*t+t*t+16*s*y+8*t*y+16*y*y),
        'second_cubic_minor': (s*s+2*s*t)**2-(2*s+t+4*y)*s*s*t-
            s*s*(s*s+2*s*t+3*t*t-4*t*y),
        'second_minor_at_y1_uniform':
            (s*s*(s*s+2*s*t+3*t*t-4*t*y)).subs({t:s+1, y:1})-
            s*s*(6*s*s+4*s-1),
        'initial_z1_uniform':
            ((1+t*x)*(a+2*x)).subs(t,s+1)-
            (1+(3*s+4)*x+3*(s+1)**2*x*x+s*(s+1)**2*x**3),
    }
    for name, expr in identities.items():
        assert sp.Poly(sp.expand(expr), x, s, t, y).is_zero, name
    # The y-bound in the proof is linear and decreasing in y.
    derivative = sp.diff(s*s*(s*s+2*s*t+3*t*t-4*t*y), y)
    assert sp.expand(derivative+4*s*s*t) == 0
    return {'sympy_version': sp.__version__,
            'polynomial_identities': list(identities),
            'all_zero_residuals': True,
            'second_minor_y_derivative': str(derivative)}


def main():
    result = {
        'job_id': 'primary-20260914-hypercomb-unimodality-research-c86b16750561',
        'arithmetic': 'arbitrary-precision integers; exact symbolic identities',
        'proof': 'evidence/two-step-mode-proof.md',
        'domains': [
            {'ell': [3,16], 'n': [2,30], 'minor_test': 'all pairs i<j'},
            {'ell_values': [17,31,101,1009,1000003], 'n': [2,80],
             'minor_test': 'adjacent minors plus interval-support endpoints'},
            {'ell_values': [3,4,5], 'n': [31,240],
             'minor_test': 'adjacent minors plus interval-support endpoints'}
        ],
        'polynomials_tested': 0, 'all_pair_minors': 0,
        'adjacent_minors': 0, 'closed_formula_comparisons': 0,
        'mode_difference_range': [None, None],
        'counterexamples': [],
        'symbolic_checks': symbolic_checks(),
    }
    cases = {(ell,n): True for ell in range(3,17) for n in range(2,31)}
    cases.update({(ell,n): False for ell in [17,31,101,1009,1000003]
                  for n in range(2,81)})
    cases.update({(ell,n): False for ell in [3,4,5] for n in range(31,241)})
    digest = hashlib.sha256()
    direct_cases = {(ell,n) for ell in range(3,9) for n in range(1,15)}
    direct_cases.update({(101,31), (1009,24), (1000003,12)})
    all_ells = sorted({ell for ell,n in cases})
    for ell in all_ells:
        upper = max(n for e,n in cases if e == ell)
        s, t = ell-2, ell-1
        a, b = (1,s+t,s*t), (0,1,t)
        z0, z1 = (1,t+1), (1,3*ell-2,3*t*t,s*t*t)
        prev, cur = (0,), (1,)
        cprev, ccur = z0, z1
        if (ell,1) in direct_cases:
            assert direct_f(1,ell) == cur
            result['closed_formula_comparisons'] += 1
        for n in range(2,upper+1):
            new = plus(times(a,cur), times(b,prev))
            cnew = plus(times(a,ccur), times(b,cprev))
            if (ell,n) in direct_cases:
                assert new == direct_f(n,ell)
                result['closed_formula_comparisons'] += 1
            if (ell,n) in cases:
                full = cases[ell,n]
                w, yy = times(z1,new), times(times(z0,b),cur)
                assert cnew == plus(w,yy)
                assert log_concave(cur) and log_concave(new)
                assert log_concave(w) and log_concave(yy)
                assert support(new) == (0,2*n-2)
                assert support(w) == (0,2*n+1)
                assert support(yy) == (1,2*n-1)
                comparisons = [(cur,new), (new,times(b,cur)),
                               (w,(0,0)+yy), (yy,(0,)+w)]
                checked = sum(lr(p,q,full) for p,q in comparisons)
                key = 'all_pair_minors' if full else 'adjacent_minors'
                result[key] += checked
                difference = mode(w)-mode(yy)
                assert -1 <= difference <= 2
                lo,hi = result['mode_difference_range']
                result['mode_difference_range'] = [
                    difference if lo is None else min(lo,difference),
                    difference if hi is None else max(hi,difference)]
                r, q = sorted((mode(w),mode(yy)))
                assert all(cnew[k] <= cnew[k+1] for k in range(r))
                assert all(cnew[k] >= cnew[k+1] for k in range(q,len(cnew)-1))
                if (ell,n) == (5,3):
                    result['sharpness_witness'] = {
                        'ell':ell,'n':n,'W':w,'Y':yy,'C':cnew,
                        'W_modes':[k for k,v in enumerate(w) if v == max(w)],
                        'Y_modes':[k for k,v in enumerate(yy) if v == max(yy)],
                        'mode_distance':difference,
                        'C_log_concave':log_concave(cnew)}
                digest.update(json.dumps([ell,n,new,w,yy],separators=(',',':')).encode())
                result['polynomials_tested'] += 1
            prev,cur = cur,new
            cprev,ccur = ccur,cnew

    # Tied-mode boundary tests use only the elementary order definition.
    # Delta polynomials test the zero-support and pure-shift cases.
    boundary = [((1,1),(0,1,1)), ((1,),(0,0,1)),
                ((1,2,1),(1,3,3,1)), ((0,1,1),(0,1,1))]
    for p,q in boundary:
        lr(p,q,True)
        assert mode(p) <= mode(q)
    result['tie_and_zero_support_boundary_cases'] = len(boundary)
    assert result['closed_formula_comparisons'] == len(direct_cases)
    result['coefficient_stream_sha256'] = digest.hexdigest()
    result['source_sha256'] = hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
    assert result['source_sha256'] == '66bd66f1a94163be3cb7f8929629c0f122d7f7490759017615c0d690a842773c'
    result['limitations'] = (
        'Finite checks support the written all-parameter structural proof; '
        'they are not an exhaustive infinite verification or an independent '
        'referee. Extra test domains were selected after the proof was written '
        'in the same research context. Full hypercomb unimodality is not proved.')
    dest = Path(__file__).with_name('two-step-checks.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                     ['domains','sharpness_witness','symbolic_checks']},indent=2))


if __name__ == '__main__':
    main()
