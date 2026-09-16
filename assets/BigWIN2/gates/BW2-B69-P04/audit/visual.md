# Rendered-page visual audit

Accept. For release job `win-00069-p04-release-5a943a0eb78e`, I rendered `manuscript/main.pdf` (SHA-256 `059ace62baa7323c8f3ec4871f82bec7aab178f82916ea5631da6c2127e63f65`) at 144 dpi with `pdftoppm` and actually inspected pages 1, 2, 3, 4, and 5 individually against the authored source and extracted text.

| Page | Content inspected | Result |
|---|---|---|
| 1 | Title/author/date, abstract, statement, citations, Theorem 1 | Clear; no clipping, overlap, missing glyph, or margin loss |
| 2 | Lorentz equations (1)–(4), matrices, start of the two-census reduction | Clear; equations and subscripts legible; no overflow |
| 3 | Rooted-expansion lemma, proof, Table 1, local-block lemma | Clear; all seven table columns and counts legible; no collision |
| 4 | Interface lemma, exact signs, enumeration argument, geometric filters | Clear; display math, proof marks, and final lines intact |
| 5 | Reproducibility commands, limitations, AI disclosure, all three references | Clear; monospaced commands and bibliography legible; no clipping |

The document has consistent page numbers, margins, typefaces, headings, mathematical symbols, and reference numbering. Table 1 has no truncated cells or misleading visual encoding. There are no figures, charts, color legends, or external raster assets requiring value-by-value visual verification. The visible scope remains the accepted bounded result through 84 chambers and explicitly leaves Conjecture 7.11 unresolved.
