#!/usr/bin/env python3
"""Create a deterministic SHA-256 manifest for the sparse-core submission."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "manifests" / "sparse_core_submission_manifest.json"

FILES = [
    "paper_sparse_core/main.tex",
    "paper_sparse_core/references.bib",
    "paper_sparse_core/main.bbl",
    "output/pdf/reduced_graph_rank10_sparse_core.pdf",
    "proof/tree_core_theorem.md",
    "proof/unicyclic_core_theorem.md",
    "proof/bicyclic_core_theorem.md",
    "src/builder_tree_core_search.py",
    "src/builder_verify_tree_core_search.py",
    "src/linear_verify_tree_core_family.py",
    "src/builder_attack_tree_core_certificate.py",
    "src/builder_unicyclic_core_search.py",
    "src/linear_verify_unicyclic_core_family.py",
    "src/builder_attack_unicyclic_core_certificate.py",
    "src/builder_bicyclic_core_search.py",
    "src/linear_verify_bicyclic_core_family.py",
    "src/builder_attack_bicyclic_core_certificate.py",
    "src/verify_bicyclic_sharpness.py",
    "src/audit_bicyclic_core_theorem_doc.py",
    "src/audit_sparse_core_submission.py",
    "src/build_sparse_core_submission_manifest.py",
    "work/builder/tree_core_exact_search.json",
    "work/builder/tree_core_exact_search_verify.json",
    "work/linear_extension/tree_core_family_audit.json",
    "work/builder/tree_core_fail_closed_attacks.json",
    "work/linear_extension/tree_core_theorem_audit.md",
    "work/builder/unicyclic_core_exact_search.json",
    "work/linear_extension/unicyclic_core_family_audit.json",
    "work/builder/unicyclic_core_fail_closed_attacks.json",
    "work/linear_extension/unicyclic_core_theorem_audit.md",
    "work/builder/bicyclic_core_exact_search.json",
    "work/linear_extension/bicyclic_core_family_audit.json",
    "work/builder/bicyclic_core_fail_closed_attacks.json",
    "work/linear_extension/bicyclic_core_theorem_checks.json",
    "work/linear_extension/bicyclic_core_theorem_audit.md",
    "certificates/standard_rank10_order62.json",
    "certificates/standard_rank10_order62_verification.json",
    "certificates/standard_rank10_order62_unicyclic_core.json",
    "certificates/standard_rank10_order62_unicyclic_core_verification.json",
    "certificates/standard_rank10_order62_bicyclic_core.json",
    "certificates/standard_rank10_order62_bicyclic_core_verification.json",
    "manifests/unicyclic_core_milestone.json",
    "manifests/bicyclic_core_milestone.json",
    "audit/SPARSE_CORE_SUBMISSION_AUDIT.json",
    "audit/SPARSE_CORE_SUBMISSION_AUDIT.md",
    "literature/sparse_core_bib_audit.md",
    "CLAIM_LEDGER.md",
    "APPROACH_REGISTRY.md",
    "COUNTEREXAMPLE_DB.md",
    "proof/gap_ledger.md",
    "proof/proof_dag.md",
    "research_state.json",
    "routes/registry.json",
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    missing = [relative for relative in FILES if not (ROOT / relative).is_file()]
    if missing:
        raise FileNotFoundError(f"missing submission files: {missing}")
    payload = {
        "schema_version": 1,
        "created_utc": "2026-08-27T00:00:00Z",
        "title": "Sharp Rank--Order Bounds for Reduced Rank-Ten Graphs with Sparse Nonsingular Cores",
        "scientific_status": "submission-ready sharp partial theorem; unrestricted rank-ten conjecture remains open",
        "files": {relative: digest(ROOT / relative) for relative in FILES},
    }
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(FILES)} bound files")


if __name__ == "__main__":
    main()
