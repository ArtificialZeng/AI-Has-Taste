#!/usr/bin/env python3
"""Negative tests for the fail-closed scalar certificate verifier.

Every tampered certificate except ``badhash`` is supplied with its own actual
SHA-256 trust anchor.  Thus rejection must come from schema, type, or semantic
validation rather than merely from detecting changed bytes.
"""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Case:
    name: str
    transform: Callable[[dict[str, object]], None] | None
    expected_diagnostic: str
    raw_transform: Callable[[str], str] | None = None


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def set_extra(data: dict[str, object]) -> None:
    data["unexpected"] = 0


def drop_trace_key(data: dict[str, object]) -> None:
    del data["expected_trace"]["next_x_integer"]  # type: ignore[index]


def change_input(data: dict[str, object]) -> None:
    data["inputs"]["v_integer"] += 2  # type: ignore[index,operator]


def change_trace(data: dict[str, object]) -> None:
    data["expected_trace"]["next_x_integer"] = 1  # type: ignore[index]


def change_arithmetic(data: dict[str, object]) -> None:
    data["arithmetic"]["rounding"] = "roundTowardZero"  # type: ignore[index]


def insert_duplicate(raw: str) -> str:
    needle = '{\n  "schema_version": 1,'
    replacement = '{\n  "schema_version": 1,\n  "schema_version": 1,'
    if needle not in raw:
        raise RuntimeError("cannot construct duplicate-key fixture")
    return raw.replace(needle, replacement, 1)


def bool_as_int(data: dict[str, object]) -> None:
    data["inputs"]["A_integer"] = True  # type: ignore[index]


def float_as_int(data: dict[str, object]) -> None:
    data["exact_system"]["kappa2_A"] = 1.0  # type: ignore[index]


def nested_extra(data: dict[str, object]) -> None:
    data["arithmetic"]["unit_roundoff"]["extra"] = 0  # type: ignore[index]


def inject_nan(data: dict[str, object]) -> None:
    data["expected_trace"]["theta_integer"] = float("nan")  # type: ignore[index]


def change_exact_system(data: dict[str, object]) -> None:
    data["exact_system"]["B_integer"] += 2  # type: ignore[index,operator]


CASES = [
    Case("extra", set_extra, "top keys are not exact"),
    Case("drop", drop_trace_key, "expected_trace keys are not exact"),
    Case("change-input", change_input, "inputs differ from the audited instance"),
    Case("change-trace", change_trace, "correction/fixed-point trace mismatch"),
    Case("change-arithmetic", change_arithmetic, "unsupported arithmetic declaration"),
    Case("duplicate-key", None, "duplicate JSON key", raw_transform=insert_duplicate),
    Case("bool-as-int", bool_as_int, "must have exact type int"),
    Case("float-as-int", float_as_int, "must have exact type int"),
    Case("nested-extra", nested_extra, "unit_roundoff keys are not exact"),
    Case("nan", inject_nan, "non-standard JSON numeric constant"),
    Case("change-exact-system", change_exact_system, "serialized exact B is wrong"),
]


def run(verifier: Path, cert: Path, expected_hash: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(verifier),
            str(cert),
            "--expect-certificate-sha256",
            expected_hash,
        ],
        check=False,
        text=True,
        capture_output=True,
    )


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    verifier = root / "verification" / "verify_stagnation.py"
    certificate = root / "certificates" / "binary64_stagnation.json"
    base_raw = certificate.read_bytes()
    base_text = base_raw.decode("utf-8")
    base_data = json.loads(base_text)

    baseline = run(verifier, certificate, digest(base_raw))
    if baseline.returncode != 0:
        print("FAIL baseline certificate was rejected", file=sys.stderr)
        print(baseline.stderr, file=sys.stderr)
        return 1
    print("BASELINE rc=0 PASS")

    badhash = run(verifier, certificate, "0" * 64)
    if badhash.returncode == 0 or "SHA-256 mismatch" not in badhash.stderr:
        print("FAIL tamper=badhash was not rejected as a hash mismatch", file=sys.stderr)
        return 1
    print(f"TAMPER badhash rc={badhash.returncode} PASS")

    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="smir-tamper-") as tmp:
        tmpdir = Path(tmp)
        for case in CASES:
            data = copy.deepcopy(base_data)
            if case.transform is not None:
                case.transform(data)
            raw_text = json.dumps(data, indent=2, allow_nan=True) + "\n"
            if case.raw_transform is not None:
                raw_text = case.raw_transform(base_text)
            raw = raw_text.encode("utf-8")
            path = tmpdir / f"{case.name}.json"
            path.write_bytes(raw)
            result = run(verifier, path, digest(raw))
            diagnostic = result.stderr.strip().replace("\n", " | ")
            if result.returncode == 0:
                failures.append(f"{case.name}: verifier returned zero")
                print(f"TAMPER {case.name} rc=0 FAIL")
            elif case.expected_diagnostic not in result.stderr:
                failures.append(
                    f"{case.name}: missing diagnostic {case.expected_diagnostic!r}; "
                    f"got {diagnostic!r}"
                )
                print(f"TAMPER {case.name} rc={result.returncode} FAIL")
            else:
                print(f"TAMPER {case.name} rc={result.returncode} PASS")

    if failures:
        print("\n".join(f"FAIL {item}" for item in failures), file=sys.stderr)
        return 1
    print(f"TAMPER-SUITE PASS cases={len(CASES) + 1} all_nonzero=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
