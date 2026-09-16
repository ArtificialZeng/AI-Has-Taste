# LaTeX source

Build the manuscript with a standard TeX Live installation:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The source uses the `amsart` class and the packages listed in `main.tex`.
Bibliographic records are in `references.bib` and are processed by BibTeX.

The exact computational certificate is distributed separately as the
ancillary archive; it is not required merely to typeset the paper.
