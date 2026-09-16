"""Final domain, base-case and file-integrity checks for this bounded pass."""
import hashlib
import json
import sys
from pathlib import Path
from math import comb
from research_verify import margin_vector

ROOT=Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(name):
    return json.loads((ROOT/name).read_text())


def main():
    initial=read('evidence/triage_integrity.json')
    source=sha(ROOT/'source.md')
    assert source==initial['source_sha256_before']==initial['source_sha256_after']
    unchanged={}
    for name,expected in initial['artifacts'].items():
        if name.startswith('evidence/'):
            assert sha(ROOT/name)==expected,name
            unchanged[name]=expected
    cert=read('evidence/research_edge_probe.json')
    B=cert['edge_bound']
    assert B==32
    assert [r['s'] for r in cert['records']]==list(range(1,B+2))
    coeff_count=finite_count=0
    for r in cert['records']:
        s,t0=r['s'],r['t0']
        assert [c['j'] for c in r['certificates']]==list(range(s-1,B+1))
        for c in r['certificates']:
            assert len(c['newton_coefficients'])==2*c['j']+1
            assert min(c['newton_coefficients'])>=0
            coeff_count+=len(c['newton_coefficients'])
        expected={(t,j) for t in range(t0) if s<<t>=9 for j in range(s-1,B+1)}
        observed={(c['t'],c['j']) for c in r['finite_checks']}
        assert observed==expected and len(observed)==len(r['finite_checks'])
        finite_count+=len(observed)
    assert coeff_count==24497 and finite_count==968
    # Independent sparse-dictionary product for all induction bases.
    bases=[]
    for n in [1,2,4,8]:
        a={0:1}
        for i in range(1,n+1):
            q=i
            while q<=n:
                b=dict(a)
                for j,v in a.items():
                    b[j+i]=b.get(j+i,0)+v
                a=b
                q*=2
        degree=max(a)
        vals=[a.get(j,0) for j in range(degree+1)]
        ts=[vals[j]**2-vals[j-1]*vals[j+1] for j in range(1,degree)]
        assert all(v>=0 for v in ts)
        bases.append(dict(n=n,degree=degree,coefficients=vals,internal_minors=ts))
    # Independent complete index/stage counts, without coefficient arithmetic.
    degree=sum(i*((256//i).bit_length()) for i in range(1,257))
    expected_h=expected_original=stages=0
    for n in range(257,513):
        odd=n
        while odd%2==0:
            odd//=2
        s=odd
        while s<=n:
            degree+=s
            expected_h+=degree+1
            stages+=1
            s*=2
        expected_original+=degree-1
    main_probe=read('evidence/research_h_probe.json')
    assert main_probe['complete'] and main_probe['completed_through']==512
    assert main_probe['h_checks']==expected_h==52893866
    assert main_probe['original_internal_minors_checked']==expected_original==26228480
    assert main_probe['stages_checked']==stages==512
    assert [r['n'] for r in main_probe['rows']]==list(range(257,513))
    assert not any(main_probe[k] for k in ['h_failures','five_ninths_failures',
                                         'original_failures','stage_failures'])
    # Recompute the design-range K certificates with the separate verifier.
    kernel=read('evidence/research_kernel_probe.json')
    expected={(s,j) for j in range(B+1) for s in range(1,j+2)}
    assert {(r['s'],r['j']) for r in kernel['records']}==expected
    cache={}
    kernel_count=0
    for r in kernel['records']:
        s,j,t0=r['s'],r['j'],r['t0']
        assert s<<t0>=max(9,j+1)
        assert t0==0 or s<<(t0-1)<max(9,j+1)
        assert len(r['newton_coefficients'])==2*j+1
        vals=[]
        for h in range(2*j+1):
            key=(s,t0+h)
            if key not in cache:
                cache[key]=margin_vector(s,t0+h,B)
            vals.append(cache[key][j])
        for h,c in enumerate(r['newton_coefficients']):
            assert c==sum((-1)**(h-v)*comb(h,v)*vals[v] for v in range(h+1))>=0
            kernel_count+=1
    files=['source.md','problem.md','checkpoint.md','evidence/research.md']
    files+=['evidence/'+n for n in ['research_h_probe.py','research_h_probe.json',
        'research_edge_probe.py','research_edge_probe.json','research_verify.py',
        'research_verify.json','research_kernel_probe.py','research_kernel_probe.json',
        'research_integrity.py']]
    out=dict(job_id='primary-20260913-subsum-denominator-research-c627858a54d2',
        source_sha256_before=initial['source_sha256_before'],source_sha256_after=source,
        python_version=sys.version,unchanged_triage_artifacts=unchanged,
        complete_edge_certificate_domain=True,newton_coefficient_count=coeff_count,
        earlier_finite_case_count=finite_count,independent_sparse_bases=bases,
        full_range_counts=dict(h=expected_h,original=expected_original,stages=stages),
        kernel_design_coefficients_independently_recomputed=kernel_count,
        literal_handoffs=[str(p.relative_to(ROOT)) for p in (ROOT/'literature').glob('*handoff*.md')],
        claim_json_absent=not (ROOT/'claim.json').exists(),
        artifacts={p:sha(ROOT/p) for p in files})
    p=ROOT/'evidence/research_integrity.json'
    tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p)
    print(json.dumps({k:v for k,v in out.items() if k not in ['independent_sparse_bases',
          'artifacts','unchanged_triage_artifacts']},indent=2))


if __name__=='__main__':
    main()
