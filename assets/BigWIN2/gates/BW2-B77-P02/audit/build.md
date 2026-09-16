# Build audit

The canonical command

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

completed successfully in `manuscript/` and converged to a six-page PDF.  The
final `manuscript/main.log` and `manuscript/main.blg` contain no LaTeX error,
fatal stop, undefined control sequence, runaway argument, undefined citation or
reference, missing database entry, repeated entry, or BibTeX warning.  The
bibliography-key checker found five cited keys, five bibliography entries, and
complete agreement with `main.aux`.

`pdfinfo` recognizes an unencrypted PDF 1.5 with six US-letter pages and
extractable text.  `pdffonts` reports every font embedded and subsetted.  The
PDF identifies pdfTeX as producer and LaTeX/hyperref as creator; no suspicious
forms, JavaScript, rotation, or malformed metadata were reported.

**Verdict: accept.**
