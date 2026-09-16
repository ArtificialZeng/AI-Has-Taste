# win-00064-p02 — Sharp dimension threshold for local Lewis-weight acceleration

Let `p>2` and let `A in R^{m x n}` have full column rank and strictly positive row Lewis weights. Use the notation of Padmanabhan, arXiv:2609.04338v1, Lemma 3.1: at the fixed point, `J=(1-2/p)(I-K)` with `K=W^{-1}(P o P)`. Prove or disprove both parts:

1. If `m>n(n+1)/2`, then `lambda_min(K)=0`, so the predicted local contraction factor is exactly `1-2/p` and cannot be strictly faster than the global factor.
2. The threshold is sharp: for every `n<=m<=n(n+1)/2`, there exists such an `A` for which `K` is positive definite.

An acceptable full result must handle the Parseval-frame/Lewis-weight constraints, not merely an arbitrary positive-semidefinite matrix. A counterexample to Part 2 may become a useful exact corrected threshold. Primary evidence: `batches/inbox/bigWin-64-materials/2609.04338.pdf`, SHA-256 `caaccb291c1fd425141c79cc77835a253908cb2b62ade72903c705f5e4a1d9a1`, Section 3.2.
