#!/usr/bin/env python3
"""Fail-closed independent checker for a zero-lift summary."""

import hashlib
import json
import sys
from pathlib import Path


claim_path = Path(sys.argv[1] if len(sys.argv) > 1 else "experiments/zero-lift-evidence.json")
claim = json.loads(claim_path.read_text(encoding="utf-8"))
source_path = Path(claim["source_file"])
raw = source_path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == claim["source_sha256"]
source = json.loads(raw)
tests = source["sequence_period_tests"]
assert claim["maximum_level"] == len(tests) - 1

levels = []
summaries = []
known = {0, 6, 11, 23, 36, 42, 48, 54}
for k, item in enumerate(tests):
    assert item["k"] == k and item["period"] == 3 * (2 ** k)
    residues = item["zero_residues"]
    assert residues == sorted(residues) and len(residues) == len(set(residues))
    level = set(residues)
    levels.append(level)
    other = sorted(level - known)
    summaries.append({
        "k": k,
        "period": 3 * (2 ** k),
        "zero_residue_count": len(level),
        "counts_by_mod_3": [len([r for r in level if r % 3 == c]) for c in range(3)],
        "least_nonknown_representative": other[0] if other else None,
    })
assert summaries == claim["level_summaries"]

transitions = []
runs = []
for k in range(len(levels) - 1):
    period = 3 * (2 ** k)
    histogram = [0, 0, 0]
    lower_only = upper_only = both = 0
    for r in levels[k]:
        bits = (r in levels[k + 1], r + period in levels[k + 1])
        count = sum(bits)
        histogram[count] += 1
        lower_only += count == 1 and bits[0]
        upper_only += count == 1 and bits[1]
        both += count == 2
        if r not in known:
            run = 0
            while k + run + 1 < len(levels) and r in levels[k + run + 1]:
                run += 1
            runs.append((run, k, r))
    assert {r % period for r in levels[k + 1]} <= levels[k]
    transitions.append({
        "k": k,
        "parent_count": len(levels[k]),
        "child_count": len(levels[k + 1]),
        "parents_with_0_1_2_children": histogram,
        "lower_only": lower_only,
        "upper_only": upper_only,
        "both": both,
    })
assert transitions == claim["transitions"]
runs.sort(reverse=True)
assert claim["longest_observed_nonknown_lower_run"] == {
    "edge_count": runs[0][0],
    "start_level": runs[0][1],
    "representative": runs[0][2],
    "ties_at_maximum": sum(x[0] == runs[0][0] for x in runs),
}
print(json.dumps({
    "status": "PASS",
    "maximum_level": len(levels) - 1,
    "levels_checked": len(levels),
    "transitions_checked": len(transitions),
}, separators=(",", ":")))
