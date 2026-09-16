# Fresh mathematical referee report

**Verdict: accept.** The frozen resolution-paper claim proves the original
nonexistence assertion in its full scope. I found no unresolved mathematical
gap, quantifier mismatch, or unsupported computational inference.

## Scope and snapshot checks

This review is bound to snapshot
ebaf542da85d2cd1eee04a41a4d51aabf659e482fcdeed19b8e0a7ece4498af2
and referee job win-00083-p01-referee-596832173737. I recomputed the SHA-256
digest of every frozen file; all matched audit/snapshot.json. The candidate
statement is logically identical to the assertion in source.md: it ranges
over every finite simple undirected graph on exactly 17 vertices and imposes
only the pairwise-codegree bound and the value 123. It does not silently assume
planarity, regularity, a degree sequence, or an edge count.

## Reconstruction of the reduction

For a putative graph, the codegree hypothesis is exactly ordinary
four-cycle-freeness. Double-counting length-two paths gives

\[
 123=\sum_v\binom{d_v}{2},\qquad
 \sum_v d_v^2=246+2m.
\]

Cauchy--Schwarz gives $4m^2\le17(246+2m)$. This fails at $m=37$, and the
difference of the two sides is increasing thereafter, so $m\le36$.

I checked the cited statements in the frozen copy of arXiv:2609.08803v1. Since
$123>\binom{16}{2}=120$, connectedness follows, so every degree is positive.
There is a minor off-by-one typo in the printed proof of Lemma 5.2: for a
disconnected 17-vertex graph the number of cross-component pairs is at least
16, not 17. The correct bound is already enough here (the target has only
$136-123=13$ zero-codegree pairs), so the lemma's conclusion and this proof
are unaffected. Theorem 5.9 excludes $123=\binom{16}{2}+3$ in the planar,
odd-order case. Corollary 5.8 then places any remaining nonplanar witness in
$5\le\Delta\le9$.

I also reconstructed Lemma 5.3 rather than treating its citation as a black
box. Fix $x$ and set $A=V\setminus N(x)$, so $|A|=17-d_x$. For every
$y\ne x$, at most one neighbor of $y$ lies in $N(x)$; hence at least
$d_y-1$ of its neighbors lie in $A$. Pairs of those neighbors belonging to
two different vertices $y$ would have two common neighbors, contrary to
four-cycle-freeness. Therefore

\[
 \binom{17-d_x}{2}\ge
 \sum_{y\ne x}\binom{d_y-1}{2}.
\]

Thus it is exhaustive to enumerate positive nonincreasing 17-tuples bounded
by 9 satisfying the target binomial sum, even degree sum at most 72,
graphicality, and this inequality for every entry.

## Exact finite check

I reran all three frozen programs. Their saved counts reproduced exactly:
1,368 arithmetic candidates, 1,356 graphical candidates, and eight survivors.
The unpruned program traversed all
$\binom{25}{17}=1{,}081{,}575$ multisets and obtained agreement between the
Erdős--Gallai and Havel--Hakimi tests. In addition, I wrote and ran a fresh
in-memory exhaustive enumeration, with a separately coded Erdős--Gallai loop;
it independently returned the same counts and the same eight multisets:

\[
\begin{array}{c|c|l}
 &m&\text{degrees}\\ \hline
1&34&5^{12},2^3,1^2\\
2&34&5^{11},4^2,2,1^3\\
3&35&5^{11},4,3,2^4\\
4&35&5^{11},3^4,2,1\\
5&35&5^{10},4^3,3,2^2,1\\
6&35&5^9,4^5,3,1^2\\
7&36&5^9,4^3,3^5\\
8&36&5^8,4^6,3^2,2.
\end{array}
\]

The programs use only exact integer arithmetic. The unpruned traversal and
the simple necessary tests make this a reproducible finite reduction rather
than an unsupported solver-status claim.

## Audit of the eight eliminations

Let $H=\{v:d_v=5\}$, $L=V\setminus H$, and
$\epsilon(v)=5-d_v$. For $x\in H$, the sets
$N(y)\setminus\{x\}$, $y\in N(x)$, are pairwise disjoint; otherwise their
common element and $x$ form a four-cycle. Consequently

\[
 \sum_{y\in N(x)}(d_y-1)\le16,
 \qquad D_x:=\sum_{y\in N(x)}\epsilon(y)\ge4.
\]

If $r_x$ counts vertices having no common neighbor with $x$, the same
disjoint union gives the exact identity $r_x=D_x-4$. If $t_x$ is the
number of triangles through $x$, then triangles through $x$ use disjoint
pairs of incident edges: an edge in two triangles would yield a four-cycle.
Thus

\[
 r_x\ge d_x-2t_x,
\]

and in particular every degree-5 vertex has $r_x\ge1$.

Put

\[
 S=\sum_{y\in L}d_y\epsilon(y),\qquad
 C=\sum_{uv\in E(L)}(\epsilon(u)+\epsilon(v)).
\]

Directly counting low-to-high incidences gives

\[
 \sum_{x\in H}D_x=S-C,
 \qquad \sum_{x\in H}r_x=S-C-4|H|. \tag{*}
\]

For cases 1--6, the independently recomputed pairs $(S,4|H|)$ are
$(26,48),(26,44),(34,44),(34,44),(34,40),(34,36)$. Each contradicts
$4|H|\le\sum_H D_x\le S$. In case 7, (*) gives
$\sum_H r_x=6-C\le6$, while the nine odd-degree vertices of $H$ require
the sum to be at least 9.

For case 8, $|H|=8$ and $S=42$, so (*) gives
$R_H=10-C\ge8$, hence $C\le2$. Every low--low edge has cost at least 2,
with equality only for a 4--4 edge. Therefore $q=e(L)\in\{0,1\}$ and
$C=2q$. The low and high degree sums then give

\[
 e(H)=4+q.
\]

Summing $r_x\ge5-2t_x$ over $H$ yields
$T_H:=\sum_Ht_x\ge15+q$. Conversely, all triangles are edge-disjoint. A
triangle with two high vertices can charge its two high incidences to its
unique high--high edge; a triangle with three high vertices charges its three
incidences to its three distinct high--high edges; and a triangle with one
high vertex charges its high incidence to its low--low edge. Hence no
high--high edge receives more than two charges and no low--low edge more than
one, giving

\[
 T_H\le2e(H)+e(L)=8+3q.
\]

This contradicts $T_H\ge15+q$ for both $q=0$ and $q=1$. The eight-case
reduction is exhaustive, so the claimed graph does not exist.

## Contribution and literature scope

The frozen primary source proves only planar nonexistence at this parameter,
reports computation through order 16, and explicitly conjectures that its
nonplanar case does not occur. The candidate supplies the missing order-17
nonplanar elimination by new elementary inequalities after an exact,
independently reproducible degree reduction. This is a substantive full
resolution of the frozen problem, not a toy restriction or routine restatement.
The dated literature record found no later equivalent primary result on
2026-09-09; appropriately, the candidate presents that as a bounded search
record and does not claim priority.

There are no remaining mathematical gaps. For clarity in the eventual
manuscript, I recommend giving the one-line connectedness argument directly
rather than reproducing the source's harmless off-by-one typo.
