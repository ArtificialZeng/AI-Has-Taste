#!/usr/bin/env python3
"""Exact count of labeled simple cubic graphs, independently of a generator.

F(c1,c2,c3) counts realizations of any fixed labeled residual degree sequence
with ci occurrences of i; degree-zero vertices have exactly one extension and
are omitted. Eliminate a particular maximum-degree vertex and choose its
neighbors by their residual degree classes. No quotient by graph symmetry.
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def realizations(c1,c2,c3):
    c=(c1,c2,c3)
    if not any(c): return 1
    if (c1+2*c2+3*c3)%2: return 0
    d=max(i+1 for i in range(3) if c[i])
    remaining=list(c);remaining[d-1]-=1
    if d>sum(remaining): return 0
    total=0
    for chosen in product(*(range(min(d,ci)+1) for ci in remaining)):
        if sum(chosen)!=d: continue
        multiplicity=1;child=remaining.copy()
        for i,ki in enumerate(chosen):
            multiplicity*=comb(remaining[i],ki)
            child[i]-=ki
            if i: child[i-1]+=ki
        total+=multiplicity*realizations(*child)
    return total

def cubic_counts(max_n=18):
    all_counts={0:1};connected={}
    for n in range(2,max_n+1,2):
        all_counts[n]=realizations(0,0,n)
        connected[n]=all_counts[n]-sum(comb(n-1,k-1)*connected[k]*all_counts[n-k] for k in range(2,n,2))
    return all_counts,connected

if __name__=='__main__':
    import json
    a,c=cubic_counts()
    print(json.dumps(dict(all_labeled=a,connected_labeled=c,states=realizations.cache_info().currsize),indent=2))
