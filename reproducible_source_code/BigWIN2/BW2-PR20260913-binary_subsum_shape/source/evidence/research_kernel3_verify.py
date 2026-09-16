#!/usr/bin/env python3
"""Independently recompute every K3 certificate with Fraction polynomial algebra.

No SymPy and no import from the certificate generator. This is a second
algorithm in the same research pass, not an independent mathematical referee.
"""
import hashlib
import json
from itertools import product
from fractions import Fraction as R
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class P:
    def __init__(self,x=0):
        self.d=x if isinstance(x,dict) else ({(0,0,0):R(x)} if x else {})
    def __add__(self,x):
        x=x if isinstance(x,P) else P(x)
        out=self.d.copy()
        for k,v in x.d.items():out[k]=out.get(k,R(0))+v
        return P({k:v for k,v in out.items() if v})
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,x):return self+-x
    def __rsub__(self,x):return -self+x
    def __mul__(self,x):
        x=x if isinstance(x,P) else P(x)
        out={}
        for a,v in self.d.items():
            for b,w in x.d.items():
                k=tuple(i+j for i,j in zip(a,b));out[k]=out.get(k,R(0))+v*w
        return P({k:v for k,v in out.items() if v})
    __rmul__=__mul__
    def __truediv__(self,x):return self*R(1,x)
    def __pow__(self,n):
        out=P(1)
        for _ in range(n):out=out*self
        return out

def F(r,z):
    return [z+1,z*(z+1)/2,z*(z+1)*(2*z+1)/6,
            z*z*(z+1)*(z+1)/4,
            z*(z+1)*(2*z+1)*(3*z*z+3*z-1)/30][r]

def tail(m,z,delta,epsilon,active):
    q=(m-delta)/2
    v=[F(r,m)-F(r,z-1) for r in range(5)]
    h2=F(2,q)-F(2,z-1) if active else P()
    h3=F(3,q)-F(3,z-1) if active else P()
    p2=2*v[2]
    p3=4*v[3]/3-v[2]+(2*m+R(5,3))*v[1]-(m*m+m)*v[0]
    # Reversed-sum derivation, retaining the three separate contributions.
    sum_binomial4=(16*v[4]-48*v[3]+44*v[2]-12*v[1])/24
    even=(q-(z-epsilon)/2)*(q-(z-epsilon)/2+1-epsilon)
    p4=sum_binomial4+z*(2*v[2]-v[1])+2*(m*v[2]-v[3])+2*((m+1)*h2-2*h3)+even
    a2=2*m*m-m+z
    a3=(4*m*m*m+2*m)/3-2*m*(m-z)
    a4=(2*m)*(2*m-1)*(2*m-2)*(2*m-3)/24+(2*m*m-m)*z+2*h2
    return p2,p3,p4,a2,a3,a4

def literal(M,L):
    w=lambda k:int(k>=L)
    p2=2*sum(k*k*w(k) for k in range(M+1))
    p3=sum(((4*k**3+2*k)//3-(M-k)*(M-k+1))*w(k) for k in range(M+1))
    from math import comb
    p4=0
    for k in range(1,M+1):
        rr=sum(w(h) for h in range(k))
        p4+=comb(2*k,4)*w(k)+comb(2*k,2)*(k*w(k)-rr)
        p4+=2*sum(h*h*w(h) for h in range(k//2+1))
        p4+=2*sum(h*h*w(h) for h in range(k))
        p4+=rr if k%2==0 else 0
    rr=sum(w(h) for h in range(M))
    a2=2*M*M-rr
    a3=(4*M**3+2*M)//3-2*M*rr
    a4=comb(2*M,4)+comb(2*M,2)*(M-rr)+2*sum(h*h*w(h) for h in range(M//2+1))
    return p2,p3,p4,a2,a3,a4

def variables(row):
    vv=[]
    for axis in range(3):
        value=row['gap_base'][axis]+2*row['offset'][axis]
        poly=P(value)
        if not row['fixed'][axis]:
            powers=[0]*3;powers[axis]=1
            poly=poly+P({tuple(powers):R(2)})
        vv.append(poly)
    U,B,C=vv;delta=row['delta'];m=2*(U+B+C)+delta
    name=row['region']
    if name=='LL':l,t=U,U+B;acts=True,True
    elif name=='HH':l,t=2*U+B+C+delta,2*U+2*B+C+delta;acts=False,False
    elif name=='LH2':l,t=B+U,B+2*U+C+delta;acts=True,False
    else:l,t=U,2*U+B+2*C+delta;acts=True,False
    return m,l,t,acts

def matches(row,M,L,T):
    if M%2!=row['delta']:return False
    q=M//2;delta=M%2;name=row['region']
    if name=='LL':
        if not L<=T<=q:return False
        gaps=[L,T-L,q-T]
    elif name=='HH':
        if not q<L<=T:return False
        gaps=[L-q-delta,T-L,M-T]
    elif name=='LH2':
        if not L<=q<T or T>q+L+delta:return False
        gaps=[T-q-delta,q+L+delta-T,q-L]
    else:
        if not L<=q<T or T<q+L+delta:return False
        gaps=[L,M-T,T-q-L-delta]
    for axis,value in enumerate(gaps):
        difference=value-row['gap_base'][axis]
        if difference<0 or difference%2:return False
        x=difference//2
        if x<row['offset'][axis]:return False
        if row['fixed'][axis] and x!=row['offset'][axis]:return False
    return True

def main():
    src=ROOT/'evidence/research_kernel3.json'
    data=json.loads(src.read_text());assert not data['failures']
    monomials=0
    for i,row in enumerate(data['certificates']):
        m,l,t,acts=variables(row)
        q=(m-row['delta'])/2
        for constraint in [m-5,l,t-l,m-t,
            q-l if acts[0] else l-q-1,
            q-t if acts[1] else t-q-1]:
            assert all(v>=0 for v in constraint.d.values()),('domain containment',i)
        for polynomial,parity in [(m,row['delta']),(l,row['epsilon']),(t,row['eta'])]:
            assert polynomial.d.get((0,0,0),0)%2==parity
            assert all(v%2==0 for k,v in polynomial.d.items() if any(k))
        p2,p3,p4,a2,a3,a4=tail(m,l,row['delta'],row['epsilon'],acts[0])
        q2,q3,q4,b2,b3,b4=tail(m,t,row['delta'],row['eta'],acts[1])
        exact=720*(2*p3*q3-p2*q4-q2*p4-2*a3*b3+a2*b4+b2*a4)
        expected={tuple(p):R(v) for p,v in row['terms']}
        assert exact.d==expected,('polynomial identity',i)
        assert all(v>=0 for v in expected.values()),i
        monomials+=len(expected)
    # Complete infinite coverage: membership in an orthant leaf depends only
    # on min(X_i,H), with H one greater than every leaf offset. The condition
    # sum X_i >= threshold is also preserved because threshold <= H.
    H=1+max(max(row['offset']) for row in data['certificates'])
    root_checks=0;clipped_checks=0
    for delta in (0,1):
        roots=[('LL',[0,0,0],[False]*3),
               ('HH',[1-delta,0,0],[False]*3),
               ('LH2',[1-delta,0,0],[False]*3)]
        roots+=([('LH1',[0,0,0],[False]*3)] if delta else
                [('LH1u',[1,0,0],[False]*3),('LH1c',[0,0,1],[True,False,False])])
        for name,base,base_fixed in roots:
            for residues in product(*[([0] if f else range(2)) for f in base_fixed]):
                gap0=[x+y for x,y in zip(base,residues)]
                leaves=[row for row in data['certificates'] if row['region']==name
                        and row['delta']==delta and row['gap_base']==gap0]
                assert leaves
                assert max(0,((3-delta)-sum(gap0)+1)//2)<=H
                for vector in product(*[([0] if f else range(H+1)) for f in base_fixed]):
                    if 2*(sum(gap0)+2*sum(vector))+delta<5:continue
                    assert any(all((vector[a]==row['offset'][a] if row['fixed'][a]
                                    else vector[a]>=row['offset'][a]) for a in range(3))
                               for row in leaves),(name,delta,gap0,vector)
                    clipped_checks+=1
                root_checks+=1
    # Check the supplementary strictness and A-positivity expansions.
    z=P({(1,0,0):R(1)})
    strict_arrays={
        0:[46638720,139543488,175898688,123122688,52593728,14069952,2302592,210432,8192],
        1:[8985600,34793280,55319456,48077056,25219648,8213440,1623424,177664,8192]}
    alpha_arrays={0:[8064,28632,41224,31014,12916,2832,256],
                  1:[40500,105300,113725,65304,21028,3600,256]}
    beta_arrays={0:[96,406,463,206,32],1:[465,1056,823,270,32]}
    for delta in (0,1):
        m=2*z+(5 if delta else 6)
        p2,p3,p4,a2,a3,a4=tail(m,P(0),delta,0,True)
        strict=1440*(p3*p3-p2*p4-a3*a3+a2*a4)
        assert strict.d=={(i,0,0):R(v) for i,v in enumerate(strict_arrays[delta])}
        m=2*z+4+delta;q=(m-delta)/2
        C2=m*(2*m-1);C3=2*m*(2*m-1)*(2*m-2)/6
        C4=2*m*(2*m-1)*(2*m-2)*(2*m-3)/24
        q2=q*(q+1)*(2*q+1)/3
        alpha=9*(C3*C3-C2*(C4+q2))
        beta=3*(4*m*C3-C2*C2-C4-q2)
        assert alpha.d=={(i,0,0):R(v) for i,v in enumerate(alpha_arrays[delta])}
        assert beta.d=={(i,0,0):R(v) for i,v in enumerate(beta_arrays[delta])}
    # Independent finite domain-mapping and literal arithmetic checks.
    pairs=0;zeros=[];minimum_positive=None
    rows_by_parity={d:[r for r in data['certificates'] if r['delta']==d] for d in (0,1)}
    for M in range(5,49):
        basis=[literal(M,L) for L in range(M+1)]
        for L,(p2,p3,p4,a2,a3,a4) in enumerate(basis):
            for T in range(L,M+1):
                assert any(matches(row,M,L,T) for row in rows_by_parity[M%2]),(M,L,T)
                q2,q3,q4,b2,b3,b4=basis[T]
                twice=2*p3*q3-p2*q4-q2*p4-2*a3*b3+a2*b4+b2*a4
                assert twice>=0,(M,L,T,twice)
                if twice==0:zeros.append([M,L,T])
                else:minimum_positive=twice if minimum_positive is None else min(minimum_positive,twice)
                pairs+=1
    report=dict(job_id=data['job_id'],certificate_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
        algorithm='Separate Python Fraction multivariate polynomial algebra; no SymPy or generator imports',
        verified_polynomial_identities=len(data['certificates']),nonnegative_monomials=monomials,
        infinite_coverage=dict(parity_roots=root_checks,clipping_threshold=H,
                              exhaustive_clipped_vectors=clipped_checks,
                              argument='Each fixed equality or lower-bound membership and the sum constraint is preserved by coordinate clipping at H.'),
        supplementary_arrays=dict(scale_1440_K00=strict_arrays,scale_9_alpha=alpha_arrays,scale_3_beta=beta_arrays),
        literal_kernel_and_domain_mapping_m_range=[5,48],literal_pairs=pairs,
        minimum_positive_twice_kernel=minimum_positive,zero_entries=zeros,
        limits='All-parameter identities and complete clipped-orthant coverage; literal checks are finite. Mathematical derivation and scope in research-kernel3-proof.md. No fresh referee.')
    out=ROOT/'evidence/research_kernel3_verify.json'
    temp=out.with_suffix('.tmp');temp.write_text(json.dumps(report,indent=2)+'\n');temp.replace(out)
    print(json.dumps({k:v for k,v in report.items() if k!='zero_entries'},indent=2))

if __name__=='__main__':main()
