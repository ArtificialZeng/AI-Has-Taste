# Build audit

The canonical publication command was replayed from a cleaned `manuscript/`
directory:

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

It completed successfully and converged after BibTeX and the required LaTeX
reruns.  The final output is a five-page PDF.  `main.log` and `main.blg` contain
no undefined citations or cross-references, absent bibliography records,
duplicate entries, BibTeX warnings, LaTeX errors, fatal errors, emergency
stops, undefined control sequences, or runaway arguments.  The read-only
bibliography checker also found exact agreement among the six TeX, BibTeX, and
AUX keys.  PDF metadata reports the intended title and author, letter-size
pages, no encryption, no forms, and no JavaScript.

Build verdict: **accept**.

This fresh build audit is bound to release job
`win-00071-p02-release-3fccddad94e0`.
