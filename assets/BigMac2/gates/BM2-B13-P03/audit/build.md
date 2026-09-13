# Fresh build audit

## Binding

- Release job: `bigMac-00013-p03-release-4189b067aff7`.
- Evidence snapshot: `393c635435e81b9dc70256f6851164d5d45067c12ff2d04143ac46090b6303c6`.
- Manuscript snapshot: `8487aa4f23241b4179277a1ce3bdde7e416eebd1cfe23df81005e94282a62ca3`.
- PDF SHA-256: `0bef46e936a25d8d0af1f3ea63a3cf60c8b5c982e46281d50a845a7ea5f88909`.
- Build log: `manuscript/main.log`, SHA-256
  `e1b6dcecff22e91d6164dd9254d6d8dd7d7967af0f324c1afbf2317d5d43301b`.

## Clean build

From `manuscript/`, I ran

```text
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The `-gg` pass removed generated dependencies and forced the complete build.
Latexmk ran pdfLaTeX, BibTeX, and the resolving pdfLaTeX pass, exited zero, and
reported the three-page PDF up to date. The final `main.log` is nonempty and
records successful output of `main.pdf`.

The final log and `main.blg` contain no compiler failure, undefined citation,
undefined reference, rerun request, changed-label warning, overfull box,
underfull box, or emitted LaTeX/package warning. (The package filename
`infwarerr.sty` contains the substring "error" but is not a diagnostic.) The
auxiliary file binds every equation/theorem label and both bibliography keys.

`pdfinfo` reports the intended title and author, letter-size pages, PDF 1.7,
three pages, no encryption, and no JavaScript. `pdftotext` extracts 5,671 bytes
of nonempty text. `pdffonts` reports every used font embedded and subsetted with
Unicode mappings. The optional `qpdf` executable is not installed; it is not a
required gate tool, and the successful compiler output plus `pdfinfo` and
`pdftotext` checks provide the required build evidence.

Inspection of `main.fls` and the BibTeX transcript confirms that the only
authored dependencies are the two sorted files in `publication.json`:
`manuscript/main.tex` and `manuscript/references.bib`; `main.bbl` is generated
from the latter. No local figure, imported TeX source, or custom style is used.

After the build, `freeze-manuscript` succeeded and recorded the current PDF
digest above without changing the evidence or authored-source digests.

## Verdict

**Accept.** This is a clean, reproducible build with resolved citations and
cross-references, a valid text-bearing PDF, complete authored dependency scope,
and no relevant compiler or layout warning.
