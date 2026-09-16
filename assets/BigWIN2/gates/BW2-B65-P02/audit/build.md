# Clean build audit

**Verdict:** accept. The final build is bound to manuscript digest
`0da936705ab0cf058273a7011cafc6e356f009fe9839401d2bb04a2ba38db508`
and PDF digest
`2484660967e3aa26e86828bd2ef8afbcc9919639a8bad59b86f02dee1d482177`.

From `manuscript/`, `latexmk -C main.tex` removed the prior derived build
state, after which

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

ran pdfLaTeX, BibTeX, and the required rerun to convergence. It produced a
four-page PDF. A final scan of `main.log` and `main.blg` found no undefined
citations or references, missing database entry, BibTeX warning, duplicate
entry, LaTeX error, fatal stop, runaway argument, overfull box, or underfull
box.

The bibliography checker reports three cited keys, three bibliography keys,
and three `.aux` bibliography keys, with all set differences empty. The final
log SHA-256 is
`fa8b1b474c4a0e562762625329fe86fc7585569d25143fa23d96526c9695730e`.
All 23 fonts reported by `pdffonts` are embedded, subsetted, and Unicode
mapped. `pdfinfo` reports four unrotated letter-size pages and the intended
title, author, subject, and keywords.
