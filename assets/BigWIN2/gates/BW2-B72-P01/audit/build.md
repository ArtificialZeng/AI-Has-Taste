# Clean build audit

**Accept.**  The canonical manuscript was freshly rebuilt in `manuscript/`
with

`latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex`.

BibTeX and pdfLaTeX completed with exit status zero and converged.  The final
log scan found no LaTeX or BibTeX errors, fatal or emergency stops, undefined
citations or references, missing database entries, repeated entries, relevant
warnings, overfull boxes, or underfull boxes.  The bibliography checker reports
three cited keys, three database keys, and the identical three-key AUX set,
with no unused entry.

`pdfinfo` reports a valid four-page US-letter PDF with extractable text.  After
the scope-neutral title-macro repair and existing metadata setup, its metadata contains the full manuscript
title, author Xiaojian Zeng, an accurate subject, and five relevant keywords.
`pdffonts` lists eighteen font instances, all embedded and subsetted with
Unicode mappings.  `pdftotext` extracted 244 lines, 1,552 words, and 9,141
bytes.  The final PDF SHA-256 is
`42a2fc03d1ccd7aa8514ddc188a67c5178c51ee536feb566a6856363876a76a8`.
