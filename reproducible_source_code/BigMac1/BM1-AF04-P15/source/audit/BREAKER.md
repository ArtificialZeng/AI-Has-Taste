# Breaker record

Role completed after Builder: 2026-08-30T04:44Z.

## Adversarial attacks

### Quantifier attacks

- Rejected the inference from one long finite word to an infinite word.
  König's lemma applies only to arbitrarily large depths in the prefix tree of
  one fixed finite alphabet.
- Rejected a uniform bound depending only on alphabet size. Keränen prefixes
  weighted by \(1,N,N^2,N^3\) give four-letter ASF words of length at least
  \(N-1\), so a negative solution cannot arise from such a bound.
- Rejected the modular van der Waerden route. If the modulus is \(m\), the
  guaranteed progression gap depends on \(m\); the resulting second
  difference bound is therefore not independently smaller than \(m\).
- Restricted the finite theorem to primitive normalized maximum at most 5.
  No monotonicity in maximum letter, alphabet inclusion, or alphabet size is
  assumed.
- Restricted the substitution theorem to four-state 2-uniform endomorphism
  fixed points. It does not cover codings from more hidden states,
  nonuniform morphisms, or uniform length at least 3.
- Restricted the Rao--Rosenfeld projection experiment to 30,000 symbols and
  primitive coefficient height at most 100.

### Computational attacks

- A handwritten second baseline witness initially had 63 digits. The
  independent verifier rejected it; the certificate was corrected from the
  discovery output and then rebuilt successfully.
- An early shell batch passed a space-separated alphabet as one argument and
  produced meaningless depth-one records. Those records were discarded, and
  every alphabet was rerun with four explicit integer arguments.
- The strict verifier is exercised against deletion of a required field,
  insertion of an unexpected field, a noninteger count, a nonprimitive
  alphabet, an inconsistent maximizer list/count, and a malformed digest.
  A seventh test deletes an entire canonical alphabet record. All seven
  schema and coverage corruptions must be rejected. Independently, the full
  replay compares every numeric tree invariant and rejects any mismatch.
- The two discovery and verifier kernels use different sum organizations:
  left prefix sums versus right-tail cumulative sums. This does not prove
  implementation independence by itself, but it removes shared executable
  state and shared traversal output.

## Breaker disposition

No attack invalidated the bounded census or the four-state 2-uniform no-go
statement. The attacks do invalidate several tempting routes to the original
infinite problem. Consequently, the infinite question remains open and may
not be marked proved or disproved.
