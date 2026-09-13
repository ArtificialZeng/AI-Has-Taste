# Proof audit

Status: **PASS for the finite endpoint; OPEN for the stated all-rank gap**.

## Audited endpoint

The released theorem quantifies over every comparable ordered pair in
`[e,v_10]`.  The verifier regenerates the 12,866-element universe by both a
full rank-matrix filter of `S_10` and the complete subword set, regenerates all
6,229,297 comparable pairs, and evaluates each pair with integer arithmetic.
The normalized Dyer recurrence and a separate ordinary-R recurrence agree
after an exact Laurent change of variables.  Membership is tested against the
complete 434-element Fibonacci-product catalog in degree at most eight.

The latest run reports zero failures, 22 normalized classes, maximum
coefficient 15, `index_sum_patterns=true`, and fingerprint
`0x78cf5914f6aaeb37`.  It reproduces every rank 2--9 baseline first.  The
closed-schema rejection suite rejects eight damaged inputs, including an
overflowing endpoint.  Exact hashes and independent referee findings are in
`audit/referee_work.md` and the release manifest.

## Structural claims and limits

Support multiplicativity, the boolean-block case, and the capped-ladder
ambient-rank reduction were checked against the definitions and the subword
property.  They prove an infinite independent-block class and reduce the new
connected n=10 boundary to the three listed support/cap types.  They are not
used as a shortcut in the exhaustive certificate.

The all-rank conjecture is not claimed.  The proposed path-forest and
disjoint-footprint lemmas remain unproved and are explicitly isolated in
`proof/gap_ledger.md`; no sentence in the manuscript treats them as theorems.

No Lean, Coq, Isabelle, or other proof assistant was used.  The endpoint is
bound only to the exact finite verifier and its stated mathematical
specification.
