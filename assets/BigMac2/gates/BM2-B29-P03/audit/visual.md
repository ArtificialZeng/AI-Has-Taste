# Fresh rendered-page visual audit

## Bound artifact and method

- Release job: `bigMac-00029-p03-release-c1fda9dfb459`.
- Evidence snapshot: `742b93162211e835fe67ffd8e2ed442a562f83e734d6b3030d5534c3dd21d7f5`.
- Manuscript snapshot: `e5e03004830aff9dab501eb34a552ddcc086782f9fb316694afae43b5ddcf856`.
- PDF: `09e3f5ce396a5ad4c2127b40e9d26512f5c0fb27fb87c6a3da73d2e9732a2819`.

`pdfinfo` reports exactly five A4 pages.  I rendered every page at 150 dpi with
Poppler to `audit/rendered-pages/page-1.png` through `page-5.png` and inspected
each raster at original detail.  This audit is based on the rendered pages,
not on text extraction alone.

## Page-by-page observations

| Page | Material reviewed | Observation |
|---|---|---|
| 1 | Title, author block, abstract, context formula, theorem and graph6 string | Balanced margins and spacing; title and author metadata are legible; formula, graph6 data, and theorem are fully visible; no clipping or collision. |
| 2 | Citation qualification, definitions, cut-decomposition lemma and proof, orientation-product lemma and proof | All prose and displayed equations are sharp; proof-end symbols and citation links are visible; no overlap or orphaned line. |
| 3 | Census method, command line, Table 1, independent counter description, start of merged census | Table rules, column headings, values, symbols, and monospaced command are legible; no material crosses margins. |
| 4 | Table 2, stream digest, independent census discussion, equality proof and exact inequalities | Table and long SHA-256 line fit cleanly; graph6 string, powers, products, and proof-end symbol are legible; no clipping. |
| 5 | Reproducibility commands, assistance disclosure, and all three bibliography entries | Commands and disclosure are readable; URLs and DOI lines wrap within margins; all references are complete and citation links are legible. |

The manuscript contains no figures or charts requiring a data-integrity review.
All tables use unambiguous labels and consistent alignment.  There are no blank,
rotated, duplicated, or image-only pages, and no unreadable color contrast,
overlap, truncation, or malformed glyphs.

## Verdict

**Accept.**  Pages 1--5 were individually reviewed and are submission-ready.
