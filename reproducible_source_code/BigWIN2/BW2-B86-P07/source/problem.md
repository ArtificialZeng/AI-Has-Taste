# Precise interpreted problem

## Frozen input and ambient conventions

The immutable input is `source.md`, whose SHA-256 is
`0ef7e09d275314f53febd468b6f3933ff31d2255762112050dd71580ebc4b160`.
All graphs below are finite, simple, and undirected. Graph isomorphism and
ordinary subgraph containment are understood up to relabeling.

For two graphs `A` and `B` of order five, write `A \preceq B` when there is a
bijection `phi: V(A) -> V(B)` such that `phi(E(A))` is a subset of `E(B)`.
(Because the orders agree, the injective map in ordinary subgraph containment
is necessarily a bijection.) They are *comparable* when `A \preceq B` or
`B \preceq A`, and *incomparable* otherwise. This is ordinary-subgraph, not
induced-subgraph, comparability.

Let `T*` have vertex set `{c,a,b,d,e}` and edge set
`{ca,cb,cd,de}`. Thus its degree multiset is `{3,2,1,1,1}`, its independence
number is three, and its only nontrivial automorphism swaps `a` and `b`.

For every finite simple graph `G` with `|V(G)| >= 5`, define

```
G is T*-exact
<=> for every U subset V(G) with |U| = 5,
    G[U] is isomorphic to T*, or
    neither G[U] \preceq T* nor T* \preceq G[U].
```

Only `G[U]` is induced; the two containment tests in the second line are
ordinary containment. Every five-subset is quantified, with no restriction to
selected subsets. Define

```
f(T*) = max {|V(G)| : G is a finite T*-exact graph}.
```

The frozen target is the precise equality `f(T*) = 8`. Equivalently, the
required mathematical work is (i) an eight-vertex `T*`-exact example and (ii)
nonexistence of a nine-vertex `T*`-exact graph; hereditary failure then rules
out every larger graph. The scope is this single five-vertex tree, not all
trees.

## Nearest prior result and source status

The primary source is Yair Caro, Zsolt Tuza, and Christina Zarb,
*Induced/Incomparable versus Ramsey*,
[arXiv:2605.22077v2](https://arxiv.org/abs/2605.22077), retrieved 2026-09-10.
The arXiv record identifies v2, revised 2026-05-27, as the latest version; the
PDF itself says “Latest update on May 28, 2026.” Its definition is on PDF p.2,
Fact 2.1(4) is on p.4, Theorem 5.1 is on p.14, Theorem 6.1 is on pp.15–16, and
Problem 1 is on p.24. Fact 2.1(4) states the needed hereditary observation.
For `T*`, Theorem 5.1 gives

```
f(T*) >= (alpha(T*) - 1)(5 - 1) = 8,
```

and Theorem 6.1 gives `f(T*) <= (5 - 1)^2 = 16`. Section 7 asks for `f(T)`
for every tree, so determining `f(T*)` is explicitly covered by a source-open
problem. The specific proposed value eight is not asserted by that paper and
remains an unproved target at intake.

There is a bibliographic error in the frozen source: current arXiv metadata and
the v2 PDF name Christina Zarb, not Mariusz Zarb. This does not alter the
mathematical statement, and `source.md` remains unchanged.

Live checks on 2026-09-10 inspected the arXiv v2 record and PDF and searched
the exact title plus combinations of `H-exact`, `T*`, and `subdivided claw`.
They located the primary preprint and non-primary mirrors/reviews, but no later
primary paper resolving this tree or an equivalent formulation. This limited
search supports continued investigation; it is not a priority or novelty
claim. The experimental arXiv HTML conversion shows an inconsistent internal
“Latest update” date, but its relevant definitions and results agree with the
v2 PDF and version record used here.

## Direct intake checks

The known lower construction is `G = 2 K_4`. Every five-set meets its two
components in sizes `4+1` or `3+2`, hence induces respectively `K_4 + K_1`
(six edges) or `K_3 + K_2` (four edges). Both are disconnected and therefore
cannot contain the connected spanning graph `T*`. The former has too many
edges to be contained in `T*`; the latter has the same edge count as `T*` but
is nonisomorphic, so it also cannot be contained in `T*`. Thus `2 K_4` is
`T*`-exact. This is the source's lower-bound mechanism, not a new result.

The exact script `evidence/triage_reconstruct.py` exhausts all `2^10 = 1024`
labeled five-vertex edge patterns. It independently obtains 60 labeled copies
of `T*` (`5!/2`), 817 comparable patterns including those copies, and hence
757 comparable but nonisomorphic forbidden patterns. It also checks all 56
five-subsets of `2 K_4`. These finite counts do not prove nine-vertex
nonexistence.

## Proposed contribution and verification route

Nearest prior result `X`: `8 <= f(T*) <= 16`. Proposed delta `Y`: prove the
nine-vertex nonexistence theorem, sharpening the upper bound to eight.
Verification route `Z`: use variables `x_ij` for the 36 unordered pairs
`0 <= i < j <= 8`. For each of the `binom(9,5) = 126` ordered-by-vertex
five-sets `U` and each of the 757 forbidden local patterns `P`, add the
ten-literal clause that is false exactly when `G[U] = P` (use `not x_ij` for
an edge of `P` and `x_ij` for a nonedge). The unsymmetrized encoding therefore
has exactly `126 * 757 = 95,382` clauses.

To qualify as a proof, research must save the deterministic generator and full
CNF, obtain a full DRUP/RUP refutation ending in the empty clause, and replay
every proof addition with a separately implemented unit-propagation checker
that also parses deletions. A solver's `UNSAT` response, the intake counts, or
the expected hashes quoted in `source.md` is not a certificate. The installed
Python environment has Python-SAT 1.8.dev24 with proof-capable Glucose and
Lingeling bindings, and a nontrivial four-clause UNSAT smoke test returned
proofs ending in `0`; this makes the first certificate attempt bounded and
locally executable.
