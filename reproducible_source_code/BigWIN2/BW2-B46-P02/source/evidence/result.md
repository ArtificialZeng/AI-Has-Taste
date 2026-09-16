# Exact four-color result for the specified graph

## Result

Alice has a winning strategy in the four-color game on the ten-vertex graph
defined in `problem.md`. Consequently, using the cited lower bound
\(4\leq\chi_g(M_2(C_3))\),
\[
\chi_g(M_2(C_3))=4.
\]

This is an exact finite result, not a floating-point experiment. The complete
machine-readable strategy is `strategy.json`; vertex numbers 0--2, 3--5, and
6--8 are respectively \(v_1^0,v_2^0,v_3^0\), \(v_1^1,v_2^1,v_3^1\), and
\(v_1^2,v_2^2,v_3^2\), while vertex 9 is \(\omega\). Colors are 1--4.

## Certificate semantics and soundness

Every state in the DAG is a proper partial coloring in canonical form. The
allowed symmetries are simultaneous permutations of the three indices in all
three layers and arbitrary permutations of the four color names. They preserve
the graph, move legality, terminal status, and the player to move. Canonical
states are the lexicographically least states in their symmetry orbit.

At every Alice node the certificate gives one legal move. At every Bob node it
gives every raw legal pair (uncolored vertex, available color), without first
quotienting or deduplicating those replies. Each edge points to the canonical
form of the state obtained by its stated move. The number of colored vertices
increases by one along every edge, so the DAG is well-founded. Every reachable
leaf is a fully colored state. Induction backward on the number of uncolored
vertices therefore proves that the recorded move wins for Alice at each Alice
node and survives every possible legal move at each Bob node, including the
empty initial state.

`verify_strategy.py` checks this argument without importing solver code. It
reconstructs the 18-edge graph, checks properness, move legality, terminal
labels, turn parity, successor states, and exact Bob-reply coverage. For an
independent implementation of the quotient, it enumerates all
\(6\cdot24=144\) index/color actions per state rather than using the solver's
first-occurrence color normalization. Its recorded run checks 1,020 nodes and
2,467 edges, including 1,809 raw Bob moves; the 36 reachable leaves are all
fully colored and none is dead. See `verification.json` for the exact report
and certificate SHA-256.

## Reproduction

From the project directory:

```sh
python3 evidence/minimax_solver.py --output evidence/strategy.json
python3 evidence/verify_strategy.py evidence/strategy.json \
  --report evidence/verification.json
```

The first script performs Boolean minimax with memoization after the stated
safe symmetry reduction and exports the winning strategy. The second script is
the decisive checker: a successful replay of the full strategy certificate is
itself sufficient to establish Alice's four-color upper bound, independently
of the solver's unexplained outcome bit.
