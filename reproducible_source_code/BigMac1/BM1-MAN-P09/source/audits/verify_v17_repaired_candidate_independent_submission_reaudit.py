#!/usr/bin/env python3
"""Independent read-only re-audit of the repaired v17 submission candidate.

The candidate tree is never written.  Mutation switches alter only the
in-memory LaTeX string and exist to demonstrate that the proof-order and
transcription gates fail closed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[3]
PKG = WORKSPACE / "tmp/pdfs/v17_candidate"

EXPECTED_FILES = {
    "main.tex": "cfd1be699b3fba93b16288d846552ce883f2b75883a930ea527c1de87b67e6ff",
    "main.pdf": "41f816165950f9d5369f0cc4583b33f396fb7bb3d3b937d8a62f8b1177611939",
    "main.bbl": "3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b",
    "references.bib": "989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600",
    "README.md": "c0fc9523b19569feb40c9d72cb8b6937a2ad84968c39f536338b436f084d2aea",
    "RELEASE_MANIFEST.sha256": "0d08df65797fb1c5ddfb4fc9cd9b9f77d46420a90aca00962057f71fb817530b",
    "audits/BUILD_TEST_REPORT_2026-08-26_V17_CANDIDATE.md":
        "0db088d87c473089d13539d30232cf3903224c81bc02b37a3bce94bcfdbccdb0",
}

NESTED_MANIFESTS = {
    "certificate_workspace/tmp/research/compact_ball_inward_z_constant_lift_x497_500_source_freeze_manifest.sha256":
        ("e7220043d9ac01c91e72ebf4029a8c248bff77bb2225b2884b5c372c60df108d", 8),
    "certificate_workspace/tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x497_500_independent_referee_manifest.sha256":
        ("50c451f84eabfdb7832e3610c37bd347dc1419c109f64b7c7cece41e8e60eb06", 35),
    "certificate_workspace/tmp/research/compact_ball_cap_x_shear_x1_source_freeze_manifest.sha256":
        ("8d68e2cbeb9e56e86b818dfcdfb1e4ebc1ac5cc5a678ab4c3857a55cde0d2cc5", 8),
    "certificate_workspace/tmp/research/audit/compact_ball_cap_x_shear_x1_independent_referee_manifest.sha256":
        ("3cdbb03409be176c7d557056e3fcbd426e14563f35d81edc18b03dbd43064a9c", 40),
    "certificate_workspace/tmp/research/compact_ball_uncovered_box_x5_8_xy_source_freeze_manifest.sha256":
        ("9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d", 21),
    "certificate_workspace/tmp/research/audit/compact_ball_uncovered_box_x5_8_xy_independent_referee_manifest.sha256":
        ("dcd4d091a8b2b9fc714c1e79571a3f251b747777ff91721fe1f5a1f7ab9a67cd", 64),
}

REPORT_HASHES = {
    "certificate_workspace/audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X497_500_INDEPENDENT_REFEREE_AUDIT.md":
        "ed2cb48240fa5a17eef9e9e76c4e547942642de1cc3997f2c23ae95818b61c45",
    "certificate_workspace/audit/COMPACT_BALL_CAP_X_SHEAR_X1_INDEPENDENT_REFEREE_AUDIT.md":
        "b8db0fa9bf450312c8921ca9ace147c09b451060647a9b90cb1267992144e71d",
    "certificate_workspace/audit/COMPACT_BALL_UNCOVERED_BOX_X5_8_XY_INDEPENDENT_REFEREE_AUDIT.md":
        "d5560cb01f08bae6634f2b48710dacfda1e03bdd5f8752c651dc3c728586cb0a",
}

EXPECTED_BIB = {
    "MR2223270", "Crouzeix_2003", "MR2449098", "MR2047592", "Crouzeix_2016"
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)
    print(f"PASS {label}")


def run(args: list[str]) -> str:
    return subprocess.run(
        args, check=True, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ).stdout


def check_hashes() -> None:
    for relative, expected in EXPECTED_FILES.items():
        path = PKG / relative
        require(path.is_file(), f"candidate file exists: {relative}")
        require(digest(path) == expected, f"candidate SHA: {relative}")
    for relative, expected in REPORT_HASHES.items():
        require(digest(PKG / relative) == expected,
                f"frozen independent-referee report SHA: {relative}")


def verify_top_manifest() -> None:
    manifest = PKG / "RELEASE_MANIFEST.sha256"
    obj = json.loads(manifest.read_text(encoding="utf-8"))
    records = obj.get("files")
    require(isinstance(records, dict), "top manifest has a files object")
    actual = {
        p.relative_to(PKG).as_posix()
        for p in PKG.rglob("*") if p.is_file() and p != manifest
    }
    require(len(records) == 1174, "top manifest has 1174 records")
    require(set(records) == actual, "top manifest file set is exact")
    for relative, record in records.items():
        path = PKG / relative
        require(path.stat().st_size == record.get("bytes"),
                f"manifest size: {relative}")
        require(digest(path) == record.get("sha256"),
                f"manifest SHA: {relative}")
    print("PASS independent top-manifest replay 1174/1174")


def verify_line_manifest(relative: str, expected_sha: str, expected_count: int) -> None:
    path = PKG / relative
    require(digest(path) == expected_sha, f"nested manifest SHA: {relative}")
    count = 0
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"nested manifest syntax {relative}:{lineno}")
        expected, target_relative = match.groups()
        target = PKG / "certificate_workspace" / target_relative
        require(target.is_file(), f"nested target exists: {target_relative}")
        require(digest(target) == expected, f"nested target SHA: {target_relative}")
        count += 1
    require(count == expected_count, f"nested manifest count {expected_count}: {relative}")


def verify_bibliography(tex: str) -> None:
    cited: set[str] = set()
    for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", tex):
        cited.update(x.strip() for x in group.split(","))
    bib = (PKG / "references.bib").read_text(encoding="utf-8")
    bibkeys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))
    aux = (PKG / "main.aux").read_text(encoding="utf-8", errors="replace")
    auxkeys = set(re.findall(r"\\bibcite\{([^}]+)\}", aux))
    bbl = (PKG / "main.bbl").read_text(encoding="utf-8", errors="replace")
    bblkeys = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", bbl))
    require(cited == EXPECTED_BIB, "exact five-key citation set")
    require(bibkeys == EXPECTED_BIB, "exact five-key BibTeX set")
    require(auxkeys == EXPECTED_BIB, "exact five-key AUX closure")
    require(bblkeys == EXPECTED_BIB, "exact five-key BBL closure")
    for token in (
        "10.1007/s00013-005-1533-5", "10.1007/s00013-003-0569-7",
        "10.3934/cpaa.2009.8.37", "10.1007/s00020-002-1188-6",
        "10.1137/15M1020411",
    ):
        require(token in bib, f"verified DOI retained: {token}")


def mutate_tex(tex: str, mode: str) -> str:
    if mode == "bare-qquad":
        marker = r"S=\frac{13}{30000}\tau X,\qquad"
        require(marker in tex, "bare-qquad mutation target exists")
        return tex.replace(marker, marker.replace(r"\qquad", "qquad"), 1)
    if mode == "proof-order":
        start_marker = "On the adjacent cell $99/100\\le X\\le497/500$"
        end_marker = "Thus the second cell is also strictly legal, rank two, and valid for both\n" \
                     "signed lifts.\n"
        start = tex.index(start_marker)
        end = tex.index(end_marker, start) + len(end_marker)
        block = tex[start:end]
        tex = tex[:start] + tex[end:]
        destination = tex.index(r"\begin{equation}\label{eq:constant-Z}")
        return tex[:destination] + block + "\n" + tex[destination:]
    if mode == "numeric-proof":
        marker = "Their $72$ exact nodes per cell are falsification\ndiagnostics only."
        require(marker in tex, "numeric-proof mutation target exists")
        return tex.replace(marker, "Their $72$ exact nodes per cell prove positivity.", 1)
    return tex


def verify_structure(tex: str) -> None:
    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    require(len(labels) == len(set(labels)), "LaTeX labels are unique")
    refs: set[str] = set()
    for group in re.findall(r"\\(?:eqref|ref|Cref|cref)\{([^}]+)\}", tex):
        refs.update(x.strip() for x in group.split(","))
    require(refs <= set(labels), "all explicit references have labels")
    require(len(re.findall(r"\\begin\{proof\}(?:\[[^]]*\])?", tex)) == tex.count(r"\end{proof}"),
            "proof environments are balanced")
    require(re.search(r"(?<!\\)qquad", tex) is None, "no bare qquad token")

    rec_label = tex.index(r"\label{thm:recentered-sheet}")
    rec_proof_start = tex.index(r"\begin{proof}", rec_label)
    rec_proof_end = tex.index(r"\end{proof}", rec_proof_start)
    z_definition = tex.index(r"\begin{equation}\label{eq:constant-Z}")
    constant_label = tex.index(r"\label{thm:constant-sheet}")
    constant_proof_start = tex.index(r"\begin{proof}", constant_label)
    constant_proof_end = tex.index(r"\end{proof}", constant_proof_start)
    second_cell = tex.index("On the adjacent cell $99/100\\le X\\le497/500$")
    gate_sign = tex.index("For the gate sign, the source starts", constant_proof_start)
    require(rec_proof_start < rec_proof_end < z_definition,
            "recentered proof closes before constant-Z definition")
    require(z_definition < constant_label < constant_proof_start < second_cell < gate_sign < constant_proof_end,
            "constant second-cell legality is definition-after-use safe and in its own proof")
    require(second_cell not in range(rec_proof_start, rec_proof_end),
            "constant second cell is absent from recentered proof")

    normalized = re.sub(r"\s+", " ", tex)
    exact_claims = (
        "the cleared gate and core have $32/32$ nonzero $(S,X)$ coefficients, $1581$ centered monomials, and bidegree $(7,4)$",
        "$40/40$ strictly positive Bernstein lower controls on each cell",
        "Each cell has unique weakest index $(7,0)$",
        "the cleared gate and core have $48/48$ nonzero $(S,X)$ coefficients, $2263$ centered monomials, and bidegree $(7,8)$",
        "$72/72$ strictly positive",
        "All $531/531$ controls are strictly positive",
        "$(0,0,6)$",
        r"\frac{8332318460470459}{15187500000000000}>0",
        r"=\frac{30189}{62500}>0",
        r"\det C=\frac5{72}S>0",
    )
    for claim in exact_claims:
        require(claim in normalized, f"exact local-certificate transcription: {claim[:54]}")

    for disclaimer in (
        "not a covering of the compact ball",
        "The unrestricted assertion",
        "not a raw-gate counterexample",
        "neither a negative raw-gate example nor a maximality statement",
        "any claim that closure of this one stitched $X$-sheet through $X=1$ covers the surrounding compact ball or yields a global parameterization",
        "arbitrary-node operator bridges and the optimal constant of a fixed crossing lens",
    ):
        require(disclaimer in normalized, f"scope disclaimer: {disclaimer[:58]}")
    require("diagnostics only" in tex and "nodes per cell prove positivity" not in tex,
            "sampled nodes remain diagnostics, never proof")
    require(not any(tag in tex for tag in ("CE-046", "CE-048", "CE-059", "CE-060")),
            "rejected CE routes are not reused")

    require(r"\author{Yonghua Xiong$^{*}$}" in tex,
            "Yonghua Xiong carries the corresponding-author marker")
    require(r"\thanks{\textsuperscript{*} Corresponding Author: Yonghua Xiong.}" in tex,
            "corresponding-author footnote is exact")
    require("An AI coding assistant" in tex and "No Lean or other proof assistant formalizes" in tex,
            "AI and Lean disclosures are explicit")


def verify_pdf_and_final_logs() -> None:
    info = run(["pdfinfo", str(PKG / "main.pdf")])
    require(re.search(r"^Pages:\s+41$", info, re.MULTILINE) is not None,
            "PDF has 41 pages")
    require(re.search(r"^Encrypted:\s+no$", info, re.MULTILINE) is not None,
            "PDF is unencrypted")
    require("Yonghua Xiong" in re.search(r"^Author:\s+(.+)$", info, re.MULTILINE).group(1),
            "PDF author metadata contains Yonghua Xiong")
    fonts = run(["pdffonts", str(PKG / "main.pdf")])
    rows = [line for line in fonts.splitlines()[2:] if line.strip()]
    require(bool(rows) and all(
        re.search(r"\s+yes\s+yes\s+yes\s+\d+\s+\d+\s*$", row) is not None
        for row in rows
    ), "all PDF fonts are embedded/subset/Unicode")
    text = run(["pdftotext", "-layout", str(PKG / "main.pdf"), "-"])
    require("qquad0" not in text and "??" not in text,
            "PDF text contains no repaired-token residue or unresolved placeholder")
    require("YONGHUA XIONG" in text and
            "Corresponding Author: Yonghua Xiong." in text,
            "PDF text contains author name and corresponding-author footnote")
    require("531/531" in text and "72/72" in text and "40/40" in text,
            "PDF text retains the three new exact control counts")

    log = (PKG / "main.log").read_text(encoding="utf-8", errors="replace")
    blg = (PKG / "main.blg").read_text(encoding="utf-8", errors="replace")
    forbidden = re.compile(
        r"undefined references|Citation .* undefined|Reference .* undefined|"
        r"LaTeX Warning|Package .* Warning|Overfull|Underfull|multiply defined",
        re.IGNORECASE,
    )
    require(forbidden.search(log) is None, "converged main.log is clean")
    require("Warning" not in blg and "error" not in blg.lower(),
            "converged main.blg is clean")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation", choices=("none", "bare-qquad", "proof-order", "numeric-proof"),
        default="none",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(f"V17 REPAIRED-CANDIDATE INDEPENDENT REAUDIT mutation={args.mutation}")
    check_hashes()
    verify_top_manifest()
    for relative, (expected_sha, expected_count) in NESTED_MANIFESTS.items():
        verify_line_manifest(relative, expected_sha, expected_count)
    print("PASS all six post-v16 exact-certificate chains")
    tex = (PKG / "main.tex").read_text(encoding="utf-8")
    tex = mutate_tex(tex, args.mutation)
    verify_bibliography(tex)
    verify_structure(tex)
    verify_pdf_and_final_logs()
    require(args.mutation == "none", "normal unmutated audit mode")
    print("CLASSIFICATION fatal=0 major=0 minor=0")
    print("VERDICT PASS — repaired v17 candidate is submission-ready")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"FAIL CLOSED: {exc}", file=sys.stderr)
        sys.exit(1)
