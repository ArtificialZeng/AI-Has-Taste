"""Reconstruct k=4 bottom-up from Wastlund (9)/(41), then certify Hurwitz signs.

Run from project root: python3 evidence/research_k4_certificate.py
Exact symbolic identities, not a finite parameter sweep. No imported triage code.
"""
import hashlib
import itertools
import json
from pathlib import Path
import signal
import time

import sympy as S
from sympy.polys.fields import field
from sympy.polys.rings import ring

signal.alarm(180)
started = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260914-matching-mgf-zero-free-research-551b3f76b932'
K, M, N, T = field('m,n,t', S.QQ)
m, n, t, z, x, y = S.symbols('m n t z x y')


def reconstruct(k):
    # L[i,j] = F^(i-j)_{i,m,n-k+i}; diagonal uses the separate d=0 rule.
    L = {(0, 0): K.one}
    for i in range(1, k+1):
        nn = N-k+i
        for j in range(i):
            L[i, j] = (nn*L.get((i-1, j), K.zero)
                       + (M-j)*(i-j+1)*T*L.get((i, j-1), K.zero)
                       + (M-j)*nn*L.get((i-1, j-1), K.zero)) / (
                           (M-j)*nn-(i-j)*T)
        L[i, i] = T/nn*L[i, i-1]+L[i-1, i-1]
    return L[k, k]


f = reconstruct(4)
raw = json.loads((ROOT/'evidence/k4-rational.json').read_text())
pn = S.Poly(f.numer.as_expr(), t)
content, p = pn.primitive()
A = m*n*S.prod(m-i for i in range(1, 4))*S.prod(n-j for j in range(1, 4))
Q = S.prod((m-i)*(n-j)-(4-i-j)*t for i in range(4) for j in range(4-i))
checks = {
    'triage_rational_identity': f == K.from_expr(S.sympify(raw['numerator'])) / K.from_expr(S.sympify(raw['denominator'])),
    'numerator_content_is_A': S.expand(content-A) == 0,
    'denominator_is_Q': S.expand(f.denom.as_expr()-Q) == 0,
    'normalization': S.cancel(f.as_expr().subs(t,0)) == 1,
    'sextic_leading_coefficient_12': p.degree() == 6 and p.LC() == 12,
    'transpose_symmetry_of_P': S.expand(p.as_expr()-p.as_expr().xreplace({m:n,n:m})) == 0,
}
# Calibration uses an independently printed formula, after specialization.
f3 = reconstruct(3).as_expr().subs({m:3,n:3})
checks['eq10'] = S.cancel(f3-6*(162-90*t+16*t*t-t**3)/((4-t)*(3-t)**5)) == 0
assert all(checks.values()), checks

Hraw = S.Poly(S.expand(sum(p.nth(i)*(m*n)**i*4**(6-i)*(1-z)**i*(1+z)**(6-i)
                          for i in range(7))), z)
h = [S.cancel(c/(m*n)**3) for c in Hraw.all_coeffs()]
old = json.loads((ROOT/'evidence/triage-certificate-screen.json').read_text())
checks['triage_transform_identity'] = all(S.expand(c-S.sympify(d)) == 0
    for c,d in zip(h,old['h_coefficients_descending_z']))
assert checks['triage_transform_identity']
R, X, Y = ring('x,y', S.ZZ)
hs = [R.from_expr(c.subs({m:x+4,n:y+4})) for c in h]


def determinant(a):
    # Leibniz expansion in ZZ[x,y], with exact polynomial arithmetic.
    size = len(a)
    out = R.zero
    for perm in itertools.permutations(range(size)):
        sign = (-1)**sum(perm[i]>perm[j] for i in range(size) for j in range(i+1,size))
        term = R.one
        for i,j in enumerate(perm):
            term *= a[i][j]
            if not term:
                break
        out += sign*term
    return out


def summary(poly):
    values = list(poly.values())
    return {'degrees_xy': list(poly.degrees()), 'terms':len(poly),
            'positive_coefficients':sum(c>0 for c in values),
            'negative_coefficients':sum(c<0 for c in values),
            'minimum_nonzero_coefficient':str(min(values)),
            'constant':str(poly.get((0,0),0))}


def serialize(poly):
    return [[i,j,str(c)] for (i,j),c in sorted(poly.items())]


# A[r,c] = h[2*c-r+1], r,c zero based; h outside 0..6 is zero.
hurwitz = [[hs[2*c-r+1] if 0<=2*c-r+1<=6 else R.zero
            for c in range(6)] for r in range(6)]
minors = []
for size in range(1,7):
    minors.append(determinant([row[:size] for row in hurwitz[:size]]))
    print('minor',size,json.dumps(summary(minors[-1])),flush=True)
checks['delta6_identity'] = minors[5] == hs[6]*minors[4]
checks['all_h_positive_coefficients'] = all(all(c>0 for c in q.values()) and q.get((0,0),0)>0 for q in hs)
checks['all_minors_positive_coefficients'] = all(all(c>0 for c in q.values()) and q.get((0,0),0)>0 for q in minors)
output = {
    'proposer_job_id':JOB, 'scope':'Exact reconstruction and universal shifted-coefficient certificate for k=4; pending fresh mathematical review.',
    'sympy_version':S.__version__, 'source_sha256':hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
    'checks':checks, 'parameter_domain':'m=4+x,n=4+y with real x,y>=0; probabilistic interpretation for integer m,n>=4',
    'P_ascending_t':[str(p.nth(i)) for i in range(7)], 'A':str(A), 'Q':str(Q),
    'H_definition':'4^6/(m*n)^3*(1+z)^6*P(m*n/4*(1-z)/(1+z))',
    'h_descending_z':[str(c) for c in h],
    'coefficient_encoding':'Each row [i,j,c] means c*x^i*y^j; omitted entries are zero; integer coefficients are decimal strings.',
    'shifted_h':[serialize(q) for q in hs], 'hurwitz_minors':[serialize(q) for q in minors],
    'shifted_h_summary':[summary(q) for q in hs], 'hurwitz_minors_summary':[summary(q) for q in minors],
    'seconds':time.monotonic()-started,
}
target=ROOT/'evidence/research-k4-certificate.json'
temp=target.with_suffix('.json.tmp')
temp.write_text(json.dumps(output,indent=2)+'\n')
temp.replace(target)
print(json.dumps({'checks':checks,'seconds':output['seconds']},indent=2),flush=True)
