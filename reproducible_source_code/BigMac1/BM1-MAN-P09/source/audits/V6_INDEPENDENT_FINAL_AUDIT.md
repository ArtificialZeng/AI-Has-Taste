# v6 independent final manuscript and archive audit

Date: 2026-08-24 (Asia/Shanghai).

Verdict: **PASS at the independent technical gate, with the scientific status
restricted to two exact computer-assisted partial theorems.**  No fatal or
major mathematical, transcription, certificate, build, bibliography, archive,
or visual defect was found.  The unrestricted complex Hermitian gate, the full
compact-ball quartic, the common-metric theorem, the arbitrary-node bridge, and
the optimal fixed crossing-lens constant remain open.

This verdict is not an unconditional submission-ready declaration.  Before an
actual journal submission, the author must still confirm the displayed name,
affiliation, and email, and must select a venue and confirm that venue's AI
disclosure, acknowledgments, funding, bibliography-style, and source-format
requirements.  No journal peer review is implied.

## 1. Definition-level and quantifier audit

The audit reconstructed the two v6 endpoint changes from the displayed
definitions and the exact programs, rather than accepting the builder report.
The v5-to-v6 `main.tex` diff was inspected in full, and the complete 1,039-line
v6 source was read.

### Common gate and normalization

The manuscript retains the literal fully conjugated gate

```text
G(Q)=a^2|xi_2|^2
    +1/4 |c conjugate(xi_1)+a xi_3+i(ac-(Q^2)_31)|^2
    +1/4 |c conjugate(xi_2)-i(Q^2)_32|^2
    -8a^2(Re xi_1)^2.
```

Both entries of `Q^2`, both conjugations, and the negative danger term agree
with both independent reconstructions.  The manuscript uses one consistent
normalization `Gamma=4G`.  Thus the scale polynomial is
`P=Delta^2 Gamma=4 Delta^2 G`, while the compact-ball polynomial is
`36 Gamma=144G`.  No factor-of-four or factor-of-thirty-six drift was found.

### All-scale island

The formal statement correctly fixes `a=3/5`, `c=4/5` and quantifies over

```text
ell in [8,10],                 w in [-31/100,-29/100],
k   in [-301/100,-299/100],   z in [-101/100,-99/100],
r   in [99/100,103/100],      t in [943/239,969/239].
```

It quantifies over the complete strict legal scale half-line

```text
T>0                    when g<=0,
T>Delta*g/n            when g>0,
```

and states positivity of the cleared polynomial at the applicable closure
endpoint without silently enlarging the strict Schur-boundary branch.  The
active block is positive definite, the Schur complement is zero, and the
resulting Hermitian matrix is PSD of rank two.  The danger sign, the two live
complex phases, the `r=101/100` seam, and both closed `t` endpoints are all
covered.  The theorem does not use real-part monotonicity, the old
discriminant sign, absorption, or a fixed copositivity allocation.

The exact cross multiplication for the fresh radius ceiling is

```text
239*27162772450885609710321172264010161955258866496
-13*499232790087220155922502903379517386791638099025
=1876344627798693774222427164702679015573805219 > 0.
```

Hence the displayed `rho_wide` is strictly larger than `13/239`.  The positive
cross-product is also the printed low-cell `N0` reserve numerator.  All
fourteen fresh reserves in the appendix match the source and referee outputs;
the literal smallest is the derivative-free high-cell danger reserve
`87/500`, and the unique finite ratio bottleneck is the low-cell `N0` sign.
The independent 96-corner test splits exactly into 48 `g>0` and 48 `g<=0`
cases and has minimum direct `T=1` gate

```text
3791537219332938219668993327 / 1612003174500796900000000 > 0.
```

That finite test is correctly labeled diagnostic; the continuum theorem is
proved by the two exact center tensors and fourteen derivative reserves.

### Moving-sheet island

The manuscript correctly retains the strict domain `0<S<=1/10000`; it does
not include `S=0`, where `lambda=(1+M)/S` is undefined.  The new final cell is

```text
1/20<=X<=1/19,
u=380(X-1/20) in [0,1],
S=X*sigma,  0<sigma<=1/500.
```

Thus `u=0` is exactly the predecessor seam and `u=1` is the new endpoint.
The legality proof is separate from the gate estimate and covers

```text
59/400 < Z < 1/6,
1-x^2-y^2-Z >= 4887491031701/10555545000000 > 0,
det(C)=(5/9)SZ>0,
lambda>0,
```

so the data are strictly dangerous and the Hermitian compression and `Q`
are PSD of rank two.  Both signs of `z` are covered because the reconstructed
compression depends on the signed variable only through `z^2=Z`; no division
by `Z-1/8` occurs.  The theorem retains the normalized-scale constraint
`lambda*S=1+M` and makes no maximality, full-collar, or full-ball claim.

The source and referee independently reconstruct 20 quotient terms, 16
higher terms, and 947 centered parameter monomials.  Both reproduce the
strict continuum reserve

```text
26756976522448207008651434175031131058236664369690137089162898293759
/13308465593548800000000000000000000000000000000000000000 > 0.
```

The wrapped `m_19` numerator and denominator in Appendix B concatenate to
exactly these integers.  The 72 legal endpoint/seam nodes and the two printed
endpoint values are correctly described as falsification checks, not as the
continuum proof.

### Stale-endpoint and scope search

No `363/92`, `373/92`, `5M_f/92`, “all eight closed cells,” or “seven
adjacent-layer” statement remains in `main.tex`.  Its occurrences of `1/20`
are the necessary predecessor cell, seam, and diagnostic endpoint for the new
X19 cell, not a stale theorem endpoint.  Historical `5/92` and `X20` mentions
in `README.md` explicitly describe the frozen v5 baseline and do not
contradict the v6 statement.  The abstract, introduction, theorem statements,
scope section, and disclosure all say that the general problems remain open.

## 2. Exact verifier and manifest replay

All commands were run from the packaged `certificate_workspace/`, which is
the repository-relative layout explicitly documented in `README.md`.

Normal exact execution returned exit code 0 for all four new programs:

```text
3e2cb11a74a7e77993f3464ccdd888f2dd5d495903b137444adf05344e68bf09
  scale source
c29f5c864a66c369c439976fb9873d8a22a4a935c3286e7656e16638371c71a8
  scale independent referee
1287290731cb2b5dd24789116f4f1dadc23dd213d45c90ae302f65101326fc34
  X19 source
35e9d90c6ac1fcb8ba2d304e60ddd98d5a56f2e8347a174cfed9af009ba2a01c
  X19 independent referee
```

The four corresponding `python -O -B` executions each returned exit code 1
with the intended explicit fail-closed error.  The source and referee programs
therefore do not silently pass when optimized Python removes assertions.

The four direct dependency manifests passed.  The grouped scale-cubic
manifest passed with 60 entries and the grouped moving-sheet manifest passed
with 63 entries.  Before this audit report was added, the candidate release
manifest passed all 273 bound-file checks and had SHA-256

```text
fa580e1fe38b1d745e9cfaeff9beb9704058b8b8504fa5f1471f33ea0aa3bfce.
```

The `certificates/` copies are convenience reading groups.  Running a copied
verifier directly from that directory is not a supported replay layout; it
correctly rejects missing repository-relative dependencies.  The README's
documented `certificate_workspace/` commands succeed, so this is not a
reproducibility defect.

## 3. ZIP, clean build, bibliography, and logs

The final archive passed `unzip -t` and contains 274 files plus 10 directory
entries.  Its SHA-256 agrees with the external sidecar:

```text
00ff125f69333c31205b44f75785b14042d389b19713febd207129df3921152a.
```

A fresh extraction contained exactly one top-level release directory.  Its
273-entry release manifest passed before any clean-build mutation.  The
distributed `main.pdf` was byte-identical to the separately delivered output
PDF, and the extracted `main.tex` and `references.bib` were byte-identical to
the candidate tree.

From the fresh extraction,

```text
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

both returned exit code 0 under TeX Live 2026 / `latexmk` 4.88.  BibTeX was
run from the packaged `references.bib`; the rebuilt `main.bbl` was
byte-identical to the distributed bibliography.  The converged `main.log`
and `main.blg` contain no undefined citation or reference, missing database
entry, repeated entry, LaTeX or package warning, overfull/underfull box,
fatal error, undefined control sequence, or runaway argument.

The clean rebuild has the same 482,426-byte page content but a different
SHA-256 because pdfTeX regenerated time metadata.  Rendering the clean rebuild
and the delivered PDF independently at 150 dpi produced 17 pairwise
byte-identical PNG pages.  Thus the archived PDF/output-PDF byte identity and
the clean-rebuild visual identity are both established without pretending
that timestamped PDF containers are reproducible byte for byte.

The bibliography checker and the mathematics-workflow LaTeX auditor both
reported

```text
cited keys: 5
BibTeX keys: 5
missing bibliography files: 0
cited keys missing from bibliography: 0
unused entries: 0
auxiliary-file disagreements: 0.
```

The five keys are `MR2223270`, `Crouzeix_2003`, `MR2449098`, `MR2047592`,
and `Crouzeix_2016`.  The v6 and frozen v5 `references.bib` files are
byte-identical with SHA-256
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`,
and the v6 delta changes no citation context.  Therefore the frozen official
primary-source audit remains the applicable per-reference audit; no changed
citation surface required a new web lookup.

## 4. PDF inspection

The delivered PDF has:

```text
SHA-256: 108df96cbe20e438db0e7dbcb6534a2d65339431f210627a2caf691a865558d2
size:    482426 bytes
pages:   17
paper:   612 x 792 pt (US letter)
title:   Two exact positivity islands for a complex Hermitian rank-two
         scalar gate arising in a common-metric problem
author:  Zijian Zeng
```

All 17 pages were rendered and independently inspected, including the title
page, theorem statements, table, long formulas, wrapped exact integers,
verbatim blocks, disclosure, references, headers, footers, page numbers, and
the final-page whitespace.  There is no clipping, overlap, missing glyph,
black box, broken equation/table, or malformed reference.  All listed fonts
are embedded subsets.  The large whitespace on the reference page is a clean
consequence of the short bibliography and `\raggedbottom`, not a rendering
failure.

## 5. Disclosure and remaining gates

The README and builder report accurately call this a local partial-theorem
candidate and state the pending author/venue confirmations.  The manuscript
discloses that symbolic computation and an AI coding assistant were used for
certificate verification, endpoint transcription, packaging, typesetting,
and build checks.  It does not attribute an unverified mathematical claim to
AI.  It states accurately that no Lean or other proof assistant formalizes
either complex theorem; older real-algebraic formalizations are not presented
as support for this paper.

No `main.tex`, certificate, PDF, or bibliography repair is required.  The root
release task must now add this audit to the release manifest, update the README
from “awaiting independent final referee” to “independent technical audit
passed,” regenerate the ZIP and sidecar, and rerun the final manifest/archive
checks.  Those packaging updates do not change the mathematical verdict.

Scientific terminal status: **partial theorem**.  Proof-assistant status:
**none for either theorem in this manuscript**.
