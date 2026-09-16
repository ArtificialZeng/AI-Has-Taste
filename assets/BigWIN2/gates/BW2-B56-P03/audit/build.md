# Clean build audit

**Accept.** From `manuscript/`, `latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed and
converged. The final PDF has four letter-size pages and SHA-256
`67b4503458761f67fbce9f43c2396efa1321c2cece4d17989fb8504d1b466c91`.

The final `main.log` and `main.blg` were scanned for undefined citations or
references, missing database entries, BibTeX warnings, repeated entries,
LaTeX errors, fatal errors, emergency stops, undefined control sequences, and
runaway arguments; no match remained. The key checker reported six cited and
six defined keys with exact `.aux` agreement. Cross-reference
`Theorem~\ref{thm:main}` resolves.

`pdfinfo` reports the expected title and author metadata, four pages, letter
page size, and PDF version 1.5. Fonts are embedded and the PDF has extractable
text.
