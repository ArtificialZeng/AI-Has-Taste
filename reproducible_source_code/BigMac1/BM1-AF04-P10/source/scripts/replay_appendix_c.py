#!/usr/bin/env python3
"""Exact discovery replay for the published 333-plane construction.

This program is deliberately standard-library only.  It uses Python integers
as 128-bit membership masks for subspaces of F_2^7.  It is discovery/replay
code, not the independent verifier in ``verification/``.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
import time
from collections import Counter
from pathlib import Path


N = 7
ALL_VECTOR_MASK = (1 << (1 << N)) - 1


def rref(rows: list[int] | tuple[int, ...], n: int = N) -> tuple[int, ...]:
    work = [int(x) for x in rows if x]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(work)) if (work[i] >> col) & 1), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for i in range(len(work)):
            if i != rank and ((work[i] >> col) & 1):
                work[i] ^= work[rank]
        rank += 1
        if rank == len(work):
            break
    # Return the rows after *all* later-pivot eliminations.  Retaining a copy
    # at pivot-discovery time would span the same subspace but need not be RREF.
    return tuple(work[:rank])


def span_mask(rows: list[int] | tuple[int, ...]) -> int:
    members = [0]
    for row in rref(rows):
        members += [x ^ row for x in members]
    mask = 0
    for value in members:
        mask |= 1 << value
    return mask


def basis_from_mask(mask: int) -> tuple[int, ...]:
    vectors = [v for v in range(1, 1 << N) if (mask >> v) & 1]
    basis = rref(vectors)
    if span_mask(basis) != mask:
        raise AssertionError("membership mask is not a linear subspace")
    return basis


def dimension(mask: int) -> int:
    size = mask.bit_count()
    if size == 0 or size & (size - 1):
        raise AssertionError("subspace cardinality is not a power of two")
    return size.bit_length() - 1


def distance(a: int, b: int) -> int:
    intersection_size = (a & b).bit_count()
    if intersection_size == 0 or intersection_size & (intersection_size - 1):
        raise AssertionError("intersection cardinality is not a power of two")
    return dimension(a) + dimension(b) - 2 * (intersection_size.bit_length() - 1)


def enumerate_subspaces(n: int = N) -> list[int]:
    spaces: list[int] = []
    columns = range(n)
    for k in range(n + 1):
        for pivot_cols in itertools.combinations(columns, k):
            pivot_set = set(pivot_cols)
            free = [
                (row, col)
                for row, pivot in enumerate(pivot_cols)
                for col in columns
                if col not in pivot_set and col > pivot
            ]
            for assignment in range(1 << len(free)):
                rows = [1 << p for p in pivot_cols]
                for bit_index, (row, col) in enumerate(free):
                    if (assignment >> bit_index) & 1:
                        rows[row] |= 1 << col
                canonical = tuple(rows)
                if rref(canonical, n) != canonical:
                    raise AssertionError("RREF enumerator emitted a noncanonical basis")
                spaces.append(span_mask(canonical))
    if len(spaces) != len(set(spaces)):
        raise AssertionError("RREF enumeration has duplicates")
    return spaces


def parse_matrix(rows: list[str]) -> tuple[int, ...]:
    if len(rows) != N or any(len(row) != N or set(row) - {"0", "1"} for row in rows):
        raise ValueError("invalid 7x7 binary matrix")
    return tuple(sum((ch == "1") << j for j, ch in enumerate(row)) for row in rows)


def row_times_matrix(vector: int, matrix_rows: tuple[int, ...]) -> int:
    result = 0
    for i, row in enumerate(matrix_rows):
        if (vector >> i) & 1:
            result ^= row
    return result


def act(mask: int, matrix_rows: tuple[int, ...]) -> int:
    basis = basis_from_mask(mask)
    return span_mask(tuple(row_times_matrix(row, matrix_rows) for row in basis))


def decode_representative(encoded: str) -> int:
    if len(encoded) != N or any(ch not in "01234567" for ch in encoded):
        raise ValueError(f"invalid Appendix C representative: {encoded!r}")
    rows = [0, 0, 0]
    for col, ch in enumerate(encoded):
        digit = int(ch)
        for row in range(3):
            if (digit >> row) & 1:
                rows[row] |= 1 << col
    if len(rref(rows)) != 3:
        raise ValueError(f"Appendix C representative has rank below three: {encoded}")
    return span_mask(rows)


def orbit(seed: int, generators: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    seen = {seed}
    stack = [seed]
    while stack:
        current = stack.pop()
        for generator in generators:
            image = act(current, generator)
            if image not in seen:
                seen.add(image)
                stack.append(image)
    return tuple(sorted(seen))


def load_published_code(data_path: Path) -> tuple[list[int], dict[str, int]]:
    raw = json.loads(data_path.read_text(encoding="utf-8"))
    if raw.get("schema") != "appendix-c-333-v1":
        raise ValueError("unexpected Appendix C data schema")
    generators = tuple(parse_matrix(matrix) for matrix in raw["generators"])
    code: set[int] = set()
    observed: Counter[int] = Counter()
    representative_count = 0
    for expected_length_text, representatives in raw["representatives"].items():
        expected_length = int(expected_length_text)
        for encoded in representatives:
            representative_count += 1
            current_orbit = orbit(decode_representative(encoded), generators)
            observed[len(current_orbit)] += 1
            if len(current_orbit) != expected_length:
                raise AssertionError(
                    f"orbit length mismatch for {encoded}: {len(current_orbit)} != {expected_length}"
                )
            if code.intersection(current_orbit):
                raise AssertionError(f"duplicate Appendix C orbit at {encoded}")
            code.update(current_orbit)
    expected = {int(k): int(v) for k, v in raw["expected_orbit_census"].items()}
    if dict(observed) != expected:
        raise AssertionError(f"orbit census mismatch: {dict(observed)} != {expected}")
    if representative_count != 103 or len(code) != 333:
        raise AssertionError("Appendix C size mismatch")
    return sorted(code), {str(k): observed[k] for k in sorted(observed)}


def binary_row(row: int) -> str:
    return "".join("1" if (row >> col) & 1 else "0" for col in range(N))


def canonical_json_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data/appendix_c_333.json"))
    parser.add_argument("--code-output", type=Path, default=Path("certificates/published_334_code.json"))
    parser.add_argument("--report-output", type=Path, default=Path("experiments/baseline_replay.json"))
    parser.add_argument("--blocker-limit", type=int, default=6)
    args = parser.parse_args()
    if not 0 <= args.blocker_limit <= 333:
        parser.error("--blocker-limit must lie between 0 and 333")

    started = time.time()
    planes, orbit_census = load_published_code(args.data)
    for i, first in enumerate(planes):
        if dimension(first) != 3:
            raise AssertionError("published word is not three-dimensional")
        for second in planes[i + 1 :]:
            if distance(first, second) < 4:
                raise AssertionError("published planes violate minimum distance four")

    full_space = ALL_VECTOR_MASK
    mixed = planes + [full_space]
    for plane in planes:
        if distance(plane, full_space) != 4:
            raise AssertionError("full-space extension has incorrect distance")

    spaces = enumerate_subspaces()
    layer_census = Counter(dimension(mask) for mask in spaces)
    expected_layers = {0: 1, 1: 127, 2: 2667, 3: 11811, 4: 11811, 5: 2667, 6: 127, 7: 1}
    if dict(layer_census) != expected_layers or len(spaces) != 29212:
        raise AssertionError("ambient subspace census mismatch")

    plane_set = set(planes)
    blocker_histogram: Counter[int] = Counter()
    limited_candidates: list[tuple[int, tuple[int, ...]]] = []
    compatible_outside: list[int] = []
    for candidate in spaces:
        if candidate in plane_set:
            continue
        blockers = tuple(i for i, plane in enumerate(planes) if distance(candidate, plane) < 4)
        blocker_histogram[len(blockers)] += 1
        if not blockers:
            compatible_outside.append(candidate)
        if len(blockers) <= args.blocker_limit:
            limited_candidates.append((candidate, blockers))
    if compatible_outside != [full_space]:
        raise AssertionError("the unique direct extension is not the full space")

    code_payload = {
        "schema": "subspace-code-certificate-v1",
        "ambient_field_order": 2,
        "ambient_dimension": 7,
        "minimum_subspace_distance": 4,
        "claimed_size": 334,
        "provenance": {
            "base_code": "arXiv:1708.06224v5, Appendix C",
            "extension": "the whole ambient seven-space"
        },
        "codewords": [
            {"basis": [binary_row(row) for row in basis_from_mask(mask)]}
            for mask in sorted(mixed, key=lambda item: (dimension(item), basis_from_mask(item)))
        ]
    }
    code_bytes = canonical_json_bytes(code_payload)
    args.code_output.write_bytes(code_bytes)

    data_bytes = args.data.read_bytes()
    source_bytes = Path(__file__).read_bytes()
    report = {
        "schema": "appendix-c-replay-report-v1",
        "arithmetic": "exact integer bit masks over F_2",
        "randomness": None,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "appendix_data_sha256": sha256_bytes(data_bytes),
        "replay_source_sha256": sha256_bytes(source_bytes),
        "code_certificate_sha256": sha256_bytes(code_bytes),
        "published_plane_count": len(planes),
        "orbit_census": orbit_census,
        "minimum_distance": min(distance(a, b) for i, a in enumerate(planes) for b in planes[i + 1 :]),
        "mixed_code_size": len(mixed),
        "ambient_subspace_count": len(spaces),
        "ambient_layer_census": {str(k): layer_census[k] for k in range(8)},
        "compatible_outside_count": len(compatible_outside),
        "compatible_outside_bases": [
            [binary_row(row) for row in basis_from_mask(mask)] for mask in compatible_outside
        ],
        "blocker_histogram_0_through_limit": {
            str(k): blocker_histogram[k] for k in range(args.blocker_limit + 1)
        },
        "candidates_with_at_most_limit_blockers": len(limited_candidates),
        "blocker_limit": args.blocker_limit,
        "elapsed_seconds_diagnostic_only": round(time.time() - started, 6)
    }
    args.report_output.write_bytes(canonical_json_bytes(report))
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
