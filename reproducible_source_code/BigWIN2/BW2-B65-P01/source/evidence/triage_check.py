#!/usr/bin/env python3
"""Exact finite triage check; it makes no claim beyond K=1,...,25.

For a fixed K, agreement at offsets 5 throughout a window of length max(S)=c
from q propagates forever by the SG recurrence. Failure at q-1 makes q minimal
for period 5. A nonconstant 5-block makes 5 least: any smaller eventual period,
together with period 5, would force eventual period gcd(p,5)=1.
"""

from hashlib import sha256


def grundy_prefix(K: int):
    c = 10 * K + 1
    q = 2 * c + 5
    p = 5
    stop = q + p + c
    values = []
    for n in range(stop):
        options = {values[n - s] for s in (4, 6, c) if s <= n}
        g = 0
        while g in options:
            g += 1
        values.append(g)
    return c, q, p, values


def check(K: int):
    c, q, p, values = grundy_prefix(K)
    assert all(values[n + p] == values[n] for n in range(q, q + c))
    assert values[q - 1 + p] != values[q - 1]
    block = values[q : q + p]
    assert len(set(block)) > 1
    digest = sha256(bytes(values[:q])).hexdigest()
    return c, q, "".join(map(str, block)), values[q - 1], values[q - 1 + p], digest


if __name__ == "__main__":
    for K in range(1, 26):
        c, q, block, left, right, digest = check(K)
        print(
            f"K={K:2d} c={c:3d} q={q:3d} period={block} "
            f"boundary={left}!={right} prefix_sha256={digest}"
        )
