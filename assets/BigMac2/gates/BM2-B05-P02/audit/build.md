# Fresh clean-build audit

On 2026-09-06 I removed only LaTeX-derived files with
`latexmk -C article.tex`, then ran the publication command
`latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex` from
`manuscript/`.  Latexmk performed the required BibTeX and repeat-pdflatex
passes and exited successfully.

The final engine log is `manuscript/article.log`, SHA-256
`016eca9c737108459b92a071aead9e6a4f66be6491c94c55a6a7c70f36892648`.
The final log has no fatal error, LaTeX/package warning, undefined citation or
reference, multiply-defined label, overfull box, or underfull box.  The BibTeX
log identifies `references.bib` and has no warning.  `pdftotext` extracts the
title, theorem, proof, disclosure, and both resolved bibliography entries.

The PDF has a valid PDF 1.7 header, four letter-size pages, no encryption, and
all 23 listed fonts are embedded with Unicode mappings.  Its SHA-256 is
`f782dbdb9bf1690ebefe06fa3d71c2f9d46cea92ff597b9f241bc13a63f7fa7d`.

Verdict: **accept**; this is a clean build of the frozen publication sources.

