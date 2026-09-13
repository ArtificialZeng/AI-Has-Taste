#!/usr/bin/env python3
"""Independent exhaustive verifier for a serialized finite search result.

Trust boundary:
* no discovery module is imported;
* all semistandard tableaux are generated directly from shapes and fillings;
* P(word) is evaluated by column-inserting the reversed word;
* the complete packed membership-bit stream is rebuilt and hashed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import tempfile
from typing import Any, Iterable, Iterator


TOP_KEYS = {
    "schema_version",
    "claim",
    "parameters",
    "counts",
    "first_violation",
    "runtime_seconds_diagnostic_only",
    "artifacts",
}
PARAMETER_KEYS = {
    "u_alphabet",
    "u_require_packed",
    "u_min_length",
    "u_max_length",
    "w_alphabet",
    "w_min_length",
    "w_max_length",
    "k_first",
    "k_last_compared",
}
COUNT_KEYS = {
    "u_classes_by_length",
    "w_classes_by_length",
    "u_classes_total",
    "w_classes_total",
    "class_pairs",
    "membership_bits",
    "trace_bytes",
    "adjacent_membership_comparisons",
    "violations",
}
ARTIFACT_KEYS = {
    "trace_file",
    "trace_sha256",
    "discovery_source",
    "discovery_source_sha256",
    "sealer_source",
    "sealer_source_sha256",
    "python",
}


def fail(message: str) -> "NoReturn":  # type: ignore[name-defined]
    raise ValueError(message)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def partitions(total: int, maximum: int | None = None) -> Iterator[tuple[int, ...]]:
    """Partitions in a fixed deterministic order; zero has the empty shape."""
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def fillings(shape: tuple[int, ...], alphabet: int) -> Iterator[tuple[tuple[int, ...], ...]]:
    cells = [(i, j) for i, length in enumerate(shape) for j in range(length)]
    rows = [[0] * length for length in shape]

    def visit(position: int) -> Iterator[tuple[tuple[int, ...], ...]]:
        if position == len(cells):
            yield tuple(tuple(row) for row in rows)
            return
        i, j = cells[position]
        lower = 1
        if j:
            lower = max(lower, rows[i][j - 1])
        if i:
            lower = max(lower, rows[i - 1][j] + 1)
        for value in range(lower, alphabet + 1):
            rows[i][j] = value
            yield from visit(position + 1)

    yield from visit(0)


def tableau_key(tableau: tuple[tuple[int, ...], ...]) -> str:
    return "".join("[" + "".join(f"{x}," for x in row) + "]" for row in tableau)


def row_word(tableau: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(x for row in reversed(tableau) for x in row)


def tableau_classes(
    alphabet: int,
    min_length: int,
    max_length: int,
    packed_123: bool,
) -> tuple[list[tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]], dict[str, int]]:
    result: list[tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]] = []
    counts: dict[str, int] = {}
    for size in range(min_length, max_length + 1):
        at_size = []
        for shape in partitions(size):
            if len(shape) > alphabet:
                continue
            for tableau in fillings(shape, alphabet):
                if packed_123 and {x for row in tableau for x in row} != {1, 2, 3}:
                    continue
                at_size.append((tableau_key(tableau), tableau, row_word(tableau)))
        at_size.sort(key=lambda item: item[0])
        counts[str(size)] = len(at_size)
        result.extend((tableau, word) for _, tableau, word in at_size)
    return result, counts


def column_insert(tableau: list[list[int]], x: int) -> None:
    column = 0
    while True:
        hit = -1
        row = 0
        while row < len(tableau) and column < len(tableau[row]):
            if tableau[row][column] >= x:
                hit = row
                break
            row += 1
        if hit < 0:
            if row == len(tableau):
                if column != 0:
                    fail("internal invalid shape during column insertion")
                tableau.append([x])
            else:
                if len(tableau[row]) != column:
                    fail("internal invalid row boundary during column insertion")
                tableau[row].append(x)
            return
        tableau[hit][column], x = x, tableau[hit][column]
        column += 1


def insert_reversed_word(tableau: list[list[int]], reversed_word: tuple[int, ...]) -> None:
    for x in reversed_word:
        column_insert(tableau, x)


class HashingBitWriter:
    def __init__(self) -> None:
        self.digest = hashlib.sha256()
        self.byte = 0
        self.used = 0
        self.bits = 0
        self.bytes = 0
        self.buffer = bytearray()

    def write(self, bit: bool) -> None:
        self.byte = (self.byte << 1) | int(bit)
        self.used += 1
        self.bits += 1
        if self.used == 8:
            self._flush_byte()

    def _flush_byte(self) -> None:
        self.buffer.append(self.byte)
        self.byte = 0
        self.used = 0
        self.bytes += 1
        if len(self.buffer) == 1 << 16:
            self.digest.update(self.buffer)
            self.buffer.clear()

    def finish(self) -> str:
        if self.used:
            self.byte <<= 8 - self.used
            self._flush_byte()
        if self.buffer:
            self.digest.update(self.buffer)
            self.buffer.clear()
        return self.digest.hexdigest()


def exact_int(value: Any, name: str, minimum: int, maximum: int) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        fail(f"{name} is not an integer in [{minimum},{maximum}]")
    return value


def parse_and_check_artifacts(result_path: Path, source_dir: Path) -> dict[str, Any]:
    try:
        data = json.loads(result_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail(f"unreadable result JSON: {error}")
    optional_metadata = {"enumerator", "run_label"}
    if (
        type(data) is not dict
        or not TOP_KEYS <= set(data)
        or not (set(data) - TOP_KEYS) <= optional_metadata
    ):
        fail("top-level keys are missing or unexpected")
    if "enumerator" in data and data["enumerator"] != "six_coordinates_1a2b3c_over_2d3e_over_3f":
        fail("unknown tableau enumerator metadata")
    if "run_label" in data and (type(data["run_label"]) is not str or not data["run_label"]):
        fail("invalid run label metadata")
    if data["schema_version"] != 1 or data["claim"] != "finite_no_membership_change":
        fail("result does not claim a supported zero-violation finite run")
    if data["first_violation"] is not None:
        fail("zero-violation result contains a violation witness")
    if type(data["runtime_seconds_diagnostic_only"]) not in (int, float):
        fail("invalid diagnostic runtime")
    params = data["parameters"]
    counts = data["counts"]
    artifacts = data["artifacts"]
    if type(params) is not dict or set(params) != PARAMETER_KEYS:
        fail("parameter keys are missing or unexpected")
    if type(counts) is not dict or set(counts) != COUNT_KEYS:
        fail("count keys are missing or unexpected")
    if type(artifacts) is not dict or set(artifacts) != ARTIFACT_KEYS:
        fail("artifact keys are missing or unexpected")
    if params["u_alphabet"] != 3 or params["u_require_packed"] is not True:
        fail("this verifier only certifies 3-packed u")
    if params["w_min_length"] != 0:
        fail("w_min_length must be zero for the finite claim")

    u_min = exact_int(params["u_min_length"], "u_min_length", 3, 12)
    u_max = exact_int(params["u_max_length"], "u_max_length", u_min, 12)
    w_alphabet = exact_int(params["w_alphabet"], "w_alphabet", 1, 7)
    w_max = exact_int(params["w_max_length"], "w_max_length", 0, 24)
    k_first = exact_int(params["k_first"], "k_first", 3, 50)
    k_last = exact_int(params["k_last_compared"], "k_last_compared", k_first, 50)

    for key, hash_key, directory in (
        ("trace_file", "trace_sha256", result_path.parent),
        ("discovery_source", "discovery_source_sha256", source_dir),
        ("sealer_source", "sealer_source_sha256", source_dir),
    ):
        name = artifacts[key]
        if type(name) is not str or not name or Path(name).name != name:
            fail(f"unsafe or invalid artifact name in {key}")
        artifact_path = directory / name
        expected_hash = artifacts[hash_key]
        if type(expected_hash) is not str or len(expected_hash) != 64:
            fail(f"invalid declared hash for {key}")
        try:
            actual_hash = file_sha256(artifact_path)
        except OSError as error:
            fail(f"cannot read {artifact_path}: {error}")
        if actual_hash != expected_hash:
            fail(f"hash mismatch for {key}")

    trace_path = result_path.parent / artifacts["trace_file"]
    if type(counts["trace_bytes"]) is not int or trace_path.stat().st_size != counts["trace_bytes"]:
        fail("trace byte count mismatch")
    if counts["violations"] != 0:
        fail("finite no-change claim has a nonzero violation count")
    data["_validated"] = (u_min, u_max, w_alphabet, w_max, k_first, k_last)
    return data


def verify(result_path: Path, source_dir: Path) -> dict[str, Any]:
    data = parse_and_check_artifacts(result_path, source_dir)
    u_min, u_max, w_alphabet, w_max, k_first, k_last = data.pop("_validated")
    counts = data["counts"]
    expected_trace_hash = data["artifacts"]["trace_sha256"]

    core_source = source_dir / "verifier_core.cpp"
    if not core_source.is_file():
        fail("independent verifier_core.cpp is missing")
    with tempfile.TemporaryDirectory(prefix="plactic-certifier-") as temporary_name:
        temporary = Path(temporary_name)
        executable = temporary / "verifier_core"
        rebuilt_trace = temporary / "trace.bin"
        rebuilt_summary = temporary / "summary.json"
        compilation = subprocess.run(
            [
                "c++", "-std=c++20", "-O3", "-Wall", "-Wextra", "-Wpedantic",
                str(core_source), "-o", str(executable),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if compilation.returncode != 0:
            fail(f"independent verifier core did not compile: {compilation.stdout}")
        execution = subprocess.run(
            [
                str(executable), str(u_min), str(u_max), str(w_alphabet), str(w_max),
                str(k_first), str(k_last), str(rebuilt_trace), str(rebuilt_summary),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if execution.returncode != 0:
            fail(f"independent verifier core rejected the claim: {execution.stdout}")
        try:
            rebuilt = json.loads(rebuilt_summary.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            fail(f"invalid independent core summary: {error}")
        rebuilt_hash = file_sha256(rebuilt_trace)

    if counts["u_classes_by_length"] != rebuilt.get("u_counts"):
        fail("u class counts do not match direct SSYT enumeration")
    if counts["w_classes_by_length"] != rebuilt.get("w_counts"):
        fail("w class counts do not match direct SSYT enumeration")
    if counts["u_classes_total"] != rebuilt.get("u_total"):
        fail("u class total mismatch")
    if counts["w_classes_total"] != rebuilt.get("w_total"):
        fail("w class total mismatch")
    pairs = rebuilt.get("pairs")
    if counts["class_pairs"] != pairs:
        fail("class pair count mismatch")
    if counts["adjacent_membership_comparisons"] != pairs * (k_last - k_first + 1):
        fail("adjacent comparison count mismatch")
    if rebuilt.get("bits") != counts["membership_bits"]:
        fail("rebuilt membership bit count mismatch")
    if rebuilt.get("bytes") != counts["trace_bytes"]:
        fail("rebuilt trace byte count mismatch")
    if rebuilt.get("adjacent") != counts["adjacent_membership_comparisons"]:
        fail("rebuilt adjacent comparison count mismatch")
    if rebuilt.get("violations") != 0:
        fail(f"independent verifier found {rebuilt.get('violations')} membership changes")
    if rebuilt_hash != expected_trace_hash:
        fail("independently rebuilt trace hash mismatch")
    return {
        "u_classes": rebuilt["u_total"],
        "w_classes": rebuilt["w_total"],
        "pairs": pairs,
        "comparisons": counts["adjacent_membership_comparisons"],
        "trace_sha256": rebuilt_hash,
        "core_sha256": file_sha256(core_source),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    try:
        summary = verify(args.result.resolve(), args.source_dir.resolve())
    except (ValueError, OSError) as error:
        print(f"FINITE_VERIFY_REJECTED reason={error}")
        return 1
    print(
        "FINITE_VERIFY_OK"
        f" result_sha256={file_sha256(args.result)}"
        f" verifier_sha256={file_sha256(Path(__file__))}"
        f" core_sha256={summary['core_sha256']}"
        f" trace_sha256={summary['trace_sha256']}"
        f" u_classes={summary['u_classes']}"
        f" w_classes={summary['w_classes']}"
        f" class_pairs={summary['pairs']}"
        f" adjacent_comparisons={summary['comparisons']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
