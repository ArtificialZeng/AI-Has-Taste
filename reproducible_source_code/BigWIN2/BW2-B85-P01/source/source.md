# Frozen source problem: product-local-unitary equivalence of two pairs of stabilizer codes

Canonical id: win-00085-p01
Frozen on: 2026-09-10 (Asia/Shanghai)
Primary source:
- Mahmoud, *Minimal Counterexamples of the MacWilliams Extension Theorem for
  Stabilizer Codes*, arXiv:2607.26214v1, Theorem 5.3(ii),(iii) on PDF
  pp.10--11 and Question 5.4 on PDF p.11.
Required prior literature:
- Van den Nest--Dehaene--De Moor, *Local invariants of stabilizer codes*,
  arXiv:quant-ph/0404106v2, especially equation (14) on PDF p.5.

## Definitions

Every displayed Pauli generator has phase +1. For a commuting independent
set of Pauli generators, let Q(S) be the common +1 eigenspace of the generated
stabilizer group S. Let P_pi be the tensor-factor permutation induced by a
permutation pi of the qubits.

On five qubits define

```
S_A = <ZZZZI, XXIIX, IIXXX>,
S_B = <ZZIZX, XIZXI, IXXYI>.
```

On six qubits define

```
S_+ = <XXIIXX, IIXXXX, ZZZZIX>,
S_- = <XXZXII, ZZXYII, IZZZXX>.
```

The allowed local operation is a product of arbitrary one-qubit unitaries
U_1 tensor ... tensor U_n, followed or preceded by a qubit permutation. It is
not an arbitrary entangling unitary. Antiunitaries are outside the statement.

## Statement

For each of the two pairs `(S_A,S_B)` and `(S_+,S_-)`, determine whether there
exist one-qubit unitaries U_i and a qubit permutation pi such that

```
(U_1 tensor ... tensor U_n) P_pi Q(S_left) = Q(S_right).
```

In particular, prove or disprove product-local-unitary-plus-permutation
equivalence separately for both pairs.

## Scope and contribution boundary

The primary source proves that the pairs have full support and are related by
weight-preserving stabilizer-group isomorphisms that do not extend to
monomial maps. It asks, but does not answer, the code-space equivalence above.

Support-dimension and reduced-state-rank invariants are prior art: equation
(14) of arXiv:quant-ph/0404106v2 already identifies the dimensions of
stabilizer subcodes supported in specified coordinate sets as local-unitary
invariants. A contribution here may be the explicit application and smallest
separating incidence certificate for Mahmoud's two new instances; it must not
claim invention of the invariant.

The Batch85 desktop computation of all eight elements in each stabilizer and
the resulting exceptional marginal-rank patterns is discovery-stage evidence,
not an accepted proof. A computer-assisted resolution must publish the full
Pauli/support tables and an independent checker for generator independence,
commutation, support-subspace dimensions, reduced-projector ranks, and the
nonexistence or existence of a coordinating permutation.

This file is immutable. Any altered phases, generator convention, or larger
equivalence group must be frozen as a different problem.
