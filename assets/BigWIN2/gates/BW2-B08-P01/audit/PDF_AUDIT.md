# PDF audit

Status: PASS.

Final file: `results/whiskered_wlp_n8.pdf`.

- Built from `paper/main.tex` with `latexmk`/pdfLaTeX and BibTeX.
- Three pages; PDF metadata title and author are correct.
- Final LaTeX log contains no undefined references or citations, errors,
  overfull boxes, underfull boxes, or warnings.
- `audit_latex.py` reports `cited=4 bib=4 missing=0 unused=0`.
- Every page was rendered at 120 dpi and inspected in
  `audit/pdf_final_reaudit/`.
- No clipping, overlap, missing glyphs, black boxes, broken table rules, or
  anomalous final-page whitespace was observed. The former address-only fourth
  page was eliminated; the address and both email addresses now fit cleanly at
  the end of page 3.
- The searchable PDF text contains no prompt, model/vendor name, internal
  workflow description, or checksum-like string.
