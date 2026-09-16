# SC229 research assessment

Job: `newwin-00001-p09-research-6b8b4cffaffd`. Date: 2026-09-12.
Proposed outcome: candidate / resolution-paper / proved, pending a fresh
mathematical referee. This document records proposer evidence, not an audit.

## Decisive new argument

`evidence/decoder-proof.md` proves the all-arity decoder lemma requested by
triage and combines it with realization to give a bijection between full
linear term functions and rooted labelled trees with one distinguished child
at every nonleaf. In the leftmost decomposition, the root factor has a
root-2 slice equal to 1, which excludes a disjoint AND decomposition. Child
indicators have a leftmost-root-0 slice equal to 0, which excludes a disjoint
OR decomposition; their complements are therefore AND-prime. Essentiality
is proved inductively by explicit disjoint-support assignment witnesses.
Cartesian factorization over coordinate partitions is unique by common
refinement, so these factors can be recovered from the truth set alone.
The root factor is uniquely recognizable by its zero-at-value-0 slice;
its root-1 slice recovers the distinguished child. Complementing the other
factors recovers the ordinary children. Singleton indicators are explicitly
separated from ternary projections in the base case.

This supplies an exhaustive normal form without duplicate functions, not
just a generate-and-deduplicate procedure. The resulting all-n formula is

    c_n = (n-1)! sum_{k=0}^{n-1} binom(n,k) k^(n-1-k)/(n-1-k)!,

with 0^0=1. The proof also supplies a positive integer recurrence from direct
labelled-tree counting. The EGF and explicit formula are consequences of
the classification; the universal statement does not rest on finite tests.

## New exact computational attacks

Reproduce with `python3 evidence/decoder-check.py` from the project directory.
This program differs from the earlier census: it constructs the finest
AND factorization from a truth set by enumerating all coordinate partitions,
recognizes the root, and recursively decodes the child functions without
being given a syntactic term or tree code. It compares the result with the
separate syntactic encoding only after decoding.

It retains all literal full binary terms without equivalence pruning for
n=1,...,5: respectively 1,2,12,120,1680 terms. Every distinct resulting
function is decoded on all 3^n assignments. The 1,2,12,108,1340 functions
(1,463 total) all recover the correct tree. Sixteen additional examples,
eight each on n=6 and n=7, test left and right combs, balanced trees, large
distinguished children, compound ordinary children, and reversed labels.
These are structured tests on every assignment, not complete n=6 or n=7
decoder censuses. All details and exact syntaxes are in
`evidence/decoder-check.json`.

The run made 7,277 recursive decoder calls, tested 95,249 coordinate
partitions, inspected 5,798 recovered factors, and performed 31,490
essential-coordinate checks; 3,354 recursive calls exercised singleton
indicators. No assertion failed. The integer recurrence and the explicit
sum agree exactly for n=1,...,12, and their first six values match the
earlier independent literal census in `evidence/triage-check.json`.
Values above the census range are formula/model values, not additional
exhaustive counts. All calculations use finite sets, integers and rational
numbers; there is no floating-point mathematical evidence or randomness.

## Proposer attack on possible gaps

- The all-zero relation is excluded from Cartesian factorization; each
  q_t attains 1 by an explicit assignment, so the exclusion is justified.
- Factors with unused coordinates are excluded by proved essentiality.
- Root recognition tests the value-0 slice specifically. A singleton
  complement has a zero slice at value 1, but none at value 0, so it cannot
  impersonate the root factor.
- The root may have only its distinguished child; the formula, factorization,
  and recursive decoding all cover that case with an empty ordinary product.
- Every recovered child support is nonempty and strictly smaller; the
  recursion is finite and is based on indicators, not an assumed Boolean
  value for a singleton ternary projection.
- The source permits arbitrary variable order with labels fixed. The model
  counts labelled trees with distinguished children and does not quotient
  by relabelling or silently fix the original variable order.

No mathematical gap is presently identified by the proposer. This is a
same-context proof check, not a fresh model review, formal verification, or
peer review. The comparison in `literature/research-screen.md` identifies
the 2024 open question and the earlier leftmost-tree method; priority claims
remain bounded by inspected literature.

## Handoff

One next test: a fresh referee should try to invalidate Sections 2--4 of
`evidence/decoder-proof.md` by challenging uniqueness of the disjoint
factorization, uniqueness of the recognized root, or recursive singleton
recovery, then check that labelled counting gives the frozen full-scope
formula. Recomputing `evidence/decoder-check.py` is corroboration, not a
substitute for that all-arity audit. No additional speculative target or
manuscript is proposed by this job.
