#!/usr/bin/env python3
"""Independent Cartesian brute force for N<=10, compared with exact_search."""
import itertools
import json
from fractions import Fraction
from pathlib import Path
from exact_search import primes_upto, prove_no_cheaper

def brute(n):
    ps=primes_upto(n); best=None; witness=None
    for choices in itertools.product(*[range(-1,p) for p in ps]):
        cov=set(); cost=Fraction(); w=[]
        for p,a in zip(ps,choices):
            if a>=0:
                cost+=Fraction(1,p); w.append([p,a])
                cov.update(x for x in range(1,n+1) if x%p==a)
        if len(cov)==n and (best is None or cost<best): best,witness=cost,w
    return best,witness

rows=[]
for n in range(1,11):
    best,w=brute(n)
    row={"N":n,"brute_cost":None if best is None else str(best)}
    if w is not None:
        result=prove_no_cheaper(n,w)
        assert not result["cheaper_cover_exists"]
        row["exact_search_cost"]=f'{result["witness_cost_numerator"]}/{result["witness_cost_denominator"]}'
    rows.append(row)
Path("logs").mkdir(parents=True, exist_ok=True)
Path("logs/small_n_crosscheck.json").write_text(json.dumps(rows,indent=2)+"\n")
print(json.dumps(rows,indent=2))
