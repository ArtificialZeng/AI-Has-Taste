# Checkpoint

## Current conclusion

The frozen original claim is disproved for the exact labelled 812-vertex
`AGL(1,29)` base. Fresh mathematical review accepted the full fixed-instance
scope in `audit/math.json`. The proof remains the exact positive-integer
weighted-cycle certificate: demand `16,216,704`, per-vertex upper bound
`15,153,552`, and strict gap `1,063,152`. It does not exclude another base or
resolve the broader `H15` route.

## Release evidence

The clean rebuild of `manuscript/main.tex` and
`manuscript/references.bib` produced the four-page
`manuscript/main.pdf`. The refreshed frozen bindings are:

- evidence snapshot: `3ac774183b824d2e691a0481a81677a129319bd9f0b0cb27bbdc6712048d40c5`;
- manuscript snapshot: `08921f24c115758764be51d319f69d959ec432364ad1c635f60c3484fbf0a4d2`;
- PDF: `8697653017d6d5ee5713540a58a36e406db16550f7d68e083527a7eda3256d1a`;
- build log: `c1c456acdd1fb42b7d0028b52d206e574ab4c44459a27475c97fa3f6d5478ba0`.

`audit/citations.json`, `audit/build.json`, and `audit/visual.json` are fresh
release-job audits. All citation keys and rendered references resolve. The
Garcia record and narrow claim use were checked against the arXiv record and
the frozen primary-source screen. Direct Zenodo metadata refresh was
unavailable but the arXiv record identifies the data DOI. The Zeng metadata
is preserved from the authoritative user-designated workbook
(`metadata_basis=user_designated_workbook`; external refresh unavailable), and
the manuscript limits it to the workbook-supported methodological comparison.
The final compiler/Biber logs are clean, `pdftotext` is nonempty, PDF metadata
is correct, and rendered pages 1--4 were individually inspected without
clipping, overlap, illegibility, or broken references. `source.md` remains
unchanged at SHA-256
`29441258d1fb9526154bab4ea6f8c973728e4ab25b86dc18932baa2b03e5e596`.

## Obstacles and limits

No mathematical, build, citation-support, or visual obstacle remains. The
literature search is bounded and makes no priority claim. Unavailable optional
metadata refreshes are disclosed and do not affect the theorem or clean local
PDF.

## One next test

The release gate now passes on this exact state. The supervisor's next test is
`release_gate.py publish`, followed by digest comparison of the activated
`release/main.pdf` against PDF digest `8697653017d6d5ee5713540a58a36e406db16550f7d68e083527a7eda3256d1a`.
