# Q5 central-section classification — release source

This archive accompanies *Local extrema of central hyperplane sections of the
five-dimensional cube* by Zijian Zeng.

## Build the paper

```text
cd paper
SOURCE_DATE_EPOCH=1788048000 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The complete LaTeX source is `paper/main.tex` with bibliography
`paper/references.bib`.  No generated auxiliary file is required.

## Reproduce the exact audit

```text
/opt/anaconda3/bin/python3 src/verify_all.py
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 audit/independent_referee/independent_verifier.py
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 audit/independent_referee/mutation_tests.py
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 audit/independent_referee/test_parser_failclosed.py
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python3 audit/independent_referee/release_referee.py
```

The master audit expects Python 3.13, SymPy, and Singular.  Decisive proof
inputs are serialized under `certificates/` and `results/`.  The release
verifiers reject malformed or noncanonical certificate input fail closed.

## Scope

The terminal mathematical status is `PROVED`.  No Lean, Coq, Isabelle,
Agda, or other interactive proof assistant was used; no formalization
endpoint is claimed.  Novelty statements are database-bounded through
2026-08-30, as recorded in `literature/search_log.md`.

Every file in the source archive is bound by the included `MANIFEST.json`.
