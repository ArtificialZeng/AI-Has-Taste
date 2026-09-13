# Recentered inward-Z lift on the exact cell `19/20 <= X <= 39/40`

## Status and scope

This is a frozen **source candidate**, pending an independent no-import
referee.  It treats one closed rational cell only.  The full compact-ball
quartic, general complex common-metric gate, arbitrary-node/dimension
problems, and optimal fixed-lens constant remain open.

```text
Xanchor = 83059/100000,
Z = Z_old + 2 (X-Xanchor),
19/20 <= X <= 39/40.
```

## Exact reconstruction and splice

The source hash-binds and verifies the independently audited `X<=19/20`
source, source manifest, referee, report, and referee manifest.  A
fail-closed specialization of the frozen self-contained builder reconstructs
the original Hermitian `Q`, all of `Q^2`, and the fully conjugated raw gate.

At `X=19/20`, chart parameters, cleared raw gate, and cleared core splice
exactly.  The raw gate has degree four in `Z`; the cleared/core structure is
`34/34/1659` with `(S,X)` bidegree `(7,4)`.

## Exact positivity certificate

All 40 centered Bernstein lower controls are strict.  The source explicitly
checks that the weakest index is unique and equal to `(7,0)`, with reserve

```text
65753227483600516126610845662485171091398716929447176145929597779919072751981383227
-------------------------------------------------------------------------------------.
239735779200073728000000000000000000000000000000000000000000000000000000
```

The final normal log preserves the complete weakest polynomial.  The 72
exact original-gate nodes are breaker diagnostics only; the continuous proof
is the exact 40-control tensor.

## Full-cell legality

Both signed lifts of `z` are legal over the complete cell, with

```text
Z >= 408175999230334873/15857127000000000000,
Z <= 79307/2600000,
dZ/dX >= 126699/2750000,
T <= -91841/3250,
danger >= 5767/650000,
det(C) >= [408175999230334873/28542828600000000000] S > 0.
```

This is strict local positivity, not chart illegality and not a legal
raw-gate counterexample.

## Replay and next gate

```sh
.venv/bin/python -u tmp/research/compact_ball_inward_z_recentered_lift_x39_40_exact_gate.py
shasum -a 256 -c tmp/research/compact_ball_inward_z_recentered_lift_x39_40_source_freeze_manifest.sha256
```

The next gate is an independent no-import reconstruction of definitions,
splice, legality, 40 controls, unique weakest polynomial/reserve,
diagnostics, attacks, and manifest.
