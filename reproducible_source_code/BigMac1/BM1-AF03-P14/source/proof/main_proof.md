# Complete local-extremum classification for central sections of \(Q_5\)

## Theorem

Let
\[
Q_5=[-1/2,1/2]^5,
\qquad
\sigma(v)=\mathcal H^4(Q_5\cap v^\perp),\quad v\in S^4.
\]
Up to independent sign changes and coordinate permutations, the locally
extremal directions are exactly
\[
d_1=(1,0,0,0,0),\qquad
d_2=(1,1,0,0,0)/\sqrt2,\qquad
d_5=(1,1,1,1,1)/\sqrt5.
\]
Here \(d_1\) is a strict local minimum, while \(d_2\) is a global
maximum and \(d_5\) is a strict local maximum.  In particular, every locally
extremal central hyperplane section of \(Q_5\) is diagonal.

More precisely, the full-support critical directions are exactly \(d_5\) and
\[
v_\alpha={1\over\sqrt{2\alpha^2+3}}(\alpha,\alpha,1,1,1),
\qquad
\alpha={24+\sqrt{69}\over13}.
\]
The latter direction is a saddle.  The only support-four non-diagonal
critical orbit is \((1,1,2,2,0)/\sqrt{10}\), and it too is a saddle.

## 1. Exact section formula and regularity

For a positive support vector \(a=(a_1,\ldots,a_s)\), put
\(R=\|a\|_2\), \(A=\sum_i a_i\), and \(a_E=\sum_{i\in E}a_i\).  Coarea,
followed by inclusion--exclusion for the distribution of a sum of independent
uniform variables, gives
\[
F_s(a)={R\over (s-1)!\prod_i a_i}
\sum_{E\subseteq[s]}(-1)^{|E|}
\left({A\over2}-a_E\right)_+^{s-1}.                 \tag{1}
\]
This is scale invariant, and it equals \(\sigma(a/R)\) when the other
coordinates of the normal vanish.  A derivation from the defining section
measure is given in `proof/agent_builder_report.md`, Section 2, and is
independently checked by `src/builder_verify_formulas.py`.

For \(s=5\), pairing complementary subsets in (1) gives, with
\(T=A/2\), \(S=R^2\), \(L_{ij}=T-a_i-a_j\), and
\(\psi(x)=x|x|^3\),
\[
P=T^4-\sum_i(T-a_i)^4+\sum_{i<j}\psi(L_{ij}),
\qquad
F_5(a)={\sqrt S\,P\over24\prod_i a_i}.             \tag{2}
\]
Since \(\psi\in C^3\), the full-support section function is \(C^3\) across
every pair-sum wall.  In a fixed chamber with high-pair set
\(N=\{ij:L_{ij}<0\}\),
\[
P_N=T^4-\sum_i(T-a_i)^4+\sum_{i<j}L_{ij}^4
       -2\sum_{ij\in N}L_{ij}^4.                  \tag{3}
\]
No wall form is divided out in what follows.

If \(a_0\ge\sum_{i>0}a_i\), direct parametrization gives
\(F_5(a)=R/a_0\).  In the full-support region its logarithmic derivative in
each coordinate \(a_j\), \(j>0\), is \(a_j/S>0\); hence neither the dominant
region nor its equality wall contains a full-support critical point.  We may
therefore assume strict balance.

At a balanced positive point, differentiating (2) yields the homogeneous
critical equations
\[
G_i=a_iS P_i+(a_i^2-S)P=0,\qquad 0\le i\le4.       \tag{4}
\]
Euler homogeneity makes one equation dependent.  Thus one may set \(a_4=1\)
and solve four polynomial equations without losing a positive projective
solution.

## 2. Exhaustion of the full-support chambers and walls

Order the coordinates \(a_0\ge\cdots\ge a_4>0\).  The strict high-pair graph
\(N\) is shifted: replacing an endpoint by a lower index cannot decrease a
pair sum.  It is also intersecting, because two disjoint high pairs would
already sum to more than \(2T=\sum_i a_i\), leaving a positive fifth
coordinate.  Every shifted intersecting graph on five ordered vertices is
one of
\[
\varnothing,\quad
\{01\},\quad
\{01,02\},\quad
\{01,02,03\},\quad
\{01,02,03,04\},\quad
\{01,02,12\}.                                     \tag{5}
\]
These are called empty, star1, star2, star3, star4, and triangle.

This also covers walls.  Indeed, every point of the finite pair-sum
hyperplane arrangement is in the closure of a full-dimensional chamber.
Choose a generic sequence converging to it inside the positive balanced cone;
after passing to a subsequence and permuting equal limiting coordinates, the
sequence has one of the six sign graphs in (5).  Because (2) is \(C^3\), a
critical point on the wall satisfies the polynomial extension (4) from that
closure.  Singleton balance walls were already excluded above.

The exact chamber results are:

| ordered chamber/closure | exact outcome | certificate and verifier |
|---|---|---|
| empty closure | only \(a_0=\cdots=a_4\) | `results/empty_highpair_classification_certificate.json`; `src/verify_empty_highpair_classification.py` |
| star1 closure | only \((\alpha,\alpha,1,1,1)\) | `certificates/star1_exact_certificate.json`; `src/builder_verify_star1.py` |
| star2 closure | no critical point | `results/star2_bernstein_no_go_certificate.json`; `src/verify_star2_bernstein.py` |
| star3 closure | no critical point | `certificates/star3_decomposition.json`; `src/builder_verify_star3.py` |
| star4 interior | no critical point; its pair-wall boundary lies in an earlier star closure | `results/breaker_star4_certificate.json`; `src/breaker_star4_verify.py` |
| triangle closure | no critical point | `results/triangle_highpair_no_go_certificate.json`; `src/verify_triangle_highpair_no_go.py` |

For clarity, the decisive exact arguments are summarized next.

* In the empty closure, every coordinate is a root of one common nonzero
  quartic.  The one-, two-, three-, and four-distinct-value cases are exhausted
  using exact divided differences, resultants, Vieta relations, and rational
  Sturm chains.  Only the one-value solution remains.
* In star1 gap coordinates, a degree-nine simplex-Bernstein identity for
  \(-6H_x+7H_y-8H_z+4H_w\) forces \(x=z=0\).  The remaining exact ideal has
  five radical graph components of degrees \(2,2,2,3,6\).  Four violate
  \(u,w\ge0\); the fifth is
  \(w=0\), \(52u^2-36u-15=0\), whose unique nonnegative root gives
  \(\alpha=u+3/2=(24+\sqrt{69})/13\).
* In star2, a fixed linear combination of the four cleared logarithmic
  derivatives has 1125 strictly positive degree-eight Bernstein coefficients
  on an exact product-simplex chart.  This contradicts simultaneous
  criticality, including its closure.
* The saturated star3 ideal is radical of degree 14 and decomposes into four
  explicit components of degrees \(2,4,4,4\).  Rational isolating intervals
  show that every positive real component root violates
  \(a_0\ge\cdots\ge a_4=1\).
* Six exact ideal consequences reduce star4 to equality patterns among its
  four leaves.  The final all-equal-leaf branch is excluded on \([2,\infty)\)
  by a rational Sturm chain.  If the smallest star edge becomes a wall, the
  point belongs to the star3 closure; every other pair-wall degeneration is
  similarly covered by a shorter-star closure.
* In the triangle closure, a saturated exact basis reduces the semialgebraic
  problem to two factors.  One has no real zero; the other contradicts the
  weak high-edge inequality.  No strict inequality is used, so all incident
  pair and singleton walls are included.

Each listed verifier rebuilds (3)--(4) from the chamber graph rather than
importing discovery output.  The certificates use rational/integer
polynomials, exact ideal membership or Bernstein identities, and rational
Sturm or algebraic sign tests.  Their separate mutation suites reject altered
graphs, coefficients, factors, endpoints, and semantic claims.  Consequently
(5) and the table prove the asserted exhaustive full-support critical list.

At \(v_\alpha\), the tangent representation splits under
\(S_2\times S_3\) into a large-block difference, two small-block differences,
and a block-contrast line.  Exact reduction modulo
\(13\alpha^2-48\alpha+39=0\) gives negative quadratic forms on the first two
summands and a positive form on the last.  Thus \(v_\alpha\) is a saddle.
At \(d_5\), the tangent Hessian has four equal eigenvalues
\[
-{5\sqrt5\over32}<0,                               \tag{6}
\]
so \(d_5\) is a strict local maximum.

## 3. Support-deficient directions

If a point of \(S^4\) is a local extremum, its restriction to the coordinate
subsphere determined by its support is a local extremum of the corresponding
\(F_s\).  We therefore need only the exact classifications for \(s\le4\).

For \(s=3\), the dominant region again has no positive critical point.  In
the balanced ordered region scale the smallest coordinate to one and call the
others \(a,b\).  With
\[
P=T^2-\sum_{q\in\{a,b,1\}}(T-q)^2,
\]
the two cleared logarithmic derivatives \(H_a,H_b\) satisfy
\[
\operatorname{Res}_a(H_a,H_b)
=-64b^7(b-1)^8(b^2+1)(b^2+b+1)^3.                 \tag{7}
\]
Positivity forces \(b=1\), after which
\[
H_a=-2a^2(a-1)^2,\qquad H_b=a^3(a-1)^2,
\]
so \(a=1\).  For \(s=2\), the ordered positive formula is \(R/a_0\)
away from the equality point; it has no interior critical point.  These
computations leave only diagonal directions in supports at most three.  The
serialized check is `results/q3_classification_certificate.json`, independently
reconstructed by `src/verify_q3_classification.py`.

For \(s=4\), the complete exact rational branch proof in
`proof/agent_builder_report.md`, Section 3.1--3.2, reconstructs the last known
baseline and gives all critical directions: the diagonal directions and
\[
p=(1,1,2,2)/\sqrt{10}.                             \tag{8}
\]
The tangent Hessian eigenvalues at (8) are
\[
-{5\sqrt{10}\over12},\qquad
-{25\sqrt{10}\over24},\qquad
 {5\sqrt{10}\over24},                             \tag{9}
\]
so its embedding \((p,0)\) is already a saddle inside its support subsphere.
The separate file `results/breaker_q4_baseline_certificate.json`, checked by
`src/breaker_verify_q4_baseline.py`, certifies the rational tangent form and
the saddle signature in (9) only.  It is not used as a certificate of the
preceding exhaustion; that conclusion depends on the explicit branch proof
in `proof/agent_builder_report.md`, Section 3.

It remains to type the diagonal support strata in the ambient \(Q_5\).

* Near \(d_1\), the largest coordinate dominates and \(F_5=1/a_0\) on the
  unit sphere.  Hence \(d_1\) is a strict local minimum.
* \(d_2\) is a global maximum by the sharp cube-slicing theorem.
* The support-three path \((1+u,1+u,1-2u,0,0)\) has
  \[
  F_3={3\sqrt3(2u+1)\sqrt{2u^2+1}\over4(1+u)^2}
     ={3\sqrt3\over4}+{3\sqrt3\over2}u^3+O(u^4), \tag{10}
  \]
  so \(d_3\) is a saddle.
* The support-four Hessian at \(d_4\) is negative definite, but the transverse
  path \((1,1,1,1,t)\), \(t>0\), satisfies
  \[
  F_5={\sqrt{t^2+4}(3t^3-16t^2+128)\over192}
     ={4\over3}+{t^3\over32}+O(t^4).               \tag{11}
  \]
  Thus \(d_4\) has both decreasing and increasing nearby directions and is a
  saddle.
* Equation (6) makes \(d_5\) a strict local maximum.

Together with the full-support classification, this proves the theorem.

## 4. Computer-assistance boundary

No Lean, Coq, Isabelle, or other interactive proof assistant was used.  The
finite algebraic parts use exact rational polynomial arithmetic, Singular
Gröbner-basis/ideal-membership computations, SymPy exact reconstruction, and
standard-library rational Sturm and Bernstein verification.  Numerical root
searches were used only during discovery and are not inputs to any decisive
verifier.
