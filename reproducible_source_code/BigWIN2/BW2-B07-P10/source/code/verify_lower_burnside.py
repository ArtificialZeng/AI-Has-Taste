#!/usr/bin/env python3
"""Exact cycle-type verifier for a constructive Burnside lower bound."""

import collections
import functools
import json
import math
import pathlib
import sys


def partitions(n: int, largest: int | None = None):
    if n == 0:
        yield ()
        return
    if largest is None or largest > n:
        largest = n
    for first in range(largest, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def total_order_path_sum(multiplicities: collections.Counter[int]) -> int:
    """Sum products over length words, before assigning equal-length cycles."""
    total = 0

    def visit(last: int | None, remaining: int, product: int) -> None:
        nonlocal total
        if remaining == 0:
            total += product
            return
        for length in tuple(multiplicities):
            if multiplicities[length] == 0:
                continue
            multiplicities[length] -= 1
            weight = 1 if last is None else 2 ** math.gcd(last, length) - 1
            visit(length, remaining - 1, product * weight)
            multiplicities[length] += 1

    visit(None, sum(multiplicities.values()), 1)
    return total


def matching_extra(lengths: tuple[int, ...], p: list[int]) -> int:
    """Patterned two-cycle components, with any poset on unused cycles."""
    r = len(lengths)

    @functools.lru_cache(maxsize=None)
    def matching_polynomial(mask: int) -> tuple[int, ...]:
        if mask == 0:
            return (1,)
        first_bit = mask & -mask
        i = first_bit.bit_length() - 1
        rest = mask ^ first_bit
        out = list(matching_polynomial(rest))  # leave i unmatched
        choices = rest
        while choices:
            bit = choices & -choices
            choices ^= bit
            j = bit.bit_length() - 1
            weight = 2 * (2 ** math.gcd(lengths[i], lengths[j]) - 2)
            if weight == 0:
                continue
            sub = matching_polynomial(rest ^ bit)
            if len(out) < len(sub) + 1:
                out.extend([0] * (len(sub) + 1 - len(out)))
            for size, value in enumerate(sub):
                out[size + 1] += weight * value
        return tuple(out)

    polynomial = matching_polynomial((1 << r) - 1)
    return sum(polynomial[t] * p[r - 2 * t] for t in range(1, len(polynomial)))


def main(path: str) -> None:
    try:
        raw = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
        n = raw["target_n"]
        p = raw["labeled_poset_counts_0_to_17"]
        expected = raw["expected"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f"VERIFY FAILED: malformed certificate: {exc}")
    if n != 17 or len(p) != 18 or any(type(v) is not int or v <= 0 for v in p):
        raise SystemExit("VERIFY FAILED: invalid labeled-count table")

    uniform_sum = path_sum = component_sum = 0
    for cycle_type in partitions(n):
        mult = collections.Counter(cycle_type)
        r = len(cycle_type)
        centralizer = 1
        equal_assignments = 1
        for length, copies in mult.items():
            centralizer *= length ** copies * math.factorial(copies)
            equal_assignments *= math.factorial(copies)
        class_size = math.factorial(n) // centralizer
        uniform = p[r]
        path_extra = total_order_path_sum(mult.copy()) * equal_assignments - math.factorial(r)
        component_extra = 0 if r == 2 else matching_extra(cycle_type, p)
        if min(uniform, path_extra, component_extra) < 0:
            raise SystemExit("VERIFY FAILED: negative fixed-set contribution")
        uniform_sum += class_size * uniform
        path_sum += class_size * path_extra
        component_sum += class_size * component_extra

    numerator = uniform_sum + path_sum + component_sum
    lower = (numerator + math.factorial(n) - 1) // math.factorial(n)
    got = {
        "burnside_uniform_numerator": uniform_sum,
        "burnside_total_order_extra_numerator": path_sum,
        "burnside_matching_extra_numerator": component_sum,
        "burnside_lower_numerator": numerator,
        "lower_bound_u17": lower,
    }
    for key, value in got.items():
        if expected.get(key) != value:
            raise SystemExit(f"VERIFY FAILED: {key}: got {value}")
    print(f"VERIFY PASSED: U(17) >= {lower}; exact Burnside numerator {numerator}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("VERIFY FAILED: usage: verify_lower_burnside.py CERTIFICATE.json")
    main(sys.argv[1])
