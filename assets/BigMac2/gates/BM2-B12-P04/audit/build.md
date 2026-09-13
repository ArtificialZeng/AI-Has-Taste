# Clean-build audit

The two frozen authored inputs were rebuilt from a clean auxiliary state with:

`latexmk -C article.tex`

`latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex`

The build completed under pdfTeX 1.40.29 and BibTeX 0.99e. The final compiler
log is `manuscript/article.log`, SHA-256
`b610d1149d605e28cb1386306e496a036d86989cac2d9806aa8d469e24a63c97`.
The final pass reports a 3-page, 300789-byte PDF and contains no LaTeX/package
warnings, undefined or multiply-defined references, undefined citations,
overfull/underfull boxes, fatal errors, or rerun requests. `article.blg` likewise
contains no warning or error. The bibliography resolves both cited keys.

`pdfinfo` confirms the intended title, author, subject, three letter-size pages,
no encryption, no forms, and no JavaScript. `pdffonts` shows every font embedded
and subsetted with Unicode mappings. `pdftotext` extracts nonempty readable text.
The rebuilt PDF was then frozen as PDF digest
`11f776b1f55c085ad6311c2761b9803a43da4ff404a1f8268bcd3d093c65a07c`.

**Verdict: accept.** The bound log is the real final log from a clean successful
build.

