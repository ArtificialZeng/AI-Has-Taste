# Exact moving-sheet extension to the strict-danger breakpoint

Date: 2026-08-24. Status: **exact computer-assisted partial theorem,
independently reconstructed from the original gate**. The theorem is
half-open only because strict danger has an exact geometric breakpoint.
The original gate certificate itself is strict on the closed interval through
that breakpoint. The full compact-ball quartic, unrestricted complex
Hermitian gate, common-metric theorem, and fixed crossing-lens constant remain
open.

## 1. Statement

Set

```text
Xstar = 428905727/1858957100.
```

Let

```text
0 < S <= 1/10000,
1/5 <= X < Xstar,
|M| <= 1/1000,
|omega|, |nu| <= 1/100.
```

Put `A=1+M` and use the same moving sheet

```text
lambda = A/S,
y0     = 12/(25A)+nu,
wc     = -3(5MX-15M+5X-6)/(25A),
Y      = S*y0,
W      = S*(wc+omega),
Z      = 3X-X^2-Y^2+W,
x      = -1/5+X,
y      = 3/5+Y.
```

For either real sign of `z` with `z^2=Z`, keep the transverse frame,
compression, and `Q=lambda H` of the frozen reduction. With
`a=1/sqrt(6)`, `c=sqrt(5/6)`, `p=(a,0,c)^T`, and `xi=Qp`, define

\[
\begin{aligned}
 \mathcal G(Q)={}&a^2|\xi_2|^2
 +\frac14\left|c\overline{\xi_1}+a\xi_3
       +i\{ac-(Q^2)_{31}\}\right|^2\\
 &+\frac14\left|c\overline{\xi_2}-i(Q^2)_{32}\right|^2
 -8a^2(\operatorname{Re}\xi_1)^2.
\end{aligned}
\]

Then `lambda>0`, `Q` is Hermitian PSD of rank two, the datum is strictly
dangerous, and

\[
                         \boxed{\mathcal G(Q)>0}.
\]

The exact verifier proves the stronger gate statement on the closure
`1/5<=X<=Xstar`; the excluded endpoint has one and only one zero-danger
parameter corner. Together with the predecessor cells, the strict-danger
moving-sheet theorem therefore holds on

```text
0 <= X < Xstar.
```

The quantifier remains `S>0`; `lambda=A/S` is undefined at `S=0`.

## 2. Definition-level reconstruction

The source verifier imports no discovery code, predecessor verifier, cached
quartic, or coefficient table. It reconstructs the transverse frame, signed
`z` Gram columns, kernel, Hermitian `Q,Q^2`, literal fully conjugated
gate, and a separately ordered three-component Gram-vector evaluator. It
checks

\[
                 \det C=\frac59SZ
\]

and exact equality of the two gate evaluations before substituting the moving
sheet.

The independent referee again starts from signed-`z` Gram columns, uses a
different component order, and constructs the moving quotient by direct
affine-power expansion rather than the source's sparse substitution. It
imports neither source/discovery code nor serialized polynomial data. The
discovery provenance is
`tmp/research/compact_ball_positive_z_moving_sheet_x4_maximal_open_discovery.py`
with SHA-256
`68a4882218be6441475b2aa3c8084f45c16aeac09af46a0a4a597b3bba71a8f9`;
neither proof program imports it.

## 3. Exact legality and the sharp uniform breakpoint

The moving identity gives

\[
 1-x^2-y^2-Z
 =\frac35-\frac{13}{5}X-SB,
\]

where the coupled coefficient is exactly

\[
 B=\frac65y_0+w_0-\frac35X
  =\frac95+\omega+\frac65\nu-\frac{63}{125A}-\frac35X.
\]

On the closed box through `Xstar`,

```text
A >= 999/1000 > 0,
y0 >= 46999/100100 > 0,
B >= 585533340809/515860595250 > 0.
```

The derivative identities are

\[
 \partial_A B=\frac{63}{125A^2}>0,\quad
 \partial_\omega B=1,\quad
 \partial_\nu B=\frac65,\quad
 \partial_X B=-\frac35,
\]

and

\[
 \partial_X(1-x^2-y^2-Z)=-\frac{13}{5}+\frac35S<0,
 \qquad
 \partial_S(1-x^2-y^2-Z)=-B<0.
\]

Consequently the uniform minimum is attained at

```text
S=1/10000, M=1/1000, omega=nu=1/100.
```

At that corner the danger is

\[
 -\frac{1858957100X-428905727}{715000000}.
\]

It is strictly positive exactly when `X<Xstar`, and is zero at `Xstar`.
All monotonicities are strict, so this is the unique equality corner. Thus
`Xstar` is the exact maximal endpoint for uniform strict danger in this
centered box.

Independently, the source proves

```text
14/25 < Z <=
220824455717308720521/345572149964041000000 < 1,
```

while the referee obtains the sharper upper bound

```text
Z <= 552049179533075241627/863930374910102500000 < 1.
```

Since `det C=(5/9)SZ>0`, the compression and `Q` have rank two. Both
signs of `z` are covered without division by `z).

## 4. Exact continuum certificate

With

```text
N=S^3*(36 Gamma),
D=25^8*(1+M)^8,
Qhat=D*N/S^2,
```

all clearing factors are positive and

```text
36 Gamma = Qhat/[25^8(1+M)^8*S].
```

Fresh substitution has 134 pre-map monomials. The quotient has twenty
`(S,X)` terms and bidegree `(5,4)`; its first layer is the manifestly
nonnegative

\[
 25^8M^2S(1+M)^8(5M^2+14M+14).
\]

Centered exact arithmetic gives the quadratic reserve

\[
 c_0=
 \frac{2564950982194530478444050838857341987999}
 {1274019840000000000000000000}>0.
\]

The lossless chart `S=sigma X` satisfies

```text
0 < sigma <= 1/2000.
```

The sixteen higher terms contain 947 centered parameter monomials. Their
total exact absolute contribution is

\[
 R_{\rm abs}=
 \frac{311837602694763856953654581992404505154268305263846785274456274343807875982376092575027407}
 {103541941206646325492097536439091200000000000000000000000000000000000000000000000}.
\]

Discarding the other positive quadratic terms still leaves

\[
 c_0-R_{\rm abs}=
 \frac{208146457517980767271040318929344719831500991336682480497608668045656192124017623907424972593}
 {103541941206646325492097536439091200000000000000000000000000000000000000000000000}>0.
\]

The source and independent direct-affine referee reproduce this rational
reserve exactly.

## 5. Seam, breakpoint, falsification, and the nonlegal quarter endpoint

Use the closed gate coordinate

```text
X = 1/5 + u*(Xstar-1/5),  0 <= u <= 1.
```

An exact grid uses three positive `S` values, `u=0,1/2,1`, and all eight
centered corners. It contains 71 strictly legal nodes and the unique
zero-danger boundary corner. Every original gate value is strictly positive.

At `S=1/10000`, `M=-1/1000`, and `omega=nu=-1/100`,

\[
 (36\Gamma)_{X=1/5}=
 \frac{213355344357890421512795094325969057679}
 {40000000000000000000000000000000000}>0,
\]

and

\[
 (36\Gamma)_{X=Xstar}=
 \frac{440192380473245412784529502413179004647222033560333676023602100187}
 {62036421210789424476671714120000000000000000000000000000000000}>0.
\]

At the unique boundary corner,

```text
36 Gamma =
31769777656530376672684788597449530147261943789366551863977
/4459366315900461674520000000000000000000000000000000000 > 0,

Z =
220819670985134517424899959
/345572149964041000000000000 > 0,

danger = 0,

det C =
220819670985134517424899959
/6220298699352738000000000000000 > 0.
```

The requested `X=1/4` endpoint is outside the uniform legal domain. At the
worst centered corner its exact danger is

\[
 -\frac{8958387}{178750000}<0.
\]

At the separately displayed negative corner the raw gate remains positive
but danger is also negative. Hence `X=1/4` is a strict chart/legality
obstruction, not a gate counterexample, and no counterexample is registered.

## 6. Scope

This is a five-real-parameter moving-sheet partial theorem. The endpoint
`Xstar` is sharp only for uniform strict danger on this fixed centered box;
no maximality of the raw gate sign is claimed. The result does not prove a
full positive-`Z` collar, arbitrary normalized scale, the compact-ball
quartic on the whole ball, the common-metric theorem, or the optimal fixed
crossing-lens constant. No CE-046/048/059/060 route, real-part monotonicity,
dropped phase, or numerical inference is used. No proof assistant was used.

