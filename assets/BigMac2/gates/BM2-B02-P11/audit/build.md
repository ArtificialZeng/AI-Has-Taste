# Fresh clean-build audit

**Release job:** `bigMac-00002-p11-release-9217dedd5a5f`  
**Build engine:** pdfLaTeX and BibTeX via latexmk 4.88 / TeX Live 2026  
**Final compiler log:** `manuscript/article.log`  
**Final log SHA-256:**
`b4e714176332f1cd314782dc267f16737285bac1b4884b02d07d95fc35e42627`

The prior generated products were removed with `latexmk -C article.tex`.
The declared command was then run from `manuscript/`:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex
```

Latexmk started without an auxiliary file, ran pdfLaTeX, BibTeX, and the
required final pdfLaTeX pass, and reported the target up to date. The final
compiler log, rather than the expected transient first-pass diagnostics, was
audited. It contains no LaTeX warning, overfull or underfull box, undefined
citation/reference, fatal error, or rerun request. `article.blg` reports three
used entries and `warning$ -- 0`. The final `.aux` resolves all equation and
theorem labels and contains `bibcite` records for all three citation keys.

`pdfinfo` reports a valid unencrypted PDF 1.7 file with four letter-size
pages, author Xiaojian Zeng, the intended title and subject, and no forms or
JavaScript. `pdftotext -layout` extracts nonempty text from every page.
`pdffonts` reports that every font is embedded and subsetted. The built PDF
SHA-256 is
`e4fe2283f0543941fd52ebfb947677f271cdad21af5b6cfeb21ad0f2e9977dc9`.

**Verdict: accept.** This is a clean, reproducible build with resolved
citations and cross-references.

