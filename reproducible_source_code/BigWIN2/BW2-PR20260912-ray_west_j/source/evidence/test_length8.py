"""Exact ambient-deletion census. Run from project: python3 evidence/test_length8.py.

Single foreground process; numba accelerates integer loops, without parallelism.
No symmetry reductions: next_permutation visits every element of S_(m+2).
Every pair of deleted positions is considered. A timestamp array counts each
standardized pattern only once per ambient permutation. Ranks are Lehmer ranks.
"""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations, combinations
from math import factorial
from pathlib import Path
import hashlib
import json
import random
import time
import numpy as np
from numba import njit
from test_statistics import direct_g2, standardize

OUT = Path(__file__).resolve().parent
JOB = 'primary-20260912-ray-west-j-research-6795cc8901c9'


@njit
def upper_counts_fast(m):
    n = m + 2
    fac = np.ones(n+1, dtype=np.int64)
    for i in range(1, n+1):
        fac[i] = fac[i-1]*i
    pop = np.zeros(1 << n, dtype=np.int64)
    for i in range(1, 1 << n):
        pop[i] = pop[i >> 1] + (i & 1)
    counts = np.zeros(fac[m], dtype=np.int64)
    seen = np.full(fac[m], -1, dtype=np.int64)
    p = np.arange(n)
    serial = 0
    while True:
        for a in range(n):
            for b in range(a+1, n):
                x, y = p[a], p[b]
                rank, bits, k = 0, 0, 0
                for pos in range(n):
                    if pos == a or pos == b:
                        continue
                    v = p[pos]
                    digit = v - (x < v) - (y < v) - pop[bits & ((1 << v)-1)]
                    rank += digit*fac[m-k-1]
                    bits |= 1 << v
                    k += 1
                if seen[rank] != serial:
                    counts[rank] += 1
                    seen[rank] = serial
        serial += 1
        i = n - 2
        while i >= 0 and p[i] >= p[i+1]:
            i -= 1
        if i < 0:
            break
        j = n - 1
        while p[j] <= p[i]:
            j -= 1
        p[i], p[j] = p[j], p[i]
        lo, hi = i+1, n-1
        while lo < hi:
            p[lo], p[hi] = p[hi], p[lo]
            lo += 1
            hi -= 1
    return counts, serial


def base(m):
    return (m**4 + 2*m**3 + m*m + 4*m + 4)//2


def in_union(p):
    pats = {standardize(t) for t in combinations(p, 3)}
    return (not pats.intersection({(2, 3, 1), (3, 1, 2)}) or
            not pats.intersection({(1, 3, 2), (2, 1, 3)}))


def save(name, obj):
    tmp = OUT / (name + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2) + '\n')
    tmp.replace(OUT / name)


def main():
    started = datetime.now(timezone.utc).isoformat()
    t0 = time.monotonic()
    old_rows = json.loads((OUT/'exact-counts.json').read_text())
    old = {tuple(r['beta']): r['g2'] for r in old_rows}
    validation = []
    for m in range(1, 8):
        counts, ambient = upper_counts_fast(m)
        assert ambient == factorial(m+2)
        for rank, p in enumerate(permutations(range(1, m+1))):
            assert int(counts[rank]) == old[p], (p, counts[rank], old[p])
        validation.append({'m': m, 'patterns': factorial(m), 'ambient': ambient})
        print('Validated all m=', m, 'elapsed=', time.monotonic()-t0, flush=True)
    save('length8-progress.json', {'job_id': JOB, 'validation': validation,
                                 'status': 'baseline validated; length 8 pending'})
    counts, ambient = upper_counts_fast(8)
    assert ambient == factorial(10)
    ps = list(permutations(range(1, 9)))
    rows = [{'beta': p, 'g2': int(counts[r]), 'j': base(8)-int(counts[r])}
            for r, p in enumerate(ps)]
    assert len(rows) == factorial(8)
    assert all(0 <= r['j'] <= 7 for r in rows)
    save('exact-counts-length8.json', rows)
    print('Length 8 counted; elapsed=', time.monotonic()-t0, flush=True)
    table = {p: base(len(p))-g for p, g in old.items()}
    table.update({tuple(r['beta']): r['j'] for r in rows})
    failures, mismatches, changes = [], [], Counter()
    extremizers = []
    for r in rows:
        p, jp = tuple(r['beta']), r['j']
        member = in_union(p)
        if (jp == 7) != member:
            mismatches.append(r)
        if jp == 7:
            extremizers.append(p)
        for i in range(8):
            q = standardize(p[:i]+p[i+1:])
            change = jp-table[q]
            changes[change] += 1
            if change > 1:
                failures.append({'beta': p, 'gamma': q, 'deleted_position': i+1,
                                 'j_beta': jp, 'j_gamma': table[q]})
    selected = set(extremizers + random.Random(6795).sample(ps, 64))
    selected.update(tuple(r['beta']) for r in mismatches)
    for f in failures:
        selected.update([f['beta'], f['gamma']])
    checks = []
    for p in sorted(selected, key=lambda x: (len(x), x)):
        g = direct_g2(p)
        assert base(len(p))-g == table[p], (p, g, table[p])
        checks.append({'beta': p, 'g2': g, 'j': table[p]})
    save('length8-insertion-checks.json', checks)
    report = {'job_id': JOB, 'started_utc': started,
              'completed_utc': datetime.now(timezone.utc).isoformat(),
              'protocol_sha256': hashlib.sha256((OUT/'research-test-protocol.md').read_bytes()).hexdigest(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'baseline_validation': validation,
              'ambient_permutations': int(ambient), 'deletion_pairs_per_ambient': 45,
              'patterns_tested': len(rows), 'deletion_comparisons': sum(changes.values()),
              'j_histogram': dict(sorted(Counter(r['j'] for r in rows).items())),
              'j_change_histogram': dict(sorted(changes.items())),
              'equality_mismatches': mismatches, 'deletion_violations': failures,
              'extremizers': len(extremizers), 'insertion_checks': len(checks),
              'elapsed_seconds': time.monotonic()-t0,
              'status': 'Exact finite observation; E and D remain unproved universally.'}
    save('length8-test.json', report)
    save('length8-progress.json', {'job_id': JOB, 'status': 'complete',
                                 'report': 'evidence/length8-test.json'})
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
