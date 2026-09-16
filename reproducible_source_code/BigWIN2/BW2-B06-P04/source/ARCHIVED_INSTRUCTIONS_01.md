# Build instructions

The archive is self-contained apart from a standard LaTeX installation with
`amsart`, `lmodern`, `mathtools`, `booktabs`, `xcolor`, and `hyperref`.

From the extracted directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The resulting manuscript is `main.pdf`.  To remove generated files, run
`latexmk -C main.tex`.
