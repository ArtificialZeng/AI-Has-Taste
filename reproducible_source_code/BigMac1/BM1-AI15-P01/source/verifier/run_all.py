#!/usr/bin/env python3
"""Run the exact certificate checks from stable project-relative paths."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(*relative_args: str) -> None:
    command = [sys.executable, *relative_args]
    print("RUN", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true", help="run the shortest human-readable certificate only")
    args = parser.parse_args()

    run(
        "certificates/builder_verify_counterexample.py",
        "certificates/builder_counterexample.json",
    )
    if not args.fast:
        run("verifier/verify_rational_decomposition.py")
        run("discovery/breaker_projective_reconstruct.py")
        run("certificates/breaker_verify.py", "certificates/breaker_decomposition.json")
    print("ALL_PASS")


if __name__ == "__main__":
    main()
