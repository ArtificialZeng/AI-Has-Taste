#!/usr/bin/env python3
"""Cross-check SAT encoding against transparent exhaustive small enumeration."""
import itertools, json
from pysat.solvers import Solver
from sat_decision import build

def brute(n,k):
    best=-1; witnesses=[]
    for A in itertools.combinations(range(1,n+1),k):
        q=len({a+b for i,a in enumerate(A) for b in A[i:]})
        if q>best: best=q; witnesses=[A]
        elif q==best: witnesses.append(A)
    return best,witnesses[0]

rows=[]
for n in range(1,11):
  for k in range(1,n+1):
    exact,w=brute(n,k)
    checks={}
    for target in sorted(set([max(1,exact-1),exact,exact+1])):
      cnf,_,_,_=build(n,k,target)
      with Solver(name='glucose42',bootstrap_with=cnf.clauses) as s: got=s.solve()
      expected=target<=exact; checks[str(target)]=got
      if got!=expected: raise SystemExit(f'FAIL n={n} k={k} target={target}')
    rows.append({'n':n,'k':k,'exact':exact,'witness':w,'threshold_checks':checks})
print(json.dumps({'status':'PASS','method':'all subsets for 1<=k<=n<=10; SAT thresholds exact-1, exact, exact+1','cells':rows},indent=2))
