# Fresh clean-build audit

The publication was rebuilt from the current `main.tex` and `references.bib`
with

```text
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex
```

from the `manuscript` directory.  `-gg` forced a full cleanup and remake.
The run executed pdfLaTeX, BibTeX, and the required final pdfLaTeX pass and
exited successfully.  The current compiler transcript is
`manuscript/main.log`, SHA-256
`d538b8de9a36c2c38a12501ce6972a84393af07ba7d14e61bf286f2a621966a2`.

The final log has no compilation error, undefined reference, undefined
citation, multiply defined label, rerun request, overfull box, or underfull box.
`main.aux` resolves `shin2026` and `zhang2026` to bibliography entries 1 and 2
and records every equation, theorem, table, and section reference.  The BibTeX
log reports two used entries and zero warnings.  The recorder confirms that
the only authored project inputs are `main.tex` and `references.bib`; auxiliary
files are generated build products.

The output is a valid, unencrypted four-page PDF 1.7 file with nonempty text
extraction.  Its title, author, subject, and keywords match the source.  All 16
listed fonts are embedded subsets with Unicode mappings.  Build verdict:
**accept**.
