"""Independent domain counts, marker-gap identities, and direct orbit checks."""
import sys
sys.dont_write_bytecode=True
import json
from collections import Counter
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import product
from math import comb,factorial,prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('b',HERE/'research-pass1.py')
b=module_from_spec(sp)
sp.loader.exec_module(b)
sp=spec_from_file_location('old',HERE/'check-p05-small.py')
old=module_from_spec(sp)
sp.loader.exec_module(old)


def profiles(n,k,least=2):
    if k==0:
        if n==0:
            yield ()
        return
    for a in range(least,n//k+1):
        for rest in profiles(n-a,k-1,a):
            yield (a,)+rest


def no_adjacent_count(ms):
    n=sum(ms)
    total=0
    for js in product(*(range(m) for m in ms)):
        reduced=tuple(m-j for m,j in zip(ms,js))
        multinomial=factorial(sum(reduced))//prod(factorial(m) for m in reduced)
        total+=(-1)**sum(js)*prod(comb(m-1,j) for m,j in zip(ms,js))*multinomial
    sym=prod(factorial(c) for c in Counter(ms).values())
    assert total%sym==0
    return total//sym


def gap(q,p):
    if p==0:
        return len(q)
    a=q[0]
    before=[i for i in range(p) if q[i]==a]
    left=before[-1]
    right=next((i for i in range(p,len(q)) if q[i]==a),len(q))
    return left-len(before)+1+gap(q[left+1:right],p-left-1)


def main():
    checks=[]
    for name,key in [('terminal-marker.json','complete_cases'),('two-double-marker.json','cases')]:
        data=json.loads((HERE/name).read_text())
        for c in data[key]:
            n,k=c['n'],c['k']
            ms=list(profiles(n,k))
            if name.startswith('two-double'):
                ms=[p for p in ms if p.count(2)>=2]
            expected=sum(no_adjacent_count(p) for p in ms)
            assert c['enumerated']==expected,(name,n,k,c['enumerated'],expected)
            checks.append(dict(file=name,n=n,k=k,no_adjacent_rgs=expected))
    gaps=0
    for n in range(1,9):
        for k in range(1,min(n,4)+1):
            for q in old.rgs(n,k):
                image=b.recursive(q)
                for p in range(n+1):
                    target=q[:p]+(k,)+q[p:]
                    g=gap(q,p)
                    assert b.direct(target)==image[:g]+(k,)+image[g:]
                    gaps+=1
    inverse_checks=[]
    for file in sorted(HERE.glob('inverse-census-k*.json')):
        data=json.loads(file.read_text())
        k=data['k']
        for w in data['witnesses_rgs']:
            orbit=b.orbit(tuple(w),k)
            assert not b.sorted_word(orbit[k-1]) and b.sorted_word(orbit[k])
        for n,total in data['q_domain_totals'].items():
            expected=sum(no_adjacent_count(p) for p in profiles(int(n),k-1))
            assert total==expected
        inverse_checks.append(dict(k=k,checked=len(data['witnesses_rgs']),
            method='full-triple stack, run-stack and recursive map through k passes',
            q_domain_verified=True,file=file.name))
    out=dict(job_id='newwin-00001-p05-research-0171927ebd6e',
        status='exact finite verification; mathematical arguments are in research-pass1-notes.md',
        no_adjacent_domain_checks=checks,marker_gap_tests=gaps,
        inverse_orbit_checks=inverse_checks,
        source_sha256=sha256((HERE.parent/'source.md').read_bytes()).hexdigest(),
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    b.atomic_json(HERE/'research-validation.json',out)
    print(json.dumps({a:b for a,b in out.items() if a!='no_adjacent_domain_checks'},indent=2))


if __name__=='__main__':
    main()
