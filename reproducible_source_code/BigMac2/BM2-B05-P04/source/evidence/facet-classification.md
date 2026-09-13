# Exact facet classification and Cohen--Macaulay criterion

This file gives the candidate proof for the frozen statement in `source.md`,
using the precise interpretation in `problem.md`. It is mathematical evidence
for fresh review, not a record of computational certification.

Put
\[
L=r+2,\qquad U=n-2,\qquad m=n+r=L+U.
\]
Thus \(L\ge2\), \(U\ge4\), and \(\Delta_{n,r}\) consists of the subsets of
\([m]\) whose pairwise gaps lie in \([L,U]\).

## Lemma 1 (all facets, including their dimensions)

Let \(S=\{s_0<s_1<\cdots<s_q\}\) be a nonempty face, let
\(g_i=s_i-s_{i-1}\), and let \(D=s_q-s_0\). Then \(S\) is a facet if and
only if
\[
L\le g_i\le 2L-1\quad(1\le i\le q),\qquad
U-L+1\le D\le U. \tag{2}
\]
Consequently, a facet of dimension \(q\ge0\) exists if and only if
\[
qL\le U\quad\hbox{and}\quad q(2L-1)\ge U-L+1. \tag{3}
\]

**Proof.** The face condition itself is equivalent to \(g_i\ge L\) for all
\(i\) and \(D\le U\). If some \(g_i\ge2L\), inserting
\(s_{i-1}+L\) enlarges the face. If \(D\le U-L\), then either
\(s_0>L\), in which case \(s_0-L\) can be inserted, or \(s_0\le L\), in
which case \(s_q+L\le U+L=m\) can be inserted. Hence a facet must satisfy
(2).

Conversely, under (2), a point inserted into an internal gap would require
that gap to be at least \(2L\). A point inserted to the left or right would
make the new diameter at least \(D+L\ge U+1\). Thus no vertex can be added,
so the face is a facet.

For fixed \(q\), the sums of \(q\) integers in \([L,2L-1]\) are exactly all
integers in \([qL,q(2L-1)]\). This interval meets
\([U-L+1,U]\) exactly under (3); choosing \(s_0=1\) realizes the resulting
facet inside \([m]\). This proves the consequence. \(\square\)

Equivalently, the set of facet dimensions is the integer interval
\[
\max\!\left(0,\left\lceil\frac{U-L+1}{2L-1}\right\rceil\right)
\le q\le \left\lfloor\frac UL\right\rfloor. \tag{4}
\]

## Lemma 2 (the low range)

If \(2L\le U\), then \(\Delta_{n,r}\) is not Cohen--Macaulay over any
field.

**Proof.** Write \(U=QL+s\), where \(Q\ge2\) and \(0\le s<L\). Lemma 1
always supplies facets of dimension \(Q\). It also supplies facets of
dimension \(Q-1\) precisely when
\[
(Q-1)(L-1)\ge s+1. \tag{5}
\]
If (5) fails, then \((Q-1)(L-1)\le s\le L-1\). Since \(L\ge2\), this forces
\(Q=2\) and \(s=L-1\). Thus, except when
\[
U=3L-1, \tag{6}
\]
the complex has facets of two different dimensions. A Cohen--Macaulay
simplicial complex is pure, so these cases are not Cohen--Macaulay over any
field.

It remains to treat (6). By (4), the complex is then pure of dimension two.
Orient every edge increasingly and define an integral one-cochain \(\omega\)
by
\[
\omega([a,b])=
\begin{cases}
1,&L\le b-a\le2L-1,\\
2,&2L\le b-a\le3L-1
\end{cases}
\qquad(a<b),
\]
extended antisymmetrically. If \(a<b<c\) is a triangle, then both consecutive
gaps are in \([L,2L-1]\), while their sum is in \([2L,3L-1]\). Therefore
\[
\omega([a,b])+\omega([b,c])-\omega([a,c])=1+1-2=0,
\]
so \(\omega\) is a cocycle over \(\mathbb Z\), and hence after reduction over
every field.

All four terms in the following chain are edges:
\[
z=[1,L+2]-[2,L+2]+[2,2L+1]-[1,2L+1].
\]
Its boundary is zero, whereas
\[
\langle\omega,z\rangle=1-1+1-2=-1. \tag{7}
\]
The value in (7) is nonzero over every field, including characteristic two.
Thus \(z\) cannot be a boundary and
\(\widetilde H_1(\Delta_{n,r};k)\ne0\) for every field \(k\). Reisner's
criterion for this two-dimensional complex now rules out
Cohen--Macaulayness. \(\square\)

Notice that (6) is exactly the pure low-range family
\(n=3r+7\). It is the sole reason a purity-only negative proof would fail.

## Lemma 3 (the high range)

Suppose \(2L>U\).

1. If \(L<U\), then \(\Delta_{n,r}\) is a pure, connected
   one-dimensional complex and is Cohen--Macaulay over every field.
2. If \(L=U\), then \(\Delta_{n,r}\) is a disjoint union of \(L\) edges and
   is not Cohen--Macaulay over any field.
3. If \(L>U\), then \(\Delta_{n,r}\) is a nonempty zero-dimensional complex
   and is Cohen--Macaulay over every field.

**Proof.** When \(L\le U<2L\), (4) says every facet has dimension one. For
\(L<U\), consider the graph whose edges have gaps in \([L,U]\). For every
\(1\le i<U\), the two edges
\[
\{i,i+L+1\},\qquad \{i+1,i+L+1\}
\]
join \(i\) to \(i+1\); their gaps are \(L+1\) and \(L\), and all vertices
shown lie in \([m]\). Hence \(1,\ldots,U\) lie in one component. Every
\(j>U\) is adjacent to \(j-L\in[1,U]\), so the graph is connected. A pure
one-dimensional simplicial complex is Cohen--Macaulay over a field exactly
when it is connected (the one-dimensional case of Reisner's criterion),
proving (1).

If \(L=U\), then \(m=2L\) and the only edges are
\(\{i,i+L\}\), \(1\le i\le L\). This is a disconnected perfect matching,
so Reisner's criterion proves (2). If \(L>U\), no two-element face exists;
the nonempty zero-dimensional complex is Cohen--Macaulay over every field,
which proves (3). \(\square\)

## Conclusion: the frozen biconditional

For integral \(n,r\),
\[
2L>U
\quad\Longleftrightarrow\quad
r\ge\left\lfloor\frac{n-4}{2}\right\rfloor.
\]
Moreover, \(L=U\) is exactly \(r=n-4\), \(L<U\) is \(r\le n-5\), and
\(L>U\) is \(r\ge n-3\). Lemmas 2 and 3 therefore give, for every field
\(k\), every \(n\ge6\), and every \(r\ge0\),
\[
k[\Delta_{n,r}]\text{ is Cohen--Macaulay}
\quad\Longleftrightarrow\quad
r\ge\left\lfloor\frac{n-4}{2}\right\rfloor
\text{ and }r\ne n-4.
\]
There is no characteristic-dependent branch: the nonpurity and connectivity
arguments are field-independent, and the exceptional homology obstruction
pairs to the unit \(-1\) over every field.
