#!/usr/bin/env python3
"""Exact finite triage, standard library only; stop at first obstruction."""
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260914-pinnacle-fibers-triage-1b1fd3a827dc'

def atomic_json(path, data):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)

def pinnacles(p):
    return tuple(p[i] for i in range(1,len(p)-1) if p[i-1]<p[i]>p[i+1])

def table(p):
    t = [0]*len(p)
    for i,v in enumerate(p):
        t[v-1] = sum(u<v for u in p[i+1:])
    return tuple(t)

def le(a,b):
    return all(x<=y for x,y in zip(a,b))

def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask ^= bit

def admissible(n,sigma):
    if not sigma:
        return True
    S = set(sigma)
    if max(S)>n:
        return False
    for x in S:
        small = {v for v in S if v<=x}
        if 2*len(small)>=x:
            return False
        flags = [v in small for v in sigma]
        runs = sum(f and (i==0 or not flags[i-1]) for i,f in enumerate(flags))
        if runs-1>x-2*len(small)-1:
            return False
    return True

def inspect(fiber):
    # Sorting by inversion sum makes the first possible upper bound minimal
    # and the last possible lower bound maximal. We additionally verify that
    # each chosen bound compares correctly with EVERY other common bound.
    fiber = sorted(fiber, key=lambda pt:(sum(pt[1]),pt[1]))
    ts = [t for p,t in fiber]
    m = len(ts)
    up = [0]*m
    down = [0]*m
    for i,a in enumerate(ts):
        for j in range(i,m):
            if le(a,ts[j]):
                up[i] |= 1<<j
                down[j] |= 1<<i
    # In a finite lattice, a join-irreducible has a unique lower cover.
    irreducibles = []
    for i in range(m):
        strict = down[i] & ~(1<<i)
        if strict:
            c = strict.bit_length()-1
            if strict & ~down[c] == 0:
                irreducibles.append(i)
    jmasks = [sum(1<<k for k,j in enumerate(irreducibles) if down[i]>>j&1)
              for i in range(m)]
    join = [[0]*m for _ in range(m)]
    meet = [[0]*m for _ in range(m)]
    prime_failure = None
    for i in range(m):
        for j in range(i,m):
            U = up[i]&up[j]
            L = down[i]&down[j]
            u = (U & -U).bit_length()-1
            l = L.bit_length()-1
            if not U or U & ~up[u]:
                mins = [k for k in bits(U) if down[k]&U == 1<<k]
                return fiber, {'kind':'no_join','pair':[i,j],
                    'common_upper_bounds':list(bits(U)), 'minimal_upper_bounds':mins}
            if not L or L & ~down[l]:
                maxs = [k for k in bits(L) if up[k]&L == 1<<k]
                return fiber, {'kind':'no_meet','pair':[i,j],
                    'common_lower_bounds':list(bits(L)), 'maximal_lower_bounds':maxs}
            join[i][j] = join[j][i] = u
            meet[i][j] = meet[j][i] = l
            diff = jmasks[u] & ~(jmasks[i]|jmasks[j])
            if diff and prime_failure is None:
                k = (diff & -diff).bit_length()-1
                prime_failure = (irreducibles[k],i,j)
    # All joins/meets exist. A finite lattice is distributive iff every
    # join-irreducible is join-prime. Report a direct law violation if not.
    if prime_failure:
        a,b,c = prime_failure
        lhs = meet[a][join[b][c]]
        rhs = join[meet[a][b]][meet[a][c]]
        assert lhs != rhs
        return fiber, {'kind':'nondistributive','triple':[a,b,c],
                       'lhs':lhs,'rhs':rhs}
    return fiber, None

def main():
    start = time.monotonic()
    results = {'job_id':JOB,'arithmetic':'exact Python integers',
               'completed':[], 'failure':None}
    for n in range(8):
        fibers = defaultdict(list)
        for p in permutations(range(1,n+1)):
            fibers[pinnacles(p)].append((p,table(p)))
        assert sum(map(len,fibers.values())) == math.factorial(n)
        # Exhaust all distinct-value sequences, including inadmissible ones.
        expected = {()}
        for k in range(1,n+1):
            for s in permutations(range(1,n+1),k):
                if admissible(n,s):
                    expected.add(s)
        assert set(fibers) == expected, ('admissibility mismatch',n)
        checked = 0
        for sigma,fiber in sorted(fibers.items()):
            ordered, failure = inspect(fiber)
            checked += 1
            if failure:
                cert = {'job_id':JOB,'n':n,'sigma':sigma,
                        'fiber':[{'permutation':p,'iota':t} for p,t in ordered],
                        'failure':failure}
                atomic_json(ROOT/'evidence/triage_obstruction.json',cert)
                results['failure'] = {'n':n,'sigma':sigma,'size':len(fiber),
                    'kind':failure['kind'],'fibers_tested_at_this_n':checked,
                    'certificate':'evidence/triage_obstruction.json'}
                results['elapsed_seconds'] = time.monotonic()-start
                atomic_json(ROOT/'evidence/triage_exact_results.json',results)
                print(json.dumps(results),flush=True)
                return
        row = {'n':n,'permutations':math.factorial(n),'fibers':len(fibers),
               'all_induced_lattices_distributive':True,
               'admissibility_criterion_agrees':True}
        results['completed'].append(row)
        results['elapsed_seconds'] = time.monotonic()-start
        atomic_json(ROOT/'evidence/triage_exact_results.json',results)
        print(json.dumps(row),flush=True)
    print(json.dumps(results),flush=True)

if __name__ == '__main__':
    main()
