# A self-contained proof for every \(n\ge 9\)

## Theorem

For every integer \(n\ge9\) and every intersecting family
\(\mathcal F\subseteq\binom{[n]}4\),
\[
  \delta_3(\mathcal F)\le1.
\]
The bound is sharp: every full star has minimum triple degree one.

## Proof

Suppose for a contradiction that \(\delta_3(\mathcal F)\ge2\).  In
particular \(\mathcal F\ne\varnothing\), so fix an edge \(E\in\mathcal F\)
and put \(X=[n]\setminus E\).  For each triple \(T\in\binom X3\), define
\[
  C(T)=\{e\in E:T\cup\{e\}\in\mathcal F\}.
\]
Every extension \(T\cup\{x\}\) with \(x\in X\setminus T\) is disjoint
from \(E\), hence is not in \(\mathcal F\).  Consequently
\[
  d_{\mathcal F}(T)=|C(T)|\ge2. \tag{1}
\]

### The case \(n\ge10\)

Here \(|X|=n-4\ge6\), so choose disjoint triples \(T,T'\subseteq X\).
By (1), both \(C(T)\) and \(C(T')\) have at least two elements.  We may
therefore choose distinct \(e\in C(T)\) and \(e'\in C(T')\).  But then
\(T\cup\{e\}\) and \(T'\cup\{e'\}\) are disjoint members of
\(\mathcal F\), a contradiction.

### The case \(n=9\)

Now \(|X|=5\).  For every \(e\in E\), the triple \(E\setminus\{e\}\)
has the edge \(E\) as one extension.  Since its degree is at least two,
choose \(x_e\in X\) such that
\[
  (E\setminus\{e\})\cup\{x_e\}\in\mathcal F. \tag{2}
\]
If \(e\in C(T)\) for a triple \(T\subseteq X\), then
\[
  x_e\in T. \tag{3}
\]
Indeed, otherwise the edge \(T\cup\{e\}\) would be disjoint from the edge
in (2).  By (1) and (3), every triple of \(X\) contains at least two terms
of the four-term multiset \((x_e)_{e\in E}\), counted with multiplicity.

We claim that the map \(e\mapsto x_e\) is injective.  Equivalently, every
pair \(P\subset X\), being the complement of a triple, contains at most two
terms of this multiset.  If some point \(p\) had multiplicity at least two
and another point \(q\) occurred, the pair \(\{p,q\}\) would contain at
least three terms.  If no other point occurred, \(\{p,q\}\) would contain
all four terms for any \(q\ne p\).  Both alternatives contradict the pair
bound.  Thus the claim holds.

There is therefore a unique point \(x_0\in X\setminus\{x_e:e\in E\}\).
Fix \(j\in E\), and let
\[
  S=X\setminus\{x_0,x_j\},
\]
which is a triple.  We shall force three distinct elements into \(C(S)\).

Fix any \(a\in E\setminus\{j\}\), and consider the triple
\(Q_a=\{a,x_0,x_j\}\).  An extension of \(Q_a\) by a point of \(X\) can
belong to \(\mathcal F\) only if the new point is \(x_a\): otherwise it is
disjoint from the edge \((E\setminus\{a\})\cup\{x_a\}\) in (2).  Thus at
most one \(X\)-extension of \(Q_a\) lies in \(\mathcal F\).  Since
\(d_{\mathcal F}(Q_a)\ge2\), there exists some \(b\in E\setminus\{a\}\)
such that
\[
  \{a,b,x_0,x_j\}\in\mathcal F. \tag{4}
\]
For every \(c\in C(S)\), the edge \(S\cup\{c\}\) must intersect (4).
The two edges have disjoint \(X\)-parts, so \(c\in\{a,b\}\).  Hence
\[
  C(S)\subseteq\{a,b\}.
\]
Together with (1), this gives \(C(S)=\{a,b\}\), and in particular
\(a\in C(S)\).  The triple \(S\) was held fixed while \(a\) ranged over
the three elements of \(E\setminus\{j\}\).  Therefore
\(|C(S)|\ge3\), contradicting \(|C(S)|=2\).

Both cases are impossible.  Since triple degrees are integers,
\(\delta_3(\mathcal F)\not\ge2\) is equivalent to
\(\delta_3(\mathcal F)\le1\).  This proves the theorem. \(\square\)

## Endpoint and equality audit

- Empty and singleton families have minimum triple degree zero.
- A full star is intersecting and has minimum triple degree one for every
  \(n\ge4\), so the constant is sharp.  No uniqueness or classification of
  all equality families is claimed.
- The theorem's range is sharp: `discovery/breaker/n8_literal_family.json`
  is an independently verified intersecting family of 35 four-sets on eight
  vertices with \(\delta_3=2\).
- The \(n=9\) proof uses the unique unused point \(x_0\); this is exactly the
  feature that fails at the sharp counterexample endpoint \(n=8\).
