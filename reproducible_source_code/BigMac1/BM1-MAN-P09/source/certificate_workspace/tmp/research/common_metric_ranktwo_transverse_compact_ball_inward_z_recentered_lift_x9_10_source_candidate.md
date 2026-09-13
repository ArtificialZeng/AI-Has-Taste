# Recentered inward-Z lift on the exact cell `7/8 <= X <= 9/10`

## Status and scope

This is a frozen **source candidate**, not yet an independently refereed
theorem.  It treats one closed rational cell only.  It does not prove the
full compact-ball quartic, the general complex common-metric gate, an
arbitrary-node or arbitrary-dimension theorem, or the optimal fixed-lens
constant.

The chart is the previously audited global recentering

```text
Xanchor = 83059/100000,
Z = Z_old + 2 (X-Xanchor),
7/8 <= X <= 9/10.
```

## Exact reconstruction and splice

The source hash-binds the independently audited preceding cell and its
source/referee manifests.  It then applies a fail-closed, multiplicity-checked
specialization to the preceding exact source.  Executing the specialized
body reconstructs the signed frame, original Hermitian `Q`, every entry of
`Q^2`, and the fully conjugated raw gate.  It does not use sampled SDP data.

At `X=7/8` it checks, exactly and parameter by parameter:

1. the affine chart inputs;
2. the cleared raw gate;
3. the cleared core after the positive denominator clearing.

The raw gate has exact degree four in `Z`.  The cleared/core structure is
`34/34/1659`, with `(S,X)` bidegree `(7,4)`.

## Exact positivity certificate

On the full closed cell, all 40 centered Bernstein lower controls are
strictly positive.  A weakest control index is `(7,0)`, with exact reserve

```text
42704141468472845006210554786732611015027482006353404809093913974854812201090200227
-------------------------------------------------------------------------------------.
239735779200073728000000000000000000000000000000000000000000000000000000
```

The complete weakest polynomial is emitted in the replay log.  The 72 exact
original-gate nodes are breaker diagnostics only; the continuous proof is
the exact 40-control tensor, not the node sample.

## Exact full-cell legality

The source proves both signs of `z` are legal on the whole cell, with

```text
Z >= 204722284502434873/15857127000000000000,
Z <= 13733/650000,
dZ/dX >= 539199/2750000,
T <= -723953/28600,
danger >= 83767/650000,
det(C) >= [204722284502434873/28542828600000000000] S > 0.
```

Thus the candidate is neither a chart-illegality result nor a legal
raw-gate counterexample.  It is a strict local positivity source candidate.

## Fail-closed and replay gates

Four attacks must fail nonzero:

- optimized Python (`-O`);
- predecessor dependency-hash corruption;
- sparse recentered-`Z` normalization corruption;
- deletion of one core coefficient.

Normal replay:

```sh
.venv/bin/python -u tmp/research/compact_ball_inward_z_recentered_lift_x9_10_exact_gate.py
```

Frozen-set verification:

```sh
shasum -a 256 -c tmp/research/compact_ball_inward_z_recentered_lift_x9_10_source_freeze_manifest.sha256
```

The next gate is an independent no-import referee that reconstructs the
mathematics from the original definitions and independently repeats splice,
legality, 40-control, weakest-polynomial, node, attack, and manifest checks.
