#!/usr/bin/env python3
"""Bind a raw finite-search result to its exact trace and discovery source."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True, type=Path)
    parser.add_argument("--trace", required=True, type=Path)
    parser.add_argument("--discovery-source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    raw = json.loads(args.raw.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or "artifacts" in raw:
        raise SystemExit("raw result must be an unsealed JSON object")
    expected_bytes = raw.get("counts", {}).get("trace_bytes")
    if type(expected_bytes) is not int or args.trace.stat().st_size != expected_bytes:
        raise SystemExit("trace size does not match raw result")
    raw["artifacts"] = {
        "trace_file": args.trace.name,
        "trace_sha256": sha256(args.trace),
        "discovery_source": args.discovery_source.name,
        "discovery_source_sha256": sha256(args.discovery_source),
        "sealer_source": Path(__file__).name,
        "sealer_source_sha256": sha256(Path(__file__)),
        "python": platform.python_version(),
    }
    args.output.write_text(
        json.dumps(raw, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"SEALED_OK output={args.output} sha256={sha256(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
