#!/usr/bin/env python3
"""Exact exhaustive test of the frozen two-layer width inequality.

For each n, every finite n-element poset is isomorphic to a poset whose strict
order is contained in 0<1<...<n-1 (choose a linear extension).  We enumerate
all distinct transitive closures of subsets of these forward pairs.  Thus the
enumeration contains at least one labelled representative of every isomorphism
class, although it deliberately does not quotient duplicates by isomorphism.

For a fixed R, all 2^(2n) induced subsets of R x Q_1 have their widths computed
exactly by max-over-subsets dynamic programming on the antichain indicator.
Every subset is then checked for order convexity by all closed intervals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def naturally_labelled_posets(n: int):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    closures: set[tuple[int, ...]] = set()
    for chosen in range(1 << len(pairs)):
        up = [0] * n
        for k, (i, j) in enumerate(pairs):
            if chosen >> k & 1:
                up[i] |= 1 << j
        # Warshall closure; the forward labelling makes this especially small.
        for k in range(n):
            bit = 1 << k
            for i in range(n):
                if up[i] & bit:
                    up[i] |= up[k]
        closures.add(tuple(up))
    yield from sorted(closures)


def product_strict_up(up: tuple[int, ...]) -> list[int]:
    """Strict upper masks in R x Q1, indexed x+n*layer."""
    n = len(up)
    ans = [0] * (2 * n)
    for layer in (0, 1):
        for x in range(n):
            a = x + n * layer
            # Same layer: strict R comparisons.
            for y in range(n):
                if up[x] >> y & 1:
                    ans[a] |= 1 << (y + n * layer)
            # Cross layer includes equality in R.
            if layer == 0:
                ans[a] |= 1 << (x + n)
                for y in range(n):
                    if up[x] >> y & 1:
                        ans[a] |= 1 << (y + n)
    return ans


def all_widths(strict_up: list[int]) -> list[int]:
    m = len(strict_up)
    size = 1 << m
    widths = [0] * size
    for mask in range(1, size):
        b = mask & -mask
        i = b.bit_length() - 1
        rest = mask ^ b
        if widths[rest] == rest.bit_count() and not (strict_up[i] & rest):
            widths[mask] = mask.bit_count()
    # Subset-max (max-plus zeta transform): widths[P] becomes maximum size of
    # an antichain A contained in P.
    for i in range(m):
        bit = 1 << i
        for mask in range(size):
            if mask & bit and widths[mask ^ bit] > widths[mask]:
                widths[mask] = widths[mask ^ bit]
    return widths


def intervals(strict_up: list[int]) -> list[tuple[int, int, int]]:
    m = len(strict_up)
    leq_up = [strict_up[i] | (1 << i) for i in range(m)]
    lower = [0] * m
    for x in range(m):
        for y in range(m):
            if leq_up[y] >> x & 1:
                lower[x] |= 1 << y
    out = []
    for a in range(m):
        for b in range(m):
            if leq_up[a] >> b & 1:
                out.append((1 << a, 1 << b, leq_up[a] & lower[b]))
    return out


def is_convex(mask: int, intv: list[tuple[int, int, int]]) -> bool:
    for abit, bbit, between in intv:
        if mask & abit and mask & bbit and between & ~mask:
            return False
    return True


def maximum_antichain(mask: int, strict_up: list[int]) -> list[int]:
    sub = mask
    best = 0
    while True:
        ok = True
        bits = sub
        while bits:
            b = bits & -bits
            i = b.bit_length() - 1
            if strict_up[i] & sub:
                ok = False
                break
            bits ^= b
        if ok and sub.bit_count() > best.bit_count():
            best = sub
        if sub == 0:
            break
        sub = (sub - 1) & mask
    return [i for i in range(len(strict_up)) if best >> i & 1]


def run(max_n: int) -> dict:
    report = {
        "method": "all naturally-labelled transitive closures; exact antichain subset DP; all interval convexity checks",
        "coverage_note": "Every finite poset has a linear extension, so every isomorphism class at each tested order occurs among the naturally-labelled closures.",
        "orders": [],
        "counterexample": None,
    }
    digest = hashlib.sha256()
    for n in range(max_n + 1):
        poset_count = convex_count = tested_count = 0
        min_slack = None
        if n == 0:
            posets = [tuple()]
        else:
            posets = naturally_labelled_posets(n)
        for up in posets:
            poset_count += 1
            digest.update(n.to_bytes(1, "little"))
            for u in up:
                digest.update(u.to_bytes(max(1, (n + 7) // 8), "little"))
            strict = product_strict_up(up)
            widths = all_widths(strict)
            intv = intervals(strict)
            section_product_width = [0] * (1 << n)
            for s in range(1 << n):
                section_product_width[s] = widths[s | (s << n)]
            for p in range(1 << (2 * n)):
                if not is_convex(p, intv):
                    continue
                convex_count += 1
                p0 = p & ((1 << n) - 1)
                p1 = (p >> n) & ((1 << n) - 1)
                lhs = 2 * widths[p]
                rhs = section_product_width[p0] + section_product_width[p1]
                slack = lhs - rhs
                tested_count += 1
                if min_slack is None or slack < min_slack:
                    min_slack = slack
                if slack < 0:
                    report["counterexample"] = {
                        "n": n,
                        "strict_upper_masks": list(up),
                        "P_mask": p,
                        "P0_mask": p0,
                        "P1_mask": p1,
                        "width_P": widths[p],
                        "width_P0xQ1": section_product_width[p0],
                        "width_P1xQ1": section_product_width[p1],
                        "maximum_antichain_P_indices": maximum_antichain(p, strict),
                        "maximum_antichain_P0xQ1_indices": maximum_antichain(p0 | (p0 << n), strict),
                        "maximum_antichain_P1xQ1_indices": maximum_antichain(p1 | (p1 << n), strict),
                    }
                    report["orders"].append({
                        "n": n,
                        "naturally_labelled_posets": poset_count,
                        "convex_subsets_tested_before_failure": convex_count,
                        "minimum_slack": min_slack,
                    })
                    report["enumeration_sha256"] = digest.hexdigest()
                    return report
        report["orders"].append({
            "n": n,
            "naturally_labelled_posets": poset_count,
            "convex_subsets": convex_count,
            "inequalities_tested": tested_count,
            "minimum_slack": min_slack,
        })
    report["enumeration_sha256"] = digest.hexdigest()
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run(args.max_n)
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
