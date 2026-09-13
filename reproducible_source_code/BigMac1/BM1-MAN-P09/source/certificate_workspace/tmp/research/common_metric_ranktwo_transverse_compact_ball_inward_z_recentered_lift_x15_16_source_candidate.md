# Recentered inward-Z lift on the exact cell `11/12 <= X <= 15/16`

## Status and scope

This is a frozen **source candidate**, pending an independent no-import
referee.  It treats one closed rational cell only and does not settle the
full compact-ball quartic, the general complex common-metric gate,
arbitrary nodes or dimensions, or the optimal fixed-lens constant.

The chart is the previously audited global recentering

```text
Xanchor = 83059/100000,
Z = Z_old + 2 (X-Xanchor),
11/12 <= X <= 15/16.
```

## Original reconstruction and splice

The source hash-binds the independently audited `X<=11/12` source and its
source/referee manifests.  A fail-closed, multiplicity-checked specialization
of the frozen self-contained builder reconstructs the signed frame, original
Hermitian `Q`, all entries of `Q^2`, and the fully conjugated raw gate.
No numerical SDP evidence is used.

At `X=11/12` the source verifies the chart parameters, cleared raw gate, and
cleared core splice exactly.  The raw gate has degree four in `Z`; the
cleared/core structure is `34/34/1659` with bidegree `(7,4)` in `(S,X)`.

## Exact positivity certificate

All 40 centered Bernstein lower controls on the closed cell are strictly
positive.  A weakest index is `(7,0)`, with exact reserve

```text
164130585516459842755162401427385937241790749657112188185532058233551242392421285681
--------------------------------------------------------------------------------------.
719207337600221184000000000000000000000000000000000000000000000000000000
```

The complete weakest polynomial is preserved in the normal replay log.  The
72 exact original-gate nodes are breaker diagnostics only; the continuous
proof is supplied by the exact control tensor.

## Exact full-cell legality

For both signs of `z`, the complete cell satisfies

```text
Z >= 339775913517934873/15857127000000000000,
Z <= 283103/10400000,
dZ/dX >= 332949/2750000,
T <= -289034/10725,
danger >= 44767/650000,
det(C) >= [339775913517934873/28542828600000000000] S > 0.
```

Hence this is a strict local positivity source candidate, not chart
illegality and not a legal raw-gate counterexample.

## Replay and next gate

```sh
.venv/bin/python -u tmp/research/compact_ball_inward_z_recentered_lift_x15_16_exact_gate.py
shasum -a 256 -c tmp/research/compact_ball_inward_z_recentered_lift_x15_16_source_freeze_manifest.sha256
```

The next gate is an independent no-import referee that reconstructs the
original definitions and independently repeats splice, legality, controls,
weakest-polynomial, diagnostic, attack, and manifest checks.
