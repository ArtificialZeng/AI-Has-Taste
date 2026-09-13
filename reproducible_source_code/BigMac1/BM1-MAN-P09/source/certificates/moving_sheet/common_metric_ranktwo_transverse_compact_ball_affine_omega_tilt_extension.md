# Exact affine-omega tilted moving-sheet theorem

Date: 2026-08-24. Status: exact local theorem candidate, pending root replay
and ledger synchronization. This note does not edit or widen any manuscript
claim.

## Statement

Let

```text
0<S<=1/10000,
1/5<=X<=3/13,
|M|<=1/1000,
|omega|<=1/100,
|nu|<=1/100,
A=1+M,
lambda=A/S.
```

Use the same lossless compact-ball map as the centered moving sheet, but
replace the physical omega parameter by

\[
 \omega_{\rm phys}=\omega-\frac{10636}{275}
 \left(X-\frac15\right).
\]

Equivalently, with

\[
 y_0=\frac{12}{25A}+\nu,
 \qquad
 b=\frac{45M+18}{25A}-\frac35X+\omega_{\rm phys},
\]

set

\[
 x=-\frac15+X,\qquad y=\frac35+Sy_0,\qquad
 Z=3X-X^2+Sb-S^2y_0^2.
\]

For every parameter in this closed box, for both real lifts
`z=+sqrt(Z)` and `z=-sqrt(Z)`, the fully conjugated original Hermitian gate
is strictly positive. Moreover

\[
 \lambda>0,\qquad 0<Z<1,\qquad
 1-x^2-y^2-Z\ge \frac{S}{100}>0,
\]

and the compression is positive definite of rank two because
`det C=(5/9)SZ>0`.

At `X=1/5` the tilted center is zero, so this chart has an exact seam with
the old centered sheet. The interval therefore begins inside the already
audited range `0<=X<X_*`, where

\[
 X_*=\frac{428905727}{1858957100}>\frac15.
\]

This theorem concerns the new tilted five-real-parameter slice; it is not a
monotone extrapolation of the centered theorem.

## Original gate and quotient

The source verifier reconstructs the normalized complex frame, the signed-`z`
Gram compression, `H=UCU^*`, `Q=lambda H`, and `Q^2`. It evaluates the literal
fully conjugated gate and independently checks the componentwise Gram-vector
gate before introducing the moving map.

After substituting `lambda=A/S`, the tilted map, and multiplying by the
strictly positive clearing factor `25^8 A^8 S`, the original gate becomes an
exact rational quotient with

```text
134 pre-map terms,
22 (S,X) quotient terms,
18 higher-order terms,
1013 centered (M,omega,nu) monomials.
```

One term is the manifestly nonnegative first layer

\[
 25^8 M^2S A^8(5M^2+14M+14),
\]

where

\[
 5M^2+14M+14=5\left(M+\frac75\right)^2+\frac{21}{5}>0.
\]

## Exact continuum certificate

The substitution

\[
 X=\frac15+\frac{2}{65}u,\qquad
 S=\frac{1}{2000}\tau X,qquad 0\le u,\tau\le1,
\]

is lossless up to a harmless enlargement, because

\[
 \frac{S}{X}\le\frac{1/10000}{1/5}=\frac1{2000}.
\]

Remove only the nonnegative first layer. The remaining exact polynomial has
bidegree `(5,7)` in `(tau,u)`. Its tensor Bernstein expansion has 48 controls.
For each control, exact centered arithmetic lower-bounds all
`(M,omega,nu)` variation on the unchanged radii. All 48 lower controls are
strictly positive. The common source/referee minimum is control `(0,0)`:

\[
 R_*=
 \frac{2564950982194530478444050838857341987999}
 {31850496000000000000000000000}>0.
\]

Bernstein basis functions are nonnegative on the unit square and sum to one,
so the remaining quotient is at least `R_*`. Adding the nonnegative first
layer and dividing by the positive clearing factor proves strict positivity
of the original gate on the whole closed tilted box. The older one-shot
termwise absolute remainder is negative here; that was only a failed
sufficient bound, not a negative gate value.

## Exact legality and the endpoint obstruction

The verifier obtains the uniform exact bounds

\[
 Z\ge
 \frac{8879008598718934873}{15857127000000000000}>0,
 \qquad
 Z\le\frac{8316795197}{13013000000}<1.
\]

Writing

\[
 T=\frac65y_0+b
 =\frac95+\omega+\frac65\nu-\frac{63}{125A}
 -\frac35X-\frac{10636}{275}\left(X-\frac15\right),
\]

the danger is

\[
 D=1-x^2-y^2-Z=\frac35-\frac{13}{5}X-ST.
\]

`T` increases in `M,omega,nu` and decreases in `X`. Its centered-box maximum
at the right endpoint is exactly

\[
 T_{\max}(3/13)=-\frac1{100}.
\]

For `T+1/100<=0`, one immediately has `D-S/100>=0`. Otherwise the worst
positive scale is `S=1/10000`, and exact simplification gives

\[
 D-\frac{S}{100}\ge
 -\frac{7139199(13X-3)}{35750000}\ge0.
\]

Thus `D>=S/100>0` on the entire closed interval; equality in the lower bound
is attained at the right endpoint and the maximal centered corner.

The same exact formula shows why this bounded, `S`-independent affine-center
class cannot extend beyond `3/13` while remaining strictly dangerous at every
positive scale:

\[
 \lim_{S\to0+}D=\frac35-\frac{13}{5}X<0
 \quad(X>3/13).
\]

In particular, `X=1/4` is a nonlegal route boundary, not a gate
counterexample.

## Endpoints and falsification

Both exact implementations check 72 rational nodes: three positive scales,
the seam/midpoint/endpoint, and all eight centered corners. All 72 are legal
and gate-positive. The seam and right endpoint diagnostics agree exactly:

\[
 36\Gamma\big|_{X=1/5}=
 \frac{213355344357890421512795094325969057679}
 {40000000000000000000000000000000000}>0,
\]

\[
 36\Gamma\big|_{X=3/13}=
 \frac{184421770823082033734271204948812328298851568079}
 {16726464040000000000000000000000000000000000}>0
\]

at the shared negative centered corner. At the endpoint worst-danger corner,

```text
36 Gamma =
2875017794276661652931485545294665330527919
/262440000000000000000000000000000000000,

Z = 640272135596701999/1002001000000000000,
danger = 1/1000000,
det C = 640272135596701999/18036018000000000000000.
```

The 72 nodes are falsification tests only; the 48 strict Bernstein controls
are the continuum proof.

## Independent audit and scope

The independent referee imports no discovery/source module or cached
coefficient table. It begins from signed-`z` Gram columns, uses a different
component order for the Gram gate, substitutes the affine sheet directly,
and performs a dense tau-first then `u` Bernstein transform. It reproduces
the source's counts, all 48 controls' positivity, decisive reserve, exact
legality bounds, seam/endpoint values, and 72 nodes.

Normal source/referee runs pass. Each separately rejects optimized Python, a
bad dependency hash, and a deleted quotient term; both pass external-cache
`py_compile`. Direct source-freeze, theorem, and referee manifests are
provided.

This is a strict theorem only for the stated tilted moving sheet. It does not
settle the full compact ball, construct a common metric, solve the fixed-lens
problem, prove maximal gate-sign range, or cover `X>3/13`. It uses no sampled
SDP, real-part monotonicity, dropped phase, or CE-046/048/059/060 route. No
proof assistant was used.
