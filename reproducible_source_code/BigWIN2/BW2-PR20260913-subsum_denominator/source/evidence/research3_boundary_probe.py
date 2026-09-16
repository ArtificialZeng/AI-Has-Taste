"""Structured held-out K_sharp_v1 attack near dyadic thresholds.

All Newton orders at selected j and shifts, using FLINT exact polynomials.
This is a sparse family, not exhaustive coverage between listed j values.
"""
import hashlib
import json
from math import comb
from pathlib import Path
from time import monotonic
import flint
from flint import fmpz_poly

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-subsum-denominator-research-077128f18f2f'
J_VALUES = [126,127,128,129,190,191,192,193,254,255,256,257,510,511,512,513]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def shifts(j):
    return sorted({1,2,3,(j+1)//2,(j+1)//2+1,j-1,j,j+1})

def old_poly(s,t,m):
    n = s*2**t
    A = fmpz_poly([1])
    factors = []
    for i in range(1,m+1):
        e = ((n-1)//i).bit_length()
        q = s
        while q%2 == 0:
            q //= 2
            if q==i:
                e += 1
        if e:
            factors.append(fmpz_poly([1]+[0]*(i-1)+[1]).pow_trunc(e,m+1))
    while len(factors)>1:
        factors = [factors[i].mul_low(factors[i+1],m+1)
            if i+1<len(factors) else factors[i] for i in range(0,len(factors),2)]
    return factors[0] if factors else A

def margin(A,s,j):
    def a(r):
        return int(A[r]) if r>=0 else 0
    def b(r):
        return a(r)+a(r-s)
    return 2*(b(j)**2-b(j-1)*b(j+1))-(a(j)**2-a(j-1)*a(j+1))-(a(j-s)**2-a(j-s-1)*a(j-s+1))

def differences(v):
    c=[]
    while v:
        c.append(v[0])
        v=[b-a for a,b in zip(v,v[1:])]
    return c

def main():
    start=monotonic()
    path=ROOT/'evidence/research3_boundary_probe.json'
    out=dict(job_id=JOB,kernel_version='K_sharp_v1',complete=False,
        j_values=J_VALUES,shift_rule='distinct {1,2,3,floor((j+1)/2),floor((j+1)/2)+1,j-1,j,j+1}',
        newton_order_rule='all 0<=h<=2j at every listed pair',
        arithmetic='FLINT exact integer polynomials; Python integer differences',
        flint_version=flint.__version__,records=[],negative_coefficients=[],
        implementation_sha256=sha(Path(__file__)),
        frozen_definition_sha256=sha(ROOT/'evidence/research2.md'))
    for j in J_VALUES:
        m=j+1
        P=fmpz_poly([1])
        for i in range(1,m+1):
            P=(P+P.left_shift(i)).truncate(m+1)
        for s in shifts(j):
            tau=0
            while s*2**tau<9 or 2*s*2**tau<=j+1:
                tau+=1
            A=old_poly(s,tau,m)
            vals=[]
            for v in range(2*j+1):
                vals.append(margin(A,s,j))
                A=A.mul_low(P,m+1)
            c=differences(vals)
            assert c[-1]==comb(2*j,j)//(j+1)
            r=dict(s=s,j=j,tau=tau,newton_coefficients=c)
            out['records'].append(r)
            out['negative_coefficients'].extend(dict(s=s,j=j,tau=tau,h=h,value=x)
                for h,x in enumerate(c) if x<0)
        out['elapsed_seconds']=round(monotonic()-start,3)
        tmp=path.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(out,indent=2)+'\n')
        tmp.replace(path)
        print(json.dumps(dict(j=j,polynomials=len(out['records']),
            negatives=len(out['negative_coefficients']),elapsed=out['elapsed_seconds'])),flush=True)
    out.update(complete=True,polynomials=len(out['records']),
        newton_coefficients=sum(len(r['newton_coefficients']) for r in out['records']),
        elapsed_seconds=round(monotonic()-start,3))
    tmp=path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))

if __name__=='__main__':
    main()
