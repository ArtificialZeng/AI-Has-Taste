# Clean-build audit

The manuscript build was started from
`latexmk -C -cd manuscript/main.tex`, followed by the convergent command
`latexmk -pdf -interaction=nonstopmode -halt-on-error -cd manuscript/main.tex`.
Latexmk ran the required BibTeX and PDFLaTeX passes non-interactively.

For release job `win-00076-p03-release-f17ba9de4d6f`, the final command exited
successfully and produced a three-page PDF.  The final
`manuscript/main.log` SHA-256 is
`08705ded2c853c236bb19595f41af64d78390564e56405762bd901433c74b11e`.
The required diagnostic scan of `main.log` and `main.blg` was empty.  The
read-only bibliography checker found five cited keys, five database keys, no
missing or unused keys, and exact agreement with `main.aux`.

`evidence/verify_witness.py` was rerun successfully under exact SymPy
arithmetic: all 64 ordered Jacobi triples passed, generation rank was four,
the vertical traces were `[-y,x,0]`, the horizontal trace was `1+x+y`, and its
remainder modulo the vertical ideal was `1`.

`pdfinfo` reports the intended title, author Xiaojian Zeng, letter page size,
no encryption, and three pages.  `pdffonts` reports that every font is embedded
and subset.  Build verdict: accept.
