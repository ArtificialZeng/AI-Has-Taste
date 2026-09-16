# Frozen source problem: nonexistence of SDS(9,8,1,C_3^2)

Canonical id: win-00086-p05
Frozen on: 2026-09-10 (Asia/Shanghai)
Primary sources:
- He--Wu, *Nonexistence Results and Constructions for Signed Difference
  Sets*, arXiv:2608.22936v1, equation (1.1) on PDF p.1, equations (2.3)--(2.4)
  and Lemma 2.1 on PDF p.4, Theorems 4.4 and 4.7 on PDF pp.9--11, and the
  conclusion on PDF p.18.
- The authors' official reproducibility repository
  `zhiwenhe94/sds-open-case-verification`, commit
  `de57332884c7bf417544285dee9a2cbb015a5fae`; its immutable `sds.json`
  snapshot records `SDS(9,8,1,[3,3])` with status `Open`.

## Definitions

Write `G=C_3^2` additively and identify its identity with `0_G`.  A signed
subset is

```
D = sum_{g in G} a_g g,  a_g in {0,+1,-1}.
```

It is an `SDS(9,8,1,G)` when exactly eight coefficients are nonzero and

```
D D^(-1) = 7*0_G + G
```

in the integral group ring.  Equivalently, the coefficient at zero is eight
and every nonzero group element has coefficient one.

## Statement

Decide whether `SDS(9,8,1,C_3^2)` exists.  A nonexistence proof must cover
every placement of the single zero coefficient and every assignment of the
eight signs, modulo only explicitly justified translation, global sign, and
`GL(2,3)` symmetries.

## Scope and contribution boundary

The source paper develops several general obstructions and its official
snapshot still marks this exact group-specific case open.  Before claiming a
new result, check whether a later database update, paper version, or other
primary publication has resolved the entry.  The source's own near-full
support congruence is only a necessary condition here and does not by itself
exclude the case.

Applying the principal character first fixes the positive/negative support
sizes up to global sign.  After translating the unique zero to `0_G`, a
proposed two-orbit proof must justify that the two negative positions are
either opposite nonzero vectors or a linearly independent pair.  For each
orbit it must display a nonprincipal character whose exact Eisenstein norm
contradicts the required value seven.

An independently replayable checker should enumerate all 28 unordered
negative supports after normalization, compute every character norm exactly
in `Z[omega]`, and confirm the symmetry reduction.  A database label, numeric
complex approximation, or solver assertion is not a certificate.

Any manuscript must cite He--Wu, the database/reproducibility snapshot,
Gordon's foundational signed-difference-set work, and any other literature
actually used for characters and group-ring context.  It must also include
one or two genuinely relevant user-Excel papers when available.  This is a
minimum rather than a reference limit, and irrelevant padding is forbidden.

This file is immutable.  Other groups of order nine or other parameter
triples are different problems.

