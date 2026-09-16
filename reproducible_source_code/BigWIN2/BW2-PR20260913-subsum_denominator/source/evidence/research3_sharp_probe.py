"""Held-out exact test of the unchanged K_sharp_v1, 65 <= j <= 96.

Producer: sparse shift/add products, the exact doubling identity, and
successive differences. No imports from prior coefficient implementations.
"""
import hashlib
import json
from pathlib import Path
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260913-subsum-denominator-research-077128f18f2f'
LOW, HIGH = 65, 96

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, obj):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2) + '\n')
    tmp.replace(path)

def multiply_shift(a, i):
    for r in range(len(a)-1, i-1, -1):
        a[r] += a[r-i]

def initial(s, t):
    n = s << t
    a = [1] + [0]*(HIGH+1)
    for i in range(1, HIGH+2):
        for _ in range(((n-1)//i).bit_length()):
            multiply_shift(a, i)
    i = s//(s & -s)
    while i < s:
        multiply_shift(a, i)
        i *= 2
    return a

def get(a, r):
    return a[r] if 0 <= r < len(a) else 0

def minor(a, r):
    return get(a, r)**2 - get(a, r-1)*get(a, r+1)

def margin_vector(a, s):
    b = [get(a, r)+get(a, r-s) for r in range(HIGH+2)]
    return [2*minor(b,r)-minor(a,r)-minor(a,r-s) for r in range(HIGH+1)]

def differences(v):
    c = []
    while v:
        c.append(v[0])
        v = [v[i+1]-v[i] for i in range(len(v)-1)]
    return c

def main():
    start = monotonic()
    path = ROOT/'evidence/research3_sharp_probe.json'
    out = dict(job_id=JOB, kernel_version='K_sharp_v1',
        scope='Held-out range 65<=j<=96; all 1<=s<=j+1, 0<=h<=2j',
        j_range=[LOW,HIGH], complete=False, records=[], earlier_finite_records=[],
        negative_coefficients=[], negative_earlier_margins=[],
        source_sha256=sha(ROOT/'source.md'),
        frozen_definition_sha256=sha(ROOT/'evidence/research2.md'),
        implementation_sha256=sha(Path(__file__)))
    for s in range(1, HIGH+2):
        tmin = 0
        while (s << tmin) < 9:
            tmin += 1
        tmax = tmin
        while 2*(s << tmax) <= HIGH+1:
            tmax += 1
        a = initial(s,tmin)
        vals = {}
        for t in range(tmin,tmax+2*HIGH+1):
            vals[t] = margin_vector(a,s)
            # A_(s,t+1)/A_(s,t) = product_(1<=i<2n)(1+x^i).
            for i in range(1,min(HIGH+1,2*(s<<t)-1)+1):
                multiply_shift(a,i)
        for j in range(max(LOW,s-1),HIGH+1):
            tau = tmin
            while 2*(s<<tau) <= j+1:
                tau += 1
            c = differences([vals[tau+v][j] for v in range(2*j+1)])
            out['records'].append(dict(s=s,j=j,tau=tau,newton_coefficients=c))
            out['negative_coefficients'].extend(
                dict(s=s,j=j,tau=tau,h=h,value=v) for h,v in enumerate(c) if v<0)
            for t in range(tmin,tau):
                r = dict(s=s,j=j,t=t,n=s<<t,margin=vals[t][j])
                out['earlier_finite_records'].append(r)
                if r['margin']<0:
                    out['negative_earlier_margins'].append(r)
        if s%16 == 0 or s == HIGH+1:
            out['completed_shifts'] = s
            out['elapsed_seconds'] = round(monotonic()-start,3)
            save(path,out)
            print(json.dumps(dict(s=s, polynomials=len(out['records']),
                negatives=len(out['negative_coefficients']),elapsed=out['elapsed_seconds'])),flush=True)
    out.update(complete=True,polynomials=len(out['records']),
        newton_coefficients=sum(len(r['newton_coefficients']) for r in out['records']),
        earlier_finite_checks=len(out['earlier_finite_records']),
        elapsed_seconds=round(monotonic()-start,3))
    save(path,out)
    print(json.dumps({k:v for k,v in out.items() if k not in ['records','earlier_finite_records']},indent=2))

if __name__ == '__main__':
    main()
