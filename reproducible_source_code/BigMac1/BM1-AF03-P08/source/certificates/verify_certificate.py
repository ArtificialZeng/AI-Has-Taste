#!/usr/bin/env python3
"""Compile and run the no-import exact n=10 verifier in a fresh directory."""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import platform
import subprocess
import tempfile


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=pathlib.Path,
        default=pathlib.Path(__file__).with_name("n10_finite_certificate.txt"),
    )
    args = parser.parse_args()
    certificate = args.certificate.resolve()
    source = pathlib.Path(__file__).with_name("verify_n10.cpp").resolve()
    if not certificate.is_file() or not source.is_file():
        raise SystemExit("certificate or verifier source is missing")

    with tempfile.TemporaryDirectory(prefix="kl-r-fib-verify-") as tmp:
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
                str(source),
                "-o",
                str(executable),
            ],
            check=True,
        )
        completed = subprocess.run(
            [str(executable), str(certificate)],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(completed.stdout, end="")
        if completed.returncode != 0:
            return completed.returncode

    print(f"SUCCESS certificate_sha256={sha256(certificate)}")
    print(f"SUCCESS verifier_source_sha256={sha256(source)}")
    print(f"SUCCESS python={platform.python_version()} platform={platform.platform()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
