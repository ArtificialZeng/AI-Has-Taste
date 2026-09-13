# NOVELTY_LOCK — Kusner taxicab equilateral sets, $n=5$

## Lock

- **Cutoff:** 2026-08-29 (search completed 2026-08-29 11:17 CST, UTC+08:00).
- **Locked target:** determine whether $e(\ell_1^5)=10$, equivalently whether eleven pairwise $\ell_1$-equidistant points exist in $\mathbb R^5$.
- **Novelty disposition:** **OPEN AT LITERATURE LOCK**. No proof, exact counterexample, or certified finite enumeration resolving $e(\ell_1^5)$ was located in the recorded primary-source and formal-database searches.
- **Strength:** high but bounded. A June 2026 author report says that the $p=1$ formula is known only for $n\le4$, and the arXiv/zbMATH/OpenAlex sweep extends through the cutoff. This is not a proof that no unindexed or unpublished solution exists.

## Frozen mathematical frontier

| Frontier item | Locked status | Evidence |
|---|---|---|
| Lower bound in all dimensions | $e(\ell_1^n)\ge2n$, attained by $\{\pm e_i\}$ | Direct calculation; Alon–Pudlák p. 468 |
| Exact dimensions | $e(\ell_1^n)=2n$ for $1\le n\le4$ | $n=3$: Bandelt–Chepoi–Laurent Prop. 4.1; $n=4$: Koolen–Laurent–Schrijver Prop. 8 + Thm. 9 |
| First unresolved dimension | $n=5$ | Ge–Xu–Zhou §1.1 p. 2 (2026-06-02): known only for $n\le4$ |
| General $p=1$ upper bound | $e(\ell_1^n)\le Cn\log n$ | Alon–Pudlák Thm. 1.3; current-order statement in Ge–Xu–Zhou |
| Universal finite-dimensional bound | $e(X)\le2^n$ for any $n$-dimensional normed $X$ | Petty 1971; restated in Ge–Xu–Zhou §1.1 |
| Concrete bracket at $n=5$ | $10\le e(\ell_1^5)\le32$ | Combine the lower and universal upper bounds |
| Decisive counterexample form | 11 exact points, with 55 equal rational/algebraic $\ell_1$ distances | Definition and $\binom{11}{2}=55$ |
| Decisive positive form | Exhaustive exact exclusion of every 11-point sign/order branch | Finite sign-pattern linearization; no completed enumeration was located |

## 2025–2026 novelty sweep

### June 2026 update

Ge, Xu, and Zhou, [arXiv:2606.03987v1](https://arxiv.org/abs/2606.03987), explicitly separate the two branches:

- $p=1$: §1.1 says that the value $2n$ is known only for $n\le4$. Theorem 1.3 supplies an almost-linear $C_p n\log(2n)$ bound on complementary exponent intervals, including $p=1$, but no exact $p=1$ result.
- $2\le p\le4$: Theorem 1.2 proves the different simplex formula $e(\ell_p^n)=n+1$.

Thus the preprint is a positive current-status signal for openness of the present $p=1,n=5$ target, not a solution. At the cutoff it remained arXiv v1; no journal DOI was located.

### August 2026 headline collision

Chalmers, [arXiv:2608.14013v1](https://arxiv.org/abs/2608.14013), is titled “A counterexample to Kusner’s conjecture on equilateral sets.” Its theorem constructs 58 equilateral points in $\ell_5^{56}$, disproving the $p>2$ simplex branch. The abstract and Theorem 1 specify $p=5,n=56$. It contains no $p=1$ construction or exclusion and therefore does **not** terminate this project.

### Database results through the cutoff

- arXiv API queries <code>all:Kusner</code> and <code>all:equilateral AND submittedDate:[202501010000 TO 202608292359]</code> returned the two relevant 2026 records above and no $p=1,n=5$ resolution in the inspected results.
- zbMATH Open query <code>ti:"Equilateral sets" &amp; any:Kusner</code> returned Chalmers (2026), Swanepoel (2004), and Smyth (2013); no taxicab $n=5$ solution.
- OpenAlex date-filtered search for <code>"Kusner" equilateral</code> returned the same two relevant 2026 preprints (with one duplicate Ge–Xu–Zhou record) and no taxicab solution.
- Broad exact-phrase web queries for $e(\ell_1^n)$, “rectilinear space,” $n=5$, and “Kusner” located no additional primary theorem.

Every negative statement here means only “not found under the logged queries.” Full queries and limitations are in [search_log.md](search_log.md).

## Original-source chain

1. Guy’s original record is verified by publisher/Crossref metadata: R. K. Guy, “An Olla-Podrida of Open Problems, Often Oddly Posed,” *Amer. Math. Monthly* 90(3) (1983), 196–200, DOI [10.1080/00029890.1983.11971188](https://doi.org/10.1080/00029890.1983.11971188), JSTOR DOI [10.2307/2975549](https://doi.org/10.2307/2975549).
2. The original scan was access-blocked in this run. Bandelt–Chepoi–Laurent p. 600 identifies the question as Kusner’s “Problem 0” in Guy; Ge–Xu–Zhou Conjecture 1.1 states the formula. The historical attribution is therefore locked with high confidence, while the literal 1983 wording remains not directly inspected.
3. Bibliographic correction: current publisher/Crossref metadata give pp. 196–200; some older reference lists say 196–199.

## Exact structural observations admitted at the lock

These are direct deductions, not claimed literature novelty:

1. Normalize the common distance to $1$ by positive scaling.
2. For each point pair $r<s$ and coordinate $i$, branch on $x_{ri}-x_{si}<0$, $=0$, or $>0$. On a branch, every $|x_{ri}-x_{si}|$ is linear, and both equal-distance equations and branch-consistency conditions are rational linear constraints.
3. Hence the 11-point decision is a finite union of rational-polyhedral feasibility problems. “Finite” does not imply that the raw enumeration is computationally feasible, and no exhaustive certificate is supplied by this lock.
4. Any claimed rational counterexample can be independently verified by exact recomputation of all 55 distances.

## What would invalidate this lock

Before claiming a new result, rerun the exact searches in [search_log.md](search_log.md) and search forward citations of:

- Bandelt–Chepoi–Laurent (1998), DOI 10.1007/PL00009370;
- Koolen–Laurent–Schrijver (2000), DOI 10.1023/A:1008391712305;
- Alon–Pudlák (2003), DOI 10.1007/s00039-003-0418-7;
- Ge–Xu–Zhou (2026), arXiv:2606.03987;
- Chalmers (2026), arXiv:2608.14013.

The lock must be reopened if any source claims an 11-point $\ell_1^5$ configuration, an exact upper bound $e(\ell_1^5)\le10$, or a certified exhaustive enumeration covering all 11-point coordinate order types.

## Audit note

This file performs Gate 1 only. It does not certify any new proof, counterexample, SAT result, LP infeasibility result, or Farkas certificate. Proposed computational routes remain research routes until independently serialized and verified.

## Second lock: strict structural result

- **Search time:** 2026-08-29 11:50--12:53 CST.
- **Result searched:** a hypothetical eleven-point equilateral set in
  \(\ell_1^5\) must use at least nineteen positive coordinate gaps
  (\(\sum_j q_j\ge24\)).
- **Mathematical status:** proved across proof/t15_dense_branch.md,
  proof/t16_branch.md, proof/t17_branch.md, and proof/t18_branch.md,
  conditional on the previously audited \(t\ge15\) theorem, and
  independently passed in referee rounds 2--5.
- **Novelty disposition:** **NO MATCH FOUND IN THE RECORDED SECOND SWEEP.**
  The closest prior source is KLS Proposition 2, which supplies the positive
  weighted \(k\)-nested cut-family equivalence.  No support-\(19\) theorem,
  spectral-deficit refinement, singleton-compression lemma, or rank-ten
  antichain obstruction was located in the KLS text, its inspected OpenAlex
  forward citations, the fresh arXiv sweep, or the exact/structural web
  queries S27--S37.
- **Limitation:** this is a bounded literature conclusion, not proof that no
  unpublished, unindexed, or differently phrased result exists.  It does not
  change the locked status of the original problem: \(e(\ell_1^5)=10\)
  remains open after this partial theorem.
