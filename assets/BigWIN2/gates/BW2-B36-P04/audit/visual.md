# Rendered-page visual audit

Job: `win-00036-p04-release-23764c16e129`

The final PDF with SHA-256
`3e171d8f22032e1e035fbc42bc6b9705a29f6f99b1acd69f970e990ab36000b9`
was rendered at 150 dpi with `pdftoppm`. Every page was inspected at original
render resolution as an image, not merely through extracted text.

| Page | Content inspected | Result |
|---|---|---|
| 1 | Title, author, abstract, theorem, four-source context, criterion and proof | No clipping, overlap, broken glyph, or illegible text; links and references are correctly positioned. |
| 2 | Trial-division data, both certificate tables, start of modular chain | Tables fit the margins; exponents, gcd expressions, and residues are legible and aligned. |
| 3 | Full residue table, divisibility/properness conclusion, disclosure, start of bibliography | No clipping or overlap; mathematical symbols and body-flow citation are legible. |
| 4 | Completion of the four-entry bibliography | Every entry is complete and legible; margins and page number are intact. |

There are no figures, charts, or diagrams requiring value-by-value source
comparison. Page order is correct, fonts are embedded, and no authored text
strengthens the accepted theorem. Verdict: **accept**.
