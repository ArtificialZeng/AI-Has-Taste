#!/usr/bin/env python3
"""Independent, fail-closed verifier for the Appendix C radius-six/seven claims.

This file imports no discovery module.  Distances are recomputed as
2*rank(U+W)-rank(U)-rank(W), whereas discovery used membership-mask
intersections.  The local clique subproblems are checked by exhaustive subset
dynamic programming (at most 2^15 subsets at radius seven), not discovery's
coloring branch-and-bound.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any


N = 7


class VerificationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def exact_keys(value: dict[str, Any], expected: set[str], location: str) -> None:
    require(set(value) == expected, f"{location}: key set mismatch")


def load_json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise VerificationError(f"cannot parse {path}: {exc}") from exc
    require(isinstance(value, dict), f"{path}: top level must be an object")
    return value


def canonical_line(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def row_reduce(rows: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    work = [row for row in rows if row]
    rank = 0
    for col in range(N):
        pivot = None
        for index in range(rank, len(work)):
            if (work[index] >> col) & 1:
                pivot = index
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for index in range(len(work)):
            if index != rank and ((work[index] >> col) & 1):
                work[index] ^= work[rank]
        rank += 1
        if rank == len(work):
            break
    return tuple(work[:rank])


def rank(rows: tuple[int, ...] | list[int]) -> int:
    return len(row_reduce(rows))


def subspace_distance(first: tuple[int, ...], second: tuple[int, ...]) -> int:
    return 2 * rank(first + second) - len(first) - len(second)


def membership_fingerprint(basis: tuple[int, ...]) -> int:
    vectors = [0]
    for row in basis:
        vectors += [value ^ row for value in vectors]
    mask = 0
    for value in vectors:
        mask |= 1 << value
    return mask


def parse_basis(raw: Any, location: str) -> tuple[int, ...]:
    require(isinstance(raw, list), f"{location}: basis must be a list")
    rows: list[int] = []
    for index, text in enumerate(raw):
        require(isinstance(text, str), f"{location}[{index}]: row must be text")
        require(len(text) == N and set(text) <= {"0", "1"}, f"{location}[{index}]: invalid row")
        rows.append(sum((character == "1") << col for col, character in enumerate(text)))
    canonical = row_reduce(rows)
    require(tuple(rows) == canonical, f"{location}: basis is not full-rank RREF")
    return canonical


def basis_text(basis: tuple[int, ...]) -> list[str]:
    return ["".join("1" if (row >> col) & 1 else "0" for col in range(N)) for row in basis]


def parse_matrix(raw: Any, location: str) -> tuple[int, ...]:
    require(isinstance(raw, list) and len(raw) == N, f"{location}: matrix must have seven rows")
    return parse_basis(raw, location) if False else tuple(
        sum((character == "1") << col for col, character in enumerate(row))
        for row in raw
        if isinstance(row, str) and len(row) == N and set(row) <= {"0", "1"}
    )


def checked_matrix(raw: Any, location: str) -> tuple[int, ...]:
    matrix = parse_matrix(raw, location)
    require(len(matrix) == N, f"{location}: invalid binary rows")
    require(rank(matrix) == N, f"{location}: matrix is singular")
    return matrix


def apply_row(vector: int, matrix: tuple[int, ...]) -> int:
    result = 0
    for index in range(N):
        if (vector >> index) & 1:
            result ^= matrix[index]
    return result


def apply_space(basis: tuple[int, ...], matrix: tuple[int, ...]) -> tuple[int, ...]:
    return row_reduce(tuple(apply_row(row, matrix) for row in basis))


def decode_representative(text: Any, location: str) -> tuple[int, ...]:
    require(isinstance(text, str) and len(text) == N and set(text) <= set("01234567"),
            f"{location}: invalid representative")
    rows = [0, 0, 0]
    for col, character in enumerate(text):
        digit = int(character)
        for row in range(3):
            if (digit >> row) & 1:
                rows[row] |= 1 << col
    canonical = row_reduce(rows)
    require(len(canonical) == 3, f"{location}: representative rank is not three")
    return canonical


def orbit(seed: tuple[int, ...], generators: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    seen = {seed}
    queue = deque([seed])
    while queue:
        current = queue.popleft()
        for generator in generators:
            image = apply_space(current, generator)
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return seen


def load_appendix(path: Path) -> list[tuple[int, ...]]:
    raw = load_json_object(path)
    exact_keys(raw, {"schema", "source", "encoding", "action_convention", "generators", "expected_orbit_census", "representatives"}, "appendix")
    require(raw["schema"] == "appendix-c-333-v1", "appendix: wrong schema")
    require(isinstance(raw["source"], dict), "appendix.source must be an object")
    exact_keys(raw["source"], {"title", "authors", "doi", "arxiv", "locator"}, "appendix.source")
    require(raw["source"]["doi"] == "10.3934/amc.2019029", "appendix: wrong DOI")
    require(raw["source"]["arxiv"] == "1708.06224v5", "appendix: wrong arXiv version")
    require(isinstance(raw["generators"], list) and len(raw["generators"]) == 2, "appendix: need two generators")
    generators = tuple(checked_matrix(matrix, f"appendix.generators[{i}]") for i, matrix in enumerate(raw["generators"]))
    expected = {"1": 9, "2": 26, "4": 68}
    require(raw["expected_orbit_census"] == expected, "appendix: wrong expected orbit census")
    require(isinstance(raw["representatives"], dict), "appendix.representatives must be an object")
    exact_keys(raw["representatives"], set(expected), "appendix.representatives")
    code: set[tuple[int, ...]] = set()
    observed: Counter[int] = Counter()
    for length_text in ("1", "2", "4"):
        representatives = raw["representatives"][length_text]
        require(isinstance(representatives, list) and len(representatives) == expected[length_text],
                f"appendix: wrong number of length-{length_text} representatives")
        for index, text in enumerate(representatives):
            current = orbit(decode_representative(text, f"representatives.{length_text}[{index}]"), generators)
            require(len(current) == int(length_text), f"appendix: orbit length mismatch at {text}")
            require(not code.intersection(current), f"appendix: duplicate orbit at {text}")
            code.update(current)
            observed[len(current)] += 1
    require(observed == Counter({1: 9, 2: 26, 4: 68}), "appendix: observed orbit census mismatch")
    require(len(code) == 333, "appendix: reconstructed code does not have 333 words")
    ordered = sorted(code, key=membership_fingerprint)
    for index, first in enumerate(ordered):
        require(len(first) == 3, "appendix: non-plane word")
        for second in ordered[index + 1:]:
            require(subspace_distance(first, second) >= 4, "appendix: minimum-distance violation")
    return ordered


def enumerate_rref_subspaces() -> list[tuple[int, ...]]:
    result: list[tuple[int, ...]] = []
    for dimension in range(N + 1):
        for pivots in itertools.combinations(range(N), dimension):
            pivot_set = set(pivots)
            positions = [(row, col) for row, pivot in enumerate(pivots)
                         for col in range(N) if col not in pivot_set and col > pivot]
            for bits in range(1 << len(positions)):
                rows = [1 << pivot for pivot in pivots]
                for index, (row, col) in enumerate(positions):
                    if (bits >> index) & 1:
                        rows[row] |= 1 << col
                basis = tuple(rows)
                require(row_reduce(basis) == basis, "enumerator produced non-RREF basis")
                result.append(basis)
    require(len(result) == 29212 and len(set(result)) == 29212, "ambient RREF census mismatch")
    require(Counter(map(len, result)) == Counter({0: 1, 1: 127, 2: 2667, 3: 11811, 4: 11811, 5: 2667, 6: 127, 7: 1}),
            "ambient layer census mismatch")
    return result


def verify_code_certificate(path: Path) -> str:
    raw = load_json_object(path)
    exact_keys(raw, {"schema", "ambient_field_order", "ambient_dimension", "minimum_subspace_distance", "claimed_size", "provenance", "codewords"}, "code certificate")
    require(raw["schema"] == "subspace-code-certificate-v1", "code certificate: wrong schema")
    require(raw["ambient_field_order"] == 2 and raw["ambient_dimension"] == 7, "code certificate: wrong ambient space")
    require(raw["minimum_subspace_distance"] == 4 and raw["claimed_size"] == 334, "code certificate: wrong claim")
    require(isinstance(raw["provenance"], dict), "code certificate: provenance must be an object")
    exact_keys(raw["provenance"], {"base_code", "extension"}, "code certificate.provenance")
    require(isinstance(raw["codewords"], list) and len(raw["codewords"]) == 334, "code certificate: wrong number of codewords")
    code: list[tuple[int, ...]] = []
    for index, item in enumerate(raw["codewords"]):
        require(isinstance(item, dict), f"codewords[{index}] must be an object")
        exact_keys(item, {"basis"}, f"codewords[{index}]")
        code.append(parse_basis(item["basis"], f"codewords[{index}].basis"))
    require(len(set(code)) == 334, "code certificate: duplicate codewords")
    require(Counter(map(len, code)) == Counter({3: 333, 7: 1}), "code certificate: wrong dimension distribution")
    for index, first in enumerate(code):
        for second in code[index + 1:]:
            require(subspace_distance(first, second) >= 4, "code certificate: distance below four")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def elements(mask: int) -> tuple[int, ...]:
    values: list[int] = []
    while mask:
        bit = mask & -mask
        values.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(values)


def subsets(mask: int) -> list[int]:
    values = elements(mask)
    result: list[int] = []
    for size in range(len(values) + 1):
        for choice in itertools.combinations(values, size):
            value = 0
            for element in choice:
                value |= 1 << element
            result.append(value)
    return result


def independent_union_closure(blockers: set[int], radius: int) -> list[int]:
    # Alternative to discovery's overlap index: split each blocker B in all
    # ways as Q union T, then query Q subset R and T disjoint R.
    extensions: dict[tuple[int, int], set[int]] = defaultdict(set)
    for blocker in blockers:
        for old_part in subsets(blocker):
            new_part = blocker ^ old_part
            if new_part:
                extensions[(old_part, new_part.bit_count())].add(new_part)
    seen = set(blockers)
    seen.add(0)
    queue = deque(sorted(seen, key=lambda value: (value.bit_count(), value)))
    while queue:
        current = queue.popleft()
        room = radius - current.bit_count()
        if room <= 0:
            continue
        for old_part in subsets(current):
            for new_size in range(1, room + 1):
                for new_part in extensions.get((old_part, new_size), ()):
                    if current & new_part:
                        continue
                    combined = current | new_part
                    if combined not in seen:
                        seen.add(combined)
                        queue.append(combined)
    return sorted(seen, key=lambda value: (value.bit_count(), value))


def exhaustive_clique_number(vertices: list[tuple[int, ...]], vertex_cap: int) -> int:
    count = len(vertices)
    require(count <= vertex_cap, f"clique subproblem exceeds certified {vertex_cap}-vertex cap")
    adjacency = [0] * count
    for i, first in enumerate(vertices):
        for j in range(i + 1, count):
            if subspace_distance(first, vertices[j]) >= 4:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    is_clique = bytearray(1 << count)
    is_clique[0] = 1
    best = 0
    for candidate in range(1, 1 << count):
        bit = candidate & -candidate
        vertex = bit.bit_length() - 1
        remainder = candidate ^ bit
        if is_clique[remainder] and not (remainder & ~adjacency[vertex]):
            is_clique[candidate] = 1
            best = max(best, candidate.bit_count())
    return best


def verify_serialized_witnesses(raw: dict[str, Any], planes: list[tuple[int, ...]],
                                candidates_by_blocker: dict[int, list[tuple[int, ...]]], radius: int) -> None:
    witnesses = raw["selected_witnesses"]
    require(isinstance(witnesses, dict) and set(witnesses) == {str(i) for i in range(radius + 1)},
            "result: selected_witnesses keys mismatch")
    for removed_text, witness in witnesses.items():
        require(isinstance(witness, dict), "result: witness must be an object")
        exact_keys(witness, {"removed_indices", "added_bases", "eligible_candidate_count", "addition_clique_size", "result_size"},
                   f"witness[{removed_text}]")
        removed = witness["removed_indices"]
        require(isinstance(removed, list) and removed == sorted(set(removed)), "witness: removals not sorted/unique")
        require(all(isinstance(x, int) and 0 <= x < 333 for x in removed), "witness: removal out of range")
        require(len(removed) == int(removed_text), "witness: removal size/key mismatch")
        removal_mask = sum(1 << x for x in removed)
        additions = [parse_basis(item, f"witness[{removed_text}].added_bases") for item in witness["added_bases"]]
        require(len(additions) == witness["addition_clique_size"], "witness: addition size mismatch")
        eligible: list[tuple[int, ...]] = []
        for blocker in subsets(removal_mask):
            eligible.extend(candidates_by_blocker.get(blocker, ()))
        require(len(eligible) == witness["eligible_candidate_count"], "witness: eligible count mismatch")
        require(all(addition in eligible for addition in additions), "witness: ineligible addition")
        require(len(set(additions)) == len(additions), "witness: duplicate addition")
        kept = [plane for index, plane in enumerate(planes) if index not in set(removed)]
        assembled = kept + additions
        require(witness["result_size"] == len(assembled), "witness: result size mismatch")
        for i, first in enumerate(assembled):
            for second in assembled[i + 1:]:
                require(subspace_distance(first, second) >= 4, "witness: infeasible assembled code")


def verify_radius_result(path: Path, appendix_path: Path, radius: int) -> dict[str, Any]:
    raw = load_json_object(path)
    expected_keys = {
        "schema", "scope", "normalization", "arithmetic", "randomness", "python", "platform", "radius",
        "ambient_subspaces", "published_planes", "outside_candidates_by_blocker_count_0_through_6",
        "unique_blocker_sets_by_size_0_through_6", "normalized_removal_unions_by_size",
        "normalized_removal_unions_total", "maximum_eligible_candidate_count",
        "maximum_eligible_candidate_count_by_removed", "best_code_size",
        "best_code_size_by_normalized_removed", "sets_with_result_at_least_334", "selected_witnesses",
        "blocker_map_sha256", "full_search_trace_sha256", "data_sha256", "source_sha256",
        "elapsed_seconds_diagnostic_only"
    }
    exact_keys(raw, expected_keys, "result")
    expected_schema = "radius-six-exchange-search-v1" if radius == 6 else "radius-exchange-search-diagnostic-v1"
    require(raw["schema"] == expected_schema and raw["radius"] == radius,
            "result: wrong schema or radius")
    require(raw["arithmetic"] == "exact integer bit masks over F_2" and raw["randomness"] is None,
            "result: wrong arithmetic/randomness declaration")
    require(raw["data_sha256"] == hashlib.sha256(appendix_path.read_bytes()).hexdigest(),
            "result: Appendix data hash mismatch")

    planes = load_appendix(appendix_path)
    spaces = enumerate_rref_subspaces()
    plane_set = set(planes)
    candidates_by_blocker: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    limited: list[tuple[tuple[int, ...], int]] = []
    histogram: Counter[int] = Counter()
    for candidate in spaces:
        if candidate in plane_set:
            continue
        blocker = 0
        for index, plane in enumerate(planes):
            if subspace_distance(candidate, plane) < 4:
                blocker |= 1 << index
        histogram[blocker.bit_count()] += 1
        if blocker.bit_count() <= radius:
            candidates_by_blocker[blocker].append(candidate)
            limited.append((candidate, blocker))
    for blocker in candidates_by_blocker:
        candidates_by_blocker[blocker].sort(key=membership_fingerprint)

    blocker_hash = hashlib.sha256()
    for candidate, blocker in sorted(limited, key=lambda item: membership_fingerprint(item[0])):
        blocker_hash.update(canonical_line({"basis": basis_text(candidate), "blockers": list(elements(blocker))}))
    require(blocker_hash.hexdigest() == raw["blocker_map_sha256"], "result: blocker map digest mismatch")

    unions = independent_union_closure(set(candidates_by_blocker), radius)
    union_census = Counter(mask.bit_count() for mask in unions)
    trace = hashlib.sha256()
    best = -1
    best_by_removed = {size: -1 for size in range(radius + 1)}
    maximum_eligible = 0
    maximum_eligible_by_removed = {size: 0 for size in range(radius + 1)}
    at_least_334 = 0
    for removal in unions:
        eligible: list[tuple[int, ...]] = []
        for blocker in subsets(removal):
            eligible.extend(candidates_by_blocker.get(blocker, ()))
        eligible.sort(key=membership_fingerprint)
        omega = exhaustive_clique_number(eligible, 2 * radius + 1)
        removed_count = removal.bit_count()
        result_size = 333 - removed_count + omega
        best = max(best, result_size)
        best_by_removed[removed_count] = max(best_by_removed[removed_count], result_size)
        maximum_eligible = max(maximum_eligible, len(eligible))
        maximum_eligible_by_removed[removed_count] = max(maximum_eligible_by_removed[removed_count], len(eligible))
        if result_size >= 334:
            at_least_334 += 1
        trace.update(canonical_line({
            "removed_indices": list(elements(removal)),
            "eligible_candidate_count": len(eligible),
            "addition_clique_size": omega,
            "result_size": result_size
        }))

    computed = {
        "ambient_subspaces": len(spaces),
        "published_planes": len(planes),
        "outside_candidates_by_blocker_count_0_through_6": {str(i): histogram[i] for i in range(radius + 1)},
        "unique_blocker_sets_by_size_0_through_6": {
            str(i): sum(mask.bit_count() == i for mask in candidates_by_blocker) for i in range(radius + 1)
        },
        "normalized_removal_unions_by_size": {str(i): union_census[i] for i in range(radius + 1)},
        "normalized_removal_unions_total": len(unions),
        "maximum_eligible_candidate_count": maximum_eligible,
        "maximum_eligible_candidate_count_by_removed": {str(i): maximum_eligible_by_removed[i] for i in range(radius + 1)},
        "best_code_size": best,
        "best_code_size_by_normalized_removed": {str(i): best_by_removed[i] for i in range(radius + 1)},
        "sets_with_result_at_least_334": at_least_334,
        "full_search_trace_sha256": trace.hexdigest()
    }
    for key, value in computed.items():
        require(raw[key] == value, f"result: recomputed field mismatch: {key}")
    require(best == 334, "result: certified local optimum is not 334")
    verify_serialized_witnesses(raw, planes, candidates_by_blocker, radius)
    return computed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--appendix", type=Path, default=Path("data/appendix_c_333.json"))
    parser.add_argument("--code", type=Path, default=Path("certificates/published_334_code.json"))
    parser.add_argument("--result", type=Path, default=Path("experiments/radius6_search.json"))
    parser.add_argument("--radius", type=int, choices=(6, 7), default=6)
    parser.add_argument("--success-output", type=Path)
    args = parser.parse_args()
    code_hash = verify_code_certificate(args.code)
    computed = verify_radius_result(args.result, args.appendix, args.radius)
    record = {
        "status": "VERIFIED",
        "claim": f"the Appendix C 333-code plus V has size 334, and no exchange deleting at most {args.radius} Appendix C planes exceeds 334",
        "certified_radius": args.radius,
        "best_code_size_in_certified_radius": computed["best_code_size"],
        "normalized_removal_unions": computed["normalized_removal_unions_total"],
        "code_certificate_sha256": code_hash,
        "appendix_data_sha256": hashlib.sha256(args.appendix.read_bytes()).hexdigest(),
        "radius_result_sha256": hashlib.sha256(args.result.read_bytes()).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_assistant_used": False
    }
    output = canonical_line(record)
    if args.success_output is not None:
        args.success_output.write_bytes(output)
    sys.stdout.buffer.write(output)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VerificationError as exc:
        print(f"VERIFY_FAIL:{exc}", file=sys.stderr)
        raise SystemExit(1)
