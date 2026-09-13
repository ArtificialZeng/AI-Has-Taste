#!/usr/bin/env python3
"""Negative controls for sweep scanners and the certificate aggregator."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_RUN = ROOT / "logs" / "runs" / "baseline_n9_builder_full"
AGGREGATOR = ROOT / "code" / "aggregate_sweep.py"
BUILDER = ROOT / "code" / "builder_scan"
CERTIFIER = ROOT / "code" / "certifier_scan"


def aggregate(run_dir: Path, *, expected: int = 191536, role: str = "builder") -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [
            "python3",
            str(AGGREGATOR),
            "--run-dir",
            str(run_dir),
            "--role",
            role,
            "--n",
            "9",
            "--target",
            "9",
            "--modulus",
            "4",
            "--expect-total",
            str(expected),
            "--scanner",
            str(BUILDER),
            "--output",
            str(run_dir / "aggregate.json"),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def demand_rejection(name: str, result: subprocess.CompletedProcess[bytes]) -> None:
    assert result.returncode != 0, f"negative control accepted: {name}"
    assert b"AGGREGATE_FAIL" in result.stdout, (name, result.stdout)
    print(f"REJECT_OK {name}")


def scanner_controls() -> None:
    cases = [("short-line", b"101\n"), ("nonbinary", b"x" * 36 + b"\n")]
    for scanner in (BUILDER, CERTIFIER):
        for name, payload in cases:
            result = subprocess.run(
                [str(scanner), "9", "9"],
                input=payload,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            assert result.returncode == 2, (scanner, name, result.returncode, result.stdout)
            assert b"MALFORMED" in result.stdout
            print(f"REJECT_OK {scanner.name}-{name}")


def main() -> None:
    if not SOURCE_RUN.is_dir():
        raise SystemExit(f"missing baseline fixture: {SOURCE_RUN}")
    scanner_controls()
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary) / "base"
        shutil.copytree(SOURCE_RUN, base)
        good = aggregate(base)
        assert good.returncode == 0 and b"AGGREGATE_OK" in good.stdout
        print("POSITIVE_CONTROL_OK aggregate")

        missing = Path(temporary) / "missing"
        shutil.copytree(SOURCE_RUN, missing)
        (missing / "slice_0000_of_0004.status").unlink()
        demand_rejection("missing-status", aggregate(missing))

        bad_status = Path(temporary) / "bad-status"
        shutil.copytree(SOURCE_RUN, bad_status)
        (bad_status / "slice_0001_of_0004.status").write_text("1\n", encoding="ascii")
        demand_rejection("nonzero-status", aggregate(bad_status))

        malformed = Path(temporary) / "malformed"
        shutil.copytree(SOURCE_RUN, malformed)
        log = malformed / "slice_0002_of_0004.log"
        log.write_text(log.read_text(encoding="utf-8") + "BUILDER_OK garbage\n", encoding="utf-8")
        # The extra garbage line is harmless; replace the actual summary to force failure.
        log.write_text("BUILDER_OK garbage\n", encoding="utf-8")
        demand_rejection("malformed-summary", aggregate(malformed))

        wrong_total = Path(temporary) / "wrong-total"
        shutil.copytree(SOURCE_RUN, wrong_total)
        demand_rejection("wrong-exact-total", aggregate(wrong_total, expected=191535))

        wrong_role = Path(temporary) / "wrong-role"
        shutil.copytree(SOURCE_RUN, wrong_role)
        demand_rejection("role-mismatch", aggregate(wrong_role, role="certifier"))

    print("SWEEP_NEGATIVE_CONTROLS_OK count=9")


if __name__ == "__main__":
    main()
