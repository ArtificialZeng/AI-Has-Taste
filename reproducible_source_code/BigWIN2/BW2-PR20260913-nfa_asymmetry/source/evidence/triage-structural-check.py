#!/usr/bin/env python3
"""Exact finite checks of two unary-relation lemmas, not an NFA census."""
import hashlib,json,math
from pathlib import Path

def mul(a,b,n):
    out=[]
    for row in a:
        val=0
        for j in range(n):
            if row>>j&1: val |= b[j]
        out.append(val)
    return tuple(out)

def power(a,k,n):
    out=tuple(1<<i for i in range(n))
    while k:
        if k&1: out=mul(out,a,n)
        a=mul(a,a,n); k//=2
    return out

results=[]
for n in range(1,5):
    H=(n-1)**2+1; L=math.lcm(*range(1,n+1))
    periodic_failures=0; transfer_failures=0; cyclic_count=0
    for code in range(1<<(n*n)):
        b=tuple((code>>(n*i))&((1<<n)-1) for i in range(n))
        if power(b,H,n)!=power(b,H+L,n): periodic_failures+=1
        # B^n is nonzero exactly when a directed n-edge walk exists,
        # which forces a cycle. Conversely any cycle gives such a walk.
        cyclic=any(power(b,n,n))
        if cyclic:
            cyclic_count+=1
            a=power(b,n-1,n); d=power(b,n-1+L,n)
            if any(x&~y for x,y in zip(a,d)): transfer_failures+=1
    results.append(dict(n=n,matrices=1<<(n*n),H=H,L=L,cyclic_matrices=cyclic_count,periodicity_failures=periodic_failures,cycle_transfer_failures=transfer_failures))
    print(results[-1],flush=True)
# Independently check arithmetic return-length characterization of Nicol's
# zero graph (s+1-cycle and an s-cycle sharing all vertices but state zero).
cycle_checks=[]
for s in range(2,13):
    n=s+1; b=[1<<(i+1) for i in range(s)]+[1 | (1<<1)]
    reach=1; failed=[]; last_rejected=None
    for length in range(0,4*s*s+1):
        expected=(length==0 or any((length-k*(s+1))>=0 and (length-k*(s+1))%s==0 for k in range(1,length//(s+1)+1)))
        actual=bool(reach&1)
        if actual!=expected: failed.append(length)
        if not actual: last_rejected=length
        nxt=0
        for i in range(n):
            if reach>>i&1: nxt |= b[i]
        reach=nxt
    cycle_checks.append(dict(s=s,checked_lengths=[0,4*s*s],failures=failed,last_rejected=last_rejected,expected_last=s*s))
report={'job_id':'primary-20260913-nfa-asymmetry-triage-46dc24ebd607','type':'exact finite observation; not proof beyond stated coverage','unary_matrices':results,'consecutive_cycle_checks':cycle_checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path('evidence/triage-structural-check.json').write_text(json.dumps(report,indent=2)+'\n')
assert all(r['periodicity_failures']==r['cycle_transfer_failures']==0 for r in results)
assert all(not r['failures'] and r['last_rejected']==r['expected_last'] for r in cycle_checks)
