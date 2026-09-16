# Clean-build audit

From `manuscript/`, the command

`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`

completed successfully through pdfLaTeX, BibTeX, and the converging pdfLaTeX
pass.  The final artifact has five letter-size pages.  The final `main.log` and
`main.blg` contain none of the audited fatal/error, undefined-citation,
undefined-reference, missing-database-entry, repeated-entry, or BibTeX warning
patterns.  The bibliography checker reports five cited keys, five BibTeX keys,
five `.aux` `\\bibcite` keys, and empty set differences.

All PDF fonts are embedded and subsetted.  `pdfinfo` reports the expected title
and author after enabling `pdfusetitle`.  Verdict: **accept**.
