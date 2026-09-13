# Fresh build audit

The publication was rebuilt from a cleaned auxiliary state with

`cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex`.

The command completed successfully and produced the current three-page
`manuscript/article.pdf`.  The final `manuscript/article.log` is nonempty and
has SHA-256
`ea92fbf68df031ccbe3a6034feff0d7199b396bbf592570aba0bed42f2ad26d7`.
Inspection of the final log, BibTeX log, auxiliary file, bibliography, and
extracted PDF found no compilation failure, unresolved citation/reference,
multiply defined label, overfull/underfull box, or rerun request.  BibTeX
reports zero warnings.

The recorder file confirms that the only authored compilation dependencies are
the two files declared in `publication.json`: `manuscript/article.tex` and
`manuscript/references.bib`; remaining inputs are system TeX resources.  PDF
metadata contain the intended title, author, subject, and keywords.  All fonts
reported by `pdffonts` are embedded, the `%PDF-` document is unencrypted, and
`pdftotext` yields nonempty readable text.

**Verdict: accept; clean build.**
