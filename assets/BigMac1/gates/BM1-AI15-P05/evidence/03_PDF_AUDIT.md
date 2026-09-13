# PDF audit

Audit date: 2026-08-29.  Status: **PASS**.

## Clean build

The release PDF was built from only `paper/main.tex` and
`paper/references.bib` copied into the newly created directory
`build/clean-20260829-v3`.  The command was:

```text
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error \
  build/clean-20260829-v3/main.tex
```

Build log: `audit/logs/latexmk_clean_v3.log`.  The scan for undefined
citations/references, missing bibliography entries, duplicate entries, TeX
errors, overfull boxes, and underfull boxes is empty in
`audit/logs/latex_all_warning_scan_final.log`.  The independent key checker
found 7 cited keys, 7 bibliography keys, and 7 `.aux` `bibcite` keys with no
differences (`audit/logs/bib_key_check_final.log`).

The resulting PDF has SHA-256
`3064f945793bb825c945fd666b99a47ad596b638f4a23a01e8edd46019b6b98f`,
four US-letter pages, no encryption, no forms or JavaScript, and all fonts
embedded.  Details are in `audit/logs/pdfinfo_final.log` and
`audit/logs/pdffonts_final.log`.

## Page-by-page visual audit

All four pages were rendered at 150 dpi with Poppler.  Rendered-image hashes
are in `audit/logs/rendered_pages_final.sha256`.

| Page | Visual check | Result |
|---|---|---|
| 1 | title, author, abstract, endpoint inequality, introduction, citations, equation (1), section transition, margins | PASS; no clipping, overlap, or malformed glyphs |
| 2 | modular proposition, displayed sets, parameterization, interval theorem, endpoint display, lower-bound formula | PASS; long integers and equations remain within margins |
| 3 | hard-cell argument, killing table, theorem close, trust-split corollary, exact-count table, representative factorization, full certificate digest | PASS; tables and 64-hex digest are complete and legible |
| 4 | scope/nonclaim, proof-assistant disclosure, all seven references, affiliation and email | PASS; bibliography and footer are complete, with balanced final-page whitespace |

Text extraction additionally found the exact new endpoint, the complete final
certificate SHA-256, “global existence problem remains open,” and “not a proof”
scope language (`audit/logs/final_pdf_text.txt`).

## Decision

The PDF is visually and mechanically suitable for release as a paper about a
`NEW_STRICT_BOUND`.  Nothing in it claims that Erdős Problem 647 is solved.
The final source ZIP was also extracted into a new directory and rebuilt; its
warning scan was empty and its extracted text was byte-identical to that of the
release PDF.
