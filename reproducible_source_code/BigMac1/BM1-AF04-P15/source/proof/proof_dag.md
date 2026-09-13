# Proof dependency graph

## Structural reductions

- R1 (proved): affine maps \(x\mapsto\alpha x+\beta\), \(\alpha\ne0\),
  preserve additive-square equality because both blocks have equal length.
- R2 (proved): every finite integer alphabet with at least two letters has a
  primitive normalized representative with minimum zero; reflection gives an
  additional involution.
- R3 (proved): for a fixed alphabet, arbitrarily long ASF words are equivalent
  to an infinite ASF word by K\"onig's infinity lemma on the prefix tree.
- R4 (proved): an appended letter can create a forbidden factor only at the new
  final position, so exact suffix checking makes prefix-tree DFS exhaustive.
- R5 (proved): prefix-sum equality is the midpoint identity
  \(S_i+S_{i+2\ell}=2S_{i+\ell}\).

## Certified finite endpoint DAG

1. R1--R2 enumerate all primitive normalized four-letter reflection classes
   with a bounded maximum letter.
2. R4 proves completeness of each exact DFS traversal.
3. A nonempty maximum-depth layer supplies the lower bound on \(g(A)\).
4. Closure of the full finitely branching tree supplies the matching upper
   bound.
5. The serialized counts and maximizers are reconstructed by an independent
   tail-sum implementation.

No item in this DAG implies a result for alphabets outside the enumerated
finite scope.
