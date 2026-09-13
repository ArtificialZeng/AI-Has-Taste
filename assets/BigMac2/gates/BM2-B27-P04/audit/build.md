# Fresh build audit

A from-scratch build was performed on 2026-09-09 with
`latexmk -C article.tex` followed by the publication command
`latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex` in
`manuscript/`. BibTeX and the required repeated pdfLaTeX pass completed.

The final nonempty compiler log is `manuscript/article.log`, SHA-256
`7a2a8cde477be5fa4b624d8e5dc1465d13b285f71d7579935425d1c3b07209f3`.
It reports a four-page PDF and contains no compilation failure, undefined
citation/reference, multiply-defined label, overfull/underfull box, or pending
rerun warning. `article.blg` likewise contains no BibTeX warning. PDF metadata
has the intended title, author, and subject; `pdftotext` yields nonempty text.
Verdict: **accept; clean build**.
