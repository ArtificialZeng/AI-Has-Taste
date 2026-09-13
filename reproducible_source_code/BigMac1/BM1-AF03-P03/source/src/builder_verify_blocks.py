#!/usr/bin/env python3
"""Blockwise exact/modular verification in the finite Artin--exterior model."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

from builder_coinvariant import Block, CoinvariantModel, Field, SparseReducer, SparseVector


def unit_monomial(n: int, kind: str, i: int):
    exponent = [0] * n
    theta = xi = 0
    if kind == "x":
        exponent[i] = 1
    elif kind == "theta":
        theta = 1 << i
    elif kind == "xi":
        xi = 1 << i
    else:
        raise ValueError(kind)
    return (tuple(exponent), theta, xi)


def valid_block(model: CoinvariantModel, block: Block) -> bool:
    d, t, s = block
    return 0 <= d <= model.top_x_degree and 0 <= t <= model.n and 0 <= s <= model.n


def verify(n: int, field: Field, stop_after_total: int | None = None) -> dict:
    started = time.time()
    model = CoinvariantModel(n)
    candidate_by_block = model.candidates_by_block()
    invariant_by_block: Dict[Block, List[SparseVector]] = {}
    invariant_dimensions: Dict[str, int] = {}

    for block in model.all_blocks():
        if stop_after_total is not None and sum(block) > stop_after_total:
            continue
        basis = model.block_basis(block)
        if not basis:
            continue
        inv = model.invariant_basis(block, field)
        invariant_by_block[block] = inv
        invariant_dimensions[",".join(map(str, block))] = len(inv)
        print(f"INV block={block} ambient={len(basis)} rank={len(inv)}", file=sys.stderr, flush=True)

    ideal_by_block: Dict[Block, List[SparseVector]] = {}
    blocks_result = []
    for block in model.all_blocks():
        if stop_after_total is not None and sum(block) > stop_after_total:
            continue
        basis = model.block_basis(block)
        if not basis:
            continue
        reducer = SparseReducer(field)
        if sum(block) > 0:
            for vector in invariant_by_block.get(block, []):
                reducer.add(vector)
                if reducer.rank == len(basis):
                    break

        for kind, delta in (("x", (1, 0, 0)), ("theta", (0, 1, 0)), ("xi", (0, 0, 1))):
            if reducer.rank == len(basis):
                break
            lower = tuple(block[j] - delta[j] for j in range(3))
            if not valid_block(model, lower):
                continue
            for vector in ideal_by_block.get(lower, []):
                if reducer.rank == len(basis):
                    break
                for i in range(n):
                    product_vector = model.multiply_vector_by_monomial(
                        vector,
                        lower,
                        unit_monomial(n, kind, i),
                        block,
                        field,
                    )
                    reducer.add(product_vector)
                    if reducer.rank == len(basis):
                        break

        ideal_basis = reducer.basis()
        ideal_by_block[block] = ideal_basis
        ideal_rank = reducer.rank
        candidate = candidate_by_block.get(block, [])
        candidate_added = 0
        index = model.block_index(block)
        for monomial in candidate:
            candidate_added += int(reducer.add({index[monomial]: 1}))
        after_candidate_rank = reducer.rank
        quotient_dimension = len(basis) - ideal_rank
        result = {
            "block": list(block),
            "ambient_dimension": len(basis),
            "invariant_dimension": len(invariant_by_block.get(block, [])),
            "ideal_rank": ideal_rank,
            "quotient_dimension": quotient_dimension,
            "candidate_count": len(candidate),
            "candidate_added_mod_ideal": candidate_added,
            "candidate_spans": after_candidate_rank == len(basis),
            "candidate_independent": candidate_added == len(candidate),
        }
        blocks_result.append(result)
        print(
            "IDEAL block={} ambient={} ideal={} quotient={} candidate={} add={} span={}".format(
                block,
                len(basis),
                ideal_rank,
                quotient_dimension,
                len(candidate),
                candidate_added,
                after_candidate_rank == len(basis),
            ),
            file=sys.stderr,
            flush=True,
        )

    complete = stop_after_total is None or stop_after_total >= model.top_x_degree + 2 * n
    total_ambient = sum(item["ambient_dimension"] for item in blocks_result)
    total_quotient = sum(item["quotient_dimension"] for item in blocks_result)
    total_candidate = sum(item["candidate_count"] for item in blocks_result)
    result = {
        "schema": "builder-block-verification-v1",
        "n": n,
        "field": "Q" if field.prime is None else f"F_{field.prime}",
        "complete": complete,
        "stop_after_total": stop_after_total,
        "ambient_dimension": total_ambient,
        "invariant_dimension": sum(invariant_dimensions.values()),
        "quotient_dimension": total_quotient,
        "candidate_count": total_candidate,
        "all_blocks_span": all(item["candidate_spans"] for item in blocks_result),
        "all_blocks_independent": all(item["candidate_independent"] for item in blocks_result),
        "elapsed_seconds": time.time() - started,
        "blocks": blocks_result,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256_without_this_field"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--prime", type=int, default=None, help="discovery only; omit for exact Q")
    parser.add_argument("--stop-after-total", type=int, default=None)
    args = parser.parse_args()
    result = verify(args.n, Field(args.prime), args.stop_after_total)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
