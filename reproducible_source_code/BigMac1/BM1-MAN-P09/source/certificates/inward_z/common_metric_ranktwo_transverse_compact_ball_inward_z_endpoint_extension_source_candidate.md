# Inward-Z endpoint extension to `X=131/520`: exact source candidate

Date: 2026-08-25. Status: **exact source-level partial-theorem candidate,
pending a genuinely independent definition-level referee**.

This candidate extends the already audited inward-Z sheet only across the
new rational cell

```text
0<S<=1/10000,                1/4<=X<=131/520,
|M|<=1/1000,                |omega|,|nu|<=1/100,
A=1+M,                      lambda=A/S,
y0=12/(25A)+nu,
b=(45M+18)/(25A)-(3/5)X+omega-(10636/275)(X-1/5),
x=-1/5+X,                   y=3/5+S y0,
Z=9/13-X^2+S b-S^2 y0^2.
```

For both signed lifts `z=+-sqrt(Z)`, the source program reconstructs the
signed compact-ball Gram columns, the Hermitian `Q`, every entry of `Q^2`,
and the fully conjugated original scalar gate.  It imports no predecessor
coefficient or Bernstein table.  Clearing only the positive factor
`25^8 A^8 S^3` again gives 32 `(S,X)` coefficients of bidegree `(7,4)`.
After removing the manifestly nonnegative layer

```text
S^3 25^8 M^2 A^8 (5M^2+14M+14),
```

the core has 32 `(S,X)` coefficients and 1,581 centered
`(M,omega,nu)` monomials.

On the lossless new-cell map

```text
X=1/4+u/520,                 S=tau/10000,
0<=u,tau<=1,
```

the source independently regenerates a bidegree-`(7,4)` Bernstein tensor.
All 40 centered rational lower controls are strictly positive; there are no
closure-zero controls.  The unique weakest control is `(0,0)`, with exact
lower reserve

```text
987933779504207075207504779933987999
/7187610992640000000000000000.
```

It lies on `tau=0`, where its complete parameter polynomial is

```text
95367431640625 (M+1)^12 / 685464.
```

The complete `tau=0` row is strict.  Hence every Bernstein row is strict and
their total weight is exactly one; no artificial-boundary strictness repair
is needed on this new cell.  The old global-cell closure zeros do not persist
because that rectangle touched the left seam `X=3/13`, where the core at
`S=0` vanishes.  The new cell begins strictly to its right.  The source also
checks directly, before either Bernstein transform, that the frozen theorem's
cleared gate at `X=1/4` is identical term by term to the new cell at `u=0`.

At the new endpoint, exact monotone bounds give

```text
b_min = -7674229/5291000,
Z_min = 129601350803598453349/206142651000000000000,
danger >= 110013/13000000,
det(C) >=
129601350803598453349/3710567718000000000000000.
```

Thus the source candidate is strictly legal, strictly dangerous, rank two,
and raw-gate positive throughout the displayed continuum.  The alternative
counterexample outcome does not occur on this cell; no chart-legality failure
or merely sufficient-certificate failure is being relabeled as a gate result.

Run only with the project environment:

```text
.venv/bin/python tmp/research/compact_ball_inward_z_endpoint_extension.py
```

The verifier fails closed under optimized Python, a corrupted dependency
hash, or deletion of one exact core coefficient.  No sampled SDP, floating
sign decision, real-part monotonicity, fixed allocation, or route
CE-046/048/059/060 is used.  No proof assistant is used.

The claimed status remains a source candidate until a separate implementation
reconstructs the original gate, the 40 controls, the exact reserve, the
splice, and the legality bounds.  Even after such an audit, this would be a
small partial theorem only.  It does not prove the full compact-ball quartic,
the general common-metric gate, an arbitrary-node bridge, or the fixed
crossing-lens optimal constant.  It is not a paper or a submission package.
