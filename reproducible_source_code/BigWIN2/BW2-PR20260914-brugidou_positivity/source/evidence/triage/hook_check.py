#!/usr/bin/env python3
"""Exact triage checks; no claim of an all-partition proof or new finite coverage."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
def clean(p):
    return {k: v for k, v in p.items() if v}
def add(p, r, scale=1, shift=0):
    z = defaultdict(Q, p)
    for k, v in r.items():
        z[k + shift] += scale * v
    return clean(z)
def mul(p, r):
    z = defaultdict(Q)
    for k, v in p.items():
        for j, w in r.items():
            z[k + j] += v * w
    return clean(z)
def divide_one_minus_q(p):
    z = {}; acc = Q(0)
    for k in range(max(p) + 1):
        acc += p.get(k, 0)
        if acc:
            z[k] = acc
    assert acc == 0, 'nonzero remainder at q=1'
    return z
@lru_cache(None)
def power(n):
    # Newton: p_n = (-1)^(n-1)n e_n + sum (-1)^(j-1)e_j p_(n-j).
    z = {comb(n, 2): Q((-1)**(n-1), factorial(n-1))}
    for j in range(1, n):
        z = add(z, power(n-j), Q((-1)**(j-1), factorial(j)), comb(j, 2))
    return z
@lru_cache(None)
def augmented(lam):
    if len(lam) == 1:
        return power(lam[0])
    a, rest = lam[-1], lam[:-1]
    z = mul(power(a), augmented(rest))
    for i in range(len(rest)):
        merged = list(rest); merged[i] += a
        z = add(z, augmented(tuple(sorted(merged, reverse=True))), -1)
    return z
@lru_cache(None)
def tree(n):
    z = {k: factorial(n-1)*v for k, v in power(n).items()}
    for _ in range(n-1):
        z = divide_one_minus_q(z)
    assert all(v.denominator == 1 for v in z.values())
    return z
@lru_cache(None)
def K(a, b):
    if a == 2:
        return {k: Q(1) for k in range(b+1)}
    z = {k: comb(a+b-1, a-2)*v for k, v in tree(a-1).items()}
    z = add(z, K(a-1, b+1), -1, b+1)
    return divide_one_minus_q(z)
def row(p):
    assert all(v.denominator == 1 for v in p.values())
    return [int(p.get(k, 0)) for k in range(max(p)+1)]

definition_checks = 0
for n in range(2, 11):
    for a in range(2, n+1):
        b = n-a
        lhs = augmented((a,)+(1,)*b)
        rhs = {k+comb(b+1, 2): factorial(b)*v/Q(factorial(n-1)) for k, v in K(a,b).items()}
        for _ in range(a-1):
            rhs = mul(rhs, {0:Q(1), 1:Q(-1)})
        assert lhs == rhs, (a,b)
        definition_checks += 1
calibration = json.loads((ROOT/'evidence/intake/calibrate.json').read_text())
calibration_checks = 0
for r in calibration['rows']:
    lam = r['partition']
    if lam[0] >= 2 and all(x == 1 for x in lam[1:]):
        a,b = lam[0],len(lam)-1
        assert [factorial(b)*v for v in row(K(a,b))] == r['coefficients']
        calibration_checks += 1
for b in range(31):
    explicit = [b+2]*(b+1)+list(range(b+1,0,-1))
    assert row(K(3,b)) == explicit
boundaries=[]
for a in range(3,13):
    cutoff=max(0,comb(a-2,2)-1)
    for b in sorted({max(0,cutoff-1),cutoff,cutoff+1}):
        v=row(K(a,b)); assert min(v)>0
        assert len(v)-1 == comb(a-1,2)+(a-1)*b
        boundaries.append({'a':a,'b':b,'cutoff':cutoff,'degree':len(v)-1,
                           'min_coefficient':min(v),'coefficient_sha256':
                           hashlib.sha256(json.dumps(v).encode()).hexdigest()})
result={
    'job_id':'primary-20260914-brugidou-positivity-triage-820b8c1104a3',
    'arithmetic':'exact integers and fractions.Fraction; deterministic',
    'definition_checks':definition_checks,'definition_max_size':10,
    'prior_calibration_hook_checks':calibration_checks,'prior_calibration_max_size':12,
    'explicit_a3_checks':31,'explicit_a3_b_range':[0,30],
    'cutoff_cases':boundaries,'failures':[],
    'qualification':'Checks validate formulas and boundaries only; analytic induction is in hook-route.md. No universal positivity or novelty follows from these computations.',
    'source_sha256':hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cutoff_cases'}))
print('cutoff cases:',len(boundaries))
