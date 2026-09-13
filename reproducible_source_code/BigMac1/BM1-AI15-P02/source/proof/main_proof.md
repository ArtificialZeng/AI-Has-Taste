# An exact all-`n` proof of Barker's recurrence for A321614

## Theorem

Let `a(n)` be the number of orbits of maximum, hence `2n`-king,
nonattacking placements on a `4 x 2n` board under the four operations
identity, top–bottom reflection, left–right reflection, and half-turn. This
same four-element group is used when `n=2`. Set `a(0)=1`. Then

\[
\sum_{n\ge0}a(n)x^n=
\frac{(1-2x)(1-6x+17x^2-18x^3-2x^4+7x^5+6x^6-3x^7)}
{(1-x)^2(1-3x)^2(1-3x+x^2)(1-x-x^2)(1-3x^2)}.
\]

The fraction is reduced over `Q(x)`. Consequently Barker's order-ten
recurrence holds for every `n >= 10` and is the minimal eventual homogeneous
constant-coefficient recurrence over `Q`.

## 1. Maximum placements are paths in twelve states

Number rows `0,1,2,3`. Split the columns into consecutive pairs. Within each
column pair, its top two and bottom two rows form two disjoint `2 x 2`
subboards. Each is a clique for king attacks and contains at most one king.
Thus a `4 x 2n` board contains at most `2n` nonattacking kings. Placing kings
in rows 0 and 2 of the left column of every pair attains the bound. Equality
forces every top and bottom `2 x 2` subboard to contain exactly one king.

Encode a column by its four-bit occupancy mask. The legal column masks are

\[
\mathcal C=\{0,1,2,4,5,8,9,10\}.
\]

For `p,q in C`, write `p ~ q` when they can occur in adjacent columns:

\[
q\mathbin{\&}\bigl(p\mathbin{|}(p\ll1)\mathbin{|}(p\gg1)\bigr)=0.
\]

The possible two-column blocks of total weight two are exactly, in the order
used below,

\[
\mathcal B=((0,5),(0,9),(0,10),(1,4),(1,8),(2,8),
(4,1),(5,0),(8,1),(8,2),(9,0),(10,0)).
\]

Define the `12 x 12` zero-one matrix

\[
T_{(p,q),(r,s)}=[q\sim r]
\]

and let `u` be the all-ones column. The equality structure just proved gives
a bijection between maximum placements and paths in this graph. Hence the
identity fixed count is

\[
I_0=1,\qquad I_n=u^T T^{n-1}u\quad(n\ge1). \tag{1}
\]

This is a bijection, not a stabilized or asymptotic subsystem.

## 2. The four group elements on state paths

Let `rho` reverse the four row bits. On a block define

\[
h(p,q)=(\rho p,\rho q),\quad
j_v(p,q)=(q,p),\quad
j_r(p,q)=(\rho q,\rho p).
\]

Top–bottom reflection acts pointwise by `h`. Left–right reflection reverses
the block word and applies `j_v`; the half-turn reverses it and applies
`j_r`. Directly from adjacent-column compatibility,

\[
T_{p,q}=T_{j_vq,j_vp}=T_{j_rq,j_rp}. \tag{2}
\]

The only `h`-fixed blocks are `(0,9)` and `(9,0)`. Their induced transition
matrix is triangular with diagonal entries one and its other nonzero entry
equal to one. Its length-`n` path count is therefore

\[
H_n=n+1,\qquad H(x)=\sum_{n\ge0}H_nx^n=\frac1{(1-x)^2}. \tag{3}
\]

For a reversing involution `j`, put

\[
d_j(p)=T_{p,jp},\qquad f_j(p)=[jp=p].
\]

A fixed path of length `2m` is uniquely determined by its first half, with
the single extra middle-edge condition `d_j`. A fixed path of length `2m+1`
is uniquely determined by its first half and a `j`-fixed center. Thus

\[
F^j_{2m}=u^TT^{m-1}d_j\ (m\ge1),\qquad
F^j_{2m+1}=u^TT^mf_j\ (m\ge0). \tag{4}
\]

For the vertical reflection, `d_v` has three ones and `f_v=0`; for the
half-turn, `d_r` has seven ones and `f_r` has two. Formula (4) handles both
parities, including `n=1`, without negative matrix powers.

## 3. Finite integer resolvent certificate

Put

\[
D_0(y)=1-9y+28y^2-33y^3+9y^4
=(1-3y)^2(1-3y+y^2).
\]

Let `Z(y)=z_0+z_1y+z_2y^2+z_3y^3`, where the rows, in the displayed order
of `B`, are

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `z_0` | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `z_1` | 3 | 3 | 3 | -3 | -3 | -4 | -4 | -6 | -3 | -3 | -6 | -6 |
| `z_2` | -1 | -1 | -1 | 0 | 0 | 3 | 3 | 10 | 0 | 0 | 10 | 10 |
| `z_3` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | -3 | 0 | 0 | -3 | -3 |

Direct coefficientwise integer multiplication gives the decisive identity

\[
Z(y)(I-yT)=D_0(y)u^T. \tag{5}
\]

The serialized matrix and independent verifier rebuild `B,T` from the bit
rules before checking all coefficients of (5). Therefore (5), not a finite
prefix, gives

\[
u^T(I-yT)^{-1}=\frac{Z(y)}{D_0(y)} \tag{6}
\]

as a formal power-series identity.

Summing the entries of the rows `z_i` and applying (1) yields

\[
I(x)=\sum_{n\ge0}I_nx^n
=\frac{1+3x-x^2}{(1-3x)^2(1-3x+x^2)}. \tag{7}
\]

The same exact row-vector products give

\[
Z(y)d_v=3-18y+30y^2-9y^3,
\]

\[
Z(y)d_r=7-32y+36y^2-9y^3,qquad
Z(y)f_r=2-6y.
\]

Substitution into (4), with `y=x^2`, and exact factor cancellation gives

\[
V(x)=\sum_{n\ge0}V_nx^n=\frac1{1-3x^2}, \tag{8}
\]

\[
R(x)=\sum_{n\ge0}R_nx^n
=\frac{1+x+x^2}{(1-x-x^2)(1-3x^2)}. \tag{9}
\]

Thus every fixed-point branch has been proved for all lengths from one
finite integer matrix identity.

## 4. Burnside and Barker's recurrence

Burnside's lemma and the formal `n=0` convention give

\[
A(x)=\sum_{n\ge0}a(n)x^n=\frac{I(x)+H(x)+V(x)+R(x)}4. \tag{10}
\]

Exact polynomial addition in (10) gives

\[
A(x)=\frac{N(x)}{D(x)},
\]

where

\[
N(x)=(1-2x)(1-6x+17x^2-18x^3-2x^4+7x^5+6x^6-3x^7)
\]

and

\[
D(x)=(1-x)^2(1-3x)^2(1-3x+x^2)(1-x-x^2)(1-3x^2).
\]

Expanding,

\[
\begin{aligned}
D(x)={}&1-12x+54x^2-98x^3-17x^4+346x^5-505x^6\\
&+210x^7+120x^8-126x^9+27x^{10}.
\end{aligned}
\]

Since `deg N=8`, coefficient comparison in `D(x)A(x)=N(x)` proves for every
`n >= 10`

\[
\begin{aligned}
a(n)={}&12a(n-1)-54a(n-2)+98a(n-3)+17a(n-4)-346a(n-5)\\
&+505a(n-6)-210a(n-7)-120a(n-8)+126a(n-9)-27a(n-10).
\end{aligned}
\]

## 5. Exact minimality

The three quadratic factors of `D` are irreducible over `Q` (their
discriminants are 5, 5, and 12). Reducing the expanded numerator

\[
N=1-8x+29x^2-52x^3+34x^4+11x^5-8x^6-15x^7+6x^8
\]

modulo the five distinct irreducible factors of `D` gives, respectively,

| factor | remainder of `N` |
|---|---|
| `1-x` | `-2` |
| `1-3x` | `170/2187` |
| `1-3x+x^2` | `-37+97x` |
| `1-x-x^2` | `275-445x` |
| `1-3x^2` | `128/9-(74/3)x` |

All are nonzero, so `gcd(N,D)=1`. The machine certificate additionally
stores and verifies an exact rational Bezout identity. Therefore `N/D` is
reduced. A scalar sequence with a reduced rational ordinary generating
function of denominator degree ten has no homogeneous constant-coefficient
recurrence of smaller eventual order. This proves exact minimality.

## 6. The square boundary and the repaired convention

At `n=2`, the board is `4 x 4`. Direct enumeration of all 79 maximum
placements gives fixed counts

\[
(79,3,3,7)
\]

for identity, the two axial reflections and half-turn, hence 23 orbits under
the fixed rectangle subgroup. The four additional square symmetries have
fixed counts `3,3,7,7`, so the full square group gives 14 orbits.

This is material: replacing only `a(2)=23` by 14 makes the stated recurrence
fail at `n=10,11,12`. Thus the theorem must, and here does, specify the fixed
four-element rectangle subgroup even at `n=2`.

## 7. Reproducibility and proof-assistant disclosure

The compact resolvent certificate is checked by

```bash
python3 agents/builder/verify_certificate.py
```

An independently designed certificate embeds all four branches into one
68-dimensional integer representation and verifies 68 observable zeros for
the reversed denominator polynomial. Cayley–Hamilton proves every later zero:

```bash
python3 code/build_certificate.py
python3 code/verify_certificate.py certificate/a321614_certificate.json
```

The breaker independently enumerates placements and both group conventions:

```bash
python3 agents/breaker/verify_audit.py agents/breaker/audit_output.json
```

All decisive computation uses exact integers/rationals and the Python
standard library. No random search, floating point, SAT oracle, CAS, Lean,
Coq, Isabelle, or other proof assistant is used.
