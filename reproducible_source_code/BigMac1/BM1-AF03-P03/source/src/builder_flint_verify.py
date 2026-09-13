#!/usr/bin/env python3
"""Characteristic-zero block verifier backed by python-flint 0.9.0.

This is an independent exact-arithmetic execution path.  It imports only the
Builder branch's algebra model, never another branch's discovery output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from typing import Dict, Iterable, List

import flint
from flint import fmpq, fmpq_mat
from gmpy2 import mpq

from builder_coinvariant import Block, CoinvariantModel, Field, SparseVector
from builder_verify_blocks import unit_monomial, valid_block


def to_fmpq(value):
    if isinstance(value, fmpq):
        return value
    if hasattr(value, "numerator") and hasattr(value, "denominator"):
        return fmpq(int(value.numerator), int(value.denominator))
    return fmpq(int(value))


def from_fmpq(value: fmpq):
    return mpq(int(value.numerator), int(value.denominator))


class FlintQReducer:
    """Batched exact row-space reducer over Q."""

    def __init__(self, ncols: int, batch_size: int = 512):
        self.ncols = ncols
        self.batch_size = batch_size
        self._basis: List[SparseVector] = []
        self._pending: List[SparseVector] = []

    def add(self, vector: SparseVector) -> None:
        if len(self._basis) == self.ncols:
            return
        cleaned = {i: value for i, value in vector.items() if value != 0}
        if not cleaned:
            return
        self._pending.append(cleaned)
        if len(self._pending) >= self.batch_size:
            self.flush()

    def add_many(self, vectors: Iterable[SparseVector]) -> None:
        for vector in vectors:
            self.add(vector)
            if len(self._basis) == self.ncols:
                break

    def flush(self) -> None:
        if not self._pending or len(self._basis) == self.ncols:
            self._pending.clear()
            return
        rows = self._basis + self._pending
        flat = [0] * (len(rows) * self.ncols)
        for i, row in enumerate(rows):
            offset = i * self.ncols
            for col, value in row.items():
                flat[offset + col] = to_fmpq(value)
        matrix = fmpq_mat(len(rows), self.ncols, flat)
        reduced, rank = matrix.rref()
        new_basis: List[SparseVector] = []
        for i in range(rank):
            row: SparseVector = {}
            for col in range(self.ncols):
                value = reduced[i, col]
                if value:
                    row[col] = from_fmpq(value)
            new_basis.append(row)
        self._basis = new_basis
        self._pending = []

    @property
    def rank(self) -> int:
        self.flush()
        return len(self._basis)

    def is_full(self) -> bool:
        return len(self._basis) == self.ncols

    def basis(self) -> List[SparseVector]:
        self.flush()
        return list(self._basis)


def invariant_basis(model: CoinvariantModel, block: Block, batch_size: int) -> List[SparseVector]:
    ambient = model.block_basis(block)
    reducer = FlintQReducer(len(ambient), batch_size)
    rational = Field()
    for monomial in ambient:
        # This may be zero: a signed stabilizer can cancel the orbit sum.
        reducer.add(model.reynolds(monomial, block, rational))
    return reducer.basis()


def verify(n: int, batch_size: int) -> dict:
    started = time.time()
    model = CoinvariantModel(n)
    rational = Field()
    candidates = model.candidates_by_block()
    invariants: Dict[Block, List[SparseVector]] = {}
    inv_total = 0

    for block in model.all_blocks():
        ambient = model.block_basis(block)
        if not ambient:
            continue
        inv = invariant_basis(model, block, batch_size)
        invariants[block] = inv
        inv_total += len(inv)
        print(f"INVQ block={block} ambient={len(ambient)} rank={len(inv)}", file=sys.stderr, flush=True)

    # Since the polynomial coinvariant factor is the regular representation,
    # this is an independent structural consistency check on every Reynolds
    # block and on all Koszul signs.
    if inv_total != 4**n:
        raise RuntimeError(f"invariant dimension {inv_total} != 4^{n}")

    ideals: Dict[Block, List[SparseVector]] = {}
    block_results = []
    for block in model.all_blocks():
        ambient = model.block_basis(block)
        if not ambient:
            continue
        reducer = FlintQReducer(len(ambient), batch_size)
        if sum(block) > 0:
            reducer.add_many(invariants.get(block, []))

        for kind, delta in (("x", (1, 0, 0)), ("theta", (0, 1, 0)), ("xi", (0, 0, 1))):
            if reducer.is_full():
                break
            lower = tuple(block[j] - delta[j] for j in range(3))
            if not valid_block(model, lower):
                continue
            for vector in ideals.get(lower, []):
                if reducer.is_full():
                    break
                for i in range(n):
                    reducer.add(
                        model.multiply_vector_by_monomial(
                            vector,
                            lower,
                            unit_monomial(n, kind, i),
                            block,
                            rational,
                        )
                    )
                    if reducer.is_full():
                        break

        ideal_basis = reducer.basis()
        ideals[block] = ideal_basis
        ideal_rank = len(ideal_basis)
        candidate = candidates.get(block, [])

        augmented = FlintQReducer(len(ambient), batch_size)
        augmented.add_many(ideal_basis)
        index = model.block_index(block)
        augmented.add_many({index[monomial]: 1} for monomial in candidate)
        augmented_rank = augmented.rank
        candidate_added = augmented_rank - ideal_rank
        item = {
            "block": list(block),
            "ambient_dimension": len(ambient),
            "invariant_dimension": len(invariants.get(block, [])),
            "ideal_rank": ideal_rank,
            "quotient_dimension": len(ambient) - ideal_rank,
            "candidate_count": len(candidate),
            "candidate_added_mod_ideal": candidate_added,
            "candidate_spans": augmented_rank == len(ambient),
            "candidate_independent": candidate_added == len(candidate),
        }
        block_results.append(item)
        print(
            f"IDEALQ block={block} ambient={len(ambient)} ideal={ideal_rank} "
            f"quotient={len(ambient)-ideal_rank} candidate={len(candidate)} "
            f"add={candidate_added} span={augmented_rank == len(ambient)}",
            file=sys.stderr,
            flush=True,
        )

    result = {
        "schema": "builder-flint-characteristic-zero-v1",
        "n": n,
        "field": "Q",
        "complete": True,
        "arithmetic_backend": f"python-flint {flint.__version__} fmpq_mat.rref",
        "python": sys.version,
        "platform": platform.platform(),
        "batch_size": batch_size,
        "ambient_dimension": sum(item["ambient_dimension"] for item in block_results),
        "invariant_dimension": inv_total,
        "quotient_dimension": sum(item["quotient_dimension"] for item in block_results),
        "candidate_count": sum(item["candidate_count"] for item in block_results),
        "all_blocks_span": all(item["candidate_spans"] for item in block_results),
        "all_blocks_independent": all(item["candidate_independent"] for item in block_results),
        "elapsed_seconds": time.time() - started,
        "blocks": block_results,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256_without_this_field"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--batch-size", type=int, default=512)
    args = parser.parse_args()
    print(json.dumps(verify(args.n, args.batch_size), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
