# Exact horizon-9 defense certificate

## Claim certified

In the game formalized in `problem.md`, one positional O policy prevents X from
owning a transversal at every ply through ply 9, against every legal sequence
of X moves. Combined with the already established upper bound \(T_4\leq 11\)
recorded in `source.md`, this gives \(T_4=11\).

## Certificate and proof reduction

Cells are indexed by `4*row+column`, for rows and columns `0,1,2,3`.
`horizon9_policy.json` lists an O move for each reachable nonterminal O state,
represented by two disjoint 16-bit ownership masks. The implicit DAG has an
edge for every free-cell move at an X node and the listed edge at an O node.
Every edge adds one occupied cell, so the DAG is acyclic.

`verify_horizon9_policy.py` does not import the solver. It reconstructs all 24
transversal masks from the 24 permutations of four columns. Starting from the
empty board, it checks ownership disjointness and alternating move counts. At
each X node before the horizon it recursively checks all free-cell successors;
at each O node it checks and follows the certified legal move. It terminates a
branch immediately upon a win and rejects any X-winning branch. At the end it
also rejects missing, duplicate, illegal, or unreachable O-policy records.

The resulting `horizon9_verification.json` records 28,604 reachable states,
41,768 universally checked X edges, 6,861 checked O edges, 111 branches ending
in an O win, 16,721 safe horizon leaves, and zero X-winning leaves. Hence the
finite induction implemented by the verifier proves that this one O policy
answers every legal X history and prevents an X transversal through ply 9.
Therefore X cannot force a win by ply 9. X wins only on odd plies, so the
recorded upper bound by ply 11 forces the exact value \(T_4=11\).

## Reproduction

Run from the project root:

```sh
python3 evidence/horizon9_solver.py \
  evidence/horizon9_policy.json evidence/horizon9_solver_summary.json
python3 evidence/verify_horizon9_policy.py \
  evidence/horizon9_policy.json evidence/horizon9_verification.json
```

SHA-256 of the decisive policy is
`0fa7169bbccb23fb540c1138227447648375d4cc5dd8da4f9e35fc15b904509f`.
The solver is an unsymmetrized exact AND--OR search; its value alone is not
treated as proof. The proof artifact is the exact policy together with the
separately implemented exhaustive verifier and the inspectable reduction above.
