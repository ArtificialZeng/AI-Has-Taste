#!/usr/bin/env python3
"""Fail-closed independent verifier for finite_two_generator_certificate.json.

Unlike the producer's BFS by positive words, this checker obtains closure by
repeatedly adjoining inverses and all pairwise products. It independently
enumerates every ordered pair for cases marked exhaustive and compares the
complete subgroup-order histogram.
"""
import hashlib, itertools, json, platform, sys
from collections import Counter
from math import factorial
from pathlib import Path

def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    r=[0]*len(p)
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
def signbit(p):
    # independent cycle-count formula
    seen=set(); cycles=0
    for i in range(len(p)):
        if i not in seen:
            cycles+=1; j=i
            while j not in seen: seen.add(j); j=p[j]
    return (len(p)-cycles)&1
def mul(x,y): return comp(x[0],y[0]),comp(x[1],y[1])
def inverse(x): return inv(x[0]),inv(x[1])
def universe(m,n):
    return {(p,q) for p in itertools.permutations(range(m))
                  for q in itertools.permutations(range(n)) if signbit(p)==signbit(q)}
def closure(a,b,e):
    # Symmetric Cayley-graph traversal (producer uses only positive generators
    # and returns only an order, not the full set).
    gens=(a,b,inverse(a),inverse(b)); s={e}; todo=[e]
    while todo:
        x=todo.pop()
        for g in gens:
            y=mul(g,x)
            if y not in s: s.add(y); todo.append(y)
    return s
def decode(z,m,n):
    if not isinstance(z,list) or len(z)!=2: raise ValueError("bad pair encoding")
    p=tuple(i-1 for i in z[0]); q=tuple(i-1 for i in z[1])
    if sorted(p)!=list(range(m)) or sorted(q)!=list(range(n)): raise ValueError("not permutations")
    if signbit(p)!=signbit(q): raise ValueError("not in fibre product")
    return p,q
def main():
    path=Path(sys.argv[1] if len(sys.argv)>1 else "certificates/finite_two_generator_certificate.json")
    raw=path.read_bytes(); d=json.loads(raw)
    if d.get("format")!="parity-fibre-product-finite-v1": raise ValueError("bad format")
    required={(3,3),(4,3),(4,4)}; seen=set()
    reports=[]
    for c in d.get("cases",[]):
        m,n=c["m"],c["n"]; U=universe(m,n); N=len(U); e=(tuple(range(m)),tuple(range(n)))
        if N!=c["group_order"] or N!=factorial(m)*factorial(n)//2: raise AssertionError("group order")
        wit=c.get("witness")
        if wit is not None:
            a,b=(decode(wit[0],m,n),decode(wit[1],m,n))
            if closure(a,b,e)!=U: raise AssertionError(f"invalid witness {(m,n)}")
        if c.get("exhaustive"):
            seen.add((m,n)); hist=Counter(len(closure(a,b,e)) for a in U for b in U)
            claimed={int(k):v for k,v in c["generated_order_histogram"].items()}
            if hist!=claimed or sum(hist.values())!=N*N or c["ordered_pairs_checked"]!=N*N: raise AssertionError("histogram")
            if max(hist)!=c["max_generated_order"]: raise AssertionError("maximum")
            if wit is None and max(hist)==N: raise AssertionError("missing witness despite generating pair")
            reports.append(f"({m},{n}) exhaustive pairs={N*N} max={max(hist)}/{N}")
        else: reports.append(f"({m},{n}) witness verified order={N}")
    if not required <= seen: raise AssertionError("required exceptional cases absent")
    codehash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    inhash=hashlib.sha256(raw).hexdigest()
    print("VERIFIED parity-fibre-product-finite-v1")
    print("input_sha256="+inhash); print("verifier_sha256="+codehash)
    print("python="+platform.python_version()+" "+platform.python_implementation())
    print("; ".join(reports))
if __name__=="__main__": main()
