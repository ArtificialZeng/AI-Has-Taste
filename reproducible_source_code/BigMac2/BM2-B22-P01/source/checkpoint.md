# Checkpoint

- Job: `bigMac-00022-p01-release-c14619b2439d` (`release`, 2026-09-09).
- Candidate: accepted `resolution-paper`; original status `proved`. The frozen
  theorem remains the exact full-scope identity
  `W_2(L,R,d)=c_2^2 L^2 R^2` for finite `d>=1`, `L>0`, and `R>=0`.
- Mathematical provenance: `release_gate.py check-math` passed for evidence
  snapshot `6a00a06eb5398d38ae7fbf777eaafd922f200ff5cc110f0d64e3ee2ee0b09344`
  and referee job `bigMac-00022-p01-referee-848372920490`. No mathematical
  evidence or manuscript source changed in release review.
- Citation audit: the advisory `citation-check-skill` was explicitly applied
  in two passes. All six records and their nearby claims were checked. Du's
  original local PDF confirms the `N=1`, `N>=7`, and open `2<=N<=6` scope;
  Taylor's exact interpolation condition matches equation (2); the two
  relevant workbook-selected Preprints records were verified on their official
  pages and remain narrow methodological comparisons. There are no undefined,
  contradicted, or unverified citations. See `audit/citations.md`.
- Build audit: after `latexmk -C`, the declared build command exited zero. The
  final `manuscript/main.log` has SHA-256
  `2bfb7cb03c8cae3e8d9e2978bd3dc90d77c617b2203b184fe5d2bef82ae99509`
  and no final warnings. The fresh PDF has six pages, extractable text, embedded
  fonts, and SHA-256
  `a94a4a29396791b6a8b98df1f5c9ffa4c4e3deaf7b0eb95eb8e75af85b47f422`.
- Manuscript snapshot: digest
  `620e40ff64cedd8ed7101252b6a8e79283e2a36d2efc3e85c63381f969847f0d`,
  bound to the current PDF digest above.
- Visual audit: pages 1 through 6 were rendered at 170 dpi and each inspected
  at original resolution. Equations, tables, references, links, margins, and
  metadata are legible with no clipping or overlap. See `audit/visual.md`.
- Integrity: `source.md` remains unchanged with SHA-256
  `cb630d3906f2a0db9b936972143987f99a01faad43bec348a26b8f7c81dfadf8`.
- Release gate: the final schema/provenance checklist passed and
  `release_gate.py check` returned `ok:true` for the current six-page PDF.
- Status: **ready for supervisor publication**.
- Obstacles: none. External metadata refresh was available for all cited
  records; no citation limitation was needed.

## Next test

The supervisor should run `release_gate.py publish` to activate the exact
audited PDF and manifest.
