#!/usr/bin/env python3
"""Independent fail-closed referee for the Q5 paper-only release delta.

This program intentionally imports only the Python standard library and never
imports a project verifier, certificate builder, or discovery module.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


EXPECTED = {
    "paper/main.tex": "1bcccfa9a6db0660c1e3d349351ad4740ea7f9ea5b90e050701c94bb7f19bd58",
    "proof/main_proof.md": "1d53b2d70c0ee37e306929414e3c7d4b84baaa7469868c204bcf4a4fa03ea85f",
    "audit/independent_referee/frozen_inputs.json": "af44b6d7739996eab1726eaca41f3078aa1b9efd20cb78cc8ca0e5efbcd375e5",
    "src/verify_all.py": "b781d39f0b89fda14a8969458d098942569d0ad191103546d8904ec4566bc1a2",
    "audit/verification_log.json": "18f6a4fb55480a3d097d6b96b2d69fa7497f4e7ccf88b689083b267139de4903",
    "audit/independent_referee/independent_verifier.py": "e6ce6ac216afa419442acc9cb6cce3dd256826a5ab28f9262bfd9e5fba5ab73d",
    "audit/independent_referee/verification_result.json": "333821801a789688976abea57f6d76475f4b6c8eb955e4a6008ca4983289ff6b",
    "paper/references.bib": "dcba8a3ac13a247390162d618a422ea07ecfa80d38dc3589b271936299789d6b",
    "audit/CITATION_AUDIT.md": "ebb7dae6b0baaf260e29e995b629491e945ad0e08b09e521b67efe82ca726468",
    "audit/BIB_AUDIT.md": "c6a6f2f619d14f9fc76c777b45d0d1f575610f9d3fdc9110ed8142f32338dd22",
    "literature/claim_ledger.md": "231d4287d95437fdc234dc48ebe5c8a926033561fafdd70b2a82b02d753f98e5",
    "literature/search_log.md": "5eac1815c990d42789caea0d80e6880e49c0ffee98b8c7b6269cf46b356c6b22",
}

PRIOR_PAPER_SHA256 = "1f2237109932b4b017e9d017187923b8d0f79a0ab2b1f93384ce8e53f217556a"
MAIN_THEOREM_SHA256 = "75046013b842548e5de654d036692510b3dc5007cc97f44da8dc59edb436bea9"
FULL_SUPPORT_THEOREM_SHA256 = "49e81a712de7111366f43ab5ab7c7cfbee391a63134cccedfc4d00048c1db701"

CERTIFICATES = {
    "results/empty_highpair_classification_certificate.json": "3d5c97a23ad36956387e4ddbdaca0f74720953f34a59af422ed15944b23e1e6a",
    "certificates/star1_exact_certificate.json": "70cf7f980c89ff36e6b07ccecde268bcde6d8cf5f9da171759b5d8ba5c0e3fa7",
    "results/star2_bernstein_no_go_certificate.json": "fd591e360a57668ad818ba8adb8e48d5670a211da3f43528c7f3f68517310a80",
    "certificates/star3_decomposition.json": "f966e220261ffc316d37aaac9522e0484e2b931792c5fe985aae351052254024",
    "results/breaker_star4_certificate.json": "b57cad6aeea0d3db3ac39999bfbdcdcacd48c36d5b2de4883e6806a080bfc935",
    "results/triangle_highpair_no_go_certificate.json": "5e0bab27d028cdfc65027c3c346d3f0397dd13a623b1bf7782616823019278a1",
    "results/q3_classification_certificate.json": "6f704264551c322228d9af0fffcd03e7ae5071be2ddbe04d0f54ed583cb8db28",
    "results/breaker_q4_baseline_certificate.json": "1c732a3b4c95b2bd743a05248dff841457ec11cdd70c76a96435dffb89a86c15",
    "results/breaker_saddle_certificate.json": "6bac02ad20ab063e8db1bbe8f79d1495dcb3134788f43b760ad119131872d03a",
}

EXPECTED_CITE_KEYS = {
    "Ball1986",
    "Ambrus2022",
    "AmbrusGargyan2024",
    "AmbrusGargyan2025",
    "Pournin2025Erratum",
}

EXPECTED_MASTER_NAMES = [
    "formula reconstruction",
    "Q3 classification",
    "Q3 classification mutations",
    "Q4 certificate",
    "Q5 saddle certificate",
    "Q4/Q5 saddle mutations",
    "empty chamber",
    "empty chamber mutations",
    "star1 chamber",
    "star1 mutations",
    "star1 independent audit",
    "star1 independent-audit mutations",
    "star2 chamber",
    "star2 mutations",
    "star2 independent audit",
    "star2 independent-audit mutations",
    "star3 chamber and mutations",
    "star4 chamber",
    "star4 mutations",
    "triangle chamber",
    "triangle mutations",
    "non-star1 canonical JSON attacks",
    "independent referee parser attacks",
]


class RefereeFailure(Exception):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    if not path.is_file():
        raise RefereeFailure(f"missing file: {path}")
    return sha256_bytes(path.read_bytes())


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise RefereeFailure(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RefereeFailure(f"cannot parse {path}: {exc}") from exc


def exact_int(value: Any, label: str) -> int:
    if type(value) is not int:  # bool is deliberately rejected
        raise RefereeFailure(f"{label}: expected canonical integer")
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RefereeFailure(message)


def extract_block(text: str, start: str, end: str) -> str:
    require(text.count(start) == 1, f"non-unique block start: {start}")
    begin = text.index(start)
    finish = text.find(end, begin)
    require(finish >= 0, f"missing block end after {start}")
    return text[begin : finish + len(end)]


def reverse_paper_delta(paper: str) -> str:
    current_c01 = (
        "Ambrus and G\\'argy\\'an conjectured that, for every $n\\geq2$, every locally\n"
        "extremal central section of $Q_n$ is diagonal\n"
        "\\cite[Conjecture~1.3]{AmbrusGargyan2024}.  They also\n"
    )
    prior_c01 = (
        "Ambrus and G\\'argy\\'an conjectured that every locally extremal central section\n"
        "of a cube is diagonal \\cite[Conjecture~1.3]{AmbrusGargyan2024}.  They also\n"
    )
    current_correction = (
        "The status of diagonal sections itself requires care.  Ambrus and\n"
        "G\\'argy\\'an proved that, for $n\\geq4$, $d_k$ is not locally extremal when\n"
        "$3\\leq k\\leq n-1$ \\cite{AmbrusGargyan2025}.  Pournin's erratum corrects an\n"
        "omitted transverse term in the constrained-Hessian criterion for proper\n"
        "subdiagonals and explicitly leaves the main-diagonal conclusions unchanged\n"
        "\\cite{Pournin2025Erratum}.  The sharp global upper bound is Ball's cube\n"
    )
    prior_correction = (
        "The status of diagonal sections itself requires care.  A corrected result of\n"
        "Ambrus and G\\'argy\\'an shows that $d_k$ is not locally extremal when\n"
        "$3\\leq k\\leq n-1$ \\cite{AmbrusGargyan2025}; the correction addresses a\n"
        "missing Hessian term identified in Pournin's erratum\n"
        "\\cite{Pournin2025Erratum}.  The sharp global upper bound is Ball's cube\n"
    )
    require(paper.count("\\date{August 30, 2026}") == 1, "release date is absent or duplicated")
    require("\\date{August 29, 2026}" not in paper, "stale release date remains")
    require(paper.count(current_c01) == 1, "Conjecture 1.3 delta is absent or duplicated")
    require(paper.count(current_correction) == 1, "AG25/Pournin delta is absent or duplicated")
    reversed_text = paper.replace("\\date{August 30, 2026}", "\\date{August 29, 2026}")
    reversed_text = reversed_text.replace(current_c01, prior_c01)
    reversed_text = reversed_text.replace(current_correction, prior_correction)
    return reversed_text


def audit(root: Path) -> dict[str, Any]:
    for relative, expected_hash in EXPECTED.items():
        got = sha256_file(root / relative)
        require(got == expected_hash, f"hash mismatch: {relative}: {got}")

    binding = load_json(root / "audit/independent_referee/frozen_inputs.json")
    require(binding.get("schema") == "q5-independent-referee-binding-v1", "wrong binding schema")
    entries = binding.get("inputs")
    require(type(entries) is list and len(entries) == 17, "binding must contain exactly 17 inputs")
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, entry in enumerate(entries):
        require(type(entry) is dict, f"binding input {index}: expected object")
        require(set(entry) == {"id", "path", "sha256", "kind"}, f"binding input {index}: wrong schema")
        item_id = entry["id"]
        relative = entry["path"]
        claimed_hash = entry["sha256"]
        require(type(item_id) is str and item_id not in seen_ids, f"duplicate/invalid binding id: {item_id}")
        require(type(relative) is str and relative not in seen_paths, f"duplicate/invalid binding path: {relative}")
        relative_path = Path(relative)
        require(not relative_path.is_absolute() and ".." not in relative_path.parts, f"unsafe binding path: {relative}")
        require(type(claimed_hash) is str and re.fullmatch(r"[0-9a-f]{64}", claimed_hash) is not None,
                f"invalid binding hash: {relative}")
        require(sha256_file(root / relative_path) == claimed_hash, f"bound input mismatch: {relative}")
        seen_ids.add(item_id)
        seen_paths.add(relative)
    require(
        next(x for x in entries if x["id"] == "paper_claim_map")["sha256"] == EXPECTED["paper/main.tex"],
        "binding does not name the current paper",
    )
    require(
        next(x for x in entries if x["id"] == "main_proof")["sha256"] == EXPECTED["proof/main_proof.md"],
        "binding does not name the frozen proof",
    )

    paper = (root / "paper/main.tex").read_text(encoding="utf-8")
    reversed_paper = reverse_paper_delta(paper)
    require(sha256_bytes(reversed_paper.encode("utf-8")) == PRIOR_PAPER_SHA256,
            "paper contains changes outside the authorized release delta")

    main_theorem = extract_block(paper, "\\begin{theorem}\\label{thm:main}", "\\end{theorem}")
    full_theorem = extract_block(
        paper,
        "\\begin{theorem}[full-support critical set]\\label{thm:fullsupport}",
        "\\end{theorem}",
    )
    require(sha256_bytes(main_theorem.encode("utf-8")) == MAIN_THEOREM_SHA256, "main theorem block changed")
    require(sha256_bytes(full_theorem.encode("utf-8")) == FULL_SUPPORT_THEOREM_SHA256,
            "full-support theorem block changed")

    table = extract_block(paper, "\\begin{table}[ht]", "\\end{table}")
    q3_row = "$Q_3$ support & \\texttt{6f704264} & resultant and positivity \\\\"
    require(table.count(q3_row) == 1, "Q3 certificate table row is missing or duplicated")
    endpoint_rows = [line.strip() for line in table.splitlines() if " & " in line and line.strip().endswith("\\\\")]
    require(len(endpoint_rows) == 9, "certificate table must have one header and eight endpoint rows")
    require(len(set(endpoint_rows)) == len(endpoint_rows), "certificate table has a duplicate row")

    for relative, expected_hash in CERTIFICATES.items():
        require(sha256_file(root / relative) == expected_hash, f"certificate changed: {relative}")

    master = load_json(root / "audit/verification_log.json")
    require(master.get("status") == "PASS", "master log is not PASS")
    checks = master.get("checks")
    require(type(checks) is list and len(checks) == 23, "master log must contain 23 checks")
    require([item.get("name") for item in checks] == EXPECTED_MASTER_NAMES, "master check list/order changed")
    for item in checks:
        require(type(item) is dict, "master check must be an object")
        require(exact_int(item.get("returncode"), f"master returncode {item.get('name')}") == 0,
                f"master check failed: {item.get('name')}")

    independent = load_json(root / "audit/independent_referee/verification_result.json")
    require(independent.get("status") == "PASS", "independent result is not PASS")
    require(independent.get("binding_sha256") == EXPECTED["audit/independent_referee/frozen_inputs.json"],
            "independent result binding mismatch")
    require(independent.get("verifier_sha256") == EXPECTED["audit/independent_referee/independent_verifier.py"],
            "independent result verifier mismatch")
    independent_binding = independent.get("results", {}).get("binding", {})
    require(exact_int(independent_binding.get("inputs"), "independent bound-input count") == 17,
            "independent result input count changed")
    require(independent_binding.get("hashes_enforced") is True, "independent hashes are not enforced")

    cite_keys: set[str] = set()
    for match in re.finditer(r"\\cite\w*(?:\[[^\]]*\])?\{([^}]*)\}", paper):
        cite_keys.update(key.strip() for key in match.group(1).split(","))
    bibliography = (root / "paper/references.bib").read_text(encoding="utf-8")
    bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bibliography, re.MULTILINE))
    require(cite_keys == EXPECTED_CITE_KEYS, f"unexpected citation surface: {sorted(cite_keys)}")
    require(bib_keys == EXPECTED_CITE_KEYS, f"unexpected bibliography surface: {sorted(bib_keys)}")

    citation_audit = (root / "audit/CITATION_AUDIT.md").read_text(encoding="utf-8")
    pass_one = citation_audit.split("## Pass 2", 1)[0]
    claim_ids = re.findall(r"^\| (C\d\d) \|", pass_one, re.MULTILINE)
    require(claim_ids == [f"C{i:02d}" for i in range(1, 12)], "citation audit is not frozen at C01--C11")
    require("| Total frozen claims | 11 |" in citation_audit, "citation audit total changed")
    require("| Verified in the final manuscript | 11 |" in citation_audit, "not all claims are verified")
    require("| Unverified | 0 |" in citation_audit, "citation audit has an unverified claim")

    require("Release-phase novelty rerun — 2026-08-30" in (root / "literature/search_log.md").read_text(encoding="utf-8"),
            "release novelty rerun is missing")
    require("The database-bounded literature search recorded with this manuscript found no" in paper,
            "paper novelty wording is not database-bounded")

    return {
        "binding_inputs": 17,
        "master_checks": 23,
        "independent_inputs": 17,
        "bibtex_keys": 5,
        "claims": 11,
        "certificates": len(CERTIFICATES),
        "q3_table_rows": 1,
        "prior_paper_reconstructed": True,
        "theorem_changed": False,
        "proof_changed": False,
        "certificate_changed": False,
    }


def make_outputs(root: Path, details: dict[str, Any], findings: list[dict[str, str]]) -> tuple[str, str]:
    counts = {name: 0 for name in ("fatal", "major", "local", "expository")}
    for finding in findings:
        counts[finding["severity"]] += 1
    status = "PASS" if not findings else "FAIL"
    script_hash = sha256_file(Path(__file__).resolve())
    report = f"""# Release-delta hostile referee report

Date: 2026-08-30 (Asia/Shanghai)  
Mode: independent standard-library CLI; no project imports  
Verdict: **{status}**  
Submission-gate delta: **{status}**

## Finding counts

| fatal | major | local | expository |
|---:|---:|---:|---:|
| {counts['fatal']} | {counts['major']} | {counts['local']} | {counts['expository']} |

## Bound release inputs

```text
{EXPECTED['paper/main.tex']}  paper/main.tex
{EXPECTED['proof/main_proof.md']}  proof/main_proof.md
{EXPECTED['audit/independent_referee/frozen_inputs.json']}  audit/independent_referee/frozen_inputs.json
{EXPECTED['src/verify_all.py']}  src/verify_all.py
{EXPECTED['audit/verification_log.json']}  audit/verification_log.json
{EXPECTED['audit/independent_referee/independent_verifier.py']}  audit/independent_referee/independent_verifier.py
{EXPECTED['audit/independent_referee/verification_result.json']}  audit/independent_referee/verification_result.json
{script_hash}  audit/independent_referee/release_referee.py
```

The CLI recomputed all 17 hashes in the frozen binding.  It also bound the
current paper, proof, master verifier/log, independent verifier/result, all
nine decisive certificate files, bibliography, citation audit, claim ledger,
and release novelty log.

## Paper-only delta

PASS checks, unless a finding is listed below:

- release date is exactly August 30, 2026;
- Ambrus--Gargyan 2024 Conjecture 1.3 is stated with `n>=2` and `Q_n`;
- Ambrus--Gargyan 2025 is stated with `n>=4` and `3<=k<=n-1`;
- Pournin's correction is limited to the omitted proper-subdiagonal transverse
  constrained-Hessian term and explicitly preserves the main diagonal;
- the Q3 certificate-table row occurs exactly once and every endpoint row in
  that table is unique.

Reversing only those three textual replacements (date, Conjecture 1.3 sentence,
and AG25/Pournin paragraph) reconstructs the preceding paper SHA-256 exactly:
`{PRIOR_PAPER_SHA256}`.  The two theorem blocks have their frozen hashes, the
proof is byte-identical, and all nine certificate hashes are unchanged.

## Citation and novelty boundary

The citation surface is exactly five keys and matches the five-entry BibTeX
database.  The separately frozen audit contains exactly C01--C11 and reports
11/11 verified, zero unverified.  The release novelty rerun is dated 2026-08-30
and the paper uses only a database-bounded not-found statement.

## Exact gates

- frozen binding: {details.get('binding_inputs', 0)}/17;
- master log: {details.get('master_checks', 0)}/23 checks PASS;
- independent result: {details.get('independent_inputs', 0)} hash-bound inputs PASS;
- decisive certificate hashes: {details.get('certificates', 0)}/9 unchanged;
- Q3 table row: {details.get('q3_table_rows', 0)}/1, with no duplicate endpoint row.

## Findings

{json.dumps(findings, indent=2, ensure_ascii=False) if findings else 'None.'}

## Decision

**{status}: submission-gate delta {status}.**
"""
    report_hash = sha256_bytes(report.encode("utf-8"))
    verdict = {
        "schema": "q5-release-delta-referee-verdict-v2",
        "date": "2026-08-30",
        "timezone": "Asia/Shanghai",
        "verdict": status,
        "submission_gate_delta": status,
        "mode": "independent_stdlib_no_project_imports",
        "counts": counts,
        "findings": findings,
        "frozen_hashes": {
            **{key.replace("/", "__"): value for key, value in EXPECTED.items()},
            "prior_paper_main_tex": PRIOR_PAPER_SHA256,
            "release_referee": script_hash,
            "release_delta_report": report_hash,
        },
        "checks": details,
        "paper_delta": {
            "date_august_30": status,
            "ag24_conjecture_1_3_n_ge_2": status,
            "ag25_n_ge_4_and_3_le_k_le_n_minus_1": status,
            "pournin_proper_subdiagonal_transverse_term": status,
            "pournin_main_diagonal_unchanged": status,
            "q3_table_row_unique": status,
            "theorem_changed": details.get("theorem_changed") if not findings else None,
            "proof_changed": details.get("proof_changed") if not findings else None,
            "certificate_changed": details.get("certificate_changed") if not findings else None,
        },
        "proof_assistant_used": False,
    }
    return report, json.dumps(verdict, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    inferred_root = Path(__file__).resolve().parents[2]
    parser.add_argument("--root", type=Path, default=inferred_root)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--verdict", type=Path, default=None)
    args = parser.parse_args()
    root = args.root.resolve()
    report_path = args.report or root / "audit/independent_referee/RELEASE_DELTA_REPORT.md"
    verdict_path = args.verdict or root / "audit/independent_referee/release_delta_verdict.json"
    findings: list[dict[str, str]] = []
    details: dict[str, Any] = {}
    try:
        details = audit(root)
    except Exception as exc:  # fail closed, including unexpected audit errors
        findings.append({"severity": "fatal", "id": "R-D1", "message": str(exc)})
    report, verdict = make_outputs(root, details, findings)
    report_path.write_text(report, encoding="utf-8")
    verdict_path.write_text(verdict, encoding="utf-8")
    status = "PASS" if not findings else "FAIL"
    print(json.dumps({
        "status": status,
        "report": str(report_path),
        "report_sha256": sha256_file(report_path),
        "verdict": str(verdict_path),
        "verdict_sha256": sha256_file(verdict_path),
        "counts": {name: sum(f["severity"] == name for f in findings)
                   for name in ("fatal", "major", "local", "expository")},
    }, sort_keys=True))
    return 0 if not findings else 1


if __name__ == "__main__":
    sys.exit(main())
