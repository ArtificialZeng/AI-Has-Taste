# Finite-result certificate

## Mathematical scope

For a connected simple graph, equality of the number of vertices and edges
is equivalent to unicyclicity. Nauty's command

    nauty-geng -c n n:n

therefore generates one representative of every isomorphism class of
connected unicyclic graphs of order \(n\).

The generated totals are:

| order | canonical graphs | external enumeration cross-check |
|---:|---:|---:|
| 17 | 880,840 | OEIS A001429: 880,840 |
| 18 | 2,497,405 | OEIS A001429: 2,497,405 |

The clean order-17 independent verifier assigned a distinct three-evaluation
signature to every one of the 880,840 graphs. Hence no two connected
unicyclic graphs of order 17 have the same CSF.

At order 18, the target class excludes the 825,784 triangle-unicyclic graphs
because the order is even.  The remaining 1,671,621 graphs have cycle lengths
4 through 18.  The independent verifier encountered one pair with the same
three primary values and the same refinement value; the pair also had the
same degree sequence, rooted-tree count, and internal-edge count.  It found
no evaluation match with different structural data.  Since CSF equality
implies equality at every specialization, this certifies Conjecture 63 at
order 18.  It does not certify that the one same-data evaluation match has
equal CSF.

The exact cycle-length coverage and fixed evaluation data are frozen in
`experiments/verify_n17/result.json` and
`experiments/verify_n18_target/result.json`.  Input-stream and separation
digests are kept separately under `audit/` and are deliberately excluded from
the manuscript and submission source archive.

## Trust boundary

- Nauty supplies canonical exhaustive generation.
- Exact specialization values are recomputed from graph6 input.
- The discovery and verifier implementations use different parsers,
  cycle extraction, recursion style, transfer aggregation, primes, and
  evaluation points.
- Modular values are used only to prove inequality or to retain candidates.
  A modular collision is not a proof of equality.
- Direct spanning-subset and weighted deletion--contraction programs are
  available for full integer exactification.
- The discovery scan and independent verifier agree that there is no
  different-data candidate at either order.  Their graph parsers, cycle
  routines, transfer formulations, primes, and evaluation points are
  disjoint.
