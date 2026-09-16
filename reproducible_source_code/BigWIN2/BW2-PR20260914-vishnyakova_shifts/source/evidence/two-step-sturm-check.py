"""Recompute the three obstruction witnesses with fractions only, no SymPy.

This is a second exact implementation, not an independent mathematical audit.
"""
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
assert hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest() == '599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8'
data = json.loads((ROOT/'evidence/two-step-pass-2.json').read_text())


def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def remainder(p, q):
    p = p[:]
    while len(p) >= len(q):
        factor, offset = p[-1]/q[-1], len(p)-len(q)
        for j, v in enumerate(q):
            p[j+offset] -= factor*v
        trim(p)
    return p


def normalize(p):
    return [v/abs(p[-1]) for v in p] if p else []


def sturm(p):
    seq = [normalize(p), normalize([j*p[j] for j in range(1, len(p))])]
    while seq[-1]:
        rem = remainder(seq[-2], seq[-1])
        if not rem:
            break
        seq.append(normalize([-v for v in rem]))
    return seq


def sign(v):
    return int(v > 0)-int(v < 0)


def variations(seq, endpoint):
    signs = []
    for p in seq:
        if endpoint == 'inf':
            val = sign(p[-1])
        elif endpoint == '-inf':
            val = sign(p[-1])*(-1)**(len(p)-1)
        else:
            val = F(0)
            for c in reversed(p):
                val = val*endpoint+c
            val = sign(val)
        if val:
            signs.append(val)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def multiply_linear(p, root):
    q = [F(0)]*(len(p)+1)
    for j, c in enumerate(p):
        q[j] -= root*c
        q[j+1] += c
    return q


def operator(p, t):
    q = [F(0)]*(len(p)+1)
    for j, c in enumerate(p):
        q[j] += (t+j)*c
        q[j+1] += (j+1)*c
    return q


results = []
for witness in data['configuration_only_obstructions']+[data['false_larger_strip_extension']]:
    roots = [F(r) for r in witness['input_roots']]
    assert len(set(roots)) == len(roots)
    assert sum(-1 < r < 0 for r in roots) == len(roots)-1
    assert sum(r > 0 for r in roots) == 1
    p = [F(1)]
    for r in roots:
        p = multiply_linear(p, r)
    t = F(witness['t'])
    q = operator(operator(p, t), t)
    seq = sturm(q)
    assert len(seq[-1]) == 1
    endpoints = ['-inf', F(-1), F(0), 'inf']
    vs = [variations(seq, v) for v in endpoints]
    counts = [vs[j]-vs[j+1] for j in range(3)]
    expected = witness['output_counts']
    assert counts == [expected['below_minus_one'], expected['minus_one_to_zero'], expected['positive']]
    assert len(q)-1-sum(counts) == 2
    results.append({'t': str(t), 'input_roots': [str(v) for v in roots],
        'output_coefficients_ascending': [str(v) for v in q],
        'sturm_variations_minus_inf_minus1_zero_inf': vs,
        'root_counts_below_minus1_minus1_to0_positive': counts,
        'gcd_degree': 0, 'nonreal_root_count': 2})

out = {'job_id': 'primary-20260914-vishnyakova-shifts-research-2008cf198145',
       'method': 'Python fractions.Fraction coefficient recurrence and Euclidean Sturm sequence; no SymPy imported.',
       'witnesses': results,
       'scope': 'Independent implementation for the three generic-operator counterexamples only; not a fresh referee or an audit of all-degree claims.'}
path = ROOT/'evidence/two-step-sturm-check.json'
tmp = path.with_suffix('.json.tmp')
tmp.write_text(json.dumps(out, indent=2)+'\n')
os.replace(tmp, path)
print(json.dumps(out, indent=2))
