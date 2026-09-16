#!/usr/bin/env python3
"""Complete exact verification at one fixed order, standard library only.

Interpolate the a,n coefficient polynomials on a complete triangular grid.
At each point calculate the full determinant as an integer polynomial in z,
after clearing each row's rational denominators. This checks every base
coefficient, not random or floating-point evaluations.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial, lcm
from pathlib import Path
import hashlib
import json
import time


def fall(v,k):
    ans=1
    for h in range(k):ans*=v-h
    return ans


def linear_times(poly,linear):
    out=defaultdict(int)
    for m,c in poly.items():
        for index,coef in enumerate(linear):
            if coef:
                mm=list(m);mm[index]+=1
                out[tuple(mm)]+=c*coef
    return {m:c for m,c in out.items() if c}


def polymul(p,q):
    out=defaultdict(F)
    for m,c in p.items():
        for mm,cc in q.items():out[tuple(a+b for a,b in zip(m,mm))]+=c*cc
    return {m:c for m,c in out.items() if c}


def detpoly(matrix,k):
    minors={0:{(0,)*k:1}}
    for size in range(1,k+1):
        for mask in range(1,1<<k):
            cols=[col for col in range(k) if mask>>col&1]
            if len(cols)!=size:continue
            out=defaultdict(int)
            for pos,col in enumerate(cols):
                sign=(-1)**(size-1+pos)
                for m,c in linear_times(minors[mask^(1<<col)],matrix[size-1][col]).items():
                    out[m]+=sign*c
            minors[mask]={m:c for m,c in out.items() if c}
    return minors[(1<<k)-1]


def main():
    parser=argparse.ArgumentParser();parser.add_argument('order',type=int)
    k=parser.parse_args().order
    start=time.monotonic()
    path=Path('evidence/research_flag_order_'+str(k)+'.json')
    data=json.loads(path.read_text());assert data['order']==k
    bound=k*(k+1)//2
    groups=defaultdict(dict)
    seen=set()
    for m,c in data['coefficients']:
        m=tuple(m);c=F(c)
        assert m not in seen;seen.add(m)
        assert len(m)==k+2 and all(v>=0 for v in m)
        assert sum(m[:2])<=bound and sum(m[2:])==k
        assert c>0
        groups[m[2:]][m[:2]]=c
    # Exact common denominators speed up the claimed-value evaluations.
    packed={}
    for m,poly in groups.items():
        den=lcm(*(c.denominator for c in poly.values()))
        packed[m]=(den,[(p,q,int(c*den)) for (p,q),c in poly.items()])
    # Derive the row polynomials from e^(-zy)*(1-e^(-z(x+y)))^l,
    # independently of the producer's Stirling expansion.
    row={}
    for r in range(1,k+1):
        for ell in range(1,r+1):
            row[r,ell]=[(p,r-p,F((-1)**r*comb(r,p)
                                  *sum((-1)**h*comb(ell,h)*h**p*(h+1)**(r-p)
                                       for h in range(ell+1)),factorial(r)))
                        for p in range(r+1)]
    points=0
    for av in range(bound+1):
        for nv in range(bound-av+1):
            matrix=[];scale=1
            for r in range(1,k+1):
                rrow=[]
                for shift in range(1-k,1):
                    linear=[F(0)]*k
                    for ell in range(1,r+1):
                        coef=ell**k*F(ell,ell+1)**shift*sum(
                            c*fall(av+k+shift,p)*fall(nv-shift,q)/ell**p/(ell+1)**q
                            for p,q,c in row[r,ell])
                        for h in range(ell):linear[h]+=coef
                    rrow.append(linear)
                den=lcm(*(coef.denominator for ent in rrow for coef in ent))
                matrix.append([[int(coef*den) for coef in ent] for ent in rrow])
                scale*=den
            actual=detpoly(matrix,k)
            aa=[av**p for p in range(bound+1)];nn=[nv**p for p in range(bound+1)]
            expected={}
            for m,(den,poly) in packed.items():
                num=sum(c*aa[p]*nn[q] for p,q,c in poly)*scale
                assert num%den==0
                if num:expected[m]=num//den
            assert actual==expected, (k,av,nv)
            points+=1
        if av%3==0:print('k',k,'a',av,'points',points,'seconds',round(time.monotonic()-start,2),flush=True)
    assert points==(bound+1)*(bound+2)//2
    # Check the universal constant-component product, without SymPy.
    stir=[[0]*(k+1) for _ in range(k+1)];stir[0][0]=1
    const={(0,)*k:1}
    for r in range(1,k+1):
        for ell in range(1,r+1):stir[r][ell]=stir[r-1][ell-1]+ell*stir[r-1][ell]
        lin=[sum(factorial(ell)*stir[r][ell] for ell in range(h+1,r+1)) for h in range(k)]
        const=linear_times(const,lin)
    assert const=={m:poly.get((0,0),F(0)) for m,poly in groups.items()}
    top={(0,)*(k+2):F(1)}
    for ell in range(1,k+1):
        factor={}
        for p in range(ell+1):
            for h in range(ell):
                mon=[p,ell-p]+[0]*k;mon[h+2]=1
                factor[tuple(mon)]=F(factorial(ell)*comb(ell,p),ell**p*(ell+1)**(ell-p))
        top=polymul(top,factor)
    expected_top={(p,q)+m:c for m,poly in groups.items() for (p,q),c in poly.items() if p+q==bound}
    assert top==expected_top
    out={'job_id':data['job_id'],'order':k,'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'arithmetic':'standard-library integers and Fraction',
         'a_n_total_degree_bound':bound,'complete_triangular_grid_points':points,
         'full_base_polynomial_identity_at_every_grid_point':True,
         'positive_coefficient_count':len(seen),'base_monomial_count':len(groups),
         'constant_component_product_checked':True,
         'highest_a_n_degree_component_product_checked':True,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'complete polynomial identity verification at this order; not a fresh referee'}
    dest=Path('evidence/verify_flag_order_'+str(k)+'.json');tmp=dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(dest)
    print(json.dumps(out))


if __name__=='__main__':main()
