# Exact moving-sheet extension through `X=1/22`

Date: 2026-08-24.  Status: **exact source-verified computer-assisted partial
theorem**.  The full compact-ball quartic, unrestricted complex Hermitian
gate, common-metric theorem, and fixed crossing-lens constant remain open.

## 1. Quantified statement

Let

```text
0<S<=1/10000,
1/23<=X<=1/22,
|M|<=1/1000,
|omega|,|nu|<=1/100.
```

Put `A=1+M` and use the exact moving sheet

```text
lambda = A/S,
y0     = 12/(25A)+nu,
wc     = -3(5MX-15M+5X-6)/(25A),
Y      = S*y0,
Wsh    = S*(wc+omega),
Z      = 3X-X^2-Y^2+Wsh,
x      = -1/5+X,
y      =  3/5+Y.
```

For either real sign of `z` with `z^2=Z`, set

\[
 a=1/\sqrt6,\quad c=\sqrt{5/6},\quad
 \zeta=(4+3i)/5,\quad h=\sqrt S,
\]

\[
 r_0=(-a,0,c\zeta)^T,\qquad
 f_h=(-ch,\sqrt{1-h^2},-ah\zeta)^T,\qquad U_h=(r_0\ f_h),
\]

and

\[
 j=\frac{1+5x}{3\sqrt5},\qquad
 \kappa=\frac{-3+5y}{3\sqrt5},\qquad
 \ell=\frac{\sqrt5}{3}z,
\]

\[
 H=U_h\begin{pmatrix}
 h^2&h(j+i\kappa)\\
 h(j-i\kappa)&j^2+\kappa^2+\ell^2
 \end{pmatrix}U_h^*,\qquad Q=\lambda H.
\]

Then

```text
lambda>0,
68/529 < Z <= 1479554991/11011000000 < 1/7,
x^2+y^2+Z<1,
det(compression)=(5/9)SZ>0.
```

Consequently `Q` is Hermitian positive semidefinite of rank two and lies in
the strict dangerous chart.  For `p=(1/sqrt(6),0,sqrt(5/6))^T`, let
`xi=Qp` and define the fully conjugated original scalar gate

\[
\begin{aligned}
 \mathcal G(Q)={}&a^2|\xi_2|^2
 +\frac14\left|c\overline{\xi_1}+a\xi_3
       +i\{ac-(Q^2)_{31}\}\right|^2\\
 &+\frac14\left|c\overline{\xi_2}-i(Q^2)_{32}\right|^2
 -8a^2(\operatorname{Re}\xi_1)^2.
\end{aligned}
\]

The conclusion is

\[
                         \boxed{\mathcal G(Q)>0}.
\]

Both `X` endpoints are included.  Since the independently audited predecessor
contains `X=1/23`, the two closed cells stitch without a limit argument and
give the same moving-sheet conclusion on the merged interval

```text
0<=X<=1/22.
```

The theorem has `S>0`; `S=0` is only an algebraic closure and cannot define
`lambda=A/S`.  The normalized scale is restricted to
`lambda*S=A in [999/1000,1001/1000]`.

## 2. Independent original-gate reconstruction

The source verifier imports neither a predecessor verifier, a discovery
quartic, nor cached coefficients.  Starting from the displayed transverse
frame it verifies its Gram identities, the one-dimensional kernel, and

\[
 \det\begin{pmatrix}
 h^2&h(j+i\kappa)\\h(j-i\kappa)&j^2+\kappa^2+5Z/9
 \end{pmatrix}=\frac59SZ.
\]

It forms the Hermitian matrix `Q`, its fully conjugated square `Q^2`, and the
two indexed leakage entries in the definition of `mathcal G`.  After using
only `q^2=1-h^2`, it obtains a quartic in `lambda`.  With

```text
Gamma=4*mathcal G,
```

the verifier also constructs the independent Gram-vector expression

\[
 \Gamma(\lambda H)
 =\|\mathcal B_0+\lambda\mathcal L+\lambda^2\mathcal M\|^2
  -32a^2\lambda^2(\operatorname{Re}(Hp)_1)^2
\]

and checks equality coefficient by coefficient.  The exact compact
normalization is `36 Gamma=144 mathcal G`; its quartic has constant term five.

## 3. Legality certificate

On the full parameter box,

```text
A>=999/1000>0,
y0>=46999/100100>0,
wc+omega >= 27743/40700,

wc+omega-S*y0^2
 >= 83142836564221/121977900000000 > 0.
```

Since `3X-X^2` is increasing on this cell,

\[
 Z\ge 3X-X^2+S\frac{83142836564221}{121977900000000}
   >\frac{68}{529}>\frac18.
\]

The independent upper estimate is

\[
 Z\le\frac{1479554991}{11011000000}<\frac17.
\]

The exact moving-sheet identity

\[
 x^2+y^2+Z=\frac25+\frac{13}{5}X+\frac65Y+W_{\rm sh}
\]

gives

\[
 1-x^2-y^2-Z\ge
 \frac{267603185879}{555555000000}>0.
\]

Thus scale, positive `Z`, compact-ball danger, and rank two are proved
separately from the gate estimate.  No coordinate `T=Z-1/8` is introduced or
divided out.  In particular, the argument would not acquire a hidden
division even at a cap boundary.

## 4. Lossless sigma envelope

Set

```text
N=S^3*(36 Gamma),
D=25^8*(1+M)^8,
Qhat=D*N/S^2.
```

Every clearing factor is strictly positive on the actual domain, and

```text
36 Gamma = Qhat/[25^8(1+M)^8*S].
```

The verifier reconstructs the moving substitution sparsely from the original
quartic.  Before the map there are 134 monomials.  After exact division by
`S^2`, `Qhat` has exactly twenty `(S,X)` monomials and bidegree `(5,4)`.  Its
first layer is

\[
 25^8M^2S(1+M)^8(5M^2+14M+14)\ge0.
\]

Writing the homogeneous quadratic layer as

\[
 H_2=a_2S^2+b_2SX+c_2X^2,
\]

exact centered-monomial estimates give `a_2,b_2,c_2>0` and in particular

\[
 c_2\ge c_0=
 \frac{2564950982194530478444050838857341987999}
 {1274019840000000000000000000}>0.
\]

The lossless projective coordinate on this cell is

```text
S=sigma*X,       0<sigma<=23/10000.
```

After division by positive `X^2`, retain every exact power `sigma^i` in the
sixteen higher `(S,X)` terms.  Recomputing all 947 centered parameter
monomials gives the absolute remainder

\[
 R_{\rm abs}=
 \frac{45501595887352000690514390785303819932610237699051256372767272123253}
 {16648891269120000000000000000000000000000000000000000000000}.
\]

Even after discarding the additional positive terms
`a_2 sigma^2+b_2 sigma`, the strict margin is

\[
 c_0-R_{\rm abs}=
 \frac{33473277839430772291616341971402441279238321762300948743627232727876747}
 {16648891269120000000000000000000000000000000000000000000000}>0.
\]

This proves strict positivity of the original gate on the entire closed
cell, not merely at sampled points and not merely for a surrogate
coefficient polynomial.

## 5. Endpoint and falsification checks

The same exact envelope contains both endpoints.  For the concrete corner

```text
S=1/10000, M=-1/1000, omega=nu=-1/100,
```

the left endpoint `X=1/23` has

```text
36 Gamma =
2851967535986553322459201051507517913149039
/11193640000000000000000000000000000000000 > 0,
```

and the right endpoint `X=1/22` has

```text
36 Gamma =
14817150110247071841775080222180418970749
/53240000000000000000000000000000000000 > 0.
```

These witnesses are diagnostics; continuum positivity comes from the exact
envelope above.  A separate exact rational falsification grid uses three
positive `S` values, both endpoints and their midpoint, and all eight corners
of the `(M,omega,nu)` box, for 72 legal nodes.  No negative is found.  The
smallest sampled raw value is the displayed left-endpoint value.  Sampling is
not used in the proof.

## 6. Verification and scope

Run

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x22_extension.py
```

The verifier uses exact symbolic rational arithmetic, rejects optimized
Python and unknown arguments, binds this statement and the audited `X<=1/23`
predecessor by SHA-256, and recomputes every decisive expression from the
original Hermitian definitions.

This is a partial theorem on one five-real-parameter moving-sheet family.  It
does not cover arbitrary compact-ball coordinates, arbitrary normalized
scale, the general complex Hermitian gate, common metrics, arbitrary nodes,
or the optimal fixed crossing-lens constant.  No sharpness or maximality at
`X=1/22` is claimed.
