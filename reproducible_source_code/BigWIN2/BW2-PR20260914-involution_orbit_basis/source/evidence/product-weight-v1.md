# Product-weight hypothesis, version 1

Proposed in research pass 1, 2026-09-14, before the held-out weight tests.
This is a working hypothesis, not a proved theorem or an accepted contribution.

For every admissible n,a, write J_(n,a) for the kernel of the surjection from
Q[y_ij : 1<=i<j<=n] to R(M_(n,a)), sending y_ij to the class of x_ij.
Surjectivity follows from symmetry and the homogeneous row-sum relations,
which express every diagonal variable as minus its off-diagonal row sum.

Give y_ij the positive integer weight n^2-ij. For the literal Pieri–RSK set
B_(n,a) defined in problem.md, the stronger conjecture is:

For every matching monomial m outside B of degree d, there is a relation
m - sum_(b in B_d) c_b b in J_(n,a), and every nonzero c_b satisfies
sum_(ij in b) ij > sum_(ij in m) ij.

Together with the established cardinality formula, this would make B the
standard monomials of J for any monomial order refining that weight. Products
that are not squarefree matchings already vanish in J. This would answer the
original basis question and supply a specific Groebner proof route; it is a
strict strengthening of the source's candidate assertion.

Design evidence: exact QQ straightening and positive weight margins for all
excluded matching monomials at (5,1),(6,2),(7,1). The score -ij was chosen
after inspecting those cases. They are not held-out confirmation.

First held-out falsifiers: all degrees at (8,0),(8,2),(9,1),(9,3).
Check the exact normal-form support, not just agreement with a numerical LP.
A nonpositive margin refutes this strict version, even if the basis survives.
No novelty or conjecture-note eligibility has yet been established.
