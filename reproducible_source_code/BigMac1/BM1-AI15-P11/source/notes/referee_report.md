# Gate 5 independent referee report

Date: 2026-08-29 (Asia/Shanghai)

Scope: independent reconstruction of the definitions, the deletion and rooted
recurrences, and the triple-valley criterion.  This report does not assume the
conjecture or its negation, does not audit novelty, and does not promote any
finite experiment to a theorem.  It did not use a proof assistant.  The only
audit code used here is `audit/referee_subset_evaluator.py`; it shares no
implementation with a rooted-DP discovery program and counts independent sets
by inspecting every vertex subset.

## 1. Reconstruction from definitions

Let (G=(V,E)) be a finite simple graph.  A set (S\subseteq V) is
independent when no (e\in E) is contained in (S).  Put

\[
 I_G(x)=\sum_{S\text{ independent}}x^{|S|}.
\]

This definition for **all** finite simple graphs is needed even when the
theorem concerns only trees, because deleting a vertex or a closed
neighbourhood generally produces a forest rather than a tree.  The empty
graph has exactly one independent set, the empty set, and hence polynomial
(1).

### Deletion identity

Fix (v\in V).  Partition the independent sets (S) of (G) according to
whether (v\notin S) or (v\in S).

* If (v\notin S), then (S) is, without any change of size, an independent
  set of (G-v).  This is a bijection.
* If (v\in S), then (S\setminus\{v\}) contains no vertex in (N(v)) and
  is an independent set of (G-N[v]).  Conversely, adjoining (v) to any
  independent set of (G-N[v]) gives an independent set of (G).  The size
  increases by one.

The two classes are disjoint and exhaustive, so coefficient by coefficient

\[
 I_G(x)=I_{G-v}(x)+xI_{G-N[v]}(x).
\]

No connectivity, acyclicity, nonzero coefficient, division, or limiting
argument is used in this proof.

### Multiplicativity and rooted identity

If (G=G_1\sqcup\cdots\sqcup G_d) is a disjoint union, then an independent
set of (G) is uniquely a tuple of independent sets of the components.
Sizes add, so

\[
 I_G(x)=\prod_{j=1}^d I_{G_j}(x).
\]

Now root a tree (T) at (r), and let (T_1,\ldots,T_d) be the components
below the children of (r), each rooted at that child.  Define explicitly

\[
 A_T(x)=\sum_{\substack{S\text{ independent in }T\\r\notin S}}x^{|S|},
 \qquad
 B_T(x)=\sum_{\substack{S\text{ independent in }T\\r\in S}}x^{|S|}.
\]

If (r\notin S), the choices in the child subtrees are arbitrary and
independent, giving

\[
 A_T=\prod_{j=1}^d(A_{T_j}+B_{T_j}).
\]

If (r\in S), every child is excluded; after choosing (r), the remaining
choices are precisely those counted by (A_{T_j}).  Hence

\[
 B_T=x\prod_{j=1}^d A_{T_j},\qquad I_T=A_T+B_T.
\]

For a leaf the empty-product convention gives (A_T=1), (B_T=x), so the
base and the one-vertex boundary are covered.  All equalities are in
(\mathbb Z_{\ge0}[x]).

### Positivity of the stated support

Because (T) is finite, at least one maximum independent set (M) exists.
For every (0\le k\le |M|=\alpha(T)), every (k)-subset of (M) is
independent.  Thus (i_k(T)>0) throughout the stated support, while the
definition of (alpha(T)) gives (i_k(T)=0) above it.  Also (i_0(T)=1).

## 2. Triple-valley equivalence

The following statement holds for every finite real sequence
(a_0,\ldots,a_q), without positivity.

**Lemma.**  The sequence is weakly unimodal if and only if there do not exist
(0\le k<\ell<m\le q) such that (a_k>a_\ell<a_m).

**Proof.**  If (p) is a weak-unimodal mode and (k<\ell<m), then
(\ell\le p) implies (a_k\le a_\ell), while (\ell\ge p) implies
(a_m\le a_\ell).  Thus a strict valley is impossible.

Conversely, assume there is no strict valley and let (p) be an index of a
global maximum.  If some (k<\ell\le p) had (a_k>a_\ell), then necessarily
(\ell<p) and (a_p\ge a_k>a_\ell), producing the valley
(k<\ell<p).  Hence the sequence is weakly increasing through (p).  If
some (p\le\ell<m) had (a_\ell<a_m), then necessarily (p<\ell) and
(a_p\ge a_m>a_\ell), producing the valley (p<\ell<m).  Hence it is weakly
decreasing after (p).  This is weak unimodality.  \(\square\)

It follows immediately, using integrality only for the word "integer", that

\[
 \Delta(T)=\max_{k<\ell<m}
 \min\{i_k-i_\ell,i_m-i_\ell\}>0
\]

if and only if (T) is a counterexample.  When there are fewer than three
coefficients the maximum is over the empty set; declaring it to be
(-\infty) is coherent.  An implementation should serialize this exceptional
value as `null` or a tagged value, not as a floating-point infinity.

## 3. Quantifier and boundary audit of `formal_statement.md`

The main conjecture is correctly quantified over finite, simple, undirected,
nonempty, connected, acyclic graphs.  The mode (p) ranges over the two
endpoints as well as internal indices, and the weak inequalities correctly
allow plateaux.  The single-vertex tree and empty graph arising inside a
recurrence are handled.  Isomorphism invariance is immediate because graph
isomorphisms give size-preserving bijections of independent sets.

The following repairs are advisable before the statement is used as the
formal endpoint of a proof.

1. **Local definitional gap:** define (I_G) for every finite simple graph
   before writing (I_{T-v}) and (I_{T-N[v]}).  At present the displayed
   definition is syntactically given only for a tree (T), although the prose
   later invokes forests and the empty graph.
2. **Local explicitness gap:** define (A_T,B_T) by the two displayed sums
   above, not only by the words "root excluded/included".  This fixes whether
   the root contributes to degree in (B_T) (it does).
3. **Local certificate-input gap:** an edge list alone does not determine the
   vertex set of the one-vertex tree.  Every certificate should contain an
   explicit positive integer (n) and use a fixed vertex set such as
   \(\{0,\ldots,n-1\}\), in addition to the edges.
4. **Local scope/citation gap:** the phrase "log-concavity is strictly
   stronger" unconditionally has the elementary implication in the positive
   sequence setting, but strictness *within tree independence sequences*
   additionally invokes the existence of a tree that is unimodal and not
   log-concave.  If that restricted meaning is intended, it must be separated
   from the definition and tied to a verified source or an explicit example.

No other quantifier or endpoint defect was found in the conjecture as written.

## 4. Independent evaluator and exact tests

The evaluator parses exactly

```json
{"n": 4, "edges": [[0, 1], [0, 2], [0, 3]]}
```

with vertex set (0,\ldots,n-1).  It rejects loops, repeated undirected
edges, missing or out-of-range vertices, a non-tree edge count, and
disconnection.  It then iterates through all (2^n) vertex masks, rejects a
mask if an input edge has both endpoints selected, and forms the coefficient
histogram using exact Python integers.  It independently computes
unimodality and (Delta), and prints input and code SHA-256 hashes.  This is
algorithmically independent of child-subtree polynomial products.

Reproducible commands and exact outputs:

```sh
python3 audit/referee_subset_evaluator.py --self-test
python3 audit/referee_subset_evaluator.py --rooted-audit-max-n 7
```

The first command passed:

* all 21,844 sequences of lengths (1,\ldots,7) over
  \(\{0,1,2,3\}\), comparing the definition of weak unimodality to the
  triple-valley test;
* the closed formulas (i_k(P_n)=\binom{n-k+1}{k}) and
  (I_{K_{1,q}}=(1+x)^q+x) for 30 path/star instances through 15 vertices;
* the deletion identity for every vertex of every labelled simple graph on at
  most 5 vertices (5,405 graph-vertex cases);
* the rooted identities at every root of every Prüfer-labelled tree on at
  most 6 vertices (8,477 rooted cases); and
* rejection of five malformed boundary inputs.

The second command exhaustively inspected all 126,126 labelled rooted trees
on at most 7 vertices.  It found no failure of individual unimodality of
(A_T) or (B_T) in that finite range.  This is only a test result and is not
a theorem.  It did exactly refute two tempting stronger invariants:

* For (K_{1,3}), rooted at a leaf (centre 0, root 1),
  \(A=[1,3,1,0]\) has sole weak mode 1 whereas
  \(B=[0,1,2,1]\) has sole weak mode 2.  Thus a proof cannot require the two
  rooted states always to have a common mode.
* For (K_{1,2}), rooted at its centre,
  \(A=[1,2,1]\), (B=[0,1,0]\), and the adjacent cross minors
  \(A_kB_{k+1}-A_{k+1}B_k\) are (1,-1).  Thus neither uniform direction of
  this naive ratio-monotonicity condition is true.  Writing ratios directly
  would additionally divide by the forced zero (B_0=0).

The following exact abstract examples expose two further closure traps.  They
are not asserted to be realizable rooted states; that is precisely why a proof
must use a *proved rooted-state compatibility*, not unimodality alone.

* (A=(1,100,90,0,0)) and (B=(0,1,10,90,100)) are individually weakly
  unimodal, but (A+B=(1,101,100,90,100)) has the strict valley
  (101>90<100).  Therefore individual unimodality of (A_T,B_T), even if
  proved, would not by itself prove unimodality of (I_T=A_T+B_T).
* The weakly unimodal sequences ((1,1,2)) and ((1,1,3)) have convolution
  ((1,2,6,5,6)), which has (6>5<6).  Therefore a product step cannot rely
  on generic closure of unimodality under convolution.

The subset evaluator is intentionally exponential.  If a decisive candidate
is too large for direct subset enumeration, Gate 4 still needs a clean-room
second implementation, for example unrooted include/exclude branching with
memoized vertex masks, or a separately written rooted evaluator whose input
is only the serialized edge list.  Agreement between two copies of the same
cached coefficient array is not independent verification.

## 5. Most dangerous hidden assumptions

1. **Closure by generic unimodality.**  Neither sums nor products of arbitrary
   nonnegative unimodal coefficient sequences preserve unimodality, as the
   exact examples above show.  Any positive proof must state and prove a
   stronger compatibility invariant closed simultaneously under the two
   rooted operations.
2. **Bounded search represents all trees.**  The recursive grammar "a root
   plus an arbitrary finite multiset of rooted child trees" is complete by
   induction, but a search with bounded height, degree, child types, core
   size, or mutation budget is not.  Such a search can discover a
   counterexample, but its failure cannot prove the conjecture or an
   unrestricted finite frontier.
3. **Coefficient truncation is harmless.**  Rooted polynomials have different
   degrees and forced endpoint zeros, especially (B_0=0).  Dropping or
   padding zeros inconsistently can change mode sets, ratio tests, and the
   domain of the triple maximum.  The final (I_T) must be trimmed only above
   its last positive coefficient; state comparisons must declare a common
   padding convention.
4. **Machine integers are exact enough.**  Counts grow exponentially.  Fixed
   width overflow can produce a false valley with no runtime error.  Discovery
   and certification must use arbitrary-precision integers or prove a bound
   below the machine limit.
5. **An edge list is automatically a tree certificate.**  Feasibility must be
   checked separately: explicit (n\ge1), endpoints in range, no loops or
   duplicate undirected edges, exactly (n-1) edges, and connectivity.  Only
   then does the count certify a tree counterexample.
6. **Root choice or canonical labels preserve rooted states.**  (I_T) is
   root-independent, but ((A_T,B_T)) is not.  A rooted-state database must
   canonicalize rooted trees, not merely unrooted trees, and a final evaluator
   should check that every chosen root gives the same (A_T+B_T).
7. **Attaching or amplifying gadgets simply multiplies independence
   polynomials.**  Multiplication is valid for disjoint union.  Connecting
   gadgets to keep a tree couples included/excluded root states and must use
   the two-state recurrence exactly.  A symbolic family argument must check
   this coupling and prove its parameter inequalities for every claimed
   integer parameter, including endpoints.

## 6. Gap classification and discriminating next steps

### Fatal gaps (fatal to a claimed resolution, not defects in the conjecture)

* **F1 — no global closure theorem or exact counterexample currently audited
  here.**  The recurrences alone do not imply unimodality.  **Next decidable
  step:** write the proposed rooted-state invariant as explicit coefficient
  inequalities, test it with `--rooted-audit-max-n 7`, and either exhibit the
  first exact failing rooted tree or prove both composition operations preserve
  it, including unequal degrees and endpoint zeros.
* **F2 — individual state unimodality cannot close the induction.**  The exact
  sum and convolution counterexamples above kill that logical implication.
  **Next decidable step:** require a compatibility condition sufficient for
  both (\prod(A_j+B_j)) and (x\prod A_j) and for their final sum; verify
  sufficiency algebraically before attempting induction.
* **F3 — a bounded grammar/mutation run cannot establish the universal
  quantifier.**  **Next decidable step:** for a finite theorem, provide a
  canonical generator with a proved bijection to every unlabelled tree in the
  stated range and an independently checked count manifest; for the full
  theorem, replace the bound by an induction/reduction covering arbitrary
  child multisets.

### Major gaps

* **M1 — finite-frontier certification is absent from this referee artifact.**
  **Next decidable step:** rerun the claimed range from serialized canonical
  trees and compare every coefficient vector against a second evaluator;
  publish generator counts and hashes.  A citation to somebody else's run is
  not a local certificate.
* **M2 — scalable independent verification of a large discovered candidate.**
  The present direct evaluator costs (2^n).  **Next decidable step:** feed any
  retained candidate to it; if infeasible, implement clean-room unrooted
  deletion branching or an isolated second DP and require exact coefficient
  and valley-witness agreement from the same edge-list input.
* **M3 — any parameter-amplification family needs endpoint-complete symbolic
  proof.**  A non-log-concavity inequality is not a valley inequality, and
  connecting copies is not disjoint-union multiplication.  **Next decidable
  step:** serialize the family construction, derive (A,B,I) symbolically,
  and reduce the proposed strict valley to explicit integer polynomial
  inequalities over the exact parameter range; disprove or certify them
  exactly.
* **M4 — canonicalization must match the state being stored.**  Unrooted AHU
  codes are insufficient to deduplicate rooted state pairs.  **Next decidable
  step:** compare the proposed canonical key on all Prüfer-labelled rooted
  trees through a small (n), checking that equal keys are rooted-isomorphic
  and yield equal ((A,B)), and that each rooted-isomorphism class has one key.

### Local gaps

* **L1:** extend the formal definition from (I_T) to (I_G) for finite
  simple graphs before deletion; add the explicit sums defining (A_T,B_T).
* **L2:** serialize `n` as well as edges; state the vertex-label convention.
* **L3:** state the common zero-padding/trimming rule for any coefficientwise
  state invariant and avoid divisions at (B_0=0).
* **L4:** represent empty-domain (Delta=-\infty) without an inexact numeric
  sentinel.
* **L5:** separate the elementary implication "positive log-concave implies
  unimodal" from the literature-dependent claim that strictness is witnessed
  inside tree independence sequences.

## 7. Referee verdict

The formal conjecture, the two exact recurrences, and the triple-valley
equivalence survive reconstruction from definitions.  The current identities
are foundations for search, not a proof.  The most immediate proof hazard is
an invalid closure inference from statewise unimodality, simple mode
synchronization, or naive ratio monotonicity; exact small examples already
rule out those formulations.  A disproof would require only one validated
tree and a positive exact (Delta), whereas any positive universal or finite
claim additionally requires the appropriate coverage certificate.  This
report reaches neither PROVED nor DISPROVED.
