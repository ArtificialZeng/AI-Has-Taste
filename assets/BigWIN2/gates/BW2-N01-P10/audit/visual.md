# Fresh rendered-page visual audit

Verdict: accept. Job newwin-00001-p10-release-44a34dd73dbb. Checked 2026-09-12T11:16:42.970901+00:00.

Every page of the final `manuscript/build/main.pdf` was rendered using
`pdftoppm -r 110 -png` and actually opened with view_image in this release
context, in order 1,2,3,4,5. This is image inspection, not an inference from
pdftotext or file existence. The final metadata rebuild was rendered again;
all five image hashes matched the already inspected content, and each final
image was opened and inspected once more.

Page 1: title/author, scoped abstract, complete multiplicity definition, problem display, coefficient and moment criterion are readable. Date, keywords and MSC footer remain inside the page; no collision with the page number.

Page 2: sufficient classes and fixed-sum corollary retain hypotheses; five literature paragraphs and the actual library citation are visible. Tableau contents and formulas (4)--(6) are legible; the proof starts at the bottom with its series fully visible.

Page 3: generating-function, triangular identity and Newton recurrence align correctly. Chern-shadow attribution and mod-8/3/5 arithmetic are readable; no equation overlaps margins or numbering.

Page 4: both boundary lemmas, dotted multiplicity-union notation, product A^20, scalar identity, quartic and the Li citation are visible. Proof endings and corollary proof do not overlap.

Page 5: negative controls, all finite counts, the 26th-order stopping value, limitations and assistance disclosure are readable. All six bibliography entries, DOI/preprint strings, affiliation and email fit without clipping.

No clipping, overlap, unreadable symbol, missing citation marker, detached
heading, broken mathematical display or illegible bibliography was found.
There are no data charts, external figures or numerical tables in this paper.
Displayed numerical examples and computation counts were checked against the
exact records as recorded in the citation and numerical audits. The two
negative controls explicitly have unequal sums; no visual caption presents
them as counterexamples to the fixed-sum question.

The page images are audit/release-page-1.png through audit/release-page-5.png;
individual hashes are in audit/visual.json. The title and author in PDF metadata
match the rendered title/author. The original problem remains explicitly
unresolved in the abstract and closing discussion.

Bound manuscript digest: a225a1f70e851c5d99ff55f694b4658da7f6817b346074c78a3ecc7838247f18.
Bound PDF SHA256: 79032ecd15478bde0f68a76fb829b29db438c3f0a46e008ef4cae98dfc59de29.
