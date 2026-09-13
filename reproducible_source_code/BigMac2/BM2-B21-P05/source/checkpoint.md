# Checkpoint

- Job: `bigMac-00021-p05-research-84f422bb45d5` (research pass 1).
- Outcome: **resolution-paper candidate**; the frozen original claim
  \(\bar\chi_{\ge}(H(3,3))=4\) is proved in evidence/proof.md, subject to the
  required fresh referee. This research result is not an acceptance decision.
- Immutable input preserved: source.md still has SHA-256
  `ebbe264caf080f8158cce54870acfd5a01eddf57ddb0a704f6da2eaa51da5eab`.

## Complete argument

For every vertex, its six neighbors split into three adjacent pairs indexed by
the changed coordinate; vertices from different pairs are nonadjacent. Hence
\(H(3,3)\) has no \(K_4\). Also, an adjacent pair differs in one coordinate and
has exactly one common neighbor, obtained by using the third value in that
coordinate.

If an induced subgraph on at most five vertices had minimum degree at least
three, sizes at most three would be immediate impossibilities and size four
would force a \(K_4\). At size five, the missing edges form a matching. With
zero or one missing edge there is a \(K_4\); with two missing edges \(ab,cd\)
and fifth vertex \(e\), the adjacent pair \(e,a\) has two common neighbors
\(c,d\), also impossible. Thus every majority color class has at least six
vertices, and \(6p\le27\) gives \(p\le4\).

For the matching lower bound, the four classes are
\[
\{1\}\times[3]\times[3],\qquad
\{2,3\}\times\{j\}\times[3]\quad(j=1,2,3).
\]
They partition the vertex set, are nonempty, and have induced degrees four in
the first class and three in each other class. They give a surjective majority
\(C\) four-coloring.

## Exact reproducible evidence

- evidence/verify_resolution.py exhausts all
  \(\sum_{k=1}^{5}\binom{27}{k}=101{,}583\) subsets. It finds zero sets of
  size at most five with induced minimum degree at least three.
- The same script separately verifies the explicit partition, sizes
  \([9,6,6,6]\), exact coverage/disjointness, and degree multisets
  \(4^9,3^6,3^6,3^6\).
- evidence/verify_resolution.out is a captured run. A clean rerun was
  byte-for-byte identical.
- No mathematical gap is presently known. No novelty or priority claim is
  made, and current-literature comparison remains outside this proof pass.

Next test: a fresh referee should reconstruct the size-five complement argument
and the four-class degree counts without relying on this checkpoint, rerun or
independently reproduce the finite verifier, and accept or reject the exact
resolution scope frozen in claim.json.
