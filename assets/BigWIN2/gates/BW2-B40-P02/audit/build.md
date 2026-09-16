# Clean build audit

Audit date: 2026-09-06.  The final manuscript was rebuilt from a clean LaTeX
state with

```
cd manuscript
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` converged after BibTeX and a second pdfLaTeX pass and returned exit
status 0.  The final `main.log` and `main.blg` contain none of the following:
undefined citations/references, missing database entries, BibTeX warnings,
repeated entries, LaTeX errors, fatal errors, emergency stops, undefined control
sequences, or runaway arguments.

The bibliography key checker reports seven cited keys, seven BibTeX entries,
zero missing bibliography files, zero missing keys, zero uncited entries, and
exact agreement with all seven `main.aux` bibliography keys.  Cross-references
to the theorem, lemmas, table, and equations resolve in the final PDF.

All fonts reported by `pdffonts` are embedded.  `pdfinfo` reports four letter-size
pages, no encryption, and valid title, author, subject, and keyword metadata.
The final source/PDF digests are bound in `audit/manuscript-snapshot.json`.

Verdict: accept.
