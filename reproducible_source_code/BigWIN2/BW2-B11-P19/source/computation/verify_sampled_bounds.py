#!/usr/bin/env python3
"""Independent integer cross-product checker for sampled_bounds.py."""
import math
import sys


def ratio(m, k):
    n = 48
    penalty = (203 * (k - 2)) // 9
    a = 5 * m * math.comb(n - 2, k - 2) - penalty * math.comb(n, k)
    b = math.comb(n - 4, k - 4)
    if b <= 0:
        raise AssertionError("nonpositive denominator")
    g = math.gcd(a, b)
    return a // g, b // g


expected = {
    598: (30399, 7, 4343, False),
    599: (61143, 14, 4368, True),
    600: (4392, 1, 4392, True),
}
target = 4356
for m, (want_a, want_b, want_ceil, want_resolves) in expected.items():
    a, b = ratio(m, 23)
    assert (a, b) == (want_a, want_b), (m, a, b)
    for k in range(4, 49):
        c, d = ratio(m, k)
        assert a * d >= c * b, (m, k, a, b, c, d)
    got_ceil = -((-a) // b)
    assert got_ceil == want_ceil, (m, got_ceil)
    assert (got_ceil >= target) == want_resolves
    print(f"PASS m={m} unique_formula_k23={a}/{b} ceil={got_ceil} resolves={want_resolves}")
print(f"PASS exhaustive_k=4..48 target={target} python={sys.version.split()[0]}")
