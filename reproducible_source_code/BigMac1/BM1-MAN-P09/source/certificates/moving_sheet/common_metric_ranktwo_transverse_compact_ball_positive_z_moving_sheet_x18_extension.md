# Exact moving-sheet extension on the closed cell `1/19 <= X <= 1/18`

Date: 2026-08-24.  Status: **exact computer-assisted partial theorem,
independently reconstructed from the original gate**.  The full compact-ball
quartic, unrestricted complex Hermitian gate, common-metric theorem, and fixed
crossing-lens constant remain open.

## 1. Statement

Let

```text
0 < S <= 1/10000,
1/19 <= X <= 1/18,
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
u = 342(X-1/19),       0 <= u <= 1,
X = (18+u)/342.
```

Thus `u=0` is exactly the independently audited predecessor endpoint
`X=1/19`; no continuity or limiting argument is used at the seam.

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
`0<=X<=1/18`.  The quantifier remains `S>0`; `lambda=A/S` is undefined at
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
wc+omega >= 7499/11100,
wc+omega-S*y0^2 >= 7491234233111/11088900000000 > 0.
```

Monotonic endpoint bounds give

\[
 Z>3/19-1/19^2=\frac{56}{361}>\frac18,
 \qquad
 Z\le\frac{13269177661}{81081000000}<\frac16.
\]

The moving-sheet identity

\[
 x^2+y^2+Z=\frac25+\frac{13}{5}X+\frac65Y+W
\]

gives the strict danger reserve

\[
 1-x^2-y^2-Z\ge
 \frac{759038557637}{1666665000000}>0.
\]

Finally `det C=(5/9)SZ>0`, so the compression and `Q` have rank two.  The
legality proof is independent of the gate estimate and never divides by a
chart-boundary expression.

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
S=sigma X,       0<sigma<=19/10000.
```

After division by positive `X^2`, the sixteen higher terms contain 947
centered parameter monomials.  Their total exact absolute contribution is at
most

\[
 R_{\rm abs}=
 \frac{276675774066955888671433955119085619971144287904209914384809259360019}
 {100306130042880000000000000000000000000000000000000000000000}.
\]

Discarding additional positive quadratic terms still leaves the strict
reserve

\[
 c_0-R_{\rm abs}=
 \frac{201667044956072817740185576689797163779166123712095790085615190740639981}
 {100306130042880000000000000000000000000000000000000000000000}>0.
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
 (36\Gamma)_{X=1/19}=
 \frac{1941635149051525232795626443278240808984959}
 {5212840000000000000000000000000000000000}>0,
\]

\[
 (36\Gamma)_{X=1/18}=
 \frac{16590441965844177687836029861184257679}
 {40000000000000000000000000000000000}>0.
\]

The independent referee uses sharper monotonic endpoint choices and obtains

```text
Z <= 13268907391/81081000000 < 1/6,
danger reserve >= 759044113187/1666665000000 > 0.
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
No maximality at `X=1/18` is claimed.  No proof assistant was used.
