#!/usr/bin/env python3
"""Independent exact evaluator for a literal JSON witness."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("witness")
    ap.add_argument("--n", type=int, default=38)
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--minimum", type=int)
    args = ap.parse_args()
    path = Path(args.witness)
    raw = path.read_bytes()
    data = json.loads(raw)
    A = data["set"]
    if not isinstance(A, list) or any(type(a) is not int for a in A):
        raise SystemExit("FAIL: set must be a list of integers")
    if A != sorted(set(A)) or len(A) != args.k:
        raise SystemExit("FAIL: set is not a sorted k-subset")
    if not all(1 <= a <= args.n for a in A):
        raise SystemExit("FAIL: element outside [1,n]")
    sums = set()
    multiplicities = {}
    for i, a in enumerate(A):
        for b in A[i:]:
            s = a + b
            sums.add(s)
            multiplicities[s] = multiplicities.get(s, 0) + 1
    if args.minimum is not None and len(sums) < args.minimum:
        raise SystemExit(f"FAIL: objective {len(sums)} < {args.minimum}")
    print(json.dumps({
        "status": "PASS",
        "n": args.n,
        "k": args.k,
        "set": A,
        "objective": len(sums),
        "sums": sorted(sums),
        "collision_excess": args.k * (args.k + 1) // 2 - len(sums),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
