# Proof dossier: the order-17 common-neighbor gap

This dossier proves the frozen assertion in `source.md`.  It uses the cited
paper only for its planar nonexistence theorem and its stated necessary
reductions; the new elimination of the eight remaining degree multisets is
given below.  All graphs are finite, simple, and undirected.

## 1. Reduction to eight degree multisets

Suppose that a graph \(G\) satisfies the frozen hypotheses.  Put \(d_v=\deg v\)
and \(m=|E(G)|\).  The target equation gives

\[
 \sum_v d_v^2=246+2m.
\]

Cauchy--Schwarz therefore gives
\(4m^2\le17(246+2m)\).  The left side minus the right side is positive at
\(m=37\) and is increasing thereafter, so \(m\le36\).

Here \(123>\binom{16}{2}=120\).  Source Lemma 5.2 makes \(G\) connected, so
all degrees are positive.  Source Theorem 5.9 excludes a planar \(G\) at the
target value.  Source Corollary 5.8 then gives \(5\le\Delta(G)\le9\).
Finally source Lemma 5.3 gives, for every vertex \(x\),

\[
 \binom{17-d_x}{2}\ge
 \sum_{y\ne x}\binom{d_y-1}{2}. \tag{1}
\]

Enumerating nonincreasing 17-tuples of integers in \([1,9]\), subject to
\(\max d_v\in[5,9]\), \(\sum\binom{d_v}{2}=123\), even degree sum at most
72, graphicality, and (1), gives exactly the following table.

| case | \(m\) | degree multiset |
|---:|---:|---|
| 1 | 34 | \(5^{12},2^3,1^2\) |
| 2 | 34 | \(5^{11},4^2,2,1^3\) |
| 3 | 35 | \(5^{11},4,3,2^4\) |
| 4 | 35 | \(5^{11},3^4,2,1\) |
| 5 | 35 | \(5^{10},4^3,3,2^2,1\) |
| 6 | 35 | \(5^9,4^5,3,1^2\) |
| 7 | 36 | \(5^9,4^3,3^5\) |
| 8 | 36 | \(5^8,4^6,3^2,2\) |

This finite step has three exact implementations.  The original triage program
`triage_degree_filter.py` uses a pruned sorted-tuple recursion and
Erdos--Gallai; `research_degree_check.py` uses multiplicity recursion and
Havel--Hakimi.  As a pass-2 cross-check,
`research_pass2_crosscheck.py` traverses without pruning all
\(\binom{25}{17}=1{,}081{,}575\) nondecreasing 17-multisets from
\(\{1,\ldots,9\}\) and requires NetworkX's Erdos--Gallai and Havel--Hakimi
implementations to agree.  All calculations are exact integers.  All three
programs return 1,368 arithmetic tuples, 1,356 graphical tuples, and the same
eight survivors; their programs and saved outputs make the bounds and loop
ranges inspectable.

## 2. Two elementary C4-free lemmas

Set \(H=\{v:d_v=5\}\), and for every vertex set
\(\epsilon(v)=5-d_v\).  In all eight rows \(\epsilon(v)\ge0\).

For every vertex \(x\), the sets
\(N(y)\setminus\{x\}\), as \(y\) ranges over \(N(x)\), are pairwise disjoint:
an element in two of them would make a 4-cycle.  Hence

\[
 \sum_{y\in N(x)}(d_y-1)\le16. \tag{2}
\]

For \(x\in H\), (2) is equivalent to

\[
 D_x:=\sum_{y\in N(x)}\epsilon(y)\ge4. \tag{3}
\]

Let \(r_x\) be the number of vertices \(z\in V\setminus\{x\}\) having no
common neighbor with \(x\).  The union of the pairwise-disjoint sets in (2)
is exactly the set of the other vertices that do have a common neighbor with
\(x\).  Thus, for \(x\in H\),

\[
 r_x=16-\sum_{y\in N(x)}(d_y-1)=D_x-4. \tag{4}
\]

Every odd-degree vertex satisfies \(r_x\ge1\).  Indeed, an incident edge has
a common neighbor precisely when it lies in a triangle.  No edge can lie in
two triangles: if \(uv\) had distinct third vertices \(a,b\), then
\(a-u-b-v-a\) would be a 4-cycle.  Thus triangles through \(x\) use disjoint
pairs of incident edges; an odd number of incident edges leaves at least one
edge in no triangle, and its other endpoint is counted by \(r_x\).  More
generally, if \(t_x\) is the number of triangles through \(x\), the
\(d_x-2t_x\) incident edges not lying in a triangle have distinct other
endpoints counted by \(r_x\).  Hence

\[
 r_x\ge d_x-2t_x, \tag{5}
\]

where \(t_x\) is the number of triangles through \(x\).

## 3. Elimination of cases 1--7

For a fixed row define the total low-degree deficiency supply

\[
 S=\sum_{y\notin H}d_y\epsilon(y).
\]

Summing (3) over \(H\), and observing that a low vertex \(y\) can supply
\(\epsilon(y)\) to at most all \(d_y\) of its neighbors, gives

\[
 4|H|\le\sum_{x\in H}D_x\le S. \tag{6}
\]

For cases 1--6, the pairs \((S,4|H|)\) are respectively
\((26,48),(26,44),(34,44),(34,44),(34,40),(34,36)\).  Each contradicts (6).

For a more exact sum, let \(L=V\setminus H\), and let

\[
 C=\sum_{uv\in E(G[L])}(\epsilon(u)+\epsilon(v))\ge0.
\]

Every low--low edge consumes the indicated supply at its two endpoints, so
\(\sum_{x\in H}D_x=S-C\).  By (4),

\[
 \sum_{x\in H}r_x=S-C-4|H|. \tag{7}
\]

In case 7 this is \(6-C\le6\), whereas all nine vertices of \(H\) have odd
degree and hence make the same sum at least 9.  This is a contradiction.

## 4. Elimination of case 8

Here \(|H|=8\), and the low vertices comprise six degree-4, two degree-3,
and one degree-2 vertices.  Thus \(S=42\), and (7) says

\[
 R_H:=\sum_{x\in H}r_x=10-C.
\]

Odd-degree parity gives \(R_H\ge8\), hence \(C\le2\).  Every low--low edge
has cost at least 2, with equality only for an edge joining two degree-4
vertices.  Consequently either there are no low--low edges, or there is
exactly one and it is a 4--4 edge.  Write \(q\in\{0,1\}\) for their number;
then \(C=2q\).

The low degree sum is 32, so the number of high--low edges is \(32-2q\).
The high degree sum is 40, and hence the number of high--high edges is

\[
 e(H)=\frac{40-(32-2q)}2=4+q. \tag{8}
\]

Let \(T_H=\sum_{x\in H}t_x\), the number of high-vertex incidences with
triangles.  Summing (5) over \(H\) and using \(R_H=10-2q\) gives

\[
 T_H\ge\frac{40-R_H}{2}=15+q. \tag{9}
\]

On the other hand, triangles are edge-disjoint by the 4-cycle argument above.
Charge the high incidences of each triangle as follows.  For a triangle with
two high vertices, charge both incidences to its unique high--high edge; for a
triangle with three high vertices, charge each incidence to a different one
of its three high--high edges; and for a triangle with one high vertex, charge
its one high incidence to the unique low--low edge.  Each high--high edge then
receives at most two charges and each low--low edge at most one.  Consequently,

\[
 T_H\le2e(H)+e(L)=2(4+q)+q=8+3q. \tag{10}
\]

For both \(q=0\) and \(q=1\), (9) is strictly larger than (10).  This final
contradiction eliminates case 8.  Since the reduction was exhaustive, no
graph satisfying the frozen assertion exists.

## Gap list

Empty.  A fresh referee should independently audit the cited source statements,
the exact eight-row enumeration, and the charging inequality (10).
