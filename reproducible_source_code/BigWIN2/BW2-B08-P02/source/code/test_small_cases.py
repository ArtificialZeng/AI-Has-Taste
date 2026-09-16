#!/usr/bin/env python3
"""Hand-computable smoke tests for the generic ideal enumerator."""
import importlib.util
from pathlib import Path

path = Path(__file__).with_name("verify_counterexample.py")
spec = importlib.util.spec_from_file_location("v", path)
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)


def check(n, edges, expected_h):
    leq = v.closure(n, edges)
    h, _ = v.direct_h(leq, v.ideals(leq))
    if h != expected_h: raise SystemExit("FAIL small case %r != %r" % (h, expected_h))


check(1, [], [1, 1])                         # one point interval [0,1]
check(2, [], [1, 2, 1])                      # two-element antichain: (1+t)^2
check(2, [(0, 1)], [1, 3, 1])               # direct hand enumeration
print("PASS small-cases")
