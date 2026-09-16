#!/usr/bin/env python3
"""Independent compact verifier for a saved iterate_xor result."""
import json
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "experiments/exact-evidence.json"
with open(path, encoding="utf-8") as f:
    claimed = json.load(f)
limit = claimed["limit_inclusive"]
x, y = 0, 1
zeros = [0]
for n in range(2, limit + 1):
    z = (y ^ n) - x
    x, y = y, z
    if z == 0:
        zeros.append(n)
assert zeros == claimed["zeros"]
assert y == claimed["last_value"]
for item in claimed["modular_tests"]:
    k, modulus, period = item["k"], item["modulus"], item["tested_period"]
    assert modulus == 2 ** k and period == 3 * modulus
    x, y = 0, 1
    residues = [0]
    for n in range(2, period + 2):
        x, y = y, ((y ^ n) - x) % modulus
        if n < period and y == 0:
            residues.append(n)
    assert [x, y] == item["end_state"] == [0, 1]
    assert residues == item["zero_residues"]
print(json.dumps({"status": "PASS", "limit": limit, "zeros": zeros,
                  "modular_levels": len(claimed["modular_tests"])}))
