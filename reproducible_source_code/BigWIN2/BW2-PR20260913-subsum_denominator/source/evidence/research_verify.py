"""Recompute research evidence with separate coefficient constructions.

Uses binomial convolution for edge templates (not repeated shift/add), and
signed binomial sums for Newton coefficients (not iterative differences).
This is an implementation cross-check by the researcher, not a fresh referee.
"""
import hashlib
import json
from math import comb
from pathlib import Path
from flint import fmpz_poly

ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-c627858a54d2'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def truncated_product(exponents,B):
    a=[1]+[0]*(B+1)
    for i,e in enumerate(exponents,1):
        b=[0]*(B+2)
        for r in range(min(e,(B+1)//i)+1):
            c=comb(e,r)
            for j in range(B+2-r*i):
                b[j+r*i]+=c*a[j]
        a=b
    return a


def get(a,j):
    return a[j] if 0<=j<len(a) else 0


def det(a,j):
    return get(a,j)**2-get(a,j-1)*get(a,j+1)


def exponent(n,i):
    q=0
    while i*(1<<q)<=n:
        q+=1
    return q


def margin_vector(s,t,B):
    n=s*(2**t)
    # Earlier factors before s are precisely the successive halvings of s.
    earlier=set()
    u=s
    while u%2==0:
        u//=2
        earlier.add(u)
    es=[exponent(n-1,i)+(i in earlier) for i in range(1,B+2)]
    a=truncated_product(es,B)
    b=[get(a,j)+get(a,j-s) for j in range(B+2)]
    return [2*det(b,j)-det(a,j)-det(a,j-s) for j in range(B+1)]


def main():
    cert=json.loads((ROOT/'evidence/research_edge_probe.json').read_text())
    B=cert['edge_bound']
    coefficients_checked=0
    finite_checks=0
    for record in cert['records']:
        s,t0=record['s'],record['t0']
        assert s<<t0>=max(9,B+1)
        assert t0==0 or s<<(t0-1)<max(9,B+1)
        table=[margin_vector(s,t0+h,B) for h in range(2*B+1)]
        for c in record['certificates']:
            j=c['j']
            assert c['degree_bound']==2*j
            for h,claimed in enumerate(c['newton_coefficients']):
                actual=sum((-1)**(h-v)*comb(h,v)*table[v][j] for v in range(h+1))
                assert actual==claimed and actual>=0,(s,j,h)
                coefficients_checked+=1
        for c in record['finite_checks']:
            assert margin_vector(s,c['t'],B)[c['j']]==c['margin']>=0
            finite_checks+=1
    # Independent compiled polynomial arithmetic and direct product for endpoint n.
    full=[]
    main_probe=json.loads((ROOT/'evidence/research_h_probe.json').read_text())
    for n in [256,512]:
        f=fmpz_poly([1])
        for i in range(1,n+1):
            for _ in range(exponent(n,i)):
                f=f+f.left_shift(i)
        a=[int(v) for v in f.coeffs()]
        digest=hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()
        expected=main_probe['base']['coefficients_sha256'] if n==256 else main_probe['last_coefficients_sha256']
        assert digest==expected
        assert all(v*v>=u*w for u,v,w in zip(a,a[1:],a[2:]))
        full.append(dict(n=n,degree=len(a)-1,coefficients_sha256=digest))
    # Explicit generic counterexample: both old/new polynomials are log-concave.
    N,s=16,4
    a=[comb(N,j) for j in range(N+1)]
    b=[get(a,j)+get(a,j-s) for j in range(N+s+1)]
    j=(N+s)//2
    assert all(det(a,k)>0 for k in range(N+1))
    assert all(det(b,k)>=0 for k in range(N+s+1))
    boundary=det(a,s-1)-2*a[s-2]*a[0]
    hmargin=2*det(b,j)-det(a,j)-det(a,j-s)
    assert boundary==94960 and hmargin==-15077504
    witness=dict(N=N,s=s,j=j,a=a,b=b,boundary_margin=boundary,
        old_minors=[det(a,j),det(a,j-s)],new_minor=det(b,j),h_margin=hmargin,
        scope='Counterexample only to sufficiency of symmetry, log-concavity and the first-overlap condition.')
    out=dict(job_id=JOB,source_sha256=sha(ROOT/'source.md'),
        newton_coefficients_independently_recomputed=coefficients_checked,
        finite_cases_independently_recomputed=finite_checks,
        direct_flint_full_product_checks=full,generic_boundary_counterexample=witness,
        artifacts={str(p.relative_to(ROOT)):sha(p) for p in [
            ROOT/'evidence/research_h_probe.py',ROOT/'evidence/research_h_probe.json',
            ROOT/'evidence/research_edge_probe.py',ROOT/'evidence/research_edge_probe.json',
            Path(__file__)]})
    p=ROOT/'evidence/research_verify.json'
    tmp=p.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(p)
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
