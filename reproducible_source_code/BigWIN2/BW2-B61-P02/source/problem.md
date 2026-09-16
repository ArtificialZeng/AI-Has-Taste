# Precise reading of the frozen problem

The immutable wording is in `source.md`. The interpretation below fixes notation and
certificate requirements; it does not replace or weaken that wording.

## Objects, labels, and quantifiers

For each integer `n` with `0 <= n <= 6`, fix the labelled vertex set
`V_n={1,...,n}` (with `V_0` empty). A graph is finite, simple, undirected, and has
vertex set exactly `V_n`. The literal reading includes the null graph at `n=0`; if a
convention excludes it, only that one trivial positive class is removed. For `n=0`
the empty coloring exists and the Hall inequalities are vacuous.

For a fixed graph `G` on `V_n`, define the graphic list

`L_G(v)=N_G(v)={c in V_n : vc is an edge of G}`.

For every graph `H` on the same *labelled* set `V_n`, a proper `G`-coloring of `H`
is a map `phi:V_n -> V_n` such that

1. `phi(v) in N_G(v)` for every `v`; and
2. `phi(u) != phi(v)` for every edge `uv` of `H`.

Repeated colors are allowed only on independent sets of `H`. In particular, because
`G` is simple, a vertex cannot color itself.

For `U subseteq V_n` and a color `c in V_n`, set

`alpha_{H,G}(U,c) = alpha(H[U intersect N_G(c)])`,

where `alpha` is the independence number and `alpha(empty)=0`. This equals the
maximum size of an independent set in `H[U]` all of whose vertices have `c` in
their graphic list. The Hilton--Johnson Hall condition for `(H,G)` is

`|U| <= sum_{c in V_n} alpha_{H,G}(U,c)`

for every `U subseteq V_n`. It is equivalent to check every nonempty `U` for which
the induced subgraph `H[U]` is connected (and is also equivalent to the source's
formulation for every subgraph).

The graph `G` is **Hall-universal** precisely when

`for every labelled H on V_n, [Hall(H,G) implies H has a proper G-coloring]`.

Although `H` ranges over labelled graphs, Hall-universality is invariant under a
simultaneous permutation of the common vertex set. Therefore `G` is to be reported
up to ordinary graph isomorphism. The standard expected numbers of `G`-classes for
`n=0,...,6` are `1,1,2,4,11,34,156` (209 total); the enumerator must independently
check its generated class counts rather than take this sequence as a certificate.

## Required census and certificates

For each isomorphism class of `G`:

- If `G` is not Hall-universal, give one explicitly labelled graph `H`. For every
  nonempty connected induced `H[U]`, record the exact independence-number summands
  above (or equivalent exact data) proving Hall's condition. Give a complete
  checkable certificate that no map in `product_{v in V_n} N_G(v)` properly colors
  `H`; an exhaustive assignment trace or a proof-producing SAT certificate is
  acceptable.
- If `G` is Hall-universal, give a reproducible exact exhaustive certificate over
  every one of the `2^(n choose 2)` labelled graphs `H`. Counts alone are
  insufficient: retain canonical encodings, code/version information, and hashes
  binding the per-`H` Hall and colorability results.
- Mark positive classes already implied by a theorem in the primary source and
  identify the first positive class, in an explicitly stated census ordering, not
  covered by those source families. “First” has no meaning until the ordering is
  fixed; use `(n, graph6)` lexicographic order unless the research artifact specifies
  another reproducible canonical order.

All computation is exact. Floating-point output or an unhashed numerical count is
not a proof.

## Nearest prior results and source status

Primary source inspected on 2026-09-07:

- <https://arxiv.org/abs/2609.01889> and v1 PDF, especially the definition of the
  Hilton--Johnson condition (PDF pp. 2--4), Definition 4.1 and Proposition 4.2
  (PDF p. 13), Theorems 4.6, 4.11, 4.16, and 4.19 (PDF pp. 14--20), and Conclusion
  Question 1 (PDF p. 21).
- Definition 4.1 is exactly the quantified property above. Proposition 4.2 reduces
  it to equality of edge-maximal Hall-feasible and colorable graphs.
- Proposition 2.10 makes every `G` with an isolated vertex vacuously
  Hall-universal, since then no pair `(H,G)` satisfies Hall's condition.
- Theorem 4.6 covers every `G` with a spanning `{1,2}`-factor (the totally
  Hall-universal graphs); Theorem 4.11 covers all forests; Proposition 4.9 covers a
  star-attachment construction; Theorem 4.16 classifies complete multipartite
  graphs; and Theorem 4.19 covers grids.
- The conclusion asks for the general characterization of Hall-universal graphs,
  but the paper does not give the requested finite census.

Exact-phrase searches on 2026-09-07 for `"Hall-universal" graph census six
vertices`, `"Hall-universal graphs" "at most six"`, `"graphic list coloring"
census graph`, and the arXiv domain returned the primary source but no separate
primary paper containing this census. This is only a limited literature screen, not
a priority or novelty proof. Source status is **new-question/status-uncertain**: the
finite refinement is well-defined and adjacent to an explicitly open broader
characterization, but has not been established as absent from all literature.

## Recorded source discrepancy (no silent correction)

`source.md` attributes arXiv:2609.01889v1 to Timothy Sun. The official arXiv abstract
and v1 PDF retrieved on 2026-09-07 instead list **Parikshit Chalise** as the author.
The theorem numbering and mathematical content cited in `source.md` do match the
retrieved paper. During the research pass the local PDF named by `source.md` was found
at `/home/ailab/4math-open-problems/batches/inbox/bigWin-61-materials/2609.01889.pdf`;
its SHA-256 is exactly the stated
`9920b04ae0db29b5568f063ef9d61d80d267c8e721e0b0d31e63ed87b393efc8`.
A project-local evidence copy is at `evidence/external/2609.01889.pdf`. The immutable
source has not been edited.

## Admitted target

Nearest prior result: the source families and maximality criterion above. Proposed
delta: the complete, exact isomorphism-class census through six vertices, with
witnesses and exhaustive certificates. Verification route: canonical unlabeled
generation for `G`, full labelled enumeration for `H`, exact bitset computation of
all Hall inequalities, exact coloring backtracking/SAT, and an independently
implemented verifier for emitted witnesses and hashes. This is finite and plausibly
tractable: at `n=6`, only `156 * 2^15 = 5,111,808` `(G,H)` pairs occur before
symmetry reductions.
