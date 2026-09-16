# Clean build audit

## Verdict

**Accept.** From `manuscript/`, I ran `latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. BibTeX and the
necessary repeated pdfLaTeX pass completed successfully, producing a four-page
PDF. A final latexmk check reported all targets up to date.

The final log is `manuscript/main.log` with SHA-256
`4f0b561d85c2db0c935c583fa48251f3eb0346e4c7c7d0d0050be662566f0f6e`.
The resulting PDF has SHA-256
`78a340f5cf56d2ab778921aaa8b5608f8db7a0c2dc9fb0d798ddb900f06cec72`.

The BibTeX key checker found four cited keys, four database entries, no missing
or unused entries, and exact agreement with `main.aux`. Scanning the converged
`main.log` and `main.blg` found no undefined citations or references, missing
database entries, duplicate entries, BibTeX warnings, LaTeX errors, fatal
errors, undefined control sequences, or runaway arguments. Cross-references,
table numbering, mathematical symbols, and bibliography links resolved.
`pdfinfo` reports the visible title and author exactly as the PDF Info `Title`
and `Author` values.
