# Clean build audit

The canonical manuscript was cleaned with `latexmk -C main.tex` and rebuilt
from `manuscript/` using
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. BibTeX and
the repeated pdfLaTeX passes converged successfully to a six-page PDF.

The final `manuscript/main.log` has SHA-256
`fbd4bd6aa5a64aeea7edb58e9bb960a20f52dce93b5c94e488ce2c468d72c05e`
and contains no LaTeX error, fatal error, emergency stop, undefined citation,
undefined reference, label-change warning, or rerun request.
`manuscript/main.blg` contains no missing database entry, repeated entry, or
BibTeX warning. The bibliography checker reports five cited keys, five database
keys, zero missing/unused keys, and exact `.aux` agreement.

PDF metadata contains the expected title, author Xiaojian Zeng and subject; the
document is A4, six pages, unencrypted, text-extractable, and contains no
JavaScript. Its SHA-256 is
`42e1ea24156ea470457f10aeea1a6eb8bc562b474e3bd7c2c552006c705d57d4`.

**Verdict: accept.**

