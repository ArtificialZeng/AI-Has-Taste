"""Exact Newton-basis certificates for an infinite n range at fixed edge degrees.

For fixed shift s, every stage adding s occurs at n=s*2**t, t>=0.
For n>=B+1 all exponents needed through degree B+1 are affine in t.
Thus the H margin at index j<=B is a polynomial of degree at most 2*j.
Nonnegative forward differences at t0 certify it for every integer t>=t0.
No interpolation from an unproved degree bound and no floating point are used.
"""
import argparse
import hashlib
import json
from math import comb
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-c627858a54d2'


def head(n,s,B):
    a=[1]+[0]*(B+1)
    odd=s//(s&-s)
    earlier=set()
    u=odd
    while u<s:
        earlier.add(u)
        u*=2
    for i in range(1,B+2):
        exponent=((n-1)//i).bit_length()+(i in earlier)
        for _ in range(exponent):
            for j in range(B+1,i-1,-1):
                a[j]+=a[j-i]
    return a


def at(a,j):
    return a[j] if 0<=j<len(a) else 0


def minor(a,j):
    return at(a,j)**2-at(a,j-1)*at(a,j+1)


def margins(s,t,B):
    a=head(s<<t,s,B)
    b=[at(a,j)+at(a,j-s) for j in range(B+2)]
    return [2*minor(b,j)-minor(a,j)-minor(a,j-s) for j in range(B+1)]


def differences(values):
    out=[]
    while values:
        out.append(values[0])
        values=[v-u for u,v in zip(values,values[1:])]
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--B',type=int,default=32)
    args=p.parse_args()
    B=args.B
    result=dict(job_id=JOB,edge_bound=B,
        certificate_type='integer Newton forward-difference coefficients',
        source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
        implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        records=[],finite_checks=0,polynomials=0,negative_newton_coefficients=0,
        h_counterexamples=[],holdout_evaluations=0)
    for s in range(1,B+2):
        t0=0
        while (s<<t0)<max(9,B+1):
            t0+=1
        # Check all finitely many earlier stages with n>=9 separately.
        finite=[]
        for t in range(t0):
            if (s<<t)<9:
                continue
            v=margins(s,t,B)
            for j in range(s-1,B+1):
                finite.append(dict(t=t,j=j,margin=v[j]))
                result['finite_checks']+=1
                if v[j]<0:
                    result['h_counterexamples'].append(dict(s=s,t=t,n=s<<t,j=j,margin=v[j]))
        values=[margins(s,t0+h,B) for h in range(2*B+1)]
        holdout={h:margins(s,t0+h,B) for h in [2*B+3,4*B+7]}
        certs=[]
        for j in range(s-1,B+1):
            c=differences([v[j] for v in values[:2*j+1]])
            neg=[h for h,x in enumerate(c) if x<0]
            result['negative_newton_coefficients']+=len(neg)
            result['polynomials']+=1
            certs.append(dict(j=j,degree_bound=2*j,newton_coefficients=c,
                              negative_positions=neg))
            # Exact held-out evaluations outside the interpolation grid.
            for h,v in holdout.items():
                observed=v[j]
                reconstructed=sum(x*comb(h,k) for k,x in enumerate(c))
                assert observed==reconstructed,(s,j,t0,h)
                result['holdout_evaluations']+=1
        result['records'].append(dict(s=s,t0=t0,first_n=s<<t0,
                                     finite_checks=finite,certificates=certs))
        print(json.dumps(dict(s=s,polynomials=result['polynomials'],
            negative_newton_coefficients=result['negative_newton_coefficients'])),flush=True)
    result['all_newton_coefficients_nonnegative']=result['negative_newton_coefficients']==0
    path=ROOT/'evidence/research_edge_probe.json'
    tmp=path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))


if __name__=='__main__':
    main()
