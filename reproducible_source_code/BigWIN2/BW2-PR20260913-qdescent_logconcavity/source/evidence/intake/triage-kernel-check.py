"""Exact triage verification; no uniform proof and no independent referee."""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import permutations, combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location('intake', HERE/'qdescent-calibration.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

def subtract(a,b):
    return c.add(a, tuple(-x for x in b))

def kernel(m,k,r):
    if not 1 <= k <= m:
        return ()
    return c.shift(subtract(c.gaussian(m,k),c.gaussian(m-r,k)),k*k)

def prefix_row(T,m):
    row=[(1,)]
    for n in range(2,m+1):
        new=[]
        for r in range(1,n+1):
            inds=range(r-1,n-1) if n-1 in T else range(r-1)
            z=()
            for h in inds:
                z=c.add(z,row[h])
            new.append(c.shift(z,n-r))
        row=new
    return row

def as_tuple(count):
    return tuple(count.get(i,0) for i in range(max(count,default=-1)+1))

def verify_definitions():
    db=defaultdict(Counter)
    da=defaultdict(Counter)
    visited=0
    for n in range(1,9):
        for p in permutations(range(1,n+1)):
            visited+=1
            S=tuple(i for i in range(1,n) if p[i-1]>p[i])
            inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
            if n<=7:
                db[(n,S,p[-1])][inv]+=1
            if S:
                m=max(S); k=n-m
                if m<=4 and 1<=k<=m and set(range(m+1,n+1))<=set(p[:m]):
                    da[(S,k)][inv]+=1
    bchecks=achecks=0
    for m in range(1,8):
        for mask in range(1<<(m-1)):
            T={i+1 for i in range(m-1) if mask>>i&1}
            row=prefix_row(T,m)
            for r in range(1,m+1):
                assert row[r-1]==as_tuple(db[(m,tuple(sorted(T)),r)])
                bchecks+=1
    for m in range(1,5):
        for mask in range(1<<(m-1)):
            S={m}|{i+1 for i in range(m-1) if mask>>i&1}
            x=prefix_row(S-{m},m)
            old=c.a_polys(S,m)
            for k in range(1,m+1):
                z=()
                for r in range(1,m+1):
                    z=c.add(z,c.mul(kernel(m,k,r),x[r-1]))
                assert z==old[k]==as_tuple(da[(tuple(sorted(S)),k)])
                achecks+=1
    gchecks=0
    for n in range(9):
        for k in range(n+1):
            counts=Counter(sum(t)-k*(k-1)//2 for t in combinations(range(n),k))
            assert c.gaussian(n,k)==as_tuple(counts)
            gchecks+=1
    return dict(permutations_enumerated=visited,
                prefix_last_value_checks=bchecks,prefix_range='all T subset [m-1], m=1..7, every r=1..m',
                direct_a_checks=achecks,direct_a_range='all nonempty S with max S <=4, every k=1..max S',
                gaussian_subset_checks=gchecks,gaussian_range='all 0<=k<=n<=8')

def test_kernels(ms):
    rows=[]
    for m in ms:
        K=[[kernel(m,k,r) for r in range(1,m+1)] for k in range(m+2)]
        for k in range(1,m+1):
            for r in range(1,m+1):
                z=()
                for h in range(1,min(r,m-k+1)+1):
                    z=c.add(z,c.shift(c.gaussian(m-h,k-1),k*(k-1)+m+1-h))
                assert z==K[k][r-1] and z and min(z)>=0
        checks={'strict':0,'diagonal':0}; failures=[]
        for i in range(1,m+1):
            for j in range(i,m+1):
                for r in range(m):
                    for s in range(r,m):
                        z=subtract(c.mul(K[i][r],K[j][s]),c.mul(K[i-1][r],K[j+1][s]))
                        if r!=s:
                            z=c.add(z,subtract(c.mul(K[i][s],K[j][r]),c.mul(K[i-1][s],K[j+1][r])))
                        neg=[(e,v) for e,v in enumerate(z) if v<0]
                        checks['diagonal' if i==j else 'strict']+=1
                        if neg:
                            failures.append(dict(i=i,j=j,r=r+1,s=s+1,negative=neg))
        rows.append(dict(m=m,checks=checks,failures=failures))
    return rows

def main():
    started=time.monotonic()
    frozen=HERE/'triage-kernel-reduction.md'
    out=dict(job_id='primary-20260913-qdescent-logconcavity-triage-178cb0fc6742',
             arithmetic='exact integer polynomial arrays; no floating-point mathematics',
             shared_code='polynomial arithmetic and q-Pascal Gaussian routine imported from prior calibration; direct enumeration is separate',
             source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             frozen_target_sha256=hashlib.sha256(frozen.read_bytes()).hexdigest(),
             definitions=verify_definitions())
    out['discovery_replay']=test_kernels(range(1,9))
    out['holdout']=test_kernels(range(9,13))
    out['seconds']=time.monotonic()-started
    out['conclusion']='Finite exact observations only. Target K remains unproved; a failure need not refute descent-derived a.'
    (HERE/'triage-kernel-check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':
    main()
