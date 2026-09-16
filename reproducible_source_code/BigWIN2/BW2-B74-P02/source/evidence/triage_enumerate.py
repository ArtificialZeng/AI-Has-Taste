#!/usr/bin/env python3
"""Exact bounded socle check for 2 <= c <= 20.

The search box is complete: both ideals contain x^2, y^2, and z^c, so every
standard monomial has a,b < 2 and d < c.
"""

from math import ceil


def in_original(a: int, b: int, d: int, c: int) -> bool:
    return a >= 2 or b >= 2 or d >= c or (a >= 1 and b >= 1 and d >= 1)


def in_closure(a: int, b: int, d: int, c: int) -> bool:
    # Newton half-space criterion derived from the three pure-power vertices.
    return c * (a + b) + 2 * d >= 2 * c


def socle(c: int, membership) -> list[tuple[int, int, int]]:
    answer = []
    for a in range(2):
        for b in range(2):
            for d in range(c):
                if membership(a, b, d, c):
                    continue
                if all(
                    membership(a + da, b + db, d + dd, c)
                    for da, db, dd in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
                ):
                    answer.append((a, b, d))
    return sorted(answer)


print("c | v(I_c) | v(bar(I_c)) | socle(I_c) | socle(bar(I_c))")
for c in range(2, 21):
    actual_i = socle(c, in_original)
    actual_bar = socle(c, in_closure)
    expected_i = sorted([(1, 1, 0), (1, 0, c - 1), (0, 1, c - 1)])
    e = ceil(c / 2) - 1
    expected_bar = sorted([(0, 0, c - 1), (1, 0, e), (0, 1, e)])
    assert actual_i == expected_i
    assert actual_bar == expected_bar
    vi = min(sum(u) for u in actual_i)
    vbar = min(sum(u) for u in actual_bar)
    assert vi == 2 and vbar == ceil(c / 2)
    print(f"{c:2d} | {vi:6d} | {vbar:11d} | {actual_i} | {actual_bar}")
