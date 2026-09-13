# Search log

All dates below are 2026-08-29 (Asia/Shanghai). Queries were run before the
decisive \(n=8\) computation. “No hit” is database- and query-bounded.

## Primary source and metadata

- EJC article page:
  `https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i1p40`.
  Verified authors, title, DOI `10.37236/4805`, volume 23, issue 1, article
  P1.40, and publication date 2016-03-04.
- Published PDF:
  `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p40/pdf`.
  Checked Sections 2.1, 2.3, 2.4, 3, and 7.3. Conjecture 7.6 and the reported
  \(n\leq7\) verification occur in Section 7.3.
- Crossref REST query: `https://api.crossref.org/works/10.37236/4805`.
  Metadata agreed with the journal page; Crossref reported four citing works.
- arXiv abstract/API/PDF: `https://arxiv.org/abs/1409.6659` and
  `https://export.arxiv.org/api/query?id_list=1409.6659`. The current record is
  v2, last revised 2015-08-23. The downloaded latest PDF's response filename was
  `1409.6659v2.pdf`; local SHA-256 is
  `0f77206e9db970f570ae6b7e149fb33293aef243252f386069eded4a7720a90d`.
  The “March 22, 2026” date in the experimental HTML rendering is not a
  submission-history event and was rejected as revision evidence.

## Frozen novelty queries

Web queries:

1. `"K-Knuth Equivalence for Increasing Tableaux" Conjecture 7.6 DOI`
2. `"K-Knuth" "Conjecture 7.6"`
3. `site:arxiv.org K-Knuth equivalence increasing tableaux`
4. `site:github.com K-Knuth increasing tableaux code`
5. `"every shape in the interval" "K-Knuth"`
6. `"shapes in a K-Knuth" interval`
7. `"Conjecture 7.6" tableaux`
8. `"K-Knuth equivalence classes" shapes`
9. `"10.37236/4805" K-Knuth 2024 2025 2026`
10. `"K-Knuth Equivalence for Increasing Tableaux" 2025`
11. `"K-Knuth Equivalence for Increasing Tableaux" 2026`
12. `"shape-interval" K-Knuth`

Results: exact-phrase hits for Conjecture 7.6 were copies/indexing of the 2016
paper. No later solution or counterexample was found by these queries.

## Citation-graph audit

- OpenAlex work `W1616805010` reported 16 citing records (including duplicate
  repository/arXiv versions). The snapshots are saved as
  `literature/openalex_original.json` and `literature/openalex_citing.json`.
- Semantic Scholar `CorpusId:13469516` reported 22 citing records. Its snapshot
  is `literature/semantic_scholar_original.json`.
- Searchable full text was downloaded for these 14 citing arXiv works:
  `1603.08490`, `1611.00216`, `1611.02545`, `1702.01358`, `1807.03294`,
  `1810.00148`, `1907.11415`, `1911.07799`, `2002.04810`, `2103.09551`,
  `2106.13922`, `2204.05259`, `2211.02993`, and `2408.16211`.
  Searches for `Conjecture 7.6`, `shape ... interval`, `interval ... shape`,
  `Shapes of Tableaux`, and the reported \(n\leq7\) phrase found no discussion
  of the target conjecture.
- Limitation: citation indices are incomplete and some non-arXiv citing works
  were inspected only through metadata/search snippets. Therefore the novelty
  conclusion is a bounded “not found,” not a universal absence proof.

## Public code audit

- OEIS A261601 links Ka Yu Tam's source
  `https://oeis.org/A261601/a261601.py.txt`, saved locally as
  `literature/a261601_original.py`.
- The code is Python 2, enumerates all increasing tableaux on \([n]\), creates
  Hecke-insertion transitions, and implements the primitive-pair/queue closure
  of paper Algorithm 1. It reports the table values through \(n=7\).
- This historical code is provenance only. The new independent verifier must
  neither import it nor trust discovery aggregates.

## Theorem frontier after Gate 1

- Exact published general endpoint: Conjecture 7.6 remains a conjecture in the
  source.
- Last author-reported finite endpoint: all classes on \([n]\), \(n\leq7\).
- First finite endpoint not reported there: \(n=8\).
- Nearby proved facts used structurally: Algorithm 1/Theorem 3.1,
  order-preserving standardization, and outer-hook invariance.
- No stronger later theorem or public \(n=8\) certificate was found in the
  recorded Gate 1 scope.

## Frozen-result novelty pass (Gate 1 pass 2)

After the theorem statement, implementation, and exact totals had been frozen,
a second search was run on 2026-08-29.  It used the following result-specific
queries, which could not have been used before the computation:

1. `"6,773,991" K-Knuth`
2. `"988,384" K-Knuth tableaux`
3. `"215,295" K-Knuth URT`
4. `"9,069,306" increasing tableaux`
5. `"Conjecture 7.6" "n=8" K-Knuth`
6. `"K-Knuth" "shape set" "Young lattice"`
7. `"K-Knuth" interval complete tableaux`
8. `site:github.com "K-Knuth" "n=8" tableaux`

The numerical queries returned either no result or unrelated occurrences of
the integers.  The phrase queries returned the 2016 source paper and later
works using K-Knuth equivalence, but no public proof, counterexample, or
independently stated \(n=8\) certification of Conjecture 7.6.  OEIS A261601 was
checked again and still lists only
`1, 1, 3, 13, 79, 620, 6036, 70963`, ending at \(n=7\); its linked program is
the already archived historical implementation.

**Pass-2 decision:** the bounded novelty lock remains `PASS`.  This permits the
manuscript to say that no earlier public \(n=8\) result was found in the
recorded search scope.  It does not justify an assertion about unpublished,
private, or unindexed work.
