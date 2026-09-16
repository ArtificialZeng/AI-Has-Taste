#!/usr/bin/env python3
"""Independent verifier: nested bounded loops and iterative sumset expansion."""
from pathlib import Path
import hashlib, json, platform, sys

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificate" / "f4_n201_coloring.txt"

def main() -> int:
    raw = CERT.read_bytes()
    word = "".join(raw.decode("ascii").split())
    if len(word) != 201 or any(ch not in "01" for ch in word):
        raise SystemExit("FAIL malformed certificate")
    colour = tuple(map(int, word))
    eligible = 0
    histogram = {}
    for a in range(1, 201):
        for b in range(a + 1, 201):
            if a + b + (b + 1) + (b + 2) > 201:
                break
            for c in range(b + 1, 201):
                top = 201 - a - b - c
                if top <= c:
                    break
                for d in range(c + 1, top + 1):
                    eligible += 1
                    edge = {0}
                    for x in (a, b, c, d):
                        edge |= {s + x for s in tuple(edge)}
                    edge.remove(0)
                    histogram[len(edge)] = histogram.get(len(edge), 0) + 1
                    first = colour[next(iter(edge)) - 1]
                    if all(colour[s - 1] == first for s in edge):
                        raise SystemExit(f"FAIL monochromatic A={(a,b,c,d)}")
    out = {
        "status": "PASS", "N": 201, "k": 4, "eligible_sets": eligible,
        "edge_size_histogram": histogram,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0], "platform": platform.platform(),
    }
    print(json.dumps(out, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
