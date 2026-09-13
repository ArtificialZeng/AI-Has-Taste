#!/usr/bin/env python3
"""Targeted mutations for the star1 builder verifier and independent audit."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import platform
import subprocess
import sys
import tempfile
from pathlib import Path


def row_digest(rows):
    return hashlib.sha256(json.dumps(rows, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    certificate_path = root / "certificates/star1_exact_certificate.json"
    builder_verifier = root / "src/builder_verify_star1.py"
    audit = root / "src/breaker_star1_audit.py"
    source_text = certificate_path.read_text(encoding="utf-8")
    source = json.loads(source_text)

    # expected tuple: builder verifier accepts?, independent audit accepts?
    cases = [("valid", source, (True, True))]

    duplicate_schema = source_text.replace(
        "{", '{"schema":"q5-star1-exact-v1",', 1
    )
    cases.append(("duplicate_top_level_schema_key", duplicate_schema, (False, False)))

    changed = copy.deepcopy(source)
    changed["bernstein"]["rows"][1], changed["bernstein"]["rows"][2] = changed["bernstein"]["rows"][2], changed["bernstein"]["rows"][1]
    changed["bernstein"]["rows_sha256"] = row_digest(changed["bernstein"]["rows"])
    cases.append(("reordered_bernstein_rows_refreshed_digest", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["residual_necessary_ideal"]["resultant_u"]["content"] = [2048, 2]
    cases.append(("noncanonical_resultant_content", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["surviving_component"]["w"] = False
    cases.append(("boolean_surviving_w", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["hessian"]["symmetry_dimensions"]["large_block"] = True
    cases.append(("boolean_symmetry_dimension", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["chart"]["pair_margins"].pop()
    cases.append(("deleted_pair_wall", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["chart"]["pair_margins"][0]["kind"] = "low"
    cases.append(("flipped_high_pair_kind", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["bernstein"]["rows"][9]["terms_u_w"][0][-2] += 1
    changed["bernstein"]["rows_sha256"] = row_digest(changed["bernstein"]["rows"])
    cases.append(("changed_bernstein_coefficient_refreshed_digest", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["residual_necessary_ideal"]["B"][0][-2] += 1
    cases.append(("changed_residual_B", changed, (False, False)))

    changed = copy.deepcopy(source)
    changed["hessian"]["reduced_quadratic_forms_mod_13alpha2-48alpha+39"]["small_block"]["linear_numerator_ascending"][1] += 1
    cases.append(("changed_hessian_form", changed, (False, False)))

    results = []
    with tempfile.TemporaryDirectory(prefix="star1-audit-mutations-") as directory:
        directory_path = Path(directory)
        for index, (name, payload, expected) in enumerate(cases):
            path = directory_path / f"{index:02d}-{name}.json"
            audit_output = directory_path / f"{index:02d}-{name}-audit.json"
            path.write_text(payload if isinstance(payload, str) else json.dumps(payload, sort_keys=True), encoding="utf-8")
            builder = subprocess.run([sys.executable, str(builder_verifier), str(path)], text=True, capture_output=True, check=False)
            independent = subprocess.run(
                [sys.executable, str(audit), str(path), "--output", str(audit_output), "--random-checks", "2", "--seed", str(140120260829+index)],
                text=True, capture_output=True, check=False,
            )
            observed = (builder.returncode == 0, independent.returncode == 0)
            results.append({
                "name": name,
                "expected_builder_accept": expected[0],
                "observed_builder_accept": observed[0],
                "expected_independent_accept": expected[1],
                "observed_independent_accept": observed[1],
                "builder_message": (builder.stdout or builder.stderr).strip()[:240],
                "independent_message": (independent.stdout or independent.stderr).strip()[:240],
            })

    passed = all(
        (row["observed_builder_accept"], row["observed_independent_accept"])
        == (row["expected_builder_accept"], row["expected_independent_accept"])
        for row in results
    )
    output = {
        "status": "PASS" if passed else "FAIL",
        "python": platform.python_version(),
        "builder_fail_closed_repairs_verified": [
            "duplicate JSON object keys are rejected",
            "Bernstein row order is canonicalized",
            "resultant content rational must be reduced",
            "False is rejected where survivor w must be integer zero",
            "True is rejected where a symmetry dimension must be an integer",
        ],
        "tests": results,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
