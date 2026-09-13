# Search log

## NOVELTY_LOCK pass 1: frozen claim list

Date: 2026-08-29 (Asia/Shanghai).  Before any search, claims C01--C06 in
`claim_ledger.md` were frozen.  Planned evidence priority: original paper;
publisher/DOI metadata; arXiv author version if any; MathDB only as an index;
forward citations and exact-title/formula searches for subsequent work.

The absence of a hit will be recorded only as absence in the named databases
and queries, never as a proof of novelty.

## NOVELTY_LOCK pass 2: first evidence search

Date: 2026-08-29.  Sources opened:

- Adam W. Marcus, arXiv:2108.02528v2, especially Theorem 9 and Conjecture 10:
  <https://arxiv.org/pdf/2108.02528>.
- Publisher record and Crossmark metadata:
  <https://doi.org/10.1080/00029890.2022.2115803>.
- MathDB problem record:
  <https://mathdb.com/p/351542/permanent-inequality-for-rank-at-most-two-matrices>.
- Author-hosted older 2016 preprint, used only to trace version history:
  <https://web.math.princeton.edu/~amarcus/papers/rank2perms.pdf>.

Recorded web queries (verbatim or minimally normalised):

1. `"permanent inequality" "rank at most two" Marcus`
2. `"rank at most two matrices" permanent Marcus`
3. `site:doi.org Marcus permanent rank two inequality`
4. `site:arxiv.org permanent rank two Marcus inequality`
5. `"A Determinantal Identity for the Permanent of a Rank 2 Matrix"`
6. `"Conjecture 10" permanent "rank at most 2"`
7. `"A proof is known in the case that the entries of T are all positive" permanent`
8. `"10.1080/00029890.2022.2115803" -tandfonline`
9. `"2108.02528" permanent inequality`
10. `"Permanent inequality for rank-at-most-two matrices" -MathDB`
11. `"rank-two permanent inequality"`

Findings: the original exact formula and real setting were verified; the
publisher page identified the 2022 journal version and displayed zero Crossref
citations at search time; MathDB labelled the conjecture open and recorded no
progress.  Exact-title/DOI/formula searches did not return a later proof,
counterexample, or an `n=3`/`n=4` theorem.  This is a bounded search finding,
not a proof that no such work exists.  A second novelty search after the exact
endpoint is frozen remains mandatory.

## NOVELTY_LOCK pass 3: frozen-result search

Date: 2026-08-29.  The exact result was frozen before this pass:

> Every real `3 x 3` matrix of rank at most two satisfies the Marcus block
> permanent inequality with coefficient 20.  Equality holds exactly for
> rank at most one, a zero row/column, or (in rank two) a permuted `2 x 2`
> all-zero submatrix.

Endpoint-specific queries:

1. `"20" "per(T)^2" "rank" permanent 3`
2. `"3 x 3" "rank at most 2" permanent inequality`
3. `"3×3" "rank 2" "permanent" inequality Marcus`
4. `"rank-two" "per([[T,T],[T,T]])"`
5. `"A Determinantal Identity for the Permanent of a Rank 2 Matrix"`
6. `"10.1080/00029890.2022.2115803" -tandfonline`
7. `"2108.02528" permanent inequality`

Equivalent-structure queries:

8. `"[f^2,g^2]" "[f,g]" binary forms inequality`
9. `"binary cubic" apolar "sum of squares" real rooted inequality`
10. `"apolar" "real-rooted" binary forms inequality permanent`
11. `"Bombieri inner product" real rooted polynomials product inequality`

The exact endpoint queries returned the MathDB open-conjecture record but no
order-three theorem, counterexample, or equality classification.  The broader
queries found literature on Bombieri/apolar product inequalities, including
Aldaz--Bravo--Render (arXiv:2403.10584), but inspection of the returned
statements found no theorem equivalent to the frozen contraction inequality
for two split real cubics.  The publisher record continued to display zero
Crossref citations, and MathDB continued to display `Conjecture open` with no
progress summary.

Conclusion of the lock: no prior occurrence of the frozen result was found in
the named sources and queries.  This supports a novelty claim limited to the
recorded search.  It does not prove nonexistence in unindexed literature.

## NOVELTY_LOCK pass 4: post-timeout recovery audit

Date: 2026-08-29.  Trigger: the user reported consecutive service timeouts and
asked to restart at Gate 1.  The local Gate 1 artifacts and frozen endpoint
were already present, so this pass revalidated them without overwriting the
earlier provenance.

Primary/current records reopened:

- arXiv metadata and v2 HTML for Adam W. Marcus,
  <https://arxiv.org/abs/2108.02528> and
  <https://arxiv.org/html/2108.02528v2>;
- MathDB problem record,
  <https://mathdb.com/p/351542/permanent-inequality-for-rank-at-most-two-matrices>;
- Crossref's DOI metadata service/documentation for the already audited
  journal DOI `10.1080/00029890.2022.2115803`.

Recovery queries:

1. `site:arxiv.org 2108.02528 Marcus "A Determinantal Identity for the Permanent of a Rank 2 Matrix"`
2. `site:doi.org/10.1080/00029890.2022.2115803 Marcus permanent rank 2`
3. `site:mathdb.com/p/351542 permanent inequality rank at most two matrices`
4. `"3 x 3" "rank at most two" Marcus permanent inequality`
5. `"The Rank-Two Marcus Permanent Inequality for Real 3"`
6. `"rank-two Marcus" permanent "order three"`

The arXiv record still identifies v2 (10 August 2021), Adam W. Marcus, and
the same title.  Its HTML states Theorem 9 over `R^(n x n)`, then gives the
displayed inequality as Conjecture 10 and describes the positive-entry case
only as an author report.  MathDB currently shows zero posted solutions and
no progress summary.  The exact result-title and order-three queries returned
no independently indexed prior theorem.  As before, the absence conclusion
is bounded by the named sources and queries; it is not proof about unindexed
literature.

## NOVELTY_LOCK pass 5: final result-specific second audit

Date: 2026-08-29.  Full record: `literature/novelty_recheck_n3.md`.

This pass froze both the exact matrix theorem/equality classification and the
equivalent split-real binary-cubic inequality
`[f^2,g^2]_6 <= [f,g]_3^2`.  It recorded 19 matrix-language queries, 24
binary/apolar queries, official arXiv API searches, Crossref top-ten screens,
MathDB, and forward-citation checks.

No prior occurrence of the frozen theorem or iff equality set was found in
that recorded scope.  Crossref and the publisher displayed zero Crossref
citations, but OpenAlex and Semantic Scholar clustered one citing work by
Tran.  Full-text inspection showed that it concerns the Soules
permanent-on-top conjecture and an older Marcus draft, not Conjecture 10, the
duplicated-block coefficient 20 theorem, or the `n=3` equality set.

The certified wording is only: “No prior occurrence was found in the dated
databases and queries recorded here.”  Global novelty, first-proof, and
previously-unknown claims remain uncertified.
