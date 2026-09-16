# Build audit

Release job: `win-00086-p08-release-c24024c4e62f`.

The canonical manuscript was force-rebuilt from `manuscript/main.tex` with
BibTeX by

```
cd manuscript && latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build main.tex
```

The build converged after BibTeX and the required pdfLaTeX passes.  The final
`build/main.log` has SHA-256
`38240b26dd456b7f3b91d5622ab8af2f130adf382f70bc3afc08aeec5b8643c8`
and contains no undefined citation/reference, missing database entry,
duplicate entry, LaTeX/BibTeX warning, fatal error, overfull box, or underfull
box.  The bibliography checker reports four cited keys, four database entries,
and exact TeX/AUX agreement.

`pdfinfo` recognizes a four-page US-letter PDF with the declared title,
subject, and author.  All listed fonts are embedded and subsetted.  The PDF has
extractable text and a valid PDF header.  `qpdf` was not installed; this did not
replace or weaken the successful engine, log, `pdfinfo`, font, text-extraction,
and rendered-page checks.

Verdict: **accept**.
