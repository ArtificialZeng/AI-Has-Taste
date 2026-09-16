# win-00076-p03 — dimension-at-most-four modular-mismatch witness

## Immutable primary-source record

- Primary source: Sebastiano Nicolussi Golo, Andrea Pinamonti, and Ben
  Warhurst, *Harmonic morphisms of sub-Riemannian Lie groups*,
  arXiv:2609.04299v1 [math.DG], 3 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.04299v1>
- Official HTML: <https://arxiv.org/html/2609.04299v1>
- Definition locators: Section 4.3 (a polarization is a bracket-generating
  linear subspace); equation (22) (the modular character
  \(\kappa_{H}=\operatorname{tr}\circ\operatorname{ad}\)); Definition 8.2
  and equations (57)–(60) (complements, the two projected trace characters,
  modular mismatch, and modular balance).
- Problem-boundary locators: Theorem 10.5 (modular balance is sufficient),
  Lemma 10.6 and equations (92)–(93) (all complements as graph changes and
  the transformation of \(\kappa_{\mathfrak q}|_V\)), Theorem 10.7 and
  equation (97) (the necessary half-condition), and Section 10.2,
  explicit Question 1.
- Negative control: Definition 9.1, Lemma 9.2, and Corollary 10.8 give a
  four-dimensional polarized algebra having no complement satisfying even
  \(\kappa_{\mathfrak q}|_V=0\); it is therefore not a witness to the gap
  asked about here.
- Access record: official arXiv v1 HTML read directly on 2026-09-09 under the
  batch-76 primary-source fallback.

## Frozen existential assertion

Decide whether the following statement is true:
\[
\begin{aligned}
\exists\,&\text{a finite-dimensional real Lie algebra }\mathfrak h,
\quad 1\leq \dim\mathfrak h\leq4,\\
\exists\,&V\leq\mathfrak h\text{ that Lie-generates }\mathfrak h,\\
\exists\,&\mathfrak q\leq\mathfrak h\text{ with }
\mathfrak h=V\oplus\mathfrak q
\text{ and }\kappa_{\mathfrak q}|_V=0,
\end{aligned}
\]
but \((\mathfrak h,V)\) has no modularly balanced complement.

Here \(\operatorname{ad}_B(X)=[B,X]\).  For each vector-space complement
\(\mathfrak q\) and the corresponding projections \(\pi_V,\pi_{\mathfrak q}\),
Definition 8.2 sets
\[
\kappa_V(B)=\operatorname{tr}
  \bigl(\pi_V\operatorname{ad}_B|_V\bigr),\qquad
\kappa_{\mathfrak q}(B)=\operatorname{tr}
  \bigl(\pi_{\mathfrak q}\operatorname{ad}_B|_{\mathfrak q}\bigr).
\]
The condition \(\kappa_{\mathfrak q}|_V=0\) therefore means
\[
\operatorname{tr}
  \bigl(\pi_{\mathfrak q}\operatorname{ad}_B|_{\mathfrak q}\bigr)=0
\qquad\forall B\in V.
\]
By equation (60), a complement \(\mathfrak q'\) is modularly balanced exactly
when both
\[
\operatorname{tr}
  \bigl(\pi_V'\operatorname{ad}_Z|_V\bigr)=0
  \quad\forall Z\in\mathfrak q',
\qquad
\operatorname{tr}
  \bigl(\pi_{\mathfrak q'}\operatorname{ad}_B|_{\mathfrak q'}\bigr)=0
  \quad\forall B\in V
\]
hold.  Thus “no modularly balanced complement” quantifies over every
vector-space complement \(\mathfrak q'\) of the same \(V\), not merely the
displayed witness complement \(\mathfrak q\).

No inner product, Lie group, or map is additional data in this frozen target:
Definition 8.2 notes that these trace conditions depend only on
\((\mathfrak h,V)\) and the chosen complement.

## Nearest result and exact delta

Theorem 10.5 uses existence of a modularly balanced complement as a sufficient
condition.  Theorem 10.7 extracts only
\(\kappa_{\mathfrak q}|_V=0\) as a necessary condition.  Section 10.2 states
that this is the first half of equation (60), and Question 1 asks whether a
polarized Lie algebra can satisfy that necessary half for some complement
while admitting no complement satisfying both halves.

The paper imposes no dimension bound.  The restriction
\(\dim\mathfrak h\leq4\) is a scout-imposed bounded witness search, not a
source theorem, conjecture, or claimed threshold.  A single exact witness in
this range answers the existence sentence of Question 1 positively without
any classification.  Conversely, even a complete proof that no such witness
exists through dimension four would leave the unrestricted source question
open.  The second sentence of Question 1, concerning normal harmonic maps, is
outside this target.

## Cheapest decisive attack

Start with exact real Lie-algebra normal forms in dimensions at most four and
bracket-generating subspaces \(V\), prioritizing codimension-one polarizations.
For one fixed complement \(\mathfrak q\), verify
\(\kappa_{\mathfrak q}|_V=0\) by exact trace arithmetic.  Lemma 10.6 supplies
the useful complement chart
\[
\mathfrak q_{\Psi}=\{Z-\Psi Z:Z\in\mathfrak q\},
\qquad \Psi\in\operatorname{Hom}(\mathfrak q,V),
\]
which covers every complement of \(V\).  Substitute this chart into both
trace conditions in equation (60).  Search first for rational structure
constants and rational \(V\); use algebraic parameters only if needed.

A positive certificate consists of:

- a basis and exact structure constants for \(\mathfrak h\), with
  antisymmetry and every Jacobi identity checked;
- an exact basis of \(V\) and a finite bracket-span certificate that it
  Lie-generates \(\mathfrak h\);
- an exact complement \(\mathfrak q\) and trace calculation proving
  \(\kappa_{\mathfrak q}|_V=0\);
- a symbolic parameterization of every complement \(\mathfrak q_{\Psi}\) and
  an exact inconsistency certificate showing that the two systems in
  equation (60) have no common solution.

Finding one such object proves the frozen existential assertion and answers
the existence part of the source question.  The source's four-dimensional
example is a fail-fast control: Corollary 10.8 proves that it has no complement
satisfying \(\kappa_{\mathfrak q}|_V=0\), so reproducing it is not progress on
this target.

## Failure and claim boundaries

- Failure to find a witness in a finite list, random search, or numerical
  parameter sample does not disprove the existential assertion.
- A negative dimension-at-most-four result requires exhaustive real
  normal-form coverage, all continuous parameters and all
  bracket-generating polarizations, together with the all-complements
  quantifier.  A merely bounded search without that completeness proves
  neither low-dimensional nonexistence nor the unrestricted Question 1.
- Exhibiting one complement with \(\kappa_{\mathfrak q}|_V=0\) is only the
  first half of a witness; one must rule out every modularly balanced
  complement.
- The dimension cutoff establishes no literature novelty.  Any positive
  witness still needs a separate literature audit before a novelty claim.
