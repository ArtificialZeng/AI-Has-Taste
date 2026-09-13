#!/usr/bin/env python3
"""Cross-check constructed classes against the complete DesignTheory.org file."""

from __future__ import annotations

import argparse
import bz2
import hashlib
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from discover_graph import LABELG, canonicalize_many, pasch_configurations, validate_sts

DEFAULT_URL = (
    "https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/"
    "database/t-designs/t2-v15-b35-r7-k3-L1.icgsa.txt.bz2"
)
EXPECTED_SHA256 = "11310c7e35330e842938dbcc4bb6e59144bf40576323f22499a809364d50f2c9"


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def parse_catalog(compressed):
    xml_bytes = bz2.decompress(compressed)
    root = ET.fromstring(xml_bytes)
    designs = []
    source_ids = []
    for design in (node for node in root.iter() if local_name(node.tag) == "block_design"):
        blocks_parent = next(
            node for node in design if local_name(node.tag) == "blocks"
        )
        blocks = []
        for block in blocks_parent:
            if local_name(block.tag) != "block":
                continue
            values = [
                int(node.text)
                for node in block
                if local_name(node.tag) == "z"
            ]
            blocks.append(tuple(values))
        designs.append(validate_sts(blocks))
        source_ids.append(design.attrib["id"])
    return root.attrib, source_ids, designs, xml_bytes


def write_json(path, value):
    with open(path, "w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--representatives", default="certificate/representatives.json")
    parser.add_argument("--output", default="certificate/catalog_crosscheck.json")
    parser.add_argument("--labelg", default=LABELG)
    args = parser.parse_args()

    with urllib.request.urlopen(args.url, timeout=60) as response:
        compressed = response.read()
    compressed_sha256 = hashlib.sha256(compressed).hexdigest()
    if compressed_sha256 != EXPECTED_SHA256:
        raise SystemExit(
            f"catalog SHA-256 changed: {compressed_sha256}, expected {EXPECTED_SHA256}"
        )
    root_attributes, source_ids, designs, xml_bytes = parse_catalog(compressed)
    if root_attributes.get("no_designs") != "80":
        raise SystemExit("catalog does not assert no_designs=80")
    if root_attributes.get("pairwise_nonisomorphic") != "true":
        raise SystemExit("catalog does not assert pairwise_nonisomorphic=true")
    if len(designs) != 80:
        raise SystemExit(f"parsed {len(designs)} designs, expected 80")

    catalog_records = canonicalize_many(designs, args.labelg)
    if len(set(catalog_records)) != 80:
        raise SystemExit("catalog canonicalization did not give 80 distinct classes")
    with open(args.representatives, encoding="utf-8") as stream:
        released = json.load(stream)
    released_by_record = {
        vertex["canonical_graph6"]: vertex["id"]
        for vertex in released["vertices"]
    }
    if set(catalog_records) != set(released_by_record):
        missing = sorted(set(catalog_records) - set(released_by_record))
        extra = sorted(set(released_by_record) - set(catalog_records))
        raise SystemExit(
            f"catalog mismatch: {len(missing)} missing and {len(extra)} extra classes"
        )

    mapping = []
    for source_id, blocks, record in zip(source_ids, designs, catalog_records):
        mapping.append(
            {
                "catalog_id": source_id,
                "released_id": released_by_record[record],
                "pasch_count": len(pasch_configurations(blocks)),
            }
        )
    result = {
        "schema": "sts15-catalog-crosscheck-v1",
        "source_url": args.url,
        "compressed_sha256": compressed_sha256,
        "decompressed_sha256": hashlib.sha256(xml_bytes).hexdigest(),
        "root_attributes": root_attributes,
        "parsed_design_count": len(designs),
        "distinct_canonical_class_count": len(set(catalog_records)),
        "released_class_count": len(released_by_record),
        "canonical_sets_equal": True,
        "catalog_to_released": mapping,
    }
    write_json(Path(args.output), result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
