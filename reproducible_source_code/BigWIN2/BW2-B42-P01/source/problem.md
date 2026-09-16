# Precise problem statement

## Frozen lead

The immutable statement to be interpreted is the one in `source.md`:

> Let `A(n,k)` denote the Eulerian number counting permutations of `[n+1]` with exactly `k` descents, extended by zero outside its natural triangular range. Prove or disprove that the infinite Eulerian triangle is totally positive of order four: for every `1<=s<=4` and every two strictly increasing tuples of nonnegative indices `n_1<...<n_s` and `k_1<...<k_s`,
>
> `det[A(n_i,k_j)]_{1<=i,j<=s} >= 0`.

This quotation does not replace or modify `source.md`.

## Definitions and indexing

- For an integer `n>=0`, write `[n+1]={1,...,n+1}`. For a permutation `pi=(pi_1,...,pi_{n+1})`, a descent is a position `r in {1,...,n}` such that `pi_r>pi_{r+1}`.
- For `n>=0` and `0<=k<=n`, `A(n,k)` is the number of permutations of `[n+1]` having exactly `k` descents. Thus `A(0,0)=1`. Equivalently, with zero-extension in `k`,
  `A(n,k)=(n+1-k)A(n-1,k-1)+(k+1)A(n-1,k)` for `n>=1`.
- For every `n>=0` and integer `k` outside `0<=k<=n`, set `A(n,k)=0`. Only nonnegative row and column indices occur in the claim, so values with `n<0` are outside its scope.
- The infinite matrix is `A=[A(n,k)]_(n,k>=0)`. It is lower triangular: `A(n,k)=0` when `k>n`.
- A minor of order `s` is obtained from row indices `0<=n_1<...<n_s` and column indices `0<=k_1<...<k_s`; its value is the integer determinant of the matrix whose `(i,j)` entry is `A(n_i,k_j)`. The row tuple and column tuple are independently chosen; no further relation is assumed.
- “Totally positive of order four” (`TP4`) is used in the source's non-strict convention: every minor of each order `s=1,2,3,4` is nonnegative.

## Exact quantified claim

For every integer `s` with `1<=s<=4`, for all tuples

`(n_1,...,n_s),(k_1,...,k_s) in Z_(>=0)^s`

satisfying `n_1<...<n_s` and `k_1<...<k_s`, prove

`det(A(n_i,k_j))_(1<=i,j<=s) >= 0`.

A disproof consists of one such `s`, row tuple, and column tuple with an exactly evaluated negative determinant.

## Boundary cases and scope reductions

- Zero-extension is part of the claim, not an exclusion of columns beyond a selected row. If `k_i>n_i` for some aligned position `i`, lower triangularity forces the selected determinant to be zero. Thus only *admissible* pairs, satisfying `k_i<=n_i` for all `i`, can require a positivity argument.
- The boundary rows and columns `n=0` and `k=0`, and minors containing zero entries, remain included.
- Every selected minor is finite and lies in a finite leading principal truncation, but the quantifiers impose no upper bound on its indices. A finite scan therefore cannot prove the claim.
- Orders `s<=3` are already covered by the cited nearest result. The unresolved mathematical delta is order `s=4`, including complete reduction/coverage and exact nonnegativity certificates for every remaining infinite parameter family.

## Triage status and nearest prior result

As checked on 2026-09-06, Jianxi Mao, *Eulerian triangle is totally positive of order 3*, arXiv:2608.29224v1 (submitted 2026-08-29), Theorem 1.1 on PDF p.2 proves TP3 and strict positivity of every admissible minor of order at most three. Theorem 2.5 on PDF pp.3--4 gives a reduction criterion from admissible minors with consecutive rows and columns. Remark 1.2 on PDF p.2 reports an AI-assisted reduction of TP4 to 126 order-four minors that passed symbolic checks, but explicitly says this is not regarded as a proof because the argument was not independently verified by hand. The local PDF hash agrees with the hash frozen in `source.md`.

An exact-assertion search of arXiv on 2026-09-06 found that v1 as the nearest primary result and found no later primary paper proving or disproving TP4. This is limited-search evidence, not proof of priority or comprehensive open status. The source status is therefore `open-supported` for triage, subject to a fuller literature check before any novelty claim.

Target contribution: nearest prior result = TP3 plus an unverified 126-case TP4 computation; proposed delta = an auditable proof of exhaustive order-four coverage and exact nonnegativity certificates, or an explicit exact negative minor; verification route = independently reconstruct the consecutive-minor reduction and template map, then check every template certificate exactly.
