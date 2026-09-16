#!/usr/bin/env python3
"""Separate exact verification of the k=8, r=10 negative trace witness.

Does not import the prefix-probe implementation. B is recovered from the
defining product; D(6,5), D(7,5) are counted directly by cycle type.
"""
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def value(d):
    # Only u-degrees 0,1,2 are needed to extract the j=2 Schur coefficient.
    coeff = [[0] * 3 for _ in range(9)]
    coeff[0][0] = 1
    for i in range(d + 1):
        for k in range(8, 0, -1):
            for j in range(3):
                coeff[k][j] += i * coeff[k - 1][j]
                if j:
                    coeff[k][j] += (d - i) * coeff[k - 1][j - 1]
    return coeff[8][2] - coeff[8][1]


values = [value(d) for d in range(12)]
triple = [sum((-1) ** (r - d) * comb(r, d) * values[d]
              for d in range(r + 1)) for r in (9, 10, 11)]
assert triple == [57312144, 243133456, 623045665]
minor = triple[1] ** 2 - triple[0] * triple[2]
assert minor == 23405794555448176 > 0

# Exact expansion coefficients p_i of 2B, evaluated at k=8 and r=9,10,11.
# The full expansion and derivation are in j2_reduced_prefix.py and the note.
# For trace -7, the only active product is D(6,5)D(7,5).
p9 = {-6: -1728, -5: -8928, -4: -13680, -3: 2844,
      -2: 28332, -1: 27756, 0: 8748}
p10 = {-6: -2520, -5: -9480, -4: 1048, -3: 53448,
       -2: 98360, -1: 72920, 0: 20000}
p11 = {-6: -2400, -5: -34, -4: 54910, -3: 179264,
       -2: 245520, -1: 158730, 0: 39930}
four_q = 2 * p10[-4] * p10[-3] - p9[-3] * p11[-4] - p9[-2] * p11[-5]
assert four_q == -43173744
q = four_q // 4
d6 = factorial(5)  # one 6-cycle
d7 = factorial(7) // (2 * 5) + factorial(7) // (3 * 4)
assert (d6, d7) == (120, 924)
trace = q * d6 * d7
assert trace == -1196776183680 < 0
report = {'kind': 'separate exact arithmetic verification, not a fresh referee audit',
          'k': 8, 'r': 10, 'common_defect': 5,
          'defining_product_A_values_d0_through_11': values,
          'B_triple': triple, 'actual_minor': minor,
          'trace': -7, 'only_active_pair': [-4, -3],
          'trace_coefficient': q, 'D_6_5': d6, 'D_7_5': d7,
          'negative_trace_value': trace,
          'scope': 'rejects nonnegativity of every trace for the specified defect-k-3 expansion'}
(ROOT / 'j2-defect3-witness-verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
