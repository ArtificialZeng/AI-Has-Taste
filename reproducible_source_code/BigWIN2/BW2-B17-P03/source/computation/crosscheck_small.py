#!/usr/bin/env python3
"""Brute-force cross-check of both exact decision implementations on small graphs."""
import itertools, math, pathlib, sys
sys.path.insert(0,str(pathlib.Path(__file__).parent))
import clique_search, packing_verify

cases=0
for x in range(8,31):
  ps=[packing_verify.support(n) for n in range(x+1)]
  for d in range(2,x-1,2):
    vals=[v for v in range(2,x-d+1) if math.gcd(v,v+d)==1]
    adj=[0]*len(vals)
    for i,a in enumerate(vals):
      for j in range(i+1,len(vals)):
        if clique_search.compatible(a,vals[j],d): adj[i]|=1<<j; adj[j]|=1<<i
    masks=[ps[v]|ps[v+d] for v in vals]
    exact=0
    for k in range(len(vals)+1):
      if any(all((adj[i]>>j)&1 for i,j in itertools.combinations(c,2)) for c in itertools.combinations(range(len(vals)),k)): exact=k
      else: break
    for target in range(1,exact+2):
      a=clique_search.decide(adj,target)[0]
      b=packing_verify.has_packing(masks,target)[0]
      assert a==b==(target<=exact),(x,d,target,exact,a,b)
      cases+=1
print(f'SMALL CROSSCHECK PASSED cases={cases} x=8..30 all even gaps')
