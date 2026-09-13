#!/usr/bin/env python3
"""Independent, fail-closed verifier for the serialized order-31 sweep.

This file imports no project module and does not call the production
aggregator.  It parses every completed chunk, binds the run to the preflight
artifact hashes, and reconstructs every serialized exceptional polynomial
from its parent array using a separately written exact Python evaluator.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ORDER = 31
MODULUS = 120
EXPECTED_TREES = 40_330_829_030
SAVE_LIMIT = 4096
MASK64 = (1 << 64) - 1
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "order31_sweep"
PREFLIGHT = ROOT / "certificates" / "order31_preflight.json"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL independent order-31 audit: {message}")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def nonnegative_decimal(text: str, field: str) -> int:
    if not text or any(character not in "0123456789" for character in text):
        fail(f"{field} is not a nonnegative decimal integer: {text!r}")
    return int(text)


def parse_summary(path: Path) -> dict[str, int | str | float]:
    try:
        raw = path.read_bytes()
        text = raw.decode("ascii")
    except (OSError, UnicodeDecodeError) as error:
        fail(f"cannot read strict ASCII summary {path}: {error}")
    if not text.endswith("\n") or text.count("\n") != 1:
        fail(f"summary must contain exactly one newline-terminated line: {path}")
    words = text[:-1].split(" ")
    if not words or words[0] != "RESEARCH_CHECK":
        fail(f"bad summary tag: {path}")
    fields: dict[str, str] = {}
    for word in words[1:]:
        if word.count("=") != 1:
            fail(f"bad summary token {word!r}: {path}")
        key, value = word.split("=", 1)
        if key in fields:
            fail(f"duplicate summary field {key}: {path}")
        fields[key] = value
    required = {
        "trees", "generated", "nonunimodal", "nonlogconcave",
        "sequence_hash", "parent_hash", "cpu",
    }
    if set(fields) != required:
        fail(f"summary field set mismatch: {path}")
    for hash_field in ("sequence_hash", "parent_hash"):
        value = fields[hash_field]
        if len(value) != 16 or any(c not in "0123456789abcdef" for c in value):
            fail(f"bad {hash_field}: {path}")
    try:
        cpu = float(fields["cpu"])
    except ValueError:
        fail(f"bad cpu field: {path}")
    if not (cpu >= 0.0 and cpu < float("inf")):
        fail(f"non-finite or negative cpu field: {path}")
    return {
        "trees": nonnegative_decimal(fields["trees"], "trees"),
        "generated": nonnegative_decimal(fields["generated"], "generated"),
        "nonunimodal": nonnegative_decimal(fields["nonunimodal"], "nonunimodal"),
        "nonlogconcave": nonnegative_decimal(fields["nonlogconcave"], "nonlogconcave"),
        "sequence_hash": fields["sequence_hash"],
        "parent_hash": fields["parent_hash"],
        "cpu": cpu,
    }


def add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return result


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def reconstruct(parent: list[int]) -> list[int]:
    n = len(parent)
    if n != ORDER or parent[0] != 0:
        fail("serialized parent array has wrong order or root marker")
    adjacency = [[] for _ in range(n)]
    seen_edges: set[tuple[int, int]] = set()
    for vertex in range(1, n):
        endpoint = parent[vertex] - 1
        if endpoint < 0 or endpoint >= n or endpoint == vertex:
            fail("serialized parent array has invalid endpoint")
        edge = (min(vertex, endpoint), max(vertex, endpoint))
        if edge in seen_edges:
            fail("serialized parent array has a repeated edge")
        seen_edges.add(edge)
        adjacency[vertex].append(endpoint)
        adjacency[endpoint].append(vertex)
    if len(seen_edges) != n - 1:
        fail("serialized parent array does not have n-1 distinct edges")

    visited: set[int] = set()

    def solve(vertex: int, predecessor: int) -> tuple[list[int], list[int]]:
        if vertex in visited:
            fail("cycle in serialized parent tree")
        visited.add(vertex)
        excluded = [1]
        included = [0, 1]
        for neighbour in adjacency[vertex]:
            if neighbour == predecessor:
                continue
            child_excluded, child_included = solve(neighbour, vertex)
            excluded = multiply(excluded, add(child_excluded, child_included))
            included = multiply(included, child_excluded)
        return excluded, included

    excluded, included = solve(0, -1)
    if len(visited) != n:
        fail("serialized parent tree is disconnected")
    coefficients = add(excluded, included)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def is_unimodal(coefficients: list[int]) -> bool:
    descending = False
    for left, right in zip(coefficients, coefficients[1:]):
        if right < left:
            descending = True
        elif right > left and descending:
            return False
    return True


def is_log_concave(coefficients: list[int]) -> bool:
    return all(
        coefficients[k] * coefficients[k]
        >= coefficients[k - 1] * coefficients[k + 1]
        for k in range(1, len(coefficients) - 1)
    )


def parse_exception(line: str, source: Path) -> str:
    words = line.split(" ")
    if len(words) != 4 or words[0] not in {"NONUNIMODAL", "NONLOGCONCAVE"}:
        fail(f"malformed exception line in {source}")
    values: dict[str, str] = {}
    for word in words[1:]:
        if word.count("=") != 1:
            fail(f"malformed exception token in {source}")
        key, value = word.split("=", 1)
        values[key] = value
    if set(values) != {"n", "parent", "coefficients"}:
        fail(f"exception field set mismatch in {source}")
    if nonnegative_decimal(values["n"], "exception n") != ORDER:
        fail(f"exception has wrong order in {source}")
    parent = [nonnegative_decimal(item, "parent entry")
              for item in values["parent"].split(",")]
    reported = [nonnegative_decimal(item, "coefficient")
                for item in values["coefficients"].split(",")]
    rebuilt = reconstruct(parent)
    if reported != rebuilt:
        fail(f"rebuilt coefficients disagree in {source}")
    if reported[0] != 1 or reported[1] != ORDER:
        fail(f"rebuilt polynomial failed constant/linear check in {source}")
    if words[0] == "NONUNIMODAL" and is_unimodal(reported):
        fail(f"false NONUNIMODAL label in {source}")
    if words[0] == "NONLOGCONCAVE" and is_log_concave(reported):
        fail(f"false NONLOGCONCAVE label in {source}")
    return words[0]


def main() -> None:
    try:
        preflight = json.loads(PREFLIGHT.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        fail(f"cannot read preflight: {error}")
    if (preflight.get("order"), preflight.get("modulus"),
            preflight.get("workers"), preflight.get("expected_tree_count")) != (
                ORDER, MODULUS, 8, EXPECTED_TREES):
        fail("preflight scope mismatch")
    frozen_hashes = preflight.get("sha256")
    if not isinstance(frozen_hashes, dict):
        fail("preflight lacks artifact hashes")
    verified_artifacts: dict[str, str] = {}
    for relative, expected_hash in sorted(frozen_hashes.items()):
        path = ROOT / relative
        observed = file_sha256(path)
        if observed != expected_hash:
            fail(f"artifact hash drift: {relative}")
        verified_artifacts[relative] = observed

    expected_names: set[str] = set()
    total_trees = total_generated = total_nonunimodal = total_nonlogconcave = 0
    sequence_hash = parent_hash = 0
    total_cpu = 0.0
    saved_nonunimodal = saved_nonlogconcave = 0
    serialized_digest = hashlib.sha256()

    for residue in range(MODULUS):
        stem = f"order{ORDER:02d}_chunk{residue:03d}_of_{MODULUS:03d}"
        summary_path = RESULTS / f"{stem}.summary.done"
        exceptions_path = RESULTS / f"{stem}.exceptions.done"
        expected_names.update({summary_path.name, exceptions_path.name})
        if not summary_path.is_file() or not exceptions_path.is_file():
            fail(f"missing paired completed files for residue {residue}")
        for path in (summary_path, exceptions_path):
            raw = path.read_bytes()
            serialized_digest.update(len(path.name).to_bytes(4, "big"))
            serialized_digest.update(path.name.encode("ascii"))
            serialized_digest.update(len(raw).to_bytes(8, "big"))
            serialized_digest.update(raw)

        summary = parse_summary(summary_path)
        trees = int(summary["trees"])
        generated = int(summary["generated"])
        if trees <= 0 or trees != generated:
            fail(f"checker/generator count mismatch at residue {residue}")
        total_trees += trees
        total_generated += generated
        total_nonunimodal += int(summary["nonunimodal"])
        total_nonlogconcave += int(summary["nonlogconcave"])
        sequence_hash = (sequence_hash + int(str(summary["sequence_hash"]), 16)) & MASK64
        parent_hash = (parent_hash + int(str(summary["parent_hash"]), 16)) & MASK64
        total_cpu += float(summary["cpu"])

        local_nonunimodal = local_nonlogconcave = 0
        try:
            exception_text = exceptions_path.read_text(encoding="ascii")
        except (OSError, UnicodeDecodeError) as error:
            fail(f"cannot read strict ASCII exceptions {exceptions_path}: {error}")
        for line in exception_text.splitlines():
            label = parse_exception(line, exceptions_path)
            if label == "NONUNIMODAL":
                local_nonunimodal += 1
            else:
                local_nonlogconcave += 1
        if local_nonunimodal != int(summary["nonunimodal"]):
            fail(f"NONUNIMODAL serialization count mismatch at residue {residue}")
        if local_nonlogconcave != min(int(summary["nonlogconcave"]), SAVE_LIMIT):
            fail(f"NONLOGCONCAVE serialization count mismatch at residue {residue}")
        saved_nonunimodal += local_nonunimodal
        saved_nonlogconcave += local_nonlogconcave

    actual_names = {path.name for path in RESULTS.glob("*.done") if path.is_file()}
    if actual_names != expected_names:
        fail("unexpected, missing, or misnamed .done artifacts")
    if total_trees != EXPECTED_TREES or total_generated != EXPECTED_TREES:
        fail(f"coverage total {total_trees} != {EXPECTED_TREES}")
    if total_nonunimodal != 0 or saved_nonunimodal != 0:
        fail(f"found {total_nonunimodal} non-unimodal trees")

    result = {
        "status": "PASS",
        "method": "independent no-project-import parser plus exact reconstruction of every serialized exception",
        "order": ORDER,
        "modulus": MODULUS,
        "chunks": MODULUS,
        "trees": total_trees,
        "generated": total_generated,
        "nonunimodal": total_nonunimodal,
        "nonlogconcave": total_nonlogconcave,
        "rebuilt_serialized_nonlogconcave": saved_nonlogconcave,
        "sequence_hash_sum_mod_2^64": f"{sequence_hash:016x}",
        "parent_hash_sum_mod_2^64": f"{parent_hash:016x}",
        "checker_cpu_seconds": round(total_cpu, 2),
        "serialized_done_set_sha256": serialized_digest.hexdigest(),
        "verified_artifact_sha256": verified_artifacts,
        "verifier_sha256": file_sha256(Path(__file__)),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
