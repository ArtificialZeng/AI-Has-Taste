# Source archive

This archive accompanies:

Zijian Zeng, *Links--Gould positivity for two-block alternating
2-bridge knots* (2026).

## Build the paper

Requirements: a standard LaTeX distribution with latexmk, pdflatex,
and BibTeX.

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

## Run the exact checks

Python 3 and SymPy are required.

    python3 -m pip install -r requirements.txt
    ./code/run_checks.sh

The finite parameter values in the regression suite check the
implementations. The proof for all positive parameters is contained in
main.tex and proof/double_twist_theorem.md.

## Contents

- main.tex, references.bib: manuscript source.
- proof/double_twist_theorem.md: standalone proof record.
- certificate/: two independent exact formula checkers.
- code/: two exact matrix-based boundary evaluators and the test runner.
