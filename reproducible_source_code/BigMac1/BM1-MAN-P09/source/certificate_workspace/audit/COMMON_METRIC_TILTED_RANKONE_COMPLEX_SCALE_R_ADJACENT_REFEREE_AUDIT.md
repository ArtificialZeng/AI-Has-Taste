# Referee audit: adjacent complex scale `r` layer

Date: 2026-08-23.  Status: **PASS, exact isolated nodal audit**.

## Claim under audit

The proposed result fixes `a=3/5`, `c=4/5`, `t=4` and uses

```text
ell in [8,10],
w   in [-31/100,-29/100],
k   in [-301/100,-299/100],
z   in [-101/100,-99/100],
r   in [101/100,103/100],
```

with every legal scale on the strict `q_min>q_g` branch.  It claims strict
positivity of the original fully conjugated Hermitian gate, including the
finite closed endpoint on the positive-`g` branch.

## Isolation protocol

The referee is
`audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py
--adjacent-r`.  It imports neither discovery code nor the source verifier.
It reconstructs `Delta`, `n`, the rank-two Schur boundary, the danger scalar,
and the complete legal scale half-line from definitions.  It expands the
original gate in the real scale variable, checks that only even powers occur,
and derives the cubic independently.

For each of the eight certificate polynomials it evaluates the complete
exact rational nodal tensor, applies five exact Bernstein collocation
inversions, checks every recovered control, and reconstructs every original
node.  No tensor serialized by discovery or the source verifier is read; no
floating-point value or numerical interpolation is used.

The largest tensor is `ND`, degree `(10,20,10,20,12)`, with 693,693 nodes;
the total is 734,288 controls.

## Raw result

The following command exited with code zero:

```text
.venv/bin/python audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py --adjacent-r
```

Its complete raw semantic output was:

```text
PASS independent original-gate, danger, and legal-half-line reconstruction
PASS independent nodal reconstruction of 734288 Bernstein controls
PASS independent endpoint/derivative/discriminant sign audit
PASS independent exact phase-integrity r-boundary witness
r_bounds= (101/100, 103/100)
scope=six-real-parameter partial theorem; unrestricted gate remains open
```

The source command

```text
.venv/bin/python tmp/research/verify_common_metric_tilted_rankone_complex_scale_rbox_theorem.py --adjacent-r
```

also exited with code zero and independently printed its four required PASS
lines.  The finite breaker checked 243 rational shapes and 1458 legal scales
without finding an exact negative; that fact is discovery evidence only and
is not used in the proof.

The audit certifies only this adjacent local shape box and every legal scale.
The unrestricted complex Hermitian gate remains open.  No manuscript or PDF
package is authorized by this result.
