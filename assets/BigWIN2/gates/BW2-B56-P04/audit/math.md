# Fresh mathematical referee report

## Binding and verdict

- Referee job: `win-00056-p04-referee-479a2d09f095`.
- Frozen snapshot: `f400278043022a78b6fad23f832e57d2593a690342ae64738ccd6469b18597d0`.
- Candidate scope: the `resolution-paper` statement in `claim.json`, including the
  universal two-layer inequality and its stated Boolean-lattice consequence.
- Verdict: **accept**.

I recomputed every snapshot-listed SHA-256 digest before reviewing the
mathematics; all matched `audit/snapshot.json`. The immutable `source.md` also
retained digest `d9ceaf2415c2dbb550a6bd22c78c6adbad34e4fd6ffe8456ec2ae528d4321210`.

## Reconstruction of the decisive proof

Let (B=P_0\cap P_1). Convexity gives the key fact

\[
 p\in P_0,quad q\in P_1,quad p\le q
 \quad\Longrightarrow\quad p,q\in B. \tag{1}
\]

Indeed, both ((p,1)) and ((q,0)) lie between the endpoints
((p,0),(q,1)\in P). This argument uses only the product order and works with
equality as well as strict comparison.

For each (i\in\{0,1\}), take a maximum antichain
(A_i=(L_i\times\{0\})\cup(H_i\times\{1\})) in (P_i\times Q_1).
Thus (L_i,H_i) are antichains and no (l\in L_i) satisfies (l\le h)
for (h\in H_i).

Form the bipartite comparison graph with occurrence copies of (L_1) and
(H_0). An equality edge is an isolated two-vertex component, because any
additional neighbor would contradict one of the within-side antichain
conditions. In every other nontrivial component all strict edges have the same
orientation. For example, starting with (l<h), another (L_1)-neighbor
(l') of (h) must satisfy (l'<h): either (h\le l') or equality would
make (l,l') comparable. A subsequent (H_0)-neighbor (h') must satisfy
(l'<h'), since (h'\le l') would make (h',h) comparable. Propagation along
paths proves the classification; the reverse case is symmetric.

The assignment in `evidence/proof.md` keeps equality components and
(L_1<H_0) components native, and swaps (H_0<L_1) components. It treats an
isolated (l\in L_1) as swapped precisely when some (a\in L_0) has
(a\le l), and an isolated (h\in H_0) as swapped precisely when some
(b\in H_1) has (h\le b). Every swap is legal: in a nontrivial swapped
component each vertex has an incident (h<l) edge, and (1) places its value in
(B); (1) applies directly to either isolated swap condition as well.

Writing (U) for values assigned to the upper layer and (D) for values
assigned to the lower layer, the outputs are

\[
 \mathcal U=(L_0\times\{0\})\cup(U\times\{1\}),\qquad
 \mathcal D=(D\times\{0\})\cup(H_1\times\{1\}).
\]

I checked both outputs in all possible directions:

1. Within (U), and separately within (D), same-side values are
   incomparable because (L_1) and (H_0) are antichains. A comparable
   cross-side pair is an edge in one graph component, whose endpoints are
   assigned to opposite outputs. Hence (U,D) are antichains. The fixed sets
   (L_0,H_1) are antichains as well.
2. The only product-order cross-layer threat in (mathcal U) is
   (a\le u), with (a\in L_0). A swapped (H_0)-value is excluded by the
   (L_0,H_0) input antichain; a native isolated (L_1)-value is excluded by
   its assignment rule; a native equality-component (L_1)-value equals an
   (H_0)-neighbor; and a native (L_1<H_0) value lies below an
   (H_0)-neighbor. The last two alternatives would again violate the
   (L_0,H_0) input antichain.
3. The only cross-layer threat in (mathcal D) is (d\le b), with
   (b\in H_1). A swapped (L_1)-value is excluded by the (L_1,H_1) input
   antichain; a native isolated (H_0)-value is excluded by its assignment
   rule; a native equality-component value equals an (L_1)-neighbor; and a
   native type-(L_1<H_0) value lies above an (L_1)-neighbor. The last two
   alternatives would violate the (L_1,H_1) input antichain.

These cases are exhaustive. Occurrence copies also handle
(L_1\cap H_0) correctly: equality endpoints go to opposite outputs. No two
occurrences in the same output have the same underlying value, so

\[
 |U|+|D|=|L_1|+|H_0|.
\]

It follows that

\[
 |\mathcal U|+|\mathcal D|
 =|L_0|+|H_0|+|L_1|+|H_1|
 =w(P_0\times Q_1)+w(P_1\times Q_1).
\]

Both outputs are antichains in (P), so each has size at most (w(P)),
which proves the frozen inequality for every finite (R). Empty input sets,
empty sections, isolated vertices, equality components, and disconnected
comparison graphs require no separate nonempty assumption and are covered by
the same construction.

## Downstream induction

I independently checked the parameter bookkeeping. The induction is on (n)
simultaneously for all (k\ge0). At (n=0), the only convex subsets of
(Q_0) are empty and (Q_0), giving zero and equality respectively. For the
step, identify (Q_{n+1}=Q_n\times Q_1) and write the convex sections of
(P) as (P_0,P_1\subseteq Q_n); each section is convex. Coordinate
permutation makes the convex set (P\times Q_k) a subset of
(Q_{n+k}\times Q_1), with sections (P_i\times Q_k). The lemma therefore
gives

\[
 w(P\times Q_k)\ge \tfrac12\sum_{i=0}^1w(P_i\times Q_{k+1}).
\]

Applying the induction hypothesis at ((n,k+1)), then using
(|P|=|P_0|+|P_1|), gives exactly

\[
 w(P\times Q_k)\ge w(Q_{n+k+1})|P|2^{-(n+1)}.
\]

Thus there is no illicit limiting step or division by a possibly zero
quantity, and empty sections remain valid.

## Source comparison and exact checks

The snapshot-listed Williams preprint states the same lemma and consequence.
On its PDF page 3 the proposed sorting uses an undefined set (C), verifies
only one output, and invokes “hourglass symmetry” for the other. This is not
the component proof above. Under the natural audit interpretation
(C=(P_0\cup P_1)\setminus(P_0\cap P_1)), the listed three-chain certificate
is correct: for (P_0=\{0,1,2\}), (P_1=\{0,1\}), it sends both (0,1) to
one upper output, where they are comparable. The relevant widths are all two,
so that example invalidates only the inferred source sorting, not the lemma.

As a fresh computational check, `audit/referee_verify.py` uses no candidate
verification imports. It enumerated all naturally labelled posets through four
elements, all 6,670 convex two-layer subsets, and all 48,039 pairs of maximum
section-product antichains. It checked the inequality, legality of every move,
both output antichains, and total cardinality, with no failure. It separately
reproduced the three-chain source-step failure; results are serialized in
`audit/referee-checks.json`. I also reran the snapshot-listed exhaustive
inequality program through five elements and reproduced its 180,102 convex
instances, no counterexample, and enumeration digest
`d828fe2b7725e14578a063ce98a00d44ac4ee1294758d03e92282d52dbd1f793`.
These finite checks support but are not used to prove the universal claim.

## Scope and residual limitations

The proof settles exactly the immutable universal lemma and validates exactly
the requested induction route. The accepted scope does not establish priority,
novelty of the full Daykin--Frankl theorem, or validity of the preprint's
undefined-(C) construction. Those broader assertions are not made in the
frozen claim. Within the frozen mathematical scope I found no unresolved gap.

