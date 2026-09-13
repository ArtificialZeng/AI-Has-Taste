# Formal statement

## Definitions and quantifiers

For an integer \(n\ge 3\), write \([n]=\{1,\dots,n\}\).  For an integer
\(r\), let \(\binom{[n]}r\) be the set of all \(r\)-element subsets of
\([n]\), with the convention that it is empty when \(r<0\) or \(r>n\).

A family \(\mathcal F\subseteq\binom{[n]}4\) is **intersecting** if
\[
  (\forall A,B\in\mathcal F)\quad A\cap B\ne\varnothing.
\]
For each \(S\in\binom{[n]}3\), define its degree in \(\mathcal F\) by
\[
 d_{\mathcal F}(S)=\left|\{E\in\mathcal F:S\subseteq E\}\right|,
 \qquad
 \delta_3(\mathcal F)=\min_{S\in\binom{[n]}3}d_{\mathcal F}(S).
\]
The minimum is over **all** triples of \([n]\), including triples contained
in no member of \(\mathcal F\).

## Finite endpoint theorem to be decided

For each \(n\in\{9,10\}\) and every intersecting family
\(\mathcal F\subseteq\binom{[n]}4\),
\[
  \delta_3(\mathcal F)\le 1.
\]
Equivalently, there is no family \(\mathcal F\subseteq\binom{[n]}4\) such
that simultaneously
\[
  (\forall A,B\in\mathcal F)\ A\cap B\ne\varnothing
  \quad\text{and}\quad
  (\forall S\in\tbinom{[n]}3)\ d_{\mathcal F}(S)\ge2.
\]

## Boolean formulation

Associate a Boolean variable \(x_E\) to each \(E\in\binom{[n]}4\), with
\(x_E=1\) exactly when \(E\in\mathcal F\).  The preceding nonexistence
claim is the unsatisfiability of the conjunction of
\[
 (\neg x_E\lor\neg x_{E'})
 \quad(E,E'\in\tbinom{[n]}4,\ E\cap E'=\varnothing)
\]
and, for every \(S\in\binom{[n]}3\), the exact cardinality constraint
\[
 \sum_{E\supset S}x_E\ge2.
\]
For the CNF encoding used in certification, every cardinality constraint and
every auxiliary variable must be specified explicitly, and equivalence with
the displayed inequality must be checked independently.

## Symmetry, endpoints, and equality convention

The statement is invariant under every permutation of \([n]\); no
normalization is imposed unless its preservation of satisfiability is proved.
There are no real/complex, limiting, compactness, or zero-denominator issues:
the search space is finite.  For the audited endpoints \(n\in\{9,10\}\),
empty and singleton families have \(\delta_3=0\), hence satisfy the
inequality.  Equality means
\(\delta_3(\mathcal F)=1\); for example, every full star
\(\{E\in\binom{[n]}4:i\in E\}\) has equality for \(n\ge4\).

## Relation to the full \((k,d)=(4,3)\) parameter family

By the Gate 1-verified Huang--Zhang Theorem 1.1, every \(n\ge11\) is already
covered.  Therefore proving both finite endpoints above implies
\[
 (\forall n\ge9)(\forall\text{ intersecting }\mathcal F\subseteq
 \tbinom{[n]}4)\quad \delta_3(\mathcal F)\le1.
\]
This last inference uses the external theorem for \(n\ge11\), not a finite
computation beyond \(n=10\).
