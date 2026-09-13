#!/usr/bin/env python3
"""Positive and mutation tests for the independent LRAT verification gate."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "verification" / "verify_lrat.py"
CNF9 = ROOT / "instances" / "ekr_k4d3_n9.cnf"
CNF10 = ROOT / "instances" / "ekr_k4d3_n10.cnf"
PROOF8 = ROOT / "baseline" / "ekr_k4d3_n8_sat_trace.lrat"
PROOF9 = ROOT / "certificates" / "ekr_k4d3_n9.lrat"
PROOF10 = ROOT / "certificates" / "ekr_k4d3_n10.lrat"


def run(cnf: Path, proof: Path, n: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(cnf), str(proof), "--n", str(n)],
        text=True,
        capture_output=True,
        check=False,
    )


def require_acceptance(cnf: Path, proof: Path, n: int) -> None:
    result = run(cnf, proof, n)
    if result.returncode != 0 or "VERIFIED_UNSAT_LRAT" not in result.stdout:
        raise AssertionError(f"valid proof rejected: {result}")


def require_rejection(cnf: Path, proof: Path, n: int) -> None:
    result = run(cnf, proof, n)
    if result.returncode == 0 or "REJECTED:" not in result.stderr:
        raise AssertionError(f"bad proof accepted: {result}")


def main() -> int:
    require_acceptance(CNF9, PROOF9, 9)
    require_acceptance(CNF10, PROOF10, 10)
    proof9 = PROOF9.read_text(encoding="ascii")
    lines = proof9.splitlines()
    with tempfile.TemporaryDirectory(prefix="ekr-lrat-mutations-") as tmp:
        directory = Path(tmp)

        truncated = directory / "truncated.lrat"
        truncated.write_text("\n".join(lines[:-1]) + "\n", encoding="ascii")
        require_rejection(CNF9, truncated, 9)

        bad_hint = directory / "bad_hint.lrat"
        final_tokens = lines[-1].split()
        final_tokens[-2] = "99999999"
        bad_hint.write_text("\n".join([*lines[:-1], " ".join(final_tokens)]) + "\n", encoding="ascii")
        require_rejection(CNF9, bad_hint, 9)

        trailing = directory / "trailing_garbage.lrat"
        trailing.write_text(proof9 + "not-an-lrat-line\n", encoding="ascii")
        require_rejection(CNF9, trailing, 9)

        non_ascii = directory / "non_ascii.lrat"
        non_ascii.write_bytes(PROOF9.read_bytes() + "é\n".encode("utf-8"))
        require_rejection(CNF9, non_ascii, 9)

        nonexistent_deletion = directory / "nonexistent_deletion.lrat"
        nonexistent_deletion.write_text(
            "820 d 99999 0\n" + proof9,
            encoding="ascii",
        )
        require_rejection(CNF9, nonexistent_deletion, 9)

        excessive_step_id = directory / "excessive_step_id.lrat"
        excessive_step_id.write_text(
            proof9.replace("820 ", "2147483648 ", 1),
            encoding="ascii",
        )
        require_rejection(CNF9, excessive_step_id, 9)

        require_rejection(CNF10, PROOF9, 10)
        require_rejection(CNF9, PROOF8, 9)
    print("PASS: 2 LRAT certificates accepted; 8 truncated/mutated/mismatched traces rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
