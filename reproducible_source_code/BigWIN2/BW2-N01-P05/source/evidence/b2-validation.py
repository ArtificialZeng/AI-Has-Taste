"""Exact independent domain counts and literal-stack certificates for pass 2."""
import sys
sys.dont_write_bytecode=True
import json
from collections import Counter
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path

HERE=Path(__file__).resolve().parent
def module(name,file):
    sp=spec_from_file_location(name,HERE/file)
    m=module_from_spec(sp)
    sp.loader.exec_module(m)
    return m
v=module('validation','research-validation.py')
b=v.b


def main():
    counts=[]
    certificates=[]
    for path in sorted(HERE.glob('b2-r*-n*.json')):
        data=json.loads(path.read_text())
        k,n=data['r'],data['n']
        byprofile=[dict(profile=p,count=v.no_adjacent_count(p))
                   for p in v.profiles(n,k) if p.count(2)>=2]
        expected=sum(x['count'] for x in byprofile)
        assert expected==data['enumerated'],path.name
        counts.append(dict(file=path.name,expected_count=expected,profiles=byprofile))
        for q in map(tuple,data['first_counterexamples']):
            multiplicities=Counter(q)
            assert len(q)==n and len(multiplicities)==k
            assert b.canon(q)==q and b.trunc(q)==q
            assert min(multiplicities.values())>=2
            assert sum(c==2 for c in multiplicities.values())>=2
            qo=b.orbit(q,k)
            mo=b.orbit(q+(k,),k)
            assert not b.sorted_word(qo[k-2]) and b.sorted_word(qo[k-1])
            assert not b.sorted_word(mo[k-1]) and b.sorted_word(mo[k])
            marker_positions=[w.index(k) for w in mo]
            for t in range(k):
                assert v.gap(qo[t],marker_positions[t])==marker_positions[t+1]
                assert tuple(x for x in mo[t] if x!=k)==qo[t]
            clumps=lambda w:[x for x in sorted(set(w)) if b.trunc(w).count(x)==1]
            certificates.append(dict(q=q,multiplicities=dict(multiplicities),
                q_time=k-1,marked_time=k,q_orbit=qo,marked_orbit=mo,
                marker_positions=marker_positions,
                unmarked_clumps=[clumps(w) for w in qo],
                marked_clumps=[clumps(w) for w in mo],
                bridge_max_length=2*k+1,within_original_bridge=n<=2*k+1,
                validation='literal forbidden-triple stack, run-stack, recursive map, and gap recurrence'))
    out=dict(job_id='newwin-00001-p05-research-6c0e4e7ea54b',
        status='exact counterexamples to B2 only; original problem unresolved',
        independent_domain_counts=counts,certificates=certificates,
        source_sha256=sha256((HERE.parent/'source.md').read_bytes()).hexdigest(),
        search_script_sha256=sha256((HERE/'b2-search.py').read_bytes()).hexdigest(),
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    b.atomic_json(HERE/'b2-validation.json',out)
    print(json.dumps(dict(domain_checks=len(counts),certificates=len(certificates),
        first=certificates[0] if certificates else None),indent=2))


if __name__=='__main__':
    main()
