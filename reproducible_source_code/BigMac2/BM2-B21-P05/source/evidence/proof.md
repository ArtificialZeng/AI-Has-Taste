# Proof certificate for bigMac-00021-p05

## Claim

For \(H(3,3)=K_3\square K_3\square K_3\), under the weak-majority and
surjectivity conventions fixed in problem.md,

\[
\bar\chi_{\ge}(H(3,3))=4.
\]

## Two elementary graph facts

Write vertices as triples in \([3]^3\), with adjacency meaning difference in
exactly one coordinate.

1. **There is no clique of order four.** For a fixed vertex \(v\), divide its
   six neighbors into three pairs according to the coordinate in which they
   differ from \(v\). The two vertices in one pair are adjacent, whereas two
   vertices from different pairs differ in two coordinates and are not
   adjacent. A clique containing \(v\) can therefore contain at most the two
   members of one pair, so its order is at most three.

2. **Every adjacent pair has exactly one common neighbor.** Suppose \(x,y\)
   differ in coordinate \(i\). If a common neighbor \(z\) differed from \(x\)
   in a coordinate \(j\ne i\), then \(z\) would differ from \(y\) in both \(i\)
   and \(j\), which is impossible. Hence \(z\) agrees with \(x,y\) outside
   coordinate \(i\), and its \(i\)-th entry must be the unique third member of
   \([3]\setminus\{x_i,y_i\}\). That triple is indeed a common neighbor.

## Minimum size of a color class

**Lemma.** If a nonempty set \(S\subseteq[3]^3\) satisfies
\(\delta(H(3,3)[S])\ge3\), then \(|S|\ge6\).

**Proof.** Sizes at most three are excluded by the general bound
\(\delta(H[S])\le |S|-1\). If \(|S|=4\), minimum degree at least three would
make \(H[S]\) a \(K_4\), contrary to fact 1.

Suppose instead that \(|S|=5\). In the complement of \(H[S]\), every vertex
has degree at most one, so the missing edges form a matching. If at most one
edge is missing, four vertices span a \(K_4\), again contradicting fact 1. The
only remaining case has two missing edges, say \(ab\) and \(cd\), with fifth
vertex \(e\). Then \(e\) and \(a\) are adjacent and have both \(c\) and \(d\)
as common neighbors. This contradicts fact 2. Thus no size at most five is
possible. \(\square\)

Consequently every color class in a majority \(C\)-coloring has at least six
vertices. If the coloring has \(p\) colors, its nonempty classes partition the
27 vertices, so \(6p\le27\), and hence \(p\le4\).

## Four-color construction

Let

\[
C_0=\{1\}\times[3]\times[3],\qquad
C_j=\{2,3\}\times\{j\}\times[3]\quad(j=1,2,3).
\]

These four nonempty sets are pairwise disjoint and cover \([3]^3\). Every
vertex of \(C_0\) has four neighbors in \(C_0\), obtained by changing its
second or third coordinate. Every vertex of \(C_j\) has three neighbors in
\(C_j\): one obtained by changing its first coordinate within \(\{2,3\}\),
and two obtained by changing its third coordinate. Thus coloring each \(C_i\)
with its own color is a surjective majority \(C\) four-coloring, and \(p\ge4\).

Together with \(p\le4\), this proves the claim. \(\square\)

## Reproducible exact cross-check

The script evidence/verify_resolution.py independently enumerates all
\(\sum_{k=1}^5\binom{27}{k}=101{,}583\) subsets of sizes one through five,
finds none with induced minimum degree at least three, and verifies the stated
partition, coverage, class sizes, and all induced degrees. Its captured output
is evidence/verify_resolution.out. This computation is a cross-check; the
proof above does not depend on it.
