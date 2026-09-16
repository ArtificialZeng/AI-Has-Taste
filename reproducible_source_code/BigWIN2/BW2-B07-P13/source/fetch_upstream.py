#!/usr/bin/env python3
"""Fetch the two author-hosted Mordell table PDFs and verify their identities."""

from __future__ import annotations

import hashlib
import os
import tempfile
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGET_DIR = ROOT / "data" / "upstream"
FILES = {
    "mordell_negative_0_1e6.pdf": (
        "https://personal.math.ubc.ca/~bennett/0-10%5E6.pdf",
        "5ad1afe4b3f64fbebfc8939e297782392c0b04d544d51d2a50f97732b44ab903",
    ),
    "mordell_positive_0_1e6.pdf": (
        "https://personal.math.ubc.ca/~bennett/0-10%5E6n.pdf",
        "5ee7772c7a1f7dfbc468fd6a5333f49bce69817f994d784324197b9fab68b235",
    ),
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def fetch(name: str, url: str, expected: str) -> None:
    destination = TARGET_DIR / name
    if destination.exists():
        actual = digest(destination)
        if actual != expected:
            raise ValueError(f"existing file has wrong digest: {destination}")
        print(f"VERIFIED existing {name}")
        return
    with tempfile.NamedTemporaryFile(dir=TARGET_DIR, delete=False) as stream:
        temporary = Path(stream.name)
        with urllib.request.urlopen(url) as response:
            while block := response.read(1 << 20):
                stream.write(block)
    try:
        actual = digest(temporary)
        if actual != expected:
            raise ValueError(f"downloaded file has wrong digest: {name}")
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(f"FETCHED and verified {name}")


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    for name, (url, expected) in FILES.items():
        fetch(name, url, expected)


if __name__ == "__main__":
    main()
