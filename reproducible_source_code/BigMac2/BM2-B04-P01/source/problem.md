# Precise reading of DM04-01

Provenance: `bigMac-00004-p01-triage-7174515b56db`  
Frozen input: `source.md`, SHA-256
`2183039719540ca0e5653a79785209d40ef2cb70d28ab6807a23d0790736b527`.

## Objects and conventions

Write \([6]=\{1,\ldots,6\}\) and \(E_6=\{\{i,j\}:1\le i<j\le6\}\).
The matrix domain is
\[
 \mathcal L^+_{6,1}:=
 \left\{P=(p_{ij})\in\mathbb R^{6\times6}:
 P=P^{\mathsf T},\ p_{ii}=1,\ p_{ij}>0\ (i\ne j),\
 P\text{ has at most one positive eigenvalue}\right\}.
\]
Eigenvalues are counted with multiplicity.  Singular matrices are allowed.  Since
\(\operatorname{tr}P=6\), every matrix in this set actually has exactly one
positive eigenvalue (and five nonpositive eigenvalues).

For \(S\subseteq[6]\), its cut vector \(\delta(S)\in\mathbb R^{E_6}\) has
\(\delta(S)_{ij}=1\) exactly when precisely one of \(i,j\) belongs to \(S\).
Define
\[
 \operatorname{Cut}_6=\operatorname{cone}\{\delta(S):S\subseteq[6]\},
 \qquad
 K^\vee=\{y:\langle y,x\rangle\ge0\text{ for every }x\in K\}.
\]
Thus
\[
 -\operatorname{Cut}_6^\vee
 =\left\{\alpha\in\mathbb R^{E_6}:
   \sum_{\substack{i\in S,\ j\notin S\\i<j\text{ or }j<i}}
   \alpha_{\min(i,j),\max(i,j)}\le0
   \text{ for every }S\subseteq[6]\right\},
\]
where each crossing edge is included once.  By Theorem B of Huang--Huh--Soskin--Wang,
this is precisely the cone of reduced bounded ratios on \(\mathcal L^+_{6,1}\).

The normalized slice in the problem is
\[
 \mathcal A_6:=\left\{\alpha\in-\operatorname{Cut}_6^\vee\setminus\{0\}:
 \sum_{1\le i<j\le6}\alpha_{ij}=-1\right\}.
\]
For \(\alpha\in\mathcal A_6\), set
\[
 F_\alpha(P):=\prod_{1\le i<j\le6}p_{ij}^{\alpha_{ij}},
 \qquad
 f(\alpha):=\sup_{P\in\mathcal L^+_{6,1}}F_\alpha(P).
\]
Strict positivity makes every real power well-defined.  This supremum equals the
infimum of all uniform bounding constants used in the cited papers; it need not
be attained because the domain is not closed.

## Frozen claim and refutation criterion

The claim to prove or disprove is exactly
\[
 \boxed{\quad \forall\alpha\in\mathcal A_6,\qquad f(\alpha)\le2.\quad}
\]
A disproof requires one exact \(\alpha\in\mathcal A_6\) and one exact
\(P\in\mathcal L^+_{6,1}\) with \(F_\alpha(P)>2\).  Floating-point optimization
alone is not such a certificate.  A proof must be uniform over all real
\(\alpha\) in the displayed slice and all matrices in the displayed domain.

The conditional classification clause is read literally as a classification of
**extreme rays**, not of maximizing matrices: for every extreme ray
\(R\) of \(-\operatorname{Cut}_6^\vee\), take its unique representative
\(\alpha_R\in\mathcal A_6\), and determine, up to the natural \(S_6\)-action,
which rays satisfy \(f(\alpha_R)=2\).  Equality here concerns the optimal
constant; it does not assert that some strictly positive matrix attains it.

## Finite extreme-ray reduction

Up to \(S_6\), the facets of \(\operatorname{Cut}_6\), hence the extreme rays
of \(-\operatorname{Cut}_6^\vee\), have four types.  They are hypermetric:
if \(h\in\mathbb Z^6\) has \(\sum_i h_i=1\), put
\(q(h)_{ij}=h_i h_j\).  For the representatives below, let
\[
 d(h):=-\sum_{i<j}h_i h_j=\frac{\sum_i h_i^2-1}{2},
 \qquad \widehat q(h):=q(h)/d(h)\in\mathcal A_6.
\]

| type | representative \(h\) | \(d(h)\) | known optimal constant |
|---|---:|---:|---:|
| triangular (lifted) | \((1,1,-1,0,0,0)\) | 1 | \(f(\widehat q(h))=2\) |
| pentagonal (lifted) | \((1,1,1,-1,-1,0)\) | 2 | \(f(\widehat q(h))=2\) |
| new six-point type I | \((2,1,1,-1,-1,-1)\) | 4 | unknown |
| new six-point type II | \((-2,-1,1,1,1,1)\) | 4 | unknown |

The first equality is the optimal triangular inequality.  The unnormalized
pentagonal ratio has optimal constant \(4\), so homogeneity gives
\(4^{1/2}=2\) after normalization.  For any convex combination of normalized
extreme-ray representatives, log-convexity gives
\[
 f\!\left(\sum_r\lambda_r\alpha_r\right)
 \le \prod_r f(\alpha_r)^{\lambda_r},
 \qquad \lambda_r\ge0,\quad\sum_r\lambda_r=1.
\]
Consequently, the boxed claim reduces exactly to proving \(f\le2\) for the two
new types.  If that succeeds, the equality-extreme-ray classification reduces
to deciding whether either new type has optimal constant exactly \(2\); the two
lifted types already do.

## Prior results, status, and proposed delta

- Huang--Huh--Soskin--Wang, *Bounded ratios for Lorentzian matrices*,
  arXiv:2510.25030v2 (8 Nov 2025), Definition 1.5, Theorems A and B,
  Definition 1.8 and Conjecture 1.9: identifies the reduced cone with
  \(-\operatorname{Cut}_n^\vee\), proves the sharp result through \(n=5\), and
  lists the two additional six-point hypermetric types without their optimal
  constants.  <https://arxiv.org/html/2510.25030>
- Baldi--Kummer, *A note on bounded ratios*, arXiv:2609.03934v1
  (3 Sep 2026), Section 3, especially Conjecture 3.1 and the paragraph after it:
  gives an exact \(n=7\) non-hypermetric counterexample and reports only that no
  counterexample was produced for the two new \(n=6\) hypermetric types.
  <https://arxiv.org/html/2609.03934>
- These primary sources were inspected on 6 Sep 2026.  Targeted arXiv searches
  for a separate six-point resolution found no additional item.  This limited
  search is not evidence of priority or a declaration that the problem is open.

Source status is therefore **status-uncertain**, not verified-open.  The nearest
prior result is the sharp theorem for the lifted triangular and pentagonal rays;
the proposed delta is an exact upper bound or exact counterexample for each of
the two new rays, followed (in the positive branch) by their equality status.
The natural verification route is exact inertia analysis plus polynomial/rational
inequalities on the relevant semialgebraic matrix domain.  Numerical optimization
may locate candidates but cannot complete either branch.

## Scope exclusions

The problem does not restrict \(\alpha\) to integral vectors, does not require
\(P\) to be nonsingular, and does not replace strict entrywise positivity by
nonnegativity.  Boundary matrices may be used only through a justified limiting
argument.  The rank-two conjecture in the earlier paper and the seven-point
counterexample are contextual results, not resolutions of this six-point claim.
