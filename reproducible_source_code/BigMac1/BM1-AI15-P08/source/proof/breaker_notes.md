# Breaker / certifier notes: low-degree self-inversive covering search

## Outcome of this branch

No robust numerical counterexample was found in degrees (2\) through (12).
The decisive exact result produced by this branch is a proof of the covering
inequality in degree (2).  It also implies the inequality for every even
degree on the infinite three-term support class \(\{0,n/2,n\}\); the endpoint
binomial class in odd degree maps the disk exactly to a disk.

The searches in degrees (3,4,5) are negative discovery evidence only.  They
are not finite exhaustive certificates and must not be quoted as proofs of
those degrees.

## Exact structural reduction used by the search

Multiplication by a scalar phase puts the self-inversive relation in the form

\[
 a_k=\overline{a_{n-k}}.
\]

Positive scaling then gives (A=1).  This loses no examples because both
(A) and the inradius scale by the same factor.  Thus the intrinsic free
parameters are

\[
\begin{array}{c|c}
n& (a_0,\ldots,a_n)\\ \hline
2&(\bar u,r,u),\quad r\in\mathbb R,\\
3&(\bar v,\bar u,u,v),\\
4&(\bar v,\bar u,r,u,v),\quad r\in\mathbb R,\\
5&(\bar w,\bar v,\bar u,u,v,w).
\end{array}
\]

The implementation samples these parameters directly and divides by their
largest modulus.  Hence the coefficient search class is the full normalized
self-inversive coefficient class, not a root-generated subclass.

For cubics there is a further complete quotient.  An input rotation followed
by the compensating output phase makes the endpoint pair real nonnegative.
After scaling, every cubic is represented by one of

\[
 (1,t e^{-i\phi},t e^{i\phi},1),\qquad
 (t,e^{-i\phi},e^{i\phi},t),
 \quad 0<t\le1,
\]

with the endpoint (t=0) included as a limiting stratum in the discovery
mesh.

## Exact degree-two theorem

**Proposition.** Every exact quadratic self-inversive polynomial (P)
satisfies

\[
 \rho(P(\mathbb D))\ge A(P).
\]

**Proof.** Output phase, input rotation with compensating output phase, and
precomposition by (z\mapsto-z), if needed, reduce without changing the
image up to a rotation to

\[
 P(z)=r(1+z^2)+s z,\qquad r>0,\ s\ge0.
\]

Translation by (-r) reduces the image question to

\[
 f(z)=rz^2+sz,\qquad A=\max(r,s).
\]

If (r\ge s), take any (|w|<r).  The product of the two roots of
(rz^2+sz-w=0) is (-w/r), of modulus less than one.  Therefore at least one
root lies in (mathbb D).  Hence (B(0,r)\subset f(\mathbb D)).

If (s\ge r), then for (z=e^{it}),

\[
 |f(z)-r|
 =|z(s+r(z-\bar z))|
 =|s+2ir\sin t|\ge s.
\]

Thus the connected disk (B(r,s)) avoids (f(\mathbb T)).  At its center,
the roots of (rz^2+sz-r=0) are real, have product (-1), and cannot both
have modulus one because that would force them to be (1,-1) and hence
(s=0), contradicting (s\ge r>0).  Exactly one root is in (mathbb D).
The number of roots in (mathbb D) is constant on every component of
\(\mathbb C\setminus f(\mathbb T)\), so every point of (B(r,s)) has a root
in (mathbb D).  Hence (B(r,s)\subset f(\mathbb D)).  In either case the
contained radius is (max(r,s)=A).  \(\square\)

**Infinite sparse corollary.** If (n=2m) and a self-inversive polynomial is
supported on \(\{0,m,2m\}\), then (P(z)=Q(z^m)) for a self-inversive
quadratic (Q).  Since (z^m(\mathbb D)=\mathbb D), the images are identical
and the proposition applies.  If (n) is odd and (P) is supported only on
\(\{0,n\}\), self-inversivity makes the endpoint moduli equal and
(P(\mathbb D)) is exactly a disk of radius (A).

## The two numerical image evaluators

For (w\notin P(\mathbb T)), the argument principle gives

\[
 N(w)=\#\{z\in\mathbb D:P(z)=w\}
      =\operatorname{wind}(P(\mathbb T),w),
\]

and (P(\mathbb D)=\{w:N(w)>0\}) away from the boundary.

1. **Winding-grid evaluator (G).** Sample (P(e^{it})), calculate signed
   scanline crossings on a rectangular grid, keep cells with positive
   winding, and apply an anisotropic Euclidean distance transform.  Its error
   is of order the pixel diagonal; in particular it systematically reports
   values slightly below one for some equality examples.

2. **Root/exposed-boundary evaluator (R).** At each sampled curve point,
   perturb in the two normal directions and independently count roots of
   (P(z)-w) in (mathbb D).  Retain an arc only when one adjacent side has
   root count zero.  Then maximize distance to the retained point cloud by
   differential evolution, rejecting centers whose root count is zero.
   A separate verifier reconstructs a bitmap by solving (P(z)-w) at every
   pixel and does not import the discovery implementation.

Neither evaluator supplies a rigorous upper or lower bound without an error
analysis.  They are discovery and cross-check tools only.

### Exposed-sheet numerical erratum

The first R runs used a normal displacement (2\cdot10^{-5}) times the curve
span.  Near (P(z)=a_0+a_nz^n), distinct image sheets can be much closer than
that displacement, and internal arcs were wrongly retained.  This created
spurious sub-unit values of order the small perturbing coefficients.  The raw
coefficients and G values remain valid; the old R fields are superseded by
the `breaker_refined_*_v2.json` artifacts using displacement
(2\cdot10^{-9}) times the span.  See
`experiments/breaker_evaluator_erratum.md`.

Even the v2 displacement cannot resolve sheets whose separation is itself at
or below double-precision scale.  Such points lie in the recorded numerical
neighborhood of the exact sparse subclass above and have no strict margin;
they are classified as unresolved equality-limit diagnostics, not as
counterexample candidates.

## Search coverage and results

Environment recorded in the JSON artifacts: CPython 3.13.5, NumPy 2.2.3,
SciPy 1.15.3, macOS arm64.  Coefficients, seeds, evaluator settings, centers,
mesh widths, normal displacements, and retained candidates are serialized.

### Degrees 2--5 random and structured search

- Seed `824681`: 2,000 samples per degree in each of five strata
  (`complex_gaussian`, `real_gaussian`, `log_uniform`, `unit_modulus`,
  `sparse`), hence 40,000 polynomials total.
- Seed `824682`: 750 samples per degree per stratum, hence 15,000 additional
  polynomials, retaining minima separately by stratum.
- Corrected R refinement at 8,192 boundary samples was applied to the leading
  candidates.  The smallest v2 values (rounding the displayed numerical
  output, not claiming bounds) were:

\[
\begin{array}{c|c|c}
n&\min G&\min R\text{ (v2)}\\ \hline
2&0.99233&1.000000001\\
3&1.00044&0.999999999\\
4&0.99369&1.000000029\\
5&1.00050&1.000000001
\end{array}
\]

The lone displayed cubic R value below one is smaller than one by
(8\cdot10^{-10}), comes from an inner coefficient of modulus
(7.5\cdot10^{-10}), and is below the evaluator's sheet-resolution scale.  It
has no certified or robust negative margin.  At nondegenerate per-stratum
minima, corrected R values were above one; for example the complex-Gaussian
minima for (n=3,4,5) were approximately (1.00563,1.09473,1.19003).

The independent 321-by-321 root-solve bitmap reconstructed the leading
candidate in each degree.  Its estimates were (0.99783,1.00000,0.99884,
1.00000), with respective pixel diagonals (0.01043,0.01025,0.01107,0.01025).
Thus all discrepancies from one are within the independently recorded mesh
uncertainty.

### Complete canonical cubic discovery mesh

The two cubic quotient strata above were sampled at 101 radial values and 180
phases, for 36,360 grid evaluations.  The global minimum occurred at the
near-binomial endpoint (t=10^{-6}).  Corrected 16,384-sample R refinement
gave approximately (1.000000498).  The smallest grid value on the
inner-pair-maximal stratum was (1.48639), and corrected R refinement gave
(1.50006).  This mesh is complete only as a parameter mesh, not as interval
coverage between mesh points.

### Exploratory degrees 6--12

Seed `912367` sampled 600 points per degree in each of the same five strata,
21,000 additional polynomials.  Corrected R estimates of the global retained
minima for degrees (6,7,8,9,10,11,12) were respectively

\[
1.00161,\ 1.000019,\ 1.0000004,\ 1.0000039,\ 1.00020,\
1.000031,\ 1.000045.
\]

These are exploratory only and do not establish a finite theorem.

## Reproduction

```bash
python tests/breaker_test_search.py

python src/search_self_inversive.py \
  --min-degree 2 --max-degree 5 --samples-per-mode 2000 \
  --grid-size 97 --boundary-samples 768 --retain 15 --refine 4 \
  --refine-boundary-samples 4096 --optimizer-iterations 260 \
  --seed 824681 --output experiments/breaker_search_seed824681.json

python src/search_refine_candidates.py \
  experiments/breaker_search_seed824681.json \
  --output experiments/breaker_refined_seed824681_v2.json \
  --global-per-degree 5 --per-mode 0 --boundary-samples 8192 \
  --optimizer-iterations 300 --seed 638327

python src/search_n3_canonical_mesh.py \
  --radial-steps 101 --phase-steps 180 --grid-size 81 \
  --boundary-samples 768 --retain 24 \
  --output experiments/breaker_n3_mesh_101x180.json

python src/verify_breaker_search.py \
  experiments/breaker_search_seed824681.json \
  --grid-size 321 --records-per-degree 1
```

## Hashes of principal artifacts

- `breaker_search_seed824681.json`:
  `0ccc2884b436fe2484551bdb697a208a64264922cf658635fe36cecb5225a64b`
- `breaker_refined_seed824681_v2.json`:
  `1a0f77895b96e4210acf9e33be4f3293064a2795439b2b9e95386390378d3828`
- `breaker_refined_by_stratum_seed824682_v2.json`:
  `37bced2939b4fdb2948fc0ba77eaee19f8319dcc9d1be9dc21047b34903a4a85`
- `breaker_n3_mesh_101x180.json`:
  `47db656f1185faba8d1ec00db2b7eb4a5c238df06d3efaac821f19e04329417e`
- `breaker_refined_n3_mesh_v2.json`:
  `b3041e68307e88dc1409ecb6a6c8654d13b080b0e84c63d59e91af96230bb130`
- independent 321-grid verifier output:
  `62f6b11b1ea3cb7966b986b017df9ff11a3231718f1d32298276f36263045725`
- degree 6--12 exploratory artifact:
  `81aeea0acae00f85374c40ab4ba1f96faf27d3cec135e739ae727e235d712f77`

No proof assistant was used in this branch.
