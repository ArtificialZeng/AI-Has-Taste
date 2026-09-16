# Rendered-page visual audit

Verdict: accept. Job `newwin-00001-p20-release-3992adf5ac58`, UTC 2026-09-12T12:32:05.700710+00:00. The final six-page PDF was rendered with `pdftoppm -png -scale-to 1700`. I actually opened and inspected each final PNG, pages 1, 2, 3, 4, 5 and 6, using `view_image` after the final rebuild. Text extraction and file existence were not treated as visual review. Earlier page previews were superseded by this final complete inspection.

- Page 1: Title, abstract, model, piecewise definition, coefficients and full theorem all legible; equation labels 1-4 and metadata footnotes clear.
- Page 2: Related literature, symmetry, exact branches, constants, local lemma and Wallis normalization fit; all fraction and floor/symmetry indices legible.
- Page 3: Finite product, CDF constant, local sum orientations and quadrature proof checked; wide displays and the corrected paragraph have no overflow.
- Page 4: Ratio bounds, rational expansion, grid estimate, zero smoothness and constants checked; endpoint signs and stacked fractions clear.
- Page 5: Uniform Taylor conclusion, central identities, all finite count/range assertions, direct library citation and assistance disclosure checked; nothing clipped.
- Page 6: All six references, complete authors, version/status, URLs, affiliation and email are readable; intentional remaining white space is not missing content.

No clipping, overlap, missing symbols or illegibility was observed. The manuscript has no charts, figures or data tables. Font embedding and PDF metadata were also checked. The source ECA pages 11 and 12 were separately viewed to inspect the exact published formula and approximation question; they are input evidence, not manuscript pages.

The exact final page images and their hashes are listed in `audit/visual.json`. Mathematical snapshot `cf7630d6bb75637ad046c973a80a87165a82712e35b2590de9570c5fd83fbf73`; manuscript `7b93959746febc59f27108bef0e6f383afed252661f643a166d5d32589bd16ce`; PDF `4ca5de43598fb74ebcc0a8c28110cf8ac5b7bc1c4cfe184f991656f46160a160`.
