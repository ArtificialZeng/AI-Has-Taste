#!/usr/bin/env python3
"""Exact A114216 replay, path B: Numba full-integer segmented sieve.

This deliberately independent implementation obtains base primes by trial
division, represents every integer (including evens) in irregular-width
segments, marks multiples in scalar compiled loops, and removes factors of two
from the recurrence by repeated shifts.  It shares no executable code with
path_a_numpy.py.
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


def trial_division_bases(limit: int) -> np.ndarray:
    primes = []
    for candidate in range(2, limit + 1):
        prime = True
        root = math.isqrt(candidate)
        for divisor in primes:
            if divisor > root:
                break
            if candidate % divisor == 0:
                prime = False
                break
        if prime:
            primes.append(candidate)
    return np.asarray(primes, dtype=np.uint64)


@njit(cache=True)
def mix_tuple(h, n, p, a):
    """Independently written FNV-1a of three little-endian uint64 words."""
    words = (np.uint64(n), np.uint64(p), np.uint64(a))
    for word in words:
        value = word
        for _ in range(8):
            h = h ^ (value % np.uint64(256))
            h = h * np.uint64(FNV_PRIME)
            value = value // np.uint64(256)
    return h


@njit(cache=True)
def sieve_and_replay(low, high, bases, target, index, state, digest, checkpoint_step):
    flags = np.ones(high - low, dtype=np.uint8)
    for j in range(bases.size):
        p = int(bases[j])
        square = p * p
        if square >= high:
            break
        first = ((low + p - 1) // p) * p
        if first < square:
            first = square
        for multiple in range(first, high, p):
            flags[multiple - low] = 0

    capacity = high - low
    hit_n = np.empty(capacity, dtype=np.uint64)
    hit_p = np.empty(capacity, dtype=np.uint64)
    hit_prev = np.empty(capacity, dtype=np.uint64)
    hit_total = np.empty(capacity, dtype=np.uint64)
    hit_exp = np.empty(capacity, dtype=np.uint8)
    cp_n = np.empty(capacity, dtype=np.uint64)
    cp_p = np.empty(capacity, dtype=np.uint64)
    cp_a = np.empty(capacity, dtype=np.uint64)
    cp_digest = np.empty(capacity, dtype=np.uint64)
    nh = 0
    nc = 0
    final_p = 0
    max_a = state
    for offset in range(capacity):
        if flags[offset] == 0:
            continue
        p = np.uint64(low + offset)
        previous = state
        total = previous + p
        if total < previous:
            raise OverflowError("uint64 recurrence overflow")
        exponent = 0
        while total % np.uint64(2) == 0:
            total //= np.uint64(2)
            exponent += 1
        state = total
        index += 1
        final_p = p
        digest = mix_tuple(digest, index, p, state)
        if state > max_a:
            max_a = state
        if state == 1:
            hit_n[nh] = index
            hit_p[nh] = p
            hit_prev[nh] = previous
            hit_total[nh] = previous + p
            hit_exp[nh] = exponent
            nh += 1
        if index % checkpoint_step == 0:
            cp_n[nc] = index
            cp_p[nc] = p
            cp_a[nc] = state
            cp_digest[nc] = digest
            nc += 1
        if index == target:
            break
    return (
        index, state, digest, final_p, max_a,
        hit_n[:nh], hit_p[:nh], hit_prev[:nh], hit_total[:nh], hit_exp[:nh],
        cp_n[:nc], cp_p[:nc], cp_a[:nc], cp_digest[:nc],
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=100_000_000)
    ap.add_argument("--upper", type=int, default=2_100_000_000)
    ap.add_argument("--segment-width", type=int, default=2_000_003)
    ap.add_argument("--checkpoint-step", type=int, default=1_000_000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if not (1 <= args.target <= 100_000_000):
        raise ValueError("target outside implemented certificate range")

    started = time.monotonic()
    bases = trial_division_bases(math.isqrt(args.upper - 1))
    index = 0
    state = np.uint64(0)
    digest = np.uint64(FNV_OFFSET)
    overall_max = 0
    final_p = 0
    hits = []
    checkpoints = []
    low = 2
    while index < args.target:
        high = min(args.upper, low + args.segment_width)
        if high <= low:
            raise RuntimeError("upper bound contains too few primes")
        result = sieve_and_replay(
            low, high, bases, np.uint64(args.target), np.uint64(index), state,
            digest, np.uint64(args.checkpoint_step)
        )
        index, state, digest, final_p, chunk_max = map(int, result[:5])
        overall_max = max(overall_max, chunk_max)
        for values in zip(*(x.tolist() for x in result[5:10])):
            n, p, prev, total, exponent = map(int, values)
            hits.append(
                {"n": n, "p": p, "a_previous": prev,
                 "sum": total, "power_of_two_exponent": exponent}
            )
        for values in zip(*(x.tolist() for x in result[10:14])):
            n, p, a, h = map(int, values)
            checkpoints.append({"n": n, "p": p, "a": a, "digest": f"{h:016x}"})
        low = high

    if index % args.checkpoint_step:
        checkpoints.append(
            {"n": index, "p": final_p, "a": int(state),
             "digest": f"{int(digest):016x}"}
        )
    record = {
        "schema": "a114216-exact-replay-v1",
        "path": "B",
        "algorithm": "trial-division bases + full-integer scalar segmented sieve + shift recurrence",
        "target_index": index,
        "search_upper_exclusive": args.upper,
        "segment_width": args.segment_width,
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
