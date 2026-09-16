"""Exact algebra and finite regression checks for the pass-3 proof.

Run from the project root: python3 evidence/lemma-l-check.py
The analytic inequalities and all-degree root count are proved in
lemma-l-proof.md, not inferred from these finite checks. No reviewer identity
or acceptance is asserted. JSON replacement is atomic after all checks pass.
"""
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import platform
import sympy as s

ROOT = Path(__file__).resolve().parent.parent
JOB = 'primary-20260914-vishnyakova-shifts-research-1d29f50c8dec'
SOURCE_HASH = '599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8'
assert hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest() == SOURCE_HASH
z, t, y, delta, W, V, eta, R, u = s.symbols('z t y delta W V eta R u')
a = z*(1+z)


def op(p, shift):
    return s.Poly(z*(1+z)*p.diff().as_expr()+(z+shift)*p.as_expr(), z)


identities = []
f = s.Function('f')(z)
T = lambda p: a*s.diff(p, z)+(z+t)*p
assert s.expand(T(T(f))-(a*a*s.diff(f,z,2)+a*(1+4*z+2*t)*s.diff(f,z)
                        +(2*z*z+(1+2*t)*z+t*t)*f)) == 0
identities.append('General second-order operator identity')

B = 1-4*y+2*t
C = 2*y*y-(1+2*t)*y+t*t
ratio = (1-y)**2*(W*W-V-2*eta*W)-(1-y)*B*(W-eta)+C
via_log_derivatives = (a*a).subs(z,-y)*(W*W-V-2*eta*W)/y**2 \
    +(a*(1+4*z+2*t)).subs(z,-y)*(W-eta)/y+C
assert s.cancel(ratio-via_log_derivatives) == 0
identities.append('Evaluation q(-y)/p(-y) in W,V,eta')
assert s.expand(B-2*(s.Rational(1,2)-delta*y)-2*(t+(delta-2)*y)) == 0
identities.append('Negative eta coefficient bound')

K = (1-y)*(s.Rational(5,3)-s.Rational(14,3)*y+2*t)
upper = ratio.subs(eta,s.Rational(1,3)).subs(V,W*W-W+(1-R)*W*W/R)
expected_upper = (1-y)**2*(W-(1-R)*W*W/R)-K*W+(1-y)*B/3+C
assert s.cancel(upper-expected_upper) == 0
U = t*t-t/3-s.Rational(1,4) \
    +(2*delta*t+2*delta/3-8*t/3-s.Rational(5,6))*y \
    +(delta*delta-11*delta/3+s.Rational(10,3))*y*y
assert s.cancel(expected_upper.subs(W,R/(1-y)).subs(R,s.Rational(1,2)-delta*y)-U) == 0
assert s.expand(s.Poly(U,y).nth(2)-(delta-s.Rational(5,3))*(delta-2)) == 0
identities.extend(['Cauchy upper bound algebra', 'Decreasing quadratic substitution',
                   'Convexity coefficient factorization'])
de = (1+2*t)/(1+t)**2
N = 12*t**6+60*t**5+89*t**4+12*t**3-60*t**2-40*t-7
assert s.cancel(U.subs(y,1/(2*(2+delta))).subs(delta,de)
                -N/(3*(2*t*t+6*t+3)**2)) == 0
identities.append('Endpoint U_t(Y) rational identity')


def bernstein(p):
    pol = s.Poly(s.expand(p.subs(t,s.Rational(3,10)*(u-1))), u)
    n = pol.degree()
    coeffs = [sum(pol.nth(k)*s.binomial(j,k)/s.binomial(n,k)
                  for k in range(j+1)) for j in range(n+1)]
    reconstructed = sum(coeffs[j]*s.binomial(n,j)*u**j*(1-u)**(n-j)
                        for j in range(n+1))
    assert s.expand(reconstructed-pol.as_expr()) == 0
    return coeffs


N_bern = bernstein(N)
assert N_bern == list(map(s.Rational, ['-17519/125000','-273/500','-58837/50000',
                                      '-10481/5000','-84/25','-5','-7']))
assert all(c < 0 for c in N_bern)
Q = s.Poly(1,z)
for n in range(1,4):
    Q = op(Q,t)
Q3 = 6*z**3+6*(1+t)*z**2+(3*t*t+3*t+1)*z+t**3
assert s.expand(Q.as_expr()-Q3) == 0
D3 = s.discriminant(Q.as_expr(),z)
D3_bern = bernstein(D3)
assert D3_bern == list(map(s.Rational, ['495087/125000','103179/25000','11616/3125',
                                      '10209/2500','708/125','42/5','12']))
assert all(c > 0 for c in D3_bern)
identities.extend(['Bernstein reconstruction of N on [-3/10,0]',
                   'Cubic recurrence and discriminant',
                   'Bernstein reconstruction of cubic discriminant on [-3/10,0]'])


# A distinct coefficient implementation, with Fraction rather than symbolic
# differentiation, checks outputs and Euclidean Sturm variations on each case.
def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def fmulroot(p, r):
    q = [F(0)]*(len(p)+1)
    for j,c in enumerate(p):
        q[j] -= r*c
        q[j+1] += c
    return q


def fop(p, shift):
    q = [F(0)]*(len(p)+1)
    for j,c in enumerate(p):
        q[j] += (j+shift)*c
        q[j+1] += (j+1)*c
    return q


def feval(p,x):
    v = F(0)
    for c in reversed(p):
        v = v*x+c
    return v


def frem(p,q):
    p = p[:]
    while len(p) >= len(q):
        fac, offset = p[-1]/q[-1], len(p)-len(q)
        for j,c in enumerate(q):
            p[j+offset] -= fac*c
        trim(p)
    return p


def fnorm(p):
    return [c/abs(p[-1]) for c in p] if p else []


def fsturm(p):
    seq = [fnorm(p),fnorm([j*p[j] for j in range(1,len(p))])]
    while True:
        rem = frem(seq[-2],seq[-1])
        if not rem:
            break
        seq.append(fnorm([-c for c in rem]))
    return seq


def fsign(x):
    return int(x > 0)-int(x < 0)


def fvariations(seq,x):
    signs = []
    for p in seq:
        v = (fsign(p[-1]) if x == 'inf' else
             fsign(p[-1])*(-1)**(len(p)-1) if x == '-inf' else fsign(feval(p,x)))
        if v:
            signs.append(v)
    return {'signs':signs,'variations':sum(a != b for a,b in zip(signs,signs[1:]))}


families = []
for d in (2,4,6,8):
    families.extend([
        tuple(F(j+1,d+1) for j in range(d)),
        tuple(F(100+j,100000) for j in range(d)),
        tuple(F(99900+j,100000) for j in range(d)),
    ])
tests = []
for shift in (F(-3,10),F(-29,100),F(-1,10000)):
    de_f = (1+2*shift)/(1+shift)**2
    for magnitudes in families:
        Sf = sum(1/a for a in magnitudes)
        Lam = 1/(Sf+de_f)
        yf = Lam/2
        for fraction in (F(1), F(1,11)):
            lam = fraction*Lam
            roots = [-a for a in magnitudes]+[lam]
            assert len(set(roots)) == len(roots)
            p = [F(1)]
            for r in roots:
                p = fmulroot(p,r)
            q = fop(fop(p,shift),shift)
            assert q[1] >= 0
            assert (q[1] == 0) == (fraction == 1)
            assert feval(p,-yf) < 0 and feval(q,-yf) > 0
            q_sym = op(op(s.Poly(sum(s.Rational(c.numerator,c.denominator)*z**j
                                     for j,c in enumerate(p)),z),s.Rational(shift)),s.Rational(shift))
            assert [F(q_sym.nth(j)) for j in range(q_sym.degree()+1)] == q
            seq = fsturm(q)
            assert len(seq[-1]) == 1
            endpoints = ['-inf',F(-1),F(0),'inf']
            cert = [fvariations(seq,x) for x in endpoints]
            vs = [a['variations'] for a in cert]
            counts = [vs[j]-vs[j+1] for j in range(3)]
            assert counts == [0,len(magnitudes)+2,1]
            tests.append({'t':str(shift),'negative_root_magnitudes':[str(a) for a in magnitudes],
                'lambda':str(lam),'fraction_of_bound':str(fraction),'y':str(yf),
                'q_linear_coefficient':str(q[1]),'p_at_minus_y':str(feval(p,-yf)),
                'q_at_minus_y':str(feval(q,-yf)),
                'q_coefficients_ascending':[str(c) for c in q],
                'sturm_endpoints':['-inf','-1','0','inf'],'sturm':cert,
                'root_counts_below_minus1_minus1_to0_positive':counts,'gcd_degree':0,
                'coefficient_implementations_agree':True})
    print('Completed exact regression cases at',shift,flush=True)

out = {'job_id':JOB,'source_sha256':SOURCE_HASH,'python':platform.python_version(),
       'sympy':s.__version__,'symbolic_identities_checked':identities,
       'endpoint_numerator':str(N),'endpoint_bernstein_coefficients':list(map(str,N_bern)),
       'cubic':str(Q3),'cubic_discriminant':str(s.factor(D3)),
       'cubic_discriminant_bernstein_coefficients':list(map(str,D3_bern)),
       'bernstein_parameterization':'t=(3/10)(u-1), 0<=u<=1, degree 6',
       'exact_test_count':len(tests),'equality_case_count':sum(v['fraction_of_bound']=='1' for v in tests),
       'exact_tests':tests,
       'limitations':'The quantified proof is in lemma-l-proof.md. Finite tests and symbolic identities are not an independent mathematical referee; no floating-point root decisions are used here.'}
path = ROOT/'evidence/lemma-l-check.json'
tmp = path.with_suffix('.json.tmp')
tmp.write_text(json.dumps(out,indent=2)+'\n')
os.replace(tmp,path)
print(json.dumps({'identities':len(identities),'tests':len(tests),
                  'equality_tests':out['equality_case_count']},indent=2))
