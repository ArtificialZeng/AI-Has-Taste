#!/usr/bin/env python3
"""One-command entry point for the independent exact verification."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    subprocess.run(
        [
            "python3",
            str(ROOT / "code" / "verify_mordell_certificate.py"),
            "--certificate", str(ROOT / "certificate" / "mordell_filter_certificate.json"),
            "--pocklington", str(ROOT / "certificate" / "incumbent_pocklington.json"),
            "--negative-pdf", str(ROOT / "data" / "upstream" / "mordell_negative_0_1e6.pdf"),
            "--positive-pdf", str(ROOT / "data" / "upstream" / "mordell_positive_0_1e6.pdf"),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
