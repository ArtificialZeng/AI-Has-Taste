# Fresh build audit

Verdict: accept.

From `manuscript/`, the canonical command

```
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

forced a full LaTeX--BibTeX--LaTeX rebuild and converged successfully to a
six-page PDF. The final `manuscript/main.log` contains no fatal error, LaTeX
error, undefined citation, undefined reference, emergency stop, or runaway
argument. `manuscript/main.blg` reports five used entries and `warning$ -- 0`.

The bibliography key checker, run against the final `.aux`, found five cited
keys, five bibliography keys, no missing/unused key, and no `.aux` mismatch.
All fonts reported by `pdffonts` are embedded. `pdfinfo` reports an unencrypted,
unrotated six-page letter-size PDF with extractable text.
