# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | Full conjecture after L1--L6 | Necessary divisibility, size, gap, and smoothness conditions do not yet force a common prime in the remaining domain | fatal | Search for stronger arithmetic constraints and counterexamples symmetrically | open |
| G02 | L7 / accepted \(j\le3i/2\) theorem | Local reconstruction has not checked all 12 EEES exceptional \((n,i)\) pairs or the exact finite code for \(n=2j\) | major only if this prior theorem is re-proved locally; it is not used in the certified endpoint | Independently enumerate exceptions before making a local proof claim | deferred; nondependency |
| G03 | Computational finite claim | An optimized scan is not self-certifying unless its pruning and support construction are cross-checked against a definition-level evaluator | major | Separate Legendre verifier, direct-gcd oracle, strict parser fixtures, and a hash-bound release binder | resolved: strict verifier output SHA `9a1a4300...2904ab` covers the fixed endpoint and reports 43,631,335,536 anchor candidates; the direct-gcd oracle covers 994,009 pairs; the release binder equates the canonical certificate and strict-output counts and rejects the recorded tamper matrix |
| G04 | Strong-family deformation D02 | Evidence for \(n=3^m+1\) does not classify all residues or all \(i=3\) candidates | major | Exact digit analysis plus targeted search; do not extrapolate | open |
| G05 | Novelty | July 2026 proof claim C10 may overlap any new reduction obtained here | major for publication claim | Second and final exact-endpoint searches after freeze; use bounded novelty wording only | resolved for the finite endpoint: no earlier public complete all-row \(i=3\), \(n\le10^8\) claim was located in the recorded searches; absolute priority is not claimed |

G01 remains fatal only to a claim that the original infinite conjecture is
solved; it is not a gap in the delimited finite theorem
\(i=3,\ 8\le n\le10^8\).  G04 remains an exploratory route outside that
finite theorem and likewise does not block it.
