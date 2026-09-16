#!/usr/bin/env python3
"""Separate exact verifier; no imports from the discovery script.

Enumerate inversion vectors first, decode by insertion, determine every
bound by its universal property, and check distributivity directly.
This is computation by a second implementation, not a fresh referee.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]

def generate(n):
    for t in product(*(range(v) for v in range(1,n+1))):
        p = []
        for v,z in enumerate(t,1):
            p.insert(v-1-z,v)
        signs = [p[i+1]>p[i] for i in range(n-1)]
        sigma = tuple(p[i] for i in range(1,n-1) if signs[i-1] and not signs[i])
        yield tuple(p), t, sigma

def operations(rows):
    m = len(rows)
    order = [[all(a<=b for a,b in zip(x[1],y[1])) for y in rows] for x in rows]
    joins = [[None]*m for _ in rows]
    meets = [[None]*m for _ in rows]
    for i in range(m):
        for j in range(m):
            U = [k for k in range(m) if order[i][k] and order[j][k]]
            L = [k for k in range(m) if order[k][i] and order[k][j]]
            leasts = [k for k in U if all(order[k][l] for l in U)]
            greatests = [k for k in L if all(order[l][k] for l in L)]
            assert len(leasts)==len(greatests)==1, (i,j,leasts,greatests)
            joins[i][j] = leasts[0]
            meets[i][j] = greatests[0]
    return order, joins, meets

def main():
    small = []
    for n in range(5):
        groups = {}
        for p,t,s in generate(n):
            groups.setdefault(s,[]).append((p,t))
        for rows in groups.values():
            _,J,M = operations(rows)
            for a,b,c in product(range(len(rows)),repeat=3):
                assert M[a][J[b][c]] == J[M[a][b]][M[a][c]]
        small.append({'n':n,'fibers':len(groups),'all_triples_distributive':True})
    certpath = ROOT/'evidence/triage_obstruction.json'
    cert = json.loads(certpath.read_text())
    assert cert['n']==5 and cert['sigma']==[5]
    rows = [(p,t) for p,t,s in generate(5) if s==(5,)]
    supplied = [(tuple(r['permutation']),tuple(r['iota'])) for r in cert['fiber']]
    assert len(supplied)==len(set(supplied))==56
    assert set(rows)==set(supplied), 'incomplete or incorrect fiber certificate'
    order,J,M = operations(rows)
    ids = {p:i for i,(p,t) in enumerate(rows)}
    named = {'e':(1,2,3,5,4),'b':(1,2,5,3,4),'a':(1,3,5,2,4),
             'c':(1,3,4,5,2),'d':(1,3,5,4,2)}
    idx = {name:ids[p] for name,p in named.items()}
    reverse = {i:name for name,i in idx.items()}
    bounds = []
    for name,i in idx.items():
        for other,j in idx.items():
            assert J[i][j] in reverse and M[i][j] in reverse
            bounds.append({'pair':[name,other],
                'join':reverse[J[i][j]],'meet':reverse[M[i][j]],
                'all_upper_bounds':[list(rows[k][0]) for k in range(len(rows))
                                    if order[i][k] and order[j][k]],
                'all_lower_bounds':[list(rows[k][0]) for k in range(len(rows))
                                    if order[k][i] and order[k][j]]})
    a,b,c = (idx[s] for s in ('a','b','c'))
    lhs = M[a][J[b][c]]
    rhs = J[M[a][b]][M[a][c]]
    assert lhs==a and rhs==b and a!=b
    observed = [tuple(cert['fiber'][i]['permutation']) for i in cert['failure']['triple']]
    assert observed == [named['a'],named['b'],named['c']]
    # Direct enumeration of the only four ambient lower candidates for a,c.
    lower_box = []
    for p,t,s in generate(5):
        if all(x<=y for x,y in zip(t,(0,0,1,0,1))):
            lower_box.append({'permutation':p,'iota':t,'pinnacles':s})
    assert len(lower_box)==4
    assert [x['permutation'] for x in lower_box if x['pinnacles']==(5,)]==[named['e']]
    output = {'job_id':'primary-20260914-pinnacle-fibers-triage-1b1fd3a827dc',
        'method':'inversion-vector enumeration; universal internal bounds; direct law',
        'fresh_mathematical_referee':False,'small_cases':small,
        'complete_fiber_size':len(rows),'all_pairs_have_internal_join_and_meet':True,
        'witness':{s:{'permutation':p,'iota':rows[idx[s]][1]} for s,p in named.items()},
        'distributivity':{'triple':['a','b','c'],'lhs':'a','rhs':'b','equal':False},
        'ambient_lower_box_for_a_c':lower_box,'five_element_sublattice_bounds':bounds,
        'discovery_certificate_sha256':hashlib.sha256(certpath.read_bytes()).hexdigest()}
    target = ROOT/'evidence/triage_verification.json'
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(output,indent=2)+'\n')
    tmp.replace(target)
    print(json.dumps({k:v for k,v in output.items() if k!='five_element_sublattice_bounds'}))

if __name__=='__main__':
    main()
