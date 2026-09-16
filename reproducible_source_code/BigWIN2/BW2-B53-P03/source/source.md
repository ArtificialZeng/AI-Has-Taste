# Immutable source — win-00053-p03

## Original lead

Extend the dyadic order-gadget obstruction from the proved residue class `M≡0 mod 8` to the next source-supported class `M≡4 mod 8`.

## Precise frozen statement for triage

Using exactly the full order gadget `OG(M)` of Definition 15 in the cited source—an ordering of `(M,2M]` avoiding monotone three-term arithmetic progressions and satisfying all fifteen precedence constraints induced by the attacking values 15 and 16—prove or refute:

`For every integer M>=20 with M≡4 (mod 8), OG(M) is infeasible.`

A proof must give a uniform residue-class argument, not merely repeat finite SAT checks. A disproof must provide one explicit order with a complete checker for every AP and precedence constraint. Any extracted SAT conflict pattern must be translated into a mathematical lemma or accompanied by a proof-producing certificate checker.

## Primary source and delta

- William Kasel, *Structural rigidity in the Erdős–Graham two-set permutation problem*, arXiv:2609.02939v1, Definition 15, Proposition 18, Theorems 21–22, and Remark 30: https://arxiv.org/abs/2609.02939
- Local PDF: `batches/inbox/bigWin-53-materials/2609.02939.pdf`
- SHA-256: `22997afac6b8922d994dbfc8fb111d7ea45321cb49bf6b4a44c71c3a09ad61c9`
- Retrieved 2026-09-07.

The source proves a three-constraint core infeasible for `M≡0 mod 8`, conjectures the full gadget infeasible for every `M>=16`, and reports exact finite verification for `16<=M<=200` and `M=512`. It explicitly notes that nonzero residue classes require different attack subsets. The proposed delta is the `4 mod 8` uniform subfamily; it does not claim to solve Erdős–Graham Problem #197.
