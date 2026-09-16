# Frozen source — win-00042-p01

## Immutable original lead

Let `A(n,k)` denote the Eulerian number counting permutations of `[n+1]` with exactly `k` descents, extended by zero outside its natural triangular range. Prove or disprove that the infinite Eulerian triangle is totally positive of order four: for every `1<=s<=4` and every two strictly increasing tuples of nonnegative indices `n_1<...<n_s` and `k_1<...<k_s`,

`det[A(n_i,k_j)]_{1<=i,j<=s} >= 0`.

## Source and claimed delta to verify

- Primary source: arXiv:2608.29224, Theorem 1.1 and Remark 1.2, PDF pp.1--2.
- Local immutable source PDF: `batches/inbox/bigWin-42-materials/2608.29224.pdf`, SHA-256 `737c884ecdde26c39d18d974a2904a6c68bd36ca273b4065590f056cf2e62e2f`.
- The source proves TP3. It reports a reduction of TP4 to 126 parametric templates with computer sign checks, while explicitly withholding a proof because those checks were not independently human-verified. This wording and any later literature must be rechecked during triage.

## Required resolution standard

A proof must establish complete coverage of all order-at-most-four minors and give auditable nonnegativity certificates for every surviving template, including boundary and zero cases. A disproof must give explicit row and column tuples and an exact negative determinant. Finite scans alone do not prove TP4.

