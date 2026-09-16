#!/usr/bin/env python3
"""Exact intake-only calibration for the Section9.6 comb proposal."""
import json, platform, time
from datetime import datetime, timezone
from math import comb

def vectors(d, budget, prefix=()):
    if d == 0:
        yield prefix
    else:
        for a in range(budget + 1):
            yield from vectors(d-1, budget-a, prefix+(a,))

def ideals(n):
    d=2*n
    predecessors=[1<<j for j in range(d)]
    for stage in range(n):
        root=2*stage+1
        for j in range(root):
            predecessors[j] |= 1<<root
    masks=[mask for mask in range(1,1<<d)
           if all(not (mask>>j&1) or (mask&predecessors[j])==predecessors[j]
                  for j in range(d))]
    return [([j for j in range(d) if mask>>j&1],mask.bit_count()) for mask in masks]

def add(a,b):
    c=a.copy()
    for k,v in b.items():
        c[k]=c.get(k,0)+v
        if not c[k]: del c[k]
    return c
def mul(a,b):
    c={}
    for i,u in a.items():
        for j,v in b.items():
            c[i+j]=c.get(i+j,0)+u*v
    return {k:v for k,v in c.items() if v}
def smul(a,b,m):
    c={}
    for i,u in a.items():
        for j,v in b.items():
            if i+j<=m:
                c[i+j]=add(c.get(i+j,{}),mul(u,v))
    return {k:v for k,v in c.items() if v}
def main():
    start=time.perf_counter()
    cases=[]
    for n in range(6):
        d=2*n; constraints=ideals(n); h=[0]*(d+1); checked=0
        for x in vectors(d,d):
            checked+=1
            if all(sum(x[i] for i in inds)<=bound for inds,bound in constraints):
                h[sum(a>0 for a in x)]+=1
        assert checked==comb(2*d,d)
        cases.append(dict(n=n,dimension=d,nonempty_ideals=len(constraints),
                          ambient_vectors=checked,coefficients=h,points=sum(h)))
    m=6
    F={n+1:{j-n:v for j,v in enumerate(c['coefficients']) if v}
       for n,c in enumerate(cases)}
    power={0:{0:1}}; composed={}
    for r in range(1,m+1):
        power=smul(power,F,m)
        tail={j:1 for j in range(r-1)}
        numerator=mul({j:comb(r,j) for j in range(r+1)},tail)
        Laurent={j+1-r:v for j,v in numerator.items()}
        R=add({0:1},Laurent)
        R={j:(-1)**(r-1)*v for j,v in R.items()}
        for k,v in power.items():
            composed[k]=add(composed.get(k,{}),mul(R,v))
    composed={k:v for k,v in composed.items() if v}
    print(json.dumps(dict(schema=1,observed_at=datetime.now(timezone.utc).isoformat(),
        python=platform.python_version(),arithmetic='integers and finite Laurent polynomial rings',
        randomness=False,seed=None,domain='all nonnegative integer coordinates satisfying EVERY lower-ideal inequality on recursively defined comb tau_n',
        cases=cases,composition_through_x_degree=m,
        residual={str(k):{str(j):v for j,v in p.items()} for k,p in composed.items()},
        composition_equals_x_through_degree_6=composed=={1:{0:1}},
        uniform_proof=False,independent_holdout=False,
        wall_seconds=time.perf_counter()-start),ensure_ascii=False))
if __name__=='__main__': main()
