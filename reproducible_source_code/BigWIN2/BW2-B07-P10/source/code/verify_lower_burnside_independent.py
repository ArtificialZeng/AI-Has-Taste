#!/usr/bin/env python3
"""Independent bit-mask evaluator for the Burnside subfamilies."""

import functools
import json
import math
import pathlib
import sys


def parts(n: int, cap: int):
    if n == 0:
        yield ()
        return
    for x in range(min(n, cap), 0, -1):
        for tail in parts(n - x, x):
            yield (x,) + tail


def hamilton_sum(lengths: tuple[int, ...]) -> int:
    r = len(lengths)
    if all(math.gcd(lengths[i], lengths[j]) == 1 for i in range(r) for j in range(i)):
        return math.factorial(r)
    dp: dict[tuple[int, int], int] = {(1 << i, i): 1 for i in range(r)}
    for used in range(1, 1 << r):
        for last in range(r):
            value = dp.get((used, last), 0)
            if value == 0:
                continue
            for nxt in range(r):
                if used >> nxt & 1:
                    continue
                weight = 2 ** math.gcd(lengths[last], lengths[nxt]) - 1
                key = (used | (1 << nxt), nxt)
                dp[key] = dp.get(key, 0) + value * weight
    full = (1 << r) - 1
    return sum(dp.get((full, last), 0) for last in range(r))


def matching_values(lengths: tuple[int, ...]) -> tuple[int, ...]:
    r = len(lengths)

    @functools.lru_cache(maxsize=None)
    def walk(vertices: tuple[int, ...]) -> tuple[int, ...]:
        if not vertices:
            return (1,)
        i, *tail = vertices
        tail_tuple = tuple(tail)
        answer = list(walk(tail_tuple))
        for position, j in enumerate(tail):
            weight = 2 * (2 ** math.gcd(lengths[i], lengths[j]) - 2)
            if not weight:
                continue
            remainder = tail_tuple[:position] + tail_tuple[position + 1 :]
            values = walk(remainder)
            if len(answer) < len(values) + 1:
                answer += [0] * (len(values) + 1 - len(answer))
            for t, value in enumerate(values):
                answer[t + 1] += weight * value
        return tuple(answer)

    return walk(tuple(range(r)))


def main(path: str) -> None:
    raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    if raw.get("target_n") != 17:
        raise SystemExit("VERIFY FAILED: wrong target")
    p = raw.get("labeled_poset_counts_0_to_17")
    if not isinstance(p, list) or len(p) != 18:
        raise SystemExit("VERIFY FAILED: malformed labeled counts")
    n = 17
    totals = [0, 0, 0]
    for lengths in parts(n, n):
        multiplicity: dict[int, int] = {}
        for length in lengths:
            multiplicity[length] = multiplicity.get(length, 0) + 1
        denominator = 1
        for length, count in multiplicity.items():
            denominator *= length ** count * math.factorial(count)
        conjugacy_size = math.factorial(n) // denominator
        r = len(lengths)
        path_extra = hamilton_sum(lengths) - math.factorial(r)
        poly = matching_values(lengths)
        component_extra = sum(poly[t] * p[r - 2 * t] for t in range(1, len(poly)))
        if r == 2:
            component_extra = 0
        totals[0] += conjugacy_size * p[r]
        totals[1] += conjugacy_size * path_extra
        totals[2] += conjugacy_size * component_extra
    names = [
        "burnside_uniform_numerator",
        "burnside_total_order_extra_numerator",
        "burnside_matching_extra_numerator",
    ]
    expected = raw.get("expected", {})
    for name, value in zip(names, totals):
        if expected.get(name) != value:
            raise SystemExit(f"VERIFY FAILED: {name}: got {value}")
    numerator = sum(totals)
    lower = (numerator + math.factorial(n) - 1) // math.factorial(n)
    if expected.get("burnside_lower_numerator") != numerator or expected.get("lower_bound_u17") != lower:
        raise SystemExit("VERIFY FAILED: aggregate mismatch")
    print(f"VERIFY PASSED: independent bit-mask evaluator gives U(17) >= {lower}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("VERIFY FAILED: usage: verify_lower_burnside_independent.py CERTIFICATE.json")
    main(sys.argv[1])
