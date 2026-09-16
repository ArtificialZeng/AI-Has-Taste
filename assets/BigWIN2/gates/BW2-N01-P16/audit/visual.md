# Rendered-page visual audit

Verdict: accept. Job `newwin-00001-p16-release-699cf5c87937`, 2026-09-12 UTC.
The final PDF was rendered with `pdftoppm -r 115 -png` into
`audit/release-pages/page-1.png` through `page-5.png`. Every one of these five
images was actually opened with the image-viewing tool in this release context.
The image hashes and current PDF bindings are recorded in `audit/visual.json`.

| Page | Observed content and result |
|---|---|
| 1 | Complete title, author and affiliation/email footnote; abstract, definitions, contextual citations and exact five-prime Theorem 1. Superscripts, radical notation and the strict bound are legible. No clipping or overlaps. |
| 2 | Continuation of context, quotient identity, exponent-one boundary case, product-loss inequality, gap reduction and beginning of Lemma 2. Equation numbers and math symbols are clear; the lower equation has adequate footer separation. |
| 3 | Prefix proof, four-row cutoff table, factorization and recovery formulas, all six composite witnesses and completion of Theorem 1. Table columns and inequalities align; no truncated cells or equations. |
| 4 | All thirteen factor rows and six ordered pairs, followed by the verification paragraph with the visible selected citation [5], direct cross-check, scope limits and AI/computation disclosure. The factor table and wrapped first pair row are clear. |
| 5 | Entire thirteen-row divisor appendix, including wrapped long rows, and all five references. DOI and publisher URLs wrap within margins; the preprint status/version is visible. No missing rows, overlapping text or unresolved citation markers. |

There are no figures, charts, plotted axes or photographs. Every numerical table
entry was additionally compared against the exact accepted certificate and
recomputed by the fresh release script. Body text, mathematical symbols, table
headings and bibliography are readable at normal page scale. No visual defect
requiring a source edit was found. The PDF is the same one accepted in the build
and citation records; no later build is included in this verdict.
