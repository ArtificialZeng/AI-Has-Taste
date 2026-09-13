#!/usr/bin/env python3
"""Fail-closed characteristic-zero verifier for the independent certificate.

Trust boundary
--------------
The verifier reads only a tiny JSON configuration, the cited source PDF, and
its own code.  It neither imports ``core.py``/``discover_modular.py`` nor reads
their output.  It rebuilds the supercommutative algebra from definitions.

Finite-field elimination selects a small subset of genuine integer ideal
columns; it is not used for the conclusion.  Singular 4.x then recomputes the
ranks over Q.  A block passes only if

    rank_Q(generators of I_block) = N - |B_block|,
    rank_Q(selected ideal columns together with B_block) = N.

The ideal is built inductively from exact Reynolds sums and multiplication by
the 3n algebra generators.  Thus the first equality proves the upper bound on
the ideal, while the second proves spanning and independence of the candidate
classes.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import platform
import subprocess
import sys
import tempfile
import time
from functools import lru_cache
from pathlib import Path


SCHEMA = "lentfer-r12-independent-certificate-v1"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_config(path: Path):
    try:
        raw = json.loads(path.read_text())
    except Exception as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc
    required = {"schema", "source_pdf", "source_sha256", "cases", "pivot_prime"}
    if not isinstance(raw, dict) or set(raw) != required:
        raise ValueError(f"configuration keys must be exactly {sorted(required)}")
    if raw["schema"] != SCHEMA:
        raise ValueError("unknown schema")
    if not isinstance(raw["source_pdf"], str) or not raw["source_pdf"]:
        raise ValueError("source_pdf must be a nonempty string")
    if not isinstance(raw["source_sha256"], str) or len(raw["source_sha256"]) != 64:
        raise ValueError("source_sha256 must be 64 hexadecimal characters")
    try:
        int(raw["source_sha256"], 16)
    except ValueError as exc:
        raise ValueError("source_sha256 is not hexadecimal") from exc
    if not isinstance(raw["cases"], list) or not raw["cases"]:
        raise ValueError("cases must be a nonempty list")
    for case in raw["cases"]:
        if not isinstance(case, dict) or set(case) != {"n", "expected_candidate_count"}:
            raise ValueError("each case must have exactly n and expected_candidate_count")
        n = case["n"]
        if type(n) is not int or not (1 <= n <= 5):
            raise ValueError("n must be an integer in [1,5]")
        expected = case["expected_candidate_count"]
        if type(expected) is not int or expected != 2 ** (n - 1) * math.factorial(n):
            raise ValueError("expected_candidate_count does not equal 2^(n-1)n!")
    prime = raw["pivot_prime"]
    if type(prime) is not int or prime <= 5 or any(prime % divisor == 0 for divisor in range(2, math.isqrt(prime) + 1)):
        raise ValueError("pivot_prime must be prime and greater than 5")
    return raw


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


@lru_cache(maxsize=None)
def reduce_poly(a):
    n = len(a)
    bad = next((i for i, exponent in enumerate(a) if exponent >= i + 1), None)
    if bad is None:
        return ((a, 1),)
    power = bad + 1
    base = list(a)
    base[bad] -= power
    excluded = (power,) + (0,) * (n - bad - 1)
    accum = {}
    for tail in compositions(power, n - bad):
        if tail == excluded:
            continue
        child = base.copy()
        for offset, exponent in enumerate(tail):
            child[bad + offset] += exponent
        for reduced, coefficient in reduce_poly(tuple(child)):
            accum[reduced] = accum.get(reduced, 0) - coefficient
    return tuple(sorted((monomial, coefficient) for monomial, coefficient in accum.items() if coefficient))


def artin_polynomials(n, degree):
    for a in itertools.product(*(range(i) for i in range(1, n + 1))):
        if sum(a) == degree:
            yield a


def masks_of_size(n, size):
    for mask in range(1 << n):
        if mask.bit_count() == size:
            yield mask


def block_states(n, degree, theta_degree, xi_degree):
    for a in artin_polynomials(n, degree):
        for tmask in masks_of_size(n, theta_degree):
            for smask in masks_of_size(n, xi_degree):
                yield (a, tmask, smask)


def inversion_sign(values):
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions & 1 else 1


@lru_cache(maxsize=None)
def permute_mask_sign(mask, permutation):
    images = [permutation[i] for i in range(len(permutation)) if (mask >> i) & 1]
    return sum(1 << image for image in images), inversion_sign(images)


@lru_cache(maxsize=None)
def permute_poly(a, permutation):
    moved = [0] * len(a)
    for old, new in enumerate(permutation):
        moved[new] = a[old]
    return reduce_poly(tuple(moved))


@lru_cache(maxsize=None)
def all_permutations(n):
    return tuple(itertools.permutations(range(n)))


def reynolds_state(state):
    a, tmask, smask = state
    accum = {}
    for permutation in all_permutations(len(a)):
        new_tmask, tsign = permute_mask_sign(tmask, permutation)
        new_smask, ssign = permute_mask_sign(smask, permutation)
        sign = tsign * ssign
        for reduced, coefficient in permute_poly(a, permutation):
            target = (reduced, new_tmask, new_smask)
            accum[target] = accum.get(target, 0) + sign * coefficient
    return {target: coefficient for target, coefficient in accum.items() if coefficient}


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def multiply_by_generator(state, kind, index):
    a, tmask, smask = state
    if kind == "theta":
        bit = 1 << index
        if tmask & bit:
            return {}
        # theta_i moves through existing theta variables smaller than i.
        inversions = sum(t < index for t in bits(tmask))
        sign = -1 if inversions & 1 else 1
        return {(a, tmask | bit, smask): sign}
    if kind == "xi":
        bit = 1 << index
        if smask & bit:
            return {}
        # xi_i is placed after all theta variables, then sorted among xi's.
        inversions = tmask.bit_count() + sum(s < index for s in bits(smask))
        sign = -1 if inversions & 1 else 1
        return {(a, tmask, smask | bit): sign}
    if kind == "x":
        raw = list(a)
        raw[index] += 1
        return {(reduced, tmask, smask): coefficient for reduced, coefficient in reduce_poly(tuple(raw))}
    raise ValueError("bad generator kind")


def candidate_states(n):
    for tmask in range(1 << n):
        if tmask & 1:
            continue
        for smask in range(1 << n):
            if smask & 1:
                continue
            alpha = [0]
            for i in range(1, n):
                alpha.append(alpha[-1] - 1 + int(not ((tmask >> i) & 1)) + int(not ((smask >> i) & 1)))
                if alpha[-1] < 0:
                    break
            else:
                for a in itertools.product(*(range(bound + 1) for bound in alpha)):
                    yield (tuple(a), tmask, smask)


def candidates_by_block(n):
    out = {}
    for state in candidate_states(n):
        a, tmask, smask = state
        out.setdefault((sum(a), tmask.bit_count(), smask.bit_count()), []).append(state)
    return out


class ModularSelector:
    def __init__(self, prime):
        self.prime = prime
        self.pivots = {}
        self.selected_integer_columns = []

    def offer(self, integer_vector):
        p = self.prime
        work = {row: coefficient % p for row, coefficient in integer_vector.items() if coefficient % p}
        while work:
            pivot = min(work)
            if pivot not in self.pivots:
                inverse = pow(work[pivot], -1, p)
                self.pivots[pivot] = {row: coefficient * inverse % p for row, coefficient in work.items() if coefficient * inverse % p}
                self.selected_integer_columns.append(dict(integer_vector))
                return True
            factor = work[pivot]
            for row, coefficient in self.pivots[pivot].items():
                value = (work.get(row, 0) - factor * coefficient) % p
                if value:
                    work[row] = value
                else:
                    work.pop(row, None)
        return False


def index_vector(raw, index):
    accum = {}
    for state, coefficient in raw.items():
        row = index[state]
        accum[row] = accum.get(row, 0) + coefficient
        if not accum[row]:
            del accum[row]
    return accum


def multiply_relation(vector, predecessor_states, target_index, kind, variable_index):
    accum = {}
    for row, coefficient in vector.items():
        for target, multiplier_coefficient in multiply_by_generator(predecessor_states[row], kind, variable_index).items():
            target_row = target_index[target]
            accum[target_row] = accum.get(target_row, 0) + coefficient * multiplier_coefficient
            if not accum[target_row]:
                del accum[target_row]
    return accum


def singular_ranks(nrows, generator_columns, selected_columns, candidate_rows, timeout):
    """Return two ranks over Q, computed by Singular from sparse matrices."""
    # If B_block is empty, an exact full-rank check on the selected square
    # submatrix already proves I_block=A_block: selected columns are literal
    # integer ideal elements.  Building the much wider redundant generator
    # matrix in that case adds no mathematical information.
    need_raw_rank = bool(candidate_rows)
    lines = ["option(noredefine);", "ring verifier_ring=0,(z),dp;"]
    if need_raw_rank and generator_columns:
        lines.append(f"smatrix raw[{nrows}][{len(generator_columns)}];")
        for column_index, column in enumerate(generator_columns, 1):
            for row, coefficient in column.items():
                lines.append(f"raw[{row + 1},{column_index}]={coefficient};")
        lines.append('print("RAW_RANK="+string(rank(raw)));')
        lines.append("kill raw;")
    elif need_raw_rank:
        lines.append('print("RAW_RANK=0");')
    combined_count = len(selected_columns) + len(candidate_rows)
    lines.append(f"smatrix combined[{nrows}][{combined_count}];")
    for column_index, column in enumerate(selected_columns, 1):
        for row, coefficient in column.items():
            lines.append(f"combined[{row + 1},{column_index}]={coefficient};")
    offset = len(selected_columns)
    for position, row in enumerate(candidate_rows, 1):
        lines.append(f"combined[{row + 1},{offset + position}]=1;")
    lines.append('print("COMBINED_RANK="+string(rank(combined)));')
    lines.append("quit;")
    script = "\n".join(lines) + "\n"
    with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False) as handle:
        handle.write(script)
        script_path = handle.name
    try:
        completed = subprocess.run(
            ["Singular", "-q", script_path],
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    finally:
        os.unlink(script_path)
    if completed.returncode != 0 or "?" in completed.stdout or "error" in completed.stderr.lower():
        raise RuntimeError(f"Singular failed closed: rc={completed.returncode}\nstdout={completed.stdout}\nstderr={completed.stderr}")
    values = {}
    for line in completed.stdout.splitlines():
        if "=" in line:
            key, value = line.strip().split("=", 1)
            if key in {"RAW_RANK", "COMBINED_RANK"} and value.isdigit():
                values[key] = int(value)
    expected_keys = {"RAW_RANK", "COMBINED_RANK"} if need_raw_rank else {"COMBINED_RANK"}
    if set(values) != expected_keys:
        raise RuntimeError(f"could not parse Singular rank output: {completed.stdout!r}")
    combined_rank = values["COMBINED_RANK"]
    raw_rank = values["RAW_RANK"] if need_raw_rank else combined_rank
    return raw_rank, combined_rank


def verify_case(n, expected_candidate_count, prime, timeout, block_filter=None):
    candidates = candidates_by_block(n)
    if sum(map(len, candidates.values())) != expected_candidate_count:
        raise AssertionError("candidate enumeration count mismatch")
    max_x_degree = n * (n - 1) // 2
    blocks = {}
    records = []
    started = time.time()
    for total in range(max_x_degree + 2 * n + 1):
        for degree in range(max_x_degree + 1):
            for theta_degree in range(n + 1):
                xi_degree = total - degree - theta_degree
                if not (0 <= xi_degree <= n):
                    continue
                key = (degree, theta_degree, xi_degree)
                states = tuple(block_states(n, *key))
                if not states:
                    continue
                index = {state: row for row, state in enumerate(states)}
                selector = ModularSelector(prime)
                generators = []
                block_candidates = candidates.get(key, [])
                full_ideal_target = not block_candidates
                selection_complete = False
                if key != (0, 0, 0):
                    for state in states:
                        column = index_vector(reynolds_state(state), index)
                        if column:
                            generators.append(column)
                            selector.offer(column)
                            if full_ideal_target and len(selector.selected_integer_columns) == len(states):
                                selection_complete = True
                                break
                sources = []
                if degree:
                    sources.append(((degree - 1, theta_degree, xi_degree), "x"))
                if theta_degree:
                    sources.append(((degree, theta_degree - 1, xi_degree), "theta"))
                if xi_degree:
                    sources.append(((degree, theta_degree, xi_degree - 1), "xi"))
                if not selection_complete:
                    for predecessor_key, kind in sources:
                        predecessor = blocks[predecessor_key]
                        for relation in predecessor["relations"]:
                            for variable_index in range(n):
                                column = multiply_relation(relation, predecessor["states"], index, kind, variable_index)
                                if column:
                                    generators.append(column)
                                    selector.offer(column)
                                    if full_ideal_target and len(selector.selected_integer_columns) == len(states):
                                        selection_complete = True
                                        break
                            if selection_complete:
                                break
                        if selection_complete:
                            break
                candidate_rows = [index[state] for state in block_candidates]
                selected = selector.selected_integer_columns
                should_check = block_filter is None or key in block_filter
                if should_check:
                    raw_rank, combined_rank = singular_ranks(len(states), generators, selected, candidate_rows, timeout)
                    expected_ideal_rank = len(states) - len(block_candidates)
                    ok = raw_rank == expected_ideal_rank and combined_rank == len(states) and len(selected) == expected_ideal_rank
                    print(
                        f"EXACT n={n} block={key} N={len(states)} generators={len(generators)} "
                        f"selected={len(selected)} rankI={raw_rank} B={len(block_candidates)} "
                        f"rank[I|B]={combined_rank} ok={ok} t={time.time()-started:.2f}s",
                        flush=True,
                    )
                    if not ok:
                        raise AssertionError(f"exact block failure at n={n}, block={key}")
                    records.append({
                        "block": list(key),
                        "ambient_dimension": len(states),
                        "generator_columns": len(generators),
                        "selected_ideal_columns": len(selected),
                        "ideal_rank_Q": raw_rank,
                        "candidate_count": len(block_candidates),
                        "combined_rank_Q": combined_rank,
                    })
                blocks[key] = {"states": states, "relations": selected}
    return {
        "n": n,
        "expected_candidate_count": expected_candidate_count,
        "checked_blocks": len(records),
        "blocks": records,
        "elapsed_seconds": time.time() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--case", type=int, action="append", help="verify only listed n")
    parser.add_argument("--block", action="append", help="optional d,t,s block, for diagnostics only")
    parser.add_argument("--singular-timeout", type=int, default=3600)
    args = parser.parse_args()
    try:
        config = load_config(args.certificate)
        source_path = (args.certificate.parent / config["source_pdf"]).resolve()
        if not source_path.is_file() or sha256_file(source_path) != config["source_sha256"]:
            raise ValueError("source PDF missing or SHA-256 mismatch")
        requested = set(args.case or [case["n"] for case in config["cases"]])
        configured = {case["n"] for case in config["cases"]}
        if not requested <= configured:
            raise ValueError("requested case is not present in certificate")
        block_filter = None
        if args.block:
            block_filter = set()
            for text in args.block:
                parts = text.split(",")
                if len(parts) != 3 or any(not part.isdigit() for part in parts):
                    raise ValueError("--block must have form d,t,s with nonnegative integers")
                block_filter.add(tuple(map(int, parts)))
        results = []
        for case in config["cases"]:
            if case["n"] in requested:
                results.append(verify_case(case["n"], case["expected_candidate_count"], config["pivot_prime"], args.singular_timeout, block_filter))
        record = {
            "schema": "lentfer-r12-independent-verification-record-v1",
            "certificate_sha256": sha256_file(args.certificate),
            "verifier_sha256": sha256_file(Path(__file__)),
            "source_sha256": config["source_sha256"],
            "python": sys.version,
            "platform": platform.platform(),
            "singular_version": subprocess.run(["Singular", "--version"], text=True, capture_output=True, check=True).stdout.splitlines()[0],
            "result": "PASS",
            "cases": results,
        }
        encoded = json.dumps(record, indent=2, sort_keys=True).encode() + b"\n"
        if args.output:
            args.output.write_bytes(encoded)
        print(f"PASS record_sha256={hashlib.sha256(encoded).hexdigest()}")
    except Exception as exc:
        print(f"FAIL_CLOSED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
