# Fresh rendered-page visual audit

I rendered `manuscript/article.pdf` at 160 dpi with Poppler and visually
inspected every page image at its original rendered resolution.  `pdfinfo`
reports exactly five letter-size, unrotated pages.  This audit is bound to PDF
digest `a4d13aa84c9372f466abb5f6b0d4a4127e11b4f3499b010b68708784c29f59d9`.

| Page | Actual observation |
|---|---|
| 1 | Title, author block, abstract, kernel, context, citations and Eqs. (1)--(2) are sharp and fully inside the margins.  No collision, truncation or orphaned heading is visible. |
| 2 | Theorem 1, Eqs. (3)--(10), Fourier notation and theorem/lemma typography are legible; equation numbers align and no display crosses a margin. |
| 3 | The tail-subtraction proof, integral bounds, piecewise definition and Eqs. (11)--(17) render cleanly.  Long prose and displays wrap without overlap; the proof-end box is unobstructed. |
| 4 | The resolvent section and Eqs. (18)--(24) fit comfortably.  Fractions, primes, inequalities, boundary conditions and the second proof-end box remain distinct and readable. |
| 5 | Endpoint consequence, assistance disclosure and all three bibliography entries are legible.  The long DOI wraps across lines without clipping or colliding with another entry. |

Across pages 1--5, body text, mathematical symbols and page numbers have
consistent fonts and contrast.  There are no figures or charts to inspect, no
blank or duplicated page, no clipped text, overlap, illegible glyph, broken
reference marker, excessive margin spill, or substantive presentation defect.

**Verdict: accept.**
