# Checkpoint

Provenance: `bigMac-00012-p04-release-9be4863a8fdd` (release phase), following
research job `bigMac-00012-p04-research-a692b3c6f3b3` and accepted referee job
`bigMac-00012-p04-referee-c0dd5eea6eed`.

## Current claim and status

The frozen original problem is proved at the mathematically accepted scope:
for each fixed real `alpha`, `Y_d -> 0` almost surely if and only if
`alpha > 1/2`. At `alpha=1/2`, for every `epsilon>0`,
`sum_d P(|Y_d|>epsilon)` converges exactly when `epsilon>2`.

The accepted audit is `audit/math.json` with report `audit/math.md`, bound to
snapshot digest
`cf4cff3871118a964f2e6ebdc11084f9698cf7e16533ec52b38fa970166bef78`.
No mathematical gap was reported.

## Manuscript evidence

- `manuscript/article.tex` is a concise self-contained resolution paper with
  the product-law assumptions, exact reduction to one spherical coordinate,
  two-sided moderate-tail estimate, endpoint series test, and both
  Borel--Cantelli implications.
- `manuscript/references.bib` cites the nearest Pearson-walk paper and the
  one relevant methodological comparison selected in
  `literature/user_bibliography_check.md`. The latter is explicitly stated not
  to supply any spherical-tail or Borel--Cantelli input.
- `manuscript/article.pdf` is a clean three-page build from
  `latexmk -pdf -interaction=nonstopmode -halt-on-error article.tex` using
  pdfLaTeX and BibTeX. The final log contains no warnings, undefined
  references, or overfull/underfull boxes; all fonts are embedded.
- `publication.json` lists every TeX/BibTeX input and the PDF.
- `audit/manuscript-snapshot.json` freezes manuscript digest
  `c447e4de4fd2cd1e48791c83067f28e6b21948b87c3148766e0de922f49f3e34`
  and PDF digest
  `30f3dc60a9e1cbbf21c652e6f753f14ae3ec5415d550322725cc447c7c83a846`.

The immutable `source.md` remains byte-for-byte unchanged with SHA-256
`498d1539dec19fb641258fcd83fb84090a5c6975a3e1979fbc8adc5b3904f9d1`.

## Release audit evidence

The arXiv record and the original 11-page v1 PDF were checked directly; its
Example 6.5 supports the manuscript's neighboring polynomial-family comparison.
The supplied SSRN DOI/title did not resolve through the bounded web searches,
Crossref API access failed at the network layer, and a browser attempt timed
out. To avoid relying on unavailable full text, the manuscript comparison was
narrowed to the paper's title-level topic and expressly says no result from it
is used. This is a disclosed citation-access limitation, not mathematical
evidence. `source.md` still has SHA-256
`498d1539dec19fb641258fcd83fb84090a5c6975a3e1979fbc8adc5b3904f9d1`.

A clean `latexmk` rebuild succeeded with no final warnings; the bound log is
`manuscript/article.log` (SHA-256
`b610d1149d605e28cb1386306e496a036d86989cac2d9806aa8d469e24a63c97`).
All three 170-dpi rendered pages were opened and found free of clipping,
overlap, or illegible material. Fresh reports and digest-bound records are
`audit/citations.*`, `audit/build.*`, and `audit/visual.*`. The current
manuscript digest is
`756163786146da2d169649de3ae8e7cb0588a17f2b6f5b982ed62354df9888d7` and
PDF digest is
`11f776b1f55c085ad6311c2761b9803a43da4ff404a1f8268bcd3d093c65a07c`.
`release_gate.py check` succeeded for this exact state.

## One next test

The supervisor should run `release_gate.py publish` and verify that the active
manifest binds the same manuscript and PDF digests.
