# Immutable source statement: win-00049-p01

## Title

All minimum bondage sets of the truncated-octahedral graph, up to automorphism

## Original lead (preserved)

> Classify every five-edge set that raises the domination number of the truncated-octahedral graph, not just one witness.

This is a proposed finite refinement of the cited paper. It is not quoted there as an open problem and must be described as a status-uncertain new finite classification until the literature audit is complete.

## Exact proposed statement

Let (T) be the 24-vertex truncated-octahedral graph with the exact edge list printed in Srivastava, arXiv:2609.02477v1, §3. For a graph (G), let (gamma(G)) be its domination number and let

\[
\mathcal M(T)=\{F\subseteq E(T): |F|=5\text{ and }\gamma(T-F)>\gamma(T)\}.
\]

Determine exactly:

1. the cardinality (|\mathcal M(T)|);
2. every orbit of (mathcal M(T)) under the full graph automorphism group (operatorname{Aut}(T));
3. for each orbit, a canonical representative, orbit size, stabilizer size, and the exact value of (gamma(T-F)).

The source proves (gamma(T)=8) and (b(T)=5). Hence every member of (mathcal M(T)) is automatically a minimum-cardinality bondage set. A list of examples, a classification under only a subgroup, or a search that assumes every five-edge set raises the domination number does not resolve the statement.

## Quantifiers and conventions

- The edge set is the 36-edge labeled graph in the source; unordered edge pairs are used.
- The automorphism group is the full abstract graph automorphism group computed from that edge list, not merely a visually chosen subgroup of Euclidean solid symmetries unless equality of the two is verified.
- The definition uses strict domination increase. Record if any (F) raises (gamma) beyond nine rather than assuming the increase is exactly one.
- Orbit completeness concerns all (inom{36}{5}=376{,}992) five-edge subsets.

## Primary source and nearest result

- Prateek R. Srivastava, *The Truncated Octahedral Graph Has Bondage Number Five*, arXiv:2609.02477v1.
- Official records: <https://arxiv.org/abs/2609.02477> and <https://arxiv.org/pdf/2609.02477>.
- Lemma 1 on pp.2–3 proves (gamma(T)=8); Theorem 1 on p.3 proves (b(T)=5); §5 on p.4 specifies the exhaustive verifier.
- The proof checks all 58,905 four-edge sets and supplies one five-edge witness (F_5=\{02,14,15,26,27\}). It does not enumerate all five-edge bondage sets or their automorphism orbits.

## Precise delta and value

The proposed delta is the complete internal classification of minimum bondage mechanisms on the first explicit cubic planar counterexample to the planar bondage conjecture. It does not claim a new counterexample, a smaller order, or a general theorem about all planar graphs. A useful result should expose whether the counterexample is rigid or has several inequivalent minimal failure modes.

## Required exact certificate

1. Parse and recheck the source edge list, simplicity, degree sequence, connectedness, and (gamma(T)=8).
2. Independently enumerate every dominating eight-set of (T) (the source reports 1,767) and use it to decide each five-edge subset exactly.
3. Compute (operatorname{Aut}(T)) from the labeled adjacency relation, record generators and order, and verify every generator preserves the graph.
4. Canonicalize all members of (mathcal M(T)), verify the orbit-stabilizer identity for each representative, and verify that the orbit union is disjoint and has the reported total size.
5. For each representative replay (gamma(T-F)) by an explicit dominating set for the upper bound and exhaustive exclusion for the lower bound.

## Cheapest decisive route and fast falsification

Use 24-bit closed-neighborhood masks and the source's 1,767 minimum dominating sets. For each five-edge set, test whether every minimum dominating set loses domination; enumerate size-nine candidates only for surviving sets. Obtain graph automorphisms through exact labeled isomorphisms, then orbit the accepted sets. Any missing five-edge subset, nonpreserving generator, orbit size not dividing the group order, surviving dominating eight-set, or incorrect domination witness immediately falsifies the output.

## Frozen primary material

- `batches/inbox/bigWin-49-materials/2609.02477.pdf`
- SHA-256 `38fbee3e394ed40b4c1cde696d6241beff70fde4a43d3bcd835d4dc139c14b22`
- Retrieved from the official arXiv PDF endpoint and checked as a five-page PDF on 2026-09-07.

