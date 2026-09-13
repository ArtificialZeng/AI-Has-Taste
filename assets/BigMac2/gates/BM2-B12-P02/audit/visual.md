# Fresh rendered-page visual audit

Verdict: accept. Job: `bigMac-00012-p02-release-436e003549d5`; date: 2026-09-08.
PDF SHA-256: `6c8a138c1527970c728b130ea1a4258c9ca9480f17c8ee8ad0e981f3f276a4ab`.

I rendered the current rebuilt PDF with Poppler `pdftoppm -r 150 -png` and
actually opened and visually inspected each page image. Reviewed page set is
exactly `[1, 2, 3, 4]`, matching `pdfinfo`. Prior renders/reports were not used as
a substitute for this inspection.

| Page | Image | Actual observations |
|---:|---|---|
| 1 | `audit/rendered/page-1.png` | Two-line title, author/address, date, abstract formulas and opening context fit cleanly. Subscripts, primed sigma, Delta/Phi and boxminus are distinct; no clipping or overlap. |
| 2 | `audit/rendered/page-2.png` | Lemma and proof, underlined simple lifts, roots, signed-word equation and six-column certificate table are legible. Every table word/count agrees with the exact output. Equation numbers and final root-image lines fit the margins. |
| 3 | `audit/rendered/page-3.png` | Theorem, descent lengths, set identities, corollary and universal-depth derivation are clean. Proof squares do not overlap prose. The verification paragraph continues unambiguously on page 4. |
| 4 | `audit/rendered/page-4.png` | Continuation, limited Zeng comparison, scope statement, AI/computation disclosure and all three references are legible. The full Zenodo DOI fits. Remaining whitespace is normal for a short final page. |

All pages retain consistent margins and readable mathematical symbols. No
clipped equations, missing glyphs, unreadable figures, overlaps or obscured
reference labels were found. There are no plots or diagrams; the single
certificate table was checked value by value. All fonts are embedded; metadata
and page count are recorded in the separate build evidence.
