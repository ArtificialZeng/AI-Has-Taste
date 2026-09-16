"""Final domain/provenance checks; not a mathematical acceptance gate."""
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
JOB='primary-20260913-subsum-denominator-research-077128f18f2f'
SOURCE='3d8e6928f3bd250dbdfde723603903f527d4ec0da8f85f5ac628b232991e240a'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.loads((ROOT/p).read_text())

def main():
    assert sha(ROOT/'source.md')==SOURCE
    old=read('evidence/research2_integrity.json')
    preserved={}
    for group in ['unchanged_pass1_artifacts','artifacts','primary_pdf_hashes']:
        for p,h in old[group].items():
            if p in ['problem.md','checkpoint.md']:
                continue
            assert sha(ROOT/p)==h,p
            preserved[p]=h
    small=read('evidence/research2_sharp_probe.json')
    dense=read('evidence/research3_sharp_probe.json')
    dv=read('evidence/research3_verify.json')
    sv=read('evidence/research3_design_verify.json')
    sparse=read('evidence/research3_boundary_probe.json')
    bv=read('evidence/research3_boundary_verify.json')
    records=small['records']+dense['records']
    expected={(s,j) for j in range(97) for s in range(1,j+2)}
    assert len(records)==len(expected)==4753
    assert {(r['s'],r['j']) for r in records}==expected
    count=0
    for r in records:
        s,j=r['s'],r['j']
        tau=r.get('tau',r.get('t0'))
        assert s*2**tau>=9 and 2*s*2**tau>j+1
        assert tau==0 or s*2**(tau-1)<9 or 2*s*2**(tau-1)<=j+1
        c=r['newton_coefficients']
        assert len(c)==2*j+1 and all(x>=0 for x in c)
        count+=len(c)
    assert count==613137
    finite=sv['earlier_finite_records']+dense['earlier_finite_records']
    fexpected=set()
    for s,j in expected:
        t=0
        while 2*s*2**t<=j+1:
            if s*2**t>=9:
                fexpected.add((s,j,t))
            t+=1
    assert len(finite)==len(fexpected)==3126
    assert {(r['s'],r['j'],r['t']) for r in finite}==fexpected
    assert all(r['margin']>=0 for r in finite)
    assert dv['coefficients_recomputed']==427952
    assert sv['inherited_coefficients_recomputed']==185185
    assert sparse['polynomials']==128 and sparse['newton_coefficients']==69632
    assert not sparse['negative_coefficients'] and sparse['complete']
    assert bv['large_polynomials']==128 and bv['low_order_coefficients_recomputed']==640
    assert bv['top_formula_checks']==bv['outside_grid_evaluations']==256
    assert len(bv['excluded_boundary_witnesses'])==48
    for r in bv['excluded_boundary_witnesses']:
        assert r['actual_H_margin']-r['polynomial_extrapolation']==r['discrepancy']<0
        assert r['actual_forward_difference']==r['discrepancy']
        assert r['difference_order']==4*r['n'] and r['j']==2*r['n']-1
    # Bind every executed current script and its inputs to its recorded output.
    for name in ['research3_sharp_probe','research3_verify','research3_design_verify',
                 'research3_boundary_probe','research3_boundary_verify']:
        d=read('evidence/'+name+'.json')
        assert d['job_id']==JOB
        assert d['implementation_sha256']==sha(ROOT/('evidence/'+name+'.py'))
    assert dv['certificate_sha256']==sha(ROOT/'evidence/research3_sharp_probe.json')
    assert sv['certificate_sha256']==sha(ROOT/'evidence/research2_sharp_probe.json')
    assert bv['certificate_sha256']==sha(ROOT/'evidence/research3_boundary_probe.json')
    for d in [sv,bv]:
        assert d['dependency_sha256']==sha(ROOT/'evidence/research3_verify.py')
    for d in [dense,sparse]:
        assert d['frozen_definition_sha256']==sha(ROOT/'evidence/research2.md')
    primary={}
    for name in ['bbfm-subsum-journal.pdf','chen-ono-zhang-2605.21718v2.pdf']:
        p='evidence/external/'+name
        assert sha(ROOT/p)==sha(ROOT/('literature/'+name))
        primary[p]=sha(ROOT/p)
    claim=read('claim.json')
    assert set(claim)=={'kind','original_status','statement','contribution','proposer_job_id','evidence_files'}
    assert claim['kind']=='conjecture-note' and claim['original_status']=='unresolved'
    assert claim['proposer_job_id']==JOB
    assert {'source.md','problem.md',*primary}.issubset(claim['evidence_files'])
    assert len(set(claim['evidence_files']))==len(claim['evidence_files'])
    hashes={}
    for p in claim['evidence_files']:
        assert str(Path(p))==p and not Path(p).is_absolute() and '..' not in Path(p).parts
        if p=='evidence/research3_integrity.json':
            continue
        assert (ROOT/p).is_file() and (ROOT/p).stat().st_size>0,p
        hashes[p]=sha(ROOT/p)
    out=dict(job_id=JOB,original_source_unchanged=True,source_sha256=SOURCE,
        preserved_prior_artifacts=preserved,complete_dense_polynomials=4753,
        complete_dense_coefficients=613137,complete_earlier_cases=3126,
        sparse_polynomials=128,sparse_coefficients=69632,
        independent_dense_coverage_j_max=96,
        independent_sparse_coverage='h=0..4, top two formulas, two outside-grid evaluations',
        excluded_boundary_stage_checks=48,copied_primary_sources=primary,
        literal_handoffs=list(map(str,(ROOT/'literature').glob('*handoff*.md'))),
        claim_schema_valid=True,claim_sha256=sha(ROOT/'claim.json'),
        evidence_hashes_excluding_self=hashes,python_version=sys.version,
        scope='Structural and exact-domain checks only; no mathematical acceptance or novelty certification')
    dest=ROOT/'evidence/research3_integrity.json'
    tmp=dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(dest)
    print(json.dumps({k:v for k,v in out.items() if k not in ['preserved_prior_artifacts','evidence_hashes_excluding_self']},indent=2))

if __name__=='__main__':
    main()
