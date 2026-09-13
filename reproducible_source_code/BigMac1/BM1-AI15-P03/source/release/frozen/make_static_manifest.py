#!/usr/bin/env python3
"""Create a deterministic manifest over exactly one static whitelist."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
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


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("whitelist", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    whitelist = args.whitelist.resolve()
    output = args.output.resolve()
    if not args.label.strip():
        fail("label must be nonempty")
    entries = read_whitelist(whitelist)
    files: dict[str, dict[str, int | str]] = {}
    for rel in entries:
        if forbidden(rel):
            fail(f"forbidden manifest entry: {rel}")
        source = root.joinpath(*PurePosixPath(rel).parts)
        if not source.is_file() or source.is_symlink():
            fail(f"whitelisted path is not a regular non-symlink file: {rel}")
        if source.resolve() == output:
            fail("manifest cannot list itself")
        files[rel] = {"bytes": source.stat().st_size, "sha256": digest(source)}
    whitelist_rel = whitelist.relative_to(root).as_posix()
    data = {
        "schema_version": 2,
        "label": args.label,
        "root_name": root.name,
        "whitelist": whitelist_rel,
        "whitelist_sha256": digest(whitelist),
        "files": files,
    }
    raw = (json.dumps(data, indent=2, sort_keys=True) + "\n").encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=output.name + ".", suffix=".tmp", dir=output.parent
    )
    os.close(handle)
    temporary = Path(temporary_name)
    try:
        temporary.write_bytes(raw)
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(
        json.dumps(
            {
                "status": "PASS",
                "entries": len(files),
                "output": output.relative_to(root).as_posix(),
                "sha256": hashlib.sha256(raw).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
