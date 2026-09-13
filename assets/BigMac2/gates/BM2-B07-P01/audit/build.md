# Fresh clean-build audit

Audit job: `bigMac-00007-p01-release-73c3ff96116c`; audit date: 2026-09-08.

The current frozen manuscript/PDF state was produced from a clean TeX state
with

```text
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

I freshly inspected the complete dependency declaration, `.fls`, `.blg`,
`.bbl`, extracted PDF, PDF metadata, fonts, and the final compiler transcript.
The declared authored dependencies are complete: `main.tex` imports no local
TeX/figure/style file, uses `references.bib`, and names the accompanying
certificate in the prose.  `latexmk` completed successfully after the required
BibTeX and LaTeX passes.  The nonempty existing final build log is
`manuscript/main.log`, SHA-256
`4c38c5224f696bd5f78846fc2c8b16ab5752f6ba0e9671ebadaa54b9d6eda219`.
Direct inspection and diagnostic searches found no LaTeX or package warnings,
undefined citations or cross-references, rerun request, overfull/underfull box,
fatal error, or emergency stop in that final log.

The output has a valid PDF 1.7 header, four letter-size pages, and nonempty
text extraction.  `pdfinfo` reports the intended title, author, subject, and
keywords.  `pdffonts` reports every used font as embedded and subsetted with
Unicode mapping.  The extracted bibliography contains all three resolved
entries, including the corrected author name “Shenxing Zhang.”  The PDF bound
by the current manuscript snapshot has SHA-256
`53197fd923d493f4a3bf1bd7351ffb47945e90ab77357feec09307a31491aaa7`.

Verdict: **accept**; `clean_build=true`.
