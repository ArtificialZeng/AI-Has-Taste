#!/opt/anaconda3/bin/python3
"""Mutation tests for builder_verify_star1.py."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: builder_test_star1_mutations.py VERIFIER.py CERTIFICATE.json", file=sys.stderr)
        return 2
    verifier = Path(sys.argv[1]).resolve()
    certificate_path = Path(sys.argv[2]).resolve()
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))

    baseline = subprocess.run(
        [sys.executable, str(verifier), str(certificate_path)],
        text=True,
        capture_output=True,
        check=False,
    )
    if baseline.returncode != 0:
        print("FAIL: valid certificate was rejected", baseline.stderr, file=sys.stderr)
        return 1

    mutations = []

    changed_metadata = copy.deepcopy(certificate)
    changed_metadata["chamber"] = "N={} ordered closure"
    mutations.append(("semantic chamber metadata", changed_metadata))

    changed_equation = copy.deepcopy(certificate)
    changed_equation["critical_equations"]["combination"][0] += 1
    mutations.append(("critical-equation combination", changed_equation))

    changed_hash = copy.deepcopy(certificate)
    changed_hash["bernstein"]["rows_sha256"] = "0" * 64
    mutations.append(("Bernstein table hash", changed_hash))

    changed_bernstein = copy.deepcopy(certificate)
    changed_bernstein["bernstein"]["rows"][1]["terms_u_w"][0][-2] += 1
    rows_blob = json.dumps(
        changed_bernstein["bernstein"]["rows"], separators=(",", ":"), sort_keys=True
    ).encode()
    changed_bernstein["bernstein"]["rows_sha256"] = hashlib.sha256(rows_blob).hexdigest()
    mutations.append(("positive Bernstein coefficient with refreshed digest", changed_bernstein))

    changed_component = copy.deepcopy(certificate)
    changed_component["residual_necessary_ideal"]["components"][1]["u_factor"][0][-2] += 1
    mutations.append(("component polynomial", changed_component))

    changed_resultant = copy.deepcopy(certificate)
    changed_resultant["residual_necessary_ideal"]["resultant_u"]["factors"][4][
        "polynomial_w"
    ][-1][-2] += 2
    mutations.append(("resultant factor", changed_resultant))

    changed_endpoint = copy.deepcopy(certificate)
    changed_endpoint["surviving_component"]["alpha_isolating_interval"][0] = [2, 1]
    mutations.append(("algebraic isolating interval", changed_endpoint))

    changed_hessian = copy.deepcopy(certificate)
    changed_hessian["hessian"]["reduced_quadratic_forms_mod_13alpha2-48alpha+39"][
        "block_contrast"
    ]["linear_numerator_ascending"][1] += 1
    mutations.append(("Hessian exact quadratic form", changed_hessian))

    dropped_margin = copy.deepcopy(certificate)
    dropped_margin["chart"]["pair_margins"].pop()
    mutations.append(("deleted chamber margin", dropped_margin))

    with tempfile.TemporaryDirectory(prefix="star1_mutation_") as temporary:
        temporary_path = Path(temporary)
        for index, (name, mutated) in enumerate(mutations):
            path = temporary_path / f"mutation_{index}.json"
            path.write_text(json.dumps(mutated, sort_keys=True), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(verifier), str(path)],
                text=True,
                capture_output=True,
                check=False,
            )
            if result.returncode == 0 or "REJECT:" not in result.stderr:
                print(f"FAIL: mutation accepted: {name}", file=sys.stderr)
                return 1
            print(f"PASS mutation rejected: {name}")
    print(f"PASS: all {len(mutations)} mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
