#!/usr/bin/env python3
"""Deterministic finite-field checks of the reduction; no recurrence certification."""
from pathlib import Path
from itertools import product
import hashlib
import json
import math

def add(out, key, value, p):
    out[key] = (out.get(key, 0) + value) % p
    if out[key] == 0:
        del out[key]

def multiply(a, b, p, limit=None):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            if limit is None or i+j <= limit:
                add(out, i+j, ai*bj, p)
    return out

def module_step(q, p, sign):
    out = {}
    for (k,r),c in q.items():
        if sign == 1:
            if r < p-1:
                add(out, (k,r+1), c, p)
            else:
                add(out, (k+1,1), c, p)
                add(out, (k,0), -c, p)
        else:
            if r > 0:
                add(out, (k,r-1), c, p)
            else:
                add(out, (k+1,0), c, p)
                add(out, (k,p-1), -c, p)
    return out

def normal_monomial(e, p):
    q = {(0,0):1}
    for _ in range(abs(e)):
        q = module_step(q,p,1 if e>0 else -1)
    return q

def shift(h,p):
    out={}
    for i,c in h.items():
        if i:
            add(out,i-1,c,p)
            add(out,i+p-1,c,p)
    return out

def image(q,p):
    out={}
    for (k,r),c in q.items():
        h={r:1}
        for _ in range(k):
            h=shift(h,p)
        for j,d in h.items():
            add(out,j,c*d,p)
    return out

def digit_sum(n,p):
    s=0
    while n:
        s+=n%p
        n//=p
    return s

def main():
    limit=512
    summary=[]
    for p in (2,3,5,7):
        exponents=range(-12,13)
        hs={e:image(normal_monomial(e,p),p) for e in exponents}
        maxdegree=max(max(h,default=0) for h in hs.values())
        y={}
        a=1
        while a<=limit:
            y[a]=1
            a=p*a+1
        powers=[{0:1}]
        for _ in range(maxdegree):
            powers.append(multiply(powers[-1],y,p,limit))
        series={}
        supportchecks=0
        for e,h in hs.items():
            s={}
            for r,c in h.items():
                for n,v in powers[r].items():
                    add(s,n,c*v,p)
            series[e]=s
            d=max(h,default=0)
            for n in s:
                assert any(digit_sum((p-1)*n+r,p)<=d for r in range(d+1))
                supportchecks+=1
        literal={0:1}
        ct={e:[] for e in exponents}
        comparisons=0
        for n in range(limit+1):
            for e in exponents:
                v=literal.get(-e,0)
                assert v==series[e].get(n,0),(p,e,n)
                ct[e].append(v)
                if (n-e)%p==0 and 0<=(n-e)//p<=n:
                    assert v==math.comb(n,(n-e)//p)%p
                else:
                    assert v==0
                comparisons+=1
            literal=multiply(literal,{p-1:1,-1:1},p)
        combinations=0
        zero_cases=0
        # Every Laurent Q supported on [-2,2], for p=2,3,5.
        if p<=5:
            for coeffs in product(range(p),repeat=5):
                q={}
                for e,c in zip(range(-2,3),coeffs):
                    for key,v in normal_monomial(e,p).items():
                        add(q,key,c*v,p)
                h=image(q,p)
                kernel=all(r==0 and k>0 for k,r in q)
                assert (not h)==kernel,(p,coeffs,q,h)
                zero_cases+=kernel
                for n in range(65):
                    v=sum(c*ct[e][n] for e,c in zip(range(-2,3),coeffs))%p
                    w=sum(c*powers[r].get(n,0) for r,c in h.items())%p
                    assert v==w,(p,coeffs,n)
                combinations+=1
        summary.append({'p':p,'literal_comparisons':comparisons,
                        'support_containment_checks':supportchecks,
                        'all_Q_on_minus2_to2':combinations,
                        'zero_kernel_cases_in_exhaustive_Q':zero_cases,
                        'max_H_degree':maxdegree})
    result={'job_id':'newwin-00001-p18-triage-2060d7b82e53',
            'arithmetic':'exact integers and prime fields; no randomness',
            'monomial_scope':'p=2,3,5,7; exponents -12..12; n=0..512',
            'combination_scope':'all Q on [-2,2] for p=2,3,5; n=0..64',
            'rows':summary,
            'limitation':'Finite reduction checks only; no computational certification of recurrence or nonrecurrence.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path=Path(__file__).with_name('triage-reduction-check.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
