# Exact odd-parameter periods for RESOCA 115

This archive contains the journal-neutral `amsart` source for the paper
“Exact odd-parameter periods for reversible elementary second-order cellular
automaton rule 115,” by Zijian Zeng, together with the small exact
verification bundle referenced by the manuscript.

## Build the paper

Requirements: a standard LaTeX installation with `amsart`, `latexmk`, and
BibTeX.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Run the exact verification

Requirements: Python 3.10 or later; no third-party Python package is needed.

```bash
python3 src/verify_tree_certificate.py
```

The verifier parses `certificates/tree_certificate.json`, validates the formal
statement and included implementations, checks every normalized local rule
context, exhausts two independently implemented finite tree models through
their documented depths, and compares two exact first-return simulators on
the documented cases.  These computations independently check the fragile
finite identities; the all-parameter theorem follows from the symbolic proof
in `main.tex`.

## Included files

- `main.tex`, `references.bib`: manuscript and bibliography;
- `problem/formal_statement.md`: exact theorem conventions;
- `certificates/tree_certificate.json`: serialized verification input;
- `src/verify_tree_certificate.py`: one-command verifier;
- `src/tree_model.py`, `src/breaker_tree_audit.py`: independent tree models;
- `src/referee_dense.py`, `src/referee_bitpacked.py`: independent orbit
  simulators.

No proof assistant was used.
