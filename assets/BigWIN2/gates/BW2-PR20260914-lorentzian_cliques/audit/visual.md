# Rendered-page visual audit

Verdict: **accept**. Job: primary-20260914-lorentzian-cliques-release-1bb091df0970. Generated: 2026-09-13T23:58:16.133131+00:00.

The final PDF was rendered with `pdftoppm -r 130 -png manuscript/main.pdf audit/recovery-page`. Every image was actually returned through view_image and inspected in this context, in order 1, 2, 3, 4, 5, 6. These are freshly rendered images of the final rebuilt PDF; historical images and reports were only evidence indices. The previous release's six image returns are not alleged to have failed.

- Page 1: Title, author footnote, abstract, the assignment sum and Hessian criterion are legible; all indices and citations [1,3,4] render correctly. No clipping or overlap.

- Page 2: Bistability attribution, target, theorem hypotheses, separator formula, factorial-scaled Hessian and both spectral cases are readable. Citations [2,5,6,7] and the full selected library sentence are visible in ordinary body flow.

- Page 3: Expansion and deletion proofs are intact, with correctly rendered inequalities and the singleton-component and k=2 discussion. The final proof paragraph fits within the page.

- Page 4: All coefficient factorials, the 2x2 inertia block and characteristic polynomial are legible. Cycle and complete-bipartite boundary formulas and the scope-limitation paragraph are intact.

- Page 5: Every one of the 15 numerical table cells agrees with the exact evidence. The 6820 total, 22/15 record caveat, cube value 32 and assistance disclosure are readable. Bibliography entries [1]-[4] fit without clipping.

- Page 6: Bibliography entries [5]-[7] show the correct author names, article 42, 2024/2025 version distinction, and DOI/arXiv identifiers. Whitespace is harmless; no clipping, overlaps or missing glyphs.

The sole table was checked cell by cell against both actual saved exact outputs. There are no charts, diagrams or photographic figures requiring source-data comparisons. Equations, theorem symbols, page numbers, author information and all seven references are legible. This is visual inspection of the manuscript, not a claim of visual access to Stanley's remote source scan.

Evidence digest: 433d775ecce23495c57cb0b57f8bf311721ff57d30a9c8a2b19e2d8bf4270d2d.
Manuscript digest: 5520840a8b7f7353be231676b0d5f9e3faeee90c4ea30ea71662c211cbda9974.
PDF digest: bd3460c9c0fda440e051949450b2933709fa2bf8d6d15fa80178d98be4490f65.
Image hashes are recorded in audit/visual.json.
