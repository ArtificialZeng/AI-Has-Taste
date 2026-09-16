# Clean build audit

**Verdict: accept.**  Release job
`win-00073-p02-release-1f8a76d1e73a` ran `latexmk -C main.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`.  Latexmk ran the initial pdfLaTeX pass, BibTeX, and the
converging pdfLaTeX pass, exited 0, and reported all targets current.  Only the
final converged log is used for the verdict.

The final `manuscript/main.log` has SHA-256
`55a89dd7df451f41d7d1239c98cd6e1c74ab76307c7afe95215dc9eb3d545bfa`.
Targeted scans of `main.log` and `main.blg` found no undefined citation or
reference, missing database entry, BibTeX warning, duplicate entry, LaTeX
error, fatal error, emergency stop, undefined control sequence, or runaway
argument.  The bibliography checker reports 3 cited keys, 3 present and used
entries, and exact source/aux agreement.

The resulting PDF is valid, unencrypted, text-extractable, letter-sized, and
four pages long.  All 20 reported fonts are embedded and subsetted.  Its
SHA-256 is
`3da48aeeb45362f6198f6fce0d234affc709f83f76bd4afeca6e6ce22d918a19`.
