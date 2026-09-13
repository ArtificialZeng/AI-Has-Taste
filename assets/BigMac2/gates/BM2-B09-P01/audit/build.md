# Fresh clean-build audit

Audit date: 2026-09-07 (Asia/Shanghai)  
Release job: `bigMac-00009-p01-release-0c119e668365`

This report is bound to evidence snapshot
`f9c68aabbc292cf2fd8e90b5635b9baef672e7c87ad17d46d177e0d4d622b153`,
manuscript digest
`e492c66ba6b9df7334af2f520131d3a5d6f0676fe4ab45df1ddab17a80709752`,
and PDF digest
`fdcdba76cfab26dd9d05844b0c1a9cc033a655303cd090e0ee0b1a92f8110d84`.

## Clean build

From `manuscript/`, I ran

```text
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`-gg` performed a full cleanup and forced all targets to be regenerated. The
command exited 0 after the required pdfLaTeX, BibTeX, and final pdfLaTeX passes.
Warnings about initially absent citations and labels occurred only on the first
pass after cleanup; the subsequent passes resolved them. The retained final
compiler transcript is `manuscript/main.log` (16,058 bytes), SHA-256
`6e9e573b4318eb8c64945c5fee850e2d1bbd476bc37c2f36fd8bd55c8b5b4c31`.

The final `main.log` contains no LaTeX/package warning, undefined citation,
undefined reference, multiply-defined label, overfull box, underfull box,
fatal diagnostic, or error. `main.blg` reports zero warnings and zero errors.
`main.aux` contains the three intended citation keys and resolved labels for
Theorem 1, Tables 1--2, equation (1), and Lemma 2. `main.bbl` contains the three
defined bibliography entries.

## Output checks

- The output begins with a valid `%PDF-` header and has four unrotated US-letter
  pages.
- `pdftotext` extracted 12,457 nonempty bytes, including the theorem,
  cross-references, command line, and all bibliography entries.
- PDF metadata give the intended title and author.
- `pdffonts` reports every one of the 18 Type 1 fonts as embedded and subsetted.
- The complete local authored dependency set is `manuscript/main.tex` and
  `manuscript/references.bib`; no local import, figure, class, or style is
  omitted from `publication.json`.

## Verdict

**Accept.** The current PDF is the product of a fresh clean build from the
listed sources, and the final compiler state has resolved references and no
relevant build or layout diagnostics.
