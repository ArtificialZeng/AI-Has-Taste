# PDF audit

Status: **PASS** (2026-08-29, Asia/Shanghai).

## Audited artifact

- Isolated build directory: `tmp/pdfs/clean-build-terminal-v3.mxMjvR`
- PDF: `main.pdf`
- SHA-256: `22426d70897c55f8acac4e315ba7d132194ef55aa97027a7b195b92150786f7b`
- Pages: 5, US Letter, unencrypted, no JavaScript
- Title: *Tree independence sequences are unimodal through order 31*
- Author: Zijian Zeng

## Machine checks

- The final `pdflatex`/BibTeX build completed in an isolated directory.
- `main.log` and `main.blg` contain no warning, overfull box, underfull box,
  undefined-reference, or error line.
- The citation checker reports 9 cited keys, 9 bibliography keys, 0 missing,
  and 0 unused.
- The formal Kadrawi--Levit record renders as *Ars Mathematica Contemporanea*
  25 (2025), no. 4, P4.03.
- `pdftotext -layout` contains the exact census
  `40,330,829,030`, `non-unimodal = 0`, `non-log-concave = 159`, both
  64-bit fingerprints, and the no-proof-assistant disclosure.

## Page-by-page visual inspection

All five pages were rendered to PNG at 150 dpi and inspected individually.

| Page | Result | Items inspected |
|---:|:---:|---|
| 1 | PASS | title, author, abstract, displayed sequence, citations, date, page number |
| 2 | PASS | definitions, rooted-tree recurrence, integer bounds, corrected Li--Ruskey attribution, theorem opening |
| 3 | PASS | proof continuation, exact census, hashes, corollary, proposition |
| 4 | PASS | certificate table, three principal SHA-256 values, commands, limitations, disclosure |
| 5 | PASS | AI disclosure, nine references including the formal Kadrawi--Levit journal record, affiliation and email |

No clipping, overlapping text, margin overflow, unreadable hash, broken table,
misplaced page number, or visual corruption was found.

Two preceding fresh build attempts were rejected rather than published:
Crossref's literal `#P4.03` caused a TeX fatal error, and its bare `July`
month value caused a BibTeX warning.  The two metadata-preserving
normalizations are documented in `audit/CITATION_AUDIT.md`; the third fresh
build above is the zero-warning artifact inspected here.
