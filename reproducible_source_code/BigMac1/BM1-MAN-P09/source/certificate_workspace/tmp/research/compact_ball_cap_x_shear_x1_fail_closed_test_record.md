# Fail-closed record for the `X=1` cap x-shear source candidate

## Normal source

```text
source SHA256 = ebea939556a98c28a3d8f3114b15e8841cee5758236a9957f25bb8c69a1613fc
normal exit   = 0
```

The normal source passed the exact `Z`-only no-go, original `Q,Q^2`
reconstruction, `(x,y,Z,lambda)`/cleared-gate/cleared-core seam, full `X=1`
legality, 72/72 strict continuum controls with a unique weakest index, and
72/72 diagnostic nodes.

## Effective attacks

Every final attack exited nonzero:

1. `python -O` was rejected by the explicit `__debug__` gate.
2. Bad frozen-builder and bad audited-predecessor hashes were rejected before
   algebraic work.
3. `BAD_SPARSE_NORMALIZATION` was rejected by the independent sparse/direct
   `Z` identity.
4. `DROP_Q2` was rejected by the raw-gate quartic normalization.
5. `FLIP_DANGER` was rejected by the exact cap danger identity.
6. `DROP_CORE` was rejected by the complete core-coefficient-table check.

## Preserved implementation attempt

Before the final normal run, an implementation attempt stopped at the
`T`-monotonicity assertion because SymPy had not automatically cancelled
rational expressions such as `(M+1)/(M+1)`.  The gate was not removed.
Independent exact cancellation gave residuals `(0,0,0,0)` for

```text
dT/dM     = 63/[125(1+M)^2] > 0,
dT/domega = 1,
dT/dnu    = 6/5,
dT/dX     = -10801/275.
```

The final source checks these identities with explicit `cancel/factor` and
then passes.  The preserved pre-freeze attempt hashes are

```text
log  db7b357fbf9e8949ebcb2c162d541e7d8bb72bb436c01de40faff1cfcf6ec9c1
exit 4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865
```

This was an implementation-level normalization issue, not chart illegality,
Bernstein insufficiency, resource failure, or a legal raw-gate negative.
