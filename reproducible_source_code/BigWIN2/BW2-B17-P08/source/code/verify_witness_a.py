#!/usr/bin/env python3
"""Definition-level verifier for the 201-point Folkman finite-sums witness."""
from itertools import combinations
from pathlib import Path
import hashlib, json, platform, sys

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificate" / "f4_n201_coloring.txt"

def main() -> int:
    raw = CERT.read_bytes()
    bits = b"".join(raw.split()).decode("ascii")
    if len(bits) != 201 or set(bits) - {"0", "1"}:
        raise SystemExit("FAIL malformed certificate")
    colours = [-1] + [int(x) for x in bits]
    eligible = 0
    histogram = {}
    for A in combinations(range(1, 202), 4):
        if sum(A) > 201:
            continue
        eligible += 1
        sums = {sum(B) for r in range(1, 5) for B in combinations(A, r)}
        histogram[len(sums)] = histogram.get(len(sums), 0) + 1
        seen = {colours[s] for s in sums}
        if len(seen) == 1:
            raise SystemExit(f"FAIL monochromatic A={A}, sums={sorted(sums)}")
    record = {
        "status": "PASS", "N": 201, "k": 4, "eligible_sets": eligible,
        "edge_size_histogram": histogram,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0], "platform": platform.platform(),
    }
    print(json.dumps(record, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
