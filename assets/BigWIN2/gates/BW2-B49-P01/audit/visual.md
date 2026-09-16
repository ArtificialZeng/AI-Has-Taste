# Rendered-page visual audit

Verdict: **accept**.

All four pages of the current `manuscript/main.pdf` were rendered at 144 dpi and inspected at original raster resolution. The final metadata-only rebuild produced page rasters byte-for-byte identical to the inspected images.

| Page | Render | SHA-256 | Findings |
|---|---|---|---|
| 1 | `audit/rendered/page-1.png` | `b20390922d69c9396dc3ef6456ca018cf025657441d03eb1ede4ec9269b9cf40` | Title, author block, abstract, definitions, citations, displayed edge list, and margins are clear; no clipping or overlap. |
| 2 | `audit/rendered/page-2.png` | `e87d6a7bcb93a2adb9d4ff8defecf019c19e86384dafa3e9222fa634abd7e4be` | The theorem, all eight table rows and invariants, lemma, equations, binomial count, and footline are legible; no overflow or missing glyph. |
| 3 | `audit/rendered/page-3.png` | `3ba2bdb0004b9a9e14bbb7c3953932e3b7d4de07a8d71e18acc17092ec34c90c` | Permutation displays, proof text, witnesses, citations, and section transition are legible and within margins. |
| 4 | `audit/rendered/page-4.png` | `e7ac6260a7139bd03377299e35fa3a9fac457182d0e5b4e0f14fc51f2765cdb0` | Limitations, disclosure, and all five bibliography entries are complete and legible; no widow-related loss, clipping, or overlap. |

There are no figures or quantitative charts to cross-check. The sole table has a conventional linear scale-free layout and all values agree with the accepted theorem. Mathematical symbols, equation numbers, cross-references, citations, fonts, and page numbers render consistently. PDF title and author metadata were also inspected with `pdfinfo`.
