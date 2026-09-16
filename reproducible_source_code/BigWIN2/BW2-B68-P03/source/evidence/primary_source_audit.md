# Primary-source audit (2026-09-07)

The versioned official arXiv HTML for arXiv:2609.05302v1 was inspected at
<https://arxiv.org/html/2609.05302v1>. Direct PDF retrieval from the execution
environment failed (`curl: (7) Couldn't connect to server`), so no local PDF
copy is claimed.

The official v1 HTML gives the following decisive statements:

- Introduction, lines 37--49: Andrews's generalized Frobenius definition and
  notation for the generating functions and q-products.
- Theorem 1.2, lines 67--71: for every n >= 0,
  `cphi_18(6n+5) == 0 (mod 8)`.
- Formula (3.15), lines 273--280: the exact Cui--Gu--Tang q-product formula for
  the full generating series of `cphi_18`, used independently in
  `computation/source_formula_mod16.py`.
- Concluding remarks and Conjecture 5.1, lines 698--709: the authors say the
  following congruences are based on numerical evidence and leave their proofs
  for future investigation; the displayed classes are exactly `30n+19` and
  `30n+25`, both modulo 16, for every n >= 0.

Thus the frozen conjecture is accurately transcribed.  Theorem 1.2 is also
accurately transcribed, but it is arithmetically irrelevant as a direct
modulo-8 precursor: 19 and 25 are both 1 modulo 6, not 5 modulo 6.

On 2026-09-07, exact searches for `cphi_18(6n+1)` modulo 16, the two target
progressions with colored Frobenius terminology, and generalized-pentagonal
support for `cphi_18` found no primary source stating the stronger 6-section
identity in `h_identity_dossier.md`. The official v1 paper itself states only
the two progressions as Conjecture 5.1. This bounded screen is not a priority
or exhaustiveness claim.
