# Build audit

Pass. A clean build was performed after `latexmk -C` using

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd manuscript/main.tex
```

The converged build produced `manuscript/main.pdf` with four letter-size pages.
The final `main.log` and `main.blg` contain no undefined citation, undefined
reference, missing database entry, repeated entry, LaTeX error, fatal error,
emergency stop, or BibTeX warning. The bibliography key checker reports two
cited keys, two bibliography entries, no missing or unused entry, and exact
agreement with `main.aux`.

`pdfinfo` confirms a nonempty title, author, subject, and keywords. `pdffonts`
shows every font embedded and subset. Text extraction is nonempty, all theorem,
equation, table, and bibliography references resolve, and the source/PDF hashes
match `audit/manuscript-snapshot.json`.
