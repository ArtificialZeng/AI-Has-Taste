# Certified partial result for the 17-point unlabeled-poset problem

## Theorem

Let \(U(n)\) be the number of isomorphism classes of \(n\)-element finite
posets. The exact value of \(U(17)\) is not determined here, but the following
integer bounds and disconnected count are certified:
\[
377293651326150106
\;\le U(17)\le\;
15754175376569459236,
\]
and
\[
D(17)=4554367168841547,
\]
where \(D(17)\) counts the disconnected classes. Consequently
\[
U(17)=C(17)+4554367168841547,
\]
and the sole exact unknown is the number \(C(17)\) of connected classes.

The lower bound is a constructive Burnside bound. The upper bound combines
one-point maximal extension with the order-16 relation histogram of
Brinkmann--McKay and the Kruskal--Katona clique bound.

## Proof of the disconnected value

Finite posets decompose uniquely as multisets of connected posets, hence
\[
1+\sum_{n\ge1}U(n)x^n=\prod_{k\ge1}(1-x^k)^{-C(k)}.
\]
To degree 17, the coefficient belonging to at least two components uses only
\(C(1),\ldots,C(16)\), all known from the order-16 enumeration. Expanding
\[
\prod_{k=1}^{16}(1-yx^k)^{-C(k)}
\]
gives the following coefficients of \(x^{17}y^m\):

| \(m\) | count | \(m\) | count |
|---:|---:|---:|---:|
| 2 | 4484639396830962 | 10 | 17905 |
| 3 | 68351780482060 | 11 | 2179 |
| 4 | 1340882409188 | 12 | 332 |
| 5 | 33946665077 | 13 | 64 |
| 6 | 1112290782 | 14 | 14 |
| 7 | 47328664 | 15 | 4 |
| 8 | 2624304 | 16 | 1 |
| 9 | 190010 | 17 | 1 |

Their sum is the displayed value of \(D(17)\). One verifier multiplies the
bivariate Euler factors; a second enumerates integer partitions of 17 and
multisets of connected types; a third reconstructs \(C(1),\ldots,C(16)\)
from \(U(0),\ldots,U(16)\) before recomputing the coefficient.

## Constructive Burnside lower bound

Fix a permutation \(\sigma\in S_{17}\), with distinguishable cycles
\(B_1,\ldots,B_r\) of lengths \(\lambda_1,\ldots,\lambda_r\). Uniformly
blowing up each point of any labeled \(r\)-point poset into the corresponding
cycle gives \(P(r)\) distinct posets fixed by \(\sigma\).

There are additional, explicitly disjoint fixed families. Between cycles of
lengths \(a,b\), the action of \(\langle\sigma\rangle\) on ordered pairs has
\(g=\gcd(a,b)\) orbits.

First order the \(r\) cycles linearly. For every adjacent pair, choose any
nonempty union of its \(g\) pair-orbits and orient it forward; put every
element of every earlier nonadjacent block below every element of the later
block. This is transitive. For the order \(\pi\), it gives
\[
\prod_{i=1}^{r-1}
\bigl(2^{\gcd(\lambda_{\pi_i},\lambda_{\pi_{i+1}})}-1\bigr)
\]
fixed posets. The \(r!\) choices having every adjacent relation complete are
already uniform blow-ups and are subtracted.

Second choose a nonempty matching \(M\) of cycle blocks. Each matched pair
\(i,j\) is made an isolated two-block component, with either orientation and
a nonempty proper union of pair-orbits; its number of choices is
\(2(2^{\gcd(\lambda_i,\lambda_j)}-2)\). Put an arbitrary labeled poset on the
unmatched blocks and blow its relations up uniformly. The set of nonuniform
related block-pairs recovers \(M\), so these objects are distinct. When
\(r=2\) this family is omitted because it is already in the linearly ordered
family; for \(r>2\) its block quotient is disconnected and hence it does not
overlap the linearly ordered family.

Writing \(z_\lambda=\prod_j j^{m_j}m_j!\), the conjugacy class has size
\(17!/z_\lambda\). Summing the three fixed subfamilies over every partition
\(\lambda\vdash17\) gives the exact lower numerator
\[
\begin{aligned}
L={}&134198602505888509372423191552000\\
 &+2210831977844367360\\
 &+5971256590320944751628800\\
={}&134198608477147310525345787548160.
\end{aligned}
\]
Burnside's lemma and integrality therefore give
\[
U(17)\ge \left\lceil\frac{L}{17!}\right\rceil
=377293651326150106.
\]

## One-point-extension upper bound

Every 17-point poset has a maximal point. Delete one such point to obtain a
16-point poset \(Q\). The strict lower set of the deleted point is an order
ideal of \(Q\), and conversely each order ideal defines a maximal one-point
extension. Thus
\[
U(17)\le\sum_{[Q]}d(Q),
\]
where \(d(Q)\) is the number of order ideals and the sum is over order-16
isomorphism classes. This is only an upper bound because different ideals or
different deletions may give isomorphic extensions.

If \(Q\) has \(q\) strict comparable pairs, its order ideals are in bijection
with the independent sets of its comparability graph. They are the cliques,
including the empty set and singletons, in the complement graph with
\(M=\binom{16}{2}-q\) edges. Write
\(M=\binom a2+b\), where \(0\le b<a\). By the Kruskal--Katona theorem, the
colex graph maximizes every clique size. It is \(K_a\), one further vertex
joined to \(b\) vertices of the clique, and isolates, and hence has
\[
I_{16}(q)=2^a+2^b+16-a-1
\]
cliques. For \(M=\binom{16}{2}\), take \(I_{16}(0)=2^{16}\).

Multiplying \(I_{16}(q)\) by the exact order-16 histogram in Table 59 of
Brinkmann--McKay and summing \(q=0,\ldots,120\) yields
\[
U(17)\le15754175376569459236.
\]
One checker uses the closed colex formula; another explicitly constructs each
of the 121 colex graphs and examines all \(2^{16}\) vertex subsets.

## Limitation

These bounds do not determine \(U(17)\). Burnside's lemma would be exact only
after computing the entire fixed-poset count for every cycle type. Already
for type \(2^2 1^{13}\), nonuniform relations between the two 2-cycles bring
in refined statistics such as the total number of marked cover relations over
15-point labeled posets; the available labeled totals and antichain moments do
not supply that statistic. Direct canonical generation at order 17 likewise
remains uncertified and far beyond the completed computation in this project.
