# Checkpoint

Job: `bigMac-00014-p02-release-9e8c4350a7ff` (release phase).

## Accepted scope and evidence

- `source.md` remains immutable with SHA-256
  `acde4095c880fb75747d10f4c9d37ebfd2aa609713f0e06131ba150036348c04`.
- `release_gate.py check-math` passed snapshot
  `77e5155bbd028adda1f6ea77987065be2ac927f99e1f34c12d0977b433293ea9`.
  The accepted report is `audit/math.md`, with its verdict recorded in
  `audit/math.json`.
- The manuscript preserves the frozen resolution exactly: for each fixed
  \(\rho<1\), the loop-deleted sticky graph through time \(n\) equals the iid
  graph on \(M_n+1\) skeleton labels; all four fixed-\(k\) limits transfer,
  and only then are the four \(k\to\infty\) asymptotics taken. No growing-degree
  limit, uniformity as \(\rho\uparrow1\), rate, or priority claim is included.

## Writing/build evidence

- `manuscript/main.tex` is a self-contained three-page resolution article;
  `manuscript/references.bib` contains the designated Xie--Zhou iid source and
  one conservatively used graph paper from the user-supplied workbook.
- The workbook record is cited only for an explicit broad deterministic-graph
  contrast and is stated to provide no probability or regular-variation input.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` built
  `manuscript/main.pdf`. The analytic proof uses no computation or simulation;
  the manuscript includes an accurate AI-assistance disclosure.
- Final log and rendered-page inspection found no unresolved citation,
  cross-reference, overflow, or layout defect. `publication.json` lists every
  TeX/BibTeX input and the reproducible build command.
- After correcting the workbook-authoritative capitalization of Zijian Zeng's
  name, a forced clean rebuild and `release_gate.py freeze-manuscript` passed
  with manuscript digest
  `1d4528e03af4ea52abcc3af0a0a1affceb48274577b75e3f9f85498c60a8e7be`
  and PDF digest
  `6e17f36b687befdf2133bb4e6974434a9b37fdd580ab8c8cc050124b473cb6f8`.

## Fresh release evidence

- `$citation-check-skill` was applied in two passes. The primary arXiv text
  verifies the Xie--Zhou metadata, exact four asymptotics, endpoint convention,
  loop-deletion proposition, and dependent-sequence open direction. The Zeng
  record uses `metadata_basis=user_designated_workbook`; external refresh was
  unavailable in scope, and the manuscript limits it to the locally authorized
  deterministic-graph contrast. `audit/citations.json` accepts the current
  manuscript without unsupported novelty or undefined citations.
- The clean final `manuscript/main.log` has SHA-256
  `dfc48d559c17b226fd4cd184f4077625dbce0124533c1f4053fe659fde4ca44f`
  and no fatal, undefined-reference/citation, box, or package warning.
- All three current PDF pages were rendered at 170 dpi and inspected at full
  resolution. `audit/visual.json` records pages `[1,2,3]`; there is no clipping,
  overlap, missing glyph, or legibility defect.
- `release_gate.py check` passed the current snapshot, manuscript, PDF, build
  log, release-job provenance, source enumeration, and exact page list.

## Obstacles

No mathematical, citation, build, visual, or provenance blocker remains.
External refresh was available for arXiv:2609.05290. Refresh of the Zeng landing
record was unavailable in the bounded audit, so the user-designated workbook
remains authoritative for DOI `10.5281/zenodo.22294612`.

## One next test

The supervisor should run `release_gate.py publish` on the unchanged project to
activate the already validated PDF.
