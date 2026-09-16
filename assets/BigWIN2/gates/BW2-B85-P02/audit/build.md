# Clean build audit

The generated-file state was cleaned and the publication command was executed:

\`pdflatex -interaction=nonstopmode -halt-on-error main.tex\`, \`bibtex main\`,
and three converging \`pdflatex\` passes.  The final pass exited 0; its log is
saved as \`audit/build.log\`, and it produced the current four-page PDF.

The final LaTeX and BibTeX logs contain no undefined citations or references,
missing database entries, repeated entries, LaTeX errors, fatal errors,
emergency stops, undefined control sequences, or runaway arguments.
\`check_bib_keys.py\` reports identical four-key sets in the body, bibliography,
and AUX.  The only typesetting diagnostic is a non-fatal underfull box in one
bibliography paragraph; rendered-page inspection confirms that it is legible
and within the margins.

PDF inspection reports A4 pages, four pages, no encryption, an intact PDF-1.5
header, embedded vector fonts, and extractable text.

**Verdict: ACCEPT.**
