# Rendered-page visual audit

**Verdict: accept.** The final `manuscript/main.pdf` was rendered with
Poppler at 120 dpi and pages 1 through 7 were inspected individually at
original rendered resolution.

| Page | Content checked | Result |
|---|---|---|
| 1 | title, author block, abstract, opening citations | clear; no clipping or overlap |
| 2 | theorem statement, displayed fractions, framework opening | clear; equations and prose within margins |
| 3 | event volumes, charge equations, local-lemma criterion | clear; symbols, tags, and citations legible |
| 4 | shell proof, large exact counts, displayed exclusion set | clear; no overflow or cramped line |
| 5 | certified-bound table, tail equations, proof | clear; table rules and long decimals fully visible |
| 6 | proof conclusion, reproducibility, assistance disclosure | clear; headings and paragraph breaks sound |
| 7 | all six bibliography entries | clear; complete entries, accents, URLs/DOIs via links, and no orphaned fragment |

The metadata-only source repair did not change page geometry or pixels: every
final rendered page has the same SHA-256 as the corresponding page already
inspected before that repair. There are no figures. The sole table is aligned,
legible, and not clipped. Page numbering is complete, mathematics is rendered
without missing glyphs, margins are consistent, and no overlap, cutoff,
illegibility, unexpected blank page, or visual distortion was found.
