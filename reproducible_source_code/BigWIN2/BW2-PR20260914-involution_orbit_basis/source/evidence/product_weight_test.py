"""Held-out exact attack on evidence/product-weight-v1.md.

Run: python3 evidence/product_weight_test.py 8 2
Use RREF to choose increasing-weight monomials modulo all lower degrees.
Check pivot monomials against the independently generated forward data and
inspect every homogeneous straightening coefficient for a strict weight drop.
"""
from pathlib import Path
import hashlib
import json
import sys
import time
from flint import fmpq_mat
from research_rank import all_matchings, columns_for, atomic_json


def score(m):
    return sum(i*j for i,j in m)


def test(n,a):
    start=time.monotonic()
    saved=Path(f'evidence/research-n{n}a{a}-forward.json')
    data=json.loads(saved.read_text())
    assert data['complete'] and data['all_pass']
    points=[frozenset(map(tuple,p)) for p in data['points']]
    k=(n-a)//2
    lower=[]
    output=dict(n=n,a=a,scope='All matching monomials in all degrees 0..k',
                arithmetic='QQ RREF via FLINT',
                frozen_hypothesis_sha256=hashlib.sha256(Path('evidence/product-weight-v1.md').read_bytes()).hexdigest(),
                input_file=str(saved),input_sha256=hashlib.sha256(saved.read_bytes()).hexdigest(),
                grades=[],complete=False)
    path=Path(f'evidence/product-weight-n{n}a{a}.json')
    for d in range(k+1):
        mons=sorted(all_matchings(n,d),key=lambda m:(-score(m),m))
        all_cols=lower+mons
        cols=columns_for(all_cols,points)
        reduced,rank=fmpq_mat(cols).transpose().rref()
        pivots=[next(j for j in range(len(all_cols)) if reduced[i,j])
                for i in range(rank)]
        assert pivots[:len(lower)] == list(range(len(lower)))
        new_pivots=pivots[len(lower):]
        chosen=[all_cols[j] for j in new_pivots]
        expected={tuple(map(tuple,r['monomial'])) for r in data['candidate_data']
                  if len(r['monomial'])==d}
        agrees=set(chosen)==expected
        min_margin=None
        failures=[]
        relation_count=0
        nonzero_terms=0
        for j in range(len(lower),len(all_cols)):
            if j in new_pivots:
                continue
            relation_count+=1
            for i in range(len(lower),rank):
                if not reduced[i,j]:
                    continue
                nonzero_terms+=1
                margin=score(all_cols[pivots[i]])-score(all_cols[j])
                min_margin=margin if min_margin is None else min(min_margin,margin)
                if margin <= 0:
                    failures.append(dict(excluded=all_cols[j],basis_term=all_cols[pivots[i]],
                                         coefficient=str(reduced[i,j]),margin=margin))
        grade=dict(degree=d,lower_rank=len(lower),filtered_rank=rank,
                   expected_filtered_rank=data['grades'][d]['full_filtered_rank'],
                   pivot_count=len(chosen),candidate_pivots_agree=agrees,
                   strict_product_weight_pass=agrees and not failures,
                   minimum_strict_margin=min_margin,relations_checked=relation_count,
                   nonzero_homogeneous_terms=nonzero_terms,pivot_monomials=chosen,
                   bad_margin_terms=failures[:10],
                   unexpected_pivots=[m for m in chosen if m not in expected][:10],
                   missed_candidates=[m for m in expected if m not in set(chosen)][:10])
        assert rank==grade['expected_filtered_rank']
        output['grades'].append(grade)
        atomic_json(path,output)
        print(json.dumps({k:v for k,v in grade.items() if k not in
                          ['pivot_monomials','bad_margin_terms','unexpected_pivots','missed_candidates']}),flush=True)
        lower+=chosen
    output.update(complete=True,all_pass=all(g['strict_product_weight_pass'] for g in output['grades']),
                  elapsed_seconds=time.monotonic()-start)
    atomic_json(path,output)
    print(json.dumps(dict(saved=str(path),all_pass=output['all_pass'],elapsed_seconds=output['elapsed_seconds'])),flush=True)


if __name__=='__main__':
    test(*map(int,sys.argv[1:]))
