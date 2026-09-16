#!/usr/bin/env python3
"""Independent AND-formula checker for fixed-window lift-feature attacks."""

import json
import sys

import numpy as np
from numba import njit


@njit
def zero_node_states_via_and(k: int, capacity: int):
    modulus = 1 << k
    period = 3 * modulus
    residues = np.empty(capacity, dtype=np.int64)
    previous = np.empty(capacity, dtype=np.int64)
    count = 0
    x, y = 0, 1
    for n in range(2, period):
        x, y = y, (y + n - 2 * (y & n) - x) % modulus
        if y == 0:
            assert count < capacity
            residues[count] = n
            previous[count] = x
            count += 1
    return residues, previous, count


def stats(records, width, family):
    mask = (1 << width) - 1
    buckets = {}
    counts = {}
    for k, r, x, outcome in records:
        if k < width:
            continue
        if family == "low-state-window":
            key = (r & mask, x & mask)
        elif family == "low-window-plus-component-and-block":
            key = (r & mask, x & mask, r % 3, r // (1 << k))
        else:
            assert family == "low-window-plus-leading-time-window"
            key = (r & mask, x & mask, r % 3, r // (1 << max(0, k - width)))
        buckets.setdefault(key, set()).add(outcome)
        counts[key] = counts.get(key, 0) + 1
    ambiguous = {key for key, values in buckets.items() if len(values) > 1}
    return {
        "feature_classes": len(buckets),
        "ambiguous_feature_classes": len(ambiguous),
        "records_in_ambiguous_classes": sum(counts[key] for key in ambiguous),
        "predictive": not ambiguous,
    }


path = sys.argv[1] if len(sys.argv) > 1 else "experiments/lift-state-feature-evidence.json"
with open(path, encoding="utf-8") as handle:
    claim = json.load(handle)
max_parent_k = claim["max_parent_k"]
capacity = 10000
zero_node_states_via_and(1, capacity)
levels = []
for k in range(1, max_parent_k + 2):
    r, x, count = zero_node_states_via_and(k, capacity)
    levels.append((list(map(int, r[:count])), list(map(int, x[:count]))))
records = []
for k in range(1, max_parent_k + 1):
    children = set(levels[k][0])
    period = 3 * (2 ** k)
    for r, x in zip(*levels[k - 1]):
        outcome = int(r in children) + 2 * int(r + period in children)
        records.append((k, r, x, outcome))
assert len(records) == claim["zero_nodes_with_defined_previous_state"]
for item in claim["tests"]:
    recomputed = stats(records, item["window_bits"], item["family"])
    for field, value in recomputed.items():
        assert item[field] == value
    assert item["records"] == len([z for z in records if z[0] >= item["window_bits"]])
print(json.dumps({
    "status": "PASS",
    "max_parent_k": max_parent_k,
    "records": len(records),
    "feature_tests": len(claim["tests"]),
}, separators=(",", ":")))
