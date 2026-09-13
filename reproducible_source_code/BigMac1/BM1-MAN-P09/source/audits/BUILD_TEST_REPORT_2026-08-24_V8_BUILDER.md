# v8 builder report: independently audited high-Z phase-tube integration

Date: 2026-08-24 (Asia/Shanghai).

Status: **builder-complete partial-theorem candidate pending a separate
independent v8 final manuscript/archive audit**.  This report records exact
certificate replay, transcription, bibliography, deterministic build, and
visual gates.  It is not the independent final referee report.  The complete
high-Z axis caps, a full positive-Z collar, the full compact unit ball, the
general complex Hermitian gate, one common metric for arbitrary separators,
the arbitrary-node bridge, and the optimal constant of a fixed crossing lens
remain open.  Unconditional submission-ready status also requires confirmation
of author metadata and the selected venue's disclosure, acknowledgment,
funding, bibliography, source-format, and style requirements.

## Frozen baseline and exact v8 delta

The source was copied from the frozen, independently audited v7 release.  The
v7 directory was not edited.  No global claim ledger, approach registry,
counterexample database, research state, portfolio, dispatch file, or
automation was edited, and no new mathematical search was performed.

The only mathematical delta is the already independently audited high-Z
phase-tube theorem in the lossless compact-ball chart:

```text
0<S<=1, lambda>0, 0<=x<=1/8, |y|<=1/64,
Z=z^2=63/64-x^2,
```

with both signs of `z`.  It has danger reserve at least `63/4096`, support
determinant `(5/9)SZ>0`, and `31/32<=Z<=63/64`.  The source certificate has
`300/300` strictly positive coefficient controls.  The projective full tensor
has 1125 controls: 945 are positive and precisely 180 are the artificial
`S=0` closure zeros.  The independent referee reconstructs a signed-`z`
two-atom Gram chart and obtains the controls by rational nodal collocation,
without importing the source polynomial or its Bernstein table.

The former one-dimensional `y=0` bridge arc is strictly contained because the
new theorem includes every `|y|<=1/64`.  The theorem is nevertheless only a
two-real-dimensional surface family; its scope is not enlarged to either axis
cap, a three-dimensional collar, or the full ball.  The v7 scale island and
positive-Z moving-sheet island, their citations, and all frozen limitations
are retained unchanged.

## Exact certificate replay and fail-closed tests

The two new normal replays from `certificate_workspace/` exited 0:

```sh
python -B tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_phase_tube_theorem.py
python -B audit/verify_common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_phase_tube_independent_referee.py
```

Both reported the exact calibration, legal reserve, Hermitian `Q,Q^2` gate,
two signed branches, all 300 coefficient controls, the `945+180` projective
classification, and all listed boundary faces.  Each verifier failed closed
under optimized Python, a forced dependency-hash corruption, and deletion of
one raw `C4` monomial.  The deleted-term attack left the nonzero exact residue
`25*S^4*lambda^4*x^4/81`.  The observed exit-code pattern for each verifier
was `normal/optimized/bad-dependency/dropped-term = 0/1/1/1`.

Both direct manifests passed from the distributed workspace.  Their
manifest-file SHA-256 values are:

```text
source:   bc499c5a811ba076995c2f17699a5a2bcea35e720e51e99b3ffd016edd983538
referee:  3637e39e601de8a6a1df3ed1c45877f23a5258030ac0706ff108228a7786820d
```

The decisive verifier hashes are:

```text
source:   4b5aa909e84d449f5b05813c4e15266eec4742ca366cbbde3de6ca17dbae9202
referee:  42e262cfa4d463b343f4da744255efa7e31ca8490f9d454e623c531580ef81eb
```

No Lean or other proof assistant formalizes the new complex phase-tube
theorem.  Existing formalizations elsewhere concern narrower algebraic cores
and are not cited as support here.

## Clean build, bibliography, log, and PDF QA

Environment used for replay and build:

```text
Python 3.13.5
SymPy 1.13.3
latexmk 4.88
Poppler pdftoppm 26.04.0
SOURCE_DATE_EPOCH=1787539200
FORCE_SOURCE_DATE=1
```

The source was built from a clean LaTeX state with the fixed epoch above:

```sh
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both exited 0.  The mathematics-workflow auditor reported
`cited=5 bib=5 missing=0 unused=0`.  The converged `main.log` and `main.blg`
contain no undefined citation or reference, missing database entry, repeated
entry, LaTeX/package/pdfTeX warning, fatal error, undefined control sequence,
runaway argument, overfull box, underfull box, or missing character.  The
microtype package retains protrusion but disables font expansion, eliminating
the prior engine-level font-expansion warning without changing the mathematics
or font family.

The PDF is US letter size and 20 pages.  All 20 final pages were rendered at
150 dpi with Poppler and inspected.  No clipping, overlap, missing glyph,
black box, broken equation, malformed reference, or unexpected blank page was
found.  Headers, footers, links, the new theorem and control table, the exact
data appendices, bibliography, and final-page whitespace were checked.  Every
listed font is embedded.

Frozen manuscript hashes before release-manifest generation:

```text
4c5b942f8cc0c2f143b86666f806a3247132dbc868752ef51db320abe739f12e  main.tex
1e7fc5da25897c0bbcc332262d97ebf00a60dc653e583f187ec4f30c55124045  main.pdf
3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b  main.bbl
989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600  references.bib
```

## Archive closure and remaining gate

`RELEASE_MANIFEST.sha256` binds every distributed file other than itself.  A
candidate ZIP was freshly extracted into a new temporary directory.  It had
exactly one top-level directory, 355 files, and a 354-entry manifest; every
manifest entry passed.  A clean rebuild from that extraction with the same
fixed epoch exited 0, repeated the `5/5` citation result and zero-warning log
gate, and produced a PDF byte-for-byte identical to the packaged and external
PDF, with SHA-256
`1e7fc5da25897c0bbcc332262d97ebf00a60dc653e583f187ec4f30c55124045`.
After recording this result in the builder report, the final manifest and ZIP
are regenerated and the same extraction gate is repeated.  The authoritative
external PDF and ZIP hashes are written in sidecars because a ZIP cannot
contain its own hash without changing itself.

The remaining technical gate is the separate independent v8 final
manuscript/archive audit.  The remaining nontechnical gate is confirmation of
author metadata and the selected venue requirements listed above.
