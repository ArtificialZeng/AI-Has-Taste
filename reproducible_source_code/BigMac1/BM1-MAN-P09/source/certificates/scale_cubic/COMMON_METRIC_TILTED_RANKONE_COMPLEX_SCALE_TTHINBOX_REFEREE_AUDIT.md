# Referee audit: derivative-certified complex scale `t` layer

Date: 2026-08-23.  Status: **PASS, exact isolated derivative audit**.

## Claim under audit

The candidate fixes `a=3/5`, `c=4/5` and retains

```text
ell in [8,10],
w   in [-31/100,-29/100],
k   in [-301/100,-299/100],
z   in [-101/100,-99/100],
r   in [99/100,103/100],
t   in [1999/500,2001/500],
```

together with every legal coupling scale.  The `r` interval is the union of
the two independently audited `t=4` center cells.  The new proof is the exact
mean-value estimate `p(t)>=m-|t-4| sup|partial_t p|` for all eight sign
polynomials controlling danger, PSD/Schur feasibility, the coefficient
branch, and the endpoint/derivative/discriminant branch.

## Audit isolation

The isolated referee
`audit/verify_common_metric_tilted_rankone_complex_scale_tthinbox_referee.py`
imports no source or discovery module.  It binds the two existing center
theorems, their common source/referee, and both audit notes by SHA-256; checks
that every exact center minimum occurs literally in the corresponding hashed
theorem note; extracts the even scale cubic from the original fully
conjugated gate; reconstructs the branch and discriminant; and independently
builds the exact power-coefficient majorants for all eight `t` derivatives.

The derivative majorants use the wider box `399/100<=t<=401/100`; exact
inclusion of the target box is asserted.  No six-axis Bernstein tensor is
constructed.  In particular, the forbidden direct `ND` tensor would have
9,711,702 controls.

## Raw output

Both commands exited with code zero:

```text
.venv/bin/python tmp/research/verify_common_metric_tilted_rankone_complex_scale_tthinbox_theorem.py
.venv/bin/python audit/verify_common_metric_tilted_rankone_complex_scale_tthinbox_referee.py
```

The source output was:

```text
PASS audited t=4 center dependencies and exact minima binding
PASS original Hermitian gate, rank-two PSD, and complete legal half-line
PASS eight exact center-margin/t-derivative reserves on t=[1999/500,2001/500]
PASS exact nonredundancy and phase-integrity witness
scope=derivative-certified thin t partial theorem; unrestricted gate open
```

The isolated output was:

```text
PASS isolated audited-center dependency hashes and minima binding
PASS isolated original-gate, PSD, cubic, and legal-half-line reconstruction
PASS isolated eight-polynomial derivative majorants and exact reserves
PASS isolated nonredundancy and phase-integrity witness
scope=thin t partial theorem depending on audited center boxes; unrestricted gate open
```

The initial derivative-certificate attempt at half-width `1/100` failed by
strictly negative ND reserves.  That was a certificate failure, not a gate
counterexample.  The certified half-width is `1/500`.  No direct
9,711,702-control ND tensor, floating-point interpolation, or cached control
tensor was used.

This audit promotes only a thin local active-block chart.  The unrestricted
complex Hermitian gate remains open, and no manuscript or PDF package is
authorized.
