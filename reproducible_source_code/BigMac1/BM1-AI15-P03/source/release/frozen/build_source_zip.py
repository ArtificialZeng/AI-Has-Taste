#!/usr/bin/env python3
"""Build a deterministic source ZIP from an exact static whitelist."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


FORBIDDEN_PARTS = {
    ".git",
    ".lake",
    ".pytest_cache",
    ".venv",
    "__pycache__",
    "build",
    "logs",
    "tmp",
}
FORBIDDEN_NAMES = {".DS_Store"}
FORBIDDEN_SUFFIXES = {
    ".aux",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".pyc",
    ".pyo",
    ".synctex.gz",
    ".toc",
}


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def forbidden(rel: str) -> bool:
    path = PurePosixPath(rel)
    return (
        path.is_absolute()
        or ".." in path.parts
        or any(part in FORBIDDEN_PARTS for part in path.parts)
        or path.name in FORBIDDEN_NAMES
        or any(path.name.endswith(suffix) for suffix in FORBIDDEN_SUFFIXES)
    )


def read_whitelist(path: Path) -> list[str]:
    try:
        entries = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    except OSError as exc:
        fail(f"cannot read whitelist: {exc}")
    if not entries or any(not entry for entry in entries):
        fail("whitelist is empty or contains blank entries")
    if entries != sorted(entries) or len(entries) != len(set(entries)):
        fail("whitelist must be sorted and duplicate-free")
    bad = [entry for entry in entries if forbidden(entry)]
    if bad:
        fail(f"forbidden whitelist entries: {bad}")
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("whitelist", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    whitelist = args.whitelist.resolve()
    output = args.output.resolve()
    entries = read_whitelist(whitelist)
    sources: list[tuple[str, Path]] = []
    for rel in entries:
        source = root.joinpath(*PurePosixPath(rel).parts)
        if not source.is_file() or source.is_symlink():
            fail(f"whitelisted path is not a regular non-symlink file: {rel}")
        if source.resolve() == output:
            fail("output archive cannot list itself")
        sources.append((rel, source))
    output.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=output.name + ".", suffix=".tmp", dir=output.parent
    )
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(
            temporary,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            strict_timestamps=False,
        ) as archive:
            for rel, source in sources:
                info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(
                    info,
                    source.read_bytes(),
                    compress_type=zipfile.ZIP_DEFLATED,
                    compresslevel=9,
                )
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()
    raw = output.read_bytes()
    print(
        json.dumps(
            {
                "status": "PASS",
                "entries": len(entries),
                "output": output.relative_to(root).as_posix(),
                "sha256": digest(raw),
                "bytes": len(raw),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
