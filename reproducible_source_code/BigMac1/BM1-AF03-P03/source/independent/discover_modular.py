#!/usr/bin/env python3
"""Finite-field screening for the independent exact model.

The output of this program is explicitly *not* the final certificate.  Its
purpose is to locate mismatching blocks quickly and to choose compact pivot
sets for subsequent characteristic-zero certification.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from core import block_states, candidate_by_block, multiply_by_generator, reynolds_state


@dataclass
class SparseBasisModP:
    prime: int
    pivots: dict[int, dict[int, int]]

    @classmethod
    def empty(cls, prime: int):
        return cls(prime, {})

    def copy(self):
        return SparseBasisModP(self.prime, {row: dict(vector) for row, vector in self.pivots.items()})

    def add(self, vector: dict[int, int]) -> bool:
        p = self.prime
        work = {row: coefficient % p for row, coefficient in vector.items() if coefficient % p}
        while work:
            pivot = min(work)
            old = self.pivots.get(pivot)
            if old is None:
                inverse = pow(work[pivot], -1, p)
                work = {row: (coefficient * inverse) % p for row, coefficient in work.items() if (coefficient * inverse) % p}
                self.pivots[pivot] = work
                return True
            factor = work[pivot]
            for row, coefficient in old.items():
                new_coefficient = (work.get(row, 0) - factor * coefficient) % p
                if new_coefficient:
                    work[row] = new_coefficient
                else:
                    work.pop(row, None)
        return False

    @property
    def rank(self):
        return len(self.pivots)


def indexed_vector(raw, index, prime):
    accum: dict[int, int] = {}
    for state, coefficient in raw.items():
        row = index[state]
        value = (accum.get(row, 0) + coefficient) % prime
        if value:
            accum[row] = value
        else:
            accum.pop(row, None)
    return accum


def multiplied_vector(vector, predecessor_states, target_index, kind, variable_index, prime):
    accum: dict[int, int] = {}
    for row, coefficient in vector.items():
        source = predecessor_states[row]
        for target, multiplier_coefficient in multiply_by_generator(source, kind, variable_index).items():
            target_row = target_index[target]
            value = (accum.get(target_row, 0) + coefficient * multiplier_coefficient) % prime
            if value:
                accum[target_row] = value
            else:
                accum.pop(target_row, None)
    return accum


def run(n: int, prime: int):
    candidates = candidate_by_block(n)
    blocks: dict[tuple[int, int, int], dict] = {}
    max_x_degree = n * (n - 1) // 2
    failures = []
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
                ideal = SparseBasisModP.empty(prime)
                invariant_rank = 0

                if key != (0, 0, 0):
                    for state in states:
                        if ideal.add(indexed_vector(reynolds_state(state), index, prime)):
                            invariant_rank += 1

                sources = []
                if degree:
                    sources.append(((degree - 1, theta_degree, xi_degree), "x"))
                if theta_degree:
                    sources.append(((degree, theta_degree - 1, xi_degree), "theta"))
                if xi_degree:
                    sources.append(((degree, theta_degree, xi_degree - 1), "xi"))
                generator_columns = 0
                for predecessor_key, kind in sources:
                    predecessor = blocks[predecessor_key]
                    predecessor_states = predecessor["states"]
                    predecessor_basis = predecessor["ideal"]
                    for vector in predecessor_basis.pivots.values():
                        for variable_index in range(n):
                            generator_columns += 1
                            ideal.add(multiplied_vector(vector, predecessor_states, index, kind, variable_index, prime))

                block_candidates = candidates.get(key, [])
                combined = ideal.copy()
                candidate_increments = 0
                for state in block_candidates:
                    candidate_increments += combined.add({index[state]: 1})
                ok = candidate_increments == len(block_candidates) and combined.rank == len(states)
                if not ok:
                    failures.append({
                        "block": key,
                        "ambient": len(states),
                        "ideal_rank": ideal.rank,
                        "candidate_count": len(block_candidates),
                        "candidate_rank_increment": candidate_increments,
                        "combined_rank": combined.rank,
                    })
                blocks[key] = {"states": states, "ideal": ideal}
                elapsed = time.time() - started
                print(
                    f"n={n} p={prime} block={key} N={len(states)} inv={invariant_rank} "
                    f"I={ideal.rank} B={len(block_candidates)} combined={combined.rank} ok={ok} t={elapsed:.2f}s",
                    flush=True,
                )

    summaries = []
    for key in sorted(blocks):
        states = blocks[key]["states"]
        ideal = blocks[key]["ideal"]
        block_candidates = candidates.get(key, [])
        summaries.append({
            "block": list(key),
            "ambient_dimension": len(states),
            "ideal_rank_mod_p": ideal.rank,
            "quotient_dimension_mod_p": len(states) - ideal.rank,
            "candidate_count": len(block_candidates),
        })
    return {
        "schema": "independent-modular-screen-v1",
        "warning": "Finite-field screening only; not a characteristic-zero proof.",
        "n": n,
        "prime": prime,
        "python": sys.version,
        "platform": platform.platform(),
        "elapsed_seconds": time.time() - started,
        "candidate_total": sum(len(v) for v in candidates.values()),
        "ambient_total": sum(len(blocks[key]["states"]) for key in blocks),
        "quotient_total_mod_p": sum(len(blocks[key]["states"]) - blocks[key]["ideal"].rank for key in blocks),
        "failures": failures,
        "blocks": summaries,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--prime", type=int, default=1_000_003)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.n, args.prime)
    encoded = json.dumps(result, indent=2, sort_keys=True).encode()
    if args.output:
        args.output.write_bytes(encoded + b"\n")
        print(f"output_sha256={hashlib.sha256(encoded + b'\n').hexdigest()}")
    print(json.dumps({key: result[key] for key in ("n", "prime", "candidate_total", "ambient_total", "quotient_total_mod_p", "failures", "elapsed_seconds")}, sort_keys=True))


if __name__ == "__main__":
    main()
