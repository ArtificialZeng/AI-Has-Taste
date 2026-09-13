# Recentered inward-Z lift on the exact cell `15/16 <= X <= 19/20`

## Status and scope

This is a frozen **source candidate**, pending an independent no-import
referee.  It treats one closed rational cell only.  The full compact-ball
quartic, general complex common-metric gate, arbitrary-node/dimension
problems, and optimal fixed-lens constant remain open.

The chart is

```text
Xanchor = 83059/100000,
Z = Z_old + 2 (X-Xanchor),
15/16 <= X <= 19/20.
```

## Exact reconstruction and splice

The source hash-binds the independently audited `X<=15/16` source and its
source/referee manifests.  A fail-closed, multiplicity-checked specialization
of the frozen self-contained builder reconstructs the signed frame, original
Hermitian `Q`, every entry of `Q^2`, and the fully conjugated raw gate.

At `X=15/16` it verifies the chart parameters, cleared raw gate, and cleared
core splice exactly.  The raw gate has degree four in `Z`; the cleared/core
structure is `34/34/1659` with `(S,X)` bidegree `(7,4)`.

## Exact positivity certificate

All 40 centered Bernstein lower controls are strictly positive.  The unique
weakest index expected for independent audit is `(7,0)`, with source reserve

```text
15364004537485683830512016158976405126737501996882768005086777230415845013529148963
-------------------------------------------------------------------------------------.
59933944800018432000000000000000000000000000000000000000000000000000000
```

The final replay log preserves the complete weakest polynomial.  The 72
exact original-gate nodes are breaker diagnostics only; the continuum proof
is the exact 40-control tensor.

## Exact full-cell legality

For both signed lifts of `z`, the whole cell satisfies

```text
Z >= 386655427244434873/15857127000000000000,
Z <= 1163/40625,
dZ/dX >= 264199/2750000,
T <= -1588319/57200,
danger >= 31767/650000,
det(C) >= [386655427244434873/28542828600000000000] S > 0.
```

Thus the candidate is strict local positivity, not chart illegality and not
a legal raw-gate counterexample.

## Replay and next gate

```sh
.venv/bin/python -u tmp/research/compact_ball_inward_z_recentered_lift_x19_20_exact_gate.py
shasum -a 256 -c tmp/research/compact_ball_inward_z_recentered_lift_x19_20_source_freeze_manifest.sha256
```

The next gate is an independent no-import referee rebuilding the original
definitions and independently checking splice, legality, exact controls,
weakest polynomial/reserve and uniqueness, diagnostics, attacks, and the
frozen manifest.
