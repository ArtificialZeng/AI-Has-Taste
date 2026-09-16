# Rendered-page visual audit

**Verdict:** accept.  The final bound PDF was rasterized at 160 dpi and every
page was inspected from `audit/rendered-page-1.png` through
`audit/rendered-page-4.png`.

| Page | Contents checked | Result |
|---|---|---|
| 1 | Title, author block, abstract, context, equations (1)--(2), theorem | No clipping, overlap, malformed glyphs, or margin overflow; citations and accents are legible. |
| 2 | Low-index formulas, multiplicity lemma and start of trace-ratio lemma | Displays, equation numbers, proof marker, and page break are clear; no overprinting or cutoff. |
| 3 | Trace-ratio proof, trace identity, theorem conclusion | Long rational displays and polynomial are legible; alignment, symbols, and bottom margin are intact. |
| 4 | Assistance disclosure and four-item bibliography | Heading, wrapped references, DOI/arXiv strings, accents, and page number are clear; no orphaned or clipped text. |

All fonts used in the visible manuscript render consistently.  The PDF has
four pages, correct title and author metadata, extractable text, and no figures
or tables requiring a separate data-integrity comparison.
