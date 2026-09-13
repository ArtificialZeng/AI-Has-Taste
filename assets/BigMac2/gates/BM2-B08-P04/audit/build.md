# Clean build audit

**Verdict:** ACCEPT  
**Build command:** `latexmk -cd -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex`  
**Build log:** `manuscript/main.log`

I first ran `latexmk -C -cd manuscript/main.tex`, then performed the stated
build from no generated auxiliary state. Latexmk ran pdfLaTeX, BibTeX, and the
necessary resolving pdfLaTeX pass. The final nonempty `manuscript/main.log`
has SHA-256
`c78e89439d356b29b62e4d7620b34a78862b9e4573a7b89e0f4cdd8bd2a19b8d`.

The final log contains no LaTeX/package warnings, undefined citations,
undefined references, overfull/underfull boxes, errors, or fatal diagnostics.
`manuscript/main.blg` reports two used entries and zero warnings; the generated
`.bbl` contains both cited works. All theorem, equation and bibliography
references resolve in the extracted PDF.

The output is a valid, text-extractable four-page PDF (PDF 1.7). `pdfinfo`
reports the intended title, subject and author, letter page size, no rotation,
and no encryption. The immutable `source.md` still has SHA-256
`ef9b49c782c4ea63b2df51f5da7e2856e06aebf72b9f721bace16feb074e033e`.

