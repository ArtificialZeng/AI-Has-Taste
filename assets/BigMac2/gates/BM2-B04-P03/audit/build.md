# Clean build audit

**Verdict:** accept.

After `latexmk -C main.tex`, the command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed with
exit status 0 and produced the current five-page `manuscript/main.pdf`.
Latexmk ran BibTeX and the necessary LaTeX passes. Expected first-pass undefined
labels and citations were resolved by those reruns; the bound final compiler log
contains no LaTeX/package warnings, undefined citations or references, multiply
defined labels, overfull/underfull boxes, errors, or fatal diagnostics. BibTeX
reports zero warnings.

The final PDF has a valid PDF 1.7 header, nonempty text extraction, A4 pages,
explicit title and author metadata, and embedded fonts. Cross-references (1)--(5),
Theorem 1, Lemmas 2--5, and bibliography entries [1]--[2] all resolve in the
extracted and rendered output. The real build log is `manuscript/main.log`, with
SHA-256 `0c808ee28cf88f794c3f70acc797d1d2c6426463274da5575d88c5e02515e7be`.
