# Build audit

**Accept.** The canonical command

```text
cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

converged successfully and produced a five-page PDF. The final build log is
`manuscript/main.log` with SHA-256
`8cbd2fdc5ff9ae831c2ddc2f8f8002ab5e5b51ee053a9f288a6c30d36e15b060`.
The log and `.blg` have no LaTeX/BibTeX error, fatal stop, undefined citation or
reference, missing database entry, repeated entry, overfull box, underfull box,
or warning diagnostic. The BibTeX key checker also passed with three cited and
three defined keys and exact `.aux` agreement.

`pdfinfo` recognizes a valid unencrypted five-page letter-size PDF and records
the manuscript title and Xiaojian Zeng as author. `pdffonts` reports every used
font embedded and subsetted. The final PDF digest is
`dcdfeb1616fcf784641d232cf24e9d53141188a4bc125743bb7b94f00e04d7e7`.
