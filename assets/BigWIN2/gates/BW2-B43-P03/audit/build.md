# Clean-build audit

Verdict: **accept**.

After the PDF metadata repair, the manuscript was cleaned and rebuilt with

`cd manuscript && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

The final converged `manuscript/main.log` is nonempty, has SHA-256
`044c9fc4ce1a18e37ba182c62cc9edc8f671aa3da40ef1282ac6ac527bfad8a2`,
and reports a four-page PDF.  The final log and `.blg` have no LaTeX error,
fatal error, undefined reference/citation, missing BibTeX database entry,
duplicate entry, or BibTeX warning.  The BibTeX key checker reports exact
source/`.bib`/`.aux` agreement for all three keys.  All PDF fonts reported by
`pdffonts` are embedded.  `pdfinfo` reports the expected title and author,
letter page size, no encryption, and four pages.

