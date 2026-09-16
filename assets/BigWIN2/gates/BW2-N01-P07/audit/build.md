# Clean build audit

Verdict: accept. Job: `newwin-00001-p07-release-eea8aff93c71`. UTC review: 2026-09-12T08:35:50.951410+00:00.

The release worker ran the clean command and then the complete build from `manuscript/`, capturing both exit statuses as zero in `audit/release-build-transcript.log`:

```
latexmk -C -outdir=build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

The final product `manuscript/build/main.pdf` has four letter-size pages and extractable text. The final TeX log and BibTeX log contain no undefined citation/reference, database missing entry, duplicate entry, error, warning, missing glyph, overfull or underfull box. The final BibTeX run regenerated `main.bbl`; source, bibliography and aux contain exactly the same four keys. `audit/bib-key-check.txt` records the independent skill checker output. Intermediate first-pass warnings in the transcript are resolved by the converged final logs.

`audit/pdfinfo.txt` confirms the requested title and Xiaojian Zeng author metadata. `audit/pdffonts.txt` reports all 20 listed fonts embedded and subset; the PDF contains no form or JavaScript. `audit/release-pdf-text.txt` was checked against the authored statements, numerical values, assistance disclosure and bibliography. The source dependencies are exactly the four publication source files, with standard installed TeX packages and plainurl; no additional authored figure, TeX fragment or local style is used. Supplement integrity is recorded in `audit/release-supplement-check.json`.

The one selected citation was changed to ordinary direct `\cite{ZengEtAl2026}` with its Section 6 locator in prose. No mathematical statement changed. The accepted evidence files were never rebuilt or overwritten.

Accepted mathematical snapshot: `fe32cd463141d526a90ca7859d55059aa1c6d3392a12234796cdd4a3af87ba8e`.
Manuscript digest: `9b400315173b3f139418af88297c0b16a3cb6a2e7e69400d2159eaef4ce21e18`.
PDF digest: `06151776bf758df940a752315bb7beb008e876a8624db1f50f278b49323ed0b5`.
