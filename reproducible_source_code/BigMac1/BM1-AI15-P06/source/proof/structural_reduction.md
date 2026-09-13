# Exact structural reduction and spectral sparse-stratum obstruction

All statements in this note are over the real numbers and use exact
arithmetic.  Numerical search is not used.

## 1. Five weighted paths

Let \(x_1,\ldots,x_m\in\mathbb R^d\).  Sort the values in coordinate \(k\)
as

\[
x_{\pi_k(1),k}\le\cdots\le x_{\pi_k(m),k}
\]

and put
\(g_{k,t}=x_{\pi_k(t+1),k}-x_{\pi_k(t),k}\ge0\).  If
\(C_{k,t}=\{\pi_k(1),\ldots,\pi_k(t)\}\), then telescoping gives

\[
 |x_{r,k}-x_{s,k}|=
 \sum_{t=1}^{m-1}g_{k,t}\,\delta_{C_{k,t}}(r,s),
\]

where \(\delta_C(r,s)=1\) exactly when the cut \(C\mid C^c\) separates
\(r\) and \(s\).  Thus an equilateral \(m\)-set in \(\ell_1^d\), normalized
to distance one, is exactly a representation of the discrete metric on
\([m]\) as a nonnegative sum of the cut metrics from \(d\) chains.  Zero
gaps cover all ties, so this is an equivalence without a genericity
assumption.  Conversely, cumulative sums of the gaps reconstruct the
coordinates.

Every fixed choice of the \(d\) orders is a rational linear feasibility
problem.  A nonempty rational polyhedron contains a rational point (for
example a basic feasible point after standard-form conversion).  Therefore
a real counterexample to the target exists if and only if a rational one
does.

## 2. Tight-frame identity

Let \({\bf 1}\in\mathbb R^m\),
\(H=I_m-m^{-1}{\bf 1}{\bf 1}^{\mathsf T}\), and
\(v_C=H{\bf 1}_C\).  Retain only the \(q\) cuts whose gaps are positive,
and enumerate them as \((C_a,g_a)\), \(1\le a\le q\).  The standard
double-centering identity for squared Euclidean distances gives

\[
 \sum_{a=1}^q g_a v_{C_a}v_{C_a}^{\mathsf T}=\frac12 H. \tag{F}
\]

For completeness, map label \(r\) to the vector with components
\(\sqrt{g_a}\,{\bf1}_{C_a}(r)\).  Its squared Euclidean distance from label
\(s\) is precisely the cut-metric sum, hence one.  The centered Gram matrix
of \(m\) points with off-diagonal squared distances one is
\(-\tfrac12H(J-I)H=\tfrac12H\), which proves (F).

Since the right side of (F) has rank \(m-1\), necessarily \(q\ge m-1\).

## 3. The eleven-point sparse-stratum theorem

**Theorem.**  If eleven points form an equilateral set in any
\(\ell_1^d\), and \(q\) is the total number of positive consecutive gaps
over the \(d\) sorted coordinates, then either

\[
q\ge12
\]

or \(d\ge6\).  In particular, a putative eleven-point equilateral set in
\(\ell_1^5\) has \(q\ge12\).  Equivalently, if coordinate \(k\) assumes
\(r_k\) distinct values, then

\[
\sum_{k=1}^5(r_k-1)\ge12,
\qquad\text{so}\qquad \sum_{k=1}^5r_k\ge17.
\]

**Proof.**  Rank in (F) gives \(q\ge10\).  For nonempty proper subsets
\(C,D\subset[11]\),

\[
 \langle v_C,v_D\rangle
 =|C\cap D|-\frac{|C||D|}{11}. \tag{1}
\]

This is never zero: otherwise \(11|C\cap D|=|C||D|\), impossible because
11 is prime and \(1\le|C|,|D|\le10\).

If \(q=10\), the ten vectors \(\sqrt{g_a}v_{C_a}\) in the ten-dimensional
space \({\bf1}^{\perp}\) would, by (F), be a scaled orthonormal basis.  This
contradicts (1).

Suppose \(q=11\).  Let \(U\) have the eleven vectors
\(u_a=\sqrt{2g_a}v_{C_a}\) as columns, after choosing an orthonormal basis of
\({\bf1}^{\perp}\).  Then \(UU^{\mathsf T}=I_{10}\), so its Gram matrix is
the rank-ten orthogonal projection

\[
 U^{\mathsf T}U=I_{11}-zz^{\mathsf T}
\]

for a unit vector \(z\).  Equation (1) says no two columns are orthogonal;
hence every \(z_a\ne0\).  For every three distinct columns,

\[
 \langle u_a,u_b\rangle
 \langle u_b,u_c\rangle
 \langle u_c,u_a\rangle
 =-z_a^2z_b^2z_c^2<0. \tag{2}
\]

But three positive gaps from one coordinate give three nonempty proper
nested prefix sets \(A\subset B\subset C\).  Every pair has positive inner
product, because for \(A\subset B\),

\[
 \langle v_A,v_B\rangle
 =|A|\left(1-\frac{|B|}{11}\right)>0.
\]

Their triple product is positive, contradicting (2).  Thus at most two of
the eleven positive gaps can come from any one coordinate.  Consequently
\(q\le2d\).  For \(d=5\), this says \(q\le10\), contradicting \(q=11\).
Therefore \(q\ge12\).  More generally the same argument shows that
\(q=11\) forces \(d\ge6\).  Finally, coordinate \(k\) has exactly
\(r_k-1\) positive consecutive gaps.  This proves the asserted equivalent
form. \(\square\)

The dimension conclusion is sharp: eleven of the twelve points
\(\{\pm e_1,\ldots,\pm e_6\}\subset\ell_1^6\) are equilateral of common
distance two and have exactly eleven positive coordinate gaps.  The literal
integer data are serialized in `certificate/equilateral_witnesses.json`.

### Naimark-complement refinement

More generally, let \(q\) be the total number of positive gaps for an
equilateral \(m\)-set, and put \(r=q-(m-1)\).  Every one coordinate contains
at most \(r+1=q-m+2\) positive gaps.  Indeed, after scaling the supported
cut columns as above, their Gram matrix \(P\) is an orthogonal projection of
rank \(m-1\).  The complementary projection \(Q=I-P\) has rank \(r\), so
write \(Q_{ab}=\langle y_a,y_b\rangle\) with \(y_a\in\mathbb R^r\).
Distinct gaps from one coordinate have nested cuts and hence \(P_{ab}>0\),
so their complementary vectors satisfy \(\langle y_a,y_b\rangle<0\).

A family of \(h\) nonzero vectors in \(\mathbb R^r\) with all pairwise inner
products negative has \(h\le r+1\).  To see this, a linear dependence cannot
have both positive and negative coefficients: moving the negative terms to
the other side and taking the inner product of the two positive combinations
would equate a squared norm with a strictly negative number.  The dependence
space therefore has dimension at most one, giving rank at least \(h-1\).
(If a complementary vector is zero, it cannot share a coordinate with a
second gap; the one-vector case already satisfies the bound.)

For the first unresolved value \(m=11,q=12\), one has \(r=2\), so every
coordinate has at most three positive gaps.  Up to coordinate permutation,
the only possible five-coordinate gap-count distributions are

\[
(3,3,2,2,2),\qquad(3,3,3,2,1),\qquad(3,3,3,3,0).
\]

The spectral argument below excludes all three distributions.

## 4. Spectral-deficit strengthening to fifteen gaps

For a putative eleven-point realization in \(\ell_1^5\), let \(\ell_j\) be
the positive-gap count in coordinate \(j\), and put
\(q=\sum_j\ell_j\).  Group the Parseval columns in (F) into matrices \(A_j\)
and set \(G_j=A_j^{\mathsf T}A_j\).  Since
\(0\le A_jA_j^{\mathsf T}\le I\), the spectral deficits

\[
 \varepsilon_j=\ell_j-\operatorname{tr}G_j
\]

are nonnegative, and taking traces gives the exact budget

\[
 \sum_{j=1}^5\varepsilon_j=q-10. \tag{3}
\]

For a chain with \(\ell\) positive prefix cuts, let \(R\) be the correlation
matrix of the normalized centered cut indicators.  Its adjacent
correlations \(r_i\in(0,1)\) have Markov product form and satisfy
\(\prod_i r_i\ge1/10\).  The exact inverse quadratic form of \(R\), followed
by Cauchy--Schwarz and Jensen's inequality, gives

\[
 \varepsilon_j\ge
 \frac{2(\ell_j-1)}{10^{1/(\ell_j-1)}+1}
 \quad(\ell_j\ge2).                                      \tag{4}
\]

The following rational lower bounds suffice:

\[
 c_0=c_1=0,\quad c_2=\frac2{11},\quad c_3=\frac{24}{25},
 \quad c_4=\frac{19}{10},\quad c_5=\frac{23}{8}.          \tag{5}
\]

Their discrete increments are increasing.  Thus, for total gap counts
\(q=12,13,14\), balancing the five chain lengths minimizes the sum of the
right sides, and the exact lower bounds are respectively

\[
 \frac{678}{275}>2,\qquad
 \frac{892}{275}>3,\qquad
 \frac{1106}{275}>4.
\]

Each contradicts (3).  Together with Section 3 this proves the stronger
necessary condition

\[
 \boxed{q\ge15,\qquad\sum_{j=1}^5(\ell_j+1)\ge20.}        \tag{6}
\]

At the first surviving value \(q=15\), the Naimark bound gives
\(\ell_j\le6\).  Adding the exact lower bound \(c_6=193/50\) and performing
the finite convex one-unit exchange leaves only the sorted patterns

\[
 (3,3,3,3,3),\qquad(4,3,3,3,2).                          \tag{7}
\]

The full derivation, including the Markov inverse and radical comparisons,
is in proof/builder_notes.md; experiments/proof_cut_frame_audit.py checks
its finite integer/rational arithmetic.  The linear-algebraic implications
remain a human proof and were independently reconstructed in
audit/referee_round1.md.

## 5. Singleton-compression strengthening through eighteen gaps

Write \(t=q=\sum_j\ell_j\).  Call a supported cut copy singleton if one
side has one label, and let \(R\)
be the number of remaining non-singleton copies.  Subtracting all singleton
terms from (F) gives

\[
 H\operatorname{diag}(c)H
 =\sum_{a=1}^{R}g_av_{S_a}v_{S_a}^{\mathsf T}\succeq0.   \tag{8}
\]

The compression argument in `proof/t16_branch.md` excludes
\(1\le R\le8\).  If some \(c_r=0\), every remaining cut indicator is
constant on the zero set; orienting the cut into its complement and applying
a left inverse expresses a diagonal matrix as a positive sum of binary
rank-one matrices.  Its zero off-diagonal entries force every such binary
vector to be singleton, a contradiction.  If no \(c_r\) vanishes, the
kernel on \({\bf1}^{\perp}\) has dimension at most one, so its rank is at
least nine.

The argument extends to \(R=9\).  In the only additional case, the rank is
exactly nine and

\[
 \sum_{r=1}^{11}\frac1{c_r}=0.
\]

Positive semidefiniteness permits exactly one negative \(c_r\).  The kernel
vector \((1/c_r)_r\) therefore has one negative and ten positive entries and
has no nonempty proper zero-sum subset.  But every remaining proper cut must
be orthogonal to that kernel vector, which is impossible.  Thus no uniform
decomposition has \(1\le R\le9\).

Exact deficit and endpoint-loss comparisons now give the following finite
chain of exclusions.

- At \(t=15\), the two patterns in (7) retain enough singleton endpoints to
  invoke compression.
- At \(t=16\), only \((4,3,3,3,3)\), \((4,4,3,3,2)\), and
  \((5,3,3,3,2)\) survive the deficit bound.  Each has at least eight
  singleton copies, hence \(1\le R\le8\).
- At \(t=17\), only \((4,4,3,3,3)\), \((5,3,3,3,3)\),
  \((4,4,4,3,2)\), \((5,4,3,3,2)\), and \((6,3,3,3,2)\) survive.  Each
  has at least eight singleton copies, hence \(1\le R\le9\).

The detailed rational comparisons are in `proof/t15_dense_branch.md`,
`proof/t16_branch.md`, and `proof/t17_branch.md`.  Their independent reports
and exact finite checkers are in `audit/referee_round2_t15.md`,
`audit/referee_round3_t16.md`, and `audit/referee_round4_t17.md`; the latter
two checkers also pass a genuine-plus-tampered four-mode execution matrix in
`logs/referee_t16_t17_check_matrix.json`.  Consequently every putative
target configuration satisfies

\[
 \boxed{t\ge18,\qquad\sum_{j=1}^5(\ell_j+1)\ge23}.       \tag{9}
\]

At \(t=18\), exact convex deficit costs leave eight of the 88 sorted
five-part gap-count partitions.  An exhaustive endpoint-loss calculation
shows that every survivor retains at least eight singleton copies.  Hence the
number \(R\) of non-singleton copies lies in \([8,10]\); the argument above
excludes \(R\le9\).

The remaining \(R=10\) case has an exact design obstruction.  Fix a reference
label \(p\), orient every non-singleton cut to the side not containing \(p\),
and let \(B\) be the resulting \(10\)-by-\(10\) binary incidence matrix.
In the singleton basis, the compressed identity is

\[
 D+c_pJ=BGB^{\mathsf T},                                \tag{10}
\]

where \(G\) is positive diagonal.  Its off-diagonal entries force every
\(c_p>0\), and hence \(B\) is invertible.  Sherman--Morrison then gives, for
two distinct oriented blocks \(U,V\),

\[
 x(U\cap V)=\lambda x(U)x(V),\qquad
 0<\lambda\sum_{r\ne p}\frac1{c_r}<1.                  \tag{11}
\]

Thus every two blocks intersect, while containment would force
\(1\le\lambda\sum_{r\ne p}1/c_r<1\).  They are therefore pairwise
intersecting and incomparable.  Two cuts from one coordinate chain, however,
become either nested or disjoint when oriented away from \(p\).  Each of the
five coordinates could supply at most one non-singleton copy, contradicting
\(R=10\).

The full exact derivation is in \`proof/t18_branch.md\`; its independent
arithmetic and logic audit is \`audit/referee_round5_t18.md\`.  The separate
cardinality manifest checks all 88 partitions and \(8\cdot3^5=1944\)
endpoint categories.  Therefore the strongest audited structural conclusion
is

\[
 \boxed{t\ge19,\qquad\sum_{j=1}^5(\ell_j+1)\ge24}.       \tag{12}
\]

The compression and frame deductions are human proofs.  The checkers certify
only their stated finite arithmetic and enumeration scopes.

## 6. Two exact comparison subclasses

### Centrally symmetric configurations

If an equilateral set is centrally symmetric, translate its center to zero
and first observe that the center cannot itself be a point of a nontrivial
configuration: if \(0,v\in S\), then symmetry gives \(-v\in S\), while
\(\|v-(-v)\|_1=2\|v\|_1\) contradicts equality with
\(\|v-0\|_1=\|v\|_1\).  Hence write
\(S=\{\pm v_1,\ldots,\pm v_s\}\).  The antipodal pairs imply
\(\|v_i\|_1=\delta/2\).  For \(i\ne j\), equality in the \(\ell_1\)
triangle inequality for both \(v_i-v_j\) and \(v_i+v_j\) forces
\(v_{i,k}v_{j,k}\le0\) and \(v_{i,k}v_{j,k}\ge0\), respectively, in every
coordinate.  Hence the supports of the \(v_i\) are pairwise disjoint and
\(s\le d\).  Therefore every centrally symmetric equilateral set in
\(\ell_1^d\) has at most \(2d\) points.  Equality forces singleton supports,
so, up to the elementary \(\ell_1\)-isometries and scaling, it is the
coordinate cross polytope.

The same equality conditions also show directly that the ten-point
coordinate cross polytope in \(\ell_1^5\) cannot be extended by an eleventh
point while retaining common distance two.  Indeed, if \(x\) had distance
two from both \(e_i\) and \(-e_i\), subtracting the two equations gives
\(|x_i-1|=|x_i+1|\), hence \(x_i=0\) for every \(i\); but the origin has
distance one, not two, from each \(\pm e_i\).

### At most two levels per coordinate

Suppose coordinate \(k\) assumes at most two values, with level difference
\(w_k\ge0\).  Encode the level of point \(r\) by a sign
\(\varepsilon_{r,k}\in\{-1,1\}\) and set
\(u_r=(\sqrt{w_k}\varepsilon_{r,k})_{k=1}^d\).  Then

\[
 \|u_r-u_s\|_2^2=4\|x_r-x_s\|_1.
\]

Thus the \(u_r\) form a Euclidean equilateral set in at most \(d\)
dimensions, which has size at most \(d+1\).  In particular this subclass
cannot contain eleven points in dimension five.

## Limitation

The combined structural theorem does not rule out branches with nineteen or
more positive gaps and therefore does not prove \(e(\ell_1^5)=10\).  The
next rank boundary at \(R=11\) is not covered by the audited theorem.  The
two comparison subclasses likewise do not cover arbitrary
configurations.
