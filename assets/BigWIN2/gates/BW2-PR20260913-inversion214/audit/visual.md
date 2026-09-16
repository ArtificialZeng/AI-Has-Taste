# Rendered-page visual audit

Verdict: accept. Release job `primary-20260913-inversion214-release-94470355a3b8`. Reviewed 2026-09-12T23:40:58.291544+00:00.

The final PDF was rendered with `pdftoppm -r 120 -png manuscript/build/main.pdf audit/release-pages/page`. After the last source change and clean rebuild, this worker actually opened every final PNG with the image-viewing tool in two groups, pages 1-3 and 4-6. The page count is six, and the exact reviewed list is `[1,2,3,4,5,6]`. The preceding build's images were not substituted for final-page inspection. The current PDF SHA256 is `699f3ced30b254d80a8aed66a274fad3b040cd9b981dcce08b8dd0f8d865e2bf`; manuscript digest `d55ad7f160a9be90f7346fc4e63592c327ccf69e82d6d4dcd6747631f854f38e`.

- Page 1: Title, author, affiliation and abstract legible. The exact class definition, corrected pattern list, prior-work citations, and small-root formula fit the page; no clipping or overlaps.
- Page 2: Rational functions, orbit, all-orders theorem, unboxed quotient (8), approximants and contact (10) are clear. Initial coefficients are legible. No formula-number collision or margin spill.
- Page 3: Growth-rule ranges, boundary extraction, denominator-cleared equation (13), kernel calculation and F=c/z fit cleanly. Subscripts, signs and equation labels are readable.
- Page 4: Regularization, summand orders, finite iteration and exact tail display correctly. The denominator D_(m-1), exponent m+6 and finite-error identity are visible without collisions.
- Page 5: Uniqueness proof and Lagrange formula (22) are legible; finite verification ranges 40,48,120,9,45,47 are clear. The library citation, exact coefficient 5/16 and both factorial bases are readable. The paragraph continues normally onto page 6.
- Page 6: The continuation explicitly limits the library comparison. AI assistance disclosure is readable. All six references and their URLs fit; the local-author date and unverified hosted-version disclaimer are visible. No missing glyph, overlap or cropped URL.

No charts, statistical tables or data figures occur in the manuscript; the displayed numerical evidence is the coefficient list and explicit finite ranges, all checked against exact evidence. Font and text-bound checks supplement the visual review in `audit/release-build-check.json`. There are no clipping, overlap, illegibility or missing-character blockers. Page breaks do not obscure hypotheses or references. PDF title/author metadata is blank but the printed title and author are correct; no conflicting metadata was found.

This is a visual/typesetting review of the displayed artifact, not peer review or mathematical certification. Mathematical statements preserve the accepted scope, and the non-algebraicity question remains unresolved.
