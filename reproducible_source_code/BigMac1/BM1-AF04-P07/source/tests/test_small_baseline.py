#!/usr/bin/env python3
"""Reproduce the complete canonical baseline at orders 3 through 8."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ((3, 0, 2), (4, 1, 4), (5, 2, 12), (6, 3, 56), (7, 5, 456), (8, 7, 6880))


def run(scanner: Path, n: int, target: int, count: int) -> str:
    generator = subprocess.Popen(
        ["gentourng", "-q", str(n)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert generator.stdout is not None
    checked = subprocess.run(
        [str(scanner), str(n), str(target)],
        stdin=generator.stdout,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
        text=True,
    )
    generator.stdout.close()
    generator_stderr = generator.stderr.read() if generator.stderr is not None else b""
    generator_status = generator.wait()
    if generator_status != 0 or generator_stderr:
        raise AssertionError((generator_status, generator_stderr))
    expected_role = "BUILDER" if scanner.name == "builder_scan" else "CERTIFIER"
    pattern = re.compile(
        rf"^{expected_role}_OK n={n} target={target} count={count} "
        rf"sha256=[0-9a-f]{{64}} nodes=[1-9][0-9]* max_nodes=[1-9][0-9]*\n$"
    )
    assert checked.returncode == 0 and pattern.fullmatch(checked.stdout), checked.stdout
    return checked.stdout.strip()


def main() -> None:
    for scanner_name in ("builder_scan", "certifier_scan"):
        scanner = ROOT / "code" / scanner_name
        for n, target, count in CASES:
            print(run(scanner, n, target, count))
    print("SMALL_BASELINE_OK programs=2 orders=3..8")


if __name__ == "__main__":
    main()
