# A monotonicity-certified active-block `t` layer of radius `1/402`

Date: 2026-08-23.  Status: **exact source-verified computer-assisted partial
theorem; independent referee audit still required**.  The unrestricted
complex Hermitian gate, the common-metric theorem, and the fixed
crossing-lens problem remain open.

This theorem strictly enlarges
`common_metric_tilted_rankone_complex_scale_t403_enlargement.md`.  The key
logical observation is exact: the cubic discriminant sign `N_D>0` is not a
dependency of the terminal positivity proof.  Once the endpoint value and
endpoint derivative are positive, strict convexity makes the cubic increase
on the whole legal half-line.  Removing that redundant consistency check
allows the derivative certificate to reach radius `1/402`.

Fix

\[
 a=\frac35,\qquad c=\frac45,
\]

and let

\[
\begin{gathered}
 8\leq\ell\leq10,\qquad -\frac{31}{100}\leq w\leq-\frac{29}{100},\\
 -\frac{301}{100}\leq k\leq-\frac{299}{100},\qquad
 -\frac{101}{100}\leq z\leq-\frac{99}{100},\\
 \frac{99}{100}\leq r\leq\frac{103}{100},\qquad
 \boxed{\frac{1607}{402}\leq t\leq\frac{1609}{402}}.
                                                               \tag{0.1}
\end{gathered}
\]

Thus

\[
                  4-\frac1{402}\leq t\leq4+\frac1{402}.
\]

The half-width is larger than the preceding `1/403` layer by the exact
factor `403/402`, and larger than the original `1/500` layer by `500/402`.

For `T>0`, put `s=sqrt(T)` and define

\[
\begin{aligned}
 \Delta&=rt-z^2-w^2,\\
 n&=t(k^2+\ell^2)+r-2(kz+\ell w),\\
 g&=\frac{12}{25}\ell-zk-w\ell-t,
\end{aligned}
\]

and

\[
 Q=\begin{pmatrix}
 r&s(k+i\ell)&z+iw\\
 s(k-i\ell)&Tn/\Delta&s\\
 z-iw&s&t
 \end{pmatrix}.                                      \tag{0.2}
\]

## 1. Exact legality and all scales

The certificate proves `Delta,n>0` on the complete closed box.  Hence the
active block indexed by `(1,3)` is positive definite.  Its scalar Schur
complement in (0.2) vanishes exactly, so `Q` is Hermitian PSD of rank two.

With a free middle diagonal entry, direct reconstruction gives

\[
 q_{\min}=\frac{Tn}{\Delta},\qquad q_g=g,
 \qquad q_{\min}-q_g=\frac{Tn-\Delta g}{\Delta}.    \tag{1.1}
\]

Therefore the complete strict complementary branch is

\[
 T>0\quad(g\leq0),\qquad
 T>\frac{\Delta g}{n}\quad(g>0).                  \tag{1.2}
\]

The proof also covers the closure endpoint `T=0` when `g<=0` and the finite
endpoint `T_L=Delta*g/n` when `g>0`.  No positive scale is sampled or
truncated.  The danger scalar is uniformly strict:

\[
 \operatorname{Re}(Qp)_1=\frac35r+\frac45z<0.      \tag{1.3}
\]

## 2. Original-gate scale cubic

The fail-closed source verifier starts from the fully conjugated Hermitian
gate, keeps both complex phase coordinates, forms `Q^2`, and derives

\[
 4\Delta^2\mathcal G(Q)
 =P(T)=C_0+C_1T+C_2T^2+n^2T^3,                    \tag{2.1}
\]

with

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn.             \tag{2.2}
\]

A second residual-square expansion reproduces the same cubic.  At the formal
positive-`g` endpoint `T_L=Delta*g/n`, define

\[
 P(T_L)=\frac{N_0}{15625n^2},\qquad
 P'(T_L)=\frac{N_1}{625n}.                        \tag{2.3}
\]

The exact curvature identities are

\[
 P''(T)=2(C_2+3n^2T),                             \tag{2.4}
\]

and, when `g>0`,

\[
 C_2+3n^2T_L
 =\Delta^2(k^2+\ell^2)+\Delta gn>0.               \tag{2.5}
\]

No discriminant polynomial is needed or assumed.

## 3. Exact dependency graph: why `N_D` is redundant

The terminal proof has two disjoint branches.

### Branch `g<=0`

The certificate gives `C0,C1,Delta,n>0`.  Equation (2.2) gives

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0.
\]

Thus every coefficient of (2.1) is positive.  Consequently `P(T)>0` for
every `T>=0`.

### Branch `g>0`

The certificate gives `N0,N1,Delta,n>0`.  Hence (2.3) gives

\[
 P(T_L)>0,\qquad P'(T_L)>0.
\]

Equation (2.5) gives `P''(T_L)>0`; since the right side of (2.4) increases
with slope `6n^2>0`, one has `P''(T)>0` for every `T>=T_L`.  Therefore
`P'` remains positive and `P` increases strictly from a positive endpoint.

The cubic discriminant never occurs in either branch.  A negative lower
bound for `N_D` therefore cannot affect this theorem.  It remains neither a
gate value nor a counterexample.

## 4. Exact derivative certificate at radius `1/402`

The `r` interval is the exact union of the independently audited `t=4`
centre cells

\[
 [99/100,101/100]\quad\text{and}\quad[101/100,103/100].
\]

For each essential sign polynomial

\[
 -\operatorname{Re}(Qp)_1,\quad\Delta,\quad n,\quad
 C_0,\quad C_1,\quad N_0,\quad N_1,               \tag{4.1}
\]

the centre theorems give an exact five-axis lower bound `p(4)>=m`.  On the
wider box `399/100<=t<=401/100`, the verifier expands `partial_t p` in the
six shape variables and proves the exact absolute monomial bound
`|partial_t p|<=M`.  Since `|t-4|<=1/402`,

\[
                         p(t)\geq m-\frac{M}{402}. \tag{4.2}
\]

The smaller reserve across the two stitched cells is:

| essential group | exact least reserve at half-width `1/402` |
|---|---:|
| danger | `87/500` |
| `Delta` | `713861/251250` |
| `n` | `1170138811/4020000` |
| `C0` | `83805326319665374729/251250000000000000` |
| `C1` | `118150790449310782759/125625000000000000` |
| `N0` | `53549445496650257669039960758536579907/128640000000000000000000000` |
| `N1` | `3602140976554567042623930779/21440000000000000000` |

Every entry is strictly positive.  Hence the original fully complex gate is
strictly positive on the entire family (0.1) at both closure endpoints and
at every legal positive scale.

For comparison only, the previous eight-sign package also tracked
`N_D=-244140625*Disc_T(P)`.  At radius `1/402`, its upper-cell reserve and
the other fourteen cell/group reserves remain positive, while its lower-cell
reserve is

\[
 -\frac{
 54657263927145682718521091555313864896870775497413042370594307870877001
 }{
 20582400000000000000000000000000000000000000000000
 }<0.
\]

This is merely an absolute-derivative lower bound.  It is not an evaluation
of `N_D` at one realizable parameter tuple, still less an evaluation of the
original gate.  The present proof avoids it because the discriminant is
logically unnecessary.

## 5. Nonredundancy and phase integrity

After quotienting common positive scale on the active block, the spectral
shape invariant `(r+t)/sqrt(Delta)` has `t` derivative with the sign of

\[
                         rt-r^2-2(z^2+w^2).
\]

On the wider derivative box, this numerator has the exact lower bound
`461/625>0`.  Thus `t` is neither the coupling scale `T` nor a hidden common
active-block rescaling.  Scaling the entire datum is also not an invariance
of the original gate because it contains both the fixed term `ac` and
entries of `Q^2`.

The exact witness

\[
 \ell=9,\quad w=-31/100,\quad k=-301/100,\quad z=-101/100,
 \quad r=103/100,\quad t=2001/500,\quad T=1
\]

lies strictly inside the new interval and satisfies the strict legal branch.
Direct original-gate evaluation gives

\[
 \mathcal G(Q)=
 \frac{414461983319631411704949}{112939929245000000000}>0,
\]

whereas

\[
 4\{\mathcal G(Q)-\mathcal G(\operatorname{Re}Q)\}
 =-\frac{585660171418319979}{375732500000000}<0.
\]

The two imaginary coordinates have product `-279/100`.  Thus no complex
phase is discarded, and the proof does not use CE-046, CE-048, CE-059,
real-part monotonicity, automatic phase absorption, or a universal
copositivity allocation.

## 6. Scope

This is a strict enlargement of one seven-real-parameter island, covering
every simultaneous complex phase choice inside the displayed shape box and
every legal scale.  It does not cover arbitrary active blocks, arbitrary
phase directions, the feasible-centre branch, unbalanced densities, higher
rank or dimension, arbitrary nodes, the common-metric theorem, or the fixed
crossing-lens constant.

The source verifier uses exact rational symbolic arithmetic, imports no
discovery code, reconstructs the original gate twice, binds all audited
centre dependencies by SHA-256, and fails closed under optimized Python or a
malformed dependency.
