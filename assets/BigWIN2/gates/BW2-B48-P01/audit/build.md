# Build audit

The canonical source was rebuilt from regenerated intermediates with

`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`

in `manuscript/`. BibTeX and the required subsequent pdfLaTeX pass completed, and the final converged `manuscript/main.log` contains no undefined citation/reference, missing database entry, repeated entry, LaTeX error, fatal error, emergency stop, undefined control sequence, or runaway argument diagnostic.

The bibliography checker reports three cited keys, three BibTeX keys, no missing bibliography files, no cited keys missing from the bibliography or AUX file, and no unused bibliography keys. `pdfinfo` reports a valid four-page letter-size PDF with nonempty title, author, subject, and keywords. `pdffonts` reports every listed font embedded. `pdftotext` extracted nonempty text (315 lines, 1,610 words).

Verdict: accept; clean reproducible build.
