"""Sharp-start Newton kernel K_sharp, version 1.
Translate the frozen K polynomial one step earlier when 2*n>j+1 permits.
Independently recompute with the logarithmic-derivative coefficient recurrence.
Also certify the obstruction at the excluded boundary 2*n=j+1.
"""
import json,hashlib
from pathlib import Path
from math import comb
from time import monotonic
from research2_verify import margins,coefficients
ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-983c87564404'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    start=monotonic()
    parent=ROOT/'evidence/research2_kernel_probe.json'
    data=json.loads(parent.read_text())
    B=data['edge_bound']
    records=[]
    negatives=[]
    changed=changed_coefficients=recomputed=0
    cache={}
    def vector(s,t):
        if (s,t) not in cache: cache[s,t]=margins(s,t,B)
        return cache[s,t]
    for old in data['records']:
        s,j=old['s'],old['j']
        t0=0
        while (s<<t0)<9 or 2*(s<<t0)<=j+1: t0+=1
        assert old['t0']-t0 in (0,1)
        c=list(old['newton_coefficients'])
        if old['t0']!=t0:
            changed+=1
            changed_coefficients+=len(c)
            # Newton translation P(u-1); exact polynomial identity.
            for h in range(len(c)-2,-1,-1): c[h]-=c[h+1]
            vals=[vector(s,t0+v)[j] for v in range(2*j+1)]
            for h,x in enumerate(c):
                actual=sum((-1)**(h-v)*comb(h,v)*vals[v] for v in range(h+1))
                assert x==actual,(s,j,h)
                recomputed+=1
        for h,x in enumerate(c):
            if x<0: negatives.append(dict(s=s,j=j,t0=t0,h=h,value=x))
        records.append(dict(s=s,j=j,t0=t0,newton_coefficients=c))
    # Earliest excluded threshold: n=9, j+1=18=2*n.
    s,j=9,17
    old=next(r for r in records if r['s']==s and r['j']==j)
    assert old['t0']==1
    tail_extrapolation=sum((-1)**h*x for h,x in enumerate(old['newton_coefficients']))
    actual=vector(s,0)[j]
    a=coefficients(9,9,18)
    delta=actual-tail_extrapolation
    assert delta==-a[16]-2*a[7]<0
    order=36
    direct=sum((-1)**(order-v)*comb(order,v)*vector(s,v)[j] for v in range(order+1))
    assert direct==delta
    out=dict(job_id=JOB,kernel_version='K_sharp_v1',edge_bound=B,
        scope='Design range j<=64 at least n>=9 with 2*n>j+1; not held-out support',
        parent_certificate_sha256=sha(parent),implementation_sha256=sha(Path(__file__)),
        polynomials=len(records),newton_coefficients=sum(len(r['newton_coefficients']) for r in records),
        translated_polynomials=changed,translated_coefficients=changed_coefficients,
        independent_translated_coefficients_recomputed=recomputed,
        negative_coefficients=negatives,records=records,
        excluded_boundary_witness=dict(s=s,n=9,j=j,tail_start_t=1,
            actual_margin=actual,polynomial_extrapolation=tail_extrapolation,
            discrepancy=delta,a_16=a[16],a_7=a[7],
            forward_difference_order=order,forward_difference=direct,
            scope='Failure of extending global Newton positivity/polynomiality below 2*n>j+1; not K_sharp, K, H, or original failure'),
        elapsed_seconds=round(monotonic()-start,3))
    path=ROOT/'evidence/research2_sharp_probe.json'
    tmp=path.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(path)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))

if __name__=='__main__': main()
