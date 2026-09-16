# Precise reading: the order-17 common-neighbor gap

Triage provenance: `win-00083-p01-triage-304408ba73ba`  
Frozen input: `source.md`, SHA-256
`66dca795135d1d39b33ac000c548a361beb67db39de0cf00381572244e2790f7`.

## Definitions and quantifiers

A finite simple undirected graph is a pair \(G=(V,E)\), where \(V\) is a
finite set and \(E\subseteq\binom V2\). Thus loops, multiple edges,
orientations, and weights are excluded. For \(x\in V\), define

\[
N_G(x)=\{u\in V:\{x,u\}\in E\},\qquad d_G(x)=|N_G(x)|.
\]

The frozen assertion is exactly

\[
\neg\exists G=(V,E)\;\Bigl[
 |V|=17,
 \quad \forall x,y\in V\;(x\ne y\Rightarrow
 |N_G(x)\cap N_G(y)|\le 1),
 \quad \sum_{u\in V}\binom{d_G(u)}2=123
\Bigr].
\]

The existential quantifier ranges over **all** simple undirected graphs on
exactly 17 vertices. Planarity, connectedness, regularity, a degree sequence,
and an edge count are not hypotheses. Here
\(\binom d2=d(d-1)/2\), including value zero for \(d=0,1\).

Two distinct vertices have two distinct common neighbors if and only if the
four vertices contain a (not necessarily induced) \(4\)-cycle. Consequently,
the codegree condition is equivalent to \(C_4\)-freeness in the ordinary
subgraph sense. Double-counting length-two paths with unordered distinct
endpoints gives

\[
\sum_{u\in V}\binom{d_G(u)}2
=\sum_{\{x,y\}\in\binom V2}|N_G(x)\cap N_G(y)|.
\]

Under the codegree bound, the value 123 therefore means that exactly 123 of
the \(\binom{17}{2}=136\) unordered vertex pairs have one common neighbor and
the remaining 13 have none. This is the source realization question for
\(\gamma_{123}=(1^{123},0^{13})\) in \(\mathcal Q_{17}\).

## Source status and nearest prior result

Status at triage on 2026-09-09: **open-supported**, not known. The inspected
primary source is Ascolese--Negrini--Pagani--Pellegrini,
[*A graph reconstruction problem involving common neighbors*](https://arxiv.org/abs/2609.08803),
arXiv:2609.08803v1 (submitted 2026-09-08). Its Lemma 3.1 proves the displayed
double count. Lemma 5.2 makes any relevant witness connected. Corollary 5.8
(PDF p. 19) reduces a witness at \(v=17\) to either the high-degree planar case
or a nonplanar graph with \(5\le\Delta(G)\le9\), and the sentence immediately
after it conjectures that the latter case never occurs. Theorem 5.9
(PDF pp. 19--20) excludes \(c=\binom{16}{2}+3=123\) for **planar** graphs only.
The source reports Magma/nauty verification only through order 16.

A bounded exact-assertion/equivalent-language search on 2026-09-09 found no
later primary result settling the order-17 instance; because v1 appeared only
one day earlier, this is a search record rather than a priority guarantee.
The Afzaly--McKay authoritative
[*Extremal Graphs and Turan numbers*](https://users.cecs.anu.edu.au/~bdm/data/extremal.html)
table (retrieved 2026-09-09) records
\(\operatorname{ex}(17,C_4)=36\) and one extremal isomorphism class. The needed
36-edge bound also follows independently from the target equation: if
\(m=|E|\), Cauchy--Schwarz gives

\[
123=\frac12\left(\sum_{u\in V}d_G(u)^2-2m\right)
\ge \frac{2m^2}{17}-m,
\]

which fails for every integer \(m\ge37\). The extremal row alone does not
settle the 34- and 35-edge cases.

## Triage reduction and target

Combining connectedness, \(5\le\Delta\le9\), the Cauchy 36-edge bound, the
handshaking lemma, graphicality, and source Lemma 5.3 leaves exactly eight degree
multisets; this exact finite calculation is reproducible in
`evidence/triage_degree_filter.py` and `evidence/triage_degree_filter.txt`.
All eight have maximum degree five and 34--36 edges.

Nearest prior result \(X\): planar nonexistence and the source reductions above.
Proposed delta \(Y\): decide the remaining order-17 nonplanar instance.
Verification route \(Z\): exhaust the eight degree multisets with an exact
adjacency encoding of degrees and pairwise codegree at most one. Any satisfying
assignment is to be checked directly; nonexistence requires frozen instances,
independently checked UNSAT certificates, and a human-checkable proof that the
degree reduction is exhaustive. A solver status by itself is not a proof.
