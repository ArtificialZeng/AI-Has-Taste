"""Independent checks of the sparse large-j attack and boundary obstruction.

Large-j certificates: h=0..4, top two formulas and two outside-grid values.
This does NOT independently recompute their middle Newton coefficients.
Excluded-boundary family: every stage for 9<=n<=32, actual high differences.
"""
import hashlib
import json
from math import comb
from pathlib import Path
from time import monotonic
from research3_verify import coefficients, margin_vector

ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-077128f18f2f'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    start=monotonic()
    p=ROOT/'evidence/research3_boundary_probe.json'
    d=json.loads(p.read_text())
    assert d['complete'] and not d['negative_coefficients']
    js=[126,127,128,129,190,191,192,193,254,255,256,257,510,511,512,513]
    expected={(s,j) for j in js for s in {1,2,3,(j+1)//2,(j+1)//2+1,j-1,j,j+1}}
    assert len(d['records'])==len(expected)
    assert {(r['s'],r['j']) for r in d['records']}==expected
    low=top=evaluations=0
    for r in d['records']:
        s,j,tau=r['s'],r['j'],r['tau']
        assert s*2**tau>=9 and 2*s*2**tau>j+1
        assert tau==0 or s*2**(tau-1)<9 or 2*s*2**(tau-1)<=j+1
        c=r['newton_coefficients']
        assert len(c)==2*j+1 and all(x>=0 for x in c)
        vals=[margin_vector(s,tau+v,j)[j] for v in range(5)]
        for h in range(5):
            assert c[h]==sum((-1)**(h-v)*comb(h,v)*vals[v] for v in range(h+1))
            low+=1
        C=comb(2*j,j)//(j+1)
        Cp=comb(2*j-2,j-1)//j
        a1=coefficients(s,tau,1)[1]
        assert c[-1]==C
        assert c[-2]==(a1+2*(s==1))*C+(2*j-1)*(C-Cp)
        top+=2
        for u in (2*j+3,4*j+7):
            actual=margin_vector(s,tau+u,j)[j]
            assert actual==sum(x*comb(u,h) for h,x in enumerate(c))
            evaluations+=1
    witnesses=[]
    for n in range(9,33):
        s=n
        t=0
        while True:
            j=2*n-1
            a=coefficients(s,t,j+1)
            delta=-a[2*n-2]-2*a[2*n-s-2]
            assert delta<0
            order=4*n
            vals=[margin_vector(s,t+v,j)[j] for v in range(order+1)]
            actual=sum((-1)**(order-v)*comb(order,v)*vals[v] for v in range(order+1))
            assert actual==delta
            # Extrapolate polynomial tail of degree <=2j to u=0.
            tail=vals[1:2*j+2]
            c=[]
            while tail:
                c.append(tail[0])
                tail=[b-a for a,b in zip(tail,tail[1:])]
            extrap=sum((-1)**h*x for h,x in enumerate(c))
            assert vals[0]-extrap==delta
            witnesses.append(dict(n=n,s=s,t=t,j=j,actual_H_margin=vals[0],
                polynomial_extrapolation=extrap,discrepancy=delta,
                difference_order=order,actual_forward_difference=actual))
            if s%2:
                break
            s//=2
            t+=1
    out=dict(job_id=JOB,certificate_sha256=sha(p),
        implementation_sha256=sha(Path(__file__)),
        dependency_sha256=sha(ROOT/'evidence/research3_verify.py'),
        complete_sparse_domain=True,large_polynomials=len(expected),
        low_order_coefficients_recomputed=low,top_formula_checks=top,
        outside_grid_evaluations=evaluations,
        limitation='Middle Newton orders in the large-j sparse attack not separately recomputed',
        excluded_boundary_n_range=[9,32],excluded_boundary_witnesses=witnesses,
        elapsed_seconds=round(monotonic()-start,3))
    dest=ROOT/'evidence/research3_boundary_verify.json'
    tmp=dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(dest)
    print(json.dumps({k:v for k,v in out.items() if k!='excluded_boundary_witnesses'},indent=2))

if __name__=='__main__':
    main()
