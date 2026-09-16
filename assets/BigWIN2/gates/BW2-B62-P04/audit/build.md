# Clean-build audit

From `manuscript/`, the command

`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`

completed successfully through pdfLaTeX, BibTeX, and the converging pdfLaTeX
pass. The final artifact has four letter-size pages. The final `main.log` and
`main.blg` contain none of the audited fatal/error, undefined-citation,
undefined-reference, missing-database-entry, repeated-entry, or BibTeX warning
patterns. The bibliography checker reports four cited keys, four BibTeX keys,
four `.aux` `\\bibcite` keys, and empty set differences.

`pdfinfo` reports the expected full title and author metadata. `pdffonts` reports
that every font is embedded and subsetted. Verdict: **accept**.
