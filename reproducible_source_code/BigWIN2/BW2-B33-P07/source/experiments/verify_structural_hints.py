#!/usr/bin/env python3
"""Independent AND-formula checker for structural-handoff evidence."""

import json
import sys


path = sys.argv[1] if len(sys.argv) > 1 else "experiments/structural-hints-evidence.json"
with open(path, encoding="utf-8") as handle:
    claim = json.load(handle)
assert claim["schema_version"] == 1
p = claim["parameters"]
limit = p["direct_limit"]

# A second recurrence evaluator uses x XOR n = x+n-2(x AND n).
a = [0, 1]
for n in range(2, limit + 1):
    a.append(a[-1] + n - 2 * (a[-1] & n) - a[-2])
zeros = [n for n, value in enumerate(a) if value == 0]
assert zeros == claim["three_step_reduction"]["zeros_through_limit"]

assert a[49_139] == a[49_151] == claim["dyadic_shift"]["long_lower_run_values"]["expected_power"]
assert claim["dyadic_shift"]["long_lower_run_values"]["a_49139"] == a[49_139]
assert claim["dyadic_shift"]["long_lower_run_values"]["a_49151"] == a[49_151]

def values_mod(modulus, stop):
    out = [0, 1 % modulus]
    for n in range(2, stop):
        y = out[-1]
        out.append((y + n - 2 * (y & n) - out[-2]) % modulus)
    return out


for item in claim["dyadic_shift"]["signatures"]:
    k = item["k"]
    m = 1 << k
    length = 3 * m
    vals = values_mod(2 * m, length + 3)
    sig = [((vals[length + c] - vals[c]) // m) % 2 for c in range(3)]
    assert sig == item["signature"]

for item in claim["dyadic_shift"]["child_tables"]:
    k = item["k"]
    m = 1 << k
    length = 3 * m
    vals = values_mod(2 * m, 2 * length)
    sig = item["epsilon_signature"]
    patterns = {f"h{h}e{e}": 0 for h in range(2) for e in range(2)}
    outcomes = {"dead": 0, "lower-only": 0, "upper-only": 0, "both": 0}
    parents = []
    children = []
    for r in range(length):
        if vals[r] % m:
            continue
        parents.append(r)
        h = vals[r] // m
        e = sig[r % 3]
        lo, hi = vals[r] == 0, vals[r + length] == 0
        assert lo == (h == 0) and hi == (h == e)
        patterns[f"h{h}e{e}"] += 1
        name = "both" if lo and hi else "lower-only" if lo else "upper-only" if hi else "dead"
        outcomes[name] += 1
        if lo:
            children.append(r)
        if hi:
            children.append(r + length)
    assert len(parents) == item["parent_count"]
    assert len(children) == item["child_count"]
    assert patterns == item["pattern_counts"] and outcomes == item["outcome_counts"]
    if k == 2:
        children.sort()
        assert parents == item["parents"] and children == item["children"]

def word_map(x, y):
    for j in range(12):
        xor = y + j - 2 * (y & j)
        x, y = y, (xor - x) % 8
    return [x, y]


assert word_map(0, 0) == claim["dyadic_shift"]["twelve_step_mod8_maps"]["[0,0]"] == [4, 0]
assert word_map(1, 0) == claim["dyadic_shift"]["twelve_step_mod8_maps"]["[1,0]"] == [5, 4]

minus = [(n - 3) // 6 for n in range(3, limit + 1, 6) if a[n] == -1]
plus1 = [(n - 1) // 6 for n in range(1, limit + 1, 6) if a[n] == 1]
plus2 = [(n - 2) // 6 for n in range(2, limit + 1, 6) if a[n] == 1]
assert claim["three_step_reduction"]["unit_hits_through_limit"] == {
    "a_6q_plus_3_equals_minus_1": minus,
    "a_6q_plus_1_equals_1": plus1,
    "a_6q_plus_2_equals_1": plus2,
}

parity = [0, 1, 1, 1, 0, 0]
for n in range(2, limit + 1):
    h = (a[n] - parity[n % 6]) // 2
    y = (a[n - 1] - parity[(n - 1) % 6]) // 2
    x = (a[n - 2] - parity[(n - 2) % 6]) // 2
    assert h == (y ^ (n // 2)) - x - int(n % 6 == 3)

print(json.dumps({
    "status": "PASS",
    "direct_limit": limit,
    "signature_max_k": p["max_signature_k"],
    "child_table_max_k": p["max_child_k"],
    "zeros": zeros,
}, separators=(",", ":")))
