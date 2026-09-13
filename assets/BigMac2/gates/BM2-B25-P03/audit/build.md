# Fresh build audit

Audit date: 2026-09-09. Release job:
`bigMac-00025-p03-release-3e0a1365b5bd`.

I inspected the existing final compiler log `manuscript/main.log`, SHA-256
`64975a79fbc3aa1aa4a1b567dd7d6ba6e5d60a0a3099b4a5e3d5553d1158815c`,
together with `main.blg`, `main.aux`, `main.bbl`, `main.fls`, the extracted
PDF, and PDF metadata.

- pdfLaTeX completed successfully and wrote `main.pdf` with 3 pages and
  292,513 bytes, agreeing with the frozen PDF.
- The final log has no compiler error, fatal diagnostic, LaTeX/package
  warning, undefined reference/citation, multiply-defined label, overfull
  box, or underfull box.
- BibTeX used both database entries; `main.blg` reports zero warnings, and
  `main.aux` maps both citation keys to the two entries printed in
  `main.bbl` and the PDF.
- All cross-references to Theorem 1, Lemma 2, equation (1), and Table 1 are
  resolved in the extracted and rendered PDF.
- `main.fls` shows no imported authored TeX fragment, local style, or figure
  omitted from `publication.json`. The bibliography and four computational
  source/output files described by the authored text are all listed.
- `pdfinfo` reports a valid unencrypted PDF 1.7 with the intended title,
  author, and subject. `pdffonts` reports every font embedded and subsetted.
- `pdftotext` yields nonempty text, including the theorem, table, assistance
  disclosure, and both references.

**Verdict: accept.** The bound build log is clean and describes the current
frozen PDF.
