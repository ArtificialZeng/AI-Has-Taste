"""Independent verification: logarithmic derivatives and signed binomial sums.

No coefficient, margin or difference routines imported from the producer.
Every initial and doubled polynomial is reconstructed independently.
"""
import hashlib
import json
from math import comb
from pathlib import Path
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-subsum-denominator-research-077128f18f2f'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def coefficients(s,t,m):
    n = s*2**t
    extra = set()
    v = s
    while v%2 == 0:
        v //= 2
        extra.add(v)
    beta = [0]*(m+1)
    for i in range(1,m+1):
        e = int(i in extra)
        v = i
        while v < n:
            e += 1
            v *= 2
        for r in range(i,m+1,i):
            beta[r] += i*e*(1 if (r//i)%2 else -1)
    a = [1]
    for r in range(1,m+1):
        q,rem = divmod(sum(beta[k]*a[r-k] for k in range(1,r+1)),r)
        assert rem == 0
        a.append(q)
    return a

def at(a,r):
    return a[r] if 0<=r<len(a) else 0

def margin_vector(s,t,B):
    a = coefficients(s,t,B+1)
    # Direct expansion of the H quadratic, distinct from forming b.
    return [at(a,j)**2-at(a,j-1)*at(a,j+1)
        + at(a,j-s)**2-at(a,j-s-1)*at(a,j-s+1)
        + 4*at(a,j)*at(a,j-s)
        - 2*at(a,j-1)*at(a,j-s+1)
        - 2*at(a,j+1)*at(a,j-s-1) for j in range(B+1)]

def main():
    start = monotonic()
    path = ROOT/'evidence/research3_sharp_probe.json'
    data = json.loads(path.read_text())
    assert data['complete'] and data['j_range']==[65,96]
    B = 96
    expected = {(s,j) for j in range(65,97) for s in range(1,j+2)}
    assert len(data['records']) == len(expected)
    assert {(r['s'],r['j']) for r in data['records']} == expected
    cache = {}
    def vector(s,t):
        if (s,t) not in cache:
            cache[s,t] = margin_vector(s,t,B)
        return cache[s,t]
    pascal = [[(-1)**(h-v)*comb(h,v) for v in range(h+1)] for h in range(2*B+1)]
    count = zeros = holdouts = top = 0
    negative = []
    for r in data['records']:
        s,j,tau = r['s'],r['j'],r['tau']
        assert s*2**tau>=9 and 2*s*2**tau>j+1
        assert tau==0 or s*2**(tau-1)<9 or 2*s*2**(tau-1)<=j+1
        c = r['newton_coefficients']
        assert len(c) == 2*j+1
        vals = [vector(s,tau+v)[j] for v in range(2*j+1)]
        for h,x in enumerate(c):
            actual = sum(w*vals[v] for v,w in enumerate(pascal[h]))
            assert x == actual,(s,j,h)
            count += 1
            zeros += x == 0
            if actual<0:
                negative.append(dict(s=s,j=j,tau=tau,h=h,value=actual))
        C = comb(2*j,j)//(j+1)
        Cp = comb(2*j-2,j-1)//j
        a1 = coefficients(s,tau,1)[1]
        assert c[-1] == C
        assert c[-2] == (a1+2*(s==1))*C+(2*j-1)*(C-Cp)
        top += 2
        for u in (2*j+3,4*j+7):
            actual = vector(s,tau+u)[j]
            assert actual == sum(x*comb(u,h) for h,x in enumerate(c))
            holdouts += 1
    finite_expected = set()
    for s,j in expected:
        t = 0
        while 2*s*2**t <= j+1:
            if s*2**t >= 9:
                finite_expected.add((s,j,t))
            t += 1
    fr = data['earlier_finite_records']
    assert len(fr) == len(finite_expected)
    assert {(r['s'],r['j'],r['t']) for r in fr} == finite_expected
    for r in fr:
        assert r['n'] == r['s']*2**r['t'] >= 9
        assert r['margin'] == vector(r['s'],r['t'])[r['j']] >= 0
    assert count == data['newton_coefficients']
    assert negative == data['negative_coefficients'] == []
    out = dict(job_id=JOB,complete_domain=True,certificate_sha256=sha(path),
        implementation_sha256=sha(Path(__file__)),source_sha256=sha(ROOT/'source.md'),
        polynomials=len(expected),coefficients_recomputed=count,
        zero_coefficients=zeros,negative_coefficients=negative,
        earlier_finite_checks=len(fr),outside_grid_evaluations=holdouts,
        top_two_formula_checks=top,elapsed_seconds=round(monotonic()-start,3),
        scope='Separate exact implementation verification; not a fresh referee')
    dest = ROOT/'evidence/research3_verify.json'
    tmp = dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(dest)
    print(json.dumps(out,indent=2))

if __name__ == '__main__':
    main()
