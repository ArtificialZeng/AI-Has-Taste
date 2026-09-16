# Build and reproducibility audit

Release job: `win-00082-p01-release-b749192a753f`

The retained full compiler transcript in `audit/build.log` records a
converged `pdflatex`/BibTeX build of the current source snapshot and ends with
`Output written on main.pdf (5 pages, 379921 bytes)`.  Its SHA-256 is
`eee33bb9539006324d093b53fcf6f5730032ddc9113f4c1eccf8af00e0191d1d`.
A fresh invocation of

```
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

returned exit code 0 and confirmed that `main.pdf` was up to date.  The PDF
digest remained
`d81e54d53ae29a1b355b3dbc6ed351a6d2fdb86a3d3ed9ffe7376822c15f1013`.

The prescribed bibliography checker found five cited keys and five unique
BibTeX keys, with no missing/unused entry and exact AUX agreement.  Searches
of `main.log`, `main.blg`, and `audit/build.log` found none of the forbidden
citation, reference, BibTeX, LaTeX, fatal, or runaway diagnostics.
Cross-references and bibliography numbers resolve in the extracted PDF text.
All fonts used by the paper are embedded Type 1 fonts; the document has five
letter-size, unrotated, unencrypted pages and no JavaScript.

The deterministic command `python3 verify_slices.py` returned exit code 0:

```
tested_pairs=11340
complements: impossible=20 generating=20 antipodal=5
valid_slice_pairs=200
all_70_columns_accessible_for_some_A=no
```

No source, bibliography, PDF, accepted mathematical evidence, or manuscript
snapshot byte was changed during this audit.  Overall status: **PASS**.
