# PDF audit

Status: PASS, 2026-08-30.

## Artifact and build

- Final artifact: `output/pdf/nonparry_d4_exact_certificate.pdf`.
- Size: 391074 bytes; SHA-256:
  `20d798c51aefe50b23aa90025316ef13d4a6af99a6e5d7edd749d5af38e65d5e`.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed.
- PDF metadata reports title
  “Every Power of the Perron Root of X4-X-1 Is Non-Parry: An Exact
  Certificate”, author “Zijian Zeng”, 7 letter-size pages, and no encryption.
- `pdffonts` reports every font embedded and subsetted.
- Extracted-text checks found the theorem, author affiliation, and both email
  addresses. They found no unresolved references, placeholder text, hash,
  internal route/role identifier, completion/confidence field, or internal AI
  audit language in the manuscript.
- The citation-key audit reports `cited=4 bib=4 missing=0 unused=0`. There are
  no overfull boxes, undefined citations/references, or substantive warnings.
  One underfull bibliography line is cosmetic and does not impair readability.

## Page-by-page visual inspection

The final PDF was rendered at 144 dpi after its last source change. Every page
was inspected from that final rendering.

1. Title, author, abstract, opening definitions, and foot matter are aligned
   and readable; no clipped lines or missing glyphs.
2. Main theorem and algebraic root lemma are complete; fractions, radical,
   factorization, equation tags, and proof-ending box render correctly.
3. Cutoff and escape lemmas are complete; exact-1 recurrence, tail formulas,
   and section transition are correctly spaced.
4. The seven-row witness table and every final-state/norm formula fit within
   the text block; the long first digit word is legible.
5. The seven finite cases and the infinite cutoff proof are complete; all
   strict inequalities and verifier names render correctly.
6. Reproduction commands, limitations, disclosure, and all seven appendix
   polynomials are present and readable.
7. All four references, affiliation, location, and both email addresses are
   present; the large lower whitespace is the natural end of a references
   page, not missing content.

No page has overlap, clipping, a black box, an unintended blank region, a
missing character, or an unreadable formula.

## Source archive

- Archive: `output/latex/nonparry_d4_exact_certificate_latex.zip`.
- Size: 15285 bytes; SHA-256:
  `07c925949327ea4cc0f8603b7950acc72893f3caff54955e4b6e213306c76232`.
- The archive was unpacked into a newly created empty directory. Both exact
  verifiers passed there, `latexmk` produced a 7-page PDF, and the independent
  citation audit again reported no missing or unused bibliography key.
