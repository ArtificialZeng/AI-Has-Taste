# Clean build report

Verdict: accept

The manuscript was cleaned with `latexmk -C main.tex` and rebuilt from source
in `manuscript/` using

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

The build converged to a five-page PDF.  `manuscript/main.log` has SHA-256
`d039af2a4b7a239d8226344548ba39411ff259517fbc220aaeddb6699af331f3`.
The final log and `.blg` have no undefined citations or references, missing or
repeated bibliography entries, LaTeX errors, fatal stops, undefined control
sequences, runaway arguments, or overfull/underfull box diagnostics.

The bibliography checker found four cited keys, four canonical BibTeX entries,
no missing or unused entries, and exact agreement with the final AUX.  PDF
metadata contains the title, author, subject, and keywords.  The PDF is
unencrypted, text-extractable, letter-sized, and has five pages.

