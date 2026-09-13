# Proof dependency graph

Terminal endpoint: the finite equality `|M_14|=8|M_13|`.

1. **Published dependency B1:** Berlow's periodic-point theorem: periodic
   iff half-decreasing.
2. **Published dependency Z1:** Zhang's maximum transient theorem:
   `max t_N = 2 floor((N-1)/2)`.
3. **L1:** push is illegal iff two current stack entries exceed the next
   input (`proof/finite_result.md`, Section 1).
4. **L2:** large-label factorization
   `kappa_m o s = F_m o kappa_m` (`proof/finite_result.md`, Section 2).
5. **L3:** by B1 and L2, membership in `M_N` depends only on the skeleton;
   each skeleton has `(N-m)!` lifts.
6. **C1:** complete enumeration at lengths 13 and 14 gives
   `|Q_13|=|Q_14|=9378` and checks
   `Q_14={wL:w in Q_13}`.
7. **C2:** L3 and C1 give the exact counts and the 8-to-1 terminal-deletion
   map.

Dependencies B1 and Z1 are source-audited in the claim ledger.  C1 is bound
to the JSON certificate and independently reconstructed by the verifier.
