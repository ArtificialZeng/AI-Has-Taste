# Clean-build audit

The canonical manuscript was cleaned and rebuilt from source with
`cd manuscript && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
BibTeX and the required repeated pdfLaTeX passes converged successfully to a
six-page PDF.  The final log scan found no undefined citation or cross-reference,
missing database entry, repeated BibTeX entry, BibTeX warning, LaTeX error,
undefined control sequence, runaway argument, emergency stop, or fatal error.

All 23 fonts reported by `pdffonts` are embedded.  `pdfinfo` confirms the title,
author, letter page size, six pages, and an unencrypted PDF.  `qpdf` was not
installed, so no qpdf-specific diagnostic is claimed; this is not a visual or
build blocker because pdfTeX completed cleanly, Poppler parsed and rendered every
page, and the rendered pages were inspected separately.
