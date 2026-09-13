# Exact moving-sheet extension on the closed cell `1/21 <= X <= 1/20`

Date: 2026-08-24.  Status: **exact computer-assisted partial theorem,
independently reconstructed from the original gate**.  The full compact-ball
quartic, unrestricted complex Hermitian gate, common-metric theorem, and fixed
crossing-lens constant remain open.

## 1. Statement

Let

```text
0 < S <= 1/10000,
1/21 <= X <= 1/20,
|M| <= 1/1000,
|omega|, |nu| <= 1/100.
```

Put `A=1+M` and keep the audited moving sheet

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

The seam-preserving closed-cell coordinate is

```text
u = 420(X-1/21),       0 <= u <= 1,
X = (20+u)/420.
```

Thus `u=0` is exactly the independently audited predecessor endpoint
`X=1/21`; no limiting argument is used at the seam.

For either real sign of `z` with `z^2=Z`, set

```text
a=1/sqrt(6), c=sqrt(5/6), zeta=(4+3i)/5, h=sqrt(S),
r0=(-a,0,c*zeta),
fh=(-c*h,sqrt(1-h^2),-a*h*zeta),
U=(r0 fh),
j=(1+5x)/(3sqrt(5)),
kappa=(-3+5y)/(3sqrt(5)),
ell=sqrt(5)z/3,
C=[[h^2,h(j+i kappa)],[h(j-i kappa),j^2+kappa^2+ell^2]],
H=U C U^*, Q=lambda H.
```

For `p=(a,0,c)^T`, let `xi=Qp` and define the fully conjugated original
scalar gate

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
`ell` only through `ell^2=5Z/9`.  Both `X` endpoints are included.  Together
with the audited predecessor this extends the same moving-sheet theorem to
`0<=X<=1/20`.  The quantifier remains `S>0`; at `S=0`, `lambda=A/S` is not
defined.

## 2. Definition-level reconstruction

The source verifier begins with the displayed transverse frame and checks its
Gram matrix, one-dimensional kernel, Hermitian symmetry, and

\[
 \det C=\frac59SZ.
\]

It constructs `Q`, all nine entries of the fully conjugated `Q^2`, and the
literal gate above.  Independently, it constructs

\[
 \Gamma(\lambda H)
 =\|B_0+\lambda L+\lambda^2M_2\|^2
  -32a^2\lambda^2(\operatorname{Re}(Hp)_1)^2,
 \qquad \Gamma=4\mathcal G,
\]

and verifies equality coefficient by coefficient.  Exact elimination of
`q^2=1-h^2`, `z^2=Z`, and `h^2=S` leaves the rational quartic `36 Gamma`,
whose constant coefficient is five.  The independent verifier uses a
different component order in the Gram vector and an affine-power/nodal-style
coefficient reconstruction; it imports neither source coefficients nor a
cached quartic.

## 3. Exact legality

On the whole closed parameter box,

```text
A >= 999/1000 > 0,
y0 >= 46999/100100 > 0,
wc+omega >= 628/925,
wc+omega-S*y0^2 >= 7528197233111/11088900000000 > 0.
```

Since `3X-X^2` is increasing on the cell,

\[
 Z>3/21-1/21^2=62/441>1/8,
 \qquad
 Z\le\frac{147720681}{1001000000}<\frac3{20}.
\]

The exact identity

\[
 x^2+y^2+Z=\frac25+\frac{13}{5}X+\frac65Y+W
\]

gives the strict danger reserve

\[
 1-x^2-y^2-Z\ge
 \frac{261037535879}{555555000000}>0.
\]

Finally `det C=(5/9)SZ>0`, so the compression and `Q` have rank two.  These
facts are certified separately from the gate estimate.  In particular, the
proof neither divides by `Z-1/8` nor infers legality from gate positivity.

## 4. Exact continuum certificate

Set

```text
N=S^3*(36 Gamma),
D=25^8*(1+M)^8,
Qhat=D*N/S^2.
```

Every clearing factor is positive on the actual domain and

```text
36 Gamma = Qhat/[25^8(1+M)^8*S].
```

Fresh substitution into the original quartic gives 134 pre-map monomials.
After exact division by `S^2`, `Qhat` has twenty `(S,X)` terms and bidegree
`(5,4)`.  Its first layer is nonnegative:

\[
 25^8M^2S(1+M)^8(5M^2+14M+14)\ge0.
\]

For the quadratic layer `a_2S^2+b_2SX+c_2X^2`, centered exact arithmetic
proves `a_2,b_2,c_2>0` and

\[
 c_2\ge c_0=
 \frac{2564950982194530478444050838857341987999}
 {1274019840000000000000000000}>0.
\]

On this cell the lossless projective order is

```text
S=sigma X,       0<sigma<=21/10000.
```

After division by positive `X^2`, the sixteen higher `(S,X)` terms contain
947 centered parameter monomials.  Their exact absolute contribution is at
most

\[
 R_{\rm abs}=
 \frac{13985376150646614153686197249832270290516626676331792401160666464303}
 {5096079360000000000000000000000000000000000000000000000000}.
\]

Even after discarding the additional positive terms
`a_2 sigma^2+b_2 sigma`, the strict reserve is

\[
 c_0-R_{\rm abs}=
 \frac{10245818552627475299622517158179535681705483373323668207598839333535697}
 {5096079360000000000000000000000000000000000000000000000000}>0.
\]

This is a continuum certificate for the original gate, not a sample test or
a surrogate-coefficient claim.

## 5. Falsification and seams

An exact grid uses three positive `S` values, `u=0,1/2,1`, and all eight
corners of `(M,omega,nu)`, for 72 legal rational nodes.  No negative original
gate occurs.  At

```text
S=1/10000, M=-1/1000, omega=nu=-1/100,
```

the seam and right endpoint give respectively

\[
 (36\Gamma)_{X=1/21}=
 \frac{4188229430882337003171468410585844383897}
 {13720000000000000000000000000000000000}>0,
\]

\[
 (36\Gamma)_{X=1/20}=
 \frac{13454196138451967922937008431058757679}
 {40000000000000000000000000000000000}>0.
\]

The grid is falsification only; the strict rational envelope proves the
continuum.

## 6. Scope

This is a five-real-parameter moving-sheet theorem with normalized scale
`lambda*S in [999/1000,1001/1000]`.  It does not prove a full positive-`Z`
collar, arbitrary normalized scale, the compact-ball quartic on the whole
ball, the common-metric theorem, or the optimal fixed crossing-lens constant.
No maximality at `X=1/20` is claimed.

