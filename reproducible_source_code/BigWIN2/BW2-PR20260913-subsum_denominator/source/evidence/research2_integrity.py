"""Domain, witness, base, provenance, and immutable-input checks for pass 2.
These checks supplement the mathematical arguments; they are not a referee.
"""
import hashlib,json,sys
from pathlib import Path
from math import comb
ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-983c87564404'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads((ROOT/p).read_text())
def get(a,j): return a[j] if 0<=j<len(a) else 0
def minor(a,j): return get(a,j)**2-get(a,j-1)*get(a,j+1)

def sparse(n):
    a={0:1}
    for i in range(1,n+1):
        v=i
        while v<=n:
            b=dict(a)
            for j,c in a.items(): b[j+i]=b.get(j+i,0)+c
            a=b
            v*=2
    return [a.get(j,0) for j in range(max(a)+1)]

def main():
    old=read('evidence/research_integrity.json')
    source=sha(ROOT/'source.md')
    assert source==old['source_sha256_before']==old['source_sha256_after']
    unchanged={}
    for name,digest in old['artifacts'].items():
        if name.startswith('evidence/') or name=='source.md':
            assert sha(ROOT/name)==digest,name
            unchanged[name]=digest
    primary={'literature/bbfm-subsum-journal.pdf':'a0da6b8f736e5fc66084d2fa6913d89bce77254d7e9e4e5a5a2acce9b4a4ff31',
        'literature/chen-ono-zhang-2605.21718v2.pdf':'6593c03b6fb85a09c8e5d5a6a4f9a8f9b71d000ad394d1b2ce9292eafc8dae67'}
    for p,h in primary.items(): assert sha(ROOT/p)==h
    data=read('evidence/research2_kernel_probe.json')
    verify=read('evidence/research2_verify.json')
    sharp=read('evidence/research2_sharp_probe.json')
    bivariate=read('evidence/research2_bivariate_verify.json')
    for a in [data,verify,sharp,bivariate]: assert a['job_id']==JOB
    for stem,a in [('research2_kernel_probe',data),('research2_sharp_probe',sharp),('research2_bivariate_verify',bivariate)]:
        assert a['implementation_sha256']==sha(ROOT/('evidence/'+stem+'.py'))
    assert verify['script_sha256']==sha(ROOT/'evidence/research2_verify.py')
    assert verify['certificate_sha256']==sharp['parent_certificate_sha256']==sha(ROOT/'evidence/research2_kernel_probe.json')
    domain={(s,j) for j in range(65) for s in range(1,j+2)}
    current={}
    coefficient_count=held_count=held_polys=0
    earlier=set()
    band_count=0
    for r in data['records']:
        s,j,t0=r['s'],r['j'],r['t0']
        assert (s,j) not in current
        current[s,j]=r
        assert s*2**t0>=max(9,j+1)
        assert t0==0 or s*2**(t0-1)<max(9,j+1)
        c=r['newton_coefficients']
        assert len(c)==2*j+1 and min(c)>=0
        coefficient_count+=len(c)
        if j>=33: held_count+=len(c);held_polys+=1
        for h,x in enumerate(c):
            deficit=2*j-h
            if j>=2*deficit**2+deficit-1:
                assert x>=0
                band_count+=1
        earlier.update((s,j,t) for t in range(t0) if s*2**t>=9)
    assert set(current)==domain
    assert coefficient_count==data['newton_coefficients']==verify['coefficients_recomputed']==185185
    assert held_count==verify['held_out_coefficients']==160688
    assert held_polys==verify['held_out_polynomials']==1584
    finite=verify['earlier_finite_records']
    assert len(finite)==len(earlier)==verify['earlier_finite_checks']==3068
    assert {(r['s'],r['j'],r['t']) for r in finite}==earlier
    assert all(r['margin']>=0 and r['n']==r['s']*2**r['t'] for r in finite)
    for r in read('evidence/research_kernel_probe.json')['records']:
        assert current[r['s'],r['j']]==r
    assert not data['negative_coefficients'] and not sharp['negative_coefficients']
    sharp_domain=set()
    changed=translated=0
    for r in sharp['records']:
        s,j,t0=r['s'],r['j'],r['t0']
        assert (s,j) not in sharp_domain
        sharp_domain.add((s,j))
        n=s*2**t0
        assert n>=9 and 2*n>j+1
        assert t0==0 or n//2<9 or n<=j+1
        previous=current[s,j]
        assert previous['t0']-t0 in (0,1)
        c=list(previous['newton_coefficients'])
        if previous['t0']!=t0:
            changed+=1;translated+=len(c)
            for h in range(len(c)-2,-1,-1): c[h]-=c[h+1]
        assert c==r['newton_coefficients'] and min(c)>=0
    assert sharp_domain==domain
    assert changed==sharp['translated_polynomials']==1956
    assert translated==sharp['translated_coefficients']==sharp['independent_translated_coefficients_recomputed']==175492
    bases=[]
    for n in [1,2,4,8]:
        a=sparse(n)
        ts=[minor(a,j) for j in range(1,len(a)-1)]
        assert min(ts,default=0)>=0
        bases.append(dict(n=n,degree=len(a)-1,coefficients=a,internal_minors=ts))
    a=bases[-1]['coefficients']
    b=[get(a,j)+get(a,j-9) for j in range(len(a)+9)]
    witness=sharp['excluded_boundary_witness']
    actual=2*minor(b,17)-minor(a,17)-minor(a,8)
    assert actual==witness['actual_margin']==19668
    assert a[16]==witness['a_16']==899 and a[7]==witness['a_7']==114
    discrepancy=-a[16]-2*a[7]
    tail=current[9,17]
    extrapolation=sum((-1)**h*c for h,c in enumerate(tail['newton_coefficients']))
    assert extrapolation==witness['polynomial_extrapolation']==20795
    assert actual-extrapolation==discrepancy==witness['forward_difference']==-1127
    assert witness['forward_difference_order']==36>34
    assert bivariate['bivariate_identity_coefficients']==sum((j+1)*(2*j+1) for j in range(13))==1547
    assert bivariate['bivariate_identity_polynomials']==91
    assert bivariate['generic_A1_s3_j2_coefficients']==[0,-3,-1]
    assert not (ROOT/'claim.json').exists()
    files=['source.md','problem.md','checkpoint.md','evidence/research2.md','evidence/research2_band.md']
    for stem in ['research2_kernel_probe','research2_verify','research2_sharp_probe','research2_bivariate_verify']:
        files.extend('evidence/'+stem+ext for ext in ['.py','.json'])
    files.append('evidence/research2_integrity.py')
    out=dict(job_id=JOB,source_sha256_before=old['source_sha256_before'],source_sha256_after=source,
        python_version=sys.version,unchanged_pass1_artifacts=unchanged,primary_pdf_hashes=primary,
        complete_kernel_domain=True,kernel_polynomials=len(domain),kernel_coefficients=coefficient_count,
        held_out_polynomials=held_polys,held_out_coefficients=held_count,
        earlier_finite_checks=len(earlier),uniform_band_coefficients_in_certificate=band_count,
        complete_sharp_domain=True,sharp_translated_polynomials=changed,sharp_translated_coefficients=translated,
        independent_sparse_bases=bases,boundary_witness_sparse_verified=True,
        literal_handoffs=[str(p.relative_to(ROOT)) for p in (ROOT/'literature').glob('*handoff*.md')],
        claim_json_absent=True,next_test_unsearched_j_range=[65,96],
        artifacts={p:sha(ROOT/p) for p in files})
    path=ROOT/'evidence/research2_integrity.json'
    tmp=path.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(path)
    print(json.dumps({k:v for k,v in out.items() if k not in ['artifacts','unchanged_pass1_artifacts','independent_sparse_bases','primary_pdf_hashes']},indent=2))

if __name__=='__main__': main()
