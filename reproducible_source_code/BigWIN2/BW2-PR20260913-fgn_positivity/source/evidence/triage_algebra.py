"""Exact algebra for bounded triage; run with python3 evidence/triage_algebra.py.

This checks identities and records a next target. It does not certify an
all-dimensions theorem or the sign of the n=5 penultimate coefficient.
"""
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
r1, r2, r3, r4 = s.symbols('r1 r2 r3 r4')
a, b, c = s.symbols('a b c')
L2, L3, L5 = s.symbols('L2 L3 L5')
rhohat = r2 + r2**2 - r1**2 - r1*r3
sub = {r1: (a-2)/2, r2: (b-2*a+1)/2,
       r3: (a*a-2*b+a)/2, r4: (c-2*a*a+b)/2}

def cramer(n, k):
    rs = [1, r1, r2, r3, r4]
    A = s.Matrix(n-1, n-1, lambda i, j: rs[abs(i-j)])
    B = A.copy()
    B[:, k-2] = s.Matrix(rs[1:n])
    return s.factor(A.det()), s.factor(B.det())

D3, N43 = cramer(4, 3)
assert s.expand(N43-(1-r2)*rhohat) == 0
Fpoly = s.expand(4*rhohat.subs(sub))
assert Fpoly == b*b-a**3-2*a*b+4*a*a-2*a-1
F = [(1,-1), (2,-2), (4,4), (6,-2), (8,-1), (9,1)]
assert [sum(coef*base**t for base,coef in F) for t in [0,1,2,3]] == [-1,0,0,24]
assert s.prod(s.Rational(base)**(coef*base) for base,coef in F) == s.Rational(27,16)**2
assert s.prod(s.Rational(base)**(coef*base**2) for base,coef in F) == s.Rational(243,256)**18

D4, N53 = cramer(5, 3)
K = (1-r2)*(1-r4)-(r1-r3)**2
assert s.expand(N53-rhohat*K) == 0
_, N54 = cramer(5, 4)
P = s.Poly(s.expand(16*N54.subs(sub)), a,b,c)
terms = sorted((2**i*3**j*5**k,int(coef)) for (i,j,k),coef in P.terms())
signs = [coef for base,coef in terms]
V = sum(x*y < 0 for x,y in zip(signs, signs[1:]))

def derivative(t, order):
    return s.expand(sum(coef*(2**i*3**j*5**k)**t *
                        (i*L2+j*L3+k*L5)**order
                        for (i,j,k),coef in P.terms()))

assert derivative(1,0) == 0
assert derivative(1,1) == 80*L2-48*L3
assert all(derivative(2,j) == 0 for j in range(3))
result = {
    'job_id': 'primary-20260913-fgn-positivity-triage-00acd6d3f130',
    'evidence_type': 'exact symbolic identities, not an all-n proof',
    'sympy_version': s.__version__,
    'source_sha256': hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
    'n4': {'denominator': str(D3), 'middle_numerator': str(N43),
           'four_rhohat_polynomial_a2t_b3t': str(Fpoly),
           'exponential_terms_base_coefficient': F,
           'sign_variations': 3, 'values_at_0_1_2_3': [-1,0,0,24],
           'derivative_at_1': '2*log(27/16)>0',
           'derivative_at_2': '18*log(243/256)<0'},
    'n5': {'denominator': str(D4), 'coefficient_3_numerator': str(N53),
           'coefficient_3_factorization': 'rhohat*((1-r2)*(1-r4)-(r1-r3)**2)',
           'coefficient_4_numerator': str(N54),
           'P_definition': 'P(t)=16*N54(t), t=2H',
           'P_exponential_terms_base_coefficient': terms,
           'P_raw_sign_variations': V,
           'P_endpoint_derivatives': {
               f'P_derivative_{j}_at_{t}': str(derivative(t,j))
               for t in [1,2] for j in range(4)},
           'coefficient_4_sign_status': 'unresolved; no interval sign certificate generated'}
}
(ROOT/'evidence/triage-algebra.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'identities_checked': True, 'P_terms':len(terms),
                  'P_raw_sign_variations': V, 'output':'evidence/triage-algebra.json'}))
