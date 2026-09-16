# Clean-build audit

Verdict: **accept**.

The manuscript was rebuilt from cleaned generated files with

```text
latexmk -cd -gg -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex
```

BibTeX and three pdfLaTeX passes converged successfully to a four-page A4 PDF.
The final `manuscript/main.log` has SHA-256
`6be08ebf3ae24772639bcefbf4fc8006ef1f503ee864820620e988e8ad0d8097`.
The final log and BLG contain no undefined citation, missing database entry,
repeated entry, undefined reference, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.

The bibliography-key checker reported three cited keys, three BibTeX keys, no
missing or unused entries, and exact agreement with `manuscript/main.aux`.
All fonts reported by `pdffonts` are embedded. `pdfinfo` reports the intended
title and author, four pages, no encryption, no JavaScript, and no suspect flag.
The exact certificate also reran successfully and reproduced 32767 cases,
294903 tested coefficients, zero negative coefficients, and its frozen digest.
