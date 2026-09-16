# Clean-build audit

Release job: `win-00087-p02-release-03572e9b7dea`

The canonical manuscript was rebuilt from a cleaned auxiliary state with
`cd manuscript && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode
-halt-on-error main.tex`.  BibTeX and PDFLaTeX converged successfully to a
four-page PDF.

The final `main.log` and `main.blg` contain no undefined citation or reference,
missing database entry, repeated entry, BibTeX warning, LaTeX error, fatal stop,
runaway argument, overfull box, or underfull box.  The bibliography checker
reports six cited keys, six present entries, and exact AUX agreement.  PDF
metadata give the manuscript title and Xiaojian Zeng as author; all fonts are
embedded Type 1 fonts, pages are US letter, and the file has no encryption,
forms, or JavaScript.  Status: **PASS**.
