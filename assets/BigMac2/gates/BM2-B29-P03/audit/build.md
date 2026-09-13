# Fresh build audit

## Bound artifact

- Release job: `bigMac-00029-p03-release-c1fda9dfb459`.
- Evidence snapshot: `742b93162211e835fe67ffd8e2ed442a562f83e734d6b3030d5534c3dd21d7f5`.
- Manuscript snapshot: `e5e03004830aff9dab501eb34a552ddcc086782f9fb316694afae43b5ddcf856`.
- PDF: `09e3f5ce396a5ad4c2127b40e9d26512f5c0fb27fb87c6a3da73d2e9732a2819`.
- Build log: `manuscript/article.log`, SHA-256
  `b11d21e092ab0014b895e9ae173db4349149009a8cf739be4648e9b877e90276`.

## Clean build

From `manuscript/`, I first ran `latexmk -C article.tex`, then the declared
command

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex
```

Latexmk 4.88 performed a fresh pdfLaTeX/Biber/pdfLaTeX sequence using TeX Live
2026 and Biber 2.21, then reported all targets up to date.  Biber found all
three citation keys in `references.bib`.  The stable final compiler log is
nonempty and reports a five-page `article.pdf`.

I inspected the final log, not the transient first-pass console output.  It has
no LaTeX or package warning, fatal error, undefined reference, undefined
citation, overfull box, or underfull box.  Cross-references, table references,
theorem references, and bibliography citations resolve in extracted PDF text.
`pdfinfo` identifies a valid unencrypted A4 PDF with the intended title and
author.  `pdftotext` produces nonempty text.  `pdffonts` reports every font as
embedded and subsetted.

## Verdict

**Accept.**  The build is clean, reproducible from the complete declared source
set, and the bound log is the stable final-pass log.
