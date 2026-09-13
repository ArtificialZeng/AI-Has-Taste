#!/usr/bin/env python3
"""External-cwd normal/-O tamper matrix for verify_release_binding.py."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BINDER = PROJECT / "code" / "verify_release_binding.py"
BINDING = PROJECT / "certificates" / "i3_release_binding.json"


def stage(case_root: Path) -> tuple[Path, Path]:
    root = case_root / "project-copy"
    (root / "certificates").mkdir(parents=True)
    (root / "code").mkdir()
    shutil.copy2(PROJECT / "certificates" / "i3_scan_100m.json",
                 root / "certificates" / "i3_scan_100m.json")
    shutil.copy2(PROJECT / "certificates" / "i3_verify_100m_strict.txt",
                 root / "certificates" / "i3_verify_100m_strict.txt")
    shutil.copy2(PROJECT / "code" / "verify_i3.cpp",
                 root / "code" / "verify_i3.cpp")
    binding = case_root / "binding.json"
    shutil.copy2(BINDING, binding)
    return root, binding


def run(case: str, optimize: bool = False,
        mutate: Callable[[Path, Path], None] | None = None) -> tuple[int, str]:
    with tempfile.TemporaryDirectory(prefix=f"erdos699-{case}-") as directory:
        external_cwd = Path(directory)
        root, binding = stage(external_cwd)
        if mutate is not None:
            mutate(root, binding)
        command = [sys.executable]
        if optimize:
            command.append("-O")
        command.extend([
            str(BINDER), "--root", str(root), "--binding", str(binding)
        ])
        completed = subprocess.run(
            command,
            cwd=external_cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        return completed.returncode, completed.stdout.strip()


def rewrite_certificate(root: Path, transform: Callable[[dict[str, object]], None]) -> None:
    path = root / "certificates" / "i3_scan_100m.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    transform(data)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def changed_endpoint(root: Path, _binding: Path) -> None:
    rewrite_certificate(root, lambda data: data.__setitem__("n_max", 99_999_999))


def changed_count(root: Path, _binding: Path) -> None:
    rewrite_certificate(
        root, lambda data: data.__setitem__("candidate_indices_tested", 43_631_335_535)
    )


def bad_hash(root: Path, _binding: Path) -> None:
    source = root / "code" / "verify_i3.cpp"
    source.write_bytes(source.read_bytes() + b"\n")


def truncated_output(root: Path, _binding: Path) -> None:
    output = root / "certificates" / "i3_verify_100m_strict.txt"
    output.write_text("VERIFIED erdos699 i=3 n=[8,100000000]", encoding="utf-8")


def duplicate_certificate_field(root: Path, _binding: Path) -> None:
    path = root / "certificates" / "i3_scan_100m.json"
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace('"i": 3,', '"i": 3,\n  "i": 3,', 1),
                    encoding="utf-8")


def duplicate_binding_field(_root: Path, binding: Path) -> None:
    text = binding.read_text(encoding="utf-8")
    binding.write_text(text.replace('"i": 3,', '"i": 3,\n  "i": 3,', 1),
                       encoding="utf-8")


def main() -> int:
    checks: list[tuple[str, bool, Callable[[Path, Path], None] | None, int]] = [
        ("valid_normal_external_cwd", False, None, 0),
        ("valid_python_O_external_cwd", True, None, 0),
        ("changed_endpoint", False, changed_endpoint, 2),
        ("bad_hash", False, bad_hash, 2),
        ("changed_count_false_null", False, changed_count, 2),
        ("truncated_output", False, truncated_output, 2),
        ("duplicate_certificate_field", False, duplicate_certificate_field, 2),
        ("duplicate_binding_field", False, duplicate_binding_field, 2),
    ]
    failures = 0
    for name, optimize, mutate, expected in checks:
        rc, output = run(name, optimize=optimize, mutate=mutate)
        print(f"{name}: rc={rc} expected={expected} output={output}")
        if rc != expected:
            failures += 1
    if failures:
        print(f"TAMPER MATRIX FAILED cases={failures}", file=sys.stderr)
        return 1
    print("TAMPER MATRIX PASSED cases=8 external_cwd=true python_normal=true python_O=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
