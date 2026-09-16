# Fresh rendered-page visual audit

Verdict: accept. Job: primary-20260913-nfa-asymmetry-release-a0b9dbc9657e. Checked UTC: 2026-09-12T19:48:38.214933+00:00.

The final six-page PDF in manuscript/build/main.pdf was rendered by
`pdftoppm -r 110 -png` into audit/release-pages/. Every rendered page was
actually opened with tools.view_image in this release context, in order
1, 2, 3, 4, 5, 6. This was a fresh visual review of the final rebuilt PDF,
not reliance on the writer's earlier images or on pdftotext alone.

| Page | Inspection |
| --- | --- |
| 1 | Title, author/affiliation, accented Goralčík, abstract, first definitions and original A(q) bounds are legible. Every introduction citation is visible; formulas and foot margin fit. |
| 2 | The restricted maximum display, Theorem 1, corollary, Schwarz attribution, period identity and inclusion chain are complete and clear. The large set brace and subscripts are visible without clipping. |
| 3 | All upper-bound cases, moduli, chain/reversal discussion and identical-relation contradiction are legible. The section transition and witness parameter display fit the page. |
| 4 | Both sharpness lemmas are complete. The replacement labeled arrows have distinct endpoints and readable labels. Return-length formulas, inequalities and proof-ending squares have no collisions. |
| 5 | The exact-diagnostics section, direct Zeng citation, mixed-symbol inclusion and entire Table 1 are visible. Table cells match 2/16/512/65536 and 4/256/262144/not enumerated. Construction counts and witness integer are readable. |
| 6 | Computational/AI disclosure and all seven references are complete. Accented author names, DOI/URL breaks, publication years and preprint version notes are legible; no reference is clipped. |

No clipping, overlap, unreadable symbol, lost text, hidden citation or blank
page was observed. The lone data table was compared cell by cell with the
fresh verifier replay; there are no plotted axes or statistical graphics.
The mathematical path arrows were visually checked after their syntax-only
replacement. The bibliography is a normal visible list with all seven
entries, including six natural non-library sources and the selected library
paper. Author details, mathematical scope and assistance disclosure appear
correctly.

Rendered image hashes and the exact manuscript/PDF bindings are in
`audit/visual.json`. No manuscript or PDF edits occurred after these views.
The original-source images Schwarz pp.161/167 and Nicol p.3 were additionally
viewed for citation verification; they are not counted as manuscript pages.
