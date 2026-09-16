# Build audit

Verdict: **accept**.

The canonical source was cleaned and rebuilt with
`cd manuscript && latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.  The build ran
pdfLaTeX, Biber, and the required settling pdfLaTeX passes, then reported the
target up to date.  The final `manuscript/main.log` contains no LaTeX error,
fatal stop, undefined citation, undefined reference, overfull box, underfull
box, or warning.  `manuscript/main.blg` contains no missing-database-entry,
duplicate-entry, or BibTeX/Biber warning.

The output is a valid, unencrypted five-page PDF with extractable text.  Its
fonts are embedded.  The five cited keys equal the five canonical bibliography
entries; there are no missing or unused entries.  The recorded build-log SHA-256
is `26ab0a7a964d4d9a8676bcce26f16038b1050cd0fe72d0082605cbefe1bde06a`.
