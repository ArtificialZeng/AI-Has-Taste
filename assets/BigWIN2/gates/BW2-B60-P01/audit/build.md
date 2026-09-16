# Clean build audit

The manuscript was cleaned with `latexmk -C main.tex` and rebuilt from the
canonical sources using
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`.  BibTeX and the required subsequent pdfLaTeX passes converged.

The final `manuscript/main.log` is nonempty and contains no unresolved
citation/reference diagnostic or TeX error.  The BibTeX log contains no missing
database entry, repeated entry, or warning.  `pdfinfo` reports a valid seven-page
letter-size PDF 1.5.  `pdffonts` reports that every listed font is embedded and
subsetted with Unicode mapping.  The PDF has extractable text.

**Verdict: accept.** The clean build and its final log are reproducible from
the complete source list in `publication.json`.
