# LaTeX package for the continuous n=7 geometric Max-Cut theorem

This archive contains the journal-neutral `amsart` manuscript, its
bibliography, the locked formal statement, the exact finite certificate, and
the independent standard-library verifier.

## Build the manuscript

From the archive root:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Verify the exact certificate

Python 3.10 or later is sufficient; no third-party Python package is required.

```bash
python3 scripts/verify_certificate.py
```

The verifier reconstructs all 64 cut polynomials in two ways, checks all 189
directed comparisons, verifies 185 rational Sturm root counts, and checks the
four threshold identities.  No proof assistant was used.

## Files

- `main.tex`: manuscript source;
- `references.bib`: source-audited bibliography;
- `problem/formal_statement.md`: statement bound to the certificate;
- `certificates/n7_sturm_certificate.json`: serialized exact certificate;
- `scripts/verify_certificate.py`: independent exact verifier.
