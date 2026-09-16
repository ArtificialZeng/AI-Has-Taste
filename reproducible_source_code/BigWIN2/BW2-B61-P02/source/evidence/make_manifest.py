#!/usr/bin/env python3
"""Create deterministic SHA-256 bindings for census inputs and every status row."""

import csv
import hashlib
import json
import sys
from pathlib import Path


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: make_manifest.py census_exact.tsv")
    census_path = Path(sys.argv[1])
    with census_path.open(newline="", encoding="ascii") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    row_bindings = []
    aggregate = hashlib.sha256()
    for row in rows:
        hall = bytes.fromhex(row["hall_bits_hex"])
        colorable = bytes.fromhex(row["colorable_bits_hex"])
        payload = (
            f'{row["n"]}\0{row["graph6"]}\0{row["g_edge_mask"]}\0{row["num_H"]}\0'.encode("ascii")
            + hall + b"\0" + colorable
        )
        status_sha256 = hashlib.sha256(payload).hexdigest()
        aggregate.update(bytes.fromhex(status_sha256))
        row_bindings.append({
            "n": int(row["n"]),
            "graph6": row["graph6"],
            "g_edge_mask": int(row["g_edge_mask"]),
            "num_H": int(row["num_H"]),
            "status_sha256": status_sha256,
        })
    manifest = {
        "format": "exact-census-v1; H masks increasing; status bits little-endian within each byte",
        "census_sha256": digest(census_path),
        "representatives_sha256": digest("evidence/representatives.tsv"),
        "enumerator_sha256": digest("evidence/census_numba.py"),
        "canonicalizer_sha256": digest("evidence/generate_reps.py"),
        "classification_sha256": digest("evidence/census_classification.tsv"),
        "classifier_sha256": digest("evidence/classify_source_families.py"),
        "primary_source_pdf_sha256": digest("evidence/external/2609.01889.pdf"),
        "primary_source_text_sha256": digest("evidence/external/2609.01889.txt"),
        "aggregate_status_sha256": aggregate.hexdigest(),
        "rows": row_bindings,
    }
    json.dump(manifest, sys.stdout, indent=2, sort_keys=True)
    print()


if __name__ == "__main__":
    main()
