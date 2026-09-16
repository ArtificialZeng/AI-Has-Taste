# Precise interpreted problem

Source: `source.md`, preserved verbatim. SHA-256:
`325f63401375df5dd244202933368387e95d52d13d24097e6e8fd2b5e37317f9`.
Job: `primary-20260914-arbor-ehrhart-words-triage-5bfaab9809a5`.

For every integer \(n\ge1\), every set partition \(\pi\) of
\([n]=\{1,\ldots,n\}\) into nonempty blocks, and every rooted tree
\(\tau\) with vertex set \(\pi\), let \(B_v=v\),
\(b_v=|B_v|\), and let \(D_v\) be the union of all blocks in the subtree
rooted at \(v\), including \(B_v\). Put \(N_v=|D_v|\).
There is no planarity assumption or restriction on block labels, sizes, depth,
or branching. A child is one edge farther from the root.

Define the full-dimensional lattice polytope
\[
Q_\tau=\{x\in\mathbb R_{\ge0}^n:\sum_{i\in D_v}x_i\le N_v
\text{ for every vertex }v\}.
\]
The root inequality bounds the total by \(n\). For every integer \(m\ge0\),
\(L_\tau(m)=|mQ_\tau\cap\mathbb Z^n|\), where \(0Q_\tau=\{0\}\).
The Ehrhart numerator is defined by
\[
\sum_{m\ge0}L_\tau(m)t^m=\frac{h^*(Q_\tau,t)}{(1-t)^{n+1}}.
\]

Let \(W_\tau\subseteq[n]^n\) contain exactly the ordered length-\(n\) words
\(w\) satisfying
\[
\sum_{j=1}^n\mathbf1_{\{w_j\in D_v\}}\ge N_v\quad\text{for every }v.
\]
Letters may repeat or be absent. Using the usual numerical order on \([n]\),
\(\operatorname{des}(w)=|\{j\in\{1,\ldots,n-1\}:w_j>w_{j+1}\}|\).
The frozen target, for all the objects above, is equality in \(\mathbb Z[t]\):
\[
h^*(Q_\tau,t)=\sum_{w\in W_\tau}t^{n-1-\operatorname{des}(w)}.
\]
Equal adjacent letters count as non-descents. The exponent lies in
\(\{0,\ldots,n-1\}\). The case \(n=1\) gives \(Q=[0,1]\), \(W=\{1\}\),
and both polynomials equal 1. No \(n=0\) assertion is included.
This is the Ehrhart numerator, distinct from the polynomial enumerating
support sizes of lattice points in the undilated polytope.

## Primary comparison and dated status

The definition and target agree with Athanasiadis–Xiao–Yan,
[arXiv:2603.11654v1](https://arxiv.org/html/2603.11654v1), Introduction and
Conjecture 5.2, printed p.13. Their Theorem 1.5 proves the singleton-leaf
rooted-star (octopus) case.

For the associated preorder the root is the **maximum** vertex. Its order
ideals are disjoint unions of maximal descendant subtrees, so subtree
inequalities give all ideal inequalities on both sides.
Athanasiadis–Chapoton,
[arXiv:2605.26916v1](https://arxiv.org/html/2605.26916v1), Conjecture 4.4,
p.12, extends the assertion to all preorders and reports tests through size 7.
Their Proposition 4.5 uses modified ascents and requires a minimum vertex;
that hypothesis does not automatically hold for a branching arbor.
Remark 7.3, p.19, gives the equivalent binomial-sum target below.
Theorems 1.2/1.3 of
[Dai et al., arXiv:2608.16037v2](https://arxiv.org/html/2608.16037v2)
concern a support enumerator and a different root polytope.

Source status: **open-supported within inspected literature on 2026-09-14**.
Live version histories list v1, v1, and v2 respectively. No inspected later
resolution of the exact assertion was found; this is not an exhaustive
priority conclusion. Detailed coverage and registry limitations are in
`literature/triage-verification.md`.

## Equivalent target and proposed contribution

For \(a\in\mathbb Z_{\ge0}^n\), write \(|a|=\sum_i a_i\), and put
\[
A_\tau=\{a:|a|=n,\ \sum_{i\in D_v}a_i\ge N_v\ \forall v\}.
\]
Prove for every integer \(m\ge0\) that
\[
L_\tau(m)=\sum_{a\in A_\tau}\prod_{i=1}^n\binom{m+1}{a_i},
\]
with binomial coefficients zero when the lower argument exceeds the upper.
A decreasing-run argument converts this to the original word identity.

Nearest prior result: the octopus identity and the published general
binomial-sum equivalence. Proposed delta: a subtree transformation proving
the identity for arbitrary rooted partition trees. Verification route:
check the local binomial convolution, its compatibility with upper/lower
truncation at every subtree, and the decreasing-run conversion.
`evidence/triage-transform.md` records the complete proposed derivation;
it has not passed a separate mathematical audit. The original scope has
not been narrowed to stars or enlarged to all preorders.

## Research pass 1: candidate scope

Research job `primary-20260914-arbor-ehrhart-words-research-9e9070b093b6`
checked the local identity for arbitrary b>=1 and K>=0, its polynomial
operator form for every allowed child degree bound, the subtree induction,
and an explicit inverse for the decreasing-box construction. The complete
proposed proof is `evidence/research-proof.md`; its known mathematical gap
list is empty at the proposer stage. This is a resolution candidate for
the exact original quantifiers above, pending fresh referee review.

`literature/research-verification.md` compares the method directly with
Chapoton's already known height recurrence and checks later primary papers,
including Yan's v2 formula for a different reflexive polytope. The proposed
new step is the subtree intertwining, not any known recurrence or word
reformulation. `evidence/research-checks.md` and its Python/JSON artifacts
document exact tests of the local operators and the word map; finite tests
are not the proof.

Decisive copied primary texts to bind with the candidate are
`evidence/external/2603.11654v1.pdf` (Conjecture 5.2, p.13) and
`evidence/external/2605.26916v1.pdf` (Conjecture 4.4, p.12; Remark 7.3,
p.19), together with their existing `.txt` extracts. The source's exact
content and its mathematical interpretation above remain unchanged.
