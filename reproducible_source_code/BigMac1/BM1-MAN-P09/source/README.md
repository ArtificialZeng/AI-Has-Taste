# v18 stitched-sheet and extended local-box candidate package

**Paper:** *Exact stitched-sheet, local-box, and complex-phase-tube positivity
for a Hermitian rank-two scalar gate*

**Authors:** Zijian Zeng; Houde Liu; Kuru Ratnavelu; Ong Seng Huat; Yonghua
Xiong (corresponding author)

This is a v18 **candidate** copied from the frozen submission-ready v17
release dated 2026-08-26.  It contains
the LaTeX source, BibTeX database, generated bibliography, compiled PDF,
prior mathematical and bibliographic audits, the frozen v7 builder and
independent-final reports, and the exact source and referee certificates
underlying the partial theorems.  Frozen v17 remains byte-for-byte unchanged.
The first independent v17 submission audit
was frozen as **FAIL (fatal 0 / major 2 / minor 0)**: it found one visibly
printed missing-backslash spacing token and one constant-$Z$ second-cell legality paragraph
placed inside the preceding recentered-sheet proof.  The repaired manuscript
changes only those two manuscript defects: the command is now `\qquad`, and
the unchanged second-cell derivation now appears inside the constant-$Z$
proof after `Z_const` is defined.  A fresh independent v17 submission
reaudit of the repaired manuscript passed with **fatal 0 / major 0 / minor
0**.  It verified the exact theorem scope and proof order, six post-v16
certificate chains, five-key bibliography closure, two deterministic clean
builds, the 41-page visual and metadata gates, and five fail-closed attacks.
The failed and passing reports, the passing verifier, its results, and its
three-file manifest are retained under `audits/`.  The historical failed
report has SHA-256
`607197b7da4cb02d876ddcc93a0cc60cbb1ec832d7e2a1546c43ab55f9c8066d`;
it is not represented as a pass for the repaired bytes.  The passing report
has SHA-256
`0a6568d6cfc0f54424980b5fb7b013a34be758c61998a6879032854fc2a3fa07`.
The audited manuscript and PDF hashes are respectively
`cfd1be699b3fba93b16288d846552ce883f2b75883a930ea527c1de87b67e6ff`
and
`41f816165950f9d5369f0cc4583b33f396fb7bb3d3b937d8a62f8b1177611939`.
The formal release manifest is regenerated only after these audit artifacts
are included and is replayed again from the final archive.  The v7
baseline passed mathematical,
certificate, attack, bibliography, clean-build, archive, and 18-page visual
gates with zero fatal, major, or minor technical defects.  Relative to that
frozen baseline, v8 adds one independently audited high-Z complex-phase tube
and its source/referee certificate pair.  Relative to v8, v9 changes no
mathematical statement: it repairs the two packaged copies of the X18 source
verifier so that each derives its release root from its own `__file__` path,
uses only the package-local `certificate_workspace/`, and fails closed for an
unknown layout.  The independent v9 audit found that the grouped X18 referee
still used a one-layout parent count.  v10 repairs that referee in both
distributed copies and confines every resolved dependency to the package.
It also integrates the independently audited X16 closed cell,
extending only the same five-real-parameter moving sheet from `X<=1/17` to
`X<=1/16`.  The independent v10 final audit found zero fatal, major, or minor
technical defects.  v11 added only the root-replayed X15 and X14 closed cells,
`1/16<=X<=1/15` and `1/15<=X<=1/14`, with explicit package-confined
two-layout source and referee resolvers.  v12 incorporates the root-replayed
X13 through X5 reciprocal cells and the X4 exact centered breakpoint.  The
centered sheet has a strict gate certificate through
`X*=428905727/1858957100`, but uniform strict danger only for `X<X*`.
It also incorporates a distinct affine-`omega` tilted chart
`omega_phys=omega-(10636/275)(X-1/5)` on the closed interval
`1/5<=X<=3/13`, with `D>=S/100>0`.  The charts meet at `X=1/5`, so their
union is connected; they are not one enlarged parameter sheet.  The frozen
v12 package and PDF were not modified by v13.  The frozen v13 release added a
separate inward-`Z` sheet on `3/13<=X<=1/4`, joined parameter by parameter to
the affine-`omega` sheet only at `X=3/13`.  Its exact continuum certificate
has 32 `(S,X)` coefficients, a 32-coefficient core with 1,581 centered
monomials, and 80 Bernstein controls: three artificial `S=0` closure zeros
and 77 strict controls.  The independent v13 final audit passed with zero
fatal, zero major, and one documentation-only minor: its README treated the
JSON release manifest as a line-oriented checksum file.  The v13 PDF and ZIP
remain immutable.

The frozen v15 release extended the same inward sheet through the exact endpoint
`X=83059/100000`.  Two adjacent cells each have 40/40 strict exact Bernstein
controls, full legality, both signed lifts, and independent definition-level
referees.  At `X=4153/5000` the gate controls remain strict but the present
shape chart has an exact negative `Z` corner, giving the chart-legality root
bracket `83059/100000<root<4153/5000`.  This is not a raw-gate counterexample
or a maximality theorem.

The frozen v16 release adds a fourth, formula-distinct compact-ball sheet
`Z_rec=Z_in+2(X-83059/100000)`.  Eight independently audited exact cells
cover

```text
83059/100000 <= X <= 1019767/1040000.
```

Every cell has 40/40 strict rational Bernstein lower controls, complete
compact-ball legality, both signed lifts, exact three-level stitches, and a
separate no-import definition-level referee.  At the right endpoint the
`S=0` danger base is zero, but `T<=-4181417/143000` gives strict danger for
every physical `S>0`.  Immediately to the right, sufficiently small positive
`S` makes this particular recentered chart illegal.  This is not a negative
raw gate, a full-ball maximality theorem, a common-metric theorem, or a fixed-
lens solution.

The same release adds a fifth, seam-preserving constant-`Z` sheet

```text
Z_const = Z_rec - 2(X-1019767/1040000),
1019767/1040000 <= X <= 99/100.
```

It agrees with the recentered sheet at the parameter, cleared-gate, and
cleared-core levels.  The exact source and independent no-import referee both
recover structure `32/32/1581`, bidegree `(7,4)`, 40/40 strict rational
Bernstein controls with unique weakest index `(7,0)`, complete legality for
both signed lifts, and 72/72 diagnostic nodes.  At the seam the danger base
is zero, but the exact bound `T<=-8425123367/286000000` proves strict danger
for every physical `S>0`.  The endpoint `99/100` is only the end of the
audited cell; no continuation or maximality is asserted beyond it.

The frozen v17 release extends that same constant-$Z$ chart by one adjacent exact
cell,

```text
99/100 <= X <= 497/500.
```

The extension again has structure `32/32/1581`, bidegree `(7,4)`, and 40/40
strict controls.  Its exact legality reserve includes
`D>=9833/2600000>0`.  The displayed chart's worst-corner legality root lies
strictly between `497/500` and `199/200`; this is not a raw-gate negative or
a maximality statement.

At `X=497/500`, the frozen v17 release splices the cap chart

```text
x_cap = x_old - (3/2)(X-497/500),
y_cap = y_old,
Z_cap = Z_const + 2(X-497/500),
497/500 <= X <= 1.
```

The full parameters, positively cleared raw gate, and cleared core agree at
the seam.  The cap chart is strictly legal through `X=1`; its exact
continuum certificate has structure `48/48/2263`, bidegree `(7,8)`, and
72/72 strict controls.  The old transverse coordinates themselves cannot be
repaired at `X=1` by changing only nonnegative `Z`; that scoped chart-family
no-go is not a gate counterexample.

The frozen v17 release also adds the independent all-scale predecessor box

```text
Z=1/8, |x-5/8|<=1/1000, |y|<=1/100,
0<h<=1, lambda>0,
```

for both signed lifts.  Its exact danger reserve is
`30189/62500`, `det(C)/h^2=5/72`, and all 531/531 trivariate Bernstein
controls are strictly positive.  The previously audited fixed ray and
`x=5/8` y-strip are nested predecessor certificates, not additional headline
theorems.

The v18 candidate upgrades the displayed local-box theorem by four
independently audited adjacent cells:

```text
313/500 <= x <= 627/1000,
627/1000 <= x <= 63/100,
63/100 <= x <= 16/25,
16/25 <= x <= 7/10.
```

Their exact union is

```text
Z=1/8, 313/500<=x<=7/10, |y|<=1/100,
0<h<=1, lambda>0, both signed-z lifts.
```

Every cell has `det(C)/S=5/72`, `531/531` strict trivariate Bernstein
controls, and a `71/71` exact parameter/Hermitian/raw-gate/control left seam.
The cell danger reserves are respectively `481771/1000000`, `239/500`,
`4653/10000`, and `3849/10000`.  On the final wide cell the unique weakest
control is `C1(0,2,2)=517/1000`.  This is a four-cell stitched theorem, not
one unchecked polynomial extrapolation.  The old narrow box is retained only
as its nested predecessor.

The grouped frozen evidence and exact SHA-256 index are under
`certificates/xy_box_post_v17/`; the package-local dependency layout is
mirrored under `certificate_workspace/`.  The v18 candidate is not
submission-ready until its reproducibility, bibliography, clean-build,
archive, visual, and independent final manuscript gates have passed.  Any
later submission also requires confirmation of the
author metadata and the selected venue's AI disclosure, acknowledgments,
funding, bibliography, source-format, and style requirements.

The paper does **not** claim either complete high-Z axis cap, the unrestricted
complex Hermitian gate, any extension of the stitched local box beyond
`x=7/10` or fixed `Z=1/8`, the full compact-ball theorem, a common metric for
arbitrary data, arbitrary nodes or dimension, or the optimal constant of a
fixed crossing lens.  Those problems remain open.

## Mathematical scope through the centered breakpoint and tilted chart

In the lossless compact-ball chart, the new theorem proves the original fully
conjugated Hermitian gate strictly positive on exactly

```text
0<S<=1, lambda>0, 0<=x<=1/8, |y|<=1/64,
Z=z^2=63/64-x^2,
```

for both signs of `z`.  The danger reserve is at least `63/4096`.  The source
certificate has `300/300` strictly positive coefficient controls.  The
projective full tensor has `1125` controls: `945` are positive and the other
`180` are exactly the artificial `S=0` closure zeros.  The independent
referee reconstructs the signed-`z` raw matrix and the Bernstein tensors by
exact rational collocation, without importing the source polynomial or its
control table.  Its manifest has SHA-256
`3637e39e601de8a6a1df3ed1c45877f23a5258030ac0706ff108228a7786820d`.

The center section `y=0` is the previously audited one-dimensional bridge
arc.  Because the new theorem includes every `|y|<=1/64`, it strictly
contains that arc.  It remains a two-real-dimensional surface family, not a
three-dimensional cap, full-ball, common-metric, or fixed-lens theorem.

Relative to frozen v6, the all-scale island enlarges `|t-4|<=13/239` to
`|t-4|<=50/919`, equivalently `3626/919<=t<=3726/919`, after recomputing all
seven derivative majorants on the complete wider interval.  All fourteen
cell/sign reserves are positive, and the freshly recomputed finite reserve
ratio is strictly larger than `50/919`; no larger half-width is claimed.
The centered positive-`Z` moving-sheet island enlarges `0<=X<=1/19` through
the exact closed X18--X5 chain and the X4 breakpoint cell.  Its original
gate is strictly positive on `0<=X<=X*`, where
`X*=428905727/1858957100`; uniform strict danger is exactly `0<=X<X*`.
At `X*` the gate remains positive and exactly one centered corner has zero
danger.  The endpoint is sharp only for uniform legality of this fixed
centered box.  In particular, `X=1/4` is nonlegal for the route and is not a
counterexample.  All endpoint changes have
separate exact source and cache-independent referee verifiers, fail-closed
optimized-Python tests, and manifests.  The moving sheet still crosses
`Z=1/8` without dividing by `Z-1/8`, and the X17 cell crosses the old
`Z=1/6` locator; every later centered cell continues beyond that obsolete locator.  The
lossless reduction actually requires only
`0<S<=1`, `lambda>0`, `Z>0`, and `x^2+y^2+Z<1`; the frozen chains through
X17 and all later source/referee pairs reconstruct the original gate and
their exact legality conditions directly.

The separate affine-`omega` tilted chart retains the same radii and scale
range but replaces the physical center by
`omega_phys=omega-(10636/275)(X-1/5)`.  Exact source and independent
signed-`z` referee reconstructions prove `48/48` strictly positive Bernstein
controls on `1/5<=X<=3/13`, both signs of `z`, and the uniform reserve
`D>=S/100>0`.  At `X=1/5` its center tilt is zero, giving an exact seam with
the centered chart.  The connected union has X-projection through `3/13`,
but it is neither a single sheet, a full positive-`Z` collar, nor a full
compact-ball/common-metric/fixed-lens theorem.  The `3/13` endpoint is a
scale-uniform legality boundary for this bounded affine-center class, not a
negative raw gate.

## Inward-Z theorem and v15 legality-frontier extension

The new sheet keeps the affine-`omega` center and uses

```text
0<S<=1/10000, 3/13<=X<=83059/100000,
|M|<=1/1000, |omega|,|nu|<=1/100,
Z=9/13-X^2+S*b-S^2*y0^2.
```

It meets the frozen affine sheet parameter by parameter at `X=3/13`, but its
`Z` formula differs away from the seam.  Exact legality gives `lambda>0`,
`0<Z<1`, strict danger, and rank two for both signs of `z`.  The continuum
certificate has bidegree `(7,4)`, 32 `(S,X)` coefficients, a 32-coefficient
core with 1,581 centered monomials, and Bernstein degree `(7,9)`.  Of the 80
controls, exactly `(0,0)`, `(0,1)`, and `(1,0)` vanish on the artificial
`S=0` closure; the other 77 are strictly positive.  The proof uses the exact
weight

```text
W(tau)=1-(1-tau)^7-7*tau*(1-tau)^6>0  for tau>0.
```

The 72 exact rational node evaluations are retained only as falsification
diagnostics.  No numerical minimum is used as a theorem, and no Lean or other
proof assistant covers this result.

The first adjacent cell `1/4<=X<=131/520` uses
`X=1/4+u/520`, `S=tau/10000` and has 40/40 strict bidegree-`(7,4)`
controls.  Its unique weakest control is `(0,0)`, with exact reserve

```text
987933779504207075207504779933987999
/7187610992640000000000000000.
```

The legality-frontier cell `131/520<=X<=83059/100000` also has 40/40
strict controls and unique weakest control `(0,0)`, with reserve

```text
119539987320009056100108078372012547879
/718761099264000000000000000000.
```

Exact full-cell bounds include
`Z>=160243869095653/15857127000000000000>0`,
`Z<=170039/270400<1`,
`D>=11/1300+(10931/13000)S>0`, and a strictly positive rank-two determinant
for both signed lifts.  A separately generated 40-control tensor is still
strict at `X=4153/5000`, but the same chart has
`Z_min=-103795949201927/15857127000000000000<0` there.  Thus the rational
root bracket records chart illegality only; no point outside the legal chart
is asserted to be a gate counterexample.

## Recentered-Z theorem through its exact danger root

The new sheet keeps all parameters and the affine-`omega` center from the
inward theorem, but replaces the squared signed coordinate by

```text
Z_rec = Z_in + 2(X-83059/100000).
```

At `X=83059/100000` the added term vanishes, so the parameters, positively
cleared raw gate, and cleared core splice exactly.  The independently audited
cells are

```text
[83059/100000,17/20], [17/20,7/8], [7/8,9/10],
[9/10,11/12], [11/12,15/16], [15/16,19/20],
[19/20,39/40], [39/40,1019767/1040000].
```

For every cell, source and no-import referee reconstruct the original fully
conjugated Hermitian `Q,Q^2` gate.  After the common positive clearing and
removal of the manifestly nonnegative layer, the certificate has exact
structure `34/34/1659`, bidegree `(7,4)`, and 40/40 strict centered rational
Bernstein lower controls with unique weakest index `(7,0)`.  The complete
eight reserves are printed in the paper appendix.  Each pair also proves the
three-level seam, complete `Z`/danger/`det(C)` legality, rank two, and both
signed lifts.  The 72 exact nodes per cell are diagnostics only.

Global exact bounds include

```text
Z >= 160243869095653/15857127000000000000,
Z <= 33258337711/1081600000000 < 1,
det(C) >= [160243869095653/28542828600000000000] S > 0.
```

At the terminal root, `danger_base=0` but
`T<=-4181417/143000`, hence `D=-S*T>0` for every `S>0`.
For every larger `X`, sufficiently small positive `S` makes this formula
illegal.  The archived source/reference pairs explicitly classify this as a
chart obstruction, not a negative gate or a maximality theorem.

## Constant-Z theorem through 99/100

The fifth compact-ball sheet freezes the squared signed coordinate at its
value on the recentered danger-root seam:

```text
Z_const = Z_in + 2(1019767/1040000-83059/100000),
1019767/1040000 <= X <= 99/100.
```

Definition-level source and independent referee reconstructions prove all
nine entries of `Q^2`, degree four in `Z`, positive reversible clearing,
the three seam layers, and exact structure `32/32/1581`.  All 40 Bernstein
lower controls are strictly positive.  The unique weakest reserve is

```text
336916849934297843831968152548875021542760484743285035401593929563252614799020866001627
/1047953682726912000000000000000000000000000000000000000000000000000000000000.
```

Full-cell bounds include

```text
Z >= 143889690210214873/15857127000000000000,
Z <= 33258337711/1081600000000 < 1,
dZ/dX <= -1019767/520000 < 0,
D >= (8425123367/286000000) S > 0,
det(C) >= [143889690210214873/28542828600000000000] S > 0.
```

The source manifest has 8/8 verified files; the referee manifest has 41/41.
Normal and byte-compiled runs pass, and all eight fail-closed attacks are
rejected at their intended exact gates.  No sampled value is used as proof,
and no Lean theorem is claimed.

## Build

With a current TeX Live installation:

```sh
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 latexmk -C main.tex
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The included `main.bbl` also permits a direct LaTeX build when BibTeX is not
available.

## Portable certificate policy and fresh replay

The first v18 candidate archive contained 277 historical generated `.log` or
`.txt` files under `certificate_workspace/` with a machine-specific user-home
path.  The repaired candidate intentionally omits exactly those 277 files.
They were execution transcripts or generated diagnostics, not source
code, coefficient data, theorem statements, or inputs read by the normal
mathematical gates.  No path string was rewritten or redacted in a retained
file.  The failed predecessor ZIP has SHA-256
`0e549206bb0d2a809fe650fe818d0023868f407322d7c50da10dcf2b7a91763e`
and is retained only as audit history, not as a passing portable archive.
See `certificates/PORTABILITY_NOTE.md` for the exact policy and replay limits.

All principal source and independent-referee programs, notes, human referee
reports, normal result summaries, and historical manifests remain byte-for-
byte unchanged.  In particular,
`certificates/xy_box_post_v17/INDEX.md` still binds the 32 principal files
(eight per cell) at 32/32 exact SHA-256 matches.  The historical manifests are
also retained as provenance, but this README deliberately does **not** claim
that a line-oriented `shasum -c` over every historical generated transcript
will pass: a manifest that lists one of the 277 omitted machine-path logs will
correctly report that record missing.

A later audit also identified 15 generated or old-audit files containing 16
absolute temporary-path occurrences.  Those non-input files are omitted
without rewriting.  The exact accounting is in the portability note.

Reconstruct a Python environment from
`certificate_workspace/requirements-portable.txt`.  From
`certificate_workspace/`, the four post-v17 source gates and four literal-
free independent referees can be run directly to generate fresh outputs in a
new environment:

```sh
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000_independent_referee.py
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x63_100_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x63_100_independent_referee.py
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x16_25_independent_referee.py
python3 -B -u tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_exact_gate.py
python3 -B -u tmp/research/audit/verify_compact_ball_uncovered_box_x5_8_xy_adjacent_x7_10_independent_referee.py
```

The referee programs reconstruct the fully conjugated Hermitian gate and
Bernstein controls without importing a source coefficient table.  Fresh
stdout/stderr should be written outside the package if a byte-stable archive
is desired.  These eight normal runs are the portable mathematical replay for
the newly stitched local-box theorem; they do not retroactively regenerate
or authenticate every historical attack transcript in the project.

For a fully manifest-bound replay, use the parallel
`certificates/xy_box_post_v17_portable/` layer.  It retains the old eight
manifests only as provenance anchors and binds fresh relative-path normal and
fail-closed outputs in new source/referee/cell manifests.  Its README lists
all twelve manifest hashes and the package-root replay interface.

The `certificates/` directory groups the principal theorem materials for
reading.  `certificate_workspace/` preserves the relative code and data
layout needed by the retained programs while deliberately excluding the 277
nonportable generated transcripts.  Historical final audits remain baseline
evidence for the byte versions they name; they are not represented as audits
of later candidate bytes.  The portable-chain v18 candidate still requires a
new independent submission audit before any formal promotion.

## Integrity

`RELEASE_MANIFEST.sha256` binds every distributed file other than itself.
The deterministic v18 candidate ZIP has one top-level directory named
`common_metric_three_positivity_islands_submission_2026-08-26-v18`.
Absolute paths, parent traversal, symbolic links, and Python/Lean environment
caches are rejected by the release verifier.
The path-dependent/time-dependent latexmk transients `main.fdb_latexmk`,
`main.fls`, and `main.log` are intentionally not archive members and are
ignored if a clean-build replay regenerates them.  The two complete candidate
build logs and the empty final compile-warning gate are retained under
`audits/`; `main.pdf`, `main.bbl`, `main.blg`, `main.aux`, and `main.out` stay
manifest-bound.
Despite its historical filename, it is a JSON manifest, not a line-oriented
`shasum` file.  From this directory run

```sh
python verify_release_manifest.py
python verify_release_manifest.py --zip ../common_metric_three_positivity_islands_submission_2026-08-26-v18.zip
```

to verify the complete file set, every byte count, and every SHA-256 record.
