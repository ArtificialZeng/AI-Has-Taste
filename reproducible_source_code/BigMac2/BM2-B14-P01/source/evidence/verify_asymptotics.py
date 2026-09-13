#!/usr/bin/env python3
"""Exact algebra plus explicitly noncertified floating asymptotic diagnostics.

Run: python3 evidence/verify_asymptotics.py
No external packages. Decimal recurrences use 60 significant digits;
Gamma constants and displayed residuals use standard-library binary64 math.
"""
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def convolution(a,b,nmax):
    return [sum((a[j]*b[n-j] for j in range(n+1)), F(0))
            for n in range(nmax+1)]

def power(beta, sign, nmax):
    # (1+sign*z)^beta from the generalized binomial theorem.
    a=[F(1)]
    for n in range(1,nmax+1):
        a.append(a[-1]*(beta-n+1)*sign/n)
    return a

def exponential(rate,nmax):
    a=[F(1)]
    for n in range(1,nmax+1):
        a.append(a[-1]*rate/n)
    return a

def main():
    nmax=60
    e=exponential(F(-1,2),nmax)
    closed_d=convolution(e,power(F(-1,2),-1,nmax),nmax)
    closed_h=convolution(convolution(e,power(F(1,4),1,nmax),nmax),
                         power(F(-1,4),-1,nmax),nmax)
    d,h=[F(1),F(0)],[F(1),F(0),F(0)]
    for n in range(2,nmax+1):
        d.append((2*(n-1)*d[n-1]+d[n-2])/(2*n))
    for n in range(3,nmax+1):
        h.append((2*(n-2)*h[n-2]+h[n-3])/(2*n))
    assert d==closed_d and h==closed_h
    # Analytic multiplier Taylor coefficients at both singularities.
    plus=convolution(exponential(F(1,2),3),
                     [x/F(2)**i for i,x in enumerate(power(F(1,4),-1,3))],3)
    minus=convolution(exponential(F(-1,2),3),
                      [x/F(2)**i for i,x in enumerate(power(F(-1,4),-1,3))],3)
    assert plus==[F(1),F(3,8),F(5,128),F(-41,3072)]
    assert minus==[F(1),F(-3,8),F(13,128),F(-31,3072)]
    def first_correction(beta,linear):
        return beta*(beta+1)/2 + linear*(-beta-1)
    cor_d=first_correction(F(-1,2),F(1,2))
    cor_plus=first_correction(F(-1,4),plus[1])
    cor_minus=first_correction(F(1,4),minus[1])
    assert cor_d==cor_plus==F(-3,8)
    assert cor_minus==F(5,8)
    assert cor_plus-cor_d==0 and cor_minus-cor_d==1
    C0=2**0.25*math.sqrt(math.pi)/math.gamma(0.25)
    C1=math.e*math.sqrt(math.pi)/(2**2.25*math.gamma(0.75))
    assert abs(C1+math.e*math.sqrt(math.pi)*2**(-0.25)/math.gamma(-0.25))<1e-14
    sample=sorted({n+j for n in [64,128,256,512,1024,2048,4096,8192] for j in [0,1]})
    rows=[]
    with localcontext() as ctx:
        ctx.prec=60
        D=[Decimal(1),Decimal(0)]
        H=[Decimal(1),Decimal(0),Decimal(0)]
        for n in range(2,max(sample)+1):
            D.append((2*(n-1)*D[n-1]+D[n-2])/(2*n))
        for n in range(3,max(sample)+1):
            H.append((2*(n-2)*H[n-2]+H[n-3])/(2*n))
        for n in sample:
            p=float(H[n]/D[n])
            parity=(-1)**(n+1)
            leading=C0*n**(-0.25)
            alternating=parity*C1*n**(-0.75)
            refined=leading+alternating*(1+1/n)
            rows.append(dict(n=n,p_approx=p,
                        leading_ratio=p/leading,
                        first_alternating_normalized=(p-leading)/alternating,
                        second_alternating_normalized=(p-leading-alternating)*n/alternating,
                        refined_error_times_n_to_9_over_4=(p-refined)*n**2.25))
    result=dict(exact_algebra_status="all assertions passed",
                exact_closed_form_vs_differential_recurrence_range=[0,nmax],
                multiplier_coefficients_at_plus_one=list(map(str,plus)),
                multiplier_coefficients_at_minus_one=list(map(str,minus)),
                relative_corrections=dict(denominator=str(cor_d),
                  numerator_plus=str(cor_plus),numerator_minus=str(cor_minus),
                  quotient_nonoscillating=str(cor_plus-cor_d),
                  quotient_oscillating=str(cor_minus-cor_d)),
                numerical_evidence_kind="uncertified floating-point consistency checks, not proof or interval bounds",
                numerical_precision="60-digit Decimal coefficient recurrence; binary64 gamma constants and residual calculations",
                C0_approx=C0,C1_approx=C1,records=rows)
    (ROOT/'evidence/asymptotic_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
