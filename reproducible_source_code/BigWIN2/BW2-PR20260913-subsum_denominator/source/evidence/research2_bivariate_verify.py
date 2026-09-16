"""Direct bivariate check of the Newton identity and binomial band lemma."""
import json,hashlib
from pathlib import Path
from math import comb
ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-983c87564404'

def product(n,s,m):
    a=[1]+[0]*m
    for i in range(1,m+1):
        u=i
        while u<n:
            for k in range(m,i-1,-1): a[k]+=a[k-i]
            u*=2
    v=s
    while v%2==0:
        v//=2
        for k in range(m,v-1,-1): a[k]+=a[k-v]
    return a

def qpoly(m):
    q=[1]+[0]*m
    for i in range(1,m+1):
        for k in range(m,i-1,-1): q[k]+=q[k-i]
    return q

def matrix(a,s,m):
    w=[[0]*(m+1) for _ in range(m+1)]
    for dx,dy,c in [(0,0,1),(s,0,2),(0,s,2),(s,s,1)]:
        for x in range(m+1-dx):
            for y in range(m+1-dy): w[x+dx][y+dy]+=c*a[x]*a[y]
    return w

def next_matrix(w,q,m):
    u=[[sum(q[v]*w[x-v][y] for v in range(x+1)) for y in range(m+1)] for x in range(m+1)]
    return [[sum(q[v]*u[x][y-v] for v in range(y+1))-w[x][y] for y in range(m+1)] for x in range(m+1)]

def value(w,j):
    return w[j][j]-(w[j-1][j+1] if j else 0)

def main():
    data=json.loads((ROOT/'evidence/research2_kernel_probe.json').read_text())
    count=polys=0
    for r in data['records']:
        s,j,t0=r['s'],r['j'],r['t0']
        if j>12: continue
        m=j+1
        a=product(s*2**t0,s,m)
        q=qpoly(m)
        w=matrix(a,s,m)
        for h,c in enumerate(r['newton_coefficients']):
            assert value(w,j)==c,(s,j,h)
            count+=1
            w=next_matrix(w,q,m)
        polys+=1
    # Generic coefficient positivity does not suffice outside the proved band.
    j,s,m=2,3,3
    w=matrix([1,0,0,0],s,m)
    q=qpoly(m)
    generic=[]
    for h in range(3):
        generic.append(value(w,j))
        w=next_matrix(w,q,m)
    assert generic==[0,-3,-1]
    # Exhaustively cross-check the rational smoothing identity on finite triples.
    checks=0
    for d in range(21):
        for N in range(d,2*d*d+10):
            if (N+d)%2 or N+2<d*d: continue
            j=(N+d)//2
            for a in range(d+1):
                k=j-a
                b=lambda v: comb(N,v) if 0<=v<=N else 0
                numerator=2*b(k)-b(k-1)-b(k+1)
                assert numerator*(k+1)*(N-k+1)==b(k)*(N+2-(N-2*k)**2)
                assert numerator>=0
                checks+=1
    out=dict(job_id=JOB,bivariate_identity_polynomials=polys,
        bivariate_identity_coefficients=count,range_j=[0,12],
        generic_A1_s3_j2_coefficients=generic,smoothing_identity_finite_checks=checks,
        statement='Finite checks supplement the algebraic proof; no uniform theorem is inferred from them',
        implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=ROOT/'evidence/research2_bivariate_verify.json'
    tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p)
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
