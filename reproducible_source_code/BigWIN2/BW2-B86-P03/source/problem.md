# Precise reading

## Frozen input and ambient objects

The immutable input is `source.md`, whose SHA-256 at intake is
`9b0a3b9fc1ae610c9ab9e3165640b060077794cfe36987fb04833f06c658b2dd`.
All arithmetic below is in the prime field
\(\mathbb F_{11}=\mathbb Z/11\mathbb Z\).  Projective coordinates satisfy
\((X:Y:Z)=(\lambda X:\lambda Y:\lambda Z)\) for every
\(\lambda\in\mathbb F_{11}^{*}\).

For every function \(h:\mathbb F_{11}\to\mathbb F_{11}\), define
\[
 \Gamma_h=\{(x,h(x)):x\in\mathbb F_{11}\}\subset\mathbb F_{11}^{2}
\]
and
\[
 S_h=\{(x:h(x):1):x\in\mathbb F_{11}\}
      \cup\{(0:1:0)\}\subset\operatorname{PG}(2,11).
\]
The two fixed functions are
\(f(x)=x^4\) and \(g(x)=x^8\), evaluated on every element of
\(\mathbb F_{11}\).

Because \(\mathbb F_{11}\) has no nonidentity field automorphism, the
paper's projective collineations in \(\operatorname{P\Gamma L}(3,11)\)
are precisely those induced here by \(\operatorname{PGL}(3,11)\).

## Quantified claim

The source asks for the conjunction of the following two statements.

1. **Projective equivalence:** there exists \(M\in\operatorname{GL}(3,11)\)
   such that its induced projectivity maps \(S_f\) onto \(S_g\).
2. **CCZ inequivalence:** for every \(A\in\operatorname{GL}(2,11)\) and
   every \(t\in\mathbb F_{11}^{2}\),
   \[
       A\Gamma_f+t\ne\Gamma_g.
   \]

Equivalently, the task is to prove both clauses, or to give an exact
counterexample to at least one.  A certificate must account for the affine
zero point and the point at infinity in the first clause, and must rule out
all affine permutations of the 121-point affine plane in the second.

For a graph \(\Gamma\) and a nonzero vector
\(w\in\mathbb F_{11}^{2}\), define the ordered difference count
\[
 \Delta_\Gamma(w)=
 \#\{(P,Q)\in\Gamma^2:P-Q=w\}.
\]
If \(T(z)=Az+t\) is an affine permutation and
\(T(\Gamma)=\Gamma'\), then
\(\Delta_{\Gamma'}(Aw)=\Delta_\Gamma(w)\) for every \(w\ne0\): the map
\((P,Q)\mapsto(T(P),T(Q))\) is a bijection and translations cancel in
differences.  Since \(A\) permutes the 120 nonzero vectors, the multiset
\(\{\Delta_\Gamma(w):w\ne0\}\) is therefore a CCZ invariant in this
setting.

## Scope and nearest prior result

The field, functions, graph convention, added point at infinity, and both
equivalence notions are fixed.  Changing any of them is outside this problem.
EA inequivalence alone does not prove CCZ inequivalence.

Primary source inspected on 2026-09-10:

- Sophie Huczynska, Lukas Klawuhn, and Maura B. Paterson, *The Intersection
  Distribution: New Results and Perspectives*, arXiv:2510.04675v2,
  <https://arxiv.org/abs/2510.04675> and
  <https://arxiv.org/pdf/2510.04675>.
- Theorem 2.9, Corollary 2.10, and Example 2.11 (printed p. 9; PDF page 9)
  prove that \(x^4\) and \(x^8\) over \(\mathbb F_{11}\) are projectively
  equivalent and note only that their different degrees preclude
  EA-equivalence.
- Definition 2.14 (printed p. 12; PDF page 13) gives CCZ equivalence as an
  invertible affine transformation between graphs.  Open Problem 4 (printed
  p. 34; PDF page 34) asks whether any projectively equivalent polynomials
  can fail to be CCZ-equivalent.

Thus the source status is **open-supported** for the broader existence
question as of arXiv v2, while the projective half of this exact pair is
already known.  The proposed delta is a rigorous CCZ separation for this
pair; its bounded verification route is exact enumeration of all 120
nonzero graph differences together with an explicit projective matrix.
Targeted arXiv searches on 2026-09-10 found no later primary paper resolving
this exact pair or Open Problem 4; this limited negative search is not a
priority or open-status proof.
