# Fresh clean-build audit

**Verdict: ACCEPT.** I ran `latexmk -C article.tex` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex` in
`manuscript/`. BibTeX and the required repeated LaTeX pass completed, and
`latexmk` reported the target up to date after the final pass.

The current compiler transcript is `manuscript/article.log`, SHA-256
`5cd2bc8a687f09510b2e4feedf007e948b224fa2fd69f125c4d97b0d1286fb88`.
Inspection of that final log and `manuscript/article.blg` found no compilation
failure, undefined citation, undefined cross-reference, rerun request,
overfull/underfull box, or package warning. The generated `.bbl` contains all
three cited entries. `pdfinfo` reports six letter-size pages, embedded metadata
gives the intended title and author, and `pdftotext` produces nonempty text
containing the theorem, equations, and resolved bibliography.

The clean PDF is `manuscript/article.pdf`, SHA-256
`d72ea2216e7a5780f2e82b744acf6d9ea358cc709e74644858d419d084a961cf`.
Its `%PDF-` structure, page count, and text extraction are valid. The build did
not change either authored source or the frozen research evidence.
