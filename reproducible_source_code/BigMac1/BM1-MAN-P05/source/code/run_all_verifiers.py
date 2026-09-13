#!/usr/bin/env python3
"""Regenerate the certificate and run both exact verifiers."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent


def run(name: str) -> None:
    subprocess.run([sys.executable, str(HERE / name)], cwd=HERE, check=True)


def main() -> None:
    run("generate_certificate.py")
    run("verify_certificate.py")
    run("verify_independent.py")
    print("all exact verifiers: PASS")


if __name__ == "__main__":
    main()
