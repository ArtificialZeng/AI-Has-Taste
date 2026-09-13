# Independent audit: moving-sheet `X18` closed cell

Date: 2026-08-24. Result: **PASS**, with scope restricted to the displayed
five-real-parameter moving sheet on `1/19<=X<=1/18`.

## Audited conclusion

For

```text
0<S<=1/10000,
1/19<=X<=1/18,
|M|<=1/1000,
|omega|,|nu|<=1/100,
```

the original fully conjugated Hermitian gate is strictly positive.  The
source exact legality checks give

```text
lambda>0,
56/361 < Z <= 13269177661/81081000000 < 1/6,
1-x^2-y^2-Z >= 759038557637/1666665000000 > 0,
det C=(5/9)SZ>0.
```

Thus the datum is strictly dangerous, the compression and `Q` have rank two,
both signs of `z` are covered, and both closed endpoints are included.  The
coordinate `u=342(X-1/19)` places `u=0` exactly on the audited predecessor
seam.

## Independent reconstruction

The source rebuilds the transverse frame, all entries of `Q,Q^2`, the literal
fully conjugated gate, and an independently ordered Gram-vector gate before
substitution.  It then creates the quotient through an exact sparse moving
map.

The referee imports neither source code, discovery code, cached polynomial,
nor coefficient table.  It independently reconstructs signed-`z` Gram
columns, uses a different Gram-vector component order, and forms the quotient
by direct affine-power substitution.  Both routes recover exactly

```text
20 quotient (S,X) terms,
16 higher terms,
947 centered (M,omega,nu) monomials,
sigma=S/X<=19/10000,
```

and the same strict continuum reserve

```text
201667044956072817740185576689797163779166123712095790085615190740639981
/100306130042880000000000000000000000000000000000000000000000 > 0.
```

The referee legality derivation uses a distinct, sharper endpoint envelope:

```text
Z <= 13268907391/81081000000 < 1/6,
danger reserve >= 759044113187/1666665000000 > 0.
```

The source and referee `Z_UPPER` values therefore intentionally differ; both
are exact valid upper bounds, and the theorem records the weaker source
bound.  This is not a transcription mismatch.

Both 72-node exact falsification grids are legal and positive.  The common
seam and endpoint diagnostics for `36 Gamma` are

```text
1941635149051525232795626443278240808984959
/5212840000000000000000000000000000000000,

16590441965844177687836029861184257679
/40000000000000000000000000000000000.
```

The continuum theorem rests on the rational reserve, not on the finite grid.

## Fail-closed results

Normal source and referee runs pass.  Both reject optimized Python and an
intentionally bad predecessor dependency hash.  Each also rejects an
intentionally deleted quotient term: the source fails the `16/947` count and
the referee fails the complete 20-term gate.  Both files pass `py_compile`.

For the v10 portable package, both the source verifier and independent referee
resolve the release-local `certificate_workspace` from `__file__` in their
two explicitly supported distributed layouts and reject every other layout.
Each resolves every dependency before hashing, requires it to remain inside
that packaged workspace, and therefore cannot fall back to a checkout or
host-specific absolute path.  This packaging repair does not alter the exact
formulas, reserves, or theorem scope above.

## Bound artifacts

```text
e6145a183c099e002bcee5c39ac03f098058dd56347532941bf8c0ddcf9a9d4d  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension.md
dc4d586680587a369478154b5273b43b55e598c5bdb5451578df3592c0cea29b  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension.py
d0d606581ce6cb95b4219d3c0090d3ef0cf07ff3ed138f7e38826449240463bf  tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x18_extension_independent_referee.py
cac9bdfdc7fddebfc31ff110bd77d5cfa79360e8fbc7a0ec3c9f04f90e5a9142  tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.md
```

## Scope

This is an exact adjacent-cell partial theorem.  It does not prove a full
positive-`Z` collar, arbitrary normalized scale, the compact-ball quartic on
the whole unit ball, the common-metric theorem, or the fixed-lens constant.
No maximality at `X=1/18` is asserted, and no proof assistant was used.
