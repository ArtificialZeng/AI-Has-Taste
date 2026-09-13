# Source package

This archive accompanies *A Certified n=7 Case of a Generalized
Stack-Sorting Enumeration Conjecture* by Zijian Zeng.

## Build

From this directory, run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Exact verification

The theorem concerns only the finite endpoint n=7. The serialized exact
certificate is `certificates/n1_to_n7_counts.json`; the independent verifier
is `code/verify_certificate.py`. Run:

```text
python3 -I code/verify_certificate.py certificates/n1_to_n7_counts.json
```

The certificate and verifier use exact integers and complete enumeration.
No floating-point or modular-only inference is used. No Lean, Coq, Isabelle,
or other proof assistant was used.

`MANIFEST.json` binds the files in this source package by SHA-256.
