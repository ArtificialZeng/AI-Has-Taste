# Rendered-page visual audit

Audit date: 2026-09-06.  The final PDF bound by SHA-256
`5c1cf9462118f322a5185094dc5af15f56f4b256dc8e321a7d2da82caf41c993`
was rendered with `pdftoppm -png -r 150`.  I visually inspected every rendered
page at original image resolution.

| Page | Content checked | Result |
|---|---|---|
| 1 | title/author block, abstract, theorem statement, displayed equations | clean; no clipping, collision, overflow, missing glyph, or illegible text |
| 2 | coefficient table, related-work paragraph, recurrence and proof | clean; table rules/columns and mathematical symbols are legible |
| 3 | Pieri paragraph, `P_3` regression, graph enumeration, certificate proof | clean; page break and display spacing are sound |
| 4 | replay command, assistance disclosure, all seven references | clean; monospaced command and bibliography wrap within margins |

The document contains one table and no figures/charts.  The table values are
legible and agree with the exact values audited in `audit/citations.md` and
`audit/math.md`.  Page numbers, headings, citations, equations, and proof-end
symbols render correctly.  No visual distortion, overlap, clipping, orphaned
heading, or unreadable font was found.

Verdict: accept; pages seen: 1, 2, 3, 4.
