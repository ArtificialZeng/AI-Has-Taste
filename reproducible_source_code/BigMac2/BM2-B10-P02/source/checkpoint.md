# Checkpoint

## Accepted mathematical scope

- Research provenance: `bigMac-00010-p02-research-53f7673708d0`.
- Fresh referee provenance: `bigMac-00010-p02-referee-09e992174bab`.
- `audit/math.json` accepts the unchanged frozen `resolution-paper` claim, and
  `release_gate.py check-math` passes with snapshot digest
  `36a1a4f0329030693dcac1a4882f04ade8a4069c4fc496cffbfd95c06e5949fb`.
- The proved result is the compact-uniform boundary-layer limit
  \[
  N^{-3/2}u_N(\lfloor x\sqrt N\rfloor)\to
  U(x)=\frac{S-\Phi(x)}S A(x)+\frac{\Phi(x)}S B(x),
  \]
  with the exact Green kernel and uniform tail bound in
  `evidence/green_kernel_resolution.md`.  The unique crossing
  \(A(x_*)=B(x_*)\) gives \(C_*=A(x_*)=B(x_*)\), and every maximizing state
  satisfies \(s_N/\sqrt N\to x_*\).  Thus the full extended-half-line limit
  set is \(\{x_*\}\).  The decimal values
  \(x_*\approx0.86314241094\) and \(C_*\approx0.94149933731\) are checks only.

## Writing-phase evidence

- Writing provenance: `bigMac-00010-p02-write-ccab7020c16f`.
- The self-contained English article is `manuscript/paper.tex`, with bibliography
  input `manuscript/references.bib` and compiled output `manuscript/paper.pdf`.
  `publication.json` enumerates every publication input and the PDF.
- Clean build command:
  `cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex`.
  The final log has no undefined citations/references, overfull boxes, or other
  LaTeX warnings; the PDF has five pages and extractable text.
- `release_gate.py freeze-manuscript` passed.  The frozen manuscript digest is
  `72309c3f2641112993d2bce9b4800c1d652c78b8b6cd0fe9557eae33543c18ae` and
  the PDF digest is
  `02287a10d67551305212153f01c939eee583a1bc22963ced9849c86e46857a58`.
- Mossel's arXiv metadata was checked against the primary arXiv record.  The
  workbook-selected Zeng record was inspected in
  `literature/user_bibliography_check.md`; it is cited only for its supported
  proof-architecture analogy, with an explicit disclaimer that it supports no
  consensus-dynamics claim.

## Obstacles

No mathematical, build, or visual obstacle is known.  Fresh release citation
review verified Mossel against the primary arXiv record and exact cited
locations.  The newly deposited Zeng SSRN item could not be freshly retrieved
after bounded title/author/venue/DOI searches (web fetch rejection and no shell
DNS); `audit/citations.json` therefore discloses the single permitted citation
access limitation.  No contradicted attribution, undefined key, unsupported
novelty claim, or misleading consensus-dynamics use was found.

## Fresh release evidence

- Release provenance: `bigMac-00010-p02-release-93e775dd2753`.
- A clean `latexmk -C` then `latexmk -pdf` rebuild passed.  The final log is
  `manuscript/paper.log` with SHA-256
  `a0fd123bb7fdb2f44bedbced56b4da4ae264e7a818cc9c81b3e31aeab80cae7f`.
- The refrozen manuscript digest remains
  `72309c3f2641112993d2bce9b4800c1d652c78b8b6cd0fe9557eae33543c18ae`;
  the rebuilt PDF digest is
  `a0163022d03e98b7dac015a83a4b7c8cced1a502ec306d31f857da1e2fdd0a17`.
- Every page 1--5 was rendered at 160 dpi and individually inspected.  No
  clipping, overlap, unreadable formula, missing glyph, or bibliography defect
  was found; all fonts are embedded.
- Fresh reports and digest-bound records are `audit/citations.*`,
  `audit/build.*`, and `audit/visual.*`.

## One next test

Run `release_gate.py check` on the current project; if it succeeds, return
`ready` for the supervisor's separate `publish` step.
