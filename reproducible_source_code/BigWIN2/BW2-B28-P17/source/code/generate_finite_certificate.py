#!/usr/bin/env python3
"""Generate an exact finite two-generator certificate for parity fibre products.

Discovery/certificate producer.  Uses BFS in the directed Cayley graph with
the two generators; in a finite group, the generated monoid is the subgroup.
"""
import itertools, json, platform, sys, time
from collections import Counter, deque
from math import factorial
from pathlib import Path

def compose(p, q):
    """p after q, permutations stored as zero-based image tuples."""
    return tuple(p[q[i]] for i in range(len(p)))

def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p))) % 2

def elements(m, n):
    ps=list(itertools.permutations(range(m))); qs=list(itertools.permutations(range(n)))
    return [(p,q) for p in ps for q in qs if parity(p)==parity(q)]

def mul(x,y): return compose(x[0],y[0]), compose(x[1],y[1])

def generated_order(a,b,identity, target=None):
    seen={identity}; todo=deque([identity])
    while todo:
        x=todo.popleft()
        for g in (a,b):
            y=mul(x,g)
            if y not in seen:
                seen.add(y); todo.append(y)
                if target is not None and len(seen)==target: return target
    return len(seen)

def encode(x): return [[i+1 for i in x[0]],[i+1 for i in x[1]]]

def run_case(m,n, exhaustive):
    es=elements(m,n); ident=(tuple(range(m)),tuple(range(n))); N=len(es)
    assert N == factorial(m)*factorial(n)//2
    witness=None; histogram=Counter()
    for i,a in enumerate(es):
        for b in es:
            o=generated_order(a,b,ident,N)
            if exhaustive: histogram[o]+=1
            if o==N and witness is None: witness=[encode(a),encode(b)]
        if witness is not None and not exhaustive: break
    out={"m":m,"n":n,"group_order":N,"exhaustive":exhaustive,"witness":witness}
    if exhaustive:
        out["ordered_pairs_checked"]=N*N
        out["generated_order_histogram"]={str(k):histogram[k] for k in sorted(histogram)}
        out["max_generated_order"]=max(histogram)
    return out

def main():
    started=time.time()
    # Claimed exceptional cases: complete enumeration.  Nearby cases: exact witnesses.
    specs=[(3,3,True),(4,3,True),(4,4,True),(2,2,False),(3,2,False),(4,2,False),(5,2,False),(5,3,False),(5,4,False)]
    cert={"format":"parity-fibre-product-finite-v1",
          "encoding":"one-based image lists; product p*q means p after q",
          "producer":{"python":platform.python_version(),"implementation":platform.python_implementation()},
          "cases":[run_case(*s) for s in specs]}
    cert["elapsed_seconds_diagnostic"]=round(time.time()-started,6)
    path=Path("certificates/finite_two_generator_certificate.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(f"wrote {path}; cases={len(cert['cases'])}; elapsed={cert['elapsed_seconds_diagnostic']}s")

if __name__=="__main__": main()
