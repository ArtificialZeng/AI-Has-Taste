# Proof audit

Status: not yet run.
# Proof audit

## Terminal status

**Partial theorem.**  No perfect cuboid is produced and no global
nonexistence theorem is claimed.

## Statement-to-proof audit

| Claim | Independent check | Result |
|---|---|---|
| `u^2+v^2=5w^2` for the displayed `(r,s)` parametrization | direct expansion; signed grid in primary verifier | pass |
| all three face norms are squares | hand factorization; both edge-based verifiers | pass |
| factorization of `F=A^2+B^2+C^2` | expansion in Lemma 2.1; comparison with direct edge norm on a signed grid | pass |
| `v_13(F)=1` on four classes | values modulo `169`, not merely modulo `13` | pass |
| primitive scaling preserves the blocker | all three edges are nonzero modulo `13` in each class | pass |
| local bad sets at 23, 31, 67 | full projective enumeration, including `[1:0]`, by two implementations | pass |
| CRT ratio `95/102` | equal scalar-lift count per projective slope and exact rational arithmetic | pass |
| density corollary | Möbius inversion for each admissible residue class | pass |

## Adversarial checks

- Signed and zero parameter values were included in the identity test box.
- The projective point at infinity was checked separately for every sieve
  prime; it is not a bad point in any of the three lists.
- Zeros modulo a sieve prime were treated as survivors, not as nonsquares.
- The exponent-one claim was checked modulo `13^2`; divisibility modulo `13`
  alone was rejected as insufficient.
- The classic instance reduces to edges `(252,275,240)`, face diagonals
  `(373,348,365)`, and space norm `196729=13*15133`.
- The independent verifier imports neither the norm factorization nor the
  projective-slope implementation used by the generator.

## Remaining global gap

No argument shows that every Euler brick lies in this Lenhart-attributed
family.  The local sieve leaves `7/102` of its selected CRT cells unresolved.
These are explicit limitations in the title, abstract, introduction, and
scope section of the paper.
