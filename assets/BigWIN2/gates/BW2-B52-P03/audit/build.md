# Clean build audit

Accepted on 2026-09-07 after a clean `latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`. BibTeX and the required repeated pdfLaTeX pass completed; the
final target is `manuscript/main.pdf`, four pages.

The final `manuscript/main.log` and `manuscript/main.blg` contain none of the
screened undefined-citation/reference, missing-database-entry, repeated-entry,
BibTeX warning, LaTeX error, fatal-error, emergency-stop, undefined-control-
sequence, or runaway-argument diagnostics. The read-only bibliography checker
reports six cited keys, six BibTeX keys, no missing/unused entries, and exact
AUX agreement. PDF text extraction succeeds. `pdfinfo` confirms the title,
author, subject, keywords, four letter-size pages, no encryption, and a valid
PDF 1.5 file.

