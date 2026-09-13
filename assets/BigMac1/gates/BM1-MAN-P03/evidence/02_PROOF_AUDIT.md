# Proof audit

Status: **passed for a certified finite result**.

Audit date: 2026-08-21.

## Claimed endpoints

1. Every nondegenerate subset of the ternary four-cube
   \(\{-1,0,1\}^4\) has Borsuk number at most four, and four is attained.
2. The largest spherical code with angular constraint
   \(\langle x,y\rangle\leq 1/2\) drawn from the individually normalized
   nonzero vectors of \(\{-1,0,1\}^5\) has size 40; the only maximum in
   this fixed library is the full weight-two shell.
3. The standard 40-point \(D_5\) and 72-point \(E_6\) constructions pass
   exact size, rank, norm, and inner-product checks.

These are finite-library theorems.  The paper does not claim a Borsuk
counterexample below the published frontier or determine the unrestricted
five- or six-dimensional kissing numbers.

## Exact verification

- `python code/run_all_verifiers.py` completed without error.
- The Borsuk verifier checked all distance layers.  At squared diameter 6 it
  checked 15,056 maximal compatibility cliques in 72 signed-permutation
  orbits, together with an explicit four-coloring for every representative.
- The lower witness consists of four pairwise equidistant points, so the
  upper bound four is sharp.
- The primary kissing-code branch-and-bound search returned 40.  Conditioned
  maxima by support weight 1 through 5 were 33, 40, 38, 35, and 31.
  Signed coordinate permutations are transitive on each support shell, which
  isolates the weight-two shell in every equality case.
- An independent NetworkX exact maximum-clique evaluator also returned 40.
- Integer predicates are used for the normalized-ternary compatibility test;
  no floating-point comparison enters the proof.

## Adversarial review

- Degenerate zero-diameter sets are excluded in the theorem statement and do
  not affect the maximum.
- Subsets not maximal under the diameter constraint inherit the coloring of a
  maximal superset, which closes the coverage gap in the Borsuk enumeration.
- The six-dimensional benchmark proves the existence and exact rank of the
  displayed \(E_6\) code only.  No unproved assertion about representability
  in the naive six-coordinate ternary library is retained.
- The public 63-dimensional Borsuk repository was checked at an exact commit
  and is described as a public proof note, not as peer-reviewed literature.

Major proof gaps: none for the stated finite endpoints.

Machine-checked formal proof: not provided.  The result instead includes
deterministic exact verifiers and a hash manifest.
