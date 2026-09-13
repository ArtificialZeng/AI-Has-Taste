# Proof-builder notes: cut frames and the sparse-gap obstruction

Date: 2026-08-29  
Role: independent proof builder  
Scope: structural reduction and positive obstructions for eleven equilateral
points in \(\ell_1^5\).  Nothing below claims to settle the full problem or
to be novel relative to the literature audit.

## 1. Normalization and compactness

Let \(p_1,\ldots,p_m\in\mathbb R^n\) be equilateral with common distance
\(\delta>0\).  Translation by \(-p_m\) and multiplication by
\(\delta^{-1}\) reduce to

\[
 p_m=0,\qquad \|p_r-p_s\|_1=1\quad(r\ne s).                 \tag{1}
\]

This normalized realization space is compact.  Indeed
\(|p_{rj}|\le \|p_r\|_1=1\), so it is a closed subset of
\([-1,1]^{n(m-1)}\).  Thus limiting configurations and coordinate ties are
already present; no generic-position perturbation is needed or used.

The discrete symmetries used below are simultaneous relabeling of the points,
permutation of coordinates, and reversal of any coordinate.  Coordinatewise
translations and a common positive scale are the continuous normalizations.
Arbitrary rotations are not \(\ell_1\)-isometries.

## 2. Exact coordinate-order and cut-metric reduction

For a fixed coordinate \(j\), choose any total order
\(\pi_j(1),\ldots,\pi_j(m)\) refining the weak order of the values
\(p_{1j},\ldots,p_{mj}\), and put

\[
 g_{j,k}=p_{\pi_j(k+1),j}-p_{\pi_j(k),j}\ge0,
 \qquad S_{j,k}=\{\pi_j(1),\ldots,\pi_j(k)\}.              \tag{2}
\]

For a nonempty proper subset \(S\subset[m]\), write

\[
 \delta_S(r,s)=\mathbf 1\{|\{r,s\}\cap S|=1\}.
\]

Telescoping along the sorted coordinate gives the exact identity

\[
 |p_{rj}-p_{sj}|=\sum_{k=1}^{m-1}g_{j,k}\delta_{S_{j,k}}(r,s). \tag{3}
\]

Consequently (1) is equivalent, branch by branch, to

\[
 \sum_{j=1}^{n}\sum_{k=1}^{m-1}
 g_{j,k}\delta_{S_{j,k}}(r,s)=1
 \quad(1\le r<s\le m),\qquad g_{j,k}\ge0.                 \tag{4}
\]

Conversely, cumulative sums of gaps in (2) reconstruct coordinates from any
solution of (4), so (4) is an equivalence rather than merely a necessary
condition.  A zero gap represents a tie, including tied blocks of arbitrary
size.  A constant coordinate has all gaps zero.  In any feasible branch,
\(\sum_k g_{j,k}\le1\): apply (4) to the two points at the ends of coordinate
\(j\).  Hence each branch is itself a compact rational polytope.

There are finitely many total-order branches.  If one real branch is feasible,
then it has a rational feasible point.  One direct proof is to choose a
feasible point of minimal support.  The supported integer columns of (4) are
linearly independent (otherwise a signed null direction can be followed
until one positive entry vanishes), and a full-rank rational subsystem then
determines the supported gaps rationally.  Thus restricting a counterexample
search to rational points loses nothing.

For a fixed branch with cut-incidence matrix \(A\), Farkas' lemma gives the
equivalent exact alternative

\[
 Ag=\mathbf1,\ g\ge0
 \quad\text{or}\quad
 A^Ty\ge0,\ \mathbf1^Ty<0.                                \tag{5}
\]

Whenever the branch is infeasible, \(y\) may be chosen rational and then
scaled to an integer certificate.  A global positive proof could therefore
be a symmetry-complete finite branch enumeration plus independently checked
integer Farkas certificates.  This note does not supply that enumeration.

## 3. Double centering: an exact Parseval cut frame

Let \(z_S\in\{0,1\}^m\) be the indicator of \(S\), let
\(H=I_m-m^{-1}J_m\), and define the centered cut vector

\[
 v_S=Hz_S=z_S-\frac{|S|}{m}\mathbf1\in\mathbf1^\perp.     \tag{6}
\]

As an \(m\times m\) matrix,

\[
 \Delta_S=(\delta_S(r,s))_{r,s}
 =z_S\mathbf1^T+\mathbf1z_S^T-2z_Sz_S^T,
\]
and therefore

\[
 H\Delta_SH=-2v_Sv_S^T.                                  \tag{7}
\]

The distance matrix in (4) is \(J-I\), whose double centering is \(-H\).
Thus every equilateral realization satisfies the exact frame identity

\[
 \boxed{\displaystyle
 \sum_{j,k:g_{j,k}>0}g_{j,k}v_{S_{j,k}}v_{S_{j,k}}^T
 =\frac12H.}                                              \tag{F}
\]

On the \((m-1)\)-dimensional space \(V=\mathbf1^\perp\), the columns

\[
 a_{j,k}=\sqrt{2g_{j,k}}\,v_{S_{j,k}}                     \tag{8}
\]
form a Parseval frame: if \(A\) has these columns, then \(AA^T=I_V\).
In particular, if \(t\) denotes the total number of positive coordinate
gaps (duplicates in different coordinates counted separately), then

\[
 t\ge m-1.                                                \tag{9}
\]

The scalar form, useful for independent checking, is

\[
 \sum_{j,k}g_{j,k}\left(\sum_{r\in S_{j,k}}c_r\right)^2
 =\frac12\sum_{r=1}^m c_r^2
 \quad\text{whenever }\sum_r c_r=0.                       \tag{10}
\]

No square roots are needed in (F) or (10); they are introduced only to use
standard Parseval-frame notation.

## 4. First sparse-stratum theorem for \(m=11,n=5\)

### Intermediate theorem

If eleven points form an equilateral set in \(\ell_1^5\), then the sum of
the numbers of positive consecutive gaps across the five sorted coordinates
is at least twelve:

\[
 \sum_{j=1}^5(q_j-1)=t\ge12,                              \tag{11}
\]

where \(q_j\) is the number of distinct values in coordinate \(j\).
Equivalently,

\[
 \sum_{j=1}^5 q_j\ge17.                                  \tag{12}
\]

In particular no such realization can have at most three distinct values in
every coordinate, and more generally the entire stratum
\(\sum_j(q_j-1)\le11\) is impossible.

### Proof

For two nonempty proper subsets \(S,T\subset[11]\), put
\(s=|S|\), \(t'=|T|\), and \(u=|S\cap T|\).  From (6),

\[
 \langle v_S,v_T\rangle=u-\frac{st'}{11}
 =\frac{11u-st'}{11}.                                    \tag{13}
\]

This cannot vanish: vanishing would imply \(11\mid st'\), whereas
\(1\le s,t'\le10\).  This includes repeated cuts, for which the inner
product is their positive squared norm.

By (9), \(t\ge10\).  If \(t=10=\dim V\), then the square Parseval matrix in
(8) is orthogonal, so distinct columns are orthogonal.  This contradicts
(13).  Hence \(t\ge11\).

Suppose next that \(t=11=\dim V+1\).  Let \(P=A^TA\).  Since \(AA^T=I_V\),
\(P\) is an orthogonal projection of rank ten on \(\mathbb R^{11}\).
Its one-dimensional kernel is spanned by a unit vector \(b\), and hence

\[
 P=I_{11}-bb^T.                                           \tag{14}
\]

For distinct column indices \(r,s\), (13) and positivity of the gaps imply
\(P_{rs}=\langle a_r,a_s\rangle\ne0\), so every \(b_r\ne0\).  For any
three distinct indices \(r,s,u\), (14) yields

\[
 P_{rs}P_{ru}P_{su}
 =(-b_rb_s)(-b_rb_u)(-b_sb_u)
 =-b_r^2b_s^2b_u^2<0.                                    \tag{15}
\]

On the other hand, any three positive gaps from one coordinate have strictly
nested prefix cuts \(S\subset T\subset U\).  For nested nontrivial cuts,

\[
 \langle v_S,v_T\rangle
 =|S|-\frac{|S||T|}{11}
 =\frac{|S|(11-|T|)}{11}>0,                               \tag{16}
\]

and similarly for the other two pairs.  The positive scale factors in (8)
do not change signs, so their three Gram entries have positive product,
contradicting (15).  Thus, under the assumption \(t=11\), each of the five
coordinates could contain at most two positive gaps.  That would give
\(t\le10\), the final contradiction.  Therefore \(t\ge12\), and
\(q_j-1\) equals the number of positive gaps in coordinate \(j\), proving
(11)--(12).  All tie and constant-coordinate cases were included. \(\square\)

## 5. Naimark-complement refinement for the next strata

The following exact lemma records more of the same structure, although it
does not by itself close the full problem.

### Lemma (chain length versus frame excess)

For an equilateral \(m\)-point realization whose cut frame has \(t\) positive
gaps, let \(d=m-1\) and \(q=t-d\).  Then every single coordinate has at most
\(q+1=t-m+2\) positive gaps.

### Proof

For the Parseval matrix \(A\), let \(P=A^TA\) and \(Q=I_t-P\).  Then \(Q\)
is a positive-semidefinite orthogonal projection of rank \(q\), so choose
vectors \(y_1,\ldots,y_t\in\mathbb R^q\) with
\(Q_{rs}=\langle y_r,y_s\rangle\).  For two distinct gaps in the same
coordinate, their prefix cuts are nested, so (16) gives \(P_{rs}>0\), whence

\[
 \langle y_r,y_s\rangle=Q_{rs}=-P_{rs}<0.                 \tag{17}
\]

A collection of \(h\) nonzero vectors with all pairwise inner products
strictly negative in \(\mathbb R^q\) has \(h\le q+1\).  If a coordinate has
at least two positive gaps, (17) also shows that none of its corresponding
complement vectors is zero; if it has only one gap, the desired bound is
immediate.  For completeness,
any linear dependence among such vectors cannot have both positive and
negative coefficients: equating the two nonempty positive combinations and
taking their mutual inner product would identify a nonnegative squared norm
with a strictly negative number.  Hence the kernel of their Gram matrix has
dimension at most one (two independent one-signed dependences can be
combined to create mixed signs).  Its rank is at least \(h-1\), and so
\(h-1\le q\).  Applying this to (17) proves the lemma. \(\square\)

For \(m=11\), the first unresolved gap count at this stage is \(t=12\),
where \(q=2\).  The lemma forces each coordinate to have at most three
positive gaps.  Hence the sorted multiset of five per-coordinate gap counts
must be one of

\[
 (3,3,2,2,2),\quad(3,3,3,2,1),\quad(3,3,3,3,0).           \tag{18}
\]

This is a finite-stratum restriction at this stage.  Section 6 below uses a
spectral-deficit argument to eliminate this stratum, as well as \(t=13,14\).

### Lemma (private rational direction at \(t=12\))

Assume \(m=11,t=12\), and let one coordinate contribute three positive-gap
cuts \(S_1\subset S_2\subset S_3\).  Then:

1. the other nine centered cut vectors are linearly independent;
2. there is a unique line \(\mathbb Ru\subset V\) orthogonal to all those
   nine vectors, and this line has a nonzero rational (hence primitive
   integer) representative;
3. one orientation of \(u\) is constant at four strictly decreasing levels
   on the four ordered blocks cut out by \(S_1,S_2,S_3\);
4. every level block of every other coordinate has \(u\)-sum zero; and
5. if the four successive values of \(u\) are
   \(c_1>c_2>c_3>c_4\), then the three gaps of this coordinate are forced by

   \[
   g_i=\frac{c_i-c_{i+1}}
   {2\sum_{r\in S_i}u_r}\quad(i=1,2,3).                  \tag{19}
   \]

In particular all three gaps are rational under a primitive-integer
normalization of \(u\).  Private directions belonging to two distinct
three-gap coordinates are orthogonal.

To prove the lemma, factor the rank-two Naimark projection as \(Q=Y^TY\).
The three Naimark vectors belonging to the coordinate are pairwise strictly
obtuse.  They span \(\mathbb R^2\): three nonzero vectors on a line cannot
have all three pairwise products negative.  Their dependence space is
therefore one-dimensional, and its nonzero vector can be oriented to have
all coefficients nonnegative by the obtuse-vector argument above.  No
coefficient can vanish: taking the inner product of the dependence with the
corresponding omitted Naimark vector would equate zero with a strictly
negative sum.  Hence all three coefficients are strictly positive.

Vectors \(u\in V\) orthogonal to the other nine frame columns correspond
injectively under \(u\mapsto A^Tu\) to vectors supported on these three
indices in \(\ker Q=\operatorname{range}(A^T)\).  The latter space is exactly
the one-dimensional dependence space of the three Naimark vectors.  Hence
the other nine original cut vectors have rank nine and their orthogonal
complement in \(V\) is one-dimensional.  Since those cut vectors have
rational entries, that line is rational.

Choose the sign of \(u\) so that its three inner products with the coordinate
columns are positive.  Applying the frame identity (F) to \(u\), all other
terms vanish and

\[
 u=2\sum_{i=1}^3g_i\langle v_{S_i},u\rangle v_{S_i}.       \tag{20}
\]

The coefficients in (20) are positive.  In the nested-prefix basis, these
coefficients are precisely the successive drops in the four block values of
\(u\), proving strict decrease.  Comparing coefficients in (20) gives
(19); the prefix sums in its denominators are positive and hence nonzero.

For any other positive-gap cut \(T\), orthogonality says
\(0=\langle v_T,u\rangle=\sum_{r\in T}u_r\).  Successive differences of the
zero prefix sums, together with \(\sum_ru_r=0\), show that every level block
of that coordinate has zero \(u\)-sum.  Finally, a second private direction
is a linear combination of the three cuts in its own coordinate by (20),
all of which are orthogonal to the first private direction; hence the two
private directions are orthogonal. \(\square\)

This lemma converts every three-gap coordinate in the \(t=12\) stratum into
an exact integer zero-sum partition problem.  For two such coordinates, the
\(4\times4\) contingency table of their level blocks has positive row and
column sums totaling eleven, has the first private level vector in its left
kernel and the second in its right kernel, and therefore has rank at most
three.  Rank at most three alone is not contradictory.  For example,

\[
 N=\begin{pmatrix}
 0&1&0&0\\ 2&0&1&1\\ 2&1&1&1\\ 0&1&0&0
 \end{pmatrix},\qquad
 N^T\!\begin{pmatrix}3\\1\\-1\\-2\end{pmatrix}=0,
 \qquad
 N\!\begin{pmatrix}1\\0\\-1/2\\-3/2\end{pmatrix}=0.    \tag{21}
\]

Both displayed null vectors have four strictly decreasing entries; all row
and column sums of \(N\) are positive and the total is eleven.  Any finite
search based on this reduction must therefore retain the full frame
equations, not only the contingency-rank condition.

## 6. Spectral-deficit strengthening: \(t\ge15\)

The Parseval structure gives a stronger exact theorem than (11).

### Theorem

If eleven points form an equilateral set in \(\ell_1^5\), then

\[
 \boxed{t=\sum_{j=1}^5(q_j-1)\ge15,\qquad
 \sum_{j=1}^5q_j\ge20.}                                  \tag{22}
\]

### Step 1: total spectral deficit

Group the Parseval columns (8) by coordinate.  For coordinate \(j\), let
\(A_j\) be its \(10\times\ell_j\) column matrix, where
\(\ell_j=q_j-1\), and let

\[
 G_j=A_j^TA_j,\qquad B_j=A_jA_j^T.
\]

The positive-gap prefix cut vectors in one coordinate are linearly
independent, so \(G_j\) is positive definite when \(\ell_j>0\).  Since
\(\sum_jB_j=I_V\), one has \(0\le B_j\le I_V\); hence every eigenvalue of
\(G_j\) lies in \((0,1]\).  Define its spectral deficit by

\[
 \varepsilon_j=\ell_j-\operatorname{tr}G_j\ge0.           \tag{23}
\]

Taking traces in the Parseval identity gives the exact budget

\[
 \sum_{j=1}^5\varepsilon_j
 =\sum_j\ell_j-\operatorname{tr}(A^TA)=t-10.              \tag{24}
\]

### Step 2: a weight-free deficit bound for one chain

Consider one coordinate with \(\ell\ge1\) positive prefix cuts of sizes
\(1\le k_1<\cdots<k_\ell\le10\).  Normalize their centered indicators to
unit vectors.  Their correlation matrix \(R\) has entries

\[
 R_{ab}=\sqrt{\frac{k_a(11-k_b)}{k_b(11-k_a)}}\quad(a<b). \tag{25}
\]

Writing

\[
 r_i=R_{i,i+1}\in(0,1)\quad(1\le i<\ell),
\]

the nested-cut formula telescopes to

\[
 R_{ab}=r_ar_{a+1}\cdots r_{b-1}.                         \tag{26}
\]

If \(x_i=\|a_i\|^2>0\) for the scaled frame columns in this coordinate and
\(D=\operatorname{diag}(\sqrt{x_i})\), then
\(G=DRD\le I_\ell\).  Put \(x=(x_i)\).  Testing this matrix inequality on
\(D\mathbf1\) gives

\[
 x^TRx\le\mathbf1^Tx.                                    \tag{27}
\]

Cauchy--Schwarz in the \(R\)-inner product then gives

\[
 (\mathbf1^Tx)^2
 \le(x^TRx)(\mathbf1^TR^{-1}\mathbf1)
 \le(\mathbf1^Tx)(\mathbf1^TR^{-1}\mathbf1),
\]

and hence

\[
 \operatorname{tr}G=\mathbf1^Tx
 \le\mathbf1^TR^{-1}\mathbf1.                           \tag{28}
\]

The Markov-form correlation matrix (26) has quadratic inverse form

\[
 y^TR^{-1}y=y_1^2+
 \sum_{i=1}^{\ell-1}\frac{(y_{i+1}-r_i y_i)^2}{1-r_i^2}.
                                                                    \tag{29}
\]

(Expanding (29) directly verifies the inverse, including both endpoints.)
At \(y=\mathbf1\), this yields

\[
 \mathbf1^TR^{-1}\mathbf1
 =1+\sum_{i=1}^{\ell-1}\frac{1-r_i}{1+r_i}.
\]

Combining with (23) and (28) gives the exact, weight-independent lower bound

\[
 \boxed{\displaystyle
 \varepsilon_j\ge
 \sum_{i=1}^{\ell-1}\frac{2r_i}{1+r_i}.}                 \tag{30}
\]

### Step 3: make the bound depend only on \(\ell\)

The product of the adjacent correlations is the endpoint correlation:

\[
 \prod_{i=1}^{\ell-1}r_i
 =\sqrt{\frac{k_1(11-k_\ell)}{k_\ell(11-k_1)}}\ge\frac1{10}. \tag{31}
\]

The last inequality follows just from
\(k_1\ge1\), \(11-k_\ell\ge1\),
\(k_\ell\le10\), and \(11-k_1\le10\).  For
\(f(r)=2r/(1+r)\), the function \(s\mapsto f(e^s)\) is increasing and
strictly convex on \(s<0\), because

\[
 \frac{d^2}{ds^2}f(e^s)=\frac{2e^s(1-e^s)}{(1+e^s)^3}>0.
\]

Jensen's inequality and (31) therefore imply, for \(\ell\ge2\),

\[
 \varepsilon_j\ge
 \frac{2(\ell-1)}{10^{1/(\ell-1)}+1}.                    \tag{32}
\]

For the only chain lengths needed below, use the following exact rational
lower bounds (the inequalities are strict except in the \(\ell=2\) line):

\[
\begin{array}{c|cccccc}
 \ell&0&1&2&3&4&5\\ \hline
 \varepsilon_j\text{ lower bound }c_\ell
 &0&0&\frac2{11}&\frac{24}{25}&\frac{19}{10}&\frac{23}{8}.
\end{array}                                               \tag{33}
\]

Indeed, (32) gives

\[
 \frac4{\sqrt{10}+1}>\frac{24}{25},\qquad
 \frac6{\sqrt[3]{10}+1}>\frac{19}{10},\qquad
 \frac8{\sqrt[4]{10}+1}>\frac{23}{8}.                   \tag{34}
\]

The three comparisons are exact after observing respectively
\((19/6)^2>10\), \((41/19)^3>10\), and \((41/23)^4>10\).

The discrete increments of the rational sequence in (33) are

\[
 0,\quad\frac2{11},\quad\frac{214}{275},\quad
 \frac{47}{50},\quad\frac{39}{40},                       \tag{35}
\]

which are strictly increasing after the initial zero.  Therefore, among
five nonnegative integer chain lengths with fixed sum, \(\sum_jc_{\ell_j}\)
is minimized by distributing the lengths as evenly as possible (the usual
one-unit exchange proves this directly).

### Step 4: exclude \(t=12,13,14\)

The Naimark chain-length lemma in Section 5 says
\(\ell_j\le t-9\).  For \(t=12,13,14\), respectively, (33)--(35) and the
balanced distributions give

\[
\begin{array}{c|c|c|c}
 t&t-10&\text{minimizing lengths}&
 \sum_j\varepsilon_j\text{ lower bound}\\ \hline
12&2&(3,3,2,2,2)&2\frac{24}{25}+3\frac2{11}
   =\frac{678}{275}>2\\
13&3&(3,3,3,2,2)&3\frac{24}{25}+2\frac2{11}
   =\frac{892}{275}>3\\
14&4&(3,3,3,3,2)&4\frac{24}{25}+\frac2{11}
   =\frac{1106}{275}>4.
\end{array}                                               \tag{36}
\]

Each line contradicts the exact total-deficit identity (24).  Sections 3--4
already excluded \(t\le11\), so \(t\ge15\).  Since
\(q_j=\ell_j+1\), equation (22) follows. \(\square\)

This theorem still does not rule out \(t\ge15\).  At the first remaining
stratum \(t=15\), the total deficit is five and the Naimark bound only gives
\(\ell_j\le6\).  The balanced pattern \((3,3,3,3,3)\) is not contradicted by
(32): its lower bound is \(20/(\sqrt{10}+1)<5\).  Thus the present method has
a quantitatively explicit stopping point rather than a hidden inference.

The same calculation nevertheless narrows the \(t=15\) stratum.  Extend
(33) by

\[
 c_6=\frac{193}{50}<\frac{10}{\sqrt[5]{10}+1};            \tag{37}
\]

the strict inequality follows from \((307/193)^5>10\).  The next discrete
increment is \(c_6-c_5=197/200>39/40\), so convexity continues through six.
A one-unit exchange from the balanced pattern shows that the only sorted
five-coordinate gap-count patterns whose lower-bound sum does not already
exceed the budget five are

\[
 (3,3,3,3,3),\qquad(4,3,3,3,2).                          \tag{38}
\]

Their rational lower-bound sums are respectively \(24/5\) and
\(2729/550\), both below five.  A second balancing deviation already costs
\(2818/550>5\), and convexity makes every other partition at least as
expensive.  Thus (38) is a proved reduction, not a claim that either pattern
is feasible.

## 7. Cut-chain formulation and exact certificate route

Each coordinate contributes a chain of nested prefix cuts.  Since
\(\delta_S=\delta_{S^c}\), it is cleaner combinatorially to regard a cut as
an unordered bipartition \(\{S,S^c\}\).  A family belongs to one coordinate
exactly when its cuts can be oriented as a single strictly nested chain;
nonnegative weights then reconstruct that coordinate by cumulative sums.
Thus the target is equivalent to asking whether the uniform metric on eleven
labels has a positive weighted cut decomposition whose cut copies can be
partitioned into five such chains.

For a fixed five-chain order type this is precisely the rational LP (4).
An exhaustive positive proof needs both:

1. a symmetry-complete enumeration of all relevant five-chain order types,
   including zero-gap faces; and
2. for each infeasible branch, an integer-scaled Farkas vector from (5),
   checked independently from the serialized branch.

Zero gaps mean it is enough to enumerate total orders; every weak order is a
face of some total-order branch.  Reversals, coordinate permutations, and a
simultaneous point relabeling are safe symmetry reductions, but any stronger
canonicalization must be proved complete.

## 8. Adversarial checks and killed candidate lemmas

1. **Killed:** “Every minimal \(11\)-cut Parseval decomposition is the
   singleton decomposition.”  Besides the eleven singleton cuts of weight
   \(1/2\), the eleven translates of the quadratic-residue
   \((11,5,2)\) difference set also give a decomposition: each pair is
   separated by six blocks, so weight \(1/6\) on every block gives distance
   one.  Therefore minimal-support classification cannot assume singleton
   cuts.
2. **Not enough:** the rank bound \(t\ge10\) alone ignores the chain
   partition and is far from the target.
3. **Not enough:** the scalar trace identity
   \(\sum g_S|S|(11-|S|)=55\) gives useful diagnostics but no contradiction.
4. **Open fatal gap:** no argument here excludes \(t\ge15\).  In particular,
   the balanced \(t=15\) distribution \((3,3,3,3,3)\) survives every bound
   proved in this note.
5. **Certificate caution:** floating-point LP failure for sampled order types
   would be only diagnostic.  The exact route requires exhaustive coverage
   and rational/integer Farkas certificates.

## 9. Strongest auditable conclusion and limitations

The exact, self-contained strongest result proved here is the sparse-stratum
theorem \(t\ge15\), equivalently \(\sum_jq_j\ge20\), together with the exact
order-type/LP/frame equivalences, the Naimark chain-length lemma, and the
spectral-deficit inequality (30).  This is a nontrivial necessary condition
for an eleven-point counterexample, but it does **not** prove
\(e(\ell_1^5)=10\).  The decisive remaining gap is a global obstruction (or
an exact feasible branch) for configurations with at least fifteen positive
gaps.

No proof assistant was used.  The companion exact-arithmetic script checks
the finite arithmetic core and explicit adversarial examples; the arguments
using rank, Parseval frames, and Naimark complements remain human proofs.
