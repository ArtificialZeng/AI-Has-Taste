#!/usr/bin/env python3
"""Report LaTeX citation keys against BibTeX files and optional aux bibcite keys."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CITE_RE = re.compile(
    r"\\(?:cite\w*|nocite)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^{}]*)\}",
    re.DOTALL,
)
BIB_RESOURCE_RE = re.compile(r"\\(?:bibliography|addbibresource)(?:\[[^\]]*\])?\s*\{([^{}]+)\}")
BIB_ENTRY_RE = re.compile(r"@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
AUX_BIBCITE_RE = re.compile(r"\\bibcite\{([^}]+)\}")


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        pos = None
        escaped = False
        for idx, char in enumerate(line):
            if char == "\\":
                escaped = not escaped
                continue
            if char == "%" and not escaped:
                pos = idx
                break
            escaped = False
        lines.append(line if pos is None else line[:pos])
    return "\n".join(lines)


def split_keys(raw: str) -> set[str]:
    return {part.strip() for part in raw.replace("\n", " ").split(",") if part.strip() and part.strip() != "*"}


def extract_cites(tex_path: Path) -> set[str]:
    text = strip_comments(tex_path.read_text(encoding="utf-8", errors="replace"))
    keys: set[str] = set()
    for match in CITE_RE.finditer(text):
        keys.update(split_keys(match.group(1)))
    return keys


def discover_bibs(tex_path: Path) -> list[Path]:
    text = strip_comments(tex_path.read_text(encoding="utf-8", errors="replace"))
    bibs: list[Path] = []
    for match in BIB_RESOURCE_RE.finditer(text):
        for item in split_keys(match.group(1)):
            path = Path(item)
            if path.suffix != ".bib":
                path = path.with_suffix(".bib")
            if not path.is_absolute():
                path = tex_path.parent / path
            bibs.append(path)
    seen: set[Path] = set()
    unique: list[Path] = []
    for bib in bibs:
        resolved = bib.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(bib)
    return unique


def extract_bib_keys(bib_paths: list[Path]) -> tuple[set[str], list[Path]]:
    keys: set[str] = set()
    missing_files: list[Path] = []
    for bib_path in bib_paths:
        if not bib_path.exists():
            missing_files.append(bib_path)
            continue
        text = bib_path.read_text(encoding="utf-8", errors="replace")
        keys.update(match.group(1).strip() for match in BIB_ENTRY_RE.finditer(text))
    return keys, missing_files


def extract_aux_bibcites(aux_path: Path) -> set[str]:
    if not aux_path.exists():
        return set()
    text = aux_path.read_text(encoding="utf-8", errors="replace")
    return {match.group(1).strip() for match in AUX_BIBCITE_RE.finditer(text)}


def print_list(label: str, values: set[str] | list[Path]) -> None:
    print(f"{label}: {len(values)}")
    for value in sorted(str(v) for v in values):
        print(f"  {value}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", type=Path, help="LaTeX root file to inspect")
    parser.add_argument("--bib", action="append", type=Path, help="Additional .bib file; may be repeated")
    parser.add_argument("--aux", type=Path, help="Optional .aux file from a completed build")
    args = parser.parse_args()

    tex_path = args.tex
    if not tex_path.exists():
        print(f"error: tex file not found: {tex_path}", file=sys.stderr)
        return 2

    cited = extract_cites(tex_path)
    bib_paths = discover_bibs(tex_path)
    if args.bib:
        bib_paths.extend(args.bib)
    bib_keys, missing_files = extract_bib_keys(bib_paths)

    print(f"tex: {tex_path}")
    print_list("bibliography_files", bib_paths)
    print(f"cited_keys: {len(cited)}")
    print(f"bib_keys: {len(bib_keys)}")
    print_list("missing_bib_files", missing_files)

    missing_in_bib = cited - bib_keys
    unused_in_bib = bib_keys - cited
    print_list("cited_keys_missing_from_bib", missing_in_bib)
    print_list("bib_keys_not_cited", unused_in_bib)

    aux_mismatch = False
    if args.aux:
        aux_keys = extract_aux_bibcites(args.aux)
        missing_in_aux = cited - aux_keys
        extra_in_aux = aux_keys - cited
        print(f"aux: {args.aux}")
        print(f"aux_bibcite_keys: {len(aux_keys)}")
        print_list("cited_keys_missing_from_aux", missing_in_aux)
        print_list("aux_keys_not_cited", extra_in_aux)
        aux_mismatch = bool(missing_in_aux or extra_in_aux)

    return 1 if missing_files or missing_in_bib or aux_mismatch else 0


if __name__ == "__main__":
    raise SystemExit(main())
