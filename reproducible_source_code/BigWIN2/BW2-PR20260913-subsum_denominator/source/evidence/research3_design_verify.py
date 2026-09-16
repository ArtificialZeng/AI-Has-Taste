"""Recheck inherited K_sharp_v1 design data and all earlier base cases.

Uses the pass-3 independent logarithmic-derivative implementation. The
historical certificate is read-only. No new held-out credit is assigned.
"""
import hashlib
import json
from math import comb
from pathlib import Path
from time import monotonic
from research3_verify import coefficients, margin_vector

ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-077128f18f2f'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def base(n):
    a=[1]
    for i in range(1,n+1):
        v=i
        while v<=n:
            a=a+[0]*i
            for j in range(len(a)-1,i-1,-1):
                a[j]+=a[j-i]
            v*=2
    minors=[a[j]**2-a[j-1]*a[j+1] for j in range(1,len(a)-1)]
    assert all(x>=0 for x in minors)
    return dict(n=n,degree=len(a)-1,coefficients=a,internal_minors=minors)

def main():
    start=monotonic()
    path=ROOT/'evidence/research2_sharp_probe.json'
    d=json.loads(path.read_text())
    assert d['edge_bound']==64 and d['kernel_version']=='K_sharp_v1'
    expected={(s,j) for j in range(65) for s in range(1,j+2)}
    assert len(d['records'])==len(expected)
    assert {(r['s'],r['j']) for r in d['records']}==expected
    cache={}
    def vector(s,t):
        if (s,t) not in cache:
            cache[s,t]=margin_vector(s,t,64)
        return cache[s,t]
    weights=[[(-1)**(h-v)*comb(h,v) for v in range(h+1)] for h in range(129)]
    count=0
    finite=[]
    for r in d['records']:
        s,j,tau=r['s'],r['j'],r['t0']
        assert s*2**tau>=9 and 2*s*2**tau>j+1
        assert tau==0 or s*2**(tau-1)<9 or 2*s*2**(tau-1)<=j+1
        c=r['newton_coefficients']
        assert len(c)==2*j+1
        vals=[vector(s,tau+v)[j] for v in range(2*j+1)]
        for h,x in enumerate(c):
            assert x==sum(w*vals[v] for v,w in enumerate(weights[h]))>=0
            count+=1
        for t in range(tau):
            if s*2**t>=9:
                value=vector(s,t)[j]
                assert value>=0
                finite.append(dict(s=s,j=j,t=t,n=s*2**t,margin=value))
    out=dict(job_id=JOB,complete_domain=True,
        certificate_sha256=sha(path),implementation_sha256=sha(Path(__file__)),
        dependency_sha256=sha(ROOT/'evidence/research3_verify.py'),
        inherited_polynomials=len(expected),inherited_coefficients_recomputed=count,
        earlier_finite_checks=len(finite),earlier_finite_records=finite,
        sparse_product_bases=[base(n) for n in (1,2,4,8)],
        elapsed_seconds=round(monotonic()-start,3),
        scope='Verification of inherited design evidence; not newly held-out data')
    dest=ROOT/'evidence/research3_design_verify.json'
    tmp=dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(dest)
    print(json.dumps({k:v for k,v in out.items() if k not in ['earlier_finite_records','sparse_product_bases']},indent=2))

if __name__=='__main__':
    main()
