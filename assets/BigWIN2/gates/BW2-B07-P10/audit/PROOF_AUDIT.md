# Proof audit

Audit date: 2026-08-31.  Scope: the theorem actually stated in
`paper/main.tex`, namely the certified interval and the exact disconnected
count.  The exact value of \(U(17)\) is expressly outside that theorem.

## Human argument

- Definitions and quotient convention agree with the locked formal statement;
  duality is not factored out.
- The bivariate Euler-product coefficient uses only
  \(C(1),\ldots,C(16)\) when the component number is at least two.  This
  establishes the reduction and every listed component stratum.
- In the Burnside construction, cycles are distinguishable blocks.  Pair
  orbits have the asserted gcd count and project onto both blocks.  The
  ordered-block relation is antisymmetric and transitive, its block order and
  adjacent patterns are recoverable, and exactly the complete-adjacency
  cases overlap the uniform family.  The matching family is internally
  injective; nonuniform pairs recover the matching.  It is separated from
  the ordered family by disconnectedness for more than two blocks, and the
  two-block overlap is explicitly omitted.
- Conjugacy classes are weighted by \(17!/z_\lambda\).  Applying Burnside to
  subsets of fixed objects gives a lower bound; taking the ceiling is valid
  because \(U(17)\) is an integer.
- Deleting a maximal point gives a surjection from 16-point classes together
  with ideals onto all 17-point classes.  Ideals correspond to antichains,
  then to cliques of the complement of the comparability graph.  The cited
  Kruskal--Katona consequence bounds each clique size by colex, and the
  displayed colex formula includes the empty clique, singletons, and both
  edge extremes.

## Exact computational evidence

The clean fail-closed gate runs nine positive checks and four negative-input
checks.  The decisive arithmetic uses integers only:

- three independent disconnected evaluations agree component by component;
- two lower-bound implementations use different state spaces (cycle
  multiplicities versus distinguishable-cycle bit masks);
- two upper-bound implementations use a closed formula versus enumeration of
  all vertex subsets of every colex graph;
- a separate parser matches all 121 histogram entries to the archived source
  PDF;
- exhaustive labeled-poset checks through order 5 attack both structural
  inequalities;
- malformed certificate fixtures are rejected.

The certificate gate passes in an empty environment with only the standard
binary path and a fixed locale.  No floating point, random search, timeout,
or `UNKNOWN` result enters either endpoint.

## Edge cases and limitations

Identity and single-cycle block systems, gcd-one pairs, the \(r=2\) overlap,
zero and complete complement graphs, and the empty ideal were reviewed.
The exact route is still missing complete fixed counts for permutations with
multiple nontrivial cycles; the direct generator is limited to 16 points.
These are fatal to the original exact target but not gaps in the stated
interval theorem.

Status: **passed for the partial theorem**.  Scientific terminal status must
remain **partial theorem**, not proved or certified exact \(U(17)\).
