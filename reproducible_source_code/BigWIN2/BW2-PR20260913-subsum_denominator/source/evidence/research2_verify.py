"""Independent exact verification of frozen K through 64 and earlier cases.
Uses logarithmic-derivative recurrence and explicit signed binomial sums.
No import of the producer's coefficient or forward-difference functions.
"""
import json, hashlib
from pathlib import Path
from math import comb
from time import monotonic
ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-983c87564404'

def coefficients(n,s,m):
    earlier=set()
    k=s
    while k%2==0:
        k//=2
        earlier.add(k)
    beta=[0]*(m+1)
    for i in range(1,m+1):
        e=int(i in earlier)
        v=i
        while v<n:
            e+=1
            v*=2
        for v in range(i,m+1,i):
            beta[v]+=e*i*(1 if (v//i)%2 else -1)
    a=[1]
    for k in range(1,m+1):
        v=sum(beta[r]*a[k-r] for r in range(1,k+1))
        q,rem=divmod(v,k)
        assert rem==0
        a.append(q)
    return a

def get(a,j):
    return a[j] if 0<=j<len(a) else 0

def minor(a,j):
    return get(a,j)**2-get(a,j-1)*get(a,j+1)

def margins(s,t,B):
    a=coefficients(s*2**t,s,B+1)
    b=[get(a,j)+get(a,j-s) for j in range(B+2)]
    return [2*minor(b,j)-minor(a,j)-minor(a,j-s) for j in range(B+1)]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    start=monotonic()
    p=ROOT/'evidence/research2_kernel_probe.json'
    data=json.loads(p.read_text())
    B=data['edge_bound']
    assert B==64 and not data['negative_coefficients']
    expected={(s,j) for j in range(B+1) for s in range(1,j+2)}
    assert len(data['records'])==len(expected)
    assert {(r['s'],r['j']) for r in data['records']}==expected
    old=json.loads((ROOT/'evidence/research_kernel_probe.json').read_text())
    oldmap={(r['s'],r['j']):r for r in old['records']}
    cache={}
    def vector(s,t):
        if (s,t) not in cache:
            cache[s,t]=margins(s,t,B)
        return cache[s,t]
    count=heldcount=heldpolys=0
    finite=[]
    toprows=0
    for r in data['records']:
        s,j,t0=r['s'],r['j'],r['t0']
        assert s*2**t0>=max(9,j+1)
        assert t0==0 or s*2**(t0-1)<max(9,j+1)
        if j<=32:
            assert r==oldmap[s,j]
        else:
            heldpolys+=1
        c=r['newton_coefficients']
        assert len(c)==2*j+1
        vals=[vector(s,t0+v)[j] for v in range(2*j+1)]
        for h,x in enumerate(c):
            actual=sum((-1)**(h-v)*comb(h,v)*vals[v] for v in range(h+1))
            assert x==actual>=0,(s,j,h)
            count+=1
            heldcount+=j>=33
        # Proved top two formulas from the bivariate identity.
        catalan=comb(2*j,j)//(j+1)
        assert c[-1]==catalan
        toprows+=1
        if j>=1:
            e1=coefficients(s*2**t0,s,1)[1]
            previous=comb(2*j-2,j-1)//j
            expected_second=(e1+2*(s==1))*catalan+(2*j-1)*(catalan-previous)
            assert c[-2]==expected_second,(s,j)
            toprows+=1
        for t in range(t0):
            if s*2**t>=9:
                v=vector(s,t)[j]
                assert v>=0
                finite.append(dict(s=s,j=j,t=t,n=s*2**t,margin=v))
    assert count==data['newton_coefficients']
    out=dict(job_id=JOB,arithmetic='Python arbitrary precision integers; exact divisions',
        certificate_sha256=sha(p),script_sha256=sha(Path(__file__)),
        source_sha256=sha(ROOT/'source.md'),complete_domain=True,
        polynomials=len(expected),coefficients_recomputed=count,
        held_out_polynomials=heldpolys,held_out_coefficients=heldcount,
        pass1_certificate_unchanged=True,top_two_formula_checks=toprows,
        earlier_finite_checks=len(finite),earlier_finite_records=finite,
        elapsed_seconds=round(monotonic()-start,3))
    outpath=ROOT/'evidence/research2_verify.json'
    tmp=outpath.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(outpath)
    print(json.dumps({k:v for k,v in out.items() if k!='earlier_finite_records'},indent=2))

if __name__=='__main__':
    main()
