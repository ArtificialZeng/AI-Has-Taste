"""Test the stronger gap restriction lemma needed for a proof of the sum rule."""
import json
from pathlib import Path
from collections import Counter
from inspect_active_pairs import active_pairs
from test_sum_rule import terminal_decreasing, initial_decreasing
from test_length8 import save, OUT, JOB


def main():
    rows = json.loads((OUT/'exact-counts.json').read_text())
    table = {}
    failures = []
    coverage = Counter()
    for row in sorted(rows, key=lambda r: (len(r['beta']), r['beta'])):
        p = tuple(row['beta'])
        m = len(p)
        gaps = {x['gap_zero_based'] for x in active_pairs(p)}
        assert len(gaps) == row['j']
        table[p] = gaps
        for i in range(1, m):
            if max(p[:i]) != i:
                continue
            a, b = p[:i], tuple(v-i for v in p[i:])
            want = set(table[a]) | {k+i for k in table[b]}
            if terminal_decreasing(a) and initial_decreasing(b):
                want.add(i-1)
            coverage[m] += 1
            if want != gaps:
                failures.append({'beta': p, 'cut': i, 'actual': sorted(gaps),
                                 'predicted': sorted(want)})
    report = {'job_id': JOB,
              'statement': 'For alpha direct-sum beta, the good gaps within each summand are exactly its original good gaps. The join is good iff both incident sum-indecomposable components are decreasing.',
              'status': 'Exact finite exploratory test; universal restriction lemma unproved.',
              'patterns_validated': len(table), 'sum_cuts_tested': sum(coverage.values()),
              'coverage_by_length': dict(coverage), 'failure_count': len(failures),
              'first_failures': failures[:8]}
    save('sum-gap-test.json', report)
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
