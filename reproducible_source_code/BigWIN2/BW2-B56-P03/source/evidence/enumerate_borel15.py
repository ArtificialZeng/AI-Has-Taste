#!/usr/bin/env python3
"""Exact census of colength-15 strongly stable monomial ideals in Q[x,y,z].

The first enumeration generates every 15-element coordinate downset and then
filters by the standard-set form of strong stability.  The second enumeration
does not generate arbitrary downsets: it recursively takes unions of the
finite closures forced by coordinate predecessors and Borel right shifts.

All output orderings and hashes are deterministic.  No floating-point
arithmetic is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import FrozenSet, Iterable, Iterator, Sequence

Point = tuple[int, int, int]
Shape = FrozenSet[Point]

N = 15
ORIGIN: Point = (0, 0, 0)


def point_key(p: Point) -> tuple[int, int, int, int]:
    """Canonical graded-lex key, with x exponent compared first."""
    return (sum(p), p[0], p[1], p[2])


def shape_key(shape: Shape) -> tuple[Point, ...]:
    return tuple(sorted(shape, key=point_key))


def predecessors(p: Point) -> Iterator[Point]:
    for i in range(3):
        if p[i]:
            q = list(p)
            q[i] -= 1
            yield tuple(q)  # type: ignore[return-value]


def addable_points(shape: Shape) -> set[Point]:
    """The outer corners that can be added while preserving down-closure."""
    if not shape:
        return {ORIGIN}
    candidates: set[Point] = set()
    for p in shape:
        for i in range(3):
            q = list(p)
            q[i] += 1
            candidates.add(tuple(q))  # type: ignore[arg-type]
    return {
        p for p in candidates
        if p not in shape and all(q in shape for q in predecessors(p))
    }


def all_downsets(n: int) -> set[Shape]:
    """Generate all n-element downsets by adding one outer corner at a time."""
    level: set[Shape] = {frozenset()}
    for _ in range(n):
        level = {
            shape | {p}
            for shape in level
            for p in addable_points(shape)
        }
    return level


def right_shifts(p: Point) -> Iterator[Point]:
    """Required same-degree standard monomials for x<y<z."""
    a, b, c = p
    if a:
        yield (a - 1, b + 1, c)
        yield (a - 1, b, c + 1)
    if b:
        yield (a, b - 1, c + 1)


def is_strong_standard_set(shape: Shape) -> bool:
    return all(q in shape for p in shape for q in right_shifts(p))


def enumerate_via_downsets(n: int) -> tuple[set[Shape], int]:
    downsets = all_downsets(n)
    return {s for s in downsets if is_strong_standard_set(s)}, len(downsets)


def candidate_points(n: int) -> tuple[Point, ...]:
    """Every point possible in an n-element downset has total degree < n."""
    points = [
        (a, b, d - a - b)
        for d in range(n)
        for a in range(d + 1)
        for b in range(d - a + 1)
    ]
    return tuple(sorted(points, key=point_key))


def forced_closure(p: Point) -> Shape:
    """Closure of one point under down-moves and Borel right shifts."""
    closure = {p}
    todo = [p]
    while todo:
        q = todo.pop()
        for r in (*predecessors(q), *right_shifts(q)):
            if r not in closure:
                closure.add(r)
                todo.append(r)
    return frozenset(closure)


def enumerate_via_forced_closures(n: int) -> set[Shape]:
    """Independently generate all closed standard sets of cardinality n.

    Each finite closed set is a union of the one-point closures of its
    elements.  Breadth-first union, pruned only when cardinality exceeds n,
    therefore reaches every target and nothing outside the closure class.
    """
    closures = tuple(forced_closure(p) for p in candidate_points(n))
    seen: set[Shape] = {frozenset()}
    frontier: set[Shape] = {frozenset()}
    answers: set[Shape] = set()
    while frontier:
        next_frontier: set[Shape] = set()
        for shape in frontier:
            for closure in closures:
                enlarged = shape | closure
                size = len(enlarged)
                if size > n or enlarged in seen:
                    continue
                seen.add(enlarged)
                if size == n:
                    answers.add(enlarged)
                else:
                    next_frontier.add(enlarged)
        frontier = next_frontier
    return answers


def minimal_generators(shape: Shape) -> tuple[Point, ...]:
    maxima = [max(p[i] for p in shape) + 1 for i in range(3)]
    gens: list[Point] = []
    for a in range(maxima[0] + 1):
        for b in range(maxima[1] + 1):
            for c in range(maxima[2] + 1):
                p = (a, b, c)
                if p not in shape and all(q in shape for q in predecessors(p)):
                    gens.append(p)
    return tuple(sorted(gens, key=point_key))


def pure_power_tuple(shape: Shape) -> tuple[int, int, int]:
    return tuple(
        min(
            e
            for e in range(1, len(shape) + 1)
            if tuple(e if j == i else 0 for j in range(3)) not in shape
        )
        for i in range(3)
    )  # type: ignore[return-value]


def encoded_shape(shape: Shape) -> dict[str, object]:
    standards = [list(p) for p in shape_key(shape)]
    generators = [list(p) for p in minimal_generators(shape)]
    m = list(pure_power_tuple(shape))
    raw_key = json.dumps(standards, separators=(",", ":"))
    return {
        "id": hashlib.sha256(raw_key.encode("ascii")).hexdigest()[:16],
        "m": m,
        "standard_monomials": standards,
        "minimal_generators": generators,
    }


def canonical_json_line(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def atlas_bytes(shapes: Iterable[Shape]) -> bytes:
    records = sorted((encoded_shape(s) for s in shapes), key=lambda r: (r["m"], r["standard_monomials"]))
    return ("\n".join(canonical_json_line(r) for r in records) + "\n").encode("ascii")


def check_shape(shape: Shape, n: int) -> None:
    assert len(shape) == n
    assert ORIGIN in shape
    assert all(q in shape for p in shape for q in predecessors(p))
    assert is_strong_standard_set(shape)
    gens = minimal_generators(shape)
    assert gens
    assert all(p not in shape for p in gens)
    assert all(all(q in shape for q in predecessors(p)) for p in gens)
    m = pure_power_tuple(shape)
    assert m[0] <= m[1] <= m[2]


def run(output_dir: Path, n: int) -> dict[str, object]:
    via_downsets, downset_count = enumerate_via_downsets(n)
    via_closures = enumerate_via_forced_closures(n)
    only_downsets = via_downsets - via_closures
    only_closures = via_closures - via_downsets
    if only_downsets or only_closures:
        raise RuntimeError(
            f"generator mismatch: downset-only={len(only_downsets)}, "
            f"closure-only={len(only_closures)}"
        )
    for shape in via_downsets:
        check_shape(shape, n)

    payload = atlas_bytes(via_downsets)
    digest = hashlib.sha256(payload).hexdigest()
    atlas_path = output_dir / f"borel-atlas-{n}.jsonl"
    summary_path = output_dir / f"borel-census-{n}.json"
    atlas_path.write_bytes(payload)

    m1_counts_a = Counter(pure_power_tuple(s)[0] for s in via_downsets)
    m1_counts_b = Counter(pure_power_tuple(s)[0] for s in via_closures)
    if m1_counts_a != m1_counts_b:
        raise RuntimeError(f"m1-stratified mismatch: {m1_counts_a} != {m1_counts_b}")
    m_counts = Counter(pure_power_tuple(s) for s in via_downsets)
    summary: dict[str, object] = {
        "colength": n,
        "coordinate_downsets": downset_count,
        "strongly_stable_ideals_generator_a": len(via_downsets),
        "strongly_stable_ideals_generator_b": len(via_closures),
        "canonical_key_set_equality": True,
        "generator_a_only": 0,
        "generator_b_only": 0,
        "m1_counts_generator_a": {
            str(k): m1_counts_a[k] for k in sorted(m1_counts_a)
        },
        "m1_counts_generator_b": {
            str(k): m1_counts_b[k] for k in sorted(m1_counts_b)
        },
        "m1_stratified_equality": True,
        "pure_power_tuple_counts": {
            ",".join(map(str, k)): m_counts[k] for k in sorted(m_counts)
        },
        "atlas_file": atlas_path.name,
        "atlas_sha256": digest,
        "atlas_bytes": len(payload),
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="ascii")
    return summary


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--colength", type=int, default=N)
    args = parser.parse_args(argv)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary = run(args.output_dir, args.colength)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
