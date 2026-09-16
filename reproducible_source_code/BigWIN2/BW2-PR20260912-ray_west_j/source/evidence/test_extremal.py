"""Test the natural equality case and its proposed hereditary-deficit lemma.

The equality guess was suggested by the m<=6 discovery table before m=7
was inspected. This is finite falsification, not mathematical acceptance.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
from test_statistics import standardize, direct_g2

out = Path(__file__).resolve().parent
rows = json.loads((out / 'exact-counts.json').read_text())
table = {tuple(r['beta']): r['j'] for r in rows}
coverage, mismatches, deletion_failures = {}, [], []
diffs = Counter()
independent = []
for p, j in table.items():
    m = len(p)
    pats = {standardize(t) for t in combinations(p, 3)}
    layered = not (pats & {(2, 3, 1), (3, 1, 2)})
    colayered = not (pats & {(1, 3, 2), (2, 1, 3)})
    c = coverage.setdefault(m, {'tested': 0, 'maximal_j': 0, 'union_class': 0})
    c['tested'] += 1
    c['maximal_j'] += j == m-1
    c['union_class'] += layered or colayered
    if (j == m-1) != (layered or colayered):
        mismatches.append({'beta': p, 'j': j})
    if m > 1:
        for i in range(m):
            q = standardize(p[:i] + p[i+1:])
            diff = j - table[q]
            diffs[diff] += 1
            if diff > 1:
                deletion_failures.append({'beta': p, 'j_beta': j, 'deleted': i+1,
                                         'gamma': q, 'j_gamma': table[q]})
    if m == 7 and j == m-1:
        g = direct_g2(p)
        assert (m**4+2*m**3+m*m+4*m+4)//2-g == j
        independent.append({'beta': p, 'g2': g})

report = {
    'job_id': 'primary-20260912-ray-west-j-triage-b0b8b2bcc0bf',
    'claim': 'For every m>=1 and beta in S_m, j(beta)=m-1 iff beta is layered or colayered.',
    'status': 'Unproved proposed subsidiary equality classification',
    'discovery': 'All m<=6', 'holdout': 'All 5040 permutations of length 7',
    'coverage': coverage, 'classification_mismatches': mismatches,
    'proposed_lemma': 'Deleting one entry to gamma gives j(beta)<=j(gamma)+1; equivalently d(gamma)<=d(beta), where d(pi)=|pi|-1-j(pi).',
    'deletion_comparisons': sum(diffs.values()),
    'j_change_histogram': dict(sorted(diffs.items())),
    'deletion_lemma_counterexamples': deletion_failures,
    'nonextremal_length4': [list(p) for p,j in table.items() if len(p)==4 and j!=3],
    'independent_insertion_checks_length7_extremizers': independent,
    'limitations': 'No universal proof, independent referee, or exhaustive novelty clearance.'}
(out / 'extremal-test.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='independent_insertion_checks_length7_extremizers'}, indent=2))
