# Build audit

**PASS.**  From `manuscript/`, I removed prior LaTeX-generated intermediates
with `latexmk -C main.tex` and ran
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.  BibTeX ran
against the canonical `references.bib`, and `latexmk` converged after the
required reruns.

The final `manuscript/main.log` and `manuscript/main.blg` contain no undefined
citations or references, missing database entries, BibTeX warnings, repeated
entries, fatal errors, emergency stops, undefined control sequences, runaway
arguments, overfull boxes, or underfull boxes.  The independent key checker
found four cited keys, four BibTeX entries, four `.aux` bibliography keys, and
zero missing, unused, or mismatched keys.  The output is a three-page PDF with
extractable text and resolved cross-references.
