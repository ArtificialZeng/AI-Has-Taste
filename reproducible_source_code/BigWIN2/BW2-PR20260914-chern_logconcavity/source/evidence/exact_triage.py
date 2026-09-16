#!/usr/bin/env python3
"""Exact bounded test from the defining product; standard library only.

Run from the project directory: python3 evidence/exact_triage.py
The second implementation uses Berczi-Feher (3.3), not the product DP.
"""
import hashlib
import json
from math import comb
from pathlib import Path

K = 32
DMAX = 2 * K + 2
ROOT = Path(__file__).resolve().parent


def product_values(d):
    # C[k][m] = [z^k u^m] product_i (1+z(i+(d-i)u)).
    C = [[0] * (k + 1) for k in range(K + 1)]
    C[0][0] = 1
    for i in range(d + 1):
        for k in range(min(K, i + 1), 0, -1):
            for m in range(k + 1):
                if m < k:
                    C[k][m] += i * C[k - 1][m]
                if m:
                    C[k][m] += (d - i) * C[k - 1][m - 1]
    return {(k, j): C[k][j] - (C[k][j - 1] if j else 0)
            for k in range(K + 1) for j in range(k // 2 + 1)}


# Unsigned Stirling numbers of the first kind.
S = [[1]]
for n in range(1, DMAX + 2):
    prev = S[-1]
    S.append([((prev[m - 1] if m else 0)
               + ((n - 1) * prev[m] if m < n else 0))
              for m in range(n + 1)])


def stirling_value(k, j, d):
    total = 0
    for s in range(j + 1):
        m = d + 1 - k + s
        if 0 <= m <= d + 1 and m >= s:
            total += ((-1) ** (j - s) * comb(k - s + 1, j - s)
                      * d ** s * comb(m, s) * S[d + 1][m])
    return total


values = {(k, j): [] for k in range(K + 1) for j in range(k // 2 + 1)}
crosschecks = 0
for d in range(DMAX + 1):
    for (k, j), value in product_values(d).items():
        other = stirling_value(k, j, d)
        assert value == other, (k, j, d, value, other)
        crosschecks += 1
        values[k, j].append(value)

rows = []
violations = []
interior_minors = 0
boundary_minors = 0
zero_inside_active = []
for (k, j), vals in values.items():
    diffs = vals[:]
    coeffs = []
    while diffs:
        coeffs.append(diffs[0])
        diffs = [b - a for a, b in zip(diffs, diffs[1:])]
    assert all(b == 0 for b in coeffs[2 * k + 1:]), (k, j, 'degree')
    coeffs = coeffs[:2 * k + 1]
    active = [r for r, b in enumerate(coeffs) if b]
    assert active
    lo, hi = active[0], active[-1]
    if active != list(range(lo, hi + 1)):
        violations.append({'kind': 'internal zero', 'k': k, 'j': j})
    for r, b in enumerate(coeffs):
        if b < 0:
            violations.append({'kind': 'negative coefficient', 'k': k, 'j': j, 'r': r})
        left = coeffs[r - 1] if r else 0
        right = coeffs[r + 1] if r + 1 < len(coeffs) else 0
        minor = b * b - left * right
        if lo < r < hi:
            interior_minors += 1
            if minor == 0:
                zero_inside_active.append([k, j, r])
        else:
            boundary_minors += 1
        if minor < 0:
            violations.append({'kind': 'negative minor', 'k': k, 'j': j, 'r': r,
                               'triple': [left, b, right], 'minor': minor})
    expected_lo = 0 if k == 0 else (k if j == 0 else k - 1)
    if (lo, hi) != (expected_lo, 2 * k):
        violations.append({'kind': 'unexpected support', 'k': k, 'j': j,
                           'support': [lo, hi]})
    rows.append({'k': k, 'j': j, 'support': [lo, hi], 'B': coeffs})

lookup = {(row['k'], row['j']): row['B'] for row in rows}
assert lookup[0, 0] == [1]
assert lookup[2, 1] == [0, 1, 4, 6, 3]
assert lookup[4, 2] == [0, 0, 0, 27, 212, 660, 1000, 735, 210]
assert lookup[5, 2][4:] == [320, 3375, 14010, 29575, 33740, 19845, 4725]
assert lookup[6, 2][5:] == [3250, 44004, 233604, 646492, 1022217, 932400, 457380, 93555]

data_file = ROOT / 'exact-coefficients.json'
data_file.write_text(json.dumps(rows, indent=2) + '\n')
report = {
    'job_id': 'primary-20260914-chern-logconcavity-triage-b02871487deb',
    'kind': 'exact finite observation; not an infinite-family proof',
    'k_range': [0, K], 'j_range': 'all integers 0 <= j <= floor(k/2)',
    'd_evaluation_range': [0, DMAX], 'r_range': '0 <= r <= 2k; all later coefficients zero by degree bound',
    'rows': len(rows), 'independent_value_comparisons': crosschecks,
    'strictly_interior_minors_checked': interior_minors,
    'remaining_minors_checked': boundary_minors,
    'zero_strictly_interior_minors': zero_inside_active,
    'violations': violations,
    'source_examples_reproduced': ['k=0,j=0', 'k=2,j=1', 'k=4,5,6,j=2'],
    'observed_support': 'k=0: {0}; k>=1,j=0: [k,2k]; j>=1: [k-1,2k]',
    'coefficients_sha256': hashlib.sha256(data_file.read_bytes()).hexdigest(),
    'source_sha256': hashlib.sha256((ROOT.parent / 'source.md').read_bytes()).hexdigest()
}
(ROOT / 'exact-triage.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
