# Immutable source: win-00062-p03

## Frozen problem

For `n>=2`, let `C_n` be the set of full `n`-cycles in `S_n`. Let `Gamma_n` be the undirected graph with vertex set `C_n`, with an edge between `c` and `s_i c s_i` for every adjacent transposition `s_i=(i,i+1)`, omitting loops in the usual graph-distance convention. Thus `|C_n|=(n-1)!`.

Use Definitions 1.1 and 1.3 of arXiv:2601.12597v2 and determine, for each `n in {6,7,8}`, the exact pair

`D_n = diameter(Gamma_n)`

and

`Sort_n = max_{c in C_n} dist_Gamma_n(c,(1 2 ... n))`.

Return every distance value as an exact integer, at least one farthest ordered pair for `D_n`, at least one farthest cycle for `Sort_n`, and explicit shortest conjugation paths witnessing the upper distance values for those representatives. A complete proof must also certify that no larger distance exists by exhaustive BFS (or an equivalent exact graph argument) over every one of the `(n-1)!` vertices.

Use two independently written encodings or verifiers. Record the canonical representation of cycles, adjacency convention, vertex and edge counts, full distance histograms, deterministic hashes, language/library versions, and replay commands. An isolated path only proves a lower bound; a BFS from the canonical cycle only computes `Sort_n`, not the diameter, unless an additional valid symmetry theorem is proved.

Do not claim that these finite values prove either asymptotic Conjecture 7.1 or unimodality Conjecture 7.2.

## Primary source

- Ron M. Adin, Eli Bagno, and Yuval Roichman, *Conjugating full cycles by adjacent transpositions: diameter and sorting time*, arXiv:2601.12597v2, Definitions 1.1 and 1.3, Problems 1.2 and 1.4, and §7.
- URL: https://arxiv.org/abs/2601.12597
- Local evidence: `batches/inbox/bigWin-62-materials/2601.12597.pdf`
- PDF SHA-256: `de5de1f1ddaec97f2f0bc784107c8f9fb27787242e459cd5b3387b34dfc3aa9b`.

The source records `D_5=5>4=Sort_5` and general bounds. Whether the requested larger small-order values are already tabulated elsewhere remains subject to literature audit.

