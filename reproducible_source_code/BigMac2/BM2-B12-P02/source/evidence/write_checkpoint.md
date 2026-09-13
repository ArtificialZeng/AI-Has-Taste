# Writing-phase checkpoint

Writing job: `bigMac-00012-p02-write-6ebc82f73d43` (2026-09-07).

## Evidence

- `release_gate.py check-math` accepted snapshot
  `03c3fa4dabb4b497c7bf1c1bd4cb2f0ae986deedb09d28fad45d0ab2bde8d0bf`.
- The concise resolution paper is in `manuscript/main.tex`, with bibliography
  in `manuscript/references.bib` and compiled PDF in `manuscript/main.pdf`.
- A clean `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
  build produced a four-page PDF with no unresolved citation/reference,
  overfull-box, or fatal diagnostics in the final log.
- The manuscript cites Fromentin--Godelle for the exact Condition-A criterion
  and exceptional even-`D` context. It also includes the user-list Zenodo
  record only for the limited, explicit comparison of exact finite-group
  certification practice; no Artin-monoid claim is attributed to that paper.
- `release_gate.py freeze-manuscript` recorded manuscript digest
  `6af608c06d120f3f0ad3d1f4621bb3f92e7a96f73bd6bcc1027917064a4295af`
  and PDF digest
  `01b7d2777f18ac3dee385fbdbb2d679b2e9bc5b8467e3765a3977a1a3bb71740`.

## Obstacle

The root `checkpoint.md` is itself listed in `claim.json` as decisive evidence
and is hash-bound by the accepted mathematical snapshot. Mutating it after
acceptance would invalidate the referee audit and make the required manuscript
freeze fail. It was therefore preserved exactly; this writing update is kept
as a separate evidence checkpoint.

## One next test

Run the fresh release-phase citation, clean-build, and all-pages visual audits
against the frozen manuscript and PDF digests above.
