# Clean build audit

Release job: `win-00085-p01-release-dc2c5030af7e`

The manuscript was cleaned and rebuilt from `manuscript/main.tex` with

```text
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The complete BibTeX workflow converged successfully and produced a five-page
PDF.  A fresh `check_bib_keys.py main.tex --aux main.aux` run found four cited
keys, four bibliography keys, no missing or unused keys, and exact `.aux`
agreement.  Scanning `main.log` and `main.blg` found no undefined citations or
references, absent database entries, repeated entries, LaTeX errors, emergency
stops, runaway arguments, or fatal errors.  PDF metadata contains the intended
title and author, and `pdfinfo` recognizes an unencrypted A4 PDF with five pages.

Verdict: **ACCEPT** (`clean_build=true`).
