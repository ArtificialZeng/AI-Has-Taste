#!/usr/bin/env python3
"""Create the deterministic v18-candidate manifest, PDF copy, and ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "RELEASE_MANIFEST.sha256"
RELEASE_ID = "common_metric_three_positivity_islands_submission_2026-08-26-v18"
CREATED_UTC = "2026-08-26T00:00:00+00:00"
ZIP_TIME = (2026, 8, 26, 0, 0, 0)
TRANSIENT_BUILD_FILES = {"main.fdb_latexmk", "main.fls", "main.log"}
NONPORTABLE_BYTE_PATTERNS = (
    b"/" + b"Users/" + b"mac",
    b"/" + b"home/" + b"oai/share",
    b"Documents" + b"/ChatGPT/" + b"math",
)


def require_portable_bytes(path: Path, payload: bytes) -> None:
    if any(pattern in payload for pattern in NONPORTABLE_BYTE_PATTERNS):
        raise SystemExit(f"machine-specific workspace bytes forbidden: {path}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_manifest() -> None:
    files = {}
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and p != MANIFEST):
        relative = path.relative_to(ROOT)
        if relative.as_posix() in TRANSIENT_BUILD_FILES:
            continue
        if path.is_symlink():
            raise SystemExit(f"symlink forbidden in release tree: {relative}")
        if any(part in {".venv", ".lake", "__pycache__"} for part in relative.parts):
            raise SystemExit(f"cache directory forbidden in release tree: {relative}")
        if path.suffix == ".pyc":
            raise SystemExit(f"compiled cache forbidden in release tree: {relative}")
        payload = path.read_bytes()
        require_portable_bytes(relative, payload)
        files[relative.as_posix()] = {
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }
    payload = {"release_id": RELEASE_ID, "created_utc": CREATED_UTC, "files": files}
    MANIFEST.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def write_zip(target: Path) -> None:
    if target.exists():
        raise SystemExit(f"refusing to overwrite existing target: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(
        p
        for p in ROOT.rglob("*")
        if p.is_file() and p.relative_to(ROOT).as_posix() not in TRANSIENT_BUILD_FILES
    )
    with zipfile.ZipFile(
        target, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"{RELEASE_ID}/{relative}", date_time=ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
            info.create_system = 3
            archive.writestr(
                info,
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "zip_target",
        type=Path,
        help=f"external target for {RELEASE_ID}.zip",
    )
    parser.add_argument("--pdf-copy", type=Path)
    args = parser.parse_args()
    write_manifest()
    write_zip(args.zip_target.resolve())
    if args.pdf_copy is not None:
        pdf_target = args.pdf_copy.resolve()
        if pdf_target.exists():
            raise SystemExit(f"refusing to overwrite existing target: {pdf_target}")
        pdf_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "main.pdf", pdf_target)


if __name__ == "__main__":
    main()
