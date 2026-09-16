"""Exploratory direct-sum rule suggested by active track geometry.

For nonempty alpha,beta:
j(alpha direct-sum beta) = j(alpha)+j(beta)+e(alpha,beta),
where e=1 exactly when the last sum-indecomposable component of alpha
and the first sum-indecomposable component of beta are both decreasing.

The rule is unproved. Tested against independently obtained g2 counts.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import json
import numpy as np
from test_length8 import base, save, OUT, JOB


def terminal_decreasing(p):
    m = len(p)
    for k in range(1, m+1):
        if set(p[m-k:]) == set(range(m-k+1, m+1)):
            return p[m-k:] == tuple(range(m, m-k, -1))
    raise AssertionError


def initial_decreasing(p):
    for k in range(1, len(p)+1):
        if set(p[:k]) == set(range(1, k+1)):
            return p[:k] == tuple(range(k, 0, -1))
    raise AssertionError


def main():
    rows = json.loads((OUT/'exact-counts.json').read_text())
    rows += json.loads((OUT/'exact-counts-length8.json').read_text())
    table = {tuple(r['beta']): r['j'] for r in rows}
    td = {p: terminal_decreasing(p) for p in table}
    hd = {p: initial_decreasing(p) for p in table}
    failures, hist, coverage = [], Counter(), Counter()
    raw9 = np.load(OUT/'exact-counts-length9.npy')
    def all_rows():
        yield from table.items()
        yield from ((p, base(9)-int(raw9[r])) for r, p in
                    enumerate(permutations(range(1, 10))))
    for p, jp in all_rows():
        m = len(p)
        for i in range(1, m):
            if max(p[:i]) != i:
                continue
            a, b = p[:i], tuple(v-i for v in p[i:])
            correction = jp-table[a]-table[b]
            predicted = int(td[a] and hd[b])
            hist[correction] += 1
            coverage[m] += 1
            if correction != predicted:
                failures.append({'beta': p, 'cut': i, 'alpha': a, 'gamma': b,
                                 'j': jp, 'j_alpha': table[a], 'j_gamma': table[b],
                                 'correction': correction, 'predicted': predicted})
    report = {'job_id': JOB, 'status': 'Exploratory unproved direct-sum rule',
              'formula': __doc__, 'coverage_by_total_length': dict(coverage),
              'sum_cuts_tested': sum(coverage.values()),
              'correction_histogram': dict(sorted(hist.items())),
              'failure_count': len(failures), 'first_failures': failures[:8]}
    save('sum-rule-test.json', report)
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
