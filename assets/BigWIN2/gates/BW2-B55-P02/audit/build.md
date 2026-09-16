# Build audit

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged
successfully with BibTeX and produced a three-page PDF.  The bibliography-key
checker reports four cited keys, four bibliography keys, and the same four AUX
keys, with all missing and extra sets empty.  A final scan of `main.log` and
`main.blg` found no undefined citation/reference, missing database entry,
BibTeX warning, repeated entry, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.  All PDF fonts are embedded;
the title and author metadata are present.
