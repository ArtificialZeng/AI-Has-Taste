# Precise problem interpretation

## Frozen decision statement

Decide whether there exist data \((\mathfrak h,V,\mathfrak q)\) such that:

1. \(\mathfrak h\) is a real Lie algebra with \(1\leq\dim_{\mathbb R}\mathfrak h\leq4\);
2. \(V\subseteq\mathfrak h\) is a linear subspace whose generated Lie
   subalgebra is all of \(\mathfrak h\);
3. \(\mathfrak q\subseteq\mathfrak h\) is a vector-space complement,
   \(\mathfrak h=V\oplus\mathfrak q\), satisfying
   \(\kappa_{\mathfrak q}(B)=0\) for every \(B\in V\); and
4. no vector-space complement of this same \(V\) is modularly balanced.

The quantifier in item 4 is universal. Explicitly, for every linear subspace
\(\mathfrak q'\) with \(\mathfrak h=V\oplus\mathfrak q'\), at least one of
the following fails:
\[
 \kappa_V^{\mathfrak q'}(Z)=0\quad(\forall Z\in\mathfrak q'),
 \qquad
 \kappa_{\mathfrak q'}(B)=0\quad(\forall B\in V).
\]
The displayed witness \(\mathfrak q\) in item 3 is included among these
complements; its second condition holds, so it must fail the first if the full
witness exists.

## Definitions and conventions

For a splitting \(\mathfrak h=V\oplus\mathfrak q\), let
\(\pi_V\) and \(\pi_{\mathfrak q}\) denote the associated linear
projections and use \(\operatorname{ad}_B(X)=[B,X]\). Define
\[
 \kappa_V(B)=\operatorname{tr}\!\left(
   \pi_V\operatorname{ad}_B|_V\right),\qquad
 \kappa_{\mathfrak q}(B)=\operatorname{tr}\!\left(
   \pi_{\mathfrak q}\operatorname{ad}_B|_{\mathfrak q}\right).
\]
A complement is modularly balanced precisely when
\[
 \kappa_V|_{\mathfrak q}=0
 \quad\text{and}\quad
 \kappa_{\mathfrak q}|_V=0.
\]
Complements are not required to be Lie subalgebras or ideals. “Lie-generates”
means closure under finite real linear combinations and iterated Lie brackets.
No inner product, Lie group, or map is quantified data in this algebraic target.

After fixing one splitting \(\mathfrak h=V\oplus\mathfrak q\), every other
complement is uniquely a graph
\[
 \mathfrak q_\Psi=\{Z-\Psi Z:Z\in\mathfrak q\},
 \qquad \Psi\in\operatorname{Hom}(\mathfrak q,V).
\]
Thus the universal quantifier over complements can be converted into a finite
symbolic parameter system.

## Source status, nearest result, and scope

The primary source is Nicolussi Golo--Pinamonti--Warhurst, *Harmonic
morphisms of sub-Riemannian Lie groups*, arXiv:2609.04299v1,
<https://arxiv.org/html/2609.04299v1>, inspected on 2026-09-09. Direct
inspection verified Definition 8.2 and equations (57)--(60), Theorem 10.5,
Lemma 10.6 and equations (92)--(93), Theorem 10.7 and equation (97),
Corollary 10.8, and Question 1 in Section 10.2.

Theorem 10.5 uses a modularly balanced complement as a sufficient condition;
Theorem 10.7 obtains only existence of a complement satisfying
\(\kappa_{\mathfrak q}|_V=0\) as a necessary condition. Question 1 explicitly
asks whether the gap can occur, with no dimension restriction. Corollary 10.8
is a negative control: its four-dimensional example has no complement even
satisfying the necessary half-condition and hence is not a witness here.

The exact dimension-at-most-four assertion is a scout-introduced bounded
question, not a claim that the paper labels open. Its source status is therefore
`new-question`, adjacent to the paper's `open-supported` unrestricted Question
1. Targeted exact-phrase searches on 2026-09-09 for “modularly balanced
complement”, “modular mismatch” with polarized Lie algebras, and the text of
Question 1 found no separate primary source settling the bounded assertion.
This limited search is not a priority or openness proof.

A positive exact witness proves the frozen existential statement and answers
the existence part of Question 1. A negative answer through dimension four
requires exhaustive coverage of real Lie-algebra normal forms, continuous
parameters, all bracket-generating subspaces, and all complements; it would
not settle the unrestricted Question 1. The question about normal harmonic
maps in the second sentence of Question 1 is outside scope.

## Proposed contribution and verification route

Nearest prior result: the sufficient/necessary gap in Theorems 10.5 and 10.7.
Proposed delta: either an exact witness of dimension at most four, or a complete
low-dimensional nonexistence theorem. Verification route: exact structure
constants with Jacobi checks, an exact bracket-span certificate for \(V\), and
symbolic graph-complement trace equations. Rational arithmetic is available
through SymPy 1.14.0; algebraic parameters can be introduced only when needed.

