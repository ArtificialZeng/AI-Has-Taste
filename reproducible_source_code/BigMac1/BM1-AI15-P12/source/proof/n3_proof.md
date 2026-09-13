# The real order-three rank-two Marcus inequality

## Theorem

For every real `3 x 3` matrix `T` with `rank(T) <= 2`,

\[
 \operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
 \le 20\operatorname{per}(T)^2. \tag{1}
\]

Equality holds as follows:

1. every matrix of rank at most one is an equality case;
2. a rank-two matrix is an equality case if and only if it has a zero row, a
   zero column, or it contains a `2 x 2` all-zero submatrix after row and
   column permutations.

All assertions are over the reals.  No division by `per(T)` is used.

## 1. Rank-two factorisation and scaling

Write

\[
 T_{ij}=u_i v_j^{\mathsf T},\qquad u_i,v_j\in\mathbb R^2. \tag{2}
\]

The simultaneous change

\[
 u_i\longmapsto u_iG,\qquad
 v_j\longmapsto v_jG^{-\mathsf T},\qquad G\in GL_2(\mathbb R), \tag{3}
\]

leaves every entry of `T` unchanged.  If `T=D_r A D_s`, with diagonal
row and column scales, then, writing

\[
 \Delta(T):=20\operatorname{per}(T)^2-
 \operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix},
\]

one has the polynomial identity

\[
 \Delta(T)=\left(\prod_i r_i\prod_j s_j\right)^2\Delta(A). \tag{4}
\]

We only use (4) with nonzero scales when taking normal forms; zero scales are
handled directly below.

Assume first that `rank(T)=2` and that `T` has no zero row or column.  Then in
a rank-two factorisation (2), all `u_i,v_j` are nonzero and each of the two
factor matrices has rank two.  The three projective row directions therefore
have one of two types: three distinct directions, or one direction repeated
twice.  Three equal directions would make the factor matrix, hence `T`, have
rank at most one.

## 2. Three distinct row directions

The triply transitive real projective action induced by (3), followed by
nonzero row scalings as in (4), gives

\[
 A_{ij}=c_j+a_i d_j,\qquad (a_1,a_2,a_3)=(-1,0,1), \tag{5}
\]

where every `(c_j,d_j)` is nonzero.  Put

\[
 [ij]:=d_i c_j-c_i d_j.
\]

Direct expansion from the permanent definition gives the exact identity

\[
\begin{aligned}
 \Delta(A)=16\{&[23]^2(d_1^2+3c_1^2)
                 +[13]^2(d_2^2+3c_2^2)\\
                &+[12]^2(d_3^2+3c_3^2)\}.             \tag{6}
\end{aligned}
\]

This is a sum of squares with strictly positive weights because
`(c_j,d_j) != (0,0)`.  Hence it is nonnegative.  If it vanishes, then
`[12]=[13]=[23]=0`, so all projective column directions coincide.  That would
make the column factor matrix, hence `T`, have rank at most one.  Thus (1) is
strict on the rank-two, three-distinct-row stratum.

For reference, (6) may be checked without trusting any stored expansion by
enumerating all `3!` and `6!` permutations; this is exactly what
`certificates/verify_n3_sos.py` does.

## 3. One repeated row direction

The same operations now give

\[
 A_{ij}=c_j+a_i d_j,\qquad (a_1,a_2,a_3)=(0,0,1).       \tag{7}
\]

The second exact identity is

\[
 \Delta(A)=16\bigl([12]^2c_3^2+[13]^2c_2^2+[23]^2c_1^2\bigr). \tag{8}
\]

Thus (1) again follows.  Suppose (8) vanishes and the column factor matrix has
rank two.  If every `c_j` is nonzero, (8) forces all three brackets to vanish,
a contradiction.  If exactly one `c_j` vanishes, say `c_3=0`, then
`d_3 != 0`, and `[13]^2c_2^2=c_1^2d_3^2c_2^2>0`, again a contradiction.
All three `c_j` cannot vanish because the column factor matrix has rank two.
Consequently equality occurs exactly when, after a column permutation,

\[
 c_1=c_2=0,\qquad c_3\ne0.                             \tag{9}
\]

In (7), condition (9) says precisely that the first two (proportional) rows
and the first two columns form a `2 x 2` all-zero submatrix.  Conversely such
a zero block makes both permanents zero: the two original rows supported only
in the remaining column cannot be matched injectively, and their four copies
in the doubled block cannot be matched into the two copies of that column.

## 4. Zero and lower-rank strata

If `T` has a zero row or zero column, both permanents in (1) vanish.  If
`rank(T)<=1`, write `T=xy^T`.  Then

\[
 \operatorname{per}(T)=3!\prod_i x_i\prod_j y_j
\]

and

\[
 \operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
 =6!\left(\prod_i x_i\prod_j y_j\right)^2
 =20\operatorname{per}(T)^2.                           \tag{10}
\]

This includes all zeros.  Sections 2--4 exhaust `rank(T)<=2`, prove (1), and
give the stated equality classification.

## 5. Independent binary-form derivation

As a structural cross-check, define the split real binary cubics

\[
 f(X,Y)=\prod_i(u_{i0}X+u_{i1}Y)=\sum_{k=0}^3f_kX^{3-k}Y^k,
\]

and similarly `g` from the `v_j`.  With

\[
 [f,g]_n:=\sum_{k=0}^n\frac{f_kg_k}{\binom nk},
\]

direct counting yields

\[
 \operatorname{per}(T)=3![f,g]_3,
 \qquad
 \operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}=6![f^2,g^2]_6.
\]

Thus (1) is equivalent to `[f^2,g^2]_6 <= [f,g]_3^2`.  The independent
builder and referee audits prove this inequality by two different exact
quadratic-discriminant calculations; see `audit/agents/` and
`experiments/builder_verify_n3.py`.

## Computational disclosure

No proof assistant was used.  Exact symbolic programs verify the displayed
polynomial identities, but the proof consists of the finite identities
(6), (8), and the explicit projective case split above.
