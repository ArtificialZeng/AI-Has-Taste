#!/usr/bin/env python3
"""Independent direct verifier for a proposed admissible integer set."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("witness", type=Path)
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--size", type=int, required=True)
    args = ap.parse_args()
    data = json.loads(args.witness.read_text(encoding="utf-8"))
    values = data["set"]
    assert len(values) == args.size and len(set(values)) == args.size
    assert all(type(x) is int and 1 <= x <= args.n for x in values)
    checked = 0
    for a, b, c in itertools.combinations(values, 3):
        checked += 1
        gs = (math.gcd(a, b), math.gcd(a, c), math.gcd(b, c))
        assert not (gs[0] == gs[1] == gs[2]), (a, b, c, gs)
    print(json.dumps({"status": "VERIFIED", "triples_checked": checked,
        "input_sha256": hashlib.sha256(args.witness.read_bytes()).hexdigest()},
        sort_keys=True))


if __name__ == "__main__":
    main()
