# Build audit

Release job `win-00086-p02-release-0b3f9cf5c11e` performed a clean
`latexmk` build in `manuscript/` using

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

`latexmk -C main.tex` first removed generated auxiliary products.  The final
run converged after BibTeX and the required LaTeX rerun, produced a three-page
PDF, and returned success.  The final `main.log` contains no undefined
citation or reference, LaTeX error, fatal error, emergency stop, or undefined
control sequence.  `main.blg` contains no missing database entry, warning, or
repeated entry.

The bibliography checker found one bibliography file, six cited keys, six
BibTeX keys, no missing bibliography file, no cited key missing from the
bibliography, no unused entry, and exact equality with the six keys in
`main.aux`.  `pdfinfo`, `pdftotext`, and `pdffonts` succeeded.  All nineteen
listed Type 1 fonts are embedded, and the PDF title and author metadata match
the manuscript.

Result: **clean build accepted**.
