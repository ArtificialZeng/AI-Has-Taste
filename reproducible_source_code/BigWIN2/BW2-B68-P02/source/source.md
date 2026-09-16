# win-00068-p02 — Complete census for equitable 4-total colorability below order 20

## Frozen source statement

Throughout, graphs are finite, simple, and undirected. Let `G` be a connected cubic graph, so every vertex has degree three. A proper `4`-total coloring is a map

`phi: V(G) union E(G) -> {1,2,3,4}`

such that adjacent vertices, adjacent edges, and every incident vertex-edge pair receive different colors. The graph is **Type 1** when its total chromatic number is `chi''(G)=4`. A proper `4`-total coloring is **equitable** when, for its color classes `c_i=phi^{-1}(i)`,

`||c_i|-|c_j|| <= 1` for every `i,j in {1,2,3,4}`.

Resolve the following finite statement:

> Every connected Type 1 cubic graph `G` with `|V(G)|<20` admits at least one equitable proper `4`-total coloring.

Equivalently, decide whether the known order-20 graph `R` is minimum-order among Type 1 cubic graphs with equitable total chromatic number `chi''_e(G)=5`. The quantifier is existential over equitable colorings: the problem does **not** assert that every `4`-total coloring of such a graph is equitable.

## Required complete census and certificates

The resolution must cover, without sampling, every isomorphism class of connected simple cubic graphs of each even order below `20`. Preserve a canonical `graph6` code for every graph and record the generator, exact command, version, count by order, total count, ordering convention, and cryptographic hashes of the census and result tables. Reconcile the resulting total with the source's count of `45,982` connected cubic graphs of order less than `20`; any discrepancy must be resolved rather than ignored.

For each graph `G`, use independently replayable encodings for:

- `A_G`: existence of a proper `4`-total coloring;
- `E_G`: existence of an equitable proper `4`-total coloring.

A direct SAT encoding may use variables `x_(a,i)` for `a in V(G) union E(G)` and colors `i in {1,2,3,4}`, exact-one constraints for every element, conflict clauses for every adjacent or incident pair, and checked cardinality constraints for equitability. Since a cubic graph of order `n` has `5n/2` vertex-and-edge elements, the four color-class sizes in `E_G` must differ pairwise by at most one. The implementation and verifier must derive these bounds from this total, not assume a favorable profile.

A positive census certificate must give, for every graph, either:

1. an explicit equitable `4`-total coloring, checked directly against the `graph6` graph; or
2. a machine-checkable UNSAT certificate for `A_G`, proving that the graph is not Type 1.

If the statement is false, provide the least-order counterexample(s), their canonical `graph6` codes, an explicit proper `4`-total coloring witnessing Type 1, and a machine-checkable UNSAT certificate for `E_G`. DRAT/LRAT or another proof format is acceptable only with the exact CNF, hashes, verifier version, and a successful independent replay. Solver exit status, a database flag, or failure to find a coloring is not a certificate.

The final verifier must also check cubicity, simplicity, connectedness, order, graph6 decoding, absence of duplicate isomorphism classes, completeness of the generated census, every supplied coloring, and every UNSAT proof. Record hardware-independent seeds and all nondeterministic options. A smaller subcensus may be used during triage but cannot settle the frozen statement.

## Source and contribution boundary

Primary source: Matheus Adauto, Celina de Figueiredo, Diana Sasaki, and Rafael Schneider, *Order 14 is the largest order for which every 4-total coloring of every cubic graph is equitable*, arXiv:2609.05259v1, especially Question 7.1 and the discussion immediately following it in Section 7: <https://arxiv.org/abs/2609.05259>.

The source proves a different universal statement about **every coloring** only for certain orders, gives non-equitable colorings at orders `12`, `16`, and `18`, and observes that those displayed graphs nevertheless also admit equitable colorings. Question 7.1 instead asks whether **every Type 1 graph** below order `20` admits at least one equitable coloring and explicitly proposes a systematic census using integer programming or SAT. This project freezes exactly that finite question and requires a complete, independently checkable computational proof; it does not extend the claim to order `20` or higher.

