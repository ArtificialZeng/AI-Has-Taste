#!/usr/bin/env python3
"""Exact finite audit of the component assignment proved in proof.md.

This enumerates all naturally-labelled posets, convex P, and pairs of maximum
section-product antichains in the requested range.  It checks legality of every
moved value, both output antichains, and exact preservation of total size.
"""

from __future__ import annotations

import argparse
import json

from audit_inferred_sorting import is_antichain, maximum_antichains
from exhaustive_posets import (
    all_widths,
    intervals,
    is_convex,
    naturally_labelled_posets,
    product_strict_up,
)


def comparable(up, x, y):
    return x == y or bool(up[x] >> y & 1) or bool(up[y] >> x & 1)


def less(up, x, y):
    return bool(up[x] >> y & 1)


def repaired_outputs(up, p0, p1, a0, a1):
    n = len(up)
    full = (1 << n) - 1
    l0, h0 = a0 & full, (a0 >> n) & full
    l1, h1 = a1 & full, (a1 >> n) & full
    bset = p0 & p1
    # Vertices 0..n-1 are present L1 occurrences and n..2n-1 are present H0.
    vertices = [x for x in range(n) if l1 >> x & 1]
    vertices += [n + x for x in range(n) if h0 >> x & 1]
    adjacency = {v: [] for v in vertices}
    for l in range(n):
        if not (l1 >> l & 1):
            continue
        for h in range(n):
            if h0 >> h & 1 and comparable(up, l, h):
                adjacency[l].append(n + h)
                adjacency[n + h].append(l)
    u_values = d_values = 0
    seen = set()
    moved = []
    for start in vertices:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for w in adjacency[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        has_edge = any(adjacency[v] for v in component)
        swap = False
        if has_edge:
            edge_l = next(v for v in component if v < n and adjacency[v])
            edge_h = adjacency[edge_l][0] - n
            # Equality components use the native assignment. Strict H0<L1
            # components are swapped; L1<H0 components remain native.
            swap = less(up, edge_h, edge_l)
        else:
            v = component[0]
            x = v if v < n else v - n
            if v < n:
                swap = any(l0 >> a & 1 and (a == x or less(up, a, x)) for a in range(n))
            else:
                swap = any(h1 >> b & 1 and (x == b or less(up, x, b)) for b in range(n))
        for v in component:
            x = v if v < n else v - n
            is_l1 = v < n
            goes_u = is_l1 != swap
            if goes_u:
                u_values |= 1 << x
            else:
                d_values |= 1 << x
            native = (is_l1 and goes_u) or ((not is_l1) and not goes_u)
            if not native:
                moved.append(x)
    legal = all(bset >> x & 1 for x in moved)
    first = l0 | (u_values << n)
    second = d_values | (h1 << n)
    return first, second, legal


def audit(max_n):
    totals = []
    total_inputs = 0
    for n in range(max_n + 1):
        poset_count = convex_count = input_count = 0
        posets = [tuple()] if n == 0 else naturally_labelled_posets(n)
        for up in posets:
            poset_count += 1
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
                convex_count += 1
                p0, p1 = p & full, (p >> n) & full
                for a0 in max_antis[p0]:
                    for a1 in max_antis[p1]:
                        input_count += 1
                        first, second, legal = repaired_outputs(up, p0, p1, a0, a1)
                        good = (
                            legal
                            and is_antichain(first, strict)
                            and is_antichain(second, strict)
                            and first.bit_count() + second.bit_count()
                            == a0.bit_count() + a1.bit_count()
                        )
                        if not good:
                            return {
                                "failure": {
                                    "n": n,
                                    "strict_upper_masks": list(up),
                                    "P_mask": p,
                                    "input_antichains": [a0, a1],
                                    "outputs": [first, second],
                                    "moves_legal": legal,
                                },
                                "orders_completed": totals,
                            }
        total_inputs += input_count
        totals.append({
            "n": n,
            "naturally_labelled_posets": poset_count,
            "convex_P": convex_count,
            "pairs_of_maximum_input_antichains": input_count,
        })
    return {"failure": None, "orders": totals, "total_input_pairs": total_inputs}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=4)
    args = parser.parse_args()
    print(json.dumps(audit(args.max_n), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
