# Build audit

Verdict: **accept**.  From `manuscript/`, a clean `latexmk -C` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged to a
five-page PDF.  The final `main.log` has SHA-256
`75b694f73833663a19472c87ca50cab1b9ae5a34d74e0e0eadde750890f0508f`.
The final diagnostic scan found no undefined citation or reference, missing
BibTeX entry, repeated entry, LaTeX error, fatal error, emergency stop, undefined
control sequence, or runaway argument.

`pdfinfo` reports the full paper title, author Xiaojian Zeng, subject, keywords,
five letter-size pages, no encryption, and an extractable text layer.  `pdffonts`
reports every listed font embedded with Unicode mapping.  The canonical source,
bibliography, PDF, and build log are bound by the final manuscript snapshot.
