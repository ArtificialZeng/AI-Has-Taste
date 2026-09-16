# Build audit

Release job `win-00086-p05-release-d366fb9aae22` performed a clean rebuild from `manuscript/main.tex` with the canonical publication command:

`cd manuscript && latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`

BibTeX and the converging LaTeX pass completed successfully and produced a three-page PDF. The final `manuscript/main.log` contains no undefined citation/reference, missing database entry, repeated entry, LaTeX error, fatal error, emergency stop, undefined control sequence, or runaway-argument diagnostic. The canonical citation-key checker reports four cited keys, four bibliography entries, and exact agreement with the final AUX file.

Verdict: accept; clean converged build.
