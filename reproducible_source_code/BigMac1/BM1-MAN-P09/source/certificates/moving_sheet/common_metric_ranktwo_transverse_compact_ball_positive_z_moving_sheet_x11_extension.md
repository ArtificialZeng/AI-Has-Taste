# Exact moving-sheet extension on the closed cell `1/12 <= X <= 1/11`

Date: 2026-08-24.  Status: **exact computer-assisted partial theorem,
independently reconstructed from the original gate**.  Source/referee normal
replays, all six fail-closed attacks, compilation, and the direct source
manifest pass.  The full compact-ball
quartic, unrestricted complex Hermitian gate, common-metric theorem, and fixed
crossing-lens constant remain open.

## 1. Statement

Let

```text
0 < S <= 1/10000,
1/12 <= X <= 1/11,
|M| <= 1/1000,
|omega|, |nu| <= 1/100.
```

Put `A=1+M` and use the same audited moving sheet

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

The closed-cell coordinate is

```text
u = 132(X-1/12),       0 <= u <= 1,
X = (11+u)/132.
```

Thus `u=0` is exactly the independently audited predecessor endpoint
`X=1/12`; no continuity or limiting argument is used at the seam.

For either real sign of `z` with `z^2=Z`, keep the transverse frame,
compression, and `Q=lambda H` from the predecessor.  With
`a=1/sqrt(6)`, `c=sqrt(5/6)`, `p=(a,0,c)^T`, and `xi=Qp`, define the
fully conjugated original scalar gate

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

Both signs of `z` are covered because the compression and hence `Q,Q^2` use
`z` only through `z^2=Z`.  Both `X` endpoints are included.  Together with
the predecessor cells, this extends the same moving-sheet theorem to
`0<=X<=1/11`.  The quantifier remains `S>0`; `lambda=A/S` is undefined at
`S=0`.

## 2. Definition-level reconstruction

The source verifier reconstructs the transverse frame and checks its Gram
matrix, kernel, Hermitian symmetry, and

\[
                         \det C=\frac59SZ.
\]

It builds all entries of `Q` and `Q^2`, evaluates the displayed literal gate,
and independently evaluates a three-component Gram-vector expression.  The
two expressions are checked coefficient by coefficient before the moving
sheet is substituted.  Elimination of `q^2=1-h^2`, `z^2=Z`, and `h^2=S`
leaves the rational quartic `36 Gamma`, whose scale-constant coefficient is
five.

The referee imports neither source code, discovery code, cached quartics, nor
coefficient tables.  It uses signed-`z` Gram columns, a different component
ordering, and a direct affine-power quotient rather than the source sparse
substitution.

## 3. Exact legality

On the full closed box,

```text
A >= 999/1000 > 0,
y0 >= 46999/100100 > 0,
wc+omega >= 26633/40700,
wc+omega-S*y0^2 >= 79816166564221/121977900000000 > 0.
```

Monotonic endpoint bounds give

\[
 Z>3/12-1/12^2=\frac{35}{144}>0,
 \qquad
 Z\le\frac{2912804991}{11011000000}<1.
\]

The moving-sheet identity

\[
 x^2+y^2+Z=\frac25+\frac{13}{5}X+\frac65Y+W
\]

gives the strict danger reserve

\[
 1-x^2-y^2-Z\ge
 \frac{201946685879}{555555000000}>0.
\]

Finally `det C=(5/9)SZ>0`, so the compression and `Q` have rank two.  The
legality proof is independent of the gate estimate and never divides by a
chart-boundary expression.

### Why lying beyond `Z=1/6` is legal

This cell lies strictly beyond the predecessor’s convenient locator `Z=1/6`.
Already at the left seam `X=1/12` and in the `S -> 0+` base,

```text
3/12-1/12^2-1/6 = 11/144 > 0.
```

The lossless compact-ball reduction and both of its exact verifiers were
searched definition by definition.  Its actual nonplanar chart hypotheses
are precisely

```text
0 < S=h^2 <= 1,       lambda>0,
Z=z^2>0,              x^2+y^2+Z<1.
```

They imply a real frame (`q^2=1-S`), a positive rank-two compression, and
strict danger.  No lemma, inverse map, determinant identity, gate identity,
or denominator clearing in that reduction assumes `Z<1/6`.  The occurrences
of `Z<1/6` in the `X19`, `X18`, `X17`, `X16`, `X15`, `X14`, `X13`, and `X12` artifacts are endpoint descriptions only.
On the present box the source additionally checks

```text
A >= 999/1000>0,      S>0,      X>=1/12>0,
25^8*A^8*S>0,
```

so every division used by `lambda=A/S`, `sigma=S/X`, and the quotient is by
a strictly positive quantity.  Neither sign of `z` is divided out.

## 4. Exact continuum certificate

Set

```text
N=S^3*(36 Gamma),
D=25^8*(1+M)^8,
Qhat=D*N/S^2.
```

All clearing factors are positive, and

```text
36 Gamma = Qhat/[25^8(1+M)^8*S].
```

Fresh substitution into the original quartic produces 134 pre-map
monomials.  After exact division by `S^2`, `Qhat` has twenty `(S,X)` terms
and bidegree `(5,4)`.  Its first layer is the manifestly nonnegative term

\[
 25^8M^2S(1+M)^8(5M^2+14M+14).
\]

For the quadratic core, centered exact arithmetic proves the three
coefficients positive and gives

\[
 c_2\ge c_0=
 \frac{2564950982194530478444050838857341987999}
 {1274019840000000000000000000}>0.
\]

On this cell the lossless projective order is

```text
S=sigma X,       0<sigma<=3/2500.
```

After division by positive `X^2`, the sixteen higher terms contain 947
centered parameter monomials.  Their total exact absolute contribution is at
most

\[
 R_{\rm abs}=
 \frac{214438762584285777659078329177092477335578089311319635037488339}
 {75271680000000000000000000000000000000000000000000000}.
\]

Discarding additional positive quadratic terms still leaves the strict
reserve

\[
 c_0-R_{\rm abs}=
 \frac{151328075322151157528849784708781101149558464879438680364962511661}
 {75271680000000000000000000000000000000000000000000000}>0.
\]

This is a continuum certificate for the original gate, not a finite sample
or a surrogate inequality.

## 5. Falsification, seams, and independent bounds

An exact grid uses three positive `S` values, `u=0,1/2,1`, and all eight
corners of `(M,omega,nu)`, giving 72 legal rational nodes.  No exact negative
original gate occurs.  At

```text
S=1/10000, M=-1/1000, omega=nu=-1/100,
```

the seam and right endpoint have

\[
 (36\Gamma)_{X=1/12}=
 \frac{37195712156397840116798309327688757679}
 {40000000000000000000000000000000000}>0,
\]

\[
 (36\Gamma)_{X=1/11}=
 \frac{58882961473898540310036519874857514970749}
 {53240000000000000000000000000000000000}>0.
\]

The independent referee uses sharper monotonic endpoint choices and obtains

```text
Z <= 2912744931/11011000000 < 1,
danger reserve >= 201949716179/555555000000 > 0.
```

These differ from the source bounds because the two verifiers deliberately
use different valid envelopes; the theorem uses the weaker source bounds.
The 72-node grid is falsification only; the rational continuum reserve proves
the theorem.

## 6. Scope

This is a five-real-parameter moving-sheet theorem with normalized scale
`lambda*S in [999/1000,1001/1000]`.  It does not prove a full positive-`Z`
collar, arbitrary normalized scale, the compact-ball quartic on the whole
ball, the common-metric theorem, or the optimal fixed crossing-lens constant.
No maximality at `X=1/11` is claimed.  No proof assistant was used.



