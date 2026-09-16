#!/usr/bin/env python3
"""Reproduce boundary identities, polynomial positivity, and a cone obstruction.

Run: python3 evidence/research_boundary.py
The all-parameter proof is given in research-boundary-proof.md. SymPy expands
the displayed polynomial identities exactly; the finite recurrence checks only
calibrate the coefficient formulas and do not replace the proof.
"""
import json
from math import comb
from pathlib import Path

import sympy as sp

from research_recurrence import build, convolution, turan

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-binary-subsum-shape-research-f5d9991a30d8'


def low_coefficients(m, weights):
    """Linear formulas in formal weights w_0,...,w_m, through degree four."""
    w = weights[m]
    r0 = sum(weights[:m])
    total = [sum(weights),
        2*sum(i*weights[i] for i in range(m+1)),
        2*sum(i*i*weights[i] for i in range(m+1)),
        sum(((4*i**3+2*i)//3-(m-i)*(m-i+1))*weights[i] for i in range(m+1))]
    fourth = 0
    for k in range(1,m+1):
        lower = sum(weights[:k])
        linear = k*weights[k]-lower
        quadratic = 2*sum(i*i*weights[i] for i in range(k//2+1))
        fourth += (comb(2*k,4)*weights[k]+comb(2*k,2)*linear+quadratic
            +2*sum(i*i*weights[i] for i in range(k))+(lower if k%2 == 0 else 0))
    total.append(fourth)
    a = [w,2*m*w,2*m*m*w-r0,(4*m**3+2*m)*w//3-2*m*r0,
        comb(2*m,4)*w+comb(2*m,2)*(m*w-r0)
        +2*sum(i*i*weights[i] for i in range(m//2+1))]
    return total, a


def main():
    m, l, t, k, u, b, c = sp.symbols('m l t k u b c', integer=True, nonnegative=True)
    s1 = lambda z: (m*(m+1)-z*(z-1))/2
    s2 = lambda z: (m*(m+1)*(2*m+1)-(z-1)*z*(2*z-1))/6
    s3 = lambda z: sp.summation((4*k**3+2*k)/3-(m-k)*(m-k+1), (k,z,m))
    kernel = sp.expand(4*s2(l)*s2(t)-s1(l)*s3(t)-s1(t)*s3(l)
                       -4*m*m*(m*m-1)/3-(m-l)*(m-t))
    regions = [
        ('1 <= l <= t <= m', {l:u+1, t:u+1+b, m:u+1+b+c}, (u,b,c)),
        ('l=0, 2 <= t <= m', {l:0, t:b+2, m:b+2+c}, (b,c)),
        ('l=t=0', {l:0, t:0, m:c}, (c,)),
        ('l=0, t=1', {l:0, t:1, m:c+1}, (c,)),
    ]
    certificates = []
    for name, substitutions, variables in regions:
        polynomial = sp.Poly(sp.expand(36*kernel.subs(substitutions)), *variables)
        assert all(coefficient >= 0 for _, coefficient in polynomial.terms())
        by_c = sp.Poly(polynomial.as_expr(), c)
        certificates.append(dict(region=name, variables=[str(v) for v in variables],
            substitutions={str(v):str(x) for v,x in substitutions.items()},
            factor='36*K(l,t)',
            terms=[dict(exponents=list(exponents), coefficient=int(coefficient))
                   for exponents, coefficient in polynomial.terms()],
            coefficients_by_c_power={str(e[0]):str(sp.factor(coefficient))
                                     for e, coefficient in by_c.terms()},
            all_coefficients_nonnegative=True))

    # Independently check the kernel formula against literal finite sums.
    kernel_checks = 0
    for M in range(1,13):
        for L in range(M+1):
            for T in range(L,M+1):
                p1 = lambda z: sum(range(z,M+1))
                p2 = lambda z: sum(i*i for i in range(z,M+1))
                p3 = lambda z: sum((4*i**3+2*i)//3-(M-i)*(M-i+1)
                                   for i in range(z,M+1))
                expected = (4*p2(L)*p2(T)-p1(L)*p3(T)-p1(T)*p3(L)
                            -4*M*M*(M*M-1)//3-(M-L)*(M-T))
                assert kernel.subs({m:M,l:L,t:T}) == expected >= 0
                kernel_checks += 1

    # Coefficient-formula calibration with actual binary partition counts.
    counts = [1,1]
    for i in range(2,65):
        counts.append(counts[-1] if i%2 else counts[-1]+counts[i//2])
    boundary_checks = []
    for n, a, bb, p, polys in build(128):
        M = n//2
        moments = [sum(i**r*counts[i] for i in range(M+1)) for r in range(4)]
        R0 = moments[0]-counts[M]
        cubic = sum(((4*i**3+2*i)//3-(M-i)*(M-i+1))*counts[i]
                    for i in range(M+1))
        assert p[:3] == [moments[0],2*moments[1],2*moments[2]]
        assert (p[3] if len(p)>3 else 0) == cubic
        predicted_total, predicted_a = low_coefficients(M,counts[:M+1])
        assert predicted_total == (p+[0]*5)[:5]
        assert predicted_a == (a+[0]*5)[:5]
        assert turan(a,1) == 2*M*M*counts[M]**2+counts[M]*R0
        if n >= 4:
            assert turan(a,2) == 4*M*M*(M*M-1)//3*counts[M]**2+R0**2
            assert turan(p,2) > turan(a,2) > 0
        if n >= 6:
            assert turan(p,1) > turan(a,1) > 0
            lower_bound_times_three = (4*M*M-9*M-4)*counts[M]*R0
            assert 3*(turan(p,1)-turan(a,1)) >= lower_bound_times_three > 0
        boundary_checks.append(n)

    # New third-position target: a finite kernel screen, not a universal proof.
    third_rows = []
    for M in range(5,33):
        basis = [low_coefficients(M,[int(i>=L) for i in range(M+1)])
                 for L in range(M+1)]
        entries = []
        for L,(p,a) in enumerate(basis):
            for T in range(L,M+1):
                q,bpoly = basis[T]
                twice_kernel = (2*p[3]*q[3]-p[2]*q[4]-q[2]*p[4]
                    -(2*a[3]*bpoly[3]-a[2]*bpoly[4]-bpoly[2]*a[4]))
                entries.append((twice_kernel,L,T))
        third_rows.append(dict(m=M,pair_count=len(entries),
            minimum_twice_kernel=min(entries)[0],
            negative_entries=[dict(twice_kernel=v,l=L,t=T) for v,L,T in entries if v<0]))

    # A strict-input counterexample to the specified abstract induction cone.
    a = [10,11,12,13,14,13,12,11,10]
    total = [3*v for v in a]
    bpoly = [2*v for v in a]
    aa = convolution(a,[1,2,1])
    bb = convolution(total,[1,0,1])
    nn = [v+w for v,w in zip(aa,bb)]
    assert a == a[::-1] and bpoly == bpoly[::-1] and total == total[::-1]
    assert all(turan(total,j)>turan(a,j)>0 for j in range(1,len(a)-1))
    assert turan(nn,1) == -304 and turan(aa,1) == 521
    obstruction = dict(scope='Abstract carry-one propagation; not actual N_n inputs',
        input_A=a, input_B=bpoly, input_N=total,
        input_TA=[turan(a,j) for j in range(1,len(a)-1)],
        input_TN=[turan(total,j) for j in range(1,len(total)-1)],
        map=dict(A_new='(1+x)^2 A', B_new='(1+x^2) N', N_new='A_new+B_new'),
        output_A=aa, output_B=bb, output_N=nn,
        failure=dict(j=1, A_triple=aa[:3], B_triple=bb[:3], N_triple=nn[:3],
                     T_A=521,T_N=-304,compensation=-825))
    report = dict(job_id=JOB,
        boundary_scope='For even n>=6: T_j(N_n)>T_j(A_n)>0 at j=1,2 and reflected indices. The j=2 result already holds for even n>=4.',
        polynomial_certificate=dict(kernel=str(kernel), scale=36, regions=certificates),
        literal_kernel_sum_check_count=kernel_checks,
        coefficient_formula_calibration_even_n=boundary_checks,
        third_position_kernel_screen=dict(m_range=[5,32],
            total_pair_count=sum(row['pair_count'] for row in third_rows),rows=third_rows,
            status='Finite nonnegative-kernel observation only; all-m assertion unproved.'),
        abstract_cone_obstruction=obstruction,
        limitations='No universal assertion for the remaining internal indices; no fresh referee or novelty certification.')
    out = ROOT/'evidence/research_boundary.json'
    temp = out.with_suffix('.tmp')
    temp.write_text(json.dumps(report,indent=2)+'\n')
    temp.replace(out)
    print(json.dumps(dict(boundary_scope=report['boundary_scope'],
        positive_polynomial_regions=len(certificates),
        literal_kernel_sum_check_count=kernel_checks,
        third_position_pairs=report['third_position_kernel_screen']['total_pair_count'],
        calibration_even_n=[2,128], obstruction=obstruction['failure']),indent=2))


if __name__ == '__main__':
    main()
