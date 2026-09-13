#!/usr/bin/env python3
"""Fail-closed verifier for the frozen static-whitelist manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
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
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    whitelist = args.whitelist.resolve()
    manifest = args.manifest.resolve()
    entries = read_whitelist(whitelist)
    try:
        data = json.loads(manifest.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"cannot parse manifest: {exc}")
    if not isinstance(data, dict) or set(data) != {
        "schema_version",
        "label",
        "root_name",
        "whitelist",
        "whitelist_sha256",
        "files",
    }:
        fail("manifest schema mismatch")
    if data["schema_version"] != 2 or not isinstance(data["label"], str) or not data["label"]:
        fail("manifest version or label mismatch")
    if data["root_name"] != root.name:
        fail("manifest root name mismatch")
    if data["whitelist"] != whitelist.relative_to(root).as_posix():
        fail("manifest whitelist path mismatch")
    if data["whitelist_sha256"] != digest(whitelist):
        fail("manifest whitelist hash mismatch")
    files = data["files"]
    if not isinstance(files, dict) or list(files) != entries:
        fail("manifest file set/order differs from the static whitelist")
    for rel in entries:
        if forbidden(rel):
            fail(f"forbidden manifest entry: {rel}")
        expected = files[rel]
        if not isinstance(expected, dict) or set(expected) != {"bytes", "sha256"}:
            fail(f"record schema mismatch: {rel}")
        path = root.joinpath(*PurePosixPath(rel).parts)
        if not path.is_file() or path.is_symlink():
            fail(f"missing or non-regular file: {rel}")
        if type(expected["bytes"]) is not int or expected["bytes"] != path.stat().st_size:
            fail(f"size mismatch: {rel}")
        if not isinstance(expected["sha256"], str) or expected["sha256"] != digest(path):
            fail(f"hash mismatch: {rel}")
    print(
        json.dumps(
            {
                "status": "PASS",
                "entries": len(entries),
                "whitelist_sha256": data["whitelist_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
