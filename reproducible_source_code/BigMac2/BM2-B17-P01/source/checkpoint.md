# Checkpoint

Job: bigMac-00017-p01-research-5ad733cc06c3 (research pass 2).

## Candidate and exact scope

A `resolution-paper` candidate is frozen in `claim.json`: for every integer
\(n\ge496\), the row maximum \(\rho(n)\) is strictly less than one.  This is a
researcher proposal requiring a fresh mathematical referee; it is not an
acceptance decision or a novelty claim.

## New decisive evidence

- `source.md` remains byte-for-byte unchanged (SHA-256
  `ce462b0aacd55a07bf7a64e52e96110e6e6f953d4bf779163753c7cb2ce876b9`).
- `evidence/uniform_tail_proof.md` proves the infinite range
  \(n\ge100001\).  If \(a_*\) is the localized row maximizer and
  \(x=n-2a_*\), the adjacent-ratio transition gives
  \(H_n(x+1)<0\le H_n(x-1)\), hence \(x^2<n\).  Explicit one-sided
  Stirling bounds then give
  \[
  R_n(a_*)<\frac4{\sqrt\pi}
  \left(\frac1{\sqrt{2e}}+\sqrt{A_n}\right)C_ne^{E_n},
  \]
  where \(A_n=(n-1)/(n(n-2))\),
  \(E_n=1/(12n)+1/(12(n-2))+1/(6(n-1))\), and
  \(C_n=((1-1/n)(1-n/(n-2)^2))^{-1/2}\).  All three endpoint factors
  decrease with \(n\).  At \(N=100001\), rational bounds yield the strict
  uniform majorant
  \[
  \frac{24957787612296876183}{25000000000000000000}<1.
  \]
  The proof treats both parities and a possible adjacent maximizing tie.
- `evidence/resolution_check.py` independently extends the exact scan to every
  row \(496\le n\le100000\), and checks every rational cross-product used in
  the tail endpoint.  `evidence/resolution_check_results.json` records zero
  violations in 99,505 rows.  The largest finite value occurs at
  \((n,a)=(497,241)\), with an exact positive denominator-minus-numerator.

## Obstacles and audit status

No mathematical gap is presently known.  The analytic proof uses the classical
one-sided Stirling inequalities, whose application and constants must be
rederived by a fresh referee.  The exact computation is reproducible but is not
a substitute for that audit.  No manuscript or PDF has been created, and no
claim of priority beyond the supplied source status has been made.

## One next test

Fresh-referee test: rederive equations (3)--(8) of
`evidence/uniform_tail_proof.md` from the factorial definition, check the
maximizer/tie indexing for both parities, independently replay
`evidence/resolution_check.py`, and verify that its JSON and the endpoint
rational product match before accepting or revising the exact claim scope.
