# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the frozen `resolution-paper` claim at snapshot
`8041d56c5682f00092449a1e8e39378badd9c8c539958d539f59ee50f1fc72ef`.
The claim is that, for every integer `M >= 20` with `M congruent to 4
(mod 8)`, AP-freeness on `(M,2M]` is incompatible already with

`C4 = {t_13 preceding b_1, t_11 preceding b_2,
       t_5 preceding b_5, t_10 preceding b_3}`.

This is stronger than, and directly implies, infeasibility of the full order
gadget because all four relations are among Definition 15's fifteen attack
relations. I find the uniform proof correct in the claimed scope, including
both residue subclasses modulo 16 and their smallest cases. **Verdict:
accept.**

## Integrity and source checks

I recomputed the SHA-256 digest of every frozen file. Every digest equals its
entry in `audit/snapshot.json`; canonical hashing of the sorted compact `files`
mapping gives the recorded snapshot digest above. In particular, `source.md`
has SHA-256
`d76e82a13d4830e1f75b20784bab4579375ef74b39e398d896f37f362904eece`,
and the supplied primary-source PDF has SHA-256
`22997afac6b8922d994dbfc8fb111d7ea45321cb49bf6b4a44c71c3a09ad61c9`.

I inspected the actual cited portions of the PDF. Definition 15 agrees with
the stated gadget. Proposition 19 reports the same C4 core infeasible only at
the swept `M congruent to 0 (mod 4)` instances and expressly makes no claim
outside its finite sweep. Theorem 22 proves a different C3 core only for `M
congruent to 0 (mod 8)`. Lemma 26 supplies the mirror-flood argument for
`g=2,4`, and Remark 30 leaves the other residues of the full gadget open while
suggesting per-residue analogues. Thus the candidate is not silently replacing
an existing theorem from the cited source: its precise delta is the uniform
`M congruent to 4 (mod 8)` C4 obstruction. The dated literature record reports
no separate primary source for this exact gadget; this is an appropriately
bounded search statement, not a priority guarantee.

## Reconstruction of the decisive argument

For a numerical progression `a<b<c`, midpoint extremality gives the four
valid implications

`a≺b => c≺b`, `c≺b => a≺b`,
`b≺c => b≺a`, and `b≺a => b≺c`.

Consecutive triples on any fixed-step ladder therefore force alternating
leader and trailer rungs. The proof's extension of the flood lemma from
`g=2,4` to any positive even `g`, particularly `g=8`, is valid. If the flood
center is shifted by `g/2` from a ladder class, the two members of each
admissible mirror pair differ by `2e congruent to g (mod 2g)`, so exactly one
is a leader in either zigzag phase. The mirror rule copies the seed to its
partner. Moving the distance by `+g` or `-g`, a leader-to-neighbor edge plus
transitivity reaches one member of the next pair, and the mirror rule reaches
the other. The same construction with inequalities reversed proves the inward
version. The admissible distances form one finite consecutive interval modulo
`g`; hence induction reaches exactly all members whose reflections remain in
the block. This verifies the claimed phase-blind 8-flood and reveals no
boundary or uniformity assumption omitted from its statement.

Write `m=3M/2`. Since `M congruent to 4 (mod 8)`, `m congruent to 2 (mod 4)`.
To reconstruct Lemma 1, suppose contrary to the desired orientation that
`b_3≺b_5`. The odd 2-ladder then has leader class `3 (mod 4)`. Put
`c*=m-1` and `c**=m+1`.

- If `t_5≺m`, the polar 2-flood puts every odd value before `m`. A 4-flood
  at `c*` gives `b_3≺c*`, using reflection `2c*-b_3=t_5`. A 2-flood at
  `c*`, seeded by `c*≺m`, gives `c*≺t_10`, using reflection
  `2c*-t_10=b_8`. With `t_10≺b_3`, this is a strict cycle.
- If `m≺t_5`, the polar flood puts `m` before every odd value. A 4-flood at
  the leader `c**` gives `c**≺t_11`, with reflection `b_13`. A 2-flood at
  `c**`, seeded by `m≺c**`, gives `b_2≺c**`, with reflection `t_0`.
  Together with `t_11≺b_2`, this is a strict cycle.

All named reflections lie in `(M,2M]` for `M>=20`. Thus Q and A3 force
`b_5≺b_3`.

Under `b_5≺b_3`, the odd leader class is `1 (mod 4)`. This makes each chosen
center below a valid 4-flood center for the `3 (mod 4)` class.

For `M congruent to 4 (mod 16)`, take `c=m-5` and `d=m-1`, respectively
`1` and `5 (mod 8)`. A 4-flood gives `c≺t_13` (reflection `b_3`), and P
then gives `c≺b_1`. The 8-flood at `c`, seeded at `b_1` with reflection
`t_11`, gives `c≺d`; the target reflection is `m-9`. Similarly a 4-flood
gives `d≺t_5` (reflection `b_3`), and A1 gives `d≺b_5`. At `M=20`,
`b_5=c`, immediately contradicting `c≺d`. For the remaining members of this
subclass (`M>=36`), the 8-flood at `d`, seeded at `b_5` with reflection
`t_7`, gives `d≺c`; its target reflection is `m+3`. The tight inequality
`m-9>=M+1` is exactly `M>=20`.

For `M congruent to 12 (mod 16)`, take `c=m-1` and `d=m-5`, again `1` and
`5 (mod 8)`. The same 4-flood/P chain gives `c≺b_1` (here the first
reflection is `b_11`), and the 8-flood at `c` gives `c≺d`, with seed
reflection `t_3` and target reflection `m+3`. A 4-flood at `d` gives
`d≺t_13≺b_1`. The numerical triple `(b_1,d,t_11)` is an AP, so midpoint
extremality gives `d≺t_11`. The leader `t_11` is a 4-flood center and yields
`t_11≺t_5` with reflection `t_17`; A1 then yields `d≺b_5`. Finally, the
8-flood at `d`, with seed reflection `t_15` and target reflection `m-9`,
gives `d≺c`, contradicting `c≺d`. At the least case `M=28`, the AP has
positive common difference `M/2-6=8`, and every named point and reflection
is in the block.

The two modulo-16 branches exhaust `M congruent to 4 (mod 8)`, so the proof is
uniform rather than a finite extrapolation. Lemma 1 uses Q and A3, while the
flip uses P and A1; therefore it establishes precisely the asserted C4
infeasibility and hence the original full-gadget claim.

## Computational checks actually performed

I inspected both exact models in `c4_exact_sat.py`. In the eager model, a
tournament variable is supplied for every unordered pair, the two clauses per
numeric triple exclude both directed 3-cycles, the two clauses per in-block AP
exclude both monotone orientations, and the four C4 relations are units. Thus
an UNSAT answer is about strict total orders satisfying exactly the submitted
constraints. The rank model instead uses an all-different position for every
block element and a reified before-both/after-both midpoint condition, so it is
a materially different finite encoding.

I freshly ran the uniform schema checker through `M=16380`; it returned PASS
on 2046 instances in both modulo-16 subclasses and reproduced the stored
records digest
`1536fb575e40205abdef88a3162fa78f7bad7515932dffb9b6d1255e98a4c5ff`.
I also freshly ran the eager encoding at `M=20,28,36,44,52`, obtaining UNSAT
in every case, and the rank encoding at `M=20,28,36`, obtaining INFEASIBLE in
every case. Instance digests for the shared cases agree with the frozen
cross-check record. These finite computations are corroboration only; the
acceptance rests on the quantified argument reconstructed above.

## Gaps and final assessment

I found no unresolved mathematical gap, quantifier mismatch, degenerate
attack, out-of-block reflection, or unsupported limiting step. The proof does
not claim to solve the broader Erdos--Graham problem, and its source comparison
states the literature limitation honestly. The exact frozen full-resolution
scope passes correctness, scope, and contribution review.
