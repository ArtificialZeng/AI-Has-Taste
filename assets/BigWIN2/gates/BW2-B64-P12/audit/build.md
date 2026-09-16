# Clean build report

Verdict: accept

The manuscript was cleaned with `latexmk -C main.tex` and rebuilt from source
in `manuscript/` using

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

The build converged to a five-page PDF.  The final `manuscript/main.log` has
SHA-256 `86ac628cd415288053e73a9ad9296b3c63283ff131730ff14627c6a572876a91`.
The final log and `.blg` contain no undefined citations or references, missing
or repeated bibliography entries, LaTeX errors, fatal stops, undefined control
sequences, runaway arguments, or overfull/underfull box diagnostics.

The bibliography checker found five cited keys, five canonical BibTeX entries,
no missing or unused entries, and exact agreement with the final AUX.  The exact
symbolic verifier also completed successfully.  PDF metadata contains the title,
author, subject, and keywords; the PDF is unencrypted, text-extractable,
letter-sized, and has five pages.
