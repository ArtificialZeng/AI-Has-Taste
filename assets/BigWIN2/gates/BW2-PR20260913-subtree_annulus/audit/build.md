# Build review

Verdict: accept. Job: `primary-20260913-subtree-annulus-release-15be98070fa7`. UTC review: 2026-09-12T18:02:38.542531+00:00.
Final manuscript digest: `44da95029b6d3e9c626c3cb12517c693a117b2c3bcf58a89e909ec1852fd7c6b`.
Final PDF digest: `9fb4bdbcf1b7157bbb06eac878995a958c5b4c51944dfdd2d2e4b8b422897775`.

The final forced clean rebuild used the command recorded in `publication.json`,
with `latexmk -gg` additionally forcing regeneration of the engine/BibTeX outputs.
Its exit status was zero. The full command output is `audit/release-build-command.log`.
The checked final engine log is `manuscript/build/main.log`; the BibTeX log is
`manuscript/build/main.blg`. There are no undefined citations or cross-references,
missing/duplicate bibliography entries, fatal errors, or overfull/underfull boxes.
The separate skill checker found exactly seven matching TeX/BibTeX/aux keys.

`audit/release-build-evidence.json` records the actual input scan. The only authored
inputs are the declared main TeX and canonical bibliography; the other local
engine inputs are generated aux/bbl/out files. There are no figure inputs,
local styles, external TeX inclusions or hidden citation dependencies.
All PDF fonts are embedded. The five-page PDF has correct title and author metadata.
Source and all frozen mathematical inputs were rehashed unchanged.
