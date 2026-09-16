#!/usr/bin/env python3
"""Exact A114216 replay, path A: NumPy odd-only segmented sieve.

This implementation has no code in common with path_b_numba.py.  It constructs
base primes by a dense Eratosthenes sieve, sieves only odd candidates in NumPy
slices, and replays each extracted prime chunk in a separately compiled loop.
All recurrence arithmetic is uint64 with an explicit overflow check.
"""

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
from numba import njit


FNV_OFFSET = 14695981039346656037
FNV_PRIME = 1099511628211
U64_MAX = (1 << 64) - 1


def dense_base_primes(limit: int) -> np.ndarray:
    """Return every prime <= limit by a dense, full-integer sieve."""
    is_prime = np.ones(limit + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p :: p] = False
    return np.flatnonzero(is_prime).astype(np.uint64)


@njit(cache=True)
def fnv_word(h, word):
    """FNV-1a update with one uint64 encoded little-endian."""
    w = np.uint64(word)
    for _ in range(8):
        h ^= w & np.uint64(255)
        h *= np.uint64(FNV_PRIME)
        w >>= np.uint64(8)
    return h


@njit(cache=True)
def replay_chunk(primes, index, state, digest, checkpoint_step):
    size = primes.size
    hit_n = np.empty(size, dtype=np.uint64)
    hit_p = np.empty(size, dtype=np.uint64)
    hit_prev = np.empty(size, dtype=np.uint64)
    hit_total = np.empty(size, dtype=np.uint64)
    hit_exp = np.empty(size, dtype=np.uint8)
    cp_n = np.empty(size, dtype=np.uint64)
    cp_p = np.empty(size, dtype=np.uint64)
    cp_a = np.empty(size, dtype=np.uint64)
    cp_digest = np.empty(size, dtype=np.uint64)
    nh = 0
    nc = 0
    max_a = state
    for j in range(size):
        p = np.uint64(primes[j])
        prev = state
        total = prev + p
        if total < prev:  # exact guard against uint64 wraparound
            raise OverflowError("uint64 recurrence overflow")
        lowbit = total & (np.uint64(0) - total)
        state = total // lowbit
        index += 1
        digest = fnv_word(digest, index)
        digest = fnv_word(digest, p)
        digest = fnv_word(digest, state)
        if state > max_a:
            max_a = state
        if state == 1:
            hit_n[nh] = index
            hit_p[nh] = p
            hit_prev[nh] = prev
            hit_total[nh] = total
            exponent = 0
            t = total
            while t > 1:
                t >>= np.uint64(1)
                exponent += 1
            hit_exp[nh] = exponent
            nh += 1
        if index % checkpoint_step == 0:
            cp_n[nc] = index
            cp_p[nc] = p
            cp_a[nc] = state
            cp_digest[nc] = digest
            nc += 1
    return (
        index,
        state,
        digest,
        max_a,
        hit_n[:nh],
        hit_p[:nh],
        hit_prev[:nh],
        hit_total[:nh],
        hit_exp[:nh],
        cp_n[:nc],
        cp_p[:nc],
        cp_a[:nc],
        cp_digest[:nc],
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=100_000_000)
    ap.add_argument("--upper", type=int, default=2_100_000_000)
    ap.add_argument("--segment-odds", type=int, default=4_194_304)
    ap.add_argument("--checkpoint-step", type=int, default=1_000_000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if not (1 <= args.target <= 100_000_000):
        raise ValueError("target outside implemented certificate range")

    started = time.monotonic()
    bases = dense_base_primes(math.isqrt(args.upper - 1))
    index = 0
    state = np.uint64(0)
    digest = np.uint64(FNV_OFFSET)
    overall_max = 0
    hits = []
    checkpoints = []

    # Handle 2 separately; every later segment contains odd integers only.
    pending = [np.array([2], dtype=np.uint64)]
    low = 3
    while index < args.target:
        if pending:
            primes = pending.pop()
        else:
            high = min(args.upper, low + 2 * args.segment_odds)
            if high <= low:
                raise RuntimeError("upper bound contains too few primes")
            count = (high - low + 1) // 2
            flags = np.ones(count, dtype=np.bool_)
            last = low + 2 * (count - 1)
            for p64 in bases[1:]:
                p = int(p64)
                if p * p > last:
                    break
                start = max(p * p, ((low + p - 1) // p) * p)
                if start % 2 == 0:
                    start += p
                flags[(start - low) // 2 :: p] = False
            primes = (low + 2 * np.flatnonzero(flags)).astype(np.uint64)
            low = last + 2
        need = args.target - index
        if primes.size > need:
            primes = primes[:need]
        result = replay_chunk(
            primes,
            np.uint64(index),
            state,
            digest,
            np.uint64(args.checkpoint_step),
        )
        index, state, digest, chunk_max = map(int, result[:4])
        overall_max = max(overall_max, chunk_max)
        for values in zip(*(x.tolist() for x in result[4:9])):
            n, p, prev, total, exponent = map(int, values)
            hits.append(
                {"n": n, "p": p, "a_previous": prev,
                 "sum": total, "power_of_two_exponent": exponent}
            )
        for values in zip(*(x.tolist() for x in result[9:13])):
            n, p, a, h = map(int, values)
            checkpoints.append({"n": n, "p": p, "a": a, "digest": f"{h:016x}"})

    # A nonperiodic target is an explicit terminal checkpoint.
    if index % args.checkpoint_step:
        checkpoints.append(
            {"n": index, "p": int(primes[-1]), "a": int(state),
             "digest": f"{int(digest):016x}"}
        )
    record = {
        "schema": "a114216-exact-replay-v1",
        "path": "A",
        "algorithm": "dense base sieve + NumPy odd-only segmented sieve + lowbit recurrence",
        "target_index": index,
        "search_upper_exclusive": args.upper,
        "segment_odds": args.segment_odds,
        "base_prime_count": int(bases.size),
        "largest_base_prime": int(bases[-1]),
        "final_a": int(state),
        "final_digest_fnv1a_n_p_a_le64": f"{int(digest) & U64_MAX:016x}",
        "maximum_a_seen": overall_max,
        "hits": hits,
        "checkpoints": checkpoints,
        "arithmetic": "exact uint64; overflow checked before every addition",
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    summary = {k: record[k] for k in (
        "path", "target_index", "final_a", "final_digest_fnv1a_n_p_a_le64",
        "maximum_a_seen", "hits")}
    summary["elapsed_seconds_runtime_only"] = time.monotonic() - started
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
