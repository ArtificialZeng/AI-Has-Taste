# Build audit

The canonical manuscript was rebuilt from cleaned LaTeX intermediates with
`latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`. BibTeX and two converging pdfLaTeX passes completed successfully.
The three citation-parser-incompatible table-resize wrappers were removed;
the unscaled arrays fit within the text block in the clean build.

The final `manuscript/main.log` and `manuscript/main.blg` contain no undefined
citations or references, missing database entries, duplicate entries, BibTeX
warnings, LaTeX errors, fatal errors, emergency stops, undefined control
sequences, runaway arguments, or overfull/underfull box warnings. The
bibliography key checker reports four cited keys, four bibliography keys, and
identical source/aux key sets. The output is a five-page letter-size PDF with
embedded Latin Modern Type 1 fonts and no encryption, forms, or JavaScript.

Final log SHA-256:
`cb6028d5e9cf7b5286a8beb56cb2770bd24ef3a14a857cc47695a55881ed8edf`.
