#!/usr/bin/env python3
"""Run all release verifiers and fail on the first nonzero exit status."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "code/verify_borsuk_ternary4.py",
    "code/verify_kissing_ternary5.py",
    "code/verify_kissing_ternary5_independent.py",
    "code/verify_known_kissing_constructions.py",
]


def main():
    for script in SCRIPTS:
        print(f"=== {script} ===", flush=True)
        subprocess.run([sys.executable, script], cwd=ROOT, check=True)
    print("ALL RELEASE VERIFIERS PASSED")


if __name__ == "__main__":
    main()
