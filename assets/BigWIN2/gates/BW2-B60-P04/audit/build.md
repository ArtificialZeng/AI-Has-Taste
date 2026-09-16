# Build audit

The manuscript was forcibly rebuilt from generated-file cleanup through a
converged `pdflatex`/BibTeX sequence with:

`latexmk -cd -gg -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex`

The command succeeded and produced a four-page PDF. The final
`manuscript/main.log` contains no LaTeX/package warnings, undefined citations,
undefined references, overfull/underfull boxes, errors, emergency stops, or
fatal diagnostics. `manuscript/main.blg` contains no missing database entry,
duplicate entry, or BibTeX warning.

The bibliography consistency checker reports five cited keys, five BibTeX
keys, no missing or unused entries, and exact agreement with the five AUX
`\\bibcite` keys. The exact symbolic certificate also completed successfully,
returning the zero universal identity, the stated observability determinant,
open-set factors `(1,3,1,1,1,2)`, seven candidates, and the six-term support.

The rebuilt PDF SHA-256 is
`ad53e8e3864095811dc9f98e101956299fc1a1761f2f19990b8153a46dacc0c6`.
