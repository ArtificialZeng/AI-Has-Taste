# Fresh clean-build audit

**Overall status:** PASS

The publication command from `publication.json` was run from an empty LaTeX
build state:

```text
cd manuscript && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` 4.88 completed successfully with pdfTeX 1.40.29 and BibTeX 0.99e.
The final `manuscript/main.log`, SHA-256
`8ed49bc2b11d57a8c8e80eaee30494f30e731b7c4ee5dcfda1eceec701a1415e`,
contains no LaTeX/package warnings, errors, undefined references or citations,
multiply-defined labels, missing characters, or overfull/underfull boxes.
`manuscript/main.blg` likewise contains no warning or error.

The final PDF is readable by `pdfinfo` and `pdftotext`, has seven US-letter
pages, and carries the intended title and author metadata.  `pdffonts` reports
every listed Latin Modern and AMS font as embedded and subsetted with Unicode
mapping.  The final PDF digest is
`a67625fdee7b78d31ddcd920ba26907cd9c91c7770a013844994d78d1e52a1a6`.

Dependency inspection found no included TeX files, graphics, or other authored
inputs beyond `manuscript/main.tex` and `manuscript/references.bib`, exactly the
two `source_files` frozen in `publication.json`.  Both citations and all
cross-references resolve in the final pass.

