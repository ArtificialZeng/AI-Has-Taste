# Checkpoint

## Release state

- Release job: `bigMac-00009-p03-release-5e52c78d86fd`.
- Candidate: `resolution-paper`; frozen original status: **proved**.
- Accepted mathematical scope is unchanged: for the full fixed-order union
  $\mathcal A_4$, with arbitrary positive supported stochastic weights,
  $h_{\rm scr}(\mathcal A_4)=11$.
- Evidence snapshot:
  `eedc974190423e8943ef82f6b963b7444c569a84a97db0d7dab2272f1b5f3797`.
- Manuscript digest:
  `ffcabe5a81133faecbbd932c487c750bf440cb3db0fa982fefb3e7ac95b80612`.
- Clean-rebuilt PDF digest:
  `ded68a594b2c150cba63f2d28ca7e08b94a0530d6dfd0212164147fb51f4c193`.
- `source.md` remains byte-identical, SHA-256
  `4f9bfba8efa3d546f6395bd3dbf1f3b5375bfecc6cd2f0f03ab0163c28247545`.

## Fresh release evidence

- A full clean `latexmk` build succeeded. The current nonempty compiler log is
  `manuscript/main.log`, SHA-256
  `ed38b5762f84f9d1a6e844a893155455a4f07ec450dd1daea9c541b17327f217`,
  with no fatal, undefined citation/reference, box, or actionable warning.
- The citation audit used `$citation-check-skill` in two passes. Hsu's author,
  title, date/version, definition, theorem, remark, order-four bound 18, and
  bounded sharpness statement were checked against the primary arXiv record
  and eight-page PDF. All manuscript math claims match the accepted frozen
  scope and exact-certificate report.
- The user-bibliography Zeng item is relevant only to the stated finite-state
  and checker methodology. Its same-day Crossref-based metadata record exists
  in `literature/user_bibliography_check.md`, but fresh Crossref/SSRN metadata
  and original text did not resolve in this bounded release context. It is
  therefore disclosed under `accept_with_citation_limitations`; it supports no
  stochastic-matrix claim.
- Publication dependencies are complete and exactly `manuscript/main.tex`,
  `manuscript/references.bib`; every citation key and rendered reference is
  resolved.
- All PDF pages 1--4 were rendered at 170 dpi and actually inspected. Text,
  mathematics, both tables, references, margins, fonts, and metadata are
  legible and free of clipping or overlap.
- Fresh reports and provenance-bound records are
  `audit/citations.{md,json}`, `audit/build.{md,json}`, and
  `audit/visual.{md,json}`. `release_gate.py check` succeeds with four pages
  and the current digests above.

## Obstacles

No mathematical, build, dependency, or visual obstacle remains. The sole
bounded limitation is fresh primary endpoint/text access for the nonessential
Zeng methodological citation; it is explicitly recorded and does not support
the theorem or novelty.

## One next test

On the unchanged project tree, the supervisor should run
`release_gate.py publish` and verify that the resulting manifest binds
`release/main.pdf` to PDF digest
`ded68a594b2c150cba63f2d28ca7e08b94a0530d6dfd0212164147fb51f4c193`.
