#!/usr/bin/env python3
"""Fail-closed submission audit for the sparse-core rank-ten manuscript."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audit" / "SPARSE_CORE_SUBMISSION_AUDIT.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load(relative: str):
    with (ROOT / relative).open(encoding="utf-8") as stream:
        return json.load(stream)


def main() -> None:
    checks: list[dict[str, object]] = []

    def check(name: str, condition: bool, detail: object = None) -> None:
        checks.append({"name": name, "pass": bool(condition), "detail": detail})

    source = ROOT / "paper_sparse_core" / "main.tex"
    bib = ROOT / "paper_sparse_core" / "references.bib"
    aux = ROOT / "paper_sparse_core" / "main.aux"
    log = ROOT / "paper_sparse_core" / "main.log"
    pdf = ROOT / "paper_sparse_core" / "main.pdf"
    tex = source.read_text(encoding="utf-8")
    bib_text = bib.read_text(encoding="utf-8")
    aux_text = aux.read_text(encoding="utf-8")
    log_text = log.read_text(encoding="utf-8", errors="replace")

    required_fragments = [
        "Sharp Rank--Order Bounds for Reduced Rank-Ten Graphs with Sparse Nonsingular Cores",
        "Yonghua Xiong\\textsuperscript{*}",
        "\\textsuperscript{*}Corresponding Author.",
        "at most eleven edges",
        "cores with twelve edges",
        "conjecture remains open",
        "2678",
        "719",
        "48,967,729",
        "41,704,342",
    ]
    for fragment in required_fragments:
        check(f"manuscript contains {fragment}", fragment in tex)

    cited: set[str] = set()
    for group in re.findall(r"\\cite\w*\{([^}]*)\}", tex):
        cited.update(key.strip() for key in group.split(",") if key.strip())
    bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib_text, flags=re.MULTILINE))
    aux_keys = set(re.findall(r"\\bibcite\{([^}]+)\}", aux_text))
    check("nine cited keys", len(cited) == 9, sorted(cited))
    check("nine bibliography keys", len(bib_keys) == 9, sorted(bib_keys))
    check("citation keys equal bibliography keys", cited == bib_keys)
    check("citation keys equal auxiliary keys", cited == aux_keys)

    forbidden_log_patterns = [
        r"Citation .* undefined",
        r"There were undefined",
        r"I didn't find a database entry",
        r"Warning--",
        r"Repeated entry",
        r"LaTeX Error",
        r"Fatal error",
        r"Emergency stop",
        r"Undefined control sequence",
        r"Runaway argument",
        r"Overfull",
        r"Underfull",
    ]
    log_hits = [p for p in forbidden_log_patterns if re.search(p, log_text)]
    check("clean LaTeX log", not log_hits, log_hits)

    expected = {
        "tree": ("work/builder/tree_core_exact_search.json", 106, 15),
        "unicyclic": ("work/builder/unicyclic_core_exact_search.json", 657, 136),
        "bicyclic": ("work/builder/bicyclic_core_exact_search.json", 2678, 719),
    }
    for family, (path, total, nonsingular) in expected.items():
        data = load(path)
        if family == "tree":
            got_total = data.get("free_tree_count_self_check")
        else:
            got_total = data.get("domain_stop")
        check(f"{family} builder full domain", got_total == total, got_total)
        check(
            f"{family} builder nonsingular count",
            data.get("nonsingular_tree_cores_processed", data.get("nonsingular_cores_processed"))
            == nonsingular,
        )
        check(f"{family} builder exact negative conclusion", data.get("counterexample_candidate_found") is False)

    audit_expectations = {
        "tree": ("work/linear_extension/tree_core_family_audit.json", 15, 760220),
        "unicyclic": ("work/linear_extension/unicyclic_core_family_audit.json", 136, 11600208),
        "bicyclic": ("work/linear_extension/bicyclic_core_family_audit.json", 719, 41704342),
    }
    for family, (path, nonsingular, calls) in audit_expectations.items():
        data = load(path)
        count = data.get("nonsingular_trees", data.get("nonsingular_cores"))
        check(f"{family} independent audit PASS", data.get("status") == "PASS")
        check(f"{family} independent nonsingular count", count == nonsingular, count)
        check(f"{family} independent search calls", data.get("independent_search_total_calls") == calls)
        check(f"{family} independent negative conclusion", data.get("counterexample_found") is False)

    attacks = load("work/builder/bicyclic_core_fail_closed_attacks.json")
    check("bicyclic fail-closed attacks all rejected", attacks.get("all_attacks_rejected") is True)
    check("five bicyclic fail-closed attacks", len(attacks.get("attacks", {})) == 5)

    doc_audit = load("work/linear_extension/bicyclic_core_theorem_checks.json")
    check(
        "theorem document audit 0/0/0",
        doc_audit.get("status") == "PASS"
        and (doc_audit.get("fatal"), doc_audit.get("major"), doc_audit.get("minor")) == (0, 0, 0),
    )
    sharp = load("certificates/standard_rank10_order62_bicyclic_core_verification.json")
    check("sharpness witness PASS", sharp.get("status") == "PASS")
    check("sharpness order/rank/reduced", (sharp.get("ambient_order"), sharp.get("ambient_rank"), sharp.get("ambient_reduced")) == (62, 10, True))
    check("sharpness bicyclic core", (sharp.get("core_order"), sharp.get("core_edge_count"), sharp.get("core_connected"), sharp.get("core_bicyclic"), sharp.get("core_determinant")) == (10, 11, True, True, -1))

    manifest = load("manifests/bicyclic_core_milestone.json")
    mismatches = []
    for relative, expected_hash in manifest.get("files", {}).items():
        path = ROOT / relative
        actual = sha256(path) if path.is_file() else None
        if actual != expected_hash:
            mismatches.append({"path": relative, "expected": expected_hash, "actual": actual})
    check("milestone manifest hashes", not mismatches, mismatches)
    manifest_hash = sha256(ROOT / "manifests" / "bicyclic_core_milestone.json")
    check("manuscript binds milestone manifest", manifest_hash in tex, manifest_hash)

    reader = PdfReader(str(pdf))
    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    check("PDF has seven pages", len(reader.pages) == 7, len(reader.pages))
    check("PDF title text", "sharp rank–order bounds" in pdf_text.casefold() or "sharp rank--order bounds" in pdf_text.casefold())
    check("PDF corresponding-author text", "Corresponding Author" in pdf_text)
    check("PDF states unrestricted problem remains open", "conjecture remains open" in pdf_text)

    failures = [item for item in checks if not item["pass"]]
    report = {
        "schema_version": 1,
        "status": "PASS" if not failures else "FAIL",
        "fatal": len(failures),
        "major": 0,
        "minor": 0,
        "scope": "submission audit for the sharp sparse-core partial theorem; not the unrestricted rank-ten conjecture",
        "paper": str(source.relative_to(ROOT)),
        "paper_sha256": sha256(source),
        "pdf": str(pdf.relative_to(ROOT)),
        "pdf_sha256": sha256(pdf),
        "pdf_pages": len(reader.pages),
        "bibliography": str(bib.relative_to(ROOT)),
        "bibliography_sha256": sha256(bib),
        "milestone_manifest_sha256": manifest_hash,
        "checks": checks,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "checks": len(checks), "failures": failures}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
