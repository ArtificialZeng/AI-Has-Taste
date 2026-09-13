# Fail-closed record for the constant-Z `X497/500` source candidate

## Frozen normal source

```text
source SHA256 = d38dba1bf18b5906765f217bd764edc974cad2821ee8630fc292cffa77994653
normal exit   = 0
```

The normal run passed the original `Q,Q^2` reconstruction, three seam layers,
full chart legality, 40/40 strict controls with a unique weakest control, and
72/72 diagnostic nodes.

## Final attacks

All final attacks exited nonzero:

1. `python -O` was rejected at the explicit `__debug__` gate.
2. A bad frozen builder hash and a bad predecessor hash were independently
   rejected before algebraic work.
3. `DROP_Q2` was rejected by the raw-gate quartic-normalization check.
4. A byte-bound normalization mutant changed the frozen builder's unique
   `denominator = 25*A` line to `denominator = 24*A`; it was rejected by the
   independent `sparse/direct y map` identity.
5. `FLIP_DANGER` was rejected by the exact danger identity.
6. `DROP_CORE` was rejected by the complete core-coefficient-table check.

The normalization mutant has SHA256

```text
45f9c01d313b05e9862a2518224a8ec42d1e90f2b892ce826b17a5ade7beefbb
```

and its standalone attack log has SHA256

```text
db8507948a876c674ed413e723cd721af0a2c3df7a12a989310a4b1003501233.
```

The final aggregate gate-layer log records both the frozen source SHA and
this mutant SHA, then records nonzero exits for `DROP_Q2`, the normalization
mutant, and `FLIP_DANGER`.

## Rejected test-design attempt

An initial environment variable named `BAD_NORMALIZATION` was discovered to
have no active hook and therefore exited zero.  That no-op was rejected as an
audit-design failure, not misreported as a passed attack, and is excluded from
the frozen final attack logs.  The byte-bound `25*A -> 24*A` mutant above is
the corrected effective normalization attack.  The mathematical source was
not changed, so the successful normal source and its SHA remain valid.

## Exit interpretation

Attack nonzero exits certify that the source fails closed when decisive
dependencies or proof layers are corrupted.  They are not mathematical
counterexamples and do not alter the exact theorem candidate's scope.
