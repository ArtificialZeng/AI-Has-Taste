# Clean build audit

**Verdict: accept.** From `manuscript/`, `latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged to a
three-page PDF. The final `main.log` and `main.blg` contain no undefined
citations/references, missing database entries, repeated entries, LaTeX errors,
fatal errors, or emergency stops. The bibliography key checker reports 3 cited
keys, 3 BibTeX keys, and exact `.aux` agreement.

`pdfinfo` reports the intended title and author, letter page size, three pages,
no encryption, and PDF 1.5. `pdffonts` reports every font embedded and subset.
