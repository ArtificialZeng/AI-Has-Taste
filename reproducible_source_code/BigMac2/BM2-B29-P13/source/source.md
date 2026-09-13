# bigMac-00029-p13 — first genuine residue-choice incompatibility layer

Keep the asymptotic source problem `E(n)/N(n) -> 0` explicitly unresolved.
As a source-derived finite refinement, let `F_n` be the survivor family on
`X_n={2,...,n+1}` from Raso--Venturi, and let `E_n` be its extendible members.
For `A subset X_n`, define

`Omega_k^+(A) = (Z/kZ) \ ({m mod k : m in A, m>k} union {(n+2) mod k})`

and

`W_A(m) = {k in {2,...,m-1} : m mod k in Omega_k^+(A)}`.

Let `L_n(A)` mean that every `Omega_k^+(A)` is nonempty for `2<=k<=n`
and every omitted `m in X_n\A` has nonempty `W_A(m)`.  Determine exactly

`n_* = min {n>=1 : there exists A in F_n\E_n with L_n(A)}`

and classify every such `A` at the first layer.  A complete result must
include an exact generation certificate for all preceding layers, an
independent implementation of the source's Theorem 30 CSP criterion, and
human-readable conflict cores for every first-layer exception.

Primary source: `batches/literature/bigMac-29/2609.08528v1.pdf`, Definitions
26 and 28--29, Theorems 27 and 30, Corollaries 31 and 33, Remark 34, and
Proposition 36 (printed pages 26--31).  The source states that the local
condition is not sufficient, but does not identify the first genuine
incompatibility layer or classify it.  Publication novelty remains
status-uncertain because the source is a recent v1.
