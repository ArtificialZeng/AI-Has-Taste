# Precise problem statement

## Frozen source and interpretation

The immutable statement is in `source.md` (SHA-256
`d9ceaf2415c2dbb550a6bd22c78c6adbad34e4fd6ffe8456ec2ae528d4321210`).
The following fixes notation without changing its mathematical scope.

Let \(R=(X,\le_R)\) be an arbitrary finite poset. Let
\(Q_1=\{0,1\}\) be the two-element chain \(0<1\), and order
\(R\times Q_1\) coordinatewise:
\[
(x,i)\le (y,j)\quad\Longleftrightarrow\quad x\le_R y\text{ and }i\le j.
\]
A subset \(P\subseteq R\times Q_1\) is **order convex** when, for every
\(a,b\in P\) and every \(c\in R\times Q_1\),
\(a\le c\le b\) implies \(c\in P\). Its horizontal sections are uniquely
defined by
\[
P_i=\{x\in X:(x,i)\in P\}\qquad(i=0,1),
\]
so that \(P=(P_0\times\{0\})\cup(P_1\times\{1\})\). Each section \(P_i\)
is itself an order-convex induced subposet of \(R\).

For a finite poset \(S\), \(w(S)\) is the maximum cardinality of a subset
of pairwise incomparable elements, computed in the induced order; set
\(w(\varnothing)=0\). Every product occurring below has the product order.

## Primary universal claim (key lemma)

Determine whether
\[
  2w(P)\ \ge\ w(P_0\times Q_1)+w(P_1\times Q_1) \tag{L}
\]
holds for **every** finite poset \(R\) and **every** order-convex subset
\(P\subseteq R\times Q_1\), including empty sections and \(P=\varnothing\).
No ranked, lattice, Boolean, connectedness, or nonemptiness hypothesis is
permitted.

A disproof requires one explicitly specified finite \(R\) (for example by
its cover relations), an explicitly specified convex \(P\), exact values of
all three widths with maximum-antichain witnesses and upper-bound
certificates, and verification of convexity. Any minimality assertion must
name its metric; the intended first metric is \(|R|\), certified by exhaustive
search of all smaller finite posets. A valid nonminimal counterexample still
disproves (L), but must be described only as near-small if the comparison is
documented.

A proof must cover the full universal quantifiers. In particular, if it uses
the sorting construction in Williams, every auxiliary set must be defined and
both output subsets must be checked for all possible within-layer and
cross-layer comparison directions.

## Conditional downstream claim

Only if (L) is proved, independently check the following implication. For
integers \(n,k\ge0\), let \(Q_n=(2^{[n]},\subseteq)\), with \(Q_0\) the
one-element poset. For every order-convex \(P\subseteq Q_n\), including the
empty set, prove
\[
 w(P\times Q_k)\ \ge\ w(Q_{n+k})\,|P|\,2^{-n}. \tag{T}
\]
Here \(w(Q_m)=\binom{m}{\lfloor m/2\rfloor}\). The intended induction step
views \(Q_{n+1}\cong Q_n\times Q_1\), applies (L) to
\(P\times Q_k\subseteq Q_{n+k}\times Q_1\), and then applies the induction
hypothesis to the two convex sections with parameter \(k+1\). The base
\(n=0\), preservation of convexity, the parameter shift, and the factor
\(2^{-(n+1)}\) all remain part of the required independent verification.
Proving (L) repairs this route only; it does not establish novelty, priority,
or publication status for (T) or the Daykin--Frankl conjecture.

## Source status and nearest prior results

Status at triage on 2026-09-07: **status-uncertain**. Williams's primary
preprint, arXiv:2609.03087v1 (submitted 2026-09-02), states exactly (L) as
Lemma 2 on PDF p.2 and (T) as Theorem 1 on p.2. Its proof of Lemma 2 on p.3
uses a set \(C\) without defining it and replaces the verification of the
second proposed antichain by “hourglass symmetry.” Thus the preprint is a
claim of proof, not currently decisive evidence that the frozen lemma is
correct. The local four-page PDF was inspected and has SHA-256
`d5cb26a66fb4e4ffb03eebd1a6a584b806c89c9dda04adafe2e0054467133549`.

- K. K. Williams, *Confirmation of the Daykin-Frankl Conjecture*,
  arXiv:2609.03087v1, https://arxiv.org/abs/2609.03087 (retrieved
  2026-09-07; Lemma 2 and Theorem 1, PDF p.2; proof, p.3).
- D. E. Daykin and P. Frankl, *Inequalities for subsets of a set and KLYM
  posets*, SIAM J. Algebraic Discrete Methods 4 (1983), 67--69,
  DOI 10.1137/0604009. This is the original conjecture cited by Williams.
- D. Duffus, D. Howard, and I. Leader, *The Width of Downsets*, European
  J. Combin. 79 (2019), 46--59; arXiv:1710.05714. Williams identifies its
  binary-downset case as the nearest established special case, not a proof
  of (L).

No equivalent earlier proof or counterexample to the arbitrary-finite-poset
lemma was identified in the narrowly bounded exact/equivalent-language search.
This search statement is not a claim of novelty or priority. No historical
registry artifact was supplied in this project for a separate duplicate check.

## Triage target

Nearest claimed result: Williams's Lemma 2. Proposed delta: either supply a
complete definition-and-comparability repair, or give an exact counterexample
and locate the failed antichain assertion. Verification route: infer only as a
hypothesis
\[
C=(P_0\cup P_1)\setminus(P_0\cap P_1),
\]
audit both constructed antichains direction by direction, and symmetrically
enumerate all finite posets through five elements (six if feasible), all
convex \(P\subseteq R\times Q_1\), and exact widths. The undefined \(C\) and
the claimed symmetry must not be silently repaired.
