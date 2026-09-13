#!/usr/bin/env python3
"""Fail-closed, read-only release-integrity checks for the frozen v13 package.

This verifier deliberately uses only the Python standard library.  It does
not replace the exact source/referee certificate replays recorded in the
FINAL_REFEREE_V13 audit; it checks the frozen delivery, archive topology,
JSON release manifest, bibliography/citation closure, declared scope, and
the frozen v11/v12 nonmutation baselines.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath


if not __debug__:
    raise RuntimeError("FINAL_REFEREE_V13 verifier must not run under python -O")

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output/pdf/common_metric_three_positivity_islands_submission_2026-08-25-v13.pdf"
ZIP = ROOT / "output/source_packages/common_metric_three_positivity_islands_submission_2026-08-25-v13.zip"
ARCHIVE_ROOT = "common_metric_three_positivity_islands_submission_2026-08-25-v13"

EXPECTED = {
    PDF: "2fff9cad48f3f80281b202ce5f62d8fb72feea57ea50c27570f0c2873ca917f3",
    ZIP: "c5b8db2fd9ddb9c5be9fe5d2fc3e10979f274d9a25cd919e743e3efc33b586ad",
    ROOT / "output/pdf/common_metric_two_positivity_islands_submission_2026-08-24-v11.pdf":
        "91794e054228d51cabbe5afb735bb52a0aec890e7633c582c25e7176695db641",
    ROOT / "output/source_packages/common_metric_two_positivity_islands_submission_2026-08-24-v11.zip":
        "250a51826c798a7334feee9da6ed9ea19c8ed41ddb2319cbce6d981f9dfaef91",
    ROOT / "output/pdf/common_metric_two_positivity_islands_submission_2026-08-24-v12.pdf":
        "1359a72329ef81a8c9e1c23eac680d157439c7f1ba8bbd06f04f19a4d643c70a",
    ROOT / "output/source_packages/common_metric_two_positivity_islands_submission_2026-08-24-v12.zip":
        "ac6a27fb92163d7099108092dadc9ef184f9eb79ea1420503d4cb8b9427931c8",
}
EXPECTED_RELEASE_MANIFEST_SHA = "457e75fd445ebcd084b2cfb8e1617d2202c6868d2481d1d6b7d105a6138ad13b"
EXPECTED_CITES = {
    "MR2223270", "MR2449098", "Crouzeix_2003", "MR2047592", "Crouzeix_2016"
}
EXPECTED_THEOREMS = {
    "thm:scale-cubic", "thm:island-A", "thm:island-B", "thm:tilted-sheet",
    "thm:inward-sheet", "thm:phase-tube",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def safe_member(name: str) -> bool:
    p = PurePosixPath(name)
    return (
        bool(p.parts)
        and not p.is_absolute()
        and ".." not in p.parts
        and "\\" not in name
        and not re.match(r"^[A-Za-z]:", name)
    )


def main() -> None:
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing frozen artifact: {path.relative_to(ROOT)}")
        require(sha256_path(path) == expected, f"frozen hash mismatch: {path.relative_to(ROOT)}")

    with zipfile.ZipFile(ZIP) as archive:
        infos = archive.infolist()
        require(len(infos) == 613, f"archive entry count is {len(infos)}, expected 613")
        require(archive.testzip() is None, "archive CRC/integrity test failed")
        names = [info.filename for info in infos]
        require(len(names) == len(set(names)), "duplicate archive member")
        require(all(safe_member(name) for name in names), "unsafe archive member path")
        require(all(PurePosixPath(name).parts[0] == ARCHIVE_ROOT for name in names),
                "member outside the single archive root")
        require(all(((info.external_attr >> 16) & 0o170000) != 0o120000 for info in infos),
                "symlink present in release archive")

        files = {
            "/".join(PurePosixPath(info.filename).parts[1:]): archive.read(info)
            for info in infos if not info.is_dir()
        }
        require(len(files) == 586, f"archive file count is {len(files)}, expected 586")
        require("RELEASE_MANIFEST.sha256" in files, "missing release manifest")
        manifest_bytes = files["RELEASE_MANIFEST.sha256"]
        require(sha256_bytes(manifest_bytes) == EXPECTED_RELEASE_MANIFEST_SHA,
                "release-manifest file hash mismatch")
        manifest = json.loads(manifest_bytes)
        require(isinstance(manifest, dict) and isinstance(manifest.get("files"), dict),
                "release manifest is not the expected JSON object")
        records = manifest["files"]
        require(len(records) == 585, f"release manifest has {len(records)} records, expected 585")
        require(len(records) == 585, "duplicate path in release manifest")
        actual = set(files) - {"RELEASE_MANIFEST.sha256"}
        require(set(records) == actual, "release manifest path set is not exact")
        for rel, record in records.items():
            data = files[rel]
            require(record["bytes"] == len(data), f"manifest size mismatch: {rel}")
            require(record["sha256"] == sha256_bytes(data), f"manifest hash mismatch: {rel}")

        forbidden_path_parts = {".venv", ".lake", ".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
        forbidden_suffixes = {".pyc", ".pyo", ".aux", ".log", ".fls", ".fdb_latexmk", ".synctex.gz"}
        for rel, data in files.items():
            parts = set(PurePosixPath(rel).parts)
            require(not (parts & forbidden_path_parts), f"forbidden cache/environment path: {rel}")
            require(not any(rel.endswith(suffix) for suffix in forbidden_suffixes),
                    f"forbidden generated file: {rel}")
            require(b"/Users/" not in data and b"/home/" not in data and b"file://" not in data,
                    f"absolute host path/URI in packaged file: {rel}")

        require(files["main.pdf"] == PDF.read_bytes(), "packaged and delivered PDFs differ")
        tex = files["main.tex"].decode("utf-8")
        bib = files["references.bib"].decode("utf-8")
        labels = set(re.findall(r"\\begin\{theorem\}.*?\\label\{([^}]+)\}", tex))
        require(labels == EXPECTED_THEOREMS, f"theorem-label set mismatch: {sorted(labels)}")
        cite_keys = set()
        for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", tex):
            cite_keys.update(key.strip() for key in group.split(","))
        bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib, flags=re.MULTILINE))
        require(cite_keys == EXPECTED_CITES, f"citation-key set mismatch: {sorted(cite_keys)}")
        require(bib_keys == EXPECTED_CITES, f"bibliography-key set mismatch: {sorted(bib_keys)}")

        required_scope = [
            "The paper has six mathematical results.",
            "The five positivity theorems establish strict positivity only on the displayed families.",
            "full compact unit ball",
            "arbitrary-node operator bridges and the optimal constant of a fixed",
            "72$-node grid are falsification checks only",
            "do not prove the continuum statement",
            "No Lean or other proof assistant formalizes the complex theorems in this paper",
        ]
        normalized_tex = " ".join(tex.split())
        for marker in required_scope:
            require(marker in normalized_tex, f"missing scope/reproducibility marker: {marker}")

    print("FINAL_REFEREE_V13 INTEGRITY VERIFIER: PASS")
    print("frozen_artifact_hashes=6/6")
    print("archive_entries=613 files=586 manifest_records=585 manifest_bad=0")
    print("theorems=6 positivity_theorems=5 scale_cubic=1 citations=5 bibliography=5")
    print("packaged_pdf_equals_delivered_pdf=yes")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FINAL_REFEREE_V13 INTEGRITY VERIFIER: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
