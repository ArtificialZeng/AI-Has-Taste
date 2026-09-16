#!/usr/bin/env python3
"""Freeze the exact candidate scope and enumerate every decisive file."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    fixed = [
        "source.md",
        "problem.md",
        "evidence/external/2609.05259.pdf",
        "evidence/external/2609.05259.txt",
        "evidence/disproof.md",
        "evidence/census_generation.md",
        "evidence/census_completeness.md",
        "evidence/census_verification.json",
        "evidence/census_regeneration.json",
        "evidence/independent_census.json",
        "evidence/coloring_sweep_summary.json",
        "evidence/coloring_witnesses.jsonl",
        "evidence/witness_verification.json",
        "evidence/unsat_certification.json",
        "evidence/resolution_audit.json",
        "evidence/cnf_binding_verification.json",
        "evidence/second_encoding_verification.json",
        "evidence/second_encoding_replay.json",
        "evidence/final_verification.json",
        "evidence/scripts/verify_census.py",
        "evidence/scripts/regenerate_census.py",
        "evidence/scripts/canonical_small.c",
        "evidence/scripts/labeled_cubic_count.py",
        "evidence/scripts/independent_census.py",
        "evidence/scripts/sweep_colorings.py",
        "evidence/scripts/verify_witnesses.py",
        "evidence/scripts/certify_unsat.py",
        "evidence/scripts/audit_resolution.py",
        "evidence/scripts/check_cnf_bindings.py",
        "evidence/scripts/second_encoding.py",
        "evidence/scripts/verify_second_encoding.py",
        "evidence/scripts/final_verify.py",
        "tools/drat-trim.c",
        "tools/drat-trim",
        "tools/build_geng.sh",
        "tools/build_checkers.sh",
        "tools/nauty-root/geng",
        "tools/canonical_small",
    ]
    fixed += [f"census/n{n:02d}.g6" for n in (4, 6, 8, 10, 12, 14, 16, 18)]
    fixed += [f"evidence/logs/geng_n{n:02d}.stderr" for n in (4, 6, 8, 10, 12, 14, 16, 18)]
    fixed += [f"evidence/canonical_n{n:02d}.tsv" for n in (4, 6, 8, 10, 12, 14, 16, 18)]
    fixed += [str(path.relative_to(ROOT)) for path in sorted((ROOT / "tools" / "nauty-objects").glob("*.o"))]
    fixed += [str(path.relative_to(ROOT)) for path in sorted((ROOT / "evidence" / "unsat").glob("*/*"))]
    fixed += [
        str(path.relative_to(ROOT))
        for path in sorted((ROOT / "evidence" / "second_encoding").glob("*"))
        if path.suffix in {".cnf", ".drat"}
    ]
    assert len(fixed) == len(set(fixed))
    assert all((ROOT / path).is_file() for path in fixed)
    claim = {
        "kind": "resolution-paper",
        "original_status": "disproved",
        "statement": (
            "The frozen assertion is false. Among connected simple cubic graphs of order below 20, "
            "the minimum order of a Type 1 graph with no equitable proper 4-total coloring is 16; "
            "there are exactly 16 such isomorphism classes at that least order, with the canonical "
            "graph6 codes listed in evidence/disproof.md."
        ),
        "contribution": (
            "An independently completeness-checked census contains all 45,982 connected cubic "
            "isomorphism classes below order 20. Exhaustive classification through order 16, "
            "4,368 directly checked positive colorings, and replayed DRAT certificates prove that "
            "the first failures occur at order 16 and classify all 16 least-order counterexamples."
        ),
        "proposer_job_id": "win-00068-p02-research-5cb899a40f40",
        "evidence_files": fixed,
    }
    (ROOT / "claim.json").write_text(json.dumps(claim, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"evidence_files": len(fixed), "kind": claim["kind"], "original_status": claim["original_status"]}))


if __name__ == "__main__":
    main()
