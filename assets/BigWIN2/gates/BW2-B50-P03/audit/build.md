# Clean build audit

The canonical build command from `publication.json` was run from a clean
auxiliary state:

```
cd manuscript
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build converged successfully under pdfTeX/LaTeX with BibTeX and produced a
four-page PDF.  The final `manuscript/main.log` and `manuscript/main.blg` contain
no LaTeX error, fatal error, emergency stop, undefined control sequence,
undefined citation, undefined cross-reference, missing database entry, repeated
entry, or BibTeX warning.  The first pass's expected transient undefined labels
were resolved by latexmk and do not occur in the final log.

The bibliography checker reports four cited keys, four database keys, four
final AUX keys, no missing bibliography file, no missing or unused key, and no
AUX mismatch.  Cross-references to Theorem 1, Lemmas 2--3, and Table 1 resolve
in the rendered PDF.  PDF metadata now contains the manuscript title, author,
and subject.

Verdict: accept; the clean build and final logs are release-ready.
