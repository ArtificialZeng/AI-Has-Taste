#!/usr/bin/env python3
"""Exact symbolic and literal calculations for the third-position kernel.

Research pass 2; exploratory output is not by itself a positivity certificate.
"""
import json
from functools import lru_cache
from math import comb
from itertools import product
from pathlib import Path
import sympy as s
from research_boundary import low_coefficients

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-binary-subsum-shape-research-9e631dc6dcdd'
m,l,t = s.symbols('m l t')
u,b,c = s.symbols('u b c')

def F(r,z):
    if r==0: return z+1
    if r==1: return z*(z+1)/2
    if r==2: return z*(z+1)*(2*z+1)/6
    if r==3: return z**2*(z+1)**2/4
    if r==4: return z*(z+1)*(2*z+1)*(3*z*z+3*z-1)/30
    raise ValueError(r)

def moment(r,lo,hi):
    return s.expand(F(r,hi)-F(r,lo-1))

def tail(z,delta,epsilon,active):
    """p2,p3,p4 and a2,a3,a4 for w_k=1_(k>=z)."""
    q=(m-delta)/2
    v=[moment(r,z,m) for r in range(5)]
    p2=2*v[2]
    p3=s.Rational(4,3)*v[3]-v[2]+(2*m+s.Rational(5,3))*v[1]-(m*m+m)*v[0]
    even=(q-(z-epsilon)/2)*(q-(z-epsilon)/2+1-epsilon)
    h2=moment(2,z,q) if active else s.Integer(0)
    h3=moment(3,z,q) if active else s.Integer(0)
    p4=(s.Rational(2,3)*v[4]-2*v[3]+s.Rational(11,6)*v[2]-v[1]/2
        +z*(2*v[2]-v[1])+2*m*v[2]-2*v[3]
        +2*(m+1)*h2-4*h3+even)
    a2=2*m*m-m+z
    a3=(4*m**3+2*m)/3-2*m*(m-z)
    a4=(2*m)*(2*m-1)*(2*m-2)*(2*m-3)/24+(2*m*m-m)*z+2*h2
    return tuple(s.expand(v) for v in (p2,p3,p4,a2,a3,a4))

@lru_cache(None)
def kernel(delta,epsilon,eta,act_l,act_t):
    p2,p3,p4,a2,a3,a4=tail(l,delta,epsilon,act_l)
    q2,q3,q4,b2,b3,b4=tail(t,delta,eta,act_t)
    return s.expand(2*p3*q3-p2*q4-q2*p4-2*a3*b3+a2*b4+b2*a4)

def transform(poly,axis,offset,multiplier=1,fixed=False):
    """Exact substitution X_axis=offset+multiplier*X_axis, or a constant."""
    out={}
    for powers,co in poly.items():
        degree=powers[axis]
        for j in ([0] if fixed else range(degree+1)):
            factor=comb(degree,j)*offset**(degree-j)*multiplier**j
            if not factor: continue
            pp=list(powers);pp[axis]=j;pp=tuple(pp)
            out[pp]=out.get(pp,0)+co*factor
    return {p:co for p,co in out.items() if co}

def sum_cover(threshold,axis=0,fixed=None,offset=None):
    """Disjoint orthants covering X0+X1+X2>=threshold, Xi integers >=0."""
    fixed=[False]*3 if fixed is None else fixed
    offset=[0]*3 if offset is None else offset
    if threshold<=0:
        yield fixed,offset
        return
    if axis==3: return
    high=offset[:];high[axis]=threshold
    yield fixed[:],high
    for i in range(threshold):
        ff=fixed[:];ff[axis]=True
        oo=offset[:];oo[axis]=i
        yield from sum_cover(threshold-i,axis+1,ff,oo)

def positive_cover(poly,offset,fixed,depth=0):
    if all(v>=0 for v in poly.values()):
        return [(offset,fixed,poly)],[]
    if depth>=12 or all(fixed):
        return [],[(offset,fixed,poly)]
    choices=[]
    for axis in range(3):
        if fixed[axis]: continue
        high=transform(poly,axis,1)
        choices.append((sum(v<0 for v in high.values()),axis,high))
    _,axis,high=min(choices,key=lambda x:x[:2])
    low=transform(poly,axis,0,fixed=True)
    ff=fixed[:];ff[axis]=True
    oo=offset[:];oo[axis]+=1
    al,bl=positive_cover(low,offset[:],ff,depth+1)
    ah,bh=positive_cover(high,oo,fixed[:],depth+1)
    return al+ah,bl+bh

def certify():
    calibrations=calibration()
    results=[];failures=[]
    vars=(u,b,c)
    for delta in range(2):
        # The LH1 case with delta=0 is split to impose u+c>=1.
        chambers=[
            ('LL',True,True,{l:u,t:u+b,m:2*(u+b+c)+delta},[0,0,0],[False]*3),
            ('HH',False,False,{l:2*u+b+c+delta,t:2*u+2*b+c+delta,m:2*(u+b+c)+delta},[1-delta,0,0],[False]*3),
            ('LH2',True,False,{l:b+u,t:b+2*u+c+delta,m:2*(u+b+c)+delta},[1-delta,0,0],[False]*3),
        ]
        lh1={l:u,t:2*u+b+2*c+delta,m:2*(u+b+c)+delta}
        if delta:
            chambers.append(('LH1',True,False,lh1,[0,0,0],[False]*3))
        else:
            chambers.extend([
                ('LH1u',True,False,lh1,[1,0,0],[False]*3),
                ('LH1c',True,False,lh1,[0,0,1],[True,False,False])])
        for name,al,at,sub,base,base_fixed in chambers:
            for residue in product(*[([0] if f else range(2)) for f in base_fixed]):
                gap0=[x+y for x,y in zip(base,residue)]
                eps=int(sub[l].subs(dict(zip(vars,gap0))))%2
                eta=int(sub[t].subs(dict(zip(vars,gap0))))%2
                expr=s.Poly(720*kernel(delta,eps,eta,al,at).subs(sub,simultaneous=True),*vars)
                poly={p:int(co) for p,co in expr.terms()}
                assert all(co==int(co) for _,co in expr.terms())
                for axis in range(3):
                    poly=transform(poly,axis,gap0[axis],2,base_fixed[axis])
                threshold=max(0,((3-delta)-sum(gap0)+1)//2)
                # For the fixed-u chamber, sum constraint excludes that variable.
                start_axis=1 if base_fixed[0] else 0
                for fixed,offset in sum_cover(threshold,start_axis,base_fixed[:],[0]*3):
                    pp=poly
                    for axis in range(3): pp=transform(pp,axis,offset[axis],fixed=fixed[axis])
                    good,bad=positive_cover(pp,offset,fixed)
                    common=dict(region=name,delta=delta,epsilon=eps,eta=eta,
                        gap_base=gap0,substitutions={str(v):str(w) for v,w in sub.items()})
                    for off,fix,pol in good:
                        results.append(dict(**common,offset=off,fixed=fix,
                            terms=[[list(p),co] for p,co in sorted(pol.items())]))
                    for off,fix,pol in bad:
                        failures.append(dict(**common,offset=off,fixed=fix,
                            negative_terms=[[list(p),co] for p,co in sorted(pol.items()) if co<0]))
            print('certified chamber',delta,name,'cumulative leaves',len(results),'failures',len(failures),flush=True)
    report=dict(job_id=JOB,scale='1440*K3',tail_calibrations=calibrations,
                scope='integers m>=5, 0<=l<=t<=m',certificates=results,failures=failures)
    dest=ROOT/'evidence/research_kernel3.json'
    temp=dest.with_suffix('.tmp');temp.write_text(json.dumps(report,indent=2)+'\n');temp.replace(dest)
    print(json.dumps(dict(leaves=len(results),failures=failures[:10]),indent=2))

def calibration(limit=18):
    count=0
    for M in range(1,limit+1):
        for L in range(M+1):
            predicted=tail(l,M%2,L%2,L<=M//2)
            predicted=[v.subs({m:M,l:L}) for v in predicted]
            p,a=low_coefficients(M,[int(k>=L) for k in range(M+1)])
            assert predicted==p[2:5]+a[2:5],(M,L,predicted,p,a)
            count+=1
    return count

def exploratory():
    print('literal tail calibrations',calibration(),flush=True)
    rows=[]
    for delta,epsilon,eta in product(range(2),repeat=3):
        regions=[
            ('LL',True,True,{l:u,t:u+b,m:2*(u+b+c)+delta}),
            ('HH',False,False,{l:2*u+b+c+delta,t:2*u+2*b+c+delta,m:2*(u+b+c)+delta}),
            ('LH1',True,False,{l:u,t:2*u+b+2*c+delta,m:2*(u+b+c)+delta}),
            ('LH2',True,False,{l:b+u,t:b+2*u+c+delta,m:2*(u+b+c)+delta}),
        ]
        for name,al,at,sub in regions:
            expr=s.Poly(s.expand(720*kernel(delta,epsilon,eta,al,at).subs(sub,simultaneous=True)),u,b,c)
            negatives=[(mon,str(co)) for mon,co in expr.terms() if co<0]
            row=dict(parities=[delta,epsilon,eta],region=name,terms=len(expr.terms()),negative=negatives)
            rows.append(row)
            print(row,flush=True)
    (ROOT/'evidence/research_kernel3_exploration.json').write_text(json.dumps(dict(job_id=JOB,rows=rows),indent=2)+'\n')

if __name__=='__main__':
    certify()
