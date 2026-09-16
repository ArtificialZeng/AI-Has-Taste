#!/usr/bin/env python3
"""Exact adversarial calibration of the growing-boundary proof; no floats."""
import json
from fractions import Fraction
from math import comb, factorial, isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-binary-subsum-shape-research-9e631dc6dcdd'

def mean_bound(n):
    return min((Fraction(n+2**(k+1)-k-2,k+1),k) for k in range(n.bit_length()))

def criterion(n,j):
    M,k=mean_bound(n)
    if j*M>=n:return False
    return comb(n,j)**2*(1-j*M/n)**2>comb(n+j-2,j-1)*comb(n+j,j+1)

def low_polys(limit,degree):
    polys=[[1]+[0]*degree,[1]+[0]*degree]
    for n in range(2,limit+1):
        if n%2:
            polys.append(polys[-1][:]);continue
        a=[sum(comb(n,j-2*r)*polys[n//2][r]
               for r in range(j//2+1)) for j in range(degree+1)]
        b=polys[n-2][:];q=2
        while n%q==0:
            for j in range(degree,q-1,-1):b[j]+=b[j-q]
            q*=2
        polys.append([x+y for x,y in zip(a,b)])
    return polys

def main():
    limit=4096;degree=13
    # Coin-change dynamic programming, independent of the halving recurrence.
    counts=[0]*(limit+1);counts[0]=1;q=1
    while q<=limit:
        for n in range(q,limit+1):counts[n]+=counts[n-q]
        q*=2
    expectation_weight=[0]*(limit+1);ones=[0]*(limit+1);q=1
    while q<=limit:
        total=[0]*(limit+1)
        for n in range(q,limit+1):total[n]=counts[n-q]+total[n-q]
        for n in range(limit+1):expectation_weight[n]+=q*total[n]
        if q==1:ones=total
        q*=2
    assert all(expectation_weight[n]==n*counts[n] for n in range(limit+1))
    polys=low_polys(limit,degree)
    mean_checks=0;envelopes=0;sufficient=0;rows=[]
    for n in range(2,limit+1):
        assert polys[n][0]==counts[n]
        assert counts[n]==(counts[n-1] if n%2 else counts[n-1]+counts[n//2])
        M,K=mean_bound(n)
        assert Fraction(ones[n],counts[n])<=M
        mean_checks+=1
        for j in range(1,min(n,degree-1)+1):
            cj=polys[n][j];bc=comb(n,j)
            assert n*cj>=bc*(n*counts[n]-j*ones[n])
            assert cj<=counts[n]*comb(n+j-1,j)
            assert 2*factorial(j)*cj>=n**(j-1)*((2*n-j*(j-1))*counts[n]-2*j*ones[n])
            envelopes+=1
            if criterion(n,j):
                assert cj*cj>polys[n][j-1]*polys[n][j+1]
                sufficient+=1
        if n in [2,3,4,5,6,7,8,15,16,31,32,63,64,127,128,255,256,1023,1024,4095,4096]:
            rows.append(dict(n=n,mean_ones=str(Fraction(ones[n],counts[n])),
                bound=str(M),minimizing_K=K,
                positions_certified=[j for j in range(1,min(n,degree-1)+1) if criterion(n,j)]))
    large=[]
    for exponent in [8,16,32,64,128,256,512,1024]:
        n=2**exponent
        js=[j for j in range(1,isqrt(exponent)+3) if criterion(n,j)]
        assert js==list(range(1,len(js)+1))
        large.append(dict(n=f'2^{exponent}',certified_consecutive_j=js,
                          counts_or_N_computed=False,method='exact rational sufficient criterion G1'))
    report=dict(job_id=JOB,arithmetic='arbitrary-precision integers and rational numbers',
        scope=dict(mean_bound_n=[2,limit],low_coefficient_degree=degree,
                   mean_checks=mean_checks,coefficient_envelope_checks=envelopes,
                   sufficient_criterion_checks_against_actual_coefficients=sufficient),
        small_and_dyadic_boundaries=rows,large_parameter_certificates=large,
        limits='Finite checks calibrate the analytic proof, not its infinite quantifiers. Large-n entries apply a proved sufficient criterion; actual huge polynomials were not computed.')
    out=ROOT/'evidence/research_growing_boundary.json'
    temp=out.with_suffix('.tmp');temp.write_text(json.dumps(report,indent=2)+'\n');temp.replace(out)
    print(json.dumps(dict(scope=report['scope'],large_parameter_certificates=large),indent=2))

if __name__=='__main__':main()
