#!/usr/bin/env python3
"""Exhaustive prime-factor search for a_22 over a bounded interval."""
import argparse
import numpy as np


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("limit", type=int)
    ap.add_argument("--start", type=int, default=2)
    args = ap.parse_args()
    limit = args.limit
    start = args.start
    if not 2 <= start <= limit <= 3_000_000_000:
        raise SystemExit("limit must be in [2, 3000000000]")

    # Segmented Eratosthenes sieve: base primes through sqrt(limit) mark every
    # composite in [start, limit], so exactly the unmarked integers are prime.
    root = int(limit**0.5)
    base_mask = np.ones(root + 1, dtype=np.bool_)
    base_mask[:2] = False
    for p in range(2, int(root**0.5) + 1):
        if base_mask[p]:
            base_mask[p * p :: p] = False
    base_primes = np.flatnonzero(base_mask)
    prime = np.ones(limit - start + 1, dtype=np.bool_)
    for p0 in base_primes:
        p = int(p0)
        first = max(p * p, ((start + p - 1) // p) * p)
        if first <= limit:
            prime[first - start :: p] = False
    ps = (np.flatnonzero(prime) + start).astype(np.int64)
    # If p | a_22 then a_21^2 == -2 (mod p), hence (-2|p)=1 and an odd
    # candidate has p == 1 or 3 (mod 8).  This is only a lossless filter.
    candidates = ps[(ps != 2) & ((ps % 8 == 1) | (ps % 8 == 3))]
    r = np.ones(candidates.size, dtype=np.int64)
    for _ in range(22):
        r = (r * r + 2) % candidates
    hits = candidates[r == 0]
    print(f"interval {start} {limit}")
    print(f"prime_count {ps.size}")
    print(f"admissible_prime_count {candidates.size}")
    if hits.size == 0:
        print("hits none")
        return 1
    for q0 in hits:
        q = int(q0)
        residues = [1]
        for _ in range(22):
            residues.append((residues[-1] * residues[-1] + 2) % q)
        print(f"factor {q}")
        print("residues " + " ".join(map(str, residues)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
