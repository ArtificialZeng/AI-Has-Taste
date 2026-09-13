# Fresh build audit

Date: 2026-09-09  
Release job: `bigMac-00023-p06-release-71cb8b727e7d`

The manuscript directory was first cleaned with `latexmk -C main.tex`, then
built with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The build completed successfully after the expected initial TeX/BibTeX reruns.
The final `manuscript/main.log` is 24,396 bytes and has SHA-256
`394f8bdd321527984c33a059867fe2e3f056ee8bf2179196f4d94835675be600`.
The final log has no compilation failure, undefined citation/reference,
multiply defined label, rerun request, overfull/underfull box, or package/LaTeX
warning. `manuscript/main.blg` records four used entries and no BibTeX warning.
The final `.aux` contains all four `\bibcite` records and resolved labels for
the theorem, table, equation, and proposition.

The recorder file shows no undeclared authored project dependency. The only
authored inputs are `main.tex` and `references.bib`; local `.aux`, `.bbl`, and
`.out` inputs are generated build products. This agrees with the sorted
`publication.json` source list.

`pdfinfo` reports a valid, unencrypted four-page letter-size PDF, title *An
Exact Computer-Assisted Perfectness Census for Integral Circulant Graphs
Through Order 32*, author Xiaojian Zeng, subject matching the finite result,
and PDF version 1.7. `pdftotext -layout` produced 11,885 nonempty bytes. All
listed Latin Modern and AMS fonts are embedded and subsetted. The fresh PDF
SHA-256 is
`64dafba32a80015ecbd8d20f62a8dc0624504ae5d8211a7c7569ae380925fdcc`.

**Verdict: accept; clean build.**

