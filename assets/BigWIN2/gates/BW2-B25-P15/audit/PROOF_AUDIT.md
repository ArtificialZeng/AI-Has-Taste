# Proof audit

- Audited endpoint: `a_n` is composite for every integer index `5 <= n <= 21`.
- Reconstructed the odd-index lemma directly modulo 3.
- Re-ran the serialized-certificate verifier: all 16 index-divisor pairs passed primality, divisibility, and properness checks.
- Independently recomputed every exact recurrence term through `a_21` with SymPy-backed primality checks. All 16 listed divisors are prime and proper, every modular remainder is zero, `a_20` has 909982 bits, and `a_21 mod 3 = 0`.
- Independently recomputed the full residue chain modulo 7,795,379; it ends in zero at index 20. SymPy and deterministic trial division both certify 7,795,379 prime.
- Strengthened the manuscript's properness argument by bounding every listed divisor, not only the new endpoint.
- The unresolved gap for all indices at least 22 remains explicit; the note makes no full-resolution claim.
- No proof assistant was used.

Status: PASS (2026-09-02).
