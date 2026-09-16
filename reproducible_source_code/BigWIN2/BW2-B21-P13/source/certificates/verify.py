#!/usr/bin/env python3
"""Fail-closed exact verifier for the A078590 counterexample."""
import hashlib, json, pathlib, sys

path = pathlib.Path(__file__).with_name("counterexample.json")
raw = path.read_bytes()
d = json.loads(raw)
required = {"a1", "a2", "a3", "a4", "a5", "a6", "modulus",
            "failed_numerator_remainder", "supporting_congruences"}
if not required <= d.keys():
    raise SystemExit("FAIL: incomplete certificate")
a = [None, d["a1"], d["a2"]]
for expected in (d["a3"], d["a4"], d["a5"], d["a6"]):
    numerator = (1 << a[-1]) + 1
    if numerator % a[-2]:
        raise SystemExit("FAIL: an asserted earlier division is not exact")
    a.append(numerator // a[-2])
    if a[-1] != expected:
        raise SystemExit("FAIL: serialized term mismatch")
if pow(2, 171, 162) + 1 != 27:
    raise SystemExit("FAIL: modulo-162 congruence")
if a[6] % 18 != 3:
    raise SystemExit("FAIL: exponent congruence")
r = (pow(2, a[6], a[5]) + 1) % a[5]
if r != 9 or r != d["failed_numerator_remainder"]:
    raise SystemExit("FAIL: decisive remainder")
code_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
data_hash = hashlib.sha256(raw).hexdigest()
print(f"PASS n=7 remainder={r} data_sha256={data_hash} code_sha256={code_hash}")
