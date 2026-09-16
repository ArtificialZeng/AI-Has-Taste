#!/usr/bin/env python3
"""Independent bounded SMT verifier for the P4/Paw coefficient system.

This verifier does not import or call ``enumerate_signatures.py``.  It encodes
the eight positive coordinates directly as six-bit bit-vectors, widens every
coordinate to 32 bits before arithmetic, and asks Z3 to decide the frozen four
equations.  It first decides the strict sub-61 range and then enumerates and
blocks every model in the range through 61, ending only after an UNSAT result.

All arithmetic in the SMT formula is modulo 2^32.  The explicit bounds below
show that the difference of the two mathematical sides of each coefficient
equation has absolute value below 2^32.  Consequently bit-vector equality is
equivalent to ordinary integer equality throughout the encoded domain.
"""

from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
import platform
import sys
import time

import z3


CODE_VERSION = "1.0.0"
MAX_SUM = 61
MAX_COORDINATE = MAX_SUM - 3
VARIABLE_WIDTH = 6
ARITHMETIC_WIDTH = 32
CHECK_TIMEOUT_MS = 300_000

SCRIPT_PATH = Path(__file__).resolve()
EVIDENCE_DIR = SCRIPT_PATH.parent
PROJECT_DIR = EVIDENCE_DIR.parent
REPORT_PATH = EVIDENCE_DIR / "z3_bv_verification_61.json"
BELOW_SMT2_PATH = EVIDENCE_DIR / "z3_bv_below_61.smt2"
BASE_SMT2_PATH = EVIDENCE_DIR / "z3_bv_at_most_61.smt2"
BLOCKED_SMT2_PATH = EVIDENCE_DIR / "z3_bv_at_most_61_blocked.smt2"

NAMES = ("b0", "b1", "b2", "b3", "a0", "a1", "a2", "a3")


def atomic_text(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def atomic_json(report: dict[str, object]) -> None:
    atomic_text(REPORT_PATH, json.dumps(report, indent=2, sort_keys=True) + "\n")


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def new_variables() -> tuple[z3.BitVecRef, ...]:
    return tuple(z3.BitVec(name, VARIABLE_WIDTH) for name in NAMES)


def widened(variables: tuple[z3.BitVecRef, ...]) -> tuple[z3.BitVecRef, ...]:
    extra = ARITHMETIC_WIDTH - VARIABLE_WIDTH
    return tuple(z3.ZeroExt(extra, variable) for variable in variables)


def make_solver(maximum_sum: int) -> tuple[z3.Solver, tuple[z3.BitVecRef, ...]]:
    """Build the frozen system directly, without signature-table generation."""
    variables = new_variables()
    b0v, b1v, b2v, b3v, a0v, a1v, a2v, a3v = variables
    b0, b1, b2, b3, a0, a1, a2, a3 = widened(variables)

    solver = z3.SolverFor("QF_BV")
    solver.set(timeout=CHECK_TIMEOUT_MS, random_seed=0)
    one = z3.BitVecVal(1, VARIABLE_WIDTH)
    coordinate_cap = z3.BitVecVal(MAX_COORDINATE, VARIABLE_WIDTH)
    for variable in variables:
        solver.add(z3.UGE(variable, one), z3.ULE(variable, coordinate_cap))

    b_sum = b0 + b1 + b2 + b3
    a_sum = a0 + a1 + a2 + a3
    solver.add(b_sum == a_sum)
    solver.add(z3.ULE(b_sum, z3.BitVecVal(maximum_sum, ARITHMETIC_WIDTH)))
    solver.add(
        3 * b0 * b1 - 5 * b0 * b3 + 3 * b1 * b2 + 3 * b2 * b3
        == 3 * (a0 * a1 + a0 * a2 + a0 * a3 + a1 * a2)
    )
    solver.add(8 * b0 * b3 * (b1 + b2) == 2 * a1 * a2 * (a3 - 2 * a0))
    solver.add(4 * b0 * b1 * b2 * b3 == a0 * a1 * a2 * a3)
    return solver, variables


def exact_signature(side: str, values: tuple[int, int, int, int]) -> tuple[int, ...]:
    x0, x1, x2, x3 = values
    if side == "b":
        return (
            x0 + x1 + x2 + x3,
            3 * x0 * x1 - 5 * x0 * x3 + 3 * x1 * x2 + 3 * x2 * x3,
            8 * x0 * x3 * (x1 + x2),
            4 * x0 * x1 * x2 * x3,
        )
    return (
        x0 + x1 + x2 + x3,
        3 * (x0 * x1 + x0 * x2 + x0 * x3 + x1 * x2),
        2 * x1 * x2 * (x3 - 2 * x0),
        x0 * x1 * x2 * x3,
    )


def model_values(
    model: z3.ModelRef, variables: tuple[z3.BitVecRef, ...]
) -> tuple[int, ...]:
    return tuple(model.eval(variable, model_completion=True).as_long() for variable in variables)


def serialized_solution(values: tuple[int, ...]) -> dict[str, object]:
    b = values[:4]
    a = values[4:]
    b_signature = exact_signature("b", b)
    a_signature = exact_signature("a", a)
    if b_signature != a_signature:
        raise RuntimeError(f"Z3 model fails exact host-integer substitution: {values}")
    return {"b": list(b), "a": list(a), "signature": list(b_signature)}


def result_name(result: z3.CheckSatResult) -> str:
    return str(result)


def main() -> int:
    started = time.monotonic()
    report: dict[str, object] = {
        "schema": "p4-paw-independent-z3-bv-verifier-v1",
        "status": "running",
        "code_version": CODE_VERSION,
        "program": str(SCRIPT_PATH.relative_to(PROJECT_DIR)),
        "program_sha256": file_sha256(SCRIPT_PATH),
        "source_sha256": file_sha256(PROJECT_DIR / "source.md"),
        "runtime": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "z3": z3.get_version_string(),
        },
        "randomness": "Z3 random_seed=0; no generated or sampled inputs",
        "domain": {
            "objects": "ordered positive integer quadruple pairs (b,a)",
            "common_sum_minimum": 4,
            "common_sum_maximum": MAX_SUM,
            "coordinate_bounds": [1, MAX_COORDINATE],
            "domain_count_each_side": sum(comb(s - 1, 3) for s in range(4, MAX_SUM + 1)),
            "domain_count_identity": "sum_{s=4}^{61} binom(s-1,3) = binom(61,4)",
            "pruning": "none beyond positivity, common sum, and the stated maximum sum",
        },
        "encoding": {
            "logic": "QF_BV",
            "coordinate_width_bits": VARIABLE_WIDTH,
            "arithmetic_width_bits": ARITHMETIC_WIDTH,
            "coordinate_extension": "unsigned zero extension before every arithmetic expression",
            "equations": "the four frozen equations are asserted literally",
            "modular_soundness": {
                "criterion": "for each equality, the absolute integer difference of its sides is less than 2^32",
                "bounds_using_1_le_coordinate_le_58": {
                    "sum_difference_abs_lt": 465,
                    "quadratic_difference_abs_le": 87464,
                    "cubic_difference_abs_le": 4292464,
                    "quartic_difference_abs_le": 56582480,
                },
                "modulus": 4294967296,
                "conclusion": "bit-vector equality iff ordinary integer equality on the encoded domain",
            },
        },
        "sub_61_query": {"maximum_sum": 60, "result": None},
        "at_most_61_query": {
            "maximum_sum": 61,
            "models": [],
            "terminal_result": None,
        },
    }
    atomic_json(report)

    below_solver, _ = make_solver(60)
    atomic_text(BELOW_SMT2_PATH, below_solver.to_smt2())
    below_started = time.monotonic()
    below_result = below_solver.check()
    report["sub_61_query"] = {
        "maximum_sum": 60,
        "result": result_name(below_result),
        "elapsed_seconds": round(time.monotonic() - below_started, 6),
        "smt2_file": str(BELOW_SMT2_PATH.relative_to(PROJECT_DIR)),
        "smt2_sha256": file_sha256(BELOW_SMT2_PATH),
        "reason_unknown": below_solver.reason_unknown() if below_result == z3.unknown else None,
    }
    atomic_json(report)
    if below_result != z3.unsat:
        report["status"] = "incomplete"
        report["failure"] = "strict sub-61 query did not return UNSAT"
        atomic_json(report)
        return 2

    solver, variables = make_solver(MAX_SUM)
    atomic_text(BASE_SMT2_PATH, solver.to_smt2())
    query = report["at_most_61_query"]
    assert isinstance(query, dict)
    models: list[dict[str, object]] = []
    checks: list[dict[str, object]] = []

    while True:
        check_started = time.monotonic()
        result = solver.check()
        elapsed = round(time.monotonic() - check_started, 6)
        checks.append({"result": result_name(result), "elapsed_seconds": elapsed})
        if result == z3.unsat:
            query["terminal_result"] = "unsat"
            break
        if result != z3.sat:
            query["terminal_result"] = result_name(result)
            query["reason_unknown"] = solver.reason_unknown()
            report["status"] = "incomplete"
            report["failure"] = "at-most-61 enumeration did not terminate with UNSAT"
            query["checks"] = checks
            atomic_json(report)
            return 2

        values = model_values(solver.model(), variables)
        models.append(serialized_solution(values))
        query["models"] = sorted(models, key=lambda item: (item["b"], item["a"]))
        query["checks"] = checks
        atomic_json(report)
        solver.add(
            z3.Or(
                *[
                    variable != z3.BitVecVal(value, VARIABLE_WIDTH)
                    for variable, value in zip(variables, values)
                ]
            )
        )

    query["models"] = sorted(models, key=lambda item: (item["b"], item["a"]))
    query["model_count"] = len(models)
    query["checks"] = checks
    sums = sorted({item["signature"][0] for item in models})
    query["matching_layers"] = sums
    query["first_matching_layer"] = sums[0] if sums else None
    atomic_text(BLOCKED_SMT2_PATH, solver.to_smt2())
    query["base_smt2_file"] = str(BASE_SMT2_PATH.relative_to(PROJECT_DIR))
    query["base_smt2_sha256"] = file_sha256(BASE_SMT2_PATH)
    query["blocked_smt2_file"] = str(BLOCKED_SMT2_PATH.relative_to(PROJECT_DIR))
    query["blocked_smt2_sha256"] = file_sha256(BLOCKED_SMT2_PATH)
    report["status"] = "complete"
    report["elapsed_seconds"] = round(time.monotonic() - started, 6)
    atomic_json(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
