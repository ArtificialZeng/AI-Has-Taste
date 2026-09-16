# Build audit

The canonical manuscript was rebuilt from a clean `latexmk -C` state with

```text
cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

BibTeX and three converging pdfLaTeX passes completed with exit status 0.  The
final `manuscript/main.log` and `manuscript/main.blg` contain no fatal error,
LaTeX error, undefined citation or reference, missing database entry, repeated
entry, or BibTeX warning.  The independent bibliography-key checker reports
three cited keys, three database keys, and exact agreement with `main.aux`.

The final PDF has seven letter-sized pages, extractable text, correct title and
author metadata, and 22 embedded subset fonts with Unicode mappings.  Verdict:
**accept**.
