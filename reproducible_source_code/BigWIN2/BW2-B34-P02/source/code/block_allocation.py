#!/usr/bin/env python3
"""Exact block-allocation experiments for Ferrers CDS colorings.

Rows of equal length and columns of equal height are amalgamated.  A feasible
integer allocation records how many edges of each CDS color lie in each full
row-block/column-block rectangle.  The colored-detachment lemma quoted in
``proof/two_level_candidate.md`` shows that such an allocation lifts to an
actual proper coloring; conversely, every coloring gives an allocation.

CP-SAT is used only to find finite allocation witnesses.  Every returned
allocation is checked directly, and rho is independently recomputed as an
integral max flow on the amalgamated Ferrers network.
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
from typing import Iterator, Sequence

import networkx as nx
from ortools.sat.python import cp_model

from cds_search import cds, corner_rho, normalize_shape


@dataclass(frozen=True)
class FerrersBlocks:
    lengths: tuple[int, ...]
    row_multiplicities: tuple[int, ...]
    column_widths: tuple[int, ...]


def ferrers_blocks(raw_shape: Sequence[int]) -> FerrersBlocks:
    """Return row-length blocks and the conjugate column-width blocks."""
    shape = normalize_shape(raw_shape)
    lengths: list[int] = []
    multiplicities: list[int] = []
    for part in shape:
        if lengths and lengths[-1] == part:
            multiplicities[-1] += 1
        else:
            lengths.append(part)
            multiplicities.append(1)
    widths = [
        lengths[index] - (lengths[index + 1] if index + 1 < len(lengths) else 0)
        for index in range(len(lengths))
    ]
    return FerrersBlocks(tuple(lengths), tuple(multiplicities), tuple(widths))


def block_flow_rho(raw_shape: Sequence[int], k: int) -> int:
    """Compute rho_k by integral max flow on the amalgamated Ferrers graph."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    shape = normalize_shape(raw_shape)
    if k == 0:
        return 0
    blocks = ferrers_blocks(shape)
    graph = nx.DiGraph()
    source, sink = ("source",), ("sink",)
    for i, multiplicity in enumerate(blocks.row_multiplicities):
        graph.add_edge(source, ("r", i), capacity=k * multiplicity)
    for j, width in enumerate(blocks.column_widths):
        graph.add_edge(("c", j), sink, capacity=k * width)
    for i, multiplicity in enumerate(blocks.row_multiplicities):
        for j in range(i, len(blocks.column_widths)):
            graph.add_edge(
                ("r", i),
                ("c", j),
                capacity=multiplicity * blocks.column_widths[j],
            )
    return int(nx.maximum_flow_value(graph, source, sink))


def two_level_rho(a: int, p: int, b: int, q: int, k: int) -> int:
    """Six-affine-function formula for lambda=(a^p,b^q)."""
    if not (a > b >= 1 and p >= 1 and q >= 1 and k >= 0):
        raise ValueError("need a>b>=1, p,q>=1, and k>=0")
    total = p * a + q * b
    return min(
        total,
        k * a,
        k * (p + q),
        k * (p + b),
        k * b + p * (a - b),
        k * p + q * b,
    )


def canonical_two_level_allocation(
    a: int, p: int, b: int, q: int
) -> tuple[tuple[int, ...], tuple[tuple[int, int, int], ...]]:
    """Construct the owner proof's (top-left, top-right, bottom-left) quotas."""
    shape = (a,) * p + (b,) * q
    target = cds(shape)
    rows = p + q
    extension_width = a - b
    quotas: list[tuple[int, int, int]] = []

    if a >= rows:
        bottom_left = [value - p for value in target]
        top_right = [max(0, value - b) for value in target]
        remaining = p * extension_width - sum(top_right)
        upper = min(p, extension_width)
        for index in range(len(target)):
            increment = min(remaining, upper - top_right[index])
            top_right[index] += increment
            remaining -= increment
        if remaining:
            raise AssertionError("two-level top-right quota capacity failed")
        quotas = [
            (p - top_right[index], top_right[index], bottom_left[index])
            for index in range(len(target))
        ]
    else:
        top_right = [value - b for value in target]
        bottom_left = [max(0, value - p) for value in target]
        remaining = q * b - sum(bottom_left)
        upper = min(q, b)
        for index in range(len(target)):
            increment = min(remaining, upper - bottom_left[index])
            bottom_left[index] += increment
            remaining -= increment
        if remaining:
            raise AssertionError("two-level bottom-left quota capacity failed")
        quotas = [
            (b - bottom_left[index], top_right[index], bottom_left[index])
            for index in range(len(target))
        ]

    if [sum(quota) for quota in quotas] != list(target):
        raise AssertionError("two-level color totals failed")
    if sum(quota[0] for quota in quotas) != p * b:
        raise AssertionError("two-level top-left block total failed")
    if sum(quota[1] for quota in quotas) != p * extension_width:
        raise AssertionError("two-level top-right block total failed")
    if sum(quota[2] for quota in quotas) != q * b:
        raise AssertionError("two-level bottom-left block total failed")
    for value, (x, y, z) in zip(target, quotas):
        if min(x, y, z) < 0 or x + y > p or x + z > b:
            raise AssertionError("two-level row/column color capacity failed")
        if y > extension_width or z > q or x + y + z != value:
            raise AssertionError("two-level block/color capacity failed")
    return target, tuple(quotas)


def verify_allocation(
    raw_shape: Sequence[int],
    target: Sequence[int],
    allocation: Sequence[Sequence[Sequence[int]]],
) -> tuple[bool, str]:
    """Check a triangular row-block/column-block/color allocation exactly."""
    shape = normalize_shape(raw_shape)
    target = tuple(int(value) for value in target)
    if target != cds(shape):
        return False, "stored target is not the CDS"
    blocks = ferrers_blocks(shape)
    block_count = len(blocks.lengths)
    if len(allocation) != block_count:
        return False, "wrong row-block count"
    values: dict[tuple[int, int, int], int] = {}
    for i in range(block_count):
        expected_columns = block_count - i
        if len(allocation[i]) != expected_columns:
            return False, f"wrong column-block count in row block {i}"
        for offset, color_values in enumerate(allocation[i]):
            j = i + offset
            if len(color_values) != len(target):
                return False, f"wrong color count in block {(i, j)}"
            for color, raw_value in enumerate(color_values):
                value = int(raw_value)
                if value < 0:
                    return False, f"negative quota in block {(i, j)}, color {color}"
                values[i, j, color] = value

    for i, multiplicity in enumerate(blocks.row_multiplicities):
        for j in range(i, block_count):
            actual = sum(values[i, j, color] for color in range(len(target)))
            expected = multiplicity * blocks.column_widths[j]
            if actual != expected:
                return False, f"block {(i, j)} total {actual} != {expected}"
    for color in range(len(target)):
        actual = sum(
            values[i, j, color]
            for i in range(block_count)
            for j in range(i, block_count)
        )
        if actual != target[color]:
            return False, f"color {color} total {actual} != {target[color]}"
        for i, multiplicity in enumerate(blocks.row_multiplicities):
            degree = sum(values[i, j, color] for j in range(i, block_count))
            if degree > multiplicity:
                return False, f"row-block color capacity failed at {(i, color)}"
        for j, width in enumerate(blocks.column_widths):
            degree = sum(values[i, j, color] for i in range(j + 1))
            if degree > width:
                return False, f"column-block color capacity failed at {(j, color)}"
    return True, "verified"


def solve_block_allocation(
    raw_shape: Sequence[int], *, time_limit: float, random_seed: int
) -> tuple[str, tuple[int, ...], list[list[list[int]]] | None, float, int, int]:
    shape = normalize_shape(raw_shape)
    target = cds(shape)
    blocks = ferrers_blocks(shape)
    block_count = len(blocks.lengths)
    model = cp_model.CpModel()
    variables: dict[tuple[int, int, int], cp_model.IntVar] = {}
    for i, multiplicity in enumerate(blocks.row_multiplicities):
        for j in range(i, block_count):
            width = blocks.column_widths[j]
            for color, required in enumerate(target):
                variables[i, j, color] = model.new_int_var(
                    0, min(multiplicity, width, required), f"z_{i}_{j}_{color}"
                )
            model.add(
                sum(variables[i, j, color] for color in range(len(target)))
                == multiplicity * width
            )
    for color, required in enumerate(target):
        model.add(
            sum(
                variables[i, j, color]
                for i in range(block_count)
                for j in range(i, block_count)
            )
            == required
        )
        for i, multiplicity in enumerate(blocks.row_multiplicities):
            model.add(
                sum(variables[i, j, color] for j in range(i, block_count))
                <= multiplicity
            )
        for j, width in enumerate(blocks.column_widths):
            model.add(
                sum(variables[i, j, color] for i in range(j + 1)) <= width
            )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(time_limit)
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = int(random_seed)
    started = time.monotonic()
    status_code = solver.solve(model)
    elapsed = time.monotonic() - started
    status = solver.status_name(status_code).lower().replace(" ", "-")
    allocation = None
    if status_code in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        allocation = []
        for i in range(block_count):
            row: list[list[int]] = []
            for j in range(i, block_count):
                row.append(
                    [solver.value(variables[i, j, color]) for color in range(len(target))]
                )
            allocation.append(row)
        okay, reason = verify_allocation(shape, target, allocation)
        if not okay:
            raise AssertionError(reason)
    return status, target, allocation, elapsed, solver.num_conflicts, solver.num_branches


def three_level_square_boundary(order: int) -> Iterator[tuple[int, ...]]:
    """All order-by-order boundary shapes having at most three row lengths."""
    if order < 1:
        return
    yield (order,) * order
    for b in range(1, order):
        for p in range(1, order):
            yield (order,) * p + (b,) * (order - p)
    for b in range(2, order):
        for c in range(1, b):
            for p in range(1, order - 1):
                for q in range(1, order - p):
                    yield (order,) * p + (b,) * q + (c,) * (order - p - q)


def environment_record() -> dict[str, object]:
    return {
        "python": sys.version,
        "platform": platform.platform(),
        "networkx": nx.__version__,
        "ortools": __import__("ortools").__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shape", action="append", default=[])
    parser.add_argument("--three-level-square-boundary", type=int)
    parser.add_argument("--time-limit", type=float, default=10.0)
    parser.add_argument("--seed", type=int, default=3402002)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    candidates: list[tuple[int, ...]] = []
    for text in args.shape:
        candidates.append(normalize_shape([int(piece) for piece in text.split(",")]))
    if args.three_level_square_boundary is not None:
        candidates.extend(three_level_square_boundary(args.three_level_square_boundary))
    candidates = list(dict.fromkeys(candidates))
    if not candidates:
        parser.error("give --shape or --three-level-square-boundary")

    records: list[dict[str, object]] = []
    statuses: dict[str, int] = {}
    flow_checks = 0
    started = time.monotonic()
    for index, shape in enumerate(candidates):
        target = cds(shape)
        for k in range(len(target) + 1):
            if corner_rho(shape, k) != block_flow_rho(shape, k):
                raise AssertionError(f"rho evaluator mismatch for {shape}, k={k}")
            flow_checks += 1
        status, target, allocation, elapsed, conflicts, branches = solve_block_allocation(
            shape, time_limit=args.time_limit, random_seed=args.seed
        )
        attempts = 1
        if status not in {"optimal", "feasible", "infeasible"}:
            retry = solve_block_allocation(
                shape,
                time_limit=max(30.0, 3.0 * args.time_limit),
                random_seed=args.seed + index + 1,
            )
            retry_status, retry_target, retry_allocation, retry_elapsed, retry_conflicts, retry_branches = retry
            attempts = 2
            elapsed += retry_elapsed
            conflicts += retry_conflicts
            branches += retry_branches
            status, target, allocation = retry_status, retry_target, retry_allocation
        statuses[status] = statuses.get(status, 0) + 1
        record: dict[str, object] = {
            "shape": list(shape),
            "area": sum(shape),
            "distinct_row_lengths": len(ferrers_blocks(shape).lengths),
            "cds": list(target),
            "status": status,
            "wall_seconds": elapsed,
            "conflicts": conflicts,
            "branches": branches,
            "solver_attempts": attempts,
        }
        if allocation is not None:
            record["allocation"] = allocation
        records.append(record)
        if status not in {"optimal", "feasible"}:
            print(json.dumps(record, sort_keys=True), file=sys.stderr)
        if (index + 1) % 500 == 0:
            print(f"checked {index + 1}/{len(candidates)}", file=sys.stderr)

    payload = {
        "schema_version": 1,
        "epistemic_status": "finite exact allocation evidence; detachment lift cited; not a proof of the universal conjecture",
        "method": {
            "rho_primary": "Ferrers corner minimum",
            "rho_independent": "integral max flow on the amalgamated Ferrers network",
            "allocation_solver": "OR-Tools CP-SAT, one deterministic worker",
            "allocation_checker": "direct block/color/row-capacity/column-capacity verification",
        },
        "parameters": {
            "explicit_shapes": args.shape,
            "three_level_square_boundary": args.three_level_square_boundary,
            "time_limit_per_shape_seconds": args.time_limit,
            "seed": args.seed,
        },
        "coverage": {
            "checked": len(candidates),
            "complete_enumeration_of_declared_domain": args.three_level_square_boundary is not None
            and not args.shape,
            "rho_prefixes_cross_checked": flow_checks,
        },
        "statuses": statuses,
        "elapsed_seconds": time.monotonic() - started,
        "environment": environment_record(),
        "records": records,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0 if set(statuses).issubset({"optimal", "feasible"}) else 2


if __name__ == "__main__":
    raise SystemExit(main())
