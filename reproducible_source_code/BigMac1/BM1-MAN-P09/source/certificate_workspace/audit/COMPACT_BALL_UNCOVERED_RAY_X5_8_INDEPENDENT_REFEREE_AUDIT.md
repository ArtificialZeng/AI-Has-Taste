# Independent referee audit: fixed compact-ball ray (5/8,0,1/8)

## Verdict and scope

**PASS. Fatal 0, major 0, minor 0.**

For the fixed shape

```
(x,y,Z)=(5/8,0,1/8),
```

the fully conjugated raw gate is strictly positive for every
`0<h<=1`, every `lambda>0`, and both signed-z lifts.  This proves one
fixed-shape ray only.  It is not a theorem for an open shape neighborhood,
the full compact ball, unrestricted common metrics, fixed crossing lenses,
or arbitrary nodes.

## Independence

The candidate source, source note, 21-entry source manifest, stitched-coverage
note, and coverage manifest were used only as opaque byte strings for SHA-256.
They were not imported, executed, parsed, or read for coefficients, formulas,
claims, controls, or expected answers.

The referee rebuilds the original frame and Hermitian compression using a
mixed-column-first signed Gram construction.  It eliminates radicals in the
order signed z, h, q, and independently multiplies `Q^2` in the index order
`(1,2,0)`.  Direct compression equals the Gram construction entry by entry;
all nine `Q^2` entries agree with direct matrix multiplication.  The literal
fully conjugated gate agrees with the independent vector form before any ray
specialization.

## Strict legality

The shape has exact danger reserve

```
1-x^2-y^2-Z = 31/64 > 0.
```

The original compression satisfies

```
det(C)/S = (5/9)Z = 5/72 > 0.
```

Together with `S=h^2>0`, this makes `C` positive definite.  The original two
frame vectors remain orthonormal through `S=1`, so the compression is rank
two.  Dependence on signed z cancels exactly, proving both lifts at once.

## Exact all-scale gate certificate

Writing the independently derived polynomial as

```
36 Gamma = c0 + c1 lambda + c2 lambda^2 + c3 lambda^3 + c4 lambda^4,
```

the five coefficients are

```
c0 = 5,
c1 = 85 S/96,
c2 = 215 S(21249 S+19037)/331776,
c3 = 5 S(2654208 S^2+8572032 S+4083977)/31850496,
c4 = S(987426091008 S^3+2214366284160 S^2
       +1677691247279 S+423511736838)/110075314176.
```

The literal-free scout factors the S-adic order of every coefficient and
converts each residual to its exact Bernstein basis on `[0,1]`.  The five
residual Bernstein tuples are

```
(5),
(85/96),
(4092955/331776, 4330745/165888),
(20419885/31850496, 41849965/31850496, 76551085/31850496),
(70585289473/18345885696,
 2948226457793/330225942528,
 427517749327/20639121408,
 5302995359285/110075314176).
```

Every entry is strictly positive.  Hence all five `c_j` are strictly positive
for `0<S<=1`; since `lambda>0`, the complete gate is strictly positive.

Nine exact rational diagnostics were run only after the symbolic proof.  Their
strictly positive minimum is not used as a theorem premise.

## Fail-closed and integrity audit

Scout, formal normal, and both `py_compile` runs exit zero.  Eight attacks
were actually run serially and exit one at their intended gates: optimized
Python, bad source, bad source manifest, bad coverage binding, dropped `Q^2`,
flipped danger, one corrupted derived coefficient, and one dropped legality
gate.

No numerical evidence is promoted to a theorem.  No CE-046/048/059/060 route
is reused.  No resource failure or legal negative was encountered, and no
proof assistant was used.
