# Clean-build audit

Release job: `win-00084-p01-release-fe275ec7f516`

The canonical build was run from a cleaned auxiliary state with
`cd manuscript && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
BibTeX and two PDFLaTeX passes converged successfully to a five-page PDF.  The
final `main.log` and `main.blg` contain no undefined citations or references,
missing database entries, repeated entries, BibTeX warnings, LaTeX errors,
fatal stops, runaway arguments, overfull boxes, or underfull boxes.  The
bibliography checker reports 5 cited keys, 5 present entries, and exact AUX
agreement.  PDF metadata reports US-letter pages, embedded Type 1 fonts, and no
encryption or JavaScript.  Status: **PASS**.
