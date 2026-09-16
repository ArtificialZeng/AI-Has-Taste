# Build audit

## Verdict

Accept.  A forced clean rebuild was run from `manuscript/` with

`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`.

BibTeX and two converging pdfLaTeX passes completed successfully.  The final
`manuscript/main.log` and `manuscript/main.blg` contain no LaTeX error, fatal
error, emergency stop, undefined citation/reference, missing database entry,
repeated entry, BibTeX warning, overfull box, or underfull box diagnostic.

The read-only bibliography checker reports six cited keys, six entries, no
missing/unused key, and exact `.aux` agreement.  `pdfinfo` reports three
letter-size pages, title `The Zero-Free Columns of the Character Table of
S44`, author `Xiaojian Zeng`, and subject `Symmetric-group character tables`.
`pdffonts` confirms every listed font is embedded.  The final PDF is
extractable and nonempty.

