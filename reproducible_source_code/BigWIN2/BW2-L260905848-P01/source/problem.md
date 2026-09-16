# Precise interpreted statement and scope

This file interprets the immutable statement in `source.md` (SHA-256
`0e66f97af065e8d995c6efe336a1812c57822a0fd2bfd9d3653518bf563c44ba`).
It does not change or weaken that statement.

## Objects and quantifiers

Let \(\mathbb F_2=\{0,1\}\), let \(V=\mathbb F_2^5\), and write
\(\mathrm{Gr}_2(5,3)\) for the set of all 3-dimensional **linear** subspaces
of \(V\). For each \(i\in\{1,2,3\}\), a family is an ordinary set
\(\mathcal F_i\subseteq\mathrm{Gr}_2(5,3)\); multiplicities are not allowed.
The three families are 3-cross 1-intersecting precisely when

\[
  (\forall U_1\in\mathcal F_1)(\forall U_2\in\mathcal F_2)
  (\forall U_3\in\mathcal F_3),\qquad
  \dim(U_1\cap U_2\cap U_3)\ge 1.
\]

Thus the intersection must contain a nonzero vector. Choices in the three
families are independent, and an underlying subspace may occur in more than
one family. Empty families are allowed by the literal statement: the cross
condition is then vacuous and the desired product bound is immediate.

## Claims to resolve

For every such ordered triple of families, prove or disprove

\[
  |\mathcal F_1|\,|\mathcal F_2|\,|\mathcal F_3|\le 35^3=42875. \tag{I}
\]

If (I) is true, also classify equality. The proposed classification to test is:
whenever the product is exactly \(42875\), there exists one 1-dimensional
subspace \(L\le V\) such that, simultaneously for \(i=1,2,3\),

\[
  \mathcal F_i=\mathcal S(L):=
  \{U\in\mathrm{Gr}_2(5,3):L\le U\}. \tag{E}
\]

The equality question quantifies over *all* feasible equality triples; it does
not merely ask whether the displayed construction attains equality.

The Gaussian counts (with \(q=2\)) are

\[
 |\mathrm{Gr}_2(5,3)|={5\brack3}_2={5\brack2}_2
 =\frac{(2^5-1)(2^4-1)}{(2^2-1)(2-1)}=155,
\]

and, for each line \(L\), quotienting by \(L\) gives

\[
 |\mathcal S(L)|={4\brack2}_2
 =\frac{(2^4-1)(2^3-1)}{(2^2-1)(2-1)}=35.
\]

Hence three copies of a common full star satisfy the cross condition and attain
the proposed bound.

## Exact dual formulation

Fix any nondegenerate bilinear form on \(V\). Orthogonal complementation is a
bijection from 3-subspaces to 2-subspaces. Put
\(\mathcal A_i=\{U^\perp:U\in\mathcal F_i\}\). Since

\[
 (U_1\cap U_2\cap U_3)^\perp
 =U_1^\perp+U_2^\perp+U_3^\perp,
\]

the cross condition is equivalently

\[
  A_1+A_2+A_3\ne V
  \quad\text{for every }A_i\in\mathcal A_i. \tag{D}
\]

Thus (I) is a three-part cross-nonspanning problem on the 155 projective lines
of \(\mathrm{PG}(4,2)\). Under this duality, \(\mathcal S(L)\) becomes the set
of all 35 2-subspaces contained in the hyperplane \(L^\perp\); (E) says that
all three dual families are the full line set of the same hyperplane.

## Parameter boundary and literature status

The parameter substitution is \(q=2,r=3,t=1,n=5\) and
\(k_1=k_2=k_3=3\). It satisfies the Frankl--Tokushige conjecture's hypothesis
\(n\ge r\max_i k_i/(r-1)=9/2\), so (I) is exactly an instance of that
conjecture.

Primary sources inspected on 2026-09-10:

- Y. Li, B. Lv and J. Wen,
  [*On the Frankl--Tokushige conjecture and almost complete r-cross
  t-intersection theorems for vector spaces*](https://arxiv.org/html/2609.05848v1),
  Conjecture 1 and Theorem 1.1. The theorem assumes
  \(n\ge \frac r{r-1}(k_1+t)+1\), which here is \(n\ge7\), so it does not
  settle \(n=5\). Its introduction also records Wen--Lv's earlier binary bound;
  the published Theorem 1.1 in JCTA 220 (2026), 106127 assumes
  \(n\ge k_1+k_r+2=8\) for \(q=2\).
- T. Shimizu and N. Tokushige,
  [*A product theorem for r-cross intersecting families of
  subspaces*](https://arxiv.org/html/2608.28013v1), Conjecture 2, Theorem 3,
  and the paragraph following it. Theorem 3 is a two-family theorem requiring
  \(n\ge2k=6\). For nonempty r-cross families, fixing members of the other
  families shows every pair is cross-intersecting, so that theorem yields the
  conjectured product bound for \(n\ge6\), but not for \(n=5\). Their new main
  theorem requires \(n-k\) to be sufficiently large in terms of fixed \(q,r\);
  here \(n-k=2\), so it supplies no finite guarantee for this instance.

At \(n=5\), any two 3-subspaces already meet nontrivially because
\(\dim(U\cap W)\ge3+3-5=1\); the restriction is genuinely on triples. Also,
\(n=5\) is the least integral \(n\) satisfying the conjecture's parameter
hypothesis for the fixed values \(r=3,k=3\). Thus the advertised “first”
boundary is valid only in this fixed-\(k=3\) sense. Read globally over all
equal dimensions \(k\), the wording is too broad: \((k,n)=(2,3)\) is an
earlier binary instance satisfying \(n\ge3k/2\) but \(n<2k\), and three
2-subspaces of \(\mathbb F_2^3\) can have zero common intersection even though
every pair meets nontrivially. This scope correction does not change (I) or
(E), but no global “first instance” claim should be made without an added
restriction.

Status after the bounded search: **status-uncertain finite instance**. The two
cited 2026 papers state the encompassing conjecture and do not cover these
parameters. Exact-parameter and equivalent projective-language searches found
no separate settlement, but that limited search is not a priority or openness
claim. No proof or counterexample has yet been produced.

## Triage target

Nearest prior product result: Theorem 3 and the reduction immediately after it
in Shimizu--Tokushige give the conjectured product bound for equal dimensions
when \(n\ge 2k\), hence from \(n=6\) onward here.  The nearest cited theorem
that also gives the common-star equality classification directly is
Li--Lv--Wen Theorem 1.1, whose substitution starts at \(n=7\).  Neither result
reaches \(n=5\).

Proposed delta: resolve the first admissible \(n<2k\) boundary for the **fixed**
binary parameters \((k,r,t)=(3,3,1)\), namely \(n=5\), including equality.
The dependency-free exact check in `evidence/triage_sanity.py` confirms the
counts above and exhibits a zero-intersection triple; it does not optimize over
families.  The verification route is to enumerate the 155 subspaces in
canonical RREF form, encode every forbidden triple with zero primal
intersection (equivalently, full dual span), and use exact SAT/CP-SAT followed
by an independently replayable witness, certificate, or complete
combinatorial argument.
