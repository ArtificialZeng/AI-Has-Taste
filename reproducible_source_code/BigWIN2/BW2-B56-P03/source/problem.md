# Precise problem reading

## Frozen target

Work over \(R=\mathbb C[x,y,z]\) with the fixed variable order
\(x=x_1<y=x_2<z=x_3\). Let \(\mathcal B_{15}\) be the set of all
zero-dimensional Borel-fixed monomial ideals \(I\subset R\) with

\[
\operatorname{colength}(I)=\dim_{\mathbb C}(R/I)=15.
\]

For every \(I\in\mathcal B_{15}\), compute

\[
T(I)=\dim_{\mathbb C}\operatorname{Hom}_R(I,R/I),
\]

then determine

\[
M_{15}=\max_{I\in\mathcal B_{15}}T(I)
\quad\text{and}\quad
\mathcal M_{15}=\{I\in\mathcal B_{15}:T(I)=M_{15}\}.
\]

The required classification must list every member of \(\mathcal M_{15}\)
by its unique minimal monomial generating set (and preferably also its set of
15 standard monomials). No quotient by variable permutations or other
isomorphisms is implicit: the Borel order \(x<y<z\) is fixed. Any symmetry
compression must be accompanied by an exact expansion back to the actual
ideals.

The yes/no consequence to resolve is

\[
(\forall I\in\mathcal M_{15})\;m_1(I)=3. \tag{C15}
\]

A maximizer with \(m_1\le 2\) disproves (C15); examples that do not attain
\(M_{15}\) are irrelevant to it.

## Definitions and finite encoding

- A monomial ideal is **Borel-fixed** here in the characteristic-zero,
  strongly-stable sense: if a monomial \(u\in I\) is divisible by \(x_i\),
  then \(x_j u/x_i\in I\) for every \(j<i\). It suffices to check this on
  minimal monomial generators.
- Zero-dimensionality is equivalent to the existence of unique least
  positive integers \(m_1,m_2,m_3\) such that
  \(x^{m_1},y^{m_2},z^{m_3}\in I\). Strong stability implies
  \(m_1\le m_2\le m_3\); these are the ordered pure-power exponents used in
  (C15).
- The standard set
  \(O(I)=\{(a,b,c)\in\mathbb N^3:x^ay^bz^c\notin I\}\) has exactly 15
  elements. It is coordinatewise downward closed. Strong stability is
  equivalently encoded on its complement; in particular, if
  \(a_i>0\), \(i<j\), and \(a\in O(I)\), then
  \(a-e_i+e_j\in O(I)\). Thus the census is a finite enumeration of
  size-15 order ideals satisfying these moves.
- \(\operatorname{Hom}_R(I,R/I)\) means \(R\)-module homomorphisms. Using the
  minimal generators as sources and the 15 standard monomials as possible
  images, the syzygy-compatibility equations give a finite integer matrix.
  Its nullity over \(\mathbb Q\) equals its nullity over \(\mathbb C\), so
  exact rational linear algebra is admissible; floating-point ranks are not.

For \(N=3\), colength 15 lies in

\[
\binom{3-1+3}{3}=10\le 15<20=\binom{3+3}{3},
\]

so Conjecture B assigns \(k=3\). The finite statement (C15) is stronger than
the needed implication for a Borel-fixed point that is globally maximal on
\(\operatorname{Hilb}^{15}(\mathbb A^3)\): such a point is necessarily also
maximal inside \(\mathcal B_{15}\). Determining \(M_{15}\) among Borel-fixed
points does **not**, by itself, classify non-Borel points or prove that no
non-Borel point has a larger tangent space.

Only \(m_1=1,2,3\) can occur: if \(m_1\ge4\), strong stability forces every
monomial of total degree below 4 to be standard, already giving colength at
least \(\binom63=20\).

## Literature status and proposed delta

Status on 2026-09-07: **status-uncertain for the full requested atlas and
classification; already computationally supported for (C15).**

1. Rezaee's 2025 paper states Conjecture F and, in its table through
   colength 40, nominates at length 15
   \[
   I_*=(x^3,y^3,z^6,x^2y,x^2z,xy^2,xyz,y^2z,xz^3,yz^3).
   \]
   The conjectural formula gives \(T(I_*)=81\). This is a conjectural family
   claim, not a complete length-15 census or uniqueness classification.
2. Ascott--Rezaee--Zhou, arXiv:2506.17704v2 (2026), Table 1, reports exact
   computer values
   \(T_{\max,1}(15)=45\), \(T_{\max,2}(15)=69\), and
   \(T_{\max,3}(15)=81\), and says its Macaulay2
   computation confirms the monotonicity conjecture for \(10\le l\le35\).
   Hence it directly supports (C15). The paper does not print the full
   length-15 atlas, all tied maximizers, or a replayable length-15 output
   certificate, and its displayed code is only an illustrative call at
   length 35 with a fixed generator count.
3. Rezaee--Saberi, arXiv:2609.04054v1 (2026), Theorem B, proves Conjecture B
   only for the degree families (0.1)--(0.3). At \(k=3\) these cover
   \(10,11,12,13,14,16,17,18,19\), leaving 15 outside that theorem.

Thus the nearest prior result is the reported length-15 maxima
\(69<81\). The proposed delta is a complete independently replayable atlas,
an exact identification of every \(T=81\) tie (or correction of 81 if fresh
computation disagrees), and a second tangent-dimension verification for all
maximizers. This is a precise finite target with an available exact verifier.

## Acceptance scope

A complete result requires: (i) a proof that every member of
\(\mathcal B_{15}\) was enumerated exactly once; (ii) exact \(T(I)\) for every
enumerated ideal; (iii) the value \(M_{15}\); (iv) the full equality list
\(\mathcal M_{15}\); and (v) an independent replay of the decisive dimensions
for all maximizers and all closest \(m_1\le2\) competitors. A single software
run or the published summary table alone is evidence, not the requested
certificate.
