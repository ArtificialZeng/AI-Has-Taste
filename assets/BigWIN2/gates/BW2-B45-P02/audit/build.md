# Reproducible build audit

Verdict: **accept**.

The manuscript directory was cleaned with `latexmk -C main.tex`, then rebuilt
from `main.tex` and `references.bib` with:

`LC_ALL=C SOURCE_DATE_EPOCH=0 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

LaTeXmk 4.76, pdfTeX 1.40.22, and BibTeX 0.99d completed successfully and
converged after the required BibTeX/pdflatex passes. The result is a valid
four-page PDF with SHA-256
`2398795b5d95422aee79c339fb1820b7ab6f64ae80a791b86f5dbb14d4f25a20`.
Its fixed build timestamp is 1970-01-01 00:00:00 UTC (displayed by `pdfinfo` in
the local timezone), avoiding a clock-dependent PDF digest.

The final `main.log` and `main.blg` contain no undefined citations or references,
missing database entries, repeated entries, LaTeX errors, fatal/emergency stops,
undefined control sequences, runaway arguments, or over/underfull boxes. The
bibliography checker reports four cited keys, four entries, no missing/unused
keys, and exact TeX/AUX agreement. The exact symbolic transcription checker also
completed successfully. After the Unicode accent compatibility repair, no
source file was changed during the final clean release build;
`source.md` retains its frozen SHA-256.
