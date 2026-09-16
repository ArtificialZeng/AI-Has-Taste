# Rendered-page visual audit

Verdict: **accept**. Job: primary-20260914-triangular-square-roots-release-774ca875bd99. Reviewed at 2026-09-14T13:18:27.105865+00:00.

The final PDF was rendered with `pdftoppm -r 125 -png build/main.pdf audit/release-pages/page`. Every one of the six resulting page images was actually opened with the image-viewing tool and visually inspected in this fresh release context. This report does not rely on text extraction or a previous writer's observations.

Page 1: Title and author information fit within the margins. The abstract and full theorem show the correct open root interval and explicitly retain the unresolved Eulerian component. Definitions, initial rows and recurrence are legible; body reference numbers resolve. The final citation continues normally onto page 2.

Page 2: The continued source discussion and bounded novelty limitation are readable. The ordinary recurrence, characteristic formula, divided difference and constants are complete. The plain subsection heading is clear; equation numbers remain separate from all formulas.

Page 3: The strict-modulus lemma, its proof, selected argument branches, endpoint limits and phase formula are all unclipped. Absolute-value bars, conjugation notation, radicals and signs are readable. The first-hitting argument is complete on the page.

Page 4: The real map, ordering inequalities, trigonometric amplitude and index range fit cleanly. The ceiling brackets and sample-order/sign display are readable. The proof conclusion includes degree, simplicity, the join and the empty-path case without overlap.

Page 5: The exact versions, degrees and total of 530 signs are legible and match the frozen report and fresh replay. The homogeneous evaluation and enclosure tests fit. The Zeng citation and Bézout accent render correctly. Limitations and AI disclosure are visible. References 1–2 begin cleanly; their wrapped URLs stay inside the margins.

Page 6: References 3–6 are complete and legible, including the full 27-author SymPy list, the 2019 journal data and the Zeng preprint version/date/DOI. Long URLs wrap without clipping. The remaining white space is ordinary end-of-article space.

No clipped equations, missing symbols, overlaps, unreadable text, broken reference numbers or substantive layout defects were found. There are no figures, charts or data tables requiring separate visual-data comparison. All numbered mathematical displays were read alongside their surrounding statements.

Exact reviewed PDF SHA-256: 4b58859471d0b70afb4a7aa89c3b74b16890f30608fb017b26e3585cc3f33c5e. Manuscript digest: ba5f0bdbee3199a8021a97558ebbd7dd0fa427069cf5e43f11f8d4d5c713600f. Mathematical snapshot: afcfb64162aef0f427a3122f208edb356ac2e15cb197a2f8cd8e56b437beea5b. The individual rendered image hashes are bound in audit/visual.json. No source or PDF change was made after these views.
