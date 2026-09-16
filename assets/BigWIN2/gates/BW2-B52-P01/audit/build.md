# Clean build audit

On 2026-09-07 the generated LaTeX products were cleaned with `latexmk -C
main.tex` and rebuilt from `manuscript/main.tex` and
`manuscript/references.bib` using:

```
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The converged build produced a four-page PDF.  `manuscript/main.log` contains
no fatal error, undefined citation, undefined reference, or rerun request.
`manuscript/main.blg` contains no missing database entry, warning, or repeated
entry.  The bibliography checker reports three cited keys, three BibTeX keys,
zero missing/unused keys, and exact agreement with the final `.aux`.

PDF information and font inspection succeeded.  Every listed font is embedded;
the PDF has extractable text, valid metadata structure, no encryption, no form,
and no JavaScript.
