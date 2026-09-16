#!/usr/bin/env python3
"""Large exact int64 search for a ninth zero of OEIS A182510.

The run is certified against signed overflow by a conservative per-step bound,
and it evaluates the recurrence in two algebraically equivalent forms.  Numba
is used only to compile deterministic integer loops; no floating-point
arithmetic is involved.
"""

import argparse
import json
import platform
import time

import numpy as np
from numba import njit


INT64_MAX = (1 << 63) - 1


@njit
def search_direct(limit: int, stride: int):
    x, y = 0, 1
    zero_count, last_zero = 1, 0
    max_abs_value, max_guard = 1, 2
    checkpoint_count = limit // stride - (1 if stride == 1 else 0)
    checkpoints = np.zeros((checkpoint_count, 4), dtype=np.int64)
    j = 0
    next_checkpoint = stride if stride >= 2 else 2
    steps_completed, overflow_flag = 1, 0
    for n in range(2, limit + 1):
        # Since 0 <= (y & n) <= n, |y xor n| <= |y| + n.  Thus this
        # guard bounds both operands of the final subtraction in magnitude.
        ax, ay = abs(x), abs(y)
        margin = INT64_MAX - n
        if ay > margin:
            overflow_flag = 1
            break
        margin -= ay
        if ax > margin:
            overflow_flag = 1
            break
        guard = ax + ay + n
        if guard > max_guard:
            max_guard = guard
        z = (y ^ n) - x
        x, y = y, z
        steps_completed = n
        ay = abs(y)
        if ay > max_abs_value:
            max_abs_value = ay
        if y == 0:
            zero_count += 1
            last_zero = n
        if n == next_checkpoint:
            checkpoints[j, 0] = n
            checkpoints[j, 1] = x
            checkpoints[j, 2] = y
            checkpoints[j, 3] = zero_count
            j += 1
            next_checkpoint += stride
    summary = np.array((x, y, zero_count, last_zero, max_abs_value, max_guard,
                        steps_completed, overflow_flag),
                       dtype=np.int64)
    return summary, checkpoints


@njit
def search_via_and(limit: int, stride: int):
    x, y = 0, 1
    zero_count, last_zero = 1, 0
    max_abs_value, max_guard = 1, 2
    checkpoint_count = limit // stride - (1 if stride == 1 else 0)
    checkpoints = np.zeros((checkpoint_count, 4), dtype=np.int64)
    j = 0
    next_checkpoint = stride if stride >= 2 else 2
    steps_completed, overflow_flag = 1, 0
    for n in range(2, limit + 1):
        ax, ay = abs(x), abs(y)
        margin = INT64_MAX - n
        if ay > margin:
            overflow_flag = 1
            break
        margin -= ay
        if ax > margin:
            overflow_flag = 1
            break
        guard = ax + ay + n
        if guard > max_guard:
            max_guard = guard
        # Infinite-width signed XOR identity for n >= 0:
        # y xor n = y + n - 2*(y & n).
        z = y + n - 2 * (y & n) - x
        x, y = y, z
        steps_completed = n
        ay = abs(y)
        if ay > max_abs_value:
            max_abs_value = ay
        if y == 0:
            zero_count += 1
            last_zero = n
        if n == next_checkpoint:
            checkpoints[j, 0] = n
            checkpoints[j, 1] = x
            checkpoints[j, 2] = y
            checkpoints[j, 3] = zero_count
            j += 1
            next_checkpoint += stride
    summary = np.array((x, y, zero_count, last_zero, max_abs_value, max_guard,
                        steps_completed, overflow_flag),
                       dtype=np.int64)
    return summary, checkpoints


def normalize(result):
    summary, checkpoint_array = result
    x, y, count, last, maximum, guard, steps, overflow = (
        int(value) for value in summary
    )
    return {
        "penultimate_value": x,
        "last_value": y,
        "zero_count": count,
        "last_zero": last,
        "maximum_absolute_value": maximum,
        "maximum_conservative_step_bound": guard,
        "steps_completed": steps,
        "overflow_detected": bool(overflow),
        "checkpoints": [
            {"n": int(n), "a_n_minus_1": int(x0), "a_n": int(y0), "zero_count": int(c)}
            for n, x0, y0, c in checkpoint_array
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10_000_000_000)
    parser.add_argument("--checkpoint-stride", type=int, default=1_000_000_000)
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.limit < 2 or args.limit >= 1 << 63:
        parser.error("limit must lie in [2, 2^63)")
    if args.checkpoint_stride < 1 or args.checkpoint_stride > args.limit:
        parser.error("checkpoint stride must lie in [1, limit]")

    # Compile outside the timed research runs.
    search_direct(2, 1)
    search_via_and(2, 1)

    started = time.perf_counter()
    direct_raw = search_direct(args.limit, args.checkpoint_stride)
    direct_seconds = time.perf_counter() - started
    started = time.perf_counter()
    via_and_raw = search_via_and(args.limit, args.checkpoint_stride)
    via_and_seconds = time.perf_counter() - started
    # Normalize only after both compiled calls have returned.  Fixed-shape
    # NumPy buffers avoid aliasing/boxing ambiguity in long-run evidence.
    direct = normalize(direct_raw)
    via_and = normalize(via_and_raw)

    same = direct == via_and
    no_overflow = (not direct["overflow_detected"] and
                   not via_and["overflow_detected"] and
                   direct["steps_completed"] == args.limit and
                   via_and["steps_completed"] == args.limit and
                   direct["maximum_conservative_step_bound"] <= INT64_MAX and
                   via_and["maximum_conservative_step_bound"] <= INT64_MAX)
    record = {
        "schema_version": 1,
        "semantics": "exact signed int64 with an inductive pre-operation no-overflow guard",
        "identity_checked": "y xor n = y + n - 2*(y & n) for n >= 0",
        "limit_inclusive": args.limit,
        "checkpoint_stride": args.checkpoint_stride,
        "known_zero_indices": [0, 6, 11, 23, 36, 42, 48, 54],
        "direct_xor": direct,
        "and_identity": via_and,
        "implementations_agree": same,
        "no_signed_overflow": no_overflow,
        "int64_max": INT64_MAX,
        "python": platform.python_version(),
        "numba": __import__("numba").__version__,
        "timing_seconds_noncertifying": {
            "direct_xor": direct_seconds,
            "and_identity": via_and_seconds,
        },
    }
    if not same or not no_overflow:
        raise SystemExit("verification failure: implementations disagree or int64 bound failed")
    text = json.dumps(record, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
