#!/usr/bin/env python3
"""Definition-level verifier for the explicit lower-bound witness."""

from itertools import combinations
from math import gcd
import json

N = 127
WITNESS = [14, 20, 21, 24, 25, 30, 36, 40, 48, 63, 80, 90, 96, 98, 108, 125]

assert len(WITNESS) == 16
assert WITNESS == sorted(set(WITNESS))
assert all(1 <= x <= N for x in WITNESS)

bad = []
for a, b, c in combinations(WITNESS, 3):
    g = gcd(a, b)
    if gcd(a, c) == g and gcd(b, c) == g:
        bad.append([a, b, c, g])

result = {
    "n": N,
    "witness": WITNESS,
    "size": len(WITNESS),
    "triples_checked": 560,
    "bad_triples": bad,
    "passed": not bad,
}
print(json.dumps(result, indent=2, sort_keys=True))
assert not bad
