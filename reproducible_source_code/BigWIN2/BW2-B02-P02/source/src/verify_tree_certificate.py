#!/usr/bin/env python3
"""Fail-closed verifier for the exact RESOCA-115 tree certificate.

The verifier parses a serialized certificate, checks all bound hashes, then
recomputes the finite audits with two independently implemented tree models
and two independently implemented direct orbit simulators.  These finite
checks audit the local lemmas; the all-parameter implication remains the
human proof in ``proof/tree_conjugacy_proof.md``.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


PROJECT = Path(__file__).resolve().parents[1]
SRC = PROJECT / "src"
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(SRC))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_keys(obj: dict[str, Any], expected: set[str], where: str) -> None:
    if set(obj) != expected:
        raise ValueError(
            f"{where}: keys differ: missing={sorted(expected-set(obj))}, "
            f"extra={sorted(set(obj)-expected)}"
        )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_and_validate(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("certificate root must be an object")
    exact_keys(
        data,
        {
            "schema_version",
            "task_id",
            "formal_statement",
            "mathematical_data",
            "audits",
            "even_depth_counts",
            "theorem_values_i_0_through_20",
            "bound_code_sha256",
            "interpretation",
        },
        "root",
    )
    require(data["schema_version"] == 1, "unsupported schema version")
    require(data["task_id"] == "02_resoca115_odd", "wrong task id")

    statement = data["formal_statement"]
    require(isinstance(statement, dict), "formal_statement must be an object")
    exact_keys(statement, {"path", "sha256"}, "formal_statement")
    require(statement["path"] == "problem/formal_statement.md", "wrong statement path")
    require(
        sha256(PROJECT / statement["path"]) == statement["sha256"],
        "formal statement hash mismatch",
    )

    math = data["mathematical_data"]
    require(isinstance(math, dict), "mathematical_data must be an object")
    exact_keys(
        math,
        {
            "wolfram_rule",
            "rule_table_wolfram_order_111_to_000",
            "background_site_symbols",
            "generator_by_phase",
            "exact_window",
            "window_length",
            "target_period",
        },
        "mathematical_data",
    )
    require(math["wolfram_rule"] == 115, "wrong Wolfram rule")
    derived_table = [(115 >> code) & 1 for code in range(7, -1, -1)]
    require(
        math["rule_table_wolfram_order_111_to_000"] == derived_table,
        "rule table does not derive from integer 115",
    )
    require(math["background_site_symbols"] == [0, 1, 2], "wrong background cycle")
    require(math["generator_by_phase"] == [1, 0, 2], "wrong generator order")
    require(math["exact_window"] == "[-k-1,k]", "wrong exact window")
    require(math["window_length"] == "N=2k+2", "wrong window length")
    require(
        math["target_period"] == "P(2i+1)=2^(4i+6)-1",
        "wrong target endpoint",
    )

    audits = data["audits"]
    require(isinstance(audits, dict), "audits must be an object")
    exact_keys(
        audits,
        {
            "primary_tree_exhaustive_max_depth",
            "independent_tree_exhaustive_max_depth",
            "normalized_local_inputs",
            "direct_first_return_odd_k",
        },
        "audits",
    )
    require(audits["primary_tree_exhaustive_max_depth"] == 12, "primary depth changed")
    require(audits["independent_tree_exhaustive_max_depth"] == 14, "independent depth changed")
    require(audits["normalized_local_inputs"] == 192, "local-input count changed")
    require(
        audits["direct_first_return_odd_k"]
        == {"1": 63, "3": 1023, "5": 16383, "7": 262143},
        "direct first-return cases changed",
    )

    hashes = data["bound_code_sha256"]
    require(isinstance(hashes, dict), "bound_code_sha256 must be an object")
    expected_paths = {
        "src/tree_model.py",
        "src/breaker_tree_audit.py",
        "src/referee_dense.py",
        "src/referee_bitpacked.py",
    }
    exact_keys(hashes, expected_paths, "bound_code_sha256")
    for relative, expected_hash in hashes.items():
        require(sha256(PROJECT / relative) == expected_hash, f"code hash mismatch: {relative}")

    values = data["theorem_values_i_0_through_20"]
    require(isinstance(values, list) and len(values) == 21, "need exactly i=0,...,20")
    require(
        values == [(1 << (4 * i + 6)) - 1 for i in range(21)],
        "theorem-value table does not equal the displayed formula",
    )
    return data


def recompute(data: dict[str, Any]) -> dict[str, Any]:
    import breaker_tree_audit
    import referee_bitpacked
    import referee_dense
    import tree_model

    audits = data["audits"]
    primary_depth = audits["primary_tree_exhaustive_max_depth"]
    tree_model.exhaustive_audit(primary_depth)

    independent_depth = audits["independent_tree_exhaustive_max_depth"]
    independent = breaker_tree_audit.run(independent_depth)
    require(independent["all_candidate_checks_pass"], "independent tree audit failed")
    require(
        independent["normalized_local_table_inputs_checked"] == 192,
        "independent local table did not cover 192 inputs",
    )
    require(
        independent["normalized_local_table_failures"] == [],
        "independent local table has failures",
    )

    expected_counts = data["even_depth_counts"]
    require(isinstance(expected_counts, dict), "even_depth_counts must be an object")
    exact_keys(expected_counts, {str(n) for n in range(2, 15, 2)}, "even_depth_counts")
    by_depth = {row["depth"]: row for row in independent["audits"]}
    for depth_text, expected in expected_counts.items():
        depth = int(depth_text)
        require(
            expected == {
                "vertices": ((1 << (depth + 2)) - 1) // 3,
                "phase_states": (1 << (depth + 2)) - 1,
            },
            f"bad serialized count at depth {depth}",
        )
        row = by_depth[depth]
        require(row["vertices"] == expected["vertices"], f"vertex count failed at {depth}")
        require(row["phase_states"] == expected["phase_states"], f"state count failed at {depth}")
        require(row["cycle_count"] == 1, f"not one cycle at depth {depth}")
        require(
            row["cycle_lengths"] == [expected["phase_states"]],
            f"wrong cycle length at depth {depth}",
        )

    direct_rows = []
    for k_text, expected in audits["direct_first_return_odd_k"].items():
        k = int(k_text)
        require(expected == (1 << (2 * k + 4)) - 1, f"bad target for k={k}")
        dense_period = referee_dense.exact_period(k, expected)
        packed_period = referee_bitpacked.exact_period_packed(k, expected)
        require(dense_period == expected, f"dense first return failed for k={k}")
        require(packed_period == expected, f"packed first return failed for k={k}")
        direct_rows.append({"k": k, "period": expected})

    return {
        "primary_tree_depth": primary_depth,
        "independent_tree_depth": independent_depth,
        "independent_vertices_at_max_depth": by_depth[independent_depth]["vertices"],
        "independent_phase_states_at_max_depth": by_depth[independent_depth]["phase_states"],
        "normalized_local_inputs": 192,
        "direct_first_returns": direct_rows,
    }


def main() -> int:
    certificate = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) == 2
        else PROJECT / "certificates" / "tree_certificate.json"
    )
    if len(sys.argv) > 2:
        print("usage: verify_tree_certificate.py [certificate.json]", file=sys.stderr)
        return 2
    try:
        data = load_and_validate(certificate)
        recomputed = recompute(data)
        output = {
            "status": "PASS",
            "certificate_sha256": sha256(certificate),
            "verifier_sha256": sha256(Path(__file__)),
            "bound_code_sha256": data["bound_code_sha256"],
            "recomputed": recomputed,
        }
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
