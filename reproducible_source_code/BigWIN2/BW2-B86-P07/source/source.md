# Frozen source problem: exact H-exact extremal value for the five-vertex subdivided claw

Canonical id: win-00086-p07
Frozen on: 2026-09-10 (Asia/Shanghai)
Batch source: `batches/inbox/bigWin-86.raw.md`, item 7 (preserved verbatim there)
Primary source:
- Yair Caro, Zsolt Tuza, and Mariusz Zarb, *Induced/Incomparable versus Ramsey*, arXiv:2605.22077v2. See the definition on PDF p.2, Fact 2.1 on p.4, Theorem 5.1 on p.14, Theorem 6.1 on p.15, and Section 7, Problem 1 on p.24.

## Definitions

Let `T*` be the five-vertex subdivided claw

```
V(T*) = {c,a,b,d,e},
E(T*) = {ca,cb,cd,de}.
```

Two five-vertex graphs `F,H` are *comparable* when one contains the other as an ordinary, not necessarily induced, subgraph. A graph `G` is `H`-exact when, for every five-vertex subset `U` of `V(G)`, either `G[U]` is isomorphic to `H` or `G[U]` is incomparable with `H`. Define

```
f(H) = max{|V(G)| : G is H-exact}.
```

## Statement

Determine `f(T*)` exactly. The proposed target is

```
f(T*) = 8.
```

The primary source supplies the current bounds `8 <= f(T*) <= 16` and asks for the exact value for every tree. The lower bound is prior art; the proposed new contribution is the nine-vertex nonexistence theorem giving `f(T*) <= 8`.

## Required proof certificate

1. Verify directly that `2 K_4` is `T*`-exact, while identifying this as the source's known lower-bound mechanism rather than a new result.
2. Give a complete, deterministic encoding for nine-vertex graphs using the 36 edge variables. For each of the 126 five-vertex vertex sets, forbid every labeled five-vertex graph that is comparable with but not isomorphic to `T*`.
3. Independently reconstruct and verify the exact finite counts: 60 labeled copies of `T*`, 757 forbidden labeled graphs, and `126*757 = 95,382` clauses, each involving the ten edges of one five-set.
4. Produce the complete CNF and a complete DRUP/RUP proof ending in the empty clause. Check every proof addition by an independently implemented unit-propagation verifier, handle deletions explicitly, and record formats, versions, deterministic ordering, and SHA-256 digests.
5. Invoke the hereditary observation from Fact 2.1 only after the nine-vertex certificate is verified: if no nine-vertex `T*`-exact graph exists, no larger one exists.

An independent intake reconstruction obtained the following expected digests, which are test oracles rather than substitutes for files:

```
CNF  70b78d1ae0f25858dd024eda62addf5f7d623a410725026e7a37200bb79f8cc4
DRUP cdfb10845b6fc6c282095187e9f1af6ec2f02456bbfb32d04cacadfaaeadb760
```

The research pass must regenerate and save the generator, CNF, proof, checker, and replay log inside the project. A solver's `UNSAT` line or either hash without its full corresponding file is not a certificate.

## Scope and contribution boundary

This project concerns only the fixed five-vertex tree `T*`. It must not be presented as determining `f(T)` for every tree. The source's general bounds, star cases, path cases, and the eight-vertex lower bound are prior results.

Before asserting novelty, check the latest version of arXiv:2605.22077 and later literature for this exact tree or an equivalent formulation. Any manuscript must cite the primary source, any SAT/proof-system methods actually used, and directly relevant prior work. It must additionally include one or two genuinely relevant papers from the user's Excel library when available; that is a minimum, not a bibliography cap, and unrelated entries must never be padding.

This file is immutable. Changing ordinary-subgraph comparability to induced-subgraph comparability, or checking only selected five-subsets, changes the problem.
