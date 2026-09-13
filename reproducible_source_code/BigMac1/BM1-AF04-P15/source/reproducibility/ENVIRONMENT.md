# Reproduction environment

Verified on 2026-08-30:

- macOS arm64, target arm64-apple-darwin25.5.0
- Apple clang 21.0.0
- C++ language mode: C++20
- Python 3.14.7, standard library only for all verifier scripts
- TeX Live 2026, pdfTeX 1.40.29
- latexmk 4.88
- BibTeX 0.99e
- Poppler/pdftoppm 26.04.0

There are no Python package dependencies, network calls, random seeds, solver
versions, or floating-point tolerances in the certificate verification path.
The finite-census coordinator compiles its C++ verifier into a fresh temporary
directory on every run.

## Fast checks

    python3 -m py_compile src/list_normalized_alphabets.py \
      certificates/verify_finite_census.py \
      certificates/verify_uniform2_no_go.py tests/test_fail_closed.py
    python3 tests/test_fail_closed.py
    python3 certificates/verify_uniform2_no_go.py \
      certificates/uniform2_no_go.json

## Full exact check

    python3 certificates/verify_finite_census.py \
      certificates/census_max5.json

## Clean manuscript build

    cd paper
    latexmk -C main.tex
    latexmk -pdf -interaction=nonstopmode -halt-on-error \
      -file-line-error main.tex

## Manifest verification

    python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
      . manifests/release_manifest.json
