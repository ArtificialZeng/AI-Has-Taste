# Precise reading of win-00086-p02

## Frozen claim and conventions

Let `S_4` be the permutations of `[4]={1,2,3,4}`, composed as functions, and
let

`F_1={s in S_4 : |{i in [4]:s(i)=i}|=1}`.

Use Pan's undirected left-Cayley convention: the vertex set of
`Cay(S_4,F_1)` is `S_4`, and distinct vertices `g,h` are adjacent exactly when
`h=s g` for some `s in F_1` (equivalently `h g^{-1} in F_1`). The set `F_1`
is inverse-closed. Identify `g` with the ordered tuple
`[g(1),g(2),g(3),g(4)]`; then this Cayley graph is `A(4,4,3)`, whose two
vertices are adjacent exactly when their tuples differ in exactly three
coordinates.

The task is only the parameter `(n,t)=(4,1)`. It asks for the graph up to
isomorphism and its **full** graph automorphism group: all vertex bijections
preserving adjacency, not merely group automorphisms or automorphisms
normalizing a regular Cayley action. There is no connectedness assumption.

## Exact target statement

Put

`V_4={1,(12)(34),(13)(24),(14)(23)}`.

The proposed resolution target is the conjunction:

1. `F_1` is the set of the eight 3-cycles, hence `F_1=A_4\V_4`.
2. The two connected components are the two parity cosets of `A_4` in `S_4`.
   In either component, the three `V_4`-cosets are independent sets of size
   four, and two vertices in different such cosets are adjacent. Therefore
   `A(4,4,3) ~= Cay(S_4,F_1) ~= 2 K_{4,4,4}`.
3. Since the maximal independent sets of a connected complete tripartite graph
   `K_{4,4,4}` are exactly its three parts,

   `Aut(K_{4,4,4}) ~= (S_4)^3 semidirect S_3 = S_4 wr S_3`.

   Since the full graph has two isomorphic connected components,

   `Aut(A(4,4,3)) ~= (S_4 wr S_3) wr S_2`,

   of order `((4!)^3 3!)^2 2! = 13,759,414,272`.
4. Pan's Conjecture 3.1 at `n=4,t=1` instead prescribes a group of order
   `|R(S_4)| |Inn(S_4)| 2 = 2(4!)^2 = 1,152` (the center of `S_4` is
   trivial). Thus the target, if proved and independently audited, disproves
   the universally quantified conjecture at this parameter.

## Scope, source status, and contribution delta

The live arXiv source is still v1 and its Conjecture 3.1 quantifies over all
`n>2` and `0<=t<=n-2`; it does not exclude disconnected graphs. A 2026 journal
publication record for the revised title was located, but its full text was
not accessible in this run, so whether the conjecture was corrected or
omitted there remains unverified. No inspected primary source states the
specific decomposition above, but the bounded search cannot establish
novelty or priority.

Nearest prior result: Pan's two extreme families (`t=0` and `t=n-2`). Proposed
delta: the first intervening parameter, an explicit disconnected
counterexample, together with its full automorphism group. Verification route:
the elementary coset proof above, the reproducible exhaustive 24-vertex check
in `evidence/triage_exact_check.py`, and then a fresh mathematical referee pass
that independently checks the graph and wreath-product argument and resolves
the journal-version gap.
