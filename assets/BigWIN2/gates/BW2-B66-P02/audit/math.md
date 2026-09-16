# Fresh mathematical referee report

**Job:** `win-00066-p02-referee-7a0de3eb7671`  
**Snapshot:** `78f13812c20c2932e4184a64e78a3fb00f12c84685f6657c142f022a218613ce`  
**Verdict:** **accept**

## Frozen scope and integrity

I reviewed the exact `resolution-paper` statement in `claim.json`: the minimum
order is ten, all admissible presentations below ten are exact, and the three
listed presentations are precisely the non-exact graph-isomorphism classes at
order ten, with no repeated presentation orbit. I did not weaken this scope.

All six file hashes in `audit/snapshot.json` match the files reviewed. I also
recomputed the canonical SHA-256 digest of the snapshot's sorted compact file
map and obtained the displayed snapshot digest. The hash of `source.md` remains
`a68a5a4013b8f9b46447c7c39f4fc25a057355b6db8e45ef07b3ce7db0f5f614`.

## Reconstruction of the decisive argument

1. By the classification of finite Abelian groups, every noncyclic Abelian
   group of order at most nine has exponent at most four. The cyclic groups of
   orders two through four do as well. Corollary 4.7 of the supplied primary
   paper states, with the same uniform directed-step and uniform-pair
   normalization, that every Cayley graph over a group of exponent at most four
   satisfies
   \(\lambda_2=\operatorname{SDP}_{\rm GL}=\psi\). The only cases below ten
   not covered by that corollary are therefore the cyclic groups of orders five
   through nine.

2. For a cyclic group, translating a feasible squared-Euclidean semimetric and
   averaging over all translations preserves squared-Euclidean feasibility,
   every triangle inequality, and both objective averages. Thus an optimum can
   be taken translation invariant. A symmetric translation-invariant squared
   Euclidean semimetric on \(\mathbb Z_n\) has the Fourier form
   \[
   f(t)=\sum_{k=1}^{\lfloor n/2\rfloor}b_k
   (1-\cos(2\pi kt/n)),\qquad b_k\geq0.
   \]
   The all-pairs denominator is \(\sum_k b_k\), and the remaining metric
   constraints are the finitely many linear inequalities
   \(f(a)+f(b)-f(a+b)\geq0\). Normalizing the positive denominator to one
   therefore turns the GL infimum into a finite linear program. There is no
   limiting or compactness gap: the feasible Fourier weights lie in a closed
   subset of the simplex.

3. For each rational-certificate case, the stored identity
   \(c-Lw=\sum\lambda_{a,b}R_{a,b}+\sum\mu_i e_i\), with all multipliers
   nonnegative, gives \(N_G(f)\geq L D(f)\) for every translated GL-feasible
   metric. This lower bound deliberately uses only triangle inequalities and
   nonnegativity, so omitting the negative-type constraints cannot invalidate
   it. Exhaustive cut enumeration supplies a nontrivial cut metric with ratio
   \(L\), proving equality rather than merely a lower bound.

4. The four balanced complete-multipartite cases are handled without Fourier
   assumptions. If the graph has \(p\) equal independent parts, the mean
   squared distance across distinct parts is at least the mean within a part,
   by the centroid/variance identity. The graph numerator is the former and
   the all-pairs denominator is their convex combination, hence
   \(N_G(d)\geq D(d)\). For a cut with part counts \(a_i\) and total \(a\),
   \(p|\partial A|-(p-1)a(n-a)=p\sum_i a_i^2-a^2\geq0\). Choosing one vertex
   in every part attains equality. Thus all four cases have exact value one.

5. The four order-ten Fourier certificates include the three proposed gaps and
   one further exact case. Each listed primal weight vector is nonnegative,
   sums to one, obeys all one hundred ordered triangle constraints, and attains
   the stated objective. Each listed dual identity has nonnegative triangle
   and Fourier-weight multipliers and proves the matching lower bound. Hence
   the exact GL values of the three non-exact cases are
   \[
   \frac34,\qquad \frac{15+\sqrt5}{22},\qquad
   \frac{10+\sqrt5}{15}.
   \]
   Exhaustive exact cut enumeration gives respectively
   \(4/5,4/5,5/6\). Strictness follows from
   \(13>5\sqrt5\) and \(5>2\sqrt5\), whose positive sides may be squared.

6. Every inverse-closed generating subset of \(\mathbb Z_n\) is enumerated,
   and multiplication by every unit gives exactly the group-automorphism
   equivalence relation. The orbit counts for \(n=5,6,7,8,9,10\) are
   \(2,5,3,8,6,16\). Thus the exact certificates cover every residual
   presentation, not merely selected graphs. At order ten there is no other
   Abelian group type. The sixteen exact integer adjacency characteristic
   polynomials are pairwise distinct, which is sufficient to rule out every
   graph-isomorphism collision between different presentation-orbit
   representatives. Consequently the three gaps are three distinct graph
   classes and none has a second inequivalent order-ten Abelian Cayley
   presentation.

These steps prove exactness at every smaller order, exhibit strict gaps at
order ten, and supply the full order-ten classification required by the frozen
source. Therefore the minimum is exactly ten.

## Checks and falsification attempts performed

- I ran `python3 evidence/exact_cyclic_gl.py` from the project directory. It
  completed without an assertion failure, checked all forty cyclic presentation
  orbits from orders five through ten, printed the exact cut and GL values for
  each, found exactly the three claimed non-exact cases, and verified sixteen
  distinct order-ten characteristic polynomials.
- I separately re-enumerated inverse-closed generating subsets using a direct
  combinations-based implementation. It reproduced the orbit counts
  \(2,5,3,8,6,16\).
- As a separate attack on the order-ten classification, I implemented the
  Fourier triangle LP and cut enumeration without importing the submitted
  verifier. It reproduced the three claimed gaps and no others. A direct
  pairwise graph-isomorphism test on the sixteen representatives found zero
  collisions. This floating-point LP run is corroboration only; the verdict
  rests on the exact submitted identities and exact cut enumeration.
- I checked the cut/complement enumeration convention: every nontrivial cut has
  exactly one representative omitting vertex \(n-1\), and the directed
  generator count from the selected side counts each undirected boundary edge
  once, including involution generators.
- I attacked the normalization and degeneracy points. A nontrivial cut has
  positive denominator; a GL metric is normalized only when its all-pairs
  denominator is positive; zero distances between distinct vertices cause no
  problem. The translation average preserves numerator and denominator because
  both measures are uniform and the graph is Cayley.
- I inspected Corollary 4.7 and Section 6.4 of the supplied paper. Corollary 4.7
  has the exact exponent-at-most-four conclusion used here. Section 6.4 confirms
  the \(\mathbb Z_{10},\{\pm1,\pm3\}\) seed values \(3/4\) and \(4/5\), but
  does not supply the candidate's minimum-order proof or full order-ten
  classification.

## Contribution and remaining gaps

The result meets the frozen full-resolution scope. The exact cyclic exhaustion,
two additional order-ten gap classes, and graph-isomorphism separation provide
the missing minimum and classification beyond the cited paper's seed example.
The limited literature comparison in `problem.md` does not establish priority,
and the claim appropriately disclaims a broader priority assertion. This does
not leave a mathematical gap in the resolution.

I found no unresolved hypothesis, quantifier, exactness, coverage, or
classification defect. The frozen candidate is accepted as stated.
