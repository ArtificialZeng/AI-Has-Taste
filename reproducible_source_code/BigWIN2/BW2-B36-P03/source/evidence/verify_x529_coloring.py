#!/usr/bin/env python3
"""Small, dependency-free verifier for x529-coloring-certificate.json."""

import hashlib
import itertools
import json
import math
import pathlib
import sys


def fail(message):
    raise AssertionError(message)


def main():
    path = pathlib.Path(sys.argv[1] if len(sys.argv) == 2 else
                        "evidence/x529-coloring-certificate.json")
    document = json.loads(path.read_text())
    payload = document["payload"]
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(canonical).hexdigest() != document["payload_sha256"]:
        fail("payload SHA-256 does not match")
    if (payload["format"], payload["x"], payload["target_columns_excluded"]) != (
        "win36-x529-compatibility-coloring-v1", 529, 42
    ):
        fail("wrong certificate header")

    records = payload["even_gaps"]
    if [r["d"] for r in records] != list(range(2, 527, 2)):
        fail("the 263 admissible even gaps are not covered exactly")

    same_color_pairs_checked = 0
    for record in records:
        d = record["d"]
        expected = [v for v in range(2, 530 - d) if math.gcd(v, v + d) == 1]
        if record["vertices"] != expected:
            fail(f"d={d}: incomplete or incorrect vertex set")
        colors = record["colors"]
        if len(colors) != len(expected) or any(type(c) is not int or c < 0 for c in colors):
            fail(f"d={d}: malformed colors")
        if len(set(colors)) > 41:
            fail(f"d={d}: more than 41 colors")

        for i, j in itertools.combinations(range(len(expected)), 2):
            if colors[i] != colors[j]:
                continue
            same_color_pairs_checked += 1
            v, w = expected[i], expected[j]
            four = (v, v + d, w, w + d)
            adjacent = len(set(four)) == 4 and all(
                math.gcd(a, b) == 1 for a, b in itertools.combinations(four, 2)
            )
            if adjacent:
                fail(f"d={d}: adjacent vertices {v},{w} have the same color")

    print(json.dumps({
        "verified": True,
        "gaps_checked": len(records),
        "same_color_pairs_checked": same_color_pairs_checked,
        "certificate_payload_sha256": document["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
