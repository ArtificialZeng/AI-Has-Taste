"""Exact bounded intake checks, not a proof of Gaetz--Gao Conjecture 7."""
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import hashlib
import json
import platform
import time

def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    while c and not c[-1]: c.pop()
    return tuple(c)

def mul(a, b):
    if not a or not b: return ()
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return tuple(c)

def shift(a, k): return (0,) * k + a if a else ()

@lru_cache(None)
def gaussian(n, k):
    if k < 0 or k > n: return ()
    if k in (0, n): return (1,)
    return add(gaussian(n-1, k), shift(gaussian(n-1, k-1), n-k))

def b_polys(S, m):
    b = [(1,)]
    for n in range(2, m+2):
        new = []
        for k in range(1, n+1):
            options = b[k-1:] if n-1 in S else b[:k-1]
            total = ()
            for p in options: total = add(total, p)
            new.append(shift(total, n-k))
        b = new
    return b[:m]

def a_polys(S, m):
    b = b_polys(S, m)
    a = [()]
    for k in range(1, m+1):
        total = ()
        for i in range(1, m-k+2):
            total = add(total, mul(gaussian(m-i, k-1), b[i-1]))
        a.append(shift(total, k*(k-1)))
    return a + [()]

def direct_a(S, m, k):
    n = m+k
    coeff = ()
    for p in permutations(range(1, n+1)):
        if {i+1 for i in range(n-1) if p[i] > p[i+1]} != S: continue
        if not set(range(m+1, n+1)).issubset(p[:m]): continue
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        coeff = add(coeff, (0,)*inv+(1,))
    return coeff

def main():
    t0 = time.perf_counter()
    source_path = Path(__file__).with_name('gaetz-gao-1912.04933v2.html')
    if not source_path.is_file():
        source_path = Path(__file__).parent.parent / 'external/gaetz-gao-1912.04933v2.html'
    failures, direct_failures, support_failures = [], [], []
    sets = pairs = direct = 0
    for m in range(1, 9):
        for mask in range(1 << (m-1)):
            S = {m} | {i+1 for i in range(m-1) if mask >> i & 1}
            a = a_polys(S, m)
            sets += 1
            nonzero = [k for k in range(1, m+1) if a[k]]
            if nonzero and nonzero != list(range(min(nonzero), max(nonzero)+1)):
                support_failures.append({'S':sorted(S), 'support':nonzero})
            for i in range(1, m+1):
                for j in range(i, m+1):
                    pairs += 1
                    lhs, rhs = mul(a[i], a[j]), mul(a[i-1], a[j+1])
                    diff = add(lhs, tuple(-x for x in rhs))
                    negative = [(d,c) for d,c in enumerate(diff) if c < 0]
                    if negative:
                        failures.append({'S':sorted(S),'i':i,'j':j,'negative_coefficients':negative,'a':[list(p) for p in a]})
            if m <= 3:
                for k in range(1, m+1):
                    direct += 1
                    d = direct_a(S,m,k)
                    if d != a[k]: direct_failures.append({'S':sorted(S),'k':k,'direct':d,'transform':a[k]})
    result = {'python':platform.python_version(),'arithmetic':'exact integer coefficient arrays; no randomness or floating-point mathematics',
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_html_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
              'range':'All nonempty S with max(S)=m, 1<=m<=8; every 1<=i<=j<=m, a0=a(m+1)=0',
              'sets':sets,'coefficient_inequalities':pairs,'direct_definition_checks':direct,
              'direct_range':'All S with max(S)<=3, every1<=k<=max(S); enumerate Sym(m+k)',
              'failures':failures,'direct_failures':direct_failures,'support_failures':support_failures,
              'seconds':time.perf_counter()-t0,'conclusion':'Finite calibration only; no uniform proof or independent holdout claim.'}
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__ == '__main__': main()
