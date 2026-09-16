#!/usr/bin/env python3
"""Exact intake calibration of Brugidou v7 equations (3.10), (3.20).
No claim of novelty or universal proof; the primary reports tests through size43.
"""
from functools import lru_cache
from fractions import Fraction
from collections import Counter
from math import comb, factorial
import hashlib,json,platform,time
from pathlib import Path
START=time.perf_counter()
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return tuple(p)
def add(p,q,f=1):
    z=list(p)+(max(0,len(q)-len(p))*[0])
    for i,v in enumerate(q): z[i]+=f*v
    return trim(z)
def mul(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j]+=a*b
    return trim(z)
@lru_cache(None)
def parts(n,m=None):
    if n==0:return ((),)
    m=n if m is None else min(m,n)
    return tuple((a,)+b for a in range(m,0,-1) for b in parts(n-a,a))
def mf(lam):
    ans=1
    for v in Counter(lam).values():ans*=factorial(v)
    return ans
@lru_cache(None)
def F(lam):
    # F_lambda=(n-1)! M_lambda=q^n(lambda) J_lambda.
    n=sum(lam)
    if lam==(1,): return (1,)
    if len(lam)==1:
        out=(Fraction(0),)
        for mu in parts(n-1): out=add(out,F(mu),Fraction(n-1,mf(mu)))
        assert all(x.denominator==1 for x in out)
        return tuple(int(x) for x in out)
    a=lam[-1]; rest=lam[:-1]
    out=tuple((n-1)*comb(n-2,a-1)*x for x in mul(F((a,)),F(rest)))
    for i in range(len(rest)):
        merged=list(rest);merged[i]+=a;merged=tuple(sorted(merged,reverse=True))
        out=add(out,mul((-1,1),F(merged)))
    return trim(out)
def J(lam):
    f=F(lam);v=sum(i*a for i,a in enumerate(lam))
    assert all(x==0 for x in f[:v])
    ans=f[v:]
    assert len(ans)-1==(sum(lam)-1)*(sum(lam)-2)//2+len(lam)-1-v
    assert ans[0]!=0
    return ans
MAX_N=12
rows=[];failures=[];ineq=0;coeffs=0
for n in range(1,MAX_N+1):
    for lam in parts(n):
        a=J(lam);coeffs+=len(a)
        if not all(x>0 for x in a):failures.append({"partition":lam,"kind":"positivity","coefficients":a})
        for k in range(1,len(a)-1):
            ineq+=1
            if a[k]*a[k]<a[k-1]*a[k+1]:
                failures.append({"partition":lam,"kind":"logconcavity","index":k,"coefficients":a})
        rows.append({"partition":lam,"coefficients":a})
expected={(1,):(1,),(2,):(1,),(1,1):(1,),(3,):(2,1),(2,1):(1,1),(1,1,1):(2,),(4,):(6,6,3,1),(3,1):(3,3,2,1),(2,2):(3,2,1),(2,1,1):(2,2,2),(1,1,1,1):(6,),(3,2,1):(10,30,35,35,30,20,12,6,2)}
for lam,a in expected.items():assert J(lam)==a,(lam,J(lam),a)
# Independent defining specialization for all n<=6: Newton power sums
# and augmented-monomial product recurrence, with exact rational arithmetic.
@lru_cache(None)
def power(n):
    out=tuple([Fraction(0)]*(n*(n-1)//2)+[Fraction((-1)**(n-1),factorial(n-1))])
    for j in range(1,n):
        e=[Fraction(0)]*((n-j)*(n-j-1)//2)+[Fraction(1,factorial(n-j))]
        out=add(out,mul(e,power(j)),(-1)**(n-j-1))
    return out
@lru_cache(None)
def mono(lam):
    if len(lam)==1:return power(lam[0])
    a=lam[-1];rest=lam[:-1];out=mul(power(a),mono(rest))
    for i in range(len(rest)):
        merged=list(rest);merged[i]+=a
        out=add(out,mono(tuple(sorted(merged,reverse=True))),-1)
    return out
independent=0
for n in range(1,7):
    for lam in parts(n):
        lhs=tuple(factorial(n-1)*x for x in mono(lam))
        factor=(1,)
        for _ in range(n-len(lam)):factor=mul(factor,(1,-1))
        assert trim(lhs)==mul(factor,F(lam)),lam
        independent+=1
record={"schema":1,"python":platform.python_version(),"arithmetic":"exact integers and fractions.Fraction","randomness":False,"source":"https://arxiv.org/html/2306.15300v7","max_size":MAX_N,"partitions":len(rows),"coefficients":coeffs,"logconcavity_inequalities":ineq,"source_examples":len(expected),"independent_definition_checks_n_max":6,"independent_definition_checks":independent,"failures":failures,"wall_seconds":time.perf_counter()-START,"qualification":"Calibration only, no universal proof or novelty; source v7 already reports all partitions through size43.","script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"rows":rows}
Path(__file__).with_suffix(".json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:v for k,v in record.items() if k!="rows"}))
