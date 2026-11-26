# PDF audit

Status: **passed for submission-package handoff** (2026-11-26).

This audit applies to the 13-page manuscript
`paper/main.tex` / `paper/main.pdf`, synchronized bit-for-bit to
`output/pdf/agoh_giuga_star_pack_crt_bound.pdf`.

- **Clean build:** `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
  converged cleanly on TeX Live 2026 (`pdfTeX 1.40.29`).
- **Log & citation audit:** `scripts/audit_latex.py main.tex references.bib --log main.log`
  passed with `cited=9 bib=9 missing=0 unused=0`. Both `main.log` and `main.blg`
  contain **zero** errors, **zero** undefined references/citations, **zero**
  hyperref warnings, and **zero** overfull/underfull `\hbox` warnings.
- **PDF metadata (`pdfinfo`):**
  - Title: `Star-Pack Dominance and Forced-Prime CRT Lower Bounds for the Agoh–Giuga Conjecture`
  - Author: `Anonymous` (pending user confirmation of author metadata before submission)
  - Pages: `13` (US Letter, `612 x 792 pts`), PDF 1.7, no encryption, no JavaScript
  - File size: `642,893 bytes`
  - SHA-256 (`paper/main.pdf` and `output/pdf/agoh_giuga_star_pack_crt_bound.pdf`):
    `fc92119c228e03879baf5d03a43de099f77354661c5484b331175850545f0786`
- **Page-by-page visual inspection:** All 13 pages were rendered at 150 dpi via
  `pdftoppm -png -r 150` into `tmp/pdfs/tier2_visual_audit/page-01.png` through
  `page-13.png` and visually inspected in full. An initial visual pass caught
  and resolved: (i) hidden DOI/arXiv IDs under `plain.bst` for `@misc` entries
  [7] and [9] (fixed via explicit `howpublished`), (ii) awkward hyphenation in
  Section 2 heading (`Theo-rem`), (iii) non-bold numeral `16` in Section 3
  heading, and (iv) Table 3 floating above Section 6. After rebuild, all 13
  pages exhibit zero clipping, zero overlap, zero missing glyphs, crisp
  tables/equations, visible identifiers for all 9 references, and balanced
  final-page layout.
- **Text extraction (`pdftotext -layout`):** Cleanly recovers title, abstract,
  all headline bounds (`8,138`, `326,057`, `40,922`, `352,757`, `1,808,611`),
  both binary SHA-256 digests (`826dad79...`, `54e7192a...`), and all recent
  preprint identifiers (`10.5281/zenodo.22085830`, `arXiv:2610.09129v2`).
- **Independent certificate reproduction:** `src/verify_agoh_giuga_certificate.py`
  independently verified all 4 parts and 846 `(U, R)` witnesses in ~15.6 seconds
  with zero floating-point arithmetic (AST-audited).

This audit certifies technical, visual, and computational integrity; it does not
promise journal acceptance or imply peer review has occurred.
