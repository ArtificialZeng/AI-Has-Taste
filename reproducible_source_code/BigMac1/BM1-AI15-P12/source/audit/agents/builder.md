# Gate 5 independent proof-builder audit

Date: 2026-08-29.  Scope: the real rank-at-most-two problem in order
`n=3`, with a structural reduction for later work on `n=4`.  This note was
derived from the definition of the permanent.  It does not use numerical
evidence as a proof.

## 1. Exact binary-form reduction (all ranks and all zero cases included)

Factor a real matrix of rank at most two as

\[
 T_{ij}=r_i c_j^{\mathsf T},\qquad r_i,c_j\in\mathbb R^2.
\]

No component of these vectors is divided out.  Put

\[
 f(X,Y)=\prod_{i=1}^n(r_{i0}X+r_{i1}Y)
       =\sum_{k=0}^n f_kX^{n-k}Y^k,
\]
\[
 g(X,Y)=\prod_{j=1}^n(c_{j0}X+c_{j1}Y)
       =\sum_{k=0}^n g_kX^{n-k}Y^k
\]

and define the canonical coefficient contraction

\[
 [f,g]_n:=\sum_{k=0}^n\frac{f_kg_k}{\binom nk}.
\]

Expanding each factor in the permanent and first fixing the set of `k` rows
where the second component is selected shows directly that

\[
 \operatorname{per}(T)
 =\sum_{k=0}^n k!(n-k)!f_kg_k=n![f,g]_n.                 \tag{1}
\]

Indeed, after the row set and the corresponding column set have been fixed,
there are exactly `k!(n-k)!` compatible bijections.  In the doubled block
matrix every row vector and every column vector occurs twice.  Its two forms
are therefore `f^2` and `g^2`, and the same argument gives

\[
 \operatorname{per}\begin{pmatrix}T&T\\T&T\end{pmatrix}
 =(2n)![f^2,g^2]_{2n}.                                  \tag{2}
\]

Since `binom(2n,n)(n!)^2=(2n)!`, the Marcus inequality is **exactly**

\[
 [f^2,g^2]_{2n}\le [f,g]_n^2.                           \tag{3}
\]

This derivation is valid when `per(T)=0`, when one of the factor vectors is
zero, and when the rank is zero or one.

The contraction is invariant under the simultaneous dual change

\[
 r_i\mapsto r_iA,\qquad c_j\mapsto c_jA^{-\mathsf T}
 \quad(A\in GL_2(\mathbb R)),                            \tag{4}
\]

because it is the complete contraction of the two symmetric tensors.
Equation (4) preserves every entry of `T`; it is not a row/column scaling
quotient and introduces no excluded zero.

## 2. The complete `n=3` inequality

### Theorem

For every real `3 x 3` matrix `T` of rank at most two,

\[
 \operatorname{per}\begin{pmatrix}T&T\\T&T\end{pmatrix}
 \le 20\operatorname{per}(T)^2.                         \tag{5}
\]

### Proof on the dense simple-root stratum

First suppose that the three projective row directions are distinct and no
row factor is zero.  The triply transitive action of `PGL_2(R)`, together with
an irrelevant nonzero scalar multiplying `f`, reduces (by (4)) to

\[
 f(X,Y)=XY(X+Y).
\]

Write `g(1,z)=g_0+g_1z+g_2z^2+g_3z^3`.  Direct coefficient contraction gives

\[
 [f,g]_3=\frac{g_1+g_2}{3},
\]

and, because the only nonzero coefficients of `f^2` are `1,2,1` in
degrees `2,3,4`,

\[
 [f^2,g^2]_6=
 \frac{2g_0g_2+g_1^2}{15}
 +\frac{2g_0g_3+2g_1g_2}{10}
 +\frac{2g_1g_3+g_2^2}{15}.
\]

Consequently

\[
 45\bigl([f,g]_3^2-[f^2,g^2]_6\bigr)=N(g),              \tag{6}
\]

where

\[
 N(g)=2g_1^2+g_1g_2+2g_2^2-6g_0g_2-9g_0g_3-6g_1g_3.
                                                                    \tag{7}
\]

The form `g` is a product of three real linear forms.  On the dense chart
where `g_3` is nonzero and all three affine roots are finite, division by the
nonzero scalar `g_3` is harmless because `N` is quadratic.  Order the roots
and write them as

\[
 a=t,\qquad b=t+p,\qquad c=t+p+q,\qquad p,q\ge0.
\]

For `g(1,z)=(z-a)(z-b)(z-c)`, exact expansion of (7) gives

\[
\begin{aligned}
N={}&2(p^2+pq+q^2)t^2\\
 &+(4p^3+6p^2q-2p^2+2pq^2-2pq-2q^2)t\\
 &+2p^4+4p^3q-2p^3+2p^2q^2-3p^2q+2p^2\\
 &\hspace{35mm}-pq^2+2pq+2q^2.                         \tag{8}
\end{aligned}
\]

As a quadratic polynomial in `t`, its discriminant is

\[
 -12\,S(p,q),                                            \tag{9}
\]

where

\[
\begin{aligned}
S(p,q)={}&p^4q^2+p^4+2p^3q^3+2p^3q+p^2q^4
          +3p^2q^2+2pq^3+q^4.
\end{aligned}
\]

Every term in `S` is nonnegative.  If `(p,q) != (0,0)`, then
`S>0` (use the `p^4` or `q^4` term) and the leading coefficient in (8) is
positive.  Hence `N>0`.  If `p=q=0`, direct substitution into (8) gives
`N=0`.  Thus (3) holds on the simple-row stratum for every split real `g`.
The missing affine charts and repeated roots follow by coefficient
continuity: products with finite roots and nonzero leading coefficient are
dense in the space of products of three real homogeneous linear forms.

### Removal of the simple-row assumption

Products of three nonzero real linear forms with three distinct projective
directions are dense in all products of three real linear forms.  Both sides
of (3) are polynomial in the factor coefficients.  Perturb the row factors,
apply the already proved simple-root result, and pass to the limit.  If a row
factor is zero then `f=0` and both contractions in (3) vanish directly.
This proves (3), hence (5), without any division by `per(T)`.

## 3. Boundary and equality audit

* If `per(T)=0`, (3) gives `[f^2,g^2]_6 <= 0`; after multiplying by `6!`,
  this is exactly the required assertion.  The proof never forms a ratio by
  `per(T)`.
* If `T` has a zero row or column, both permanents are zero.  More generally,
  setting a row or column scale to zero is legitimate: under
  `T -> diag(alpha) T diag(beta)`, the small permanent is multiplied by
  `prod(alpha_i)prod(beta_j)` and the doubled permanent by its square.  These
  are polynomial identities, including zero scales.
* Rank zero is immediate.  At rank one, write `T=ab^T`.  Both sides of (5)
  are `(6!)(prod_i a_i prod_j b_j)^2`, so equality holds, including zeros.

For completeness, equality on the split-cubic strata can be read from the
same proof.  If `f` has three distinct factors, (8)--(9) gives equality
exactly when all three finite roots of `g` coincide.  Here is the direct
check of the homogeneous boundary.  When `g_3=0` and `g_2 != 0`, scale to
`g(1,z)=(z-a)(z-b)`.  Formula (7) becomes

\[
 N=2(a^2-ab+b^2)-(a+b)+2
  =\frac12(a+b-1)^2+\frac32(a-b)^2+\frac32>0.
\]

If `g_3=g_2=0` but `g_1 != 0`, then `N=2g_1^2>0`; if only `g_0`
can be nonzero, `g=g_0X^3` and `N=0`.  Thus on every homogeneous chart the
equality forms are exactly cubes (and the zero form).  If `f=L^3`, contraction of a
pure symmetric tensor shows equality for every split `g`.  If `f` has type
`L^2M` with independent `L,M`, use (4) and scaling to set `f=X^2Y`.  Then

\[
 [f,g]_3^2-[f^2,g^2]_6
 =\frac{2}{45}(g_1^2-3g_0g_2).                          \tag{10}
\]

When `g_0 != 0`, put `g=g_0\prod_i(1+r_i z)`; the last factor in (10) is

\[
 g_0^2\left((r_1+r_2+r_3)^2-3(r_1r_2+r_1r_3+r_2r_3)\right)
 =\frac{g_0^2}{2}\sum_{i<j}(r_i-r_j)^2.
\]

On `g_0=0`, direct factor inspection gives equality exactly when at least two
factors are proportional to `Y` (the cube `Y^3` included).  Thus, in the
normal form `f=X^2Y`, equality occurs when `g` is a cube or when `Y^2`
divides `g`.  This also exhibits genuine rank-two equality cases.  Applying
the same classification after swapping `f,g` is a consistency check.

### Matrix-level iff equality classification

The preceding form-level statement is equivalent to the following complete
matrix classification.

**Equality theorem.**  Equality holds in (5) if and only if at least one of
the following conditions holds:

1. `rank(T) <= 1`;
2. `T` has a zero row or a zero column;
3. after independent row and column permutations, `T` contains a `2 x 2`
   all-zero submatrix.

Conditions may overlap.  In item 3 it is enough, when proving necessity, to
assume rank two and no zero row or column.

Sufficiency is direct.  Rank-one equality was evaluated above.  A zero row or
column kills both permanents.  If the upper-left `2 x 2` block is zero, write

\[
T=\begin{pmatrix}0&0&a\\0&0&b\\u&v&w\end{pmatrix}.
\]

The first two rows cannot be assigned distinct columns in the `3 x 3`
permanent.  In the doubled matrix, the four copies of those rows have nonzero
entries in at most the two copies of the third column, so they cannot be
assigned four distinct columns.  Thus both permanents vanish.

For necessity, assume rank two and no zero row or column, and use a full-rank
factorisation `T=UV^T`.  The maps from the two-dimensional factor space to
matrix rows and columns are injective, so zero factor vectors and zero matrix
rows/columns are equivalent here.  Three equal row directions would make
`rank(U)=1`.  Hence the row directions are either all distinct or have type
`2+1`.  The nonzero row rescalings used in the following projective normal
forms multiply the full gap by the square of their product, so they preserve
its zero set.

In the distinct case take the homogeneous normal form

\[
 a=(-1,0,1),\qquad T_{ij}=c_j+a_i d_j.
\]

The independently verified SOS form is

\[
\frac{20\operatorname{per}(T)^2-\operatorname{per}(B)}{16}
=\Delta_{12}^2(d_0^2+3c_0^2)
 +\Delta_{02}^2(d_1^2+3c_1^2)
 +\Delta_{01}^2(d_2^2+3c_2^2),                         \tag{11}
\]

where `Delta_ij=d_i c_j-c_i d_j`.  With no zero column, all three weights
are positive.  Equality forces every `Delta_ij=0`, hence `rank(V)=1`,
contrary to `rank(T)=2`.  Thus this stratum has no rank-two equality without
a zero column.

In the repeated case take

\[
 a=(0,0,1),\qquad T_{ij}=c_j+a_i d_j.
\]

The second homogeneous SOS normal form is

\[
\frac{20\operatorname{per}(T)^2-\operatorname{per}(B)}{16}
=\Delta_{01}^2c_2^2+\Delta_{02}^2c_1^2
 +\Delta_{12}^2c_0^2.                                  \tag{12}
\]

Suppose first that every `c_i` is nonzero.  Equality forces all three minors
to vanish and again contradicts `rank(V)=2`.  If exactly one, say `c_0`, is
zero, then the nonzero-column assumption gives `d_0 != 0`; the first two
summands force `Delta_01=Delta_02=0`, impossible because
`Delta_01=d_0c_1 != 0`.  Therefore equality requires at least two of the
`c_i` to vanish.  All three cannot vanish because then `rank(V)=1`.  After a
column permutation, `c_0=c_1=0`, and the first two (equal up to their
previously removed nonzero row scales) matrix rows vanish in columns 0 and
1.  This is exactly a `2 x 2` zero block.  Conversely these vanishing
conditions make (12) zero.  This proves the iff statement, including the
rank-two, no-zero-row/column boundary requested by the referee.

### Comparison with the discriminant proof and the two homogeneous SOS forms

The two proofs agree by explicit dual changes of basis, not just by their
vanishing sets.  For (11), the matrix

\[
A=\begin{pmatrix}1&1\\-1&1\end{pmatrix}
\]

sends `X(X-Y)(X+Y)` to `4XY(X+Y)` and sends a column covector `(c,d)` to
`((c-d)/2,(c+d)/2)`.  Substitution into (7) gives the right side of (11)
as exactly `16N(g')`; the extra factor is the square of the scalar 4 on the
row form.  Thus the negative-discriminant proof and the first SOS are the
same invariant gap in two charts.

For (12),

\[
A=\begin{pmatrix}1&0\\-1&1\end{pmatrix}
\]

sends `X^2(X+Y)` to `X^2Y` and sends `(c,d)` to `(c,c+d)`.  Exact substitution
shows that the right side of (12) is
`2(g_1'^2-3g_0'g_2')`, precisely the homogeneous version of (10).  The
condition `Y^2 | g'` becomes "at least two `c_j` vanish," which is exactly
the `2 x 2` zero-block case above.

## 4. `n=4` structural endpoint and unresolved gap

Equations (1)--(4) remain valid verbatim.  On the generic four-row-direction
stratum, a dual `GL_2` change reduces the row form, up to scale and a
permutation of factors, to a one-parameter cross-ratio form such as

\[
 f=XY(X-Y)(X-\lambda Y),\qquad
 \lambda\in\mathbb R\setminus\{0,1\}.                  \tag{13}
\]

The desired statement is then the exact quadratic inequality in the five
coefficients of an arbitrary split real quartic `g`

\[
 [f,g]_4^2-[f^2,g^2]_8\ge0.                             \tag{14}
\]

No proof of (14), uniformly in the cross-ratio and on all collision strata,
is supplied here.  In particular, the `n=3` discriminant argument does not by
itself remove the extra parameter.  This is an explicit remaining gap, not a
numerical inference.

## 5. Independent exact checks

Run

```bash
python experiments/builder_verify_n3.py
python certificates/verify_n3_sos.py
python certificates/builder_verify_n3_equality.py
```

The script independently reconstructs (6)--(10) with exact symbolic
arithmetic, checks (1)--(2) against direct enumeration of all `3!` and `6!`
permutations for a fixed mixed-sign rank-two integer matrix, and prints
`ALL EXACT CHECKS PASSED`.  The theorem itself rests on the displayed
algebraic identities and the elementary quadratic-discriminant argument, not
on the finite test example.  The two certificate commands independently
rebuild the homogeneous SOS identities from permanent definitions and check
their exact `GL_2` relation to the discriminant proof, together with symbolic
rank-one and `2 x 2` zero-block families.

## 6. Proof-assistant disclosure and audit verdict

No proof assistant was used.  SymPy is used only to cross-check polynomial
expansions; every positivity step is displayed as a finite exact identity.
The proof-builder verdict is: **the real `n=3`, rank-at-most-two case is
proved**, while `n=4` remains open in this note.
