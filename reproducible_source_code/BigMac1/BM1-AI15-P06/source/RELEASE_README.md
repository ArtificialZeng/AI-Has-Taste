# Reproducibility release: Kusner \(\ell_1^5\) partial theorem

This source release accompanies the partial theorem that any hypothetical
eleven-point equilateral set in \(\ell_1^5\) has at least 19 positive
consecutive coordinate gaps (at least 24 coordinate levels in total).
It does **not** settle \(e(\ell_1^5)=10\).

## Requirements

- Python **3.10 or newer**. The exact scripts use only the standard library.
- TeX Live with 'latexmk', 'pdflatex', and BibTeX to rebuild the paper.

No proof assistant was used.

## Principal checks

Run from the release root:

    python3 certificate/verify_sparse_gap.py certificate/sparse_gap_claim.json
    python3 certificate/verify_equilateral_witnesses.py certificate/equilateral_witnesses.json
    python3 experiments/proof_cut_frame_audit.py
    python3 certificate/t18_verify_endpoint_manifest.py certificate/t18_endpoint_manifest.json
    python3 audit/referee_t18_check.py
    python3 certificate/verify_integer_box.py certificate/integer_box_side5.json

Optimization and isolation modes may be combined:

    python3 -O -I certificate/t18_verify_endpoint_manifest.py certificate/t18_endpoint_manifest.json

The finite-box command proves only that every equilateral subset of
\(\{0,1,2,3,4\}^5\) has size at most 10.

## Paper build

    cd paper
    latexmk -C main.tex
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

## Release exclusions

The ZIP intentionally excludes '.venv', '__pycache__', '.pyc', PDF files,
rendered page images, binary files, raw discovery logs, the generated LaTeX
files '.aux', '.blg', '.log', '.fls', and '.fdb_latexmk', and the unreviewed
exploratory file 'proof/t19_branch.md'. It retains 'paper/main.bbl' for a
portable build that does not require rerunning BibTeX.
'MANIFEST.json' records SHA-256 hashes of every included source file.
