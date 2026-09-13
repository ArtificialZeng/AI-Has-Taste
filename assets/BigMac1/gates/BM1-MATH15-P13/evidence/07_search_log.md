# Search log

Search date: 2026-08-28 (Asia/Shanghai).

## Frozen claims

The first pass froze L01--L07 in `claim_ledger.md` before broad mathematical
search.  In particular, “still open” is treated as a bounded bibliographic
claim rather than something that can be proved from an empty search result.

## Queries and repositories

- KAM 2025 problem collection: exact source downloaded to
  `literature/sources/kam_problem_collection_2025.pdf`; Problem 14 is on
  pp. 28--29.
- Exact web phrases: `"What is the small Ramsey degree of the edge"`,
  `"Are the induced chordal graphs edge-Ramsey"`, and
  `"induced linearly-ordered chordal graphs" Ramsey`.  Only the KAM problem
  collection was returned as a solution-relevant hit.
- Broader searches: `chordal graphs Ramsey degree`, `structural Ramsey theorem
  chordal graphs clique trees`, `Hubička Nešetřil chordal graphs Ramsey`, and
  2026 variants.  No paper claiming the edge degree was located.
- arXiv:2312.01466v2, *Indivisibility for Classes of Graphs*, downloaded as
  `literature/sources/guingona_et_al_indivisibility.pdf`.  Proposition 4.13 is
  vertex indivisibility for chordal graphs; it is not an edge theorem.

## Negative-search limitation

The searches above do not exclude an unpublished manuscript, a result under
different terminology, or a paper not indexed by the queried services.  A
later pass must inspect citation records and primary metadata for every source
used in a manuscript.

## Restricted split-graph novelty pass

Queries run on 2026-08-28 included:

- `"small Ramsey degree" split graphs edge`;
- `"Ramsey degree" "split graph" induced`;
- `"ordered split graphs" Ramsey property induced`;
- `edge Ramsey degree split graphs structural Ramsey`;
- `"split graphs" "small Ramsey"`;
- `"split graph" "Ramsey degrees"`;
- `"ordered split graph" "Ramsey class"`;
- `"split graphs" "Ramsey lift"`.

An arXiv API exact conjunction for `"small Ramsey degree"` and `"split
graph"` returned zero entries; a second conjunction for `"ordered split
graphs"` and `Ramsey` also returned zero entries.  The raw responses are saved
as `literature/arxiv_query_small_ramsey_split.xml` and
`literature/arxiv_query_ordered_split_ramsey.xml`.

Crossref bibliographic searches returned papers on classical graph Ramsey
numbers, anti-Ramsey numbers, ordered Ramsey numbers, and generalized split
graphs, but no structural small-Ramsey-degree computation for ordered split
graphs.  Raw responses are saved as
`literature/crossref_query_small_ramsey_split.json` and
`literature/crossref_query_ordered_split_ramsey.json`.

The source theorem for the upper bound was checked directly in
Hubička--Nešetřil, arXiv:1606.07979v4: Corollary 4.2 is the ordered
free-amalgamation Ramsey theorem, and the paragraph before Corollary 4.6
explicitly treats bipartite graphs with one part named by a unary relation.
Publisher metadata and DOI 10.1016/j.aim.2019.106791 are confirmed by the
arXiv related-DOI record.

Conclusion: no prior explicit statement of the exact value 3 was located in
the recorded search space.  This is bounded novelty evidence, not proof of
global priority.
