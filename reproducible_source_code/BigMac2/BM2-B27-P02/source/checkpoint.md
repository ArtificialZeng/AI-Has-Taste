# Checkpoint

- Release provenance: `bigMac-00027-p02-release-d905b1628ce1`.
- Candidate: **resolution-paper**; original status: **proved**.
- Accepted frozen claim: `t_3(8,8)=22`, with evidence snapshot
  `0ecbd967a46f945bd6835b7187032eedfcef4d2f0e168b18c9337c6ecc300ddd`.
- Immutable `source.md` remains byte-identical with SHA-256
  `610cc9c263bff685d832a637955902eeac836f99bcce568b8fcc33ef3cf716e2`.

## Release evidence

The dependency-free checker was rerun with the mandated interpreter and
returned `verified=true`, final infected size 64, layer sizes
`[22,14,4,3,2,2,2,2,2,2,2,2,2,2,1]`, and a connected 42-vertex complement
with 41 induced edges.

The publication-only citation repair added publisher-verified DOIs for the
Benevides et al. and Flocchini et al. records, made the source comparison to
Bushaw--Clifton Question 4.3 exact, and embedded title/author PDF metadata.
A clean `latexmk` build produced the current three-page
`manuscript/main.pdf`. The final compiler log has SHA-256
`d743dfe51579c94f31ea5754ac0302998138178806031ec5aa758525fd5f7d26`
and contains no build, reference, citation, or layout warning.

Fresh reports and provenance-bound JSON records are
`audit/citations.{md,json}`, `audit/build.{md,json}`, and
`audit/visual.{md,json}`. All three citations and nearby claims were checked;
all authored/supplementary dependencies were covered; every page `[1,2,3]`
was rendered at 180 dpi and visually inspected. Current manuscript digest is
`dc1b753854a1dbcfc26cbe1a8276cdacc299b48dbd367fec0babd75df0fe61e3`;
current PDF digest is
`97e311fe3a312ace39568a515041bbdeba0d754cefa64d3f96270c5724c53880`.

The final `release_gate.py check` returned `ok=true`, kind
`resolution-paper`, status `proved`, and page count 3.

## Obstacle disclosed

`literature/user_bibliography_check.md` was absent, so no workbook-derived
record was claimed or inspected. This did not leave an unverified citation:
the three cited records were independently confirmed from the primary arXiv
PDF/record and publisher pages. No priority claim is made.

## One next test

The supervisor should run `release_gate.py publish` and verify that the new
`release/manifest.json` binds `release/main.pdf` to PDF digest
`97e311fe3a312ace39568a515041bbdeba0d754cefa64d3f96270c5724c53880`.
