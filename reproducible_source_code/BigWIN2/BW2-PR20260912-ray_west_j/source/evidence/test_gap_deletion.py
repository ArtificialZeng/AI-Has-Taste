"""Test stronger local sufficient lemmas for D; exploratory, not pre-registered E data."""
import json
import time
from pathlib import Path
from inspect_active_pairs import active_pairs
from test_statistics import standardize

OUT = Path(__file__).resolve().parent
JOB = 'primary-20260912-ray-west-j-research-6795cc8901c9'


def main():
    rows = json.loads((OUT/'exact-counts.json').read_text())
    table, records = {}, {}
    failures, contraction, checked = [], [], 0
    for row in sorted(rows, key=lambda r: (len(r['beta']), r['beta'])):
        p = tuple(row['beta'])
        m = len(p)
        if m > 6:
            break
        matches = active_pairs(p)
        gaps = {x['gap_zero_based'] for x in matches}
        assert len(gaps) == row['j'], (p, row['j'], matches)
        table[p] = gaps
        records[p] = matches
        if m == 1:
            continue
        for i in range(m):
            q = standardize(p[:i]+p[i+1:])
            qgaps = table[q]
            checked += 1
            for k in gaps:
                if i not in (k, k+1):
                    l = k-(i<k)
                    if l not in qgaps:
                        failures.append({'beta': p, 'gamma': q, 'deleted_position': i+1,
                                         'lost_gap': k+1, 'beta_good_gaps': sorted(gaps),
                                         'gamma_good_gaps': sorted(qgaps),
                                         'beta_configurations': matches,
                                         'gamma_configurations': records[q]})
            if i-1 in gaps and i in gaps and i-1 not in qgaps:
                contraction.append({'beta': p, 'gamma': q, 'deleted_position': i+1,
                                    'beta_good_gaps': sorted(gaps),
                                    'gamma_good_gaps': sorted(qgaps),
                                    'beta_configurations': matches,
                                    'gamma_configurations': records[q]})
    report = {'job_id': JOB, 'scope': 'All permutations of lengths 1 through 6',
              'count_validation': len(table), 'deletions_tested': checked,
              'local_preservation_failure_count': len(failures),
              'local_preservation_first_witnesses': failures[:4],
              'two_gap_contraction_failure_count': len(contraction),
              'two_gap_contraction_first_witnesses': contraction[:4],
              'local_claims': [
                  'A good gap whose endpoints survive deletion remains good.',
                  'If both gaps incident to an internal entry are good, the merged gap after deletion is good.'],
              'status': 'Exploratory exact tests of sufficient lemmas; universal D unproved.'}
    target = OUT/'gap-deletion-test.json'
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(report, indent=2)+'\n'); tmp.replace(target)
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
