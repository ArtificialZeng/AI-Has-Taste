#!/usr/bin/env python3
"""Positive and destructive-input tests for the standalone exact verifier."""

from __future__ import annotations

import pathlib
import subprocess
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "certificates" / "verify_n10.cpp"
CERTIFICATE = ROOT / "certificates" / "n10_finite_certificate.txt"


def run(executable: pathlib.Path, text: str) -> subprocess.CompletedProcess[str]:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", encoding="utf-8") as stream:
        stream.write(text)
        stream.flush()
        return subprocess.run(
            [str(executable), stream.name],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )


def main() -> int:
    original = CERTIFICATE.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="kl-r-fib-rejection-") as tmp:
        executable = pathlib.Path(tmp) / "verify_n10"
        subprocess.run(
            [
                "c++",
                "-O3",
                "-std=c++20",
                "-Wall",
                "-Wextra",
                "-Werror",
                "-pedantic",
                str(SOURCE),
                "-o",
                str(executable),
            ],
            check=True,
        )

        positive = run(executable, original)
        if positive.returncode != 0 or "CERTIFIED_FINITE_RESULT" not in positive.stdout:
            raise AssertionError(f"positive certificate failed:\n{positive.stdout}")

        corruptions = {
            "missing_end": original.replace("end=TRUE\n", ""),
            "duplicate_key": original + "endpoint_n=10\n",
            "wrong_endpoint": original.replace("endpoint_n=10", "endpoint_n=9"),
            "overflow_endpoint": original.replace("endpoint_n=10", "endpoint_n=4294967306"),
            "wrong_word": original.replace("omega=2,1", "omega=1,2"),
            "wrong_recurrence": original.replace("+xF_{h-2}", "-xF_{h-2}"),
            "unknown_key": original + "trust_discovery=TRUE\n",
            "wrong_pair_count": original.replace("6229297", "6229298"),
        }
        for name, damaged in corruptions.items():
            result = run(executable, damaged)
            if result.returncode == 0 or "REJECTED:" not in result.stdout:
                raise AssertionError(f"corruption {name} was not rejected:\n{result.stdout}")
            print(f"REJECTION_OK {name}")
    print("ALL_REJECTION_TESTS_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
