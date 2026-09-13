# Checkpoint

Job: `bigMac-00024-p02-release-d817ccc7b1d1` (release-audit phase,
2026-09-09).

## Accepted scope and current state

The frozen `resolution-paper` claim has passed `release_gate.py check-math` at
snapshot `b2d23954f6d5891b916d9e20169010ea5ff36baf3d2dfde3987fd931199d1d82`.
The fresh referee accepted the full original statement: the entire positive
ordered step quadrant, arbitrary finite dimension, attainment at the displayed
radical schedule, and no uniqueness assertion. The final self-contained article
is in `manuscript/article.tex`, with bibliography in
`manuscript/references.bib` and clean PDF in `manuscript/article.pdf`. A fresh
clean build and `release_gate.py freeze-manuscript` succeeded. Citation, build,
and rendered visual audits are recorded in `audit/citations.*`,
`audit/build.*`, and `audit/visual.*`. The final `release_gate.py check` passed
for the current six-page PDF and all current provenance bindings.

## Decisive evidence used in the manuscript

- `evidence/resolution.md` supplies four exact one-dimensional witnesses and the
  positive-quadrant partition proving the global lower bound.
- Six positive smooth-convex interpolation multipliers and the rank-one residual
  `w w^T` give the dimension-free upper certificate at the claimed schedule.
- Both `evidence/exact_resolution_verify.py` and the referee's independent
  `audit/referee_verify.py` were rerun with the mandated research interpreter and
  passed their exact symbolic checks.
- The three local primary PDFs were inspected directly. The article cites them
  only for their displayed definitions, fixed-schedule/composability result, and
  numerical two-step computation; the proof itself is self-contained.
- A fresh `latexmk -C` followed by `latexmk -pdf -interaction=nonstopmode
  -halt-on-error article.tex` completed with no final warnings, undefined
  references, or overfull/underfull boxes. The bound build-log digest is
  `5cd2bc8a687f09510b2e4feedf007e948b224fa2fd69f125c4d97b0d1286fb88`.
- All six freshly rendered pages were visually inspected at 180 dpi. The
  current PDF SHA-256 is
  `d72ea2216e7a5780f2e82b744acf6d9ea358cc709e74644858d419d084a961cf`.
- The three cited claims were checked against the fixed local primary PDFs and
  accessible arXiv records. Citation keys, rendered references, and the full
  two-file publication dependency scope are resolved.
- `source.md` remains byte-for-byte unchanged at SHA-256
  `594fd4769555165cfb4e9bdf68dd348c83d4063c9d908e55abb25f1fd94fa432`.

## Obstacles and limitations

`literature/user_bibliography_check.md` remains absent. The requested workbook
cross-check was therefore unavailable, but every used record and nearby claim
was independently verified from a fixed local primary PDF and an accessible
arXiv record. No reference was treated as nonexistent, and no citation-access
issue remains. The paper limits its claim to two fixed positive steps and does
not assert uniqueness or unrestricted priority.

## One next test

The supervisor should run `release_gate.py publish` for this exact audited
state and verify that `release/main.pdf` has PDF SHA-256
`d72ea2216e7a5780f2e82b744acf6d9ea358cc709e74644858d419d084a961cf`.
