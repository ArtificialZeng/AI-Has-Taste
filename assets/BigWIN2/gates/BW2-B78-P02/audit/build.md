# Build audit

Release job: `win-00078-p02-release-382a564d0f4a`.

The canonical manuscript was rebuilt from generated-output cleanup with the
configured pdfLaTeX/BibTeX workflow. The cleanup invocation of `latexmk -gg`
produced the first pdfLaTeX pass but returned before dependency convergence;
a fresh ordinary `latexmk -pdf` invocation then ran BibTeX and two required
pdfLaTeX passes and exited successfully. This left no inherited AUX or BBL
result as the final authority. The converged command was

```
cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The final `manuscript/main.log` has SHA-256
`25b8cfd7d52aa5c1125f82bb3fe4be50a1c10283f406279cd6b1ef50834f9a1c`.
It and `main.blg` contain no undefined citation or reference, missing database
entry, repeated entry, LaTeX/BibTeX warning, fatal error, overfull box, or
underfull box. The bibliography checker reports four cited keys, four database
entries, and exact TeX/AUX agreement.

`pdfinfo` recognizes a five-page A4 PDF with the declared title and author.
Every listed font is embedded and subsetted, and the PDF has extractable text.
`qpdf` is not installed; this did not replace or weaken the successful engine,
log, metadata, font, text-extraction, and all-pages rendered visual checks.

Verdict: **accept**.
