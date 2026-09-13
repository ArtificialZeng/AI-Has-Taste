# Checkpoint — release phase

The immutable `source.md` remains SHA-256
`0e7fc6f0cd8d29cc431c9bcebf012475d8f6e821a88b9df7c8f421e772bee113`.
`release_gate.py check-math` passed against accepted snapshot
`5d141b6b1ca16a35121e8276a6b73a6a96c20f2f114c8cfd125fce39b27bcf47`.
The accepted scope is the complete frozen conjunction: Gauss feasibility at
`d=7`, mixed infeasibility at `d=7`, and mixed feasibility at `d=6`; it makes no
claim about the existence of an LCD code.

Final publication sources are `manuscript/article.tex`,
`manuscript/references.bib`, and the ancillary exact certificates/checkers
listed in `publication.json`. The note states the LPs, gives the full 23-coordinate
integral Gauss witness, and proves the mixed claims from the accepted sparse
rational point and dyadic Farkas certificate. It identifies the exact verifier
row counts and includes a reproducibility and AI-assistance disclosure.

The bibliography conservatively cites the primary Kang--Xiong preprint, the
joint-enumerator paper of Alahmadi et al., and the genuinely relevant workbook
record of Zeng et al. only for high-level exact-certificate methodology. Online
refresh of the two September/August 2026 preprints returned no result; the Zeng
et al. metadata therefore remains based on the user-designated workbook, as
required, and no mathematical attribution depends on external refresh.

Both standalone verifiers passed using the mandated research interpreter.
`latexmk` then completed a clean build of the five-page
`manuscript/article.pdf`; the final log has no warnings, undefined references,
or overfull/underfull boxes. Text extraction, PDF metadata, embedded fonts, and
rendered images of all five pages were inspected. `release_gate.py
freeze-manuscript` succeeded and wrote `audit/manuscript-snapshot.json` with
manuscript digest
`8726002cf99990b0538a7b3cc103b078be1fb51180d4d326b035c7056f1a3f9c`.

## Fresh release evidence (2026-09-09)

The citation-check workflow was invoked as an advisory two-pass audit.  Its
fixed extraction contains the three substantive attributions in the manuscript.
Primary records support Alahmadi et al.'s joint-weight-enumerator LP and the
version-specific Kang--Xiong definitions and reverse screening statement.
The Zeng et al. record is genuinely relevant only to the stated broad exact-
certificate methodology comparison; its metadata is preserved from
`literature/user_bibliography_check.md` as the user-designated authoritative
workbook record, and the Preprints.org primary page was also accessible.
No citation key is undefined and no citation supports the proof itself.

## Next test

The two exact certificate replays passed with the mandated interpreter.  A
forced clean LaTeX/BibTeX build completed with no final warnings, undefined
references, or layout diagnostics.  The manuscript snapshot was refreshed at
unchanged source digest
`8726002cf99990b0538a7b3cc103b078be1fb51180d4d326b035c7056f1a3f9c` and PDF
digest `dc0e7cdad08b8ab44088b5088619856056551f5360bb75b42e564881efc0eee7`.
Every rendered page 1--5 was inspected at 180 dpi; no clipping, collision,
overflow, illegibility, or font-embedding defect was found.  Fresh citation,
build, and visual reports and digest-bound JSON audits are in `audit/`.

No release obstacle remains.  `release_gate.py check` passes.  Next test: the
supervisor should run `release_gate.py publish` to activate the audited local
deliverable.
