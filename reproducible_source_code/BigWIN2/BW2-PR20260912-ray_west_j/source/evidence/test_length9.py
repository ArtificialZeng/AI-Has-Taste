"""Second range for unchanged E and D: python3 evidence/test_length9.py."""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json
import random
import time
import numpy as np
from test_length8 import upper_counts_fast, base, in_union, save, OUT, JOB
from test_statistics import direct_g2, standardize


def main():
    started = datetime.now(timezone.utc).isoformat()
    t0 = time.monotonic()
    old = json.loads((OUT/'exact-counts-length8.json').read_text())
    table = {tuple(r['beta']): r['j'] for r in old}
    counts, ambient = upper_counts_fast(9)
    assert ambient == factorial(11)
    np.save(OUT/'exact-counts-length9.npy', counts)
    print('Length 9 ambient census complete', time.monotonic()-t0, flush=True)
    failures, mismatches, changes, hist = [], [], Counter(), Counter()
    extremizers, selected = [], set()
    sample_ranks = set(random.Random(679509).sample(range(factorial(9)), 64))
    tested = 0
    for rank, p in enumerate(permutations(range(1, 10))):
        jp = base(9)-int(counts[rank])
        assert 0 <= jp <= 8
        hist[jp] += 1
        member = in_union(p)
        if (jp == 8) != member:
            mismatches.append({'beta': p, 'j': jp})
            selected.add(p)
        if jp == 8:
            extremizers.append(p); selected.add(p)
        if rank in sample_ranks:
            selected.add(p)
        for i in range(9):
            q = standardize(p[:i]+p[i+1:])
            change = jp-table[q]
            changes[change] += 1
            if change > 1:
                failures.append({'beta': p, 'gamma': q, 'deleted_position': i+1,
                                 'j_beta': jp, 'j_gamma': table[q]})
                selected.update([p, q])
        tested += 1
    print('Length 9 comparisons complete', time.monotonic()-t0, flush=True)
    checks = []
    for p in sorted(selected, key=lambda x: (len(x), x)):
        g = direct_g2(p)
        if len(p) == 9:
            rank = sum(sum(p[k]<p[i] for k in range(i+1, 9))*factorial(8-i)
                       for i in range(9))
            assert g == counts[rank]
        else:
            assert base(len(p))-g == table[p]
        checks.append({'beta': p, 'g2': g, 'j': base(len(p))-g})
    save('length9-insertion-checks.json', checks)
    report = {'job_id': JOB, 'started_utc': started,
              'completed_utc': datetime.now(timezone.utc).isoformat(),
              'protocol_sha256': hashlib.sha256((OUT/'length9-test-protocol.md').read_bytes()).hexdigest(),
              'ambient_permutations': int(ambient), 'deletion_pairs_per_ambient': 55,
              'patterns_tested': tested, 'deletion_comparisons': sum(changes.values()),
              'j_histogram': dict(sorted(hist.items())),
              'j_change_histogram': dict(sorted(changes.items())),
              'equality_mismatches': mismatches, 'deletion_violations': failures,
              'extremizers': len(extremizers), 'insertion_checks': len(checks),
              'counts_format': 'int64 numpy vector in lexicographic permutation order, storing g2',
              'elapsed_seconds': time.monotonic()-t0,
              'status': 'Exact finite observation; E and D remain unproved universally.'}
    save('length9-test.json', report)
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
