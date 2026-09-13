# Independent PGL2 and equality audit for the real (n=3) theorem

Date: 2026-08-29  
Scope: only the real (3\times3), rank-at-most-two Marcus gap.  This note was
reconstructed from the permanent definition and a rank factorization; it does
not take the builder's orbit or equality prose as a premise.  No proof
assistant was used.

Write

\[
\mathcal D(T)=20\operatorname{per}(T)^2-
\operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}. \tag{1}
\]

The conclusion of this audit is

\[
\mathcal D(T)=0
\iff
\begin{cases}
\operatorname{rank}T\leq1,\quad\text{or}\\
T\text{ has a zero row or zero column},\quad\text{or}\\
\operatorname{rank}T=2\text{ and, after row/column permutations, }T
\text{ has a }2\times2\text{ zero block}.
\end{cases} \tag{2}
\]

The alternatives overlap; (2) is a union, not a disjoint classification.

## 1. Rank factor maps and zero factors

For rank at most two choose

\[
T=FG^{\mathsf T},\qquad F,G\in\mathbb R^{3\times2}, \tag{3}
\]

and denote their row vectors by (f_i,g_j\in\mathbb R^2).  Thus
(T_{ij}=f_i g_j^{\mathsf T}).

If (\operatorname{rank}T=2), then every such two-column factorization of
(3) has

\[
\operatorname{rank}F=\operatorname{rank}G=2, \tag{4}
\]

because (\operatorname{rank}(FG^{\mathsf T})\leq
\min(\operatorname{rank}F,\operatorname{rank}G)).  Consequently the linear
maps

\[
L_G:f\longmapsto fG^{\mathsf T},\qquad
L_F:g\longmapsto Fg^{\mathsf T} \tag{5}
\]

from (\mathbb R^2) into (\mathbb R^3) are injective.  Hence, in the
rank-two stratum,

\[
f_i=0\iff\text{row }i\text{ of }T\text{ is zero},\qquad
g_j=0\iff\text{column }j\text{ of }T\text{ is zero}. \tag{6}
\]

This is why a zero factor cannot be silently placed in projective space.  It
is a separate matrix-level zero-row or zero-column stratum.  If (T) has a
zero row, then (\operatorname{per}(T)=0), while the doubled matrix has two
zero rows, so its permanent is also zero.  The column case is identical.
Thus every zero-factor stratum in (6) is an equality stratum.

Rank zero and rank one are best removed before projectivizing.  If
(T=xy^{\mathsf T}), then directly from the permanent definition

\[
\operatorname{per}(T)=3!\prod_i x_i\prod_jy_j,
\quad
\operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
=6!\left(\prod_i x_i\prod_jy_j\right)^2
=20\operatorname{per}(T)^2. \tag{7}
\]

Such a matrix has the embedded minimal factorization
(f_i=(x_i,0),g_j=(y_j,0)), whose nonzero factor directions are all
coincident.  A logical warning is necessary: for an *arbitrary nonminimal*
two-column factorization of a rank-one matrix, its row-factor directions need
not all coincide, because the rank-one opposite factor can have a nontrivial
kernel.  Therefore "rank at most one iff all directions coincide" is not
valid for every chosen factorization.  The sound proof treats rank at most
one by (7), and uses the projective classification only after imposing
(\operatorname{rank}T=2), where (4) holds.

## 2. Exhaustion of the nonzero rank-two row strata

Assume from now on that (T) has rank two and no zero row or column.  By
(4)--(6), all (f_i,g_j) are nonzero and each of (F,G) has rank two.

The factor gauge

\[
F\longmapsto FQ,\qquad G\longmapsto GQ^{-\mathsf T},\qquad
Q\in\operatorname{GL}_2(\mathbb R), \tag{8}
\]

leaves (T) unchanged.  On nonzero row factors it induces the full
(\operatorname{PGL}_2(\mathbb R)) action on (\mathbb RP^1).  This action
is bijective, so it preserves which factor directions coincide.

A multiset of three projective points has exactly the partitions

\[
1+1+1,\qquad 2+1,\qquad 3. \tag{9}
\]

The last partition makes all rows of (F) proportional and hence
(\operatorname{rank}F=1), contradicting rank two.  Thus the rank-two,
no-zero-row stratum is exhausted by:

- three distinct row directions; and
- one repeated direction and one different direction (type (2+1)).

There is no fourth affine or projective case.

For three distinct ordered directions, triple transitivity of
(\operatorname{PGL}_2(\mathbb R)) gives a (Q) taking them to

\[
[1:-1],\quad[1:0],\quad[1:1]. \tag{10}
\]

For type (2+1), a projective transformation takes the repeated line and
the singleton line to

\[
[1:0],\quad[1:1]. \tag{11}
\]

After (8), each actual factor vector is a nonzero scalar multiple of the
displayed representative.  Dividing each factor row by that nonzero scalar
amounts to a nonzero row scaling of (T).  Such scalings preserve the zero
set of the gap because a direct homogeneity count gives

\[
\mathcal D(D_rTD_s)=
\left(\prod_i r_i\prod_j s_j\right)^2\mathcal D(T) \tag{12}
\]

for diagonal row and column scales.  Only nonzero row scales are used here;
zero scales were already handled by (6).

Accordingly, up to equality-preserving nonzero row scalings, the two forms
are

\[
T_{ij}=c_j+a_i d_j,qquad
(a_1,a_2,a_3)=(-1,0,1) \tag{13}
\]

and

\[
T_{ij}=c_j+a_i d_j,qquad
(a_1,a_2,a_3)=(0,0,1), \tag{14}
\]

where (g_j=(c_j,d_j)\ne0).  Crucially, no (c_j) has been divided out.
The projective point at infinity is exactly (c_j=0,d_j\ne0), and it
remains inside (13)--(14).  Thus the normal forms have no affine-chart loss.

## 3. The homogeneous identities, rebuilt from the permanent definition

Put

\[
\Delta_{ij}=d_ic_j-c_id_j. \tag{15}
\]

Starting with

\[
\operatorname{per}(A)=\sum_{\sigma\in S_3}
\prod_{i=1}^3 A_{i,\sigma(i)} \tag{16}
\]

and the analogous (6!)-term definition for the doubled matrix, exact
collection of integer-coefficient monomials gives, for (13),

\[
\frac{\mathcal D(T)}{16}
=\Delta_{23}^2(d_1^2+3c_1^2)
+\Delta_{13}^2(d_2^2+3c_2^2)
+\Delta_{12}^2(d_3^2+3c_3^2), \tag{17}
\]

and, for (14),

\[
\frac{\mathcal D(T)}{16}
=\Delta_{12}^2c_3^2+
\Delta_{13}^2c_2^2+
\Delta_{23}^2c_1^2. \tag{18}
\]

I independently reconstructed (17)--(18) with a fresh permutation enumerator
in `experiments/referee_verify_pgl2_equality.py`; it imports no builder or
certificate code.

## 4. Zero set of the distinct-direction identity

Every (g_j=(c_j,d_j)\ne0), so every weight
(d_j^2+3c_j^2) in (17) is strictly positive, including at infinity
(c_j=0).  Therefore

\[
\mathcal D(T)=0\iff
\Delta_{12}=\Delta_{13}=\Delta_{23}=0. \tag{19}
\]

For nonzero vectors in (\mathbb R^2), (19) says that all three (g_j) lie
on one projective line, so (\operatorname{rank}G=1).  This contradicts
(4).  Thus the distinct-row-direction stratum is strict at rank two.

For completeness, counting the points at infinity gives the same conclusion:

- zero vanishing (c_j): (19) is possible only when all three finite
  directions coincide, hence (\operatorname{rank}G=1);
- exactly one vanishing (c_j): an infinite direction cannot coincide with
  either finite direction, so some bracket is nonzero and (17) is positive;
- exactly two vanishing (c_j): the two infinite directions coincide but the
  remaining finite direction does not, so (17) is positive;
- all three vanishing (c_j): every (g_j) is on the infinite line and
  (\operatorname{rank}G=1), giving rank at most one rather than rank two.

## 5. Zero set of the repeated-direction identity

Let

\[
z=\#\{j:c_j=0\}. \tag{20}
\]

Because every (g_j\ne0), a vanishing (c_j) forces (d_j\ne0).
Equation (18) gives the following exhaustive homogeneous case split.

### (z=0)

All three coefficients multiplying the squared brackets in (18) are
positive.  Equality forces all brackets to vanish, hence
(\operatorname{rank}G=1), impossible at rank two.

### (z=1)

After a column permutation take (c_1=0) and (c_2c_3\ne0).  Since
(d_1\ne0),

\[
\Delta_{12}=d_1c_2\ne0,qquad
\Delta_{13}=d_1c_3\ne0. \tag{21}
\]

The corresponding first two summands in (18) are strictly positive.  Thus
equality is impossible.

### (z=2)

After a column permutation take

\[
c_1=c_2=0,qquad c_3\ne0. \tag{22}
\]

Then (\Delta_{12}=0); the other two terms in (18) are killed respectively
by the factors (c_2^2) and (c_1^2).  Thus (\mathcal D(T)=0).  Moreover
(g_1,g_2) lie on the infinite line while (g_3) does not, so
(\operatorname{rank}G=2), exactly as required for the rank-two equality
stratum.

### (z=3)

All column factors lie on the infinite line, so
(\operatorname{rank}G=1) and (\operatorname{rank}T\leq1).  Equality holds
by (7), but this is not a rank-two case.

Consequently, under the rank-two/no-zero-column assumptions, the repeated
normal form has equality **iff exactly two (c_j) vanish**.

## 6. Translation of the SOS zero set to a matrix zero block

In (14) the first two row parameters are zero.  Hence

\[
T_{1j}=T_{2j}=c_j. \tag{23}
\]

Condition (22) is therefore precisely

\[
T_{11}=T_{12}=T_{21}=T_{22}=0 \tag{24}
\]

after the same row and column permutations used to select the repeated row
line and the two infinite column lines.  The nonzero row scalings suppressed
when forming (14) do not change a zero entry.  Thus (22) is a matrix-level
(2\times2) all-zero block, not merely a coordinate artifact.

Conversely, suppose a rank-two (T) with no zero row or column has, after
permutations, the upper-left block (24).  It necessarily has the support form

\[
T=\begin{pmatrix}
0&0&a\\
0&0&b\\
u&v&w
\end{pmatrix}. \tag{25}
\]

No use of the factorization is needed for sufficiency.  In the (3\times3)
permanent, the first two rows of (25) can only use the third column, so no
permutation contributes and

\[
\operatorname{per}(T)=0. \tag{26}
\]

In the doubled (6\times6) matrix, the four row copies coming from the first
two rows can be nonzero only in the two copies of the third column.  Four
distinct rows cannot be matched to only two distinct columns, so its
permanent also vanishes.  Therefore (25) is sufficient for equality.

This explicitly covers the decisive (\operatorname{per}(T)=0) boundary.
At no point was (\operatorname{per}(T)) divided out or normalized.  Other
rank-two matrices with (\operatorname{per}(T)=0) are still controlled by
(17)--(18); zero permanent alone is not asserted to imply equality.

## 7. Exhaustion and final iff

The cases are now exhaustive:

1. rank at most one: equality by (7);
2. rank two with a zero row or column: equality by the zero-row/column
   permanent definition;
3. rank two with no zero row/column and three distinct row directions:
   strict by (17)--(19);
4. rank two with no zero row/column and row type (2+1): equality exactly at
   (22), equivalently exactly when a permuted (2\times2) zero block occurs.

This proves both directions of (2), including zero factors, the factor-map
rank conditions, all projective points at infinity, every value
(z=0,1,2,3), and the (\operatorname{per}(T)=0) equality family.

## 8. Gap report and reproduction

I find no remaining logical gap in the real (n=3) PGL2 reduction or equality
classification, subject to the independently checked polynomial identities
(17)--(18).  The one formulation that must be avoided is the false converse
"rank-one matrix implies all row directions coincide in every nonminimal
two-column factorization."  The rank-first case split above repairs it.

Reproduction command and raw output:

```bash
python experiments/referee_verify_pgl2_equality.py
```

```text
PASS: distinct homogeneous SOS from 3! and 6! definitions
PASS: repeated homogeneous SOS from 3! and 6! definitions
PASS: rank-one and 2x2-zero-block sufficiency families
```
