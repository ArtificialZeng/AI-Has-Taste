#!/usr/bin/env python3
"""Exact experiments for the Latin Tableau / CDS-colorability conjecture.

The Young diagram ``shape`` is represented by a nonincreasing tuple of
positive row lengths.  Its cells are the edges of the Ferrers bipartite graph
between rows and columns.  A proper coloring of the rook graph is therefore
an edge-coloring of this bipartite graph, with every color class a matching.

All optimization in this file is integer/exact.  CP-SAT is used only as a
finite feasibility solver; every returned coloring is checked again without
calling CP-SAT.  The CDS is computed by the corner min formula and may also be
checked by a separate integral max-flow computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence

import networkx as nx
from ortools.sat.python import cp_model


def normalize_shape(parts: Sequence[int]) -> tuple[int, ...]:
    shape = tuple(int(x) for x in parts if int(x) > 0)
    if not shape or any(shape[i] < shape[i + 1] for i in range(len(shape) - 1)):
        raise ValueError(f"not a nonempty partition: {parts!r}")
    return shape


def conjugate(shape: Sequence[int]) -> tuple[int, ...]:
    shape = normalize_shape(shape)
    return tuple(sum(row_len > j for row_len in shape) for j in range(shape[0]))


def cells(shape: Sequence[int]) -> list[tuple[int, int]]:
    shape = normalize_shape(shape)
    return [(i, j) for i, row_len in enumerate(shape) for j in range(row_len)]


def corner_rho(shape: Sequence[int], k: int) -> int:
    """Return rho_k via the exact Ferrers-board min-cut formula.

    For i initial rows and j initial columns selected in the vertex cover side
    of the min cut, the value is k(i+j) plus the number of cells southeast of
    that corner.  Ferrers monotonicity makes an initial choice optimal among
    all choices with the same numbers of rows and columns.
    """
    shape = normalize_shape(shape)
    if k < 0:
        raise ValueError("k must be nonnegative")
    if k == 0:
        return 0
    rows, cols = len(shape), shape[0]
    best = sum(shape)
    for i in range(rows + 1):
        for j in range(cols + 1):
            residual = sum(max(row_len - j, 0) for row_len in shape[i:])
            best = min(best, k * (i + j) + residual)
    return best


def flow_rho(shape: Sequence[int], k: int) -> int:
    """Independent rho_k evaluator using an integral capacitated max flow."""
    shape = normalize_shape(shape)
    if k < 0:
        raise ValueError("k must be nonnegative")
    if k == 0:
        return 0
    graph = nx.DiGraph()
    source, sink = ("source",), ("sink",)
    for i in range(len(shape)):
        graph.add_edge(source, ("r", i), capacity=k)
    for j in range(shape[0]):
        graph.add_edge(("c", j), sink, capacity=k)
    for i, j in cells(shape):
        graph.add_edge(("r", i), ("c", j), capacity=1)
    return int(nx.maximum_flow_value(graph, source, sink))


def cds(shape: Sequence[int]) -> tuple[int, ...]:
    shape = normalize_shape(shape)
    total = sum(shape)
    delta: list[int] = []
    previous = 0
    max_degree = max(len(shape), shape[0])
    for k in range(1, max_degree + 1):
        current = corner_rho(shape, k)
        delta.append(current - previous)
        previous = current
    if previous != total:
        raise AssertionError("rho_Delta must cover the whole Ferrers graph")
    while delta and delta[-1] == 0:
        delta.pop()
    return tuple(delta)


def verify_coloring(
    shape: Sequence[int], delta: Sequence[int], coloring: Sequence[Sequence[int]]
) -> tuple[bool, str]:
    """Verify a serialized zero-based coloring directly from definitions."""
    shape = normalize_shape(shape)
    delta = tuple(int(x) for x in delta)
    if len(coloring) != len(shape):
        return False, "wrong number of rows"
    counts = [0] * len(delta)
    col_seen = [set() for _ in range(shape[0])]
    for i, row_len in enumerate(shape):
        if len(coloring[i]) != row_len:
            return False, f"row {i} has the wrong length"
        row_seen: set[int] = set()
        for j, raw_color in enumerate(coloring[i]):
            color = int(raw_color)
            if color < 0 or color >= len(delta):
                return False, f"cell {(i, j)} has out-of-range color {color}"
            if color in row_seen:
                return False, f"color {color} repeats in row {i}"
            if color in col_seen[j]:
                return False, f"color {color} repeats in column {j}"
            row_seen.add(color)
            col_seen[j].add(color)
            counts[color] += 1
    if tuple(counts) != delta:
        return False, f"color counts {tuple(counts)} differ from CDS {delta}"
    for k in range(1, len(delta) + 1):
        if sum(counts[:k]) != corner_rho(shape, k):
            return False, f"prefix {k} does not attain rho_{k}"
    return True, "verified"


@dataclass(frozen=True)
class SolveResult:
    status: str
    shape: tuple[int, ...]
    delta: tuple[int, ...]
    coloring: tuple[tuple[int, ...], ...] | None
    wall_seconds: float
    conflicts: int
    branches: int


def solve_shape(
    raw_shape: Sequence[int],
    *,
    time_limit: float = 30.0,
    random_seed: int = 0,
    forced_first_matching: Iterable[tuple[int, int]] | None = None,
) -> SolveResult:
    shape = normalize_shape(raw_shape)
    target = cds(shape)
    board = cells(shape)
    model = cp_model.CpModel()
    variables: dict[tuple[int, int, int], cp_model.IntVar] = {}
    for i, j in board:
        for color in range(len(target)):
            variables[i, j, color] = model.new_bool_var(f"x_{i}_{j}_{color}")
        model.add_exactly_one(variables[i, j, color] for color in range(len(target)))
    for i, row_len in enumerate(shape):
        for color in range(len(target)):
            model.add_at_most_one(variables[i, j, color] for j in range(row_len))
    for j in range(shape[0]):
        incident_rows = [i for i, row_len in enumerate(shape) if j < row_len]
        for color in range(len(target)):
            model.add_at_most_one(variables[i, j, color] for i in incident_rows)
    for color, required in enumerate(target):
        model.add(sum(variables[i, j, color] for i, j in board) == required)
    if forced_first_matching is not None:
        forced = tuple(forced_first_matching)
        if len(forced) != target[0] or len(set(forced)) != len(forced):
            raise ValueError("forced first matching must contain exactly delta_1 distinct cells")
        for i, j in forced:
            if (i, j) not in board:
                raise ValueError(f"forced cell {(i, j)} is outside the shape")
            model.add(variables[i, j, 0] == 1)

    # Equal-sized colors are interchangeable.  Force the row-major incidence
    # vector of each such color to be lexicographically no smaller than the
    # next one by ordering the integer represented by those bit vectors.
    # Chunking avoids huge coefficients while retaining safe local symmetry
    # breaking; it is not needed for correctness.
    if forced_first_matching is None:
        for color in range(len(target) - 1):
            if target[color] == target[color + 1]:
                for start in range(0, len(board), 30):
                    chunk = board[start : start + 30]
                    weights = [1 << (len(chunk) - index - 1) for index in range(len(chunk))]
                    lhs = sum(weights[t] * variables[i, j, color] for t, (i, j) in enumerate(chunk))
                    rhs = sum(weights[t] * variables[i, j, color + 1] for t, (i, j) in enumerate(chunk))
                    model.add(lhs >= rhs)
                    break

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(time_limit)
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = int(random_seed)
    solver.parameters.cp_model_presolve = True
    started = time.monotonic()
    status_code = solver.solve(model)
    elapsed = time.monotonic() - started
    status_name = solver.status_name(status_code).lower().replace(" ", "-")
    coloring = None
    if status_code in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        rows: list[tuple[int, ...]] = []
        for i, row_len in enumerate(shape):
            row: list[int] = []
            for j in range(row_len):
                chosen = [c for c in range(len(target)) if solver.value(variables[i, j, c])]
                if len(chosen) != 1:
                    raise AssertionError("CP-SAT returned a malformed assignment")
                row.append(chosen[0])
            rows.append(tuple(row))
        coloring = tuple(rows)
        okay, reason = verify_coloring(shape, target, coloring)
        if not okay:
            raise AssertionError(reason)
    return SolveResult(
        status=status_name,
        shape=shape,
        delta=target,
        coloring=coloring,
        wall_seconds=elapsed,
        conflicts=solver.num_conflicts,
        branches=solver.num_branches,
    )


def partitions_in_box(rows: int, cols: int) -> Iterator[tuple[int, ...]]:
    """Enumerate every nonempty partition fitting in rows x cols exactly once."""
    if rows < 1 or cols < 1:
        return

    def visit(prefix: tuple[int, ...], maximum: int, remaining_rows: int) -> Iterator[tuple[int, ...]]:
        if prefix:
            yield prefix
        if remaining_rows == 0:
            return
        for part in range(maximum, 0, -1):
            yield from visit(prefix + (part,), part, remaining_rows - 1)

    yield from visit((), cols, rows)


def parse_shape(text: str) -> tuple[int, ...]:
    return normalize_shape([int(piece) for piece in text.split(",")])


def random_shapes_in_box(
    rows: int,
    cols: int,
    count: int,
    *,
    min_rows: int,
    min_width: int,
    force_max_width: bool,
    seed: int,
) -> list[tuple[int, ...]]:
    """Generate a reproducible set of random shapes (not a uniform sample).

    The row count is uniform in its allowed interval and the row lengths are
    sorted independent uniform integers in the allowed width interval.  With
    ``force_max_width``, one row is fixed to the box width.  The exact seed and
    generator description are stored in the output.
    """
    if not (1 <= min_rows <= rows and 1 <= min_width <= cols):
        raise ValueError("random-shape lower bounds must fit in the box")
    rng = random.Random(seed)
    found: set[tuple[int, ...]] = set()
    attempts = 0
    max_attempts = max(1000, 100 * count)
    while len(found) < count and attempts < max_attempts:
        attempts += 1
        row_count = rng.randint(min_rows, rows)
        lower = 1
        parts = [rng.randint(lower, cols) for _ in range(row_count)]
        if force_max_width:
            parts[0] = cols
        shape = tuple(sorted(parts, reverse=True))
        if shape[0] >= min_width:
            found.add(shape)
    if len(found) != count:
        raise ValueError(f"could generate only {len(found)} distinct random shapes")
    return sorted(found, reverse=True)


def two_level_shapes(rows: int, width: int) -> Iterator[tuple[int, ...]]:
    """All shapes of exact width with at most two distinct positive row lengths."""
    for long_count in range(1, rows + 1):
        yield (width,) * long_count
    for short_width in range(1, width):
        for long_count in range(1, rows):
            for short_count in range(1, rows - long_count + 1):
                yield (width,) * long_count + (short_width,) * short_count


def result_record(result: SolveResult, *, include_coloring: bool) -> dict[str, object]:
    record: dict[str, object] = {
        "shape": list(result.shape),
        "conjugate": list(conjugate(result.shape)),
        "area": sum(result.shape),
        "cds": list(result.delta),
        "status": result.status,
        "wall_seconds": result.wall_seconds,
        "conflicts": result.conflicts,
        "branches": result.branches,
    }
    if include_coloring and result.coloring is not None:
        record["coloring_zero_based"] = [list(row) for row in result.coloring]
    return record


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
    parser.add_argument("--shape", action="append", default=[], help="comma-separated partition")
    parser.add_argument("--box", nargs=2, type=int, metavar=("ROWS", "COLS"))
    parser.add_argument("--two-level", nargs=2, type=int, metavar=("ROWS", "EXACT_WIDTH"))
    parser.add_argument("--new-boundary-only", action="store_true")
    parser.add_argument("--min-width", type=int, default=1)
    parser.add_argument("--min-rows", type=int, default=1)
    parser.add_argument("--sample", type=int, default=None)
    parser.add_argument("--random-count", type=int, default=None)
    parser.add_argument("--force-max-width", action="store_true")
    parser.add_argument("--seed", type=int, default=3402)
    parser.add_argument("--time-limit", type=float, default=30.0)
    parser.add_argument("--check-flow", action="store_true")
    parser.add_argument("--include-colorings", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    candidates: list[tuple[int, ...]] = [parse_shape(text) for text in args.shape]
    complete_enumeration = False
    if args.two_level:
        level_rows, level_width = args.two_level
        candidates.extend(two_level_shapes(level_rows, level_width))
        complete_enumeration = args.sample is None
    if args.box:
        row_bound, col_bound = args.box
        if args.random_count is not None:
            candidates.extend(
                random_shapes_in_box(
                    row_bound,
                    col_bound,
                    args.random_count,
                    min_rows=args.min_rows,
                    min_width=args.min_width,
                    force_max_width=args.force_max_width,
                    seed=args.seed,
                )
            )
        else:
            candidates.extend(partitions_in_box(row_bound, col_bound))
            complete_enumeration = args.sample is None
            if args.new_boundary_only:
                candidates = [
                    shape
                    for shape in candidates
                    if len(shape) == row_bound or shape[0] == col_bound
                ]
            candidates = [
                shape
                for shape in candidates
                if len(shape) >= args.min_rows and shape[0] >= args.min_width
            ]
    candidates = list(dict.fromkeys(candidates))
    generated_count = len(candidates)
    if args.sample is not None and args.sample < len(candidates):
        rng = random.Random(args.seed)
        candidates = rng.sample(candidates, args.sample)
        complete_enumeration = False
    if not candidates:
        parser.error("give at least one --shape, --box, or --two-level")

    records: list[dict[str, object]] = []
    statuses: dict[str, int] = {}
    flow_checks = 0
    started = time.monotonic()
    for index, shape in enumerate(candidates):
        target = cds(shape)
        if args.check_flow:
            for k in range(len(target) + 1):
                corner = corner_rho(shape, k)
                flow = flow_rho(shape, k)
                if corner != flow:
                    raise AssertionError(
                        f"rho mismatch for {shape}, k={k}: corner={corner}, flow={flow}"
                    )
                flow_checks += 1
        result = solve_shape(shape, time_limit=args.time_limit, random_seed=args.seed)
        statuses[result.status] = statuses.get(result.status, 0) + 1
        records.append(result_record(result, include_coloring=args.include_colorings))
        if result.status not in {"optimal", "feasible"}:
            print(json.dumps(records[-1], sort_keys=True), file=sys.stderr)
        if (index + 1) % 100 == 0:
            print(f"checked {index + 1}/{len(candidates)}", file=sys.stderr)

    payload = {
        "schema_version": 1,
        "method": {
            "rho_primary": "Ferrers corner min formula",
            "rho_independent": "integral capacitated max flow" if args.check_flow else None,
            "coloring_solver": "OR-Tools CP-SAT, one deterministic worker",
            "witness_checker": "direct row/column/count/prefix verification",
        },
        "parameters": {
            "shapes_explicit": args.shape,
            "box": args.box,
            "two_level": args.two_level,
            "new_boundary_only": args.new_boundary_only,
            "min_width": args.min_width,
            "min_rows": args.min_rows,
            "sample": args.sample,
            "random_count": args.random_count,
            "random_generator": (
                "row count uniform in allowed interval; sorted independent uniform positive row lengths"
                if args.random_count is not None
                else None
            ),
            "force_max_width": args.force_max_width,
            "seed": args.seed,
            "time_limit_per_shape_seconds": args.time_limit,
            "include_colorings": args.include_colorings,
        },
        "coverage": {
            "generated_before_sampling": generated_count,
            "checked": len(candidates),
            "complete_enumeration_of_declared_domain": complete_enumeration,
            "flow_equalities_checked": flow_checks,
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
