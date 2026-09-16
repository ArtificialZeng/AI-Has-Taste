# Clean build audit

The canonical command

`cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

was run after `latexmk -C main.tex`. BibTeX and subsequent pdfLaTeX passes
converged normally to a four-page PDF. The final `manuscript/main.log` and
`manuscript/main.blg` contain no undefined citation/reference, missing database
entry, repeated entry, LaTeX/package warning, error, emergency stop, overfull
box, or underfull box. The independent key checker reports four cited keys,
four BibTeX keys, no missing or unused entry, and exact AUX agreement.

`pdfinfo` reports the intended title and author, four letter-size pages, and a
valid PDF 1.5 file. `pdffonts` reports every font embedded and subsetted. The
accepted evidence snapshot remains unchanged; the rebuilt PDF was refrozen in
`audit/manuscript-snapshot.json` before this audit.
