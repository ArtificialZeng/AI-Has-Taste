# PDF audit

Audit date: **2026-08-29**.  Final source: `paper/main.pdf`; release copy:
`output/pdf/erdos699_i3_100m_certified.pdf`.

- Clean build: `latexmk -C -cd paper/main.tex`, followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -cd paper/main.tex`.
- Final `paper/main.log`: no LaTeX/package warnings, undefined references,
  overfull/underfull boxes, emergency stops, or fatal errors.
- `pdfinfo`: 5 pages, letter size, PDF 1.7, 361,808 bytes, unencrypted, no
  forms, JavaScript, or suspect objects.
- SHA-256: `ecd6979b9994c47562678637b9a545c9ff2330ef2515f9b1e4e275848916e37b`.

The latest PDF was rendered at 170 dpi with Poppler and every page was
inspected:

| Page | Visual check |
|---|---|
| 1 | Title, abstract, problem statement, citations, theorem opening, and date are readable; no clipping or overlap. |
| 2 | Theorem continuation, support lemma, Lucas lemma, and displayed formulas are complete and aligned. |
| 3 | Decision proposition, algorithm, Legendre formula, direct oracle, and release-binder scope are readable; no orphaned or obscured content. |
| 4 | SHA-256 table, tamper summary, theorem proof, and structural reductions fit within margins; hashes break only at intentional two-line splits. |
| 5 | Limitations, reproduction commands, disclosure, all four references, affiliation, and email are readable; no overflow or collision. |

The historical `Underfull \\hbox (badness 6741)` occurred in an earlier build
of the fourth GitHub bibliography item (old `.bbl` lines 25--27), not in the
title or abstract.  The entry was compacted before this release.  The current
converged `paper/main.log` and `paper/main.blg` contain no `Underfull`,
`Overfull`, undefined-reference, citation, package, or LaTeX warning.

Verdict: **pass**.  Author/affiliation/email metadata were inherited from the
project's existing manuscript scaffold and should be reconfirmed by the user
before an external submission; this does not affect the mathematical or
layout audit.
