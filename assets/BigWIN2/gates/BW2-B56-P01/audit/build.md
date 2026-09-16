# Build release audit

The manuscript was rebuilt on 2026-09-07 from `manuscript/main.tex` and
`manuscript/references.bib` with:

```text
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk -gg` removed its generated intermediates and performed the complete
pdflatex--BibTeX--pdflatex convergence sequence. The final run produced
`manuscript/main.pdf` with 5 A4 pages. The build exited 0.

The final `manuscript/main.log` and `manuscript/main.blg` were scanned for
undefined citations or references, absent database entries, BibTeX warnings,
repeated entries, LaTeX errors, fatal errors, emergency stops, undefined control
sequences, and runaway arguments. None was present. The bibliography checker
reported 8 cited keys, 8 database keys, no missing/unused keys, and exact `.aux`
agreement.

Cross-references, equation numbers (1)--(9), Theorem 1.1, Lemma 2.1, section
numbers, and bibliography labels resolve in the PDF. `pdfinfo` reports a valid
PDF 1.5 file, A4 page size, zero rotation, and five pages.

Final bindings:

- mathematical snapshot: `7bfb0b28c55d1470cd55ad3c0fe5642790ad29190ac4e282a81cfc91794a5c3d`
- manuscript digest: `71c77700622ed5d01e9a1ae9c788c703cd36cf40f86845a79e9143f0780c6442`
- PDF digest: `52699207f152303b07fe9b202740581463652bd8bde38fe6a4172838d09373c2`
- final log digest: `c0c5c4687877572a02259fb72a06f52bbe492b938422b54b9ba8dc26146c0e4c`

Verdict: **accept**.
