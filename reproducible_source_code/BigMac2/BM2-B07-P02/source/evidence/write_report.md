# Writing-phase checkpoint

Date: 2026-09-08  
Job: `bigMac-00007-p02-write-7e220237d669`

## Evidence

- `release_gate.py check-math` accepted the frozen evidence snapshot
  `eef04bbd239c132e1714ecf5692295d911d0b2fa5fcd1007a1777ad1ad1d7a52`
  and referee `bigMac-00007-p02-referee-ce689f96df77`.
- `manuscript/main.tex` preserves the accepted theorem's full quantifiers,
  value formula, cut classification, invariant-cone classification, boundary
  faces, tie, and lossless translation-averaging statement.
- `manuscript/references.bib` cites the primary Goemans--Linial/Cayley-graph
  source and the workbook-selected Zeng--Liu--Ratnavelu--Ong paper only for
  its accurately delimited exact-certificate methodology.
- `evidence/check_finite.py` reran successfully.  `latexmk -pdf
  -interaction=nonstopmode -halt-on-error main.tex` produced the four-page
  `manuscript/main.pdf` using pdfTeX and Biber.  The final log has no undefined
  citations or references, overfull boxes, underfull boxes, or package/LaTeX
  warnings.  Text extraction and all four rendered pages were inspected.
- `source.md` remains byte-for-byte unchanged with SHA-256
  `3e5ea16b71c4994ed41da59d6c974640eeb23303558f0df40da7550fab4ba6db`.

## Obstacle

The root `checkpoint.md` is itself part of the referee-accepted evidence set.
Editing it after acceptance would invalidate `audit/snapshot.json` and require
a new mathematical referee.  This additive writing checkpoint records the
phase without mutating any accepted mathematical evidence.

## One next test

Run the independent release-phase citation, clean-build, and rendered-page
audits against the frozen manuscript and PDF; repair only issues those audits
identify, then rerun the affected audit before publication.
