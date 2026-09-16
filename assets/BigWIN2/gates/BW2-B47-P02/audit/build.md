# Reproducible build audit

Verdict: **accept**. From `manuscript/`, the declared command
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged under
pdfTeX/BibTeX and produced the current three-page PDF. The final `main.log` has
SHA-256 `6c3550b528d094ba46384c67c407ae5c2642cf2b3b9401dd55a6731b9227a56b`.
The prescribed diagnostic scan found no undefined citation/reference, missing
database entry, BibTeX warning, duplicate entry, LaTeX error, fatal stop,
overfull box or underfull box. All 23 listed font subsets are embedded. PDF
title and author metadata are present and correct. The exact graph verifier
also re-passed: six graphs, 280 vertices each, degree 160, 22,400 edges each,
and all 36 ordered certificates.
