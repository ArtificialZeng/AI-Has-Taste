# Rendered-page visual audit

**Accept.** Job `primary-20260913-level-rook-fibres-release-8051a1494029`,
2026-09-12 UTC. This worker actually viewed every final rendered page using
the image-viewing tool, after the final rebuild and manuscript freeze.
The PDF and source digests are bound in `audit/visual.json`.

Rendered with `pdftoppm -scale-to 1800 -png manuscript/build/main.pdf
audit/release-render/page`. Reviewed pages **1, 2, 3, 4, 5, 6, 7**:

| Page | Material inspected | Finding |
|---|---|---|
| 1 | Title, author/affiliation/email, abstract, level totals/transpose, problem-origin references and count definition | Clear type, correct symbols, intact display equations and margins; arbitrary-m limitation visible. |
| 2 | Theorem 1, floor/ceiling capacities, input length and all literature comparisons including the late source and selected library citation | Math and citations readable; no clipped text, overlaps or unsupported visual emphasis. |
| 3 | Row-pair bijection, three-preimage example, realization of capacities and recurrence (4)--(6) | Fractions, floor/ceiling glyphs, subscripts and equation numbers clear. |
| 4 | Shifted binomial representation, prefix coefficients, reflected/saturated intervals and finite differences | Long formulas and endpoints fit; short-interval qualification remains legible. |
| 5 | Integer/operation/storage bounds, Table 1 and beginning of the dilation-oracle argument | All four table rows legible; every count/range agrees with the fresh exact verifier. Continuation onto page 6 is ordinary paragraph flow. |
| 6 | Remainder of the oracle, reproducibility commands, limitations, AI disclosure and references 1--6 | No missing citation markers; lines, DOI/URL breaks, bibliography accents and disclosure readable. |
| 7 | References 7--12, including the two distinct Jiang papers, PMLR record and selected preprint | Complete entries, readable links, correct authors and visible preprint labels; no clipping. |

There are no charts, axes, photos or data diagrams. The sole table reports exact
finite verification coverage: 5,461 capacity vectors; 7,338 shapes / 1,866 fibres;
400 seeded vectors, lengths 1--25, capacities 0--40, 74,587 values; 16 dilations,
lengths 2--14 and 18, scales 10^75+31 through 10^75+46. These were compared
value-by-value with the regenerated JSON and verifier's loops. No rounded values
or numerical interpretation is substituted. Footers and all seven page numbers
are visible; all text fits the page and no mathematical symbol is missing.

The images were inspected directly; text extraction and build success were used
as additional checks, not as substitutes for visual review.
