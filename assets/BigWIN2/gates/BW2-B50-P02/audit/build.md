# Build audit

Verdict: **accept**.

From `manuscript/`, the canonical command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged with exit
status 0 after BibTeX and the required LaTeX reruns. The final `main.log` and
`main.blg` contain no undefined citations or references, missing database entries,
duplicate entries, LaTeX/BibTeX warnings, overfull/underfull boxes, errors, emergency
stops, or runaway arguments. The citation-key checker reports four cited keys, four
BibTeX keys, no missing or unused keys, and exact `.aux` agreement.

`pdfinfo` recognizes a four-page, unencrypted letter-size PDF. Title, author, subject,
and keywords are populated. `pdffonts` reports every listed font embedded, subsetted,
and Unicode-mapped. The final build log SHA-256 is
`c8f3e3788b80a8b881ed58a7a41ab945425ebb8f0acdb5137a645dee6987c1f4`.
