# Checkpoint — fresh release audits complete

## Current accepted artifact

The frozen `resolution-paper` claim remains accepted at evidence snapshot
`9192d4d22df71aa3cafa514ea148858d23e56a971b396d396d0208e56f29727c`.
The manuscript source remains digest-bound at
`4fb76f0bcdaaddcdea9d0aca3ed92339020ecd00ff4ad27fc641fb5d4fa66de2`.
A from-scratch two-pass LaTeX build produced the current five-page PDF at
SHA-256 `19888698d7f2d0de11384534df76a0dec749a4340a3f9c1231e6478013fb08c4`.

## Fresh release evidence

- `audit/citations.md` applies the advisory `citation-check-skill` in two
  passes, verifies the Olteanu--Olteanu attribution from the primary arXiv v1
  record, and checks the workbook-selected Zeng paper only against the narrow
  methodological sentence. The latter uses
  `metadata_basis=user_designated_workbook`; direct DOI/full-text external
  refresh was unavailable, which does not leave unsupported prose or block the
  artifact.
- `audit/build.md` records a clean build from `latexmk -C`, followed by the
  declared two-pass build command. The current `manuscript/main.log` has digest
  `4db038ae6223d81bde5534bda71c0d35dc9a296c945bb17bebaa1f4c65b9f166`
  and no warning, error, undefined reference/citation, rerun, or box diagnostic.
- `audit/visual.md` records actual inspection of rendered pages 1--5 exactly
  once each. All text, formulas, metadata, fonts, links, and references are
  legible, complete, and unclipped.
- The fresh JSON records bind the current evidence, manuscript, PDF, and build
  log digests with release job ID
  `bigMac-00016-p02-release-c1f57e4287a2`.

`source.md` remains unchanged at SHA-256
`3359f80c72e10e411b339956c0e9bffb5fb0dd12ead27f9abc277b088c588622`.
No mathematical, citation, build, dependency, or visual obstacle remains.

## One next test

The fresh `release_gate.py check` succeeded with all current digest bindings.
The next test is the supervisor's separate `release_gate.py publish` action,
followed by verification that `release/manifest.json` binds this exact PDF.
