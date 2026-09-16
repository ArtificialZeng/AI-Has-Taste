# Build audit

Release job `win-00075-p04-release-8bfe4f162cde` performed a clean rebuild
with `latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`.  BibTeX and repeated pdfLaTeX passes converged successfully.

The final `manuscript/main.log` has SHA-256
`47a0901ae5cfc1c21c20e592315e8094af8c5a9d0126a505276014a6fba47dc8`.
The final diagnostic scan found no LaTeX error, fatal stop, undefined citation,
undefined reference, missing database entry, repeated BibTeX entry, BibTeX
warning, overfull box, or underfull box.  The bibliography checker reported six
cited keys, six entries, and exact source/aux agreement.  PDF metadata reports
seven letter-size pages, the intended title and author, no encryption, and all
listed fonts embedded.  The clean build is accepted.
