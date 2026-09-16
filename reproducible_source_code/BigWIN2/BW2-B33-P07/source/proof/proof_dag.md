# Proof dependency graph

No candidate resolution exists.

- T (target): \(a_n\ne0\) for every integer \(n>54\).
  - Z (exact base): the only zeros for \(0\le n\le5\cdot10^{10}\) are the eight listed.
    This is certified finite computation, not a proof of T.
  - M (modular route): characterize all indices compatible with
    \(a_n\equiv0\pmod{2^k}\) for arbitrary \(k\).
    - M1 (proved): recurrence reduction modulo \(2^k\) is exact because the
      lowest \(k\) two's-complement bits determine XOR modulo \(2^k\).
    - M2 (proved): for every initial pair, the length-\(2^k\) time-word map
      has cube equal to the identity; hence \(3\cdot2^k\) is a period.  See
      `proof/modular_period_theorem.md`.
    - M2a (exact consequence): at level \(k=33\), every integer zero lies in
      one of 354 listed residue classes modulo \(3\cdot2^{33}\).
    - M3 (open): show every nested compatible residue branch either gives one
      of the eight finite indices or no nonnegative integer.
    - M3a (proved reduction): an integer zero is exactly an infinite
      zero-residue path whose representatives are eventually constant (all
      later edges are lower). See `proof/zero_lift_tree.md`.
  - E (proved elementary structure): XOR displacement is at most \(n\),
    \(|a_n|\le n(n+1)/2\), and a zero index is \(0,4,5\pmod6\).  See
    `proof/elementary_lemmas.md`.
  - X (proved reduction): \(a_n=0\) if and only if
    \(a_{n-2}\mathbin{\mathrm{XOR}}a_{n-1}=n\); hence adjacent terms must
    have the same sign and differ by at most \(n\). See
    `proof/zero_xor_reduction.md`.
  - H (proved structural reductions): the dyadic shift signature has period
    three with an exact child table; the target is equivalent to three
    unit-value classifications; and exact bit stripping gives the corrected
    pair map H3.2. See `proof/structural_handoff_rederivation.md`.
    - H1 (proved): every zero-tree child is selected by one current quotient
      bit and the global three-phase signature.
    - H2 (proved equivalence): the three unit-value sets in H2.5 are exactly
      the original zero target in shifted coordinates.
    - H3 (open): classify those unit hits or close the iterated quotient types
      without discarding the lower residues/carries.
    - H4 (proved obstruction): each unit-subsequence rational 2-kernel span
      has dimension at least 2047; a smaller linear representation is
      impossible, but nonlinear or higher-dimensional closure remains open.
    - H5 (proved second strip): the quotient pairs satisfy the exact grouped
      map in `proof/handoff_extension_rederivation.md`; its internal
      subtraction requires a propagated borrow.  For every fixed window,
      same-window same-phase all-state examples require different affine
      corrections.  This does not exclude bit-serial closure on the
      distinguished orbit.
    - H6 (proved divisibility): binary-parent column differences and the H1
      signature give all-depth powers of two dividing the canonical U,V,W
      determinants.  The U/W exponent is stronger than the external handoff
      claimed.  Divisibility does not imply nonsingularity and therefore does
      not prove C002.
  - I (open): find a signed dyadic or zero-tree invariant that proves M3 or
    otherwise excludes zero beyond the certified base range.
