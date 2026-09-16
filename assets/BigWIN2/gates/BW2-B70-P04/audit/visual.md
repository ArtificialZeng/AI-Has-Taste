# Rendered-page visual audit

The final `manuscript/main.pdf` was rendered to PNG at 120 dpi with
`pdftoppm`, and pages 1 through 7 were each opened and visually inspected at
original rendered resolution after the final clean build.

| Page | Content checked | Result |
|---:|---|---|
| 1 | Title, author/affiliation footnote, abstract, theorem statement, opening context | Clear; no clipping or overlap |
| 2 | Phase-lock definitions, four imported inequalities, start of phase-cover proof | Clear equations and labels |
| 3 | Both interval tables, endpoint formula, joint-pruning formulas | Tables and long decimals legible and within margins |
| 4 | End of phase proof, analytic bounds, displayed tail estimates | Clear; proof-end markers render correctly |
| 5 | Box criterion, closed-box proof, leaf-count table, disk-section opening | Table and union formula clear; no collision |
| 6 | Rouché certificate, theorem completion, reproducibility commands, all body citations | Clear; monospaced commands and citation numbers legible |
| 7 | Complete three-entry bibliography and DOI/arXiv identifiers | Clear; wrapped DOI lines remain inside margins |

No figure is present.  No cropped text, overlapping element, broken glyph,
illegible symbol, malformed table, blank unintended page, or visual distortion
was found.  Page numbers and theorem/proof structure are consistent throughout.
Verdict: **accept**.
