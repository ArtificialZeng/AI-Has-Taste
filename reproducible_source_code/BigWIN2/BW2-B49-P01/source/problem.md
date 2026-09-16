# Precise problem: minimum bondage sets of the truncated-octahedral graph

## Frozen lead and interpretation

The immutable lead is `source.md`.  Its mathematical reading is the following
finite classification problem; this document fixes notation but does not alter
the lead.

Let \(T=(V,E)\) be the finite simple graph with

\[
V=\{0,1,\ldots,23\}
\]

and

\[
\begin{aligned}
E=\{&(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,4),(3,8),\\
&(4,9),(5,10),(5,11),(6,11),(6,12),(7,12),(7,13),(8,13),(8,14),\\
&(9,15),(9,16),(10,16),(10,17),(11,17),(12,18),(13,19),(14,15),\\
&(14,19),(15,20),(16,20),(17,21),(18,21),(18,22),(19,22),\\
&(20,23),(21,23),(22,23)\}.
\end{aligned}
\]

Each displayed pair denotes an unordered edge.  This is the labeled
truncated-octahedral graph used in Srivastava, arXiv:2609.02477v1, Section 3.

For a graph \(G=(V(G),E(G))\), a set \(D\subseteq V(G)\) is dominating if
every vertex in \(V(G)\setminus D\) has a neighbor in \(D\).  The domination
number is

\[
\gamma(G)=\min\{|D|:D\subseteq V(G)\text{ is dominating}\}.
\]

For \(F\subseteq E(G)\), \(G-F\) has the same vertices and edge set
\(E(G)\setminus F\).  Define

\[
\mathcal M(T)=\{F\subseteq E: |F|=5\text{ and }
                 \gamma(T-F)>\gamma(T)\}.
\]

The full abstract automorphism group

\[
\operatorname{Aut}(T)=\{\sigma\in S_{24}:
 \{u,v\}\in E\Longleftrightarrow\{\sigma(u),\sigma(v)\}\in E\}
\]

acts on edge sets by
\(\sigma F=\{\{\sigma(u),\sigma(v)\}:\{u,v\}\in F\}\).

## Exact quantified target

Determine, with an exact completeness certificate:

1. the integer \(|\mathcal M(T)|\);
2. all orbits of \(\mathcal M(T)\) under the above full group action;
3. for each orbit, a canonical representative, its orbit cardinality, its
   setwise stabilizer cardinality, and the exact integer \(\gamma(T-F)\).

For reproducibility, a canonical representative may be defined as follows:
write every edge as \((\min(u,v),\max(u,v))\), sort the five edges
lexicographically, and choose the lexicographically least resulting 5-tuple
in the orbit.  A different stated deterministic convention is acceptable,
but it must give the same orbit partition.

All 
\(
\binom{36}{5}=376{,}992
\)
five-edge subsets are quantified over.  No assumption may be made that every
five-edge set belongs to \(\mathcal M(T)\), that the domination number always
rises by exactly one, or that geometric symmetries comprise the full abstract
automorphism group.  An examples-only list or classification under a proper
subgroup does not answer the problem.

## Established baseline and scope

Srivastava proves \(\gamma(T)=8\) (Lemma 1, pp. 2--3) and \(b(T)=5\)
(Theorem 1, p. 3), where

\[
b(G)=\min\{|F|:F\subseteq E(G),\ \gamma(G-F)>\gamma(G)\}.
\]

The paper enumerates 1,767 dominating eight-sets, checks all
\(\binom{36}{4}=58{,}905\) four-edge subsets, and gives the witness
\(F_5=\{02,14,15,26,27\}\), for which \(\gamma(T-F_5)=9\).  Here \(uv\)
means the edge \(\{u,v\}\), so this witness is unambiguous.  Consequently,
assuming that established baseline, every member of \(\mathcal M(T)\) is a
minimum-cardinality bondage set.  The requested contribution is only the
complete classification of those sets; it does not claim a new counterexample
to the planar bondage conjecture or a theorem for a larger graph class.

The official v1 full text was inspected on 2026-09-07.  It establishes the
baseline and one five-edge witness but does not enumerate \(\mathcal M(T)\) or
its automorphism orbits.  Exact-phrase and equivalent-language searches on the
same date found no separate classification.  This supports the intake label
**status-uncertain new finite question**, not a claim that the problem is known
open or novel.

## Proposed delta and verification route

Nearest prior result: Srivastava's exact values \(\gamma(T)=8\), \(b(T)=5\),
and one minimum bondage set.  Proposed delta: the complete orbit
classification above.  Verification route: independently enumerate the
dominating eight-sets, test all 376,992 five-edge subsets exactly, compute the
full labeled automorphism group, form and audit the orbit partition, and for
each representative prove its reported domination number by exhaustive lower
exclusion plus an explicit dominating-set upper witness.
