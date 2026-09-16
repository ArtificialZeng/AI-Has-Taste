# Fresh rendered-page visual audit

Verdict: accept. Job `primary-20260914-comb-inverse-release-63c10542e86d`; generated 2026-09-13T21:13:24.450260+00:00.

The final PDF was rendered with `pdftoppm -r 120 -png manuscript/build/main.pdf audit/release-page`. I actually opened and inspected each of the five separate PNG pages using the image viewer after the final clean build. Text extraction alone was not used as visual review.

- Page 1, `audit/release-page-1.png`: Title, author footnote, abstract, lower-ideal/support definitions, and both defining series are readable and within margins. The unbold vector letter remains unambiguous from its coordinate definition.
- Page 2, `audit/release-page-2.png`: Main theorem and rational inverse are legible; all four prior-work citations resolve. Prefix inequalities, local weights and indicator subscripts are clear. The concluding proof text and QED symbol fit above the footer.
- Page 3, `audit/release-page-3.png`: Forest bijection, stack invariant and canonical first-leaf normalization are readable. Equation (12) at the bottom remains fully inside the page and its number does not collide with the footer.
- Page 4, `audit/release-page-4.png`: Formal double sums, geometric-series calculation, inverse proof, cubic, initial polynomials and specializations are readable, with no clipping or overlap.
- Page 5, `audit/release-page-5.png`: The two-column coverage table has a clear bold header; all five rows and ranges match the verified values. The body library citation, code instructions and AI disclosure are legible. All five bibliography entries and line-broken URLs fit on the page.

No clipped equation, overlap, missing glyph, unreadable reference or missing table value was observed. There are no graphical data plots or external illustrations. Mathematical symbols, footnote, page numbers and references were checked. The table values were compared row by row with audit/release-finite-checks.json and manuscript/comb_checks.json.

Reviewed pages: [1, 2, 3, 4, 5]. PDF digest: 7804aae2fb6f4f09261ece569ad0b9487ff4b7e349367a9cbcecae67856667ff. Manuscript digest: 863b4513670a4d8e25144e3f958007d18a47406d9eabbd1dfa952134d7d93f35. Mathematical snapshot: fac6a5d3e0cc11fe8e7a02ae312a3c4409afeaca9b3251dfc764c6d793a56ea2.
