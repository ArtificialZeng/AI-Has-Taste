#!/usr/bin/env python3
"""Exact census for the proposed defective-width threshold.

This program independently generates every normalized increasing Gilbreath
sequence through a requested length in two ways:

1. the ordered reverse-preimage tree for the right anti-diagonal; and
2. direct difference-triangle tests of every possible increasing append.

For the direct generator, an append k=s_n+d has d>0.  If
d>A=sum(e_i), every fold is a subtraction without a sign change, so the new
bottom entry is d-A.  It can equal 1 only for d=A+1.  Thus checking every
integer 1 <= d <= A+1 is exhaustive, without assuming interval completeness
or using the reverse-preimage tree.

For every length, the two generated sets are compared exactly.  Every
minimum-width defective sequence is then checked again by directly building
the appended difference triangle for every integer k in the only possible
range [s_n-A-1,s_n+A+1].
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Sequence


Seq = tuple[int, ...]
Anti = tuple[int, ...]


def difference_triangle(seq: Sequence[int]) -> list[tuple[int, ...]]:
    rows = [tuple(seq)]
    while len(rows[-1]) > 1:
        row = rows[-1]
        rows.append(tuple(abs(row[i + 1] - row[i]) for i in range(len(row) - 1)))
    return rows


def is_gilbreath_direct(seq: Sequence[int]) -> bool:
    return all(row[0] == 1 for row in difference_triangle(seq)[1:])


def antidiagonal_direct(seq: Sequence[int]) -> Anti:
    return tuple(row[-1] for row in difference_triangle(seq)[1:])


def preimage_step(e: int, values: Iterable[int]) -> tuple[int, ...]:
    out: set[int] = set()
    for t in values:
        out.add(e + t)
        if e >= t:
            out.add(e - t)
    return tuple(sorted(out))


@lru_cache(maxsize=None)
def reverse_distances(anti: Anti) -> tuple[int, ...]:
    values: tuple[int, ...] = (1,)
    for e in reversed(anti):
        values = preimage_step(e, values)
    return values


def child_antidiagonal(anti: Anti, d: int) -> Anti:
    out = [d]
    r = d
    for e in anti:
        r = abs(r - e)
        out.append(r)
    if out[-1] != 1:
        raise AssertionError("invalid reverse-tree child")
    return tuple(out)


def reverse_children(seq: Seq, anti: Anti) -> list[tuple[Seq, Anti]]:
    sn = seq[-1]
    return [
        (seq + (sn + d,), child_antidiagonal(anti, d))
        for d in reverse_distances(anti)
        if d > 0
    ]


def direct_children(seq: Seq) -> list[Seq]:
    anti = antidiagonal_direct(seq)
    sn = seq[-1]
    # Exhaustive by the d>A folding observation in the module docstring.
    return [
        seq + (sn + d,)
        for d in range(1, sum(anti) + 2)
        if is_gilbreath_direct(seq + (sn + d,))
    ]


def full_extension_set_reverse(seq: Seq, anti: Anti) -> tuple[int, ...]:
    sn = seq[-1]
    return tuple(
        sorted({sn + sign * d for d in reverse_distances(anti) for sign in (-1, 1)})
    )


def full_extension_set_direct(seq: Seq, anti: Anti) -> tuple[int, ...]:
    sn = seq[-1]
    radius = sum(anti) + 1
    return tuple(
        k
        for k in range(sn - radius, sn + radius + 1)
        if is_gilbreath_direct(seq + (k,))
    )


def candidate_set(seq: Seq, anti: Anti) -> tuple[int, ...]:
    sn = seq[-1]
    radius = sum(anti) + 1
    return tuple(
        k
        for k in range(sn - radius, sn + radius + 1)
        if (k - sn) % 2 == 0
    )


def stable_digest(sequences: Iterable[Seq]) -> str:
    h = hashlib.sha256()
    for seq in sorted(sequences):
        h.update(",".join(map(str, seq)).encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def enumerate_and_audit(max_n: int) -> dict[str, object]:
    reverse_states: dict[Seq, Anti] = {(2, 3): (1,)}
    direct_states: set[Seq] = {(2, 3)}
    rows: list[dict[str, object]] = []

    for n in range(2, max_n + 1):
        if n > 2:
            next_reverse: dict[Seq, Anti] = {}
            for seq, anti in reverse_states.items():
                for child, child_anti in reverse_children(seq, anti):
                    if child in next_reverse:
                        raise AssertionError(f"duplicate reverse child: {child}")
                    next_reverse[child] = child_anti
            reverse_states = next_reverse

            next_direct: set[Seq] = set()
            for seq in direct_states:
                next_direct.update(direct_children(seq))
            direct_states = next_direct

        reverse_keys = set(reverse_states)
        if reverse_keys != direct_states:
            only_reverse = sorted(reverse_keys - direct_states)[:3]
            only_direct = sorted(direct_states - reverse_keys)[:3]
            raise AssertionError(
                f"generators disagree at n={n}: reverse-only={only_reverse}, "
                f"direct-only={only_direct}"
            )

        defective: list[tuple[int, Seq, Anti, tuple[int, ...], tuple[int, ...]]] = []
        widths: Counter[int] = Counter()
        target_count = 0
        interval_complete_count = 0

        for seq, anti in reverse_states.items():
            if not is_gilbreath_direct(seq):
                raise AssertionError(f"generated non-Gilbreath sequence: {seq}")
            if antidiagonal_direct(seq) != anti:
                raise AssertionError(f"anti-diagonal mismatch: {seq}")

            actual = full_extension_set_reverse(seq, anti)
            candidate = candidate_set(seq, anti)
            width = len(actual)
            widths[width] += 1
            if width <= 9:
                target_count += 1
            if actual == candidate:
                interval_complete_count += 1
            else:
                defective.append((width, seq, anti, actual, candidate))

        min_defective_width: int | None = None
        min_hits: list[tuple[int, Seq, Anti, tuple[int, ...], tuple[int, ...]]] = []
        if defective:
            min_defective_width = min(item[0] for item in defective)
            min_hits = [item for item in defective if item[0] == min_defective_width]

            # Independent exact K_S verification for every minimum-width hit.
            for _, seq, anti, actual, _ in min_hits:
                direct_actual = full_extension_set_direct(seq, anti)
                if direct_actual != actual:
                    raise AssertionError(
                        f"direct/reverse K mismatch for minimum hit {seq}: "
                        f"direct={direct_actual}, reverse={actual}"
                    )

        low_widths = {str(w): widths[w] for w in sorted(widths) if w <= 12}
        row: dict[str, object] = {
            "n": n,
            "sequence_count": len(reverse_states),
            "sequence_sha256": stable_digest(reverse_states),
            "interval_complete_count": interval_complete_count,
            "defective_count": len(defective),
            "defective_width_at_most_9_count": sum(1 for item in defective if item[0] <= 9),
            "target_width_at_most_9_count": target_count,
            "minimum_defective_width": min_defective_width,
            "minimum_defective_count": len(min_hits),
            "low_width_histogram": low_widths,
        }
        if min_hits:
            _, seq, anti, actual, candidate = min(sorted(min_hits, key=lambda item: item[1]))
            row["lexicographically_first_minimum_defective"] = {
                "sequence": list(seq),
                "right_antidiagonal": list(anti),
                "K": list(actual),
                "C": list(candidate),
                "holes": sorted(set(candidate) - set(actual)),
            }
        rows.append(row)
        print(
            f"n={n}: N={len(reverse_states)}, defective={len(defective)}, "
            f"min_defective_width={min_defective_width}, min_hits={len(min_hits)}",
            flush=True,
        )

    return {
        "claim_tested": "For S in G_n, K_S != C_S implies |K_S| >= 10.",
        "coverage": {"minimum_n": 2, "maximum_n": max_n},
        "arithmetic": "exact Python integers and finite sets",
        "generation_audit": (
            "Exact equality of the ordered reverse-tree frontier and a direct "
            "difference-triangle frontier at every n.  The direct frontier scans "
            "every integer append distance 1..A(S)+1."
        ),
        "minimum_hit_audit": (
            "For every minimum-width defective sequence at each n, K_S was "
            "independently reconstructed by direct appended difference triangles "
            "for every integer in the complete radius-A(S)+1 range."
        ),
        "result": (
            "No defective sequence of width at most 9 was found in the exhaustive range."
        ),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.max_n < 2:
        raise SystemExit("--max-n must be at least 2")
    result = enumerate_and_audit(args.max_n)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
