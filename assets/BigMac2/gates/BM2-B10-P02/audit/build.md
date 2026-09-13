# Fresh build audit

Release job: `bigMac-00010-p02-release-93e775dd2753`

The manuscript was rebuilt from a clean generated-file state with

```text
cd manuscript
latexmk -C paper.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The clean run executed BibTeX and the required LaTeX reruns, exited zero, and
produced a five-page PDF.  I inspected the final compiler transcript
`manuscript/paper.log`, whose SHA-256 is
`a0fd123bb7fdb2f44bedbced56b4da4ae264e7a818cc9c81b3e31aeab80cae7f`.
It contains no fatal/error diagnostic, unresolved reference or citation,
multiply defined label, overfull/underfull box, package warning, or rerun
request.  `paper.blg` likewise reports no BibTeX warning or error.

`pdfinfo` reports an unencrypted five-page letter-size PDF, and `pdftotext`
extracts nonempty text including both numbered references.  `pdffonts` shows
that every listed font is embedded.  The final PDF SHA-256 is
`a0163022d03e98b7dac015a83a4b7c8cced1a502ec306d31f857da1e2fdd0a17`,
matching the current manuscript snapshot.

**Verdict:** accept; clean build verified.
