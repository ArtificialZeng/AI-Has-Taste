# Recentered inward-Z lift on the exact cell `9/10 <= X <= 11/12`

## Status and scope

This is a frozen **source candidate**, pending an independent no-import
referee.  It treats one closed rational cell only.  It does not settle the
full compact-ball quartic, the general complex common-metric gate,
arbitrary nodes or dimensions, or the optimal fixed-lens constant.

The chart is the previously audited global recentering

```text
Xanchor = 83059/100000,
Z = Z_old + 2 (X-Xanchor),
9/10 <= X <= 11/12.
```

## Reconstruction and three-layer splice

The source hash-binds the independently audited `X<=9/10` source and its
source/referee manifests.  A fail-closed, multiplicity-checked specialization
of the frozen self-contained builder reconstructs the signed frame, original
Hermitian `Q`, every entry of `Q^2`, and the fully conjugated raw gate.
No sampled SDP data enters the argument.

At `X=9/10`, the source exactly verifies the chart parameters, cleared raw
gate, and cleared core splice.  The raw gate has exact degree four in `Z`.
The cleared/core structure is `34/34/1659` with `(S,X)` bidegree `(7,4)`.

## Exact positivity certificate

All 40 centered Bernstein lower controls on the closed cell are strictly
positive.  A weakest control index is `(7,0)`, with exact reserve

```text
49676024530556199202731766735542701752522753368441481977751511650694115571509875227
-------------------------------------------------------------------------------------.
239735779200073728000000000000000000000000000000000000000000000000000000
```

The replay log prints the complete weakest polynomial.  The 72 exact
original-gate nodes are breaker diagnostics only; continuity is certified by
the exact 40-control tensor, not by node sampling.

## Exact full-cell legality

For both signs of `z`, the full cell obeys

```text
Z >= 292361598161734873/15857127000000000000,
Z <= 8842/365625,
dZ/dX >= 1342597/8250000,
T <= -1880089/71500,
danger >= 199301/1950000,
det(C) >= [292361598161734873/28542828600000000000] S > 0.
```

The result is therefore a strict local positivity source candidate, not a
chart obstruction and not a legal raw-gate counterexample.

## Replay and next gate

Normal replay:

```sh
.venv/bin/python -u tmp/research/compact_ball_inward_z_recentered_lift_x11_12_exact_gate.py
```

Frozen-set verification:

```sh
shasum -a 256 -c tmp/research/compact_ball_inward_z_recentered_lift_x11_12_source_freeze_manifest.sha256
```

The next gate is an independent no-import referee that reconstructs the
mathematics from original definitions and independently repeats the splice,
legality, exact controls, weakest polynomial/reserve, diagnostic, attack,
and manifest checks.
