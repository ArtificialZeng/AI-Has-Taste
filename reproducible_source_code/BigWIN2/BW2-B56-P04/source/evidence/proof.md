# Complete repair of the two-layer lemma

This file proves the frozen lemma for every finite poset and audits both output
antichains in every comparison direction.  It also verifies the stated
backward-induction consequence.  The repair does **not** use the undefined set
`C` in the source; `evidence/inferred-sorting-failure.json` shows that the
proposed interpretation of that construction can fail even for a three-chain.

## Lemma

Let (R) be a finite poset, let (P\subseteq R\times Q_1) be order convex,
and write its sections as (P_0,P_1\subseteq R). Then

\[
2w(P)\geq w(P_0\times Q_1)+w(P_1\times Q_1). \tag{L}
\]

### The convexity observation

Put (B=P_0\cap P_1). If (p\in P_0, q\in P_1), and (p\leq_R q), then

\[
(p,0)\leq(p,1)\leq(q,1),\qquad
(p,0)\leq(q,0)\leq(q,1).
\]

The endpoints belong to (P), so convexity puts both middle points in (P).
Consequently

\[
p\in P_0, q\in P_1, p\leq q\quad\Longrightarrow\quad p,q\in B. \tag{*}
\]

### Input antichains and the comparison graph

For (i=0,1), choose a maximum antichain in (P_i\times Q_1), written

\[
\mathcal A_i=(L_i\times\{0\})\mathbin\cup(H_i\times\{1\}).
\]

Thus (L_i) and (H_i) are antichains in (R), and

\[
\ell\in L_i, h\in H_i\quad\Longrightarrow\quad \ell\not\leq h. \tag{1}
\]

Make a bipartite graph (G). Its left vertices are *occurrences* (L_1^*)
corresponding to elements of (L_1), its right vertices are occurrences
(H_0^*) corresponding to elements of (H_0), and (\ell^*h^*) is an edge
exactly when their underlying elements (\ell,h\) are comparable in (R).
Occurrences are used so that if an element lies in (L_1\cap H_0), the two
copies remain distinct.

Every nontrivial component of (G) is of exactly one of the following types:

1. a single equality edge (\ell=h);
2. every edge has strict orientation (\ell<h), from (L_1) to (H_0);
3. every edge has strict orientation (h<\ell), from (H_0) to (L_1).

Indeed, an equality edge is an isolated component: any further neighbor would
be comparable to an element in the same one of the antichains (L_1,H_0).
For a strict edge (\ell<h), every other (L_1)-neighbor (\ell') of (h)
also satisfies (\ell'<h), since (h\leq\ell') would give
(\ell<\ell'), contrary to (L_1) being an antichain. Every other
(H_0)-neighbor (h') of such an (\ell') satisfies (\ell'<h'), since
(h'\leq\ell'<h) would contradict the antichain property of (H_0).
Propagation along paths proves type 2; reversing the order proves type 3.

### The complete assignment

We assign every occurrence vertex to one of two sets of underlying values,
(U) and (D).

- In a type-1 or type-2 component, put all its (L_1^*)-occurrences in (U)
  and all its (H_0^*)-occurrences in (D) (the **native** assignment).
- In a type-3 component, put all its (L_1^*)-occurrences in (D) and all its
  (H_0^*)-occurrences in (U) (the **swapped** assignment).
- For an isolated (\ell^*\in L_1^*), put it in (D) if some
  (a\in L_0) satisfies (a\leq\ell), and otherwise put it in (U).
- For an isolated (h^*\in H_0^*), put it in (U) if some
  (b\in H_1) satisfies (h\leq b), and otherwise put it in (D).

All layer moves are legal. In a type-3 component, every vertex has an incident
edge (h<\ell) with (h\in P_0,ell\in P_1), so (*) puts every underlying
value in (B). If an isolated (\ell^*) is swapped, (*) applied to
(a\leq\ell) puts (\ell\in B); if an isolated (h^*) is swapped, (*)
applied to (h\leq b) puts (h\in B). Hence a swapped value exists in the
other horizontal section of (P).

Now define two subsets of (P):

\[
\mathcal U=(L_0\times\{0\})\cup(U\times\{1\}),\qquad
\mathcal D=(D\times\{0\})\cup(H_1\times\{1\}). \tag{2}
\]

### Audit of the first output (\mathcal U)

Within its lower layer, (L_0) is an antichain by (1). Within its upper
layer, values coming from (L_1^*) are mutually incomparable, as are values
coming from (H_0^*). If one value comes from each side and they were
comparable, the two occurrence vertices would be adjacent in one component of
(G); the assignment always sends the two sides of a component to opposite
sets. Thus (U) is an antichain.

It remains to exclude a cross-layer comparison
((a,0)\leq(u,1)), i.e. (a\in L_0, u\in U, a\leq u).

- If (u) comes from a swapped (H_0^*)-occurrence, (1) for
  (L_0,H_0) directly forbids (a\leq u).
- If (u) comes from a native isolated (L_1^*)-occurrence, its assignment
  rule directly says that no (a\in L_0) satisfies (a\leq u).
- If (u\in L_1) lies in a native equality component, its neighbor in
  (H_0) has the same value (u), so (a\leq u) contradicts (1) for
  (L_0,H_0).
- If (u\in L_1) lies in a native type-2 component, it has a neighbor
  (h\in H_0) with (u<h). Then (a\leq u<h) again contradicts (1) for
  (L_0,H_0).

These cases exhaust (U), so (\mathcal U) is an antichain.

### Audit of the second output (\mathcal D)

The same graph argument, stated explicitly, shows that (D) is an antichain:
values inherited from (H_0) are pairwise incomparable, values inherited from
(L_1) are pairwise incomparable, and any cross-family comparable pair is an
edge whose endpoints were assigned to opposite sets. Also (H_1) is an
antichain by (1).

The only possible remaining comparison is
((d,0)\leq(b,1)), i.e. (d\in D, b\in H_1, d\leq b).

- If (d) comes from a swapped (L_1^*)-occurrence, (1) for
  (L_1,H_1) directly forbids (d\leq b).
- If (d) comes from a native isolated (H_0^*)-occurrence, its assignment
  rule directly says that no (b\in H_1) satisfies (d\leq b).
- If (d\in H_0) lies in a native equality component, its (L_1)-neighbor
  has value (d), so (d\leq b) contradicts (1) for (L_1,H_1).
- If (d\in H_0) lies in a native type-2 component, it has a neighbor
  (\ell\in L_1) with (\ell<d). Then (\ell<d\leq b) contradicts (1)
  for (L_1,H_1).

Thus (\mathcal D) is an antichain.

### Cardinality and conclusion

Each occurrence in (L_1^*\sqcup H_0^*) is assigned exactly once. No two
distinct occurrences assigned to the same set have the same underlying value:
the only possible cross-family equality would be an equality edge, whose two
endpoints receive opposite assignments. Therefore

\[
|U|+|D|=|L_1|+|H_0|.
\]

Using (2),

\[
|\mathcal U|+|\mathcal D|
=|L_0|+|L_1|+|H_0|+|H_1|
=w(P_0\times Q_1)+w(P_1\times Q_1).
\]

Both are antichains in (P), so their sizes are each at most (w(P)),
which proves (L).

## Verification of the backward induction

Let (Q_n=(2^{[n]},\subseteq)). We prove, simultaneously for every (k\geq0),
that every convex (P\subseteq Q_n) satisfies

\[
w(P\times Q_k)\geq w(Q_{n+k})|P|2^{-n}. \tag{T}
\]

For (n=0), either (P=\varnothing), when both sides are zero, or
(P=Q_0), when the inequality is the equality
(w(Q_k)=w(Q_k)\cdot1).

Assume the assertion for (n) and all (k\geq0). Identify
(Q_{n+1}=Q_n\times Q_1), let (P\subseteq Q_{n+1}) be convex, and write its
sections (P_0,P_1\subseteq Q_n). Each section is convex: if
(x\leq z\leq y) in (Q_n) and (x,y\in P_i), then
((x,i)\leq(z,i)\leq(y,i)), so (z\in P_i).

The product (P\times Q_k) is convex in (Q_{n+1}\times Q_k): a coordinatewise
point between two of its elements has its first coordinate in (P), by
convexity, and its second coordinate automatically in the whole (Q_k).
After permuting product coordinates, regard it as a convex subset of
(Q_{n+k}\times Q_1). Its two sections are (P_0\times Q_k) and
(P_1\times Q_k). Applying (L) gives

\[
w(P\times Q_k)\geq\frac12\sum_{i=0}^1 w(P_i\times Q_{k+1}).
\]

Apply the induction hypothesis at (n) with the shifted parameter (k+1):

\[
w(P_i\times Q_{k+1})
\geq w(Q_{n+k+1})|P_i|2^{-n}.
\]

Since (|P|=|P_0|+|P_1|), averaging yields

\[
w(P\times Q_k)
\geq w(Q_{n+k+1})|P|2^{-(n+1)},
\]

which is (T) for (n+1). Empty sections and the empty (P) are included in
the same argument. Finally, the standard exact width formula
(w(Q_m)=\binom{m}{\lfloor m/2\rfloor}) identifies the displayed constant.

## Exact finite evidence (not part of the proof)

`evidence/exhaustive_posets.py` independently enumerates all naturally labelled
posets through five elements, hence at least one representative of every finite
poset isomorphism class in that range; all convex subsets of their products
with (Q_1); and exact widths by antichain subset dynamic programming. It finds
no counterexample among 180,102 convex instances. Full counts and a deterministic
enumeration digest are in `evidence/exhaustive-through-5.json`.
