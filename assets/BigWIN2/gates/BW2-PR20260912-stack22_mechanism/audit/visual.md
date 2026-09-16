# Fresh rendered-page audit

Verdict: **accept**. Job:
`primary-20260912-stack22-mechanism-release-bd956129f546`.
UTC date: 2026-09-12.

The final seven-page PDF `manuscript/build/main.pdf` was rendered with
`pdftoppm -png -scale-to 1500 manuscript/build/main.pdf audit/release-preview/page`.
Every resulting image was actually opened with the image-viewing tool in this
release context: pages 1, 2, 3, 4, 5, 6 and 7. Text extraction alone was not
treated as visual inspection. The image hashes and final PDF binding are
recorded in `audit/visual.json`.

| Physical page | Actually inspected content and result |
|---|---|
| 1 | Two-line title, author, affiliation, email, date, abstract and model. Abstract cubic and auxiliary equations are readable; introductory citations are visible. No clipped line or title overlap. |
| 2 | Main theorem, four bit transitions, equations (1)–(3), known-result attribution and exchange lemmas. Symbols, ranks, suffixes, proof-end marks and references are clear. |
| 3 | Canonical-input reconstruction, peak criterion and comparison-forest lemma. Proof continuation into page 4 is intact and ordinary line breaks preserve text. |
| 4 | Forest-to-bit proof, protected boundary argument, E/D and A/B/C/L grammar. The empty-interior exception, endpoint arrows and equations (4)–(9) are legible and within margins. |
| 5 | Complete four-row endpoint table and uniqueness proof; auxiliary-state limitation and symbolic transfer. The table agrees rowwise with the accepted case split. Method citations and equations (10)–(12) are visible. |
| 6 | Formal inverses, residual identity and branch uniqueness; the direct library citation, finite-verification ranges and coefficient table. All ten n/u_n pairs match exact evidence. Table is unclipped; comparison text distinguishes the n=9 check from unrestricted search through n=8. |
| 7 | Verification continuation and limitations, model-assistance disclosure and all six references. Titles, versions, DOI links, preprint status and author names are readable. No long-URL stretching, clipping, hidden references or overlap. |

There are no plots, axes or external figures. The only tables are the grammar
case split and ten coefficient pairs; both were checked against the accepted
proof/exact evidence. All pages have legible normal fonts, margins and page
numbers. Standard proof continuations across page boundaries are acceptable.
The correct title and author metadata were checked with `pdfinfo`; all fonts
are embedded. No rendering repair remains.

Separately, the source-access handoff's Atkinson PDF was rendered and physical
pages 1, 7 and 8 were actually viewed for source verification. These are source
images under `audit/source-preview`, not manuscript pages and not additional
released deliverables. The manuscript visual acceptance applies only to the
final snapshot named in `audit/visual.json`.
