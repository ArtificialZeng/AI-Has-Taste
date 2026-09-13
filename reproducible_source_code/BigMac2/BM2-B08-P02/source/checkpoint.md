# Checkpoint

## Job and decision

Release-phase provenance: `bigMac-00008-p02-release-3defdfe0b6e1`.
The candidate remains a `resolution-paper`, with frozen original status
`proved` and accepted evidence snapshot
`cf4597267e383e2f6d584b9ff7d0a39dc9e6aea0ab3436c568fe4ad6aebf1752`.

## Fresh release evidence

- A from-scratch `latexmk` build completed successfully.  The bound final log
  is `manuscript/main.log` (SHA-256
  `c40b7f2ed98047df801bbad95762b1290f7dc0adab6bed095731642d9311a266`),
  with resolved citations/references and no final warnings or layout boxes.
- `audit/manuscript-snapshot.json` now binds manuscript digest
  `a5410eeaa54fffd182f197ac68b5f94a0eb68f05b50790ec06872846b789bff5`
  to PDF digest
  `f248e5787b17ec5a563a9de3ac25df0612805c5d84dfbdc5f3e3e2b40cf2a621`.
- `audit/citations.md` applies the two-pass citation-check workflow.  The
  Tamura--Yamagami primary PDF verifies both Theorem 3.1's rotation-only scope
  and Section 5's general-unitary future problem.  The user-bibliography paper
  is verified as a narrow methodological parallel only.  The direct publisher
  page had one bounded timeout, but its official indexed record and the full
  arXiv copy supplied authoritative corroboration.
- `audit/visual.md` records actual image inspection of exactly pages 1--5.
  Equations, complex-conjugation bars, references, margins, and page transitions
  are all legible and unclipped.
- Both exact verification programs pass freshly.  `source.md` remains unchanged
  at SHA-256
  `93dae429fcc298c6e538247a4cdaa8e4d6dbaddc20ed8cb4bc7fe60f9cc8d088`.
- `release_gate.py check` passes the current five-page PDF and every fresh
  citation, build, visual, role, snapshot, and build-log provenance binding.

## Obstacles and limits

No mathematical, citation, build, or visual blocker remains.  The paper makes
no priority claim beyond the inspected primary boundary.  Local release audits
do not constitute peer review or public submission.

## One next test

The supervisor may now run `release_gate.py publish` to activate the exact
validated PDF and manifest.
