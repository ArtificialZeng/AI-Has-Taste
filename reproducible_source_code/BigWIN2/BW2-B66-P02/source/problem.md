# Precise reading of win-00066-p02

## Frozen source and status

The original statement is preserved verbatim in `source.md` (SHA-256
`a68a5a4013b8f9b46447c7c39f4fc25a057355b6db8e45ef07b3ce7db0f5f614`).
This file records its mathematical reading; it does not modify or weaken it.

The minimum-order and order-ten classification question is a newly formulated
question prompted by Georgios Stamoulis, *Integrality Gap Bounds for the
Goemans--Linial SDP on Finite Abelian Cayley Graphs*,
<https://arxiv.org/abs/2609.05368> (v1).  The
supplied PDF has SHA-256
`c21f216511526cc3f0fa4a7d4bc177037bd748272b0bcb497e756c5a412787c0`.
The paper proves a ten-vertex witness but does not assert minimality or give the
requested classification.  Thus the source status at triage is `new-question`,
not a literature-certified open problem.

## Admissible presentations

Write every finite Abelian group additively.  An admissible Cayley presentation
is a pair \((\Gamma,S)\) satisfying all of the following quantifiers and
conditions:

1. \(\Gamma\) is a finite Abelian group of order \(n=|\Gamma|\ge 2\), with
   identity \(0\).
2. \(S\) is a set (not a multiset), \(S\subseteq\Gamma\setminus\{0\}\), and
   \(S=-S\).  Hence generators are repetition-free; an involution, when
   present, occurs once.
3. \(\langle S\rangle=\Gamma\).  In particular, \(S\ne\varnothing\), and the
   Cayley graph below is connected.

The restriction \(n\ge2\) makes the two optimization problems nonempty and is
forced by the cited paper's convention that the input generator multiset is
nonempty.  The one-element group would have no nontrivial cut and neither
displayed optimum would have its intended value.

For such a pair, \(G=\operatorname{Cay}(\Gamma,S)\) has vertex set \(\Gamma\)
and an undirected edge \(\{x,x+s\}\) for every \(x\in\Gamma\) and \(s\in S\).
The set, zero-free, and symmetry assumptions make this a simple, unweighted,
undirected, \(|S|\)-regular graph.  Uniform random-walk normalization means
that \(x\) is uniform in \(\Gamma\) and \(s\) is independently uniform in
\(S\).

## The two exact optima

For every nonempty proper \(A\subsetneq\Gamma\), put

\[
 N_G(A)=\Pr_{x,s}[1_A(x)\ne1_A(x+s)],\qquad
 D(A)=\Pr_{x,y}[1_A(x)\ne1_A(y)]
      =2\frac{|A|}{n}\left(1-\frac{|A|}{n}\right),
\]

where \(x,y\) are independent uniform elements of \(\Gamma\).  Its uniform
sparsity and the cut optimum are

\[
 \psi_G(A)=\frac{N_G(A)}{D(A)},\qquad
 \psi(G)=\min_{\varnothing\ne A\subsetneq\Gamma}\psi_G(A).
\]

Equivalently, if \(\partial A\) is the set of unordered graph edges with one
endpoint in \(A\), then

\[
 \psi_G(A)=\frac{n|\partial A|}{|S|\,|A|(n-|A|)}.
\]

A function \(d:\Gamma^2\to\mathbb R_{\ge0}\) is GL-feasible when there are
real vectors \((v_x)_{x\in\Gamma}\) such that
\(d(x,y)=\|v_x-v_y\|_2^2\), and, in addition, every triangle inequality
\(d(x,z)\le d(x,y)+d(y,z)\) holds.  Distinct vertices may have distance zero.
For a feasible \(d\), define

\[
 N_G(d)=\mathbb E_{x,s}d(x,x+s),\qquad
 D(d)=\mathbb E_{x,y}d(x,y),
\]

and use exactly the paper's uniform-demand Goemans--Linial normalization

\[
 \operatorname{SDP}_{\rm GL}(G)
   =\inf_{\substack{d\text{ GL-feasible}\\D(d)>0}}
       \frac{N_G(d)}{D(d)}.
\]

The general relaxation inequality is
\(\operatorname{SDP}_{\rm GL}(G)\le\psi(G)\).  “Exact” means equality, and a
“non-exact” graph means the strict inequality
\(\psi(G)>\operatorname{SDP}_{\rm GL}(G)\).

## Target and required scope

Determine

\[
 n_*:=\min\bigl\{|\Gamma|:(\Gamma,S)\text{ is admissible and }
 \psi(\operatorname{Cay}(\Gamma,S))>
 \operatorname{SDP}_{\rm GL}(\operatorname{Cay}(\Gamma,S))\bigr\}.
\]

Section 6.4 of arXiv:2609.05368v1 proves that
\(\Gamma=\mathbb Z_{10}\) and \(S=\{\pm1,\pm3\}\) give
\(\operatorname{SDP}_{\rm GL}=3/4\), \(\psi=4/5\), and ratio \(16/15\).
Consequently \(n_*\le10\).

A resolution with \(n_*=10\) must (i) cover every admissible presentation over
every Abelian group of order at most nine and prove exactness, and (ii) classify
all non-exact order-ten graphs up to ordinary graph isomorphism while retaining
all distinct Cayley presentations.  Here presentations \((\Gamma,S)\) and
\((\Gamma',S')\) are equivalent only when a group isomorphism
\(\alpha:\Gamma\to\Gamma'\) satisfies \(\alpha(S)=S'\); multiple inequivalent
presentations of isomorphic abstract graphs must still be recorded.  If instead
a smaller counterexample is found, its strict gap and the absence of examples
at every smaller order must be certified exactly.

For every asserted finite optimum, numerical SDP output is only a search aid.
Required evidence consists of complete finite-group and generator-set orbit
coverage, exhaustive exact cut optimization, and an exact primal/dual or
algebraic certificate for the GL value.

## Nearest results and bounded reduction

The supplied paper was inspected on 2026-09-07 at Corollary 4.7, Section 6.4,
and Questions 7.1--7.2.  Corollary 4.7 proves exactness whenever
\(\exp(\Gamma)\le4\); Section 6.4 supplies the witness above; its concluding
questions concern general gap bounds and rounding, not minimum order.

The primary conference paper by d'Orsi--Jones--Ruotolo--Vadhan--Zhang,
*Sparsest Cut and Eigenvalue Multiplicities on Low Degree Abelian Cayley
Graphs*, APPROX/RANDOM 2025,
<https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2025.16>
(full version <https://arxiv.org/abs/2412.17115>), was inspected on 2026-09-07.
Its Section 1.1.3 and Theorem 9 (conference pages 16:6--16:7) give a
\((1+\varepsilon)\)-approximation algorithm and spectral structure, not this
exact minimum or classification.  Searches on the same date for the exact assertion, the
ten-vertex witness, and equivalent “finite Abelian Cayley GL gap” language
found no primary source settling the new question; this limited search is not
a claim of priority or proof that no such result exists.

By the finite Abelian group classification and Corollary 4.7, all noncyclic
groups of order at most nine are already covered.  The only remaining group
types below ten are \(\mathbb Z_5,\mathbb Z_6,\mathbb Z_7,\mathbb Z_8\), and
\(\mathbb Z_9\).  Direct exact enumeration gives respectively 2, 5, 3, 8, and
6 generator-set orbits under group automorphisms, only 24 cases total.  At
order ten the only group is \(\mathbb Z_{10}\), with 16 such presentation
orbits.  The reproducible enumeration is in `evidence/cyclic_orbits.py`.
