# Rendered-page visual audit — attempt 2

PASS. Every page of the current four-page PDF was rendered by `pdftoppm -r 110 -png manuscript/main.pdf audit/rendered-attempt2/page`. Each of the four resulting PNGs was opened with `view_image` and visually inspected. The image hashes and exact PDF digest are recorded in `audit/visual.json`.

| Page | Actual inspected content | Result |
|---|---|---|
| 1 | Title, author/affiliation, abstract, lattice formula, source conjecture and introductory citations | Legible; no clipped text, collisions or broken symbols. Conjectural status and finite range are clear. |
| 2 | Main conjecture, proved conditional proposition, triple-product proof, constant-term expression | Equations and their numbers fit the margins; citation shows Theorem 2.8. No overlap or missing glyphs. |
| 3 | Finite evidence, selected-library body citation, corrected 18-to-14 reduction, residual eta quotients, grouped observations and limitations | All subscripts, fractions, indices and moduli are readable; scope limitations remain explicit. |
| 4 | Four replay commands, computational/AI disclosure, all six bibliography entries | Commands and bibliography fit within margins; citations resolve. Preprint status is visible. |

No charts, figures or data tables are present. The mathematical displays were compared with the source and accepted scope during citation review. Page breaks between the replay introduction and commands are readable and introduce no omitted content. All pages have visible sequential page numbers; no blank or superseded page was included.

Final typography repair: the strict hook rejected standard pmod and substack commands. Equivalent explicit mod notation and a single-line product index replaced them. The mathematical claims, citations and line intervals did not change. All four pages were rebuilt, rerendered, and viewed again; the final displays remain legible and no warning was found. The final extraction is round 3.
