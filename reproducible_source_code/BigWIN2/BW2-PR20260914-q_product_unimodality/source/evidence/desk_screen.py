"""Bounded exact outer desk screen; finite tests are not a theorem."""
from itertools import combinations_with_replacement
import hashlib, json, platform, time

def times_qnumber(p, a):
    out, window = [], 0
    for i in range(len(p)+a-1):
        if i < len(p): window += p[i]
        if 0 <= i-a < len(p): window -= p[i-a]
        out.append(window)
    return out

def product(aa, b, r):
    p=[1]
    for a in aa: p=times_qnumber(p,a)
    out=[]
    for i in range(len(p)+r*(b-1)):
        v=p[i] if i<len(p) else 0
        if i>=r: v+=out[i-r]
        if 0<=i-r*b<len(p): v-=p[i-r*b]
        out.append(v)
    return out

def predicted(aa,b,r):
    return any(a%r==0 for a in aa) or b<=1+sum(a//r for a in aa)

started=time.monotonic()
checks=0; failures=[]; signature=hashlib.sha256()
for k in range(1,4):
    for r in range(7,13):
        for aa in combinations_with_replacement(range(1,13),k):
            for b in range(1,9):
                p=product(aa,b,r)
                assert p==p[::-1]
                unimodal=all(p[i]>=p[i-1] for i in range(1,(len(p)-1)//2+1))
                expected=predicted(aa,b,r)
                checks+=1
                signature.update(json.dumps([aa,b,r,unimodal],separators=(',',':')).encode())
                if unimodal != expected:
                    failures.append(dict(a=aa,b=b,r=r,coefficients=p,unimodal=unimodal,condition=expected))
                    break
            if failures: break
        if failures: break
    if failures: break
calibration=[]
for aa,b,r in [([3,3,3,3],2,4),([3,5],4,2),([3],3,2)]:
    p=product(aa,b,r)
    # independent naive multiplication
    other=[1]
    for factor in [[1]*a for a in aa]+[[int(i%r==0) for i in range(r*(b-1)+1)]]:
        result=[0]*(len(other)+len(factor)-1)
        for i,x in enumerate(other):
            for j,y in enumerate(factor): result[i+j]+=x*y
        other=result
    assert p==other
    calibration.append(dict(a=aa,b=b,r=r,coefficients=p,unimodal=all(p[i]>=p[i-1] for i in range(1,(len(p)-1)//2+1)),condition=predicted(aa,b,r)))
print(json.dumps(dict(python=platform.python_version(),domain="exact integer coefficients",seed=None,
   scope="All k=1..3, r=7..12, sorted a_i=1..12, b=1..8 unless stopped on first failure",
   checks=checks,completed_grid=not failures,failures=failures,signature=signature.hexdigest(),
   calibration=calibration,elapsed_seconds=time.monotonic()-started,
   qualification="No universal proof or new conjecture claimed; adjacent extension of source finite checks"),indent=2))
