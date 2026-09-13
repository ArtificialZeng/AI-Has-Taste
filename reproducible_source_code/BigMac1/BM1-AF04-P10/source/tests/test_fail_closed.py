#!/usr/bin/env python3
"""Destructive-input tests for the independent verifier.

Each case copies inputs into a temporary directory, corrupts exactly one
field, and requires a nonzero verifier exit containing ``VERIFY_FAIL``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def run_case(root: Path, name: str, appendix: object, code: object, result: object) -> str:
    case = root / name
    case.mkdir()
    appendix_path = case / "appendix.json"
    code_path = case / "code.json"
    result_path = case / "result.json"
    if isinstance(appendix, str):
        appendix_path.write_text(appendix, encoding="utf-8")
    else:
        write_json(appendix_path, appendix)
    if isinstance(code, str):
        code_path.write_text(code, encoding="utf-8")
    else:
        write_json(code_path, code)
    if isinstance(result, str):
        result_path.write_text(result, encoding="utf-8")
    else:
        write_json(result_path, result)
    completed = subprocess.run(
        [sys.executable, "verification/verify_radius6.py", "--appendix", str(appendix_path),
         "--code", str(code_path), "--result", str(result_path)],
        text=True, capture_output=True, check=False
    )
    if completed.returncode == 0 or "VERIFY_FAIL:" not in completed.stderr:
        raise AssertionError(f"{name}: corrupt input was not rejected\nstdout={completed.stdout}\nstderr={completed.stderr}")
    line = f"PASS {name}: {completed.stderr.strip()}"
    print(line)
    return line


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="also alter the decisive radius-six optimum; this reruns the full verifier")
    parser.add_argument("--success-output", type=Path, help="write a deterministic human-readable pass log")
    args = parser.parse_args()
    appendix_text = Path("data/appendix_c_333.json").read_text()
    code_text = Path("certificates/published_334_code.json").read_text()
    result_text = Path("experiments/radius6_search.json").read_text()
    appendix = json.loads(appendix_text)
    code = json.loads(code_text)
    result = json.loads(result_text)
    lines: list[str] = []
    with tempfile.TemporaryDirectory(prefix="a274-fail-closed-") as temporary:
        root = Path(temporary)

        duplicate_code = json.loads(json.dumps(code))
        duplicate_code["codewords"][1] = duplicate_code["codewords"][0]
        lines.append(run_case(root, "duplicate_codeword", appendix_text, duplicate_code, result_text))

        extra_key = json.loads(json.dumps(result))
        extra_key["untrusted_extra"] = 1
        lines.append(run_case(root, "unknown_result_key", appendix_text, code_text, extra_key))

        singular_generator = json.loads(json.dumps(appendix))
        singular_generator["generators"][0][0] = "0000000"
        singular_text = json.dumps(singular_generator, sort_keys=True, separators=(",", ":")) + "\n"
        singular_result = json.loads(json.dumps(result))
        singular_result["data_sha256"] = hashlib.sha256(singular_text.encode()).hexdigest()
        lines.append(run_case(root, "singular_group_generator", singular_text, code_text, singular_result))

        lines.append(run_case(root, "malformed_json", appendix_text, code_text, "{\"schema\":"))

        if args.full:
            false_optimum = json.loads(json.dumps(result))
            false_optimum["best_code_size"] = 335
            lines.append(run_case(root, "false_local_optimum", appendix_text, code_text, false_optimum))
    lines.append("ALL_FAIL_CLOSED_TESTS_PASSED")
    print(lines[-1])
    if args.success_output is not None:
        args.success_output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
