# Fresh build audit

The manuscript was rebuilt from cleaned generated state with

```text
cd manuscript && latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The clean run executed pdfLaTeX, BibTeX, and the required final pdfLaTeX pass.
The current `manuscript/main.log` is nonempty and ends with successful output of
a three-page PDF.  The current `manuscript/main.blg` reports two used entries and
`warning$ -- 0`.  Searches of the final logs found no fatal errors, undefined
citations or references, multiply-defined labels, overfull/underfull boxes, or
rerun-required warnings.  The `.aux` and rendered reference section contain both
expected bibliography keys.  `pdfinfo` reports the expected title and author,
three letter-size pages, no encryption, and a valid PDF 1.7 file; `pdftotext`
returns nonempty text.

During this release audit, the three accidental literal commas in exponents and
the one comma in `\mathbb Z`'s rank exponent were corrected in `main.tex` as a
typographical, publication-only repair.  The manuscript was then clean rebuilt,
refrozen, and all release checks were repeated against the resulting digests.
The mathematical statement and evidence snapshot were unchanged.  Verdict:
**accept**.
