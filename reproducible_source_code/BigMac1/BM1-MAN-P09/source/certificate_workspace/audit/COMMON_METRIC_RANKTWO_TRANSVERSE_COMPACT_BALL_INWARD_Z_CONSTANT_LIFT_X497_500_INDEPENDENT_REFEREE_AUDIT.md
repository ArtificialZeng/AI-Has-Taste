# Independent referee audit: constant-Z cell to 497/500

## Verdict and scope

**PASS. Fatal 0, major 0, minor 0.**

The certified local statement is restricted to
`99/100 <= X <= 497/500`, `0<S<=1/10000`, the frozen
`M,omega,nu` box, and
`Z=Z_old+2(1019767/1040000-83059/100000)`.  It is not a theorem for the
full compact ball, an unrestricted common metric, fixed crossing lenses, or
arbitrary nodes.

## Independence

The current candidate source and source-manifest files were used only as
opaque byte strings for SHA-256.  The referee never imported, executed, or
parsed them and never read their specialization, coefficient table, controls,
helpers, weakest index, weakest polynomial, reserve, source note, or source
normal log.

The referee instead begins at the original compact-ball Hermitian definitions.
It uses reversed signed-z Gram columns, the elimination order `q,z,h`, an
explicit cyclic `Q^2` multiplication order, a cyclic-vector raw-gate
cross-check, and a dense `u`-first Bernstein conversion.  The literal-free
scout contains no frozen weakest index, polynomial, or reserve.  Those data
were frozen only after the scout completed successfully and were then
rederived by the formal run.

## Exact certificate

The literal-free scout and formal normal run both exit zero.  They prove
direct compression equals the reversed Gram construction, all nine `Q^2`
entries, equality of the fully conjugated raw gate and the cyclic-vector gate,
radical cancellation, `deg_Z=4`, positive reversible clearing,
`32/32/1581`, and bidegree `(7,4)`.  The parameter, cleared-gate, and
cleared-core expressions splice exactly at `X=99/100`.

All 40 exact Bernstein controls are strictly positive.  The unique weakest
control is `(7,0)`, with reserve

```
237983128275106868164816372024450404725835762778737426332055936856452553581744586321
/719207337600221184000000000000000000000000000000000000000000000000000000.
```

The complete weakest polynomial is printed in both exact logs, and its frozen
text SHA-256 is
`7135ba124304e7fa5688e925f44f698b052919a1aab86af36073dabe15d68f7b`.

Full-cell legality is exact: `Z_X<=-99/50<0`,
`Zmin=17798406223702873/15857127000000000000>0`,
`Zupper=31507/2600000`, `T<=-5332081/178750<0`, and the left-end danger
base is `9833/2600000>0`.  The determinant, both signed-z branches, positive
scale, and rank-two gates also pass.  The 72 exact nodes are diagnostics only
and play no role in the positivity or legality proof.

## Endpoint preflight and claim discipline

At `X=1` the recentered-chart danger base is
`-20233/650000`, and an exact legal-box sample has chart danger
`-555866869/17875000000`.  The referee records this solely as illegality of
the recentered chart at that endpoint.  It is not a negative raw gate, a
maximality theorem, a full-ball obstruction, or a common-metric
counterexample.

No numerical evidence is promoted to a theorem.  No CE-046/048/059/060 route
is reused.  The conclusion is exactly one local constant-Z cell and nothing
more.

## Fail-closed audit

The formal normal run and `py_compile` exit zero.  Eight attacks were actually
run serially from clean invocations and each exits one at the intended exact
gate:

1. optimized Python: `optimized Python is forbidden`;
2. bad source: `frozen candidate source SHA-256`;
3. bad source manifest: `frozen source-manifest SHA-256`;
4. bad predecessor: `frozen predecessor-referee SHA-256`;
5. bad normalization: `claimed constant-Z sparse normalization`;
6. dropped `Q^2` term: `literal fully conjugated gate equals cyclic vector gate`;
7. flipped danger sign: `constant-Z danger identity with correct sign`;
8. dropped core term: `32 core coefficients`.

No proof assistant was used.  The independent exact computation, its atomic
logs and exit records, this report, and their SHA-256 manifest are the audit
boundary.
