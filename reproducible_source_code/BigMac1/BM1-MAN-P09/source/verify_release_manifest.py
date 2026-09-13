#!/usr/bin/env python3
"""Verify the v18 candidate tree and, optionally, its release ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from pathlib import PurePosixPath
import stat
import zipfile


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "RELEASE_MANIFEST.sha256"
RELEASE_ID = "common_metric_three_positivity_islands_submission_2026-08-26-v18"
TRANSIENT_BUILD_FILES = {"main.fdb_latexmk", "main.fls", "main.log"}
NONPORTABLE_BYTE_PATTERNS = (
    b"/" + b"Users/" + b"mac",
    b"/" + b"home/" + b"oai/share",
    b"Documents" + b"/ChatGPT/" + b"math",
)


def safe_relative(name: str) -> bool:
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts


def require_portable_bytes(label: str, payload: bytes) -> None:
    if any(pattern in payload for pattern in NONPORTABLE_BYTE_PATTERNS):
        raise SystemExit(f"FAIL: machine-specific workspace bytes {label}")


def require_case_unique(names: set[str]) -> None:
    folded: dict[str, str] = {}
    for name in sorted(names):
        key = name.casefold()
        if key in folded and folded[key] != name:
            raise SystemExit(f"FAIL: case-colliding paths {folded[key]} and {name}")
        folded[key] = name


def load_records() -> dict[str, dict[str, object]]:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("release_id") != RELEASE_ID:
        raise SystemExit(f"FAIL: release_id mismatch {data.get('release_id')!r}")
    records = data.get("files")
    if not isinstance(records, dict):
        raise SystemExit("FAIL: manifest has no files object")
    if os.environ.get("V18_VERIFY_PATH_ESCAPE") == "1":
        records["../escape"] = {"bytes": 0, "sha256": "0" * 64}
    if os.environ.get("V18_VERIFY_CASE_COLLISION") == "1":
        records["readme.md"] = dict(records["README.md"])
    for relative in records:
        if not safe_relative(relative):
            raise SystemExit(f"FAIL: unsafe manifest path {relative}")
        parts = PurePosixPath(relative).parts
        if any(part in {".venv", ".lake", "__pycache__"} for part in parts) or relative.endswith(".pyc"):
            raise SystemExit(f"FAIL: cache path in manifest {relative}")
    require_case_unique(set(records))
    return records


def verify_tree(records: dict[str, dict[str, object]]) -> None:
    actual = set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == MANIFEST:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative in TRANSIENT_BUILD_FILES:
            continue
        if path.is_symlink():
            raise SystemExit(f"FAIL: symlink in release tree {relative}")
        if not safe_relative(relative):
            raise SystemExit(f"FAIL: unsafe tree path {relative}")
        parts = PurePosixPath(relative).parts
        if any(part in {".venv", ".lake", "__pycache__"} for part in parts) or relative.endswith(".pyc"):
            raise SystemExit(f"FAIL: cache path in release tree {relative}")
        actual.add(relative)
    if os.environ.get("V18_VERIFY_DROP_FILE") == "1":
        actual.discard("main.tex")
    expected = set(records)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise SystemExit(f"FAIL: file-set mismatch missing={missing} extra={extra}")
    for relative, record in sorted(records.items()):
        path = ROOT / relative
        payload = path.read_bytes()
        require_portable_bytes(relative, payload)
        digest = hashlib.sha256(payload).hexdigest()
        if os.environ.get("V18_VERIFY_BAD_HASH") == "1" and relative == "main.tex":
            digest = "0" * 64
        if digest != record.get("sha256") or len(payload) != record.get("bytes"):
            raise SystemExit(f"FAIL: record mismatch {relative}")
    print(f"PASS JSON release manifest: {len(records)}/{len(records)} records")


def verify_zip(zip_path: Path, records: dict[str, dict[str, object]]) -> None:
    prefix = f"{RELEASE_ID}/"
    expected = {prefix + relative for relative in records}
    expected.add(prefix + MANIFEST.name)
    with zipfile.ZipFile(zip_path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            raise SystemExit("FAIL: duplicate ZIP entry")
        for info in infos:
            name = info.filename
            if not name.startswith(prefix) or not safe_relative(name):
                raise SystemExit(f"FAIL: unsafe ZIP entry {name}")
            if stat.S_ISLNK((info.external_attr >> 16) & 0xFFFF):
                raise SystemExit(f"FAIL: symlink ZIP entry {name}")
            relative = name[len(prefix):]
            parts = PurePosixPath(relative).parts
            if any(part in {".venv", ".lake", "__pycache__"} for part in parts) or relative.endswith(".pyc"):
                raise SystemExit(f"FAIL: cache ZIP entry {name}")
        if set(names) != expected:
            raise SystemExit(
                f"FAIL: ZIP coverage mismatch missing={sorted(expected-set(names))[:8]} "
                f"extra={sorted(set(names)-expected)[:8]}"
            )
        for relative, record in sorted(records.items()):
            payload = archive.read(prefix + relative)
            require_portable_bytes(f"ZIP:{relative}", payload)
            digest = hashlib.sha256(payload).hexdigest()
            if digest != record.get("sha256") or len(payload) != record.get("bytes"):
                raise SystemExit(f"FAIL: ZIP record mismatch {relative}")
        if archive.read(prefix + MANIFEST.name) != MANIFEST.read_bytes():
            raise SystemExit("FAIL: ZIP manifest bytes differ from candidate tree")
    print(f"PASS safe ZIP: {len(expected)}/{len(expected)} exact entries under {RELEASE_ID}/")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", type=Path)
    args = parser.parse_args()
    records = load_records()
    verify_tree(records)
    if args.zip is not None:
        verify_zip(args.zip.resolve(), records)


if __name__ == "__main__":
    main()
