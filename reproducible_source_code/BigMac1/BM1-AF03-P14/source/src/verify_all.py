#!/usr/bin/env python3
"""Run every decisive exact verifier and its corruption tests, fail closed."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PY = Path("/opt/anaconda3/bin/python3")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not PY.is_file():
        print(f"FAIL: required exact-arithmetic interpreter missing: {PY}", file=sys.stderr)
        return 1

    commands = [
        ("formula reconstruction", [PY, "src/builder_verify_formulas.py"]),
        (
            "Q3 classification",
            [PY, "src/verify_q3_classification.py", "results/q3_classification_certificate.json"],
        ),
        ("Q3 classification mutations", [PY, "tests/test_q3_verifier.py"]),
        (
            "Q4 certificate",
            [PY, "src/breaker_verify_q4_baseline.py", "results/breaker_q4_baseline_certificate.json"],
        ),
        (
            "Q5 saddle certificate",
            [PY, "src/breaker_verify_saddle.py", "results/breaker_saddle_certificate.json"],
        ),
        (
            "Q4/Q5 saddle mutations",
            [PY, "src/breaker_test_verifiers.py", "--output", "audit/saddle_mutation_log.json"],
        ),
        (
            "empty chamber",
            [PY, "src/verify_empty_highpair_classification.py", "results/empty_highpair_classification_certificate.json"],
        ),
        ("empty chamber mutations", [PY, "tests/test_empty_highpair_verifier.py"]),
        (
            "star1 chamber",
            [PY, "src/builder_verify_star1.py", "certificates/star1_exact_certificate.json"],
        ),
        (
            "star1 mutations",
            [
                PY,
                "src/builder_test_star1_mutations.py",
                "src/builder_verify_star1.py",
                "certificates/star1_exact_certificate.json",
            ],
        ),
        (
            "star1 independent audit",
            [
                PY,
                "src/breaker_star1_audit.py",
                "certificates/star1_exact_certificate.json",
                "--output",
                "audit/star1_independent_audit.json",
            ],
        ),
        (
            "star1 independent-audit mutations",
            [
                PY,
                "src/breaker_star1_audit_tests.py",
                "--output",
                "audit/star1_audit_mutations.json",
            ],
        ),
        (
            "star2 chamber",
            [PY, "src/verify_star2_bernstein.py", "results/star2_bernstein_no_go_certificate.json"],
        ),
        ("star2 mutations", [PY, "tests/test_star2_bernstein_verifier.py"]),
        (
            "star2 independent audit",
            [
                PY,
                "src/breaker_star2_audit.py",
                "results/star2_bernstein_no_go_certificate.json",
                "--output",
                "audit/star2_independent_audit.json",
            ],
        ),
        (
            "star2 independent-audit mutations",
            [PY, "src/breaker_star2_audit_tests.py", "--output", "audit/star2_audit_mutations.json"],
        ),
        ("star3 chamber and mutations", [PY, "src/builder_verify_star3.py"]),
        (
            "star4 chamber",
            [PY, "src/breaker_star4_verify.py", "results/breaker_star4_certificate.json"],
        ),
        (
            "star4 mutations",
            [PY, "src/breaker_star4_test.py", "--output", "audit/star4_mutation_log.json"],
        ),
        (
            "triangle chamber",
            [PY, "src/verify_triangle_highpair_no_go.py", "results/triangle_highpair_no_go_certificate.json"],
        ),
        ("triangle mutations", [PY, "tests/test_triangle_highpair_verifier.py"]),
        (
            "non-star1 canonical JSON attacks",
            [PY, "tests/test_nonstar1_json_failclosed.py"],
        ),
        (
            "independent referee parser attacks",
            [PY, "audit/independent_referee/test_parser_failclosed.py"],
        ),
    ]

    records = []
    failed = False
    for name, command in commands:
        result = subprocess.run(
            [str(item) for item in command],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            timeout=300,
        )
        record = {
            "name": name,
            "command": [str(item) for item in command],
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
        records.append(record)
        status = "PASS" if result.returncode == 0 else "FAIL"
        print(f"{status}: {name}")
        if result.returncode != 0:
            failed = True
            break

    certificate_paths = [
        "results/breaker_q4_baseline_certificate.json",
        "results/q3_classification_certificate.json",
        "results/breaker_saddle_certificate.json",
        "results/empty_highpair_classification_certificate.json",
        "certificates/star1_exact_certificate.json",
        "results/star2_bernstein_no_go_certificate.json",
        "certificates/star3_decomposition.json",
        "results/breaker_star4_certificate.json",
        "results/triangle_highpair_no_go_certificate.json",
    ]
    payload = {
        "schema": "q5-master-verification-v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "status": "FAIL" if failed else "PASS",
        "python": str(PY),
        "singular_required": True,
        "certificates_sha256": {
            path: sha256(ROOT / path) for path in certificate_paths
        },
        "checks": records,
    }
    output = ROOT / "audit" / "verification_log.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
