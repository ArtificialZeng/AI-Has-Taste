#!/usr/bin/env python3
"""Adversarially audit Williams's sorting with the inferred C=(P0 union P1)\B.

The search ranges over every naturally-labelled poset, every convex two-layer
subset P, and every pair of maximum antichains used as input to the sorting.
It stops at the first output that is not an antichain or does not preserve the
sum of cardinalities.  This tests the proof construction, not merely Lemma 2.
"""

from __future__ import annotations

import argparse
import json

from exhaustive_posets import (
    all_widths,
    intervals,
    is_convex,
    naturally_labelled_posets,
    product_strict_up,
)


def is_antichain(mask: int, strict: list[int]) -> bool:
    bits = mask
    while bits:
        b = bits & -bits
        i = b.bit_length() - 1
        if strict[i] & mask:
            return False
        bits ^= b
    return True


def maximum_antichains(section: int, n: int, strict: list[int], width: int):
    universe = section | (section << n)
    sub = universe
    while True:
        if sub.bit_count() == width and is_antichain(sub, strict):
            yield sub
        if sub == 0:
            break
        sub = (sub - 1) & universe


def leq(up: tuple[int, ...], x: int, y: int) -> bool:
    return x == y or bool(up[x] >> y & 1)


def sorted_outputs(up, p0, p1, a0, a1):
    n = len(up)
    full = (1 << n) - 1
    l0, h0 = a0 & full, (a0 >> n) & full
    l1, h1 = a1 & full, (a1 >> n) & full
    bset = p0 & p1
    cset = (p0 | p1) & ~bset
    # Values assigned to the upper layer of the first output (L), and the
    # lower layer of the second output (H).  Separate input occurrences may
    # share a value; the rules below assign coincident L1/H0 occurrences one
    # to each output, as the antichain conditions force.
    l_values = l1 & ~bset
    h_values = h0 & ~bset
    classifications = []
    for x in range(n):
        bit = 1 << x
        if l1 & bset & bit:
            blockers = l0 | (h0 & cset)
            goes_l = not any(
                blockers >> z & 1 and leq(up, z, x) for z in range(n)
            )
            classifications.append(["L1", x, "L" if goes_l else "H"])
            if goes_l:
                l_values |= bit
            else:
                h_values |= bit
        if h0 & bset & bit:
            blockers = h1 | (l1 & cset)
            goes_h = not any(
                blockers >> z & 1 and leq(up, x, z) for z in range(n)
            )
            classifications.append(["H0", x, "H" if goes_h else "L"])
            if goes_h:
                h_values |= bit
            else:
                l_values |= bit
    first = l0 | (l_values << n)
    second = h_values | (h1 << n)
    return first, second, classifications, (l0, h0, l1, h1, bset, cset)


def first_failure(max_n: int):
    tested_inputs = 0
    tested_convex = 0
    tested_posets = 0
    for n in range(max_n + 1):
        posets = [tuple()] if n == 0 else naturally_labelled_posets(n)
        for up in posets:
            tested_posets += 1
            strict = product_strict_up(up)
            widths = all_widths(strict)
            intv = intervals(strict)
            full = (1 << n) - 1
            max_antis = {}
            for s in range(1 << n):
                w = widths[s | (s << n)]
                max_antis[s] = list(maximum_antichains(s, n, strict, w))
            for p in range(1 << (2 * n)):
                if not is_convex(p, intv):
                    continue
                tested_convex += 1
                p0, p1 = p & full, (p >> n) & full
                for a0 in max_antis[p0]:
                    for a1 in max_antis[p1]:
                        tested_inputs += 1
                        first, second, classes, raw = sorted_outputs(
                            up, p0, p1, a0, a1
                        )
                        preserved = (
                            first.bit_count() + second.bit_count()
                            == a0.bit_count() + a1.bit_count()
                        )
                        anti_first = is_antichain(first, strict)
                        anti_second = is_antichain(second, strict)
                        if not (preserved and anti_first and anti_second):
                            l0, h0, l1, h1, bset, cset = raw
                            return {
                                "coverage_before_first_failure": {
                                    "max_n": max_n,
                                    "posets": tested_posets,
                                    "convex_P": tested_convex,
                                    "pairs_of_maximum_input_antichains": tested_inputs,
                                },
                                "failure": {
                                    "n": n,
                                    "strict_upper_masks": list(up),
                                    "P0_mask": p0,
                                    "P1_mask": p1,
                                    "B_mask": bset,
                                    "C_mask": cset,
                                    "L0_mask": l0,
                                    "H0_mask": h0,
                                    "L1_mask": l1,
                                    "H1_mask": h1,
                                    "classifications": classes,
                                    "first_output_mask": first,
                                    "second_output_mask": second,
                                    "input_size_sum": a0.bit_count() + a1.bit_count(),
                                    "output_size_sum": first.bit_count() + second.bit_count(),
                                    "first_is_antichain": anti_first,
                                    "second_is_antichain": anti_second,
                                },
                            }
    return {
        "coverage": {
            "max_n": max_n,
            "posets": tested_posets,
            "convex_P": tested_convex,
            "pairs_of_maximum_input_antichains": tested_inputs,
        },
        "failure": None,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=4)
    args = parser.parse_args()
    print(json.dumps(first_failure(args.max_n), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
