"""Small recovery check using independent standard-library polynomial arithmetic.

Run from any directory with python3. Does not modify the prior attempt's files.
This verifies finite identities only; it is not a mathematical referee pass.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
JOB = 'primary-20260913-qdescent-logconcavity-triage-88d4196c29cf'

def add(*polys):
    ans = Counter()
    for p in polys:
        for e, c in p.items():
            ans[e] += c
    return Counter({e: c for e, c in ans.items() if c})

def shift(p, n):
    return Counter({e+n: c for e, c in p.items()})

def neg(p):
    return Counter({e: -c for e, c in p.items()})

def mul(p, t):
    ans = Counter()
    for e, c in p.items():
        for f, d in t.items():
            ans[e+f] += c*d
    return Counter({e: c for e, c in ans.items() if c})

@lru_cache(None)
def gaussian(n, k):
    if not 0 <= k <= n:
        return Counter()
    return Counter(sum(t)-k*(k-1)//2 for t in combinations(range(n), k))

def kernel(m, k, r):
    if not 1 <= k <= m:
        return Counter()
    return shift(add(gaussian(m, k), neg(gaussian(m-r, k))), k*k)

def desc(p):
    return {i+1 for i in range(len(p)-1) if p[i] > p[i+1]}

def inv(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))

def main():
    direct_checks = 0
    for m in range(1, 4):
        for mask in range(1 << (m-1)):
            T = {i+1 for i in range(m-1) if mask >> i & 1}
            S = T | {m}
            x = [Counter() for _ in range(m)]
            for p in permutations(range(1, m+1)):
                if desc(p) == T:
                    x[p[-1]-1][inv(p)] += 1
            for k in range(1, m+1):
                direct = Counter()
                for p in permutations(range(1, m+k+1)):
                    if desc(p) == S and set(range(m+1, m+k+1)) <= set(p[:m]):
                        direct[inv(p)] += 1
                reduced = add(*(mul(kernel(m, k, r), x[r-1]) for r in range(1, m+1)))
                assert direct == reduced and direct, (S, k)
                direct_checks += 1
    suffix_checks = 0
    pairs = {'strict': 0, 'diagonal': 0}
    for m in range(1, 5):
        for k in range(1, m+1):
            for r in range(1, m+1):
                suffix = add(*(shift(gaussian(m-h, k-1), k*(k-1)+m+1-h)
                               for h in range(1, min(r, m-k+1)+1)))
                assert suffix == kernel(m, k, r) and suffix
                assert all(c >= 0 for c in suffix.values())
                suffix_checks += 1
        for i in range(1, m+1):
            for j in range(i, m+1):
                for r in range(1, m+1):
                    for s in range(r, m+1):
                        z = add(mul(kernel(m, i, r), kernel(m, j, s)),
                                neg(mul(kernel(m, i-1, r), kernel(m, j+1, s))))
                        if r != s:
                            z = add(z, mul(kernel(m, i, s), kernel(m, j, r)),
                                    neg(mul(kernel(m, i-1, s), kernel(m, j+1, r))))
                        assert all(c >= 0 for c in z.values()), (m, i, j, r, s, z)
                        pairs['strict' if i < j else 'diagonal'] += 1
    files = ['source.md', 'evidence/external/gaetz-gao-1912.04933v2.html',
             'evidence/intake/triage-kernel-reduction.md',
             'evidence/intake/triage-kernel-check.py',
             'evidence/intake/triage-kernel-check.json',
             'evidence/intake/qdescent-calibration.py',
             'literature/triage-screen.md', 'literature/operational-recovery-handoff.md',
             'evidence/intake/triage-recovery-check.py']
    hashes = {f: hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}
    assert hashes['source.md'] == '09b28e35bf37a42405472803e963d8cd37dce27edee55c075e7689eab2781fcb'
    result = dict(job_id=JOB, arithmetic='exact integer sparse polynomials; no imported project arithmetic',
                  direct_a_checks=direct_checks, direct_range='all nonempty S with max S <= 3; every 1 <= k <= max S',
                  kernel_suffix_checks=suffix_checks, kernel_range='all 1 <= k,r <= m <= 4',
                  target_k_checks=pairs, target_k_range='all 1 <= i <= j <= m <= 4 and 1 <= r <= s <= m',
                  failures=[], sha256=hashes,
                  conclusion='Small recovery replay passed. Uniform Target K remains unproved. No fresh referee or novelty certification.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
