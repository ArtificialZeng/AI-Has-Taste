"""Exact triage tests of a new reformulation; no unbounded LC claim."""
from math import comb
from pathlib import Path
import hashlib
import json
import time

START = time.perf_counter()
N = 80

def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0

def term(n, r, k):
    return choose(r + 1, k + 1 - r) * choose(n - r - 1, k)

def at(p, k):
    return p[k] if 0 <= k < len(p) else 0

def lc_failure(p):
    for k in range(1, len(p) - 1):
        if p[k] ** 2 < p[k - 1] * p[k + 1]:
            return {"k": k, "triple": p[k - 1:k + 2]}
    return None

# Coefficient extraction from the published rational generating function.
num = {0: [1], 1: [-1], 2: [1, -1], 3: [-1, 2, -1]}
published = []
for n in range(N + 1):
    row = [at(num.get(n, []), k) for k in range(n + 1)]
    for lag, factor, shift in [(1, 2, 0), (2, -1, 0), (2, 1, 1),
                               (3, -1, 1), (3, 1, 2)]:
        if n >= lag:
            for k in range(n + 1):
                row[k] += factor * at(published[n - lag], k - shift)
    published.append(row)

formula_coefficients = 0
partial_sum_rows = 0
partial_sum_first_failure = None
for n in range(1, N + 1):
    row = [0] * (n + 1)
    for r in range(n):
        row = [row[k] + term(n, r, k) for k in range(n + 1)]
        partial_sum_rows += 1
        bad = lc_failure(row)
        if bad is not None and partial_sum_first_failure is None:
            partial_sum_first_failure = {"n": n, "R": r, **bad}
    assert row == published[n], (n, row, published[n])
    formula_coefficients += n + 1

# A proposed sufficient condition: every pair of summands has nonnegative
# symmetric mixed LC determinant. One exact failure rules this route out.
n, r, s, k = 4, 0, 1, 1
mixed = (2 * term(n, r, k) * term(n, s, k)
         - term(n, r, k - 1) * term(n, s, k + 1)
         - term(n, r, k + 1) * term(n, s, k - 1))
assert mixed == -1

# Three suffix states: ending 0; ending 01; ending 1 but not 01.
# Includes the one-letter word 1 in the third state.
A, B, C = [1], [0], [1]
state_first_failure = None
BC_mixed_first_failure = None
for n in range(1, N + 1):
    total = [at(B, k) + at(C, k) for k in range(n + 1)]
    assert total == published[n]
    for name, p in [("A", A), ("B", B), ("C", C)]:
        bad = lc_failure(p)
        if bad and state_first_failure is None:
            state_first_failure = {"n": n, "state": name, **bad}
    for k in range(1, n):
        d = (2 * at(B, k) * at(C, k) - at(B, k - 1) * at(C, k + 1)
             - at(B, k + 1) * at(C, k - 1))
        if d < 0 and BC_mixed_first_failure is None:
            BC_mixed_first_failure = {"n": n, "k": k, "value": d,
                                      "B": B, "C": C}
    A, B, C = ([at(A, k) + at(B, k - 1) + at(C, k - 1)
                 for k in range(n + 2)],
                [at(A, k) for k in range(n + 2)],
                [at(B, k - 1) + at(C, k) for k in range(n + 2)])

out = {
    "job_id": "primary-20260914-bigdescent-logconcavity-triage-21d5b29238e0",
    "arithmetic": "exact Python integers; standard library only",
    "formula_range": "1<=n<=80, 0<=k<=n",
    "formula_coefficients_compared": formula_coefficients,
    "formula_matches_published_GF": True,
    "suffix_recurrence_matches_published_GF_through_n": N,
    "partial_sum_rows_tested": partial_sum_rows,
    "partial_sum_range": "1<=n<=80, 0<=R<=n-1, 1<=k<=n-1",
    "partial_sum_first_LC_failure": partial_sum_first_failure,
    "pairwise_summand_mixed_counterexample": {
        "n": 4, "r": 0, "s": 1, "k": 1, "mixed_determinant": mixed,
        "summand_r": [term(4, 0, k) for k in range(3)],
        "summand_s": [term(4, 1, k) for k in range(3)]},
    "suffix_state_first_LC_failure": state_first_failure,
    "suffix_BC_mixed_first_failure": BC_mixed_first_failure,
    "source_sha256": hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "seconds": time.perf_counter() - START,
    "qualification": "Formula and suffix model are known-GF reformulations. "
                     "Finite tests do not prove uniform log-concavity. "
                     "The mixed counterexample concerns only a sufficient subsidiary condition."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
