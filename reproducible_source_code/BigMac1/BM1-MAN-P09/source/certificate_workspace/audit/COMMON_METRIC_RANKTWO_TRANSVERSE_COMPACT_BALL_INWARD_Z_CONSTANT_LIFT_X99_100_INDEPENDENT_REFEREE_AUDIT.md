# Independent referee audit: constant-Z cell to 99/100

## Verdict and scope

**PASS. Fatal 0, major 0, minor 0.**

The certified local statement is restricted to
`1019767/1040000 <= X <= 99/100`, `0<S<=1/10000`, the frozen
`M,omega,nu` box, and
`Z=Z_old+2(1019767/1040000-83059/100000)`. It is not a theorem for the
full compact ball, an unrestricted common metric, or arbitrary nodes.

## Independence

Candidate source, note, manifest and source-produced logs were used only as
opaque byte strings for SHA-256. The referee never imports, executes, parses,
or reads candidate coefficients, controls, specializations, weakest
polynomial, or helpers.

Starting from the original Hermitian `Q,Q^2` definitions, the referee uses
reversed signed-z Gram columns, q-then-z-then-h elimination, an independent
cyclic-vector raw-gate expansion, and a dense u-first Bernstein transform.

## Exact certificate

The literal-free scout and formal run agree exactly. They prove direct
compression equals the reversed Gram sum, all nine `Q^2` entries, literal
raw gate equality, `deg_Z=4`, positive reversible clearing,
`32/32/1581`, and bidegree `(7,4)`. The parameter, cleared gate and
cleared core splice exactly at `X*=1019767/1040000`.

All 40 Bernstein controls are strictly positive. The unique weakest control
is `(7,0)`, with reserve

```
336916849934297843831968152548875021542760484743285035401593929563252614799020866001627
/1047953682726912000000000000000000000000000000000000000000000000000000000000.
```

The full weakest polynomial is printed in the normal log. Exact monotonicity
gives `Z_X<=-1019767/520000<0` and
`Zmin=143889690210214873/15857127000000000000>0`. At the root the danger
base is zero and `D=-S*T`; the uniform bound
`T<=-8425123367/286000000<0` proves strict danger for every `S>0`.
The remaining det(C), both signed-z, scale and rank-two legality gates pass.

The 72 exact nodes are diagnostics only and play no role in Bernstein
positivity or legality proofs.

## Adversarial audit

Formal normal and py_compile exit zero. Eight serial attacks exit one at the
intended exact gates: optimized Python, bad source, bad predecessor, bad
source manifest, bad normalization, dropped Q^2, flipped danger sign, and
dropped core coefficient. The final attack is rejected at
`32 core coefficients`.

No numerical evidence is promoted to a theorem; no chart obstruction is
reported as a raw negative or maximality result; CE-046/048/059/060 are not
reused. No proof assistant was used.
