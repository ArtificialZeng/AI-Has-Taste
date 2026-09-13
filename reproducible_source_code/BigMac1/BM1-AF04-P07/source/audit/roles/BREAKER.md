# Breaker record

The Breaker independently searches for a literal 55-bit tournament with
maximum packing at most 14, attacks extension lemmas, and retains exact
counterexamples to any proposed pruning rule.

## 2026-08-30 actions

- Exhaustively generated the 32 combinations of canonical tournaments inside
  the parts of cyclic (C_3[T_4,T_4,T_3]) blow-ups.  Both target searchers
  found 15-packings in every case.  The structural hitting argument bounds
  all of them by 15.
- Ran `code/exact_max` on the retained literal minimizer
  `1111111000111111000111110001111000111111111111111111111`; its independent
  full branch-and-bound maximum was 15.  This discovery result is not trusted
  by the short minimizer verifier.
- Tested 100,000 deterministic random labeled tournaments (seed 20260830)
  using both exact target algorithms.  Both accepted all cases and produced
  the same input-stream digest
  `a332efdf49f930726b9493f5e0aa8b4394e87585fc699fb1ad3b34a712051386`.
- The decisive disproof search was the exhaustive canonical Builder scan: any
  first tournament without a 15-packing would have been printed literally and
  stopped its slice.  All 903,753,248 representatives were accepted, so no
  below-target candidate exists within the declared canonical-generator trust
  base.

Negative random or structured evidence is diagnostic only.  It is not used as
the universal lower-bound proof.
