# Formal statement

## Objects and conventions

For an integer (n\ge 0), a **tournament of order (n)** is a pair
(T=(V,A)) with (|V|=n) such that, for each unordered pair
(\{x,y\}\subseteq V) of distinct vertices, exactly one of
((x,y),(y,x)) lies in (A).  Thus every unordered vertex pair supports one
arc, and (|A|=\binom n2).

For a three-element set (X\subseteq V), the subtournament (T[X]) is a
**transitive triple** (TT_3) iff it is acyclic; equivalently, some vertex of
(X) has both incident arcs directed outwards; equivalently, (T[X]) is not
a directed 3-cycle.  A copy is identified by its three vertices and uses all
three arcs supported on the three unordered pairs in (\binom X2).

A (TT_3)-packing is a set (\mathcal P\subseteq\binom V3) such that every
(X\in\mathcal P) is transitive in (T) and the sets (\binom X2),
(X\in\mathcal P), are pairwise disjoint.  (For tournaments, “arc-disjoint”
and “disjoint in their underlying unordered pairs” are identical.)  Define

\[
 \nu_3(T)=\max\{|\mathcal P|:\mathcal P\text{ is a }TT_3\text{-packing of }T\}.
\]

The maximum exists because the set of triples is finite.  Define

\[
 \nu_3(n)=\min\{\nu_3(T):T\text{ is a tournament of order }n\}.
\]

The minimum exists because there are finitely many labeled tournaments.
Relabeling vertices, reversing every arc, or replacing a tournament by an
isomorphic copy does not change (\nu_3(T)).

## Target theorem

Prove or disprove the exact finite assertion

\[
 \boxed{\forall T\ (|V(T)|=11\Longrightarrow\nu_3(T)\ge 15)}. \tag{LB11}
\]

Together with the explicit cyclic three-part blow-up upper bound below, this
is equivalent to

\[
 \boxed{\nu_3(11)=15}. \tag{E11}
\]

The relevant instance of Yuster's formula is exact:

\[
 \left\lceil\frac{11\cdot10}{6}-\frac{11}{3}\right\rceil
 =\left\lceil\frac{44}{3}\right\rceil=15.
\]

## Upper-bound construction and equality convention

Partition eleven vertices into parts of sizes (4,4,3), orient every
cross-part arc cyclically (V_1\to V_2\to V_3\to V_1), and orient arcs
inside the parts arbitrarily.  A triple using one vertex from each part is
cyclic, so every transitive triple uses at least one within-part arc.  Since a
packing cannot reuse such an arc,

\[
 \nu_3(T)\le \binom42+\binom42+\binom32=15.
\]

No classification of all equality tournaments is part of (E11).  Exhibiting
one tournament attaining 15 suffices for the upper bound; proving (LB11)
requires every labeled or, equivalently, every isomorphism class of
11-vertex tournaments.

## Endpoints and degenerate cases

The present endpoint is exactly (n=11); no asymptotic limit, fractional
packing, induced-copy convention, vertex-disjointness, multi-arcs, loops, or
weighted copies are allowed.  For completeness, when (n<3), the only
packing is empty and (\nu_3(n)=0).  These degenerate orders do not enter the
target theorem.  At (n=3), the directed 3-cycle has packing number zero,
which agrees with Yuster's formula.

## Finite certificate interpretation

A positive computational proof must cover one representative of every
isomorphism class emitted by a pinned canonical tournament generator and
must exactly verify a 15-packing (or an equivalent exhaustive exact search)
for every representative.  A negative result must give a literal
55-bit tournament and an exact proof that its maximum packing is at most 14.
