# PDF audit

**Artifact:** `output/pdf/a383733_zero_set_proof.pdf`  
**Audit date:** 2026-08-29 (Asia/Shanghai)  
**Pages:** 5  
**File size:** 348,482 bytes  
**SHA-256:** `29d3ce3524c49628d613a749d5c05673eb47b8c69749107f74e8dc8efccce83b`

## Build gate

- Clean build directory: `/tmp/a383733-build.bZRVeE`.
- Engine: pdfTeX 1.40.29 (TeX Live 2026), orchestrated by latexmk 4.88.
- Bibliography: BibTeX 0.99e with `amsplain`.
- `audit_latex.py`: `cited=4 bib=4 missing=0 unused=0`.
- Final `main.log` and `main.blg`: no `Warning`, `Undefined`, `Overfull`,
  `Underfull`, or `Error` matches.
- PDF metadata: title and author match the manuscript; letter paper,
  unencrypted, no JavaScript or forms.

## Page-by-page visual inspection

Every final page was rendered with Poppler at 144 dpi and inspected at
original rendered resolution.

| Page | Content checked | Result |
|---:|---|---|
| 1 | Title, author, abstract, opening citations, footnote metadata, bottom margin | PASS: no clipping, overlap, missing glyph, broken citation, or crowding |
| 2 | graph definition, modular notation, three-item lemma, displayed equation, section transition | PASS: formulas and list align; proof square and margins are clear |
| 3 | four-family display, junction strings, underbraced half-words, coordinate ranges, section transition | PASS: all subscripts/superscripts and underbraces render sharply; no collision |
| 4 | obstruction proposition, possibility table, sliding-window formula, main theorem, start of certificate section | PASS: table rules/columns align; links and theorem hierarchy are legible |
| 5 | command block, diagnostic numbers, disclosure, four bibliography items, address/email | PASS: long code names and URLs wrap without overflow; final-page whitespace is balanced |

## Visual integrity conclusion

PASS.  The final rendering has no clipping, overlap, black boxes, missing
glyphs, broken tables, or unreadable text.  Page numbers and running headers
are consistent.  The title, equations, theorem statements, references, and
PDF metadata are all legible and correctly positioned.
