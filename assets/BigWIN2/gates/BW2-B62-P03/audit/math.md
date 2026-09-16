# Fresh mathematical referee report

## Frozen scope and snapshot

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`82296f8e26c9200dd61b008dd03dcdcb47a682c38b5652dbbf3e1ffa5a97eaab`.
Before assessing the mathematics, I recomputed the SHA-256 digest of every
snapshot-listed file; all digests agreed with `audit/snapshot.json`. The claim
is full-scope: it gives both requested quantities for every
\(n\in\{6,7,8\}\), not a restricted or quotient version of the graph.

## Reconstruction of the decisive argument

Every full cycle has a unique word \((1,a_2,\ldots,a_n)\), with the tail a
permutation of \(2,\ldots,n\). Thus verifier A's enumeration has exactly
\((n-1)!\) vertices. Relabeling every occurrence of \(i\) and \(i+1\) in such
a word, then rotating the result back to start at 1, is exactly the cycle-word
form of \(s_i c s_i\). The implementation uses precisely
\(i=1,\ldots,n-1\), never the cyclic transposition \((n,1)\), and it does not
identify reversal.

Verifier B uses a distinct representation. It enumerates all one-line maps in
\(S_n\), retaining a map exactly when the orbit of label 1 first returns after
\(n\) steps. For a permutation this is equivalent to being one \(n\)-cycle.
It constructs each edge literally as the map composition
\(s_i\circ p\circ s_i\), without using A's cycle-word edge routine. Both
programs verify nonloops, distinct generator-neighbors, involutivity under the
same generator, connectivity, and the following counts:

| \(n\) | vertices | degree | undirected edges |
|---:|---:|---:|---:|
| 6 | 120 | 5 | 300 |
| 7 | 720 | 6 | 2,160 |
| 8 | 5,040 | 7 | 17,640 |

Each program runs unweighted BFS from every vertex. Consequently every entry
of the ordered distance matrix is computed, so the maximum of the canonical
root row is \(\operatorname{Sort}_n\), while the maximum over all rows is the
diameter. This correctly avoids the invalid inference that a single rooted BFS
would determine the diameter. The resulting exact extrema are

| \(n\) | \(\operatorname{Sort}_n\) | \(D_n\) |
|---:|---:|---:|
| 6 | 6 | 7 |
| 7 | 10 | 10 |
| 8 | 13 | 14 |

The all-ordered-pairs histograms sum respectively to
\(120^2,720^2,5040^2\); their distance-one entries are twice the respective
edge counts, and their last nonzero levels occur at 7, 10, and 14. The rooted
histograms sum to the respective vertex counts and have last nonzero levels at
6, 10, and 13. A and B agree on every histogram entry and on SHA-256 hashes of
the canonical vertex stream, undirected edge stream, and entire ordered
distance-row stream.

## Fresh recomputation and witness attacks

I wrote `audit/referee_check.py` without importing or invoking either submitted
verifier. It independently builds successor maps, forms every neighbor by the
literal formula \(q(x)=s_i(p(s_i(x)))\), stores the graph as a SciPy CSR matrix,
and delegates all-pairs unweighted shortest paths to SciPy's sparse graph
engine. With CPython 3.10.12, NumPy 2.2.6, and SciPy 1.15.3, it independently
reproduced all vertex and edge counts, every rooted and ordered-pair histogram
entry, and all six extrema. Its ordered-distance-row hashes are exactly

- \(n=6\): `526c7ef0cd53c0d83e42e0f63249f7496b9c030d1109dfa683ac21303245b1f7`;
- \(n=7\): `c62e059528260bca71a36fa5a0ba4e118850e03378cc5a9dd8b6b6a6b669a081`;
- \(n=8\): `4c1bc1c3e6aeeff3e22198a39dd09fe86841484c08ad5ef8183410ac26073fb6`.

These are identical to both submitted computations. The fresh checker also
parsed and replayed the sorting and diameter paths in all six submitted JSON
records. For A's cycle-word paths and both B's cycle-word and one-line-map
serializations, every generator lies in \(1,\ldots,n-1\), every displayed
transition equals the claimed conjugation, each vertex/generator length is
consistent, and the displayed length equals the independently computed
endpoint distance. In particular the claim's selected sorting witnesses have
distances 6, 10, and 13, and its selected diameter pairs have distances 7, 10,
and 14. Thus the displayed paths give the required lower witnesses, while the
all-source searches give the matching global upper bounds.

I additionally checked the usual scope traps: ordered pairs include diagonal
distance zero; all canonical full cycles occur; inverse cycles and reversals
are not quotiented; duplicate edges cannot alter BFS distances; and no
asymptotic or unimodality conclusion is inferred from these finite runs. There
are no limiting, compactness, division, or degenerate-domain steps in this
finite exact argument.

## Source comparison and contribution

The supplied primary-source PDF has the frozen SHA-256 digest and its
Definitions 1.1 and 1.3 agree with the graph and sorting conventions used here.
Remark 3.1 identifies the same graph with the stated Schreier graph and explains
the canonical-root distance formula. The introduction records
\(D_5=5>4=\operatorname{Sort}_5\). Section 7, equation (7.1), states that the
proposed formula for \(\operatorname{Sort}_n\) was computationally verified for
all \(n\le 12\); using the paper's explicit \(k_t\) formulas yields 6, 10, and
13 for the three sorting values. Therefore those sorting values are a
reproduction, as the candidate honestly says. The cited paper gives general
bounds but does not tabulate \(D_6,D_7,D_8\). The candidate makes no priority
claim for the diameter values. Its contribution is the exact full finite
resolution requested in `source.md`, including the diameter values and a
replayable dual-verifier certificate. This review does not assert priority or
journal acceptance.

## Verdict

**Accept.** The exact frozen claim is correct in its full stated scope, the
computational exhaustion and witnesses are independently reproducible, and the
contribution is described honestly. I found no unresolved mathematical gap in
the frozen finite problem.
