#!/usr/bin/env python3
"""External four-mode genuine/tamper matrix for the t=18 verifier."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, NoReturn


CODE = Path(__file__).resolve()
PROJECT = CODE.parents[1]
VERIFIER = PROJECT / "certificate" / "t18_verify_endpoint_manifest.py"
CERTIFICATE = PROJECT / "certificate" / "t18_endpoint_manifest.json"


class MatrixError(Exception):
    pass


def fail(message: str) -> NoReturn:
    raise MatrixError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def set_scope_labels(data: dict[str, object]) -> None:
    data["scope"]["labels"] = 12


def set_gap_total(data: dict[str, object]) -> None:
    data["scope"]["positive_gap_total"] = 17


def set_denominator(data: dict[str, object]) -> None:
    data["rational_bound"]["denominator"] = 10**8


def change_formula(data: dict[str, object]) -> None:
    data["rational_bound"]["formula"] = "altered"


def change_term(data: dict[str, object]) -> None:
    data["rational_bound"]["term_lower_numerators"][0]["numerator"] += 1


def change_chain_bound(data: dict[str, object]) -> None:
    data["chain_bounds"][3]["general_minimum_lower_numerator"] += 1


def change_partition_total(data: dict[str, object]) -> None:
    data["partition_enumeration"]["total"] = 87


def remove_partition_survivor(data: dict[str, object]) -> None:
    data["partition_enumeration"]["survivors"].pop()


def change_endpoint_count(data: dict[str, object]) -> None:
    data["endpoint_loss_enumeration"]["records"][0]["compatible_assignment_count"] += 1


def change_r10_list(data: dict[str, object]) -> None:
    data["endpoint_loss_enumeration"]["R10_not_excluded_patterns"].pop()


def change_generator_hash(data: dict[str, object]) -> None:
    data["environment"]["generator_sha256"] = "0" * 64


def add_root_field(data: dict[str, object]) -> None:
    data["unexpected"] = True


def change_limitation(data: dict[str, object]) -> None:
    data["limitation"] = "claim expanded beyond certified scope"


def main() -> int:
    try:
        require(VERIFIER.is_file(), "verifier missing")
        require(CERTIFICATE.is_file(), "certificate missing")
        original = json.loads(CERTIFICATE.read_bytes())
        require(isinstance(original, dict), "certificate root must be an object")
        modes = {
            "normal": [],
            "optimized": ["-O"],
            "isolated": ["-I"],
            "optimized_isolated": ["-O", "-I"],
        }
        mutations: list[tuple[str, Callable[[dict[str, object]], None] | None]] = [
            ("genuine", None),
            ("missing_scope", lambda data: data.pop("scope")),
            ("changed_labels", set_scope_labels),
            ("changed_gap_total", set_gap_total),
            ("changed_denominator", set_denominator),
            ("changed_formula", change_formula),
            ("changed_term_numerator", change_term),
            ("changed_chain_bound", change_chain_bound),
            ("changed_partition_total", change_partition_total),
            ("removed_partition_survivor", remove_partition_survivor),
            ("changed_endpoint_count", change_endpoint_count),
            ("changed_R10_list", change_r10_list),
            ("changed_generator_hash", change_generator_hash),
            ("extra_root_field", add_root_field),
            ("changed_limitation", change_limitation),
        ]
        records = []
        with tempfile.TemporaryDirectory(prefix="kusner_t18_matrix_", dir="/private/tmp") as temp_name:
            temp = Path(temp_name)
            for mutation_name, mutate in mutations:
                candidate = copy.deepcopy(original)
                if mutate is not None:
                    mutate(candidate)
                input_path = temp / f"{mutation_name}.json"
                input_path.write_text(json.dumps(candidate, sort_keys=True) + "\n")
                for mode_name, flags in modes.items():
                    command = [sys.executable, *flags, str(VERIFIER), str(input_path)]
                    process = subprocess.run(command, cwd=temp, text=True, capture_output=True, timeout=60)
                    expected_pass = mutation_name == "genuine"
                    actual_pass = process.returncode == 0
                    require(actual_pass == expected_pass, f"unexpected exit for {mutation_name}/{mode_name}: {process.returncode}")
                    stream = process.stdout if actual_pass else process.stderr
                    try:
                        payload = json.loads(stream)
                    except json.JSONDecodeError as exc:
                        fail(f"non-JSON verifier output for {mutation_name}/{mode_name}: {exc}")
                    require(payload.get("status") == ("PASS" if expected_pass else "FAIL"), f"wrong status for {mutation_name}/{mode_name}")
                    records.append({
                        "mutation": mutation_name,
                        "mode": mode_name,
                        "expected_pass": expected_pass,
                        "returncode": process.returncode,
                        "status": payload.get("status"),
                        "input_sha256": digest(input_path),
                    })
        result = {
            "status": "PASS",
            "scope": "external t=18 verifier matrix; all mutations created in /private/tmp",
            "python": sys.version,
            "verifier_sha256": digest(VERIFIER),
            "certificate_sha256": digest(CERTIFICATE),
            "runner_sha256": digest(CODE),
            "modes": list(modes),
            "mutations": [name for name, _ in mutations],
            "executions": len(records),
            "records": records,
        }
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
