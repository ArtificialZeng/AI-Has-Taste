# Formal statement

## Version repair

The source statement names Conjecture 1.4 of arXiv:2602.02342v1.  In the
current arXiv version, v2 (8 February 2026), the same mathematical statement
is Conjecture 1.5.  Version 2 explicitly says that it was verified for
\(n\leq 4\).  The project studies the unchanged mathematical assertion at
\(n=5\), not the conjecture number.

## Definitions and quantifiers

Fix a field \(\mathbb{k}\) of characteristic zero and a Lie algebra
\(\mathfrak g\) over \(\mathbb{k}\).  No finite-dimensionality hypothesis is
imposed on \(\mathfrak g\).  Let \(C\) be a set and let
\[
 r:C\longrightarrow \mathfrak g\otimes\mathfrak g,
 \qquad c\longmapsto r^{(c)}
\]
be a family satisfying the **transitive CYBE**: for every
\(c,c',c''\in C\) such that \(c'\in\{c,c''\}\),
\[
 T(c,c',c''):=
 [r^{(c)}_{12},r^{(c')}_{13}]
 +[r^{(c)}_{12},r^{(c'')}_{23}]
 +[r^{(c')}_{13},r^{(c'')}_{23}]=0
\]
in \(U(\mathfrak g)^{\otimes3}\).

Let \([5]=\{1,2,3,4,5\}\), and let
\(a:[5]\times[5]\to C\), \((i,j)\mapsto a_{ij}\), satisfy
\[
 a_{ik}\in\{a_{ij},a_{jk}\}
 \qquad\text{for every }i,j,k\in[5].
\]
Put \(\mathfrak h=\mathfrak g^{\oplus5}\), and write
\(\iota_p:\mathfrak g\to\mathfrak h\) for the inclusion into the
\(p\)-th summand.  For \(x\in\mathfrak g\otimes\mathfrak g\), set
\(x^{p,q}=(\iota_p\otimes\iota_q)(x)\).  Define
\[
 R(a)=\mathbf r^{(a)}
 :=\sum_{i,j=1}^{5}\bigl(r^{(a_{ij})}\bigr)^{j,i}
 \in\mathfrak h\otimes\mathfrak h.
\]
This is exactly formula (1.2) of the source, rewritten in
\(\mathfrak g^{\oplus5}\otimes\mathfrak g^{\oplus5}\) notation.

The endpoint to prove is
\[
 \operatorname{CYB}_{\mathfrak h}(R(a))
 =[R(a)_{12},R(a)_{13}]
  +[R(a)_{12},R(a)_{23}]
  +[R(a)_{13},R(a)_{23}]=0
\]
in \(U(\mathfrak h)^{\otimes3}\).

## Normalizations and invariances

No normalization of \(r^{(c)}\) is made.  Simultaneous relabeling of colors
and simultaneous permutation of the five direct-sum indices preserve the
hypotheses and conclusion.  Although \(C\) may be infinite, only the finite
image of \(a\) occurs in \(R(a)\).

## Edge and degenerate cases

The statement includes \(\mathfrak g=0\), the zero family, repeated or
identical colors, constant arrays, arbitrary diagonal entries compatible with
transitivity, and triples of indices with repetitions.  If \(C=\varnothing\),
no map \([5]^2\to C\) exists, so the implication is vacuous.  No division,
genericity, rank assumption, or limiting argument is permitted.

## Stronger endpoint under investigation

The same definitions make sense for every integer \(n\ge1\).  A proof uniform
in \(n\) is admissible only if it explicitly covers repeated component indices
and reconstructs the ordinary CYBE residual from the transitive-CYBE
relations without assuming linear independence of overlapping embeddings.
