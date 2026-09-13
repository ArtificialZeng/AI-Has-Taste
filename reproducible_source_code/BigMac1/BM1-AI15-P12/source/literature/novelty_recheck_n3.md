# Result-specific novelty recheck for the real order-three theorem

## Scope and frozen endpoint

Search date: **2026-08-29** (Asia/Shanghai).  This is a fresh, result-specific
second novelty audit.  The endpoint was frozen before the searches below:

> For every `T in R^(3 x 3)` with `rank(T) <= 2`,
> \[
> \operatorname{per}\!\begin{pmatrix}T&T\\T&T\end{pmatrix}
> \le 20\operatorname{per}(T)^2.
> \]
> Equality holds if and only if at least one of the following holds: (i)
> `rank(T) <= 1`; (ii) `T` has a zero row or a zero column; (iii) `T` has
> rank two and can be independently row- and column-permuted to contain a
> `2 x 2` all-zero submatrix.  The conditions may overlap, and
> `per(T) = 0` is not excluded.

The exact binary-form formulation was also frozen.  If

\[
 f(X,Y)=\sum_{k=0}^3 f_kX^{3-k}Y^k,\qquad
 g(X,Y)=\sum_{k=0}^3 g_kX^{3-k}Y^k
\]

are products of three real homogeneous linear factors (a zero factor is
allowed), set

\[
 [f,g]_d=\sum_{k=0}^d\frac{f_kg_k}{\binom dk}.
\]

The matrix theorem is equivalent to the split-real binary-cubic contraction
inequality

\[
 [f^2,g^2]_6\le [f,g]_3^2.
\]

This is a bilinear Bombieri/Weyl/apolar coefficient contraction, not the usual
norm inequality for a product of polynomials.  Searches therefore included
both the matrix language and the binary-cubic/apolar language.

## Source baseline

1. Adam W. Marcus, [arXiv:2108.02528v2](https://arxiv.org/abs/2108.02528v2),
   *A Determinantal Identity for the Permanent of a Rank 2 Matrix*.  The
   current arXiv record says v1 was submitted 5 August 2021 and v2 was
   submitted 10 August 2021.  The full text states the duplicated-block
   inequality as Conjecture 10.  It does not state an order-three theorem or
   an equality classification.  The sentence after the conjecture reports
   the positive-entry case as known but supplies no separate proof citation;
   this remains an author report rather than an independently verified
   borrowed theorem.
2. The journal version is the *American Mathematical Monthly* 129(10)
   (2022), 962--971,
   [DOI 10.1080/00029890.2022.2115803](https://doi.org/10.1080/00029890.2022.2115803).
   The [Crossref record](https://api.crossref.org/works/10.1080%2F00029890.2022.2115803)
   returned `is-referenced-by-count = 0` during this audit; the publisher page
   likewise displayed `0 CrossRef citations to date`.  This field is not a
   complete citation census; see the forward-citation cross-check below.
3. The [MathDB problem record](https://mathdb.com/p/351542/permanent-inequality-for-rank-at-most-two-matrices)
   reproduced the all-order conjecture, displayed no progress summary, and
   displayed `Solutions 0` when opened on the audit date.  MathDB is a
   secondary/community record, so this is page-state evidence only.

## Exact searches

The following general-web queries were issued verbatim (quotation marks are
part of the query where shown):

1. `"every real 3 x 3 matrix" "rank at most two" permanent`
2. `"3 x 3" "rank at most 2" "permanent" inequality Marcus`
3. `"3×3" "rank 2" permanent inequality Marcus`
4. `"coefficient 20" "permanent" "rank" matrix`
5. `"A Determinantal Identity for the Permanent of a Rank 2 Matrix" proof Conjecture 10`
6. `"Conjecture 10" "rank at most 2" permanent`
7. `"2108.02528" permanent conjecture proof`
8. `"10.1080/00029890.2022.2115803" permanent`
9. `"The Rank-Two Marcus Permanent Inequality for Real"`
10. `"Marcus Permanent Inequality" "order three"`
11. `"Marcus permanent" "3 x 3"`
12. `"Marcus inequality" "rank-two" permanent matrix`
13. `"2g_1^2+g_1g_2+2g_2^2"`
14. `"2 x 2 zero block" "permanent" rank two`
15. `"zero row or column" "permanent" "rank two" equality`
16. `"rank-two" permanent "equality" "zero block"`
17. `"A Determinantal Identity for the Permanent of a Rank 2 Matrix" cited by`
18. `"2108.02528" "3 x 3" permanent`
19. `site:zbmath.org "10.1080/00029890.2022.2115803"`

These searches found the Marcus article, the MathDB entry, bibliographic
mirrors, and unrelated permanent problems, but no source stating the frozen
order-three inequality or its iff equality classification.

### arXiv API searches

The official arXiv export API was queried with `start=0`; at least the first
20 results were requested, and 50 were requested for the broader variants.
The exact `search_query` values and result counts were:

| `search_query` | total | audit finding |
|---|---:|---|
| `all:"rank two" AND all:permanent` | 1 | unrelated exterior-product/fermion paper |
| `all:Marcus AND all:permanent` | 9 | Marcus source plus papers using other senses of Marcus/permanent; no order-three theorem |
| `all:"rank at most 2" AND all:permanent` | 0 | no result |
| `all:"rank at most two" AND all:permanent` | 1 | unrelated multipartite-entanglement paper |
| `all:"rank-2" AND all:permanent` | 2 | Marcus source plus unrelated fused-silica paper |
| `all:"rank-two" AND all:permanent` | 1 | unrelated exterior-product/fermion paper |
| `all:"binary cubic" AND all:apolar` | 0 | no result |
| `all:"binary cubic" AND all:inequality` | 0 | no result |
| `all:apolar AND all:"product of linear forms" AND all:inequality` | 0 | no result |
| `all:apolar AND all:real-rooted` | 1 | Brändén--Haglund--Visontai--Wagner, a different monotone-column permanent theorem |
| `all:"binary forms" AND all:apolar` | 8 | Waring-rank, invariant-theory, and apolar-ideal papers; no target inequality |
| `all:"Bombieri type" AND all:inequality` | 5 | norm/product or zero-packing inequalities, not the frozen bilinear square contraction |
| `all:"Fischer-Fock" AND all:real-rooted` | 0 | no result |

The recent arXiv item most closely connected by vocabulary was Thomas
Sinclair, [arXiv:2606.10870v2](https://arxiv.org/abs/2606.10870v2), *Finite
free convolution via reproducing kernels and squarefree algebras*.  Its text
uses the same binomially weighted apolar kernel and studies finite free
convolution, but a full-text search found neither the Marcus rank-two source
nor the frozen inequality, order-three result, or equality classification.

An arXiv API `all:` query searches arXiv metadata, not every formula inside
every PDF.  The general-web full-text/phrase searches above were retained to
partly compensate for this limitation.

### Crossref title and bibliographic searches

The Crossref REST endpoint `https://api.crossref.org/works` was queried with
`rows=10` and the following literal values:

- `query.title=The Rank-Two Marcus Permanent Inequality for Real 3x3 Matrices`
- `query.title=Marcus Permanent Inequality order three`
- `query.title=Duplicated-block permanent rank two matrix`
- `query.bibliographic=rank at most two permanent inequality`
- `query.bibliographic=rank two permanent matrix Marcus`
- `query.bibliographic=3 x 3 rank two permanent inequality`
- `query.bibliographic=binary cubic apolar inequality`
- `query.bibliographic=A Determinantal Identity for the Permanent of a Rank 2 Matrix Marcus`

Crossref's search is fuzzy and returned very large `total-results` values;
therefore only the requested top ten of each response were screened, and no
exhaustiveness claim is made.  No top-ten result was the frozen theorem.  The
closest false positives that were opened were:

- Thomas H. Pate, *The Best Lower Bound for the Permanent of a Correlation
  Matrix of Rank Two*, DOI
  [10.1080/0308108031000081304](https://doi.org/10.1080/0308108031000081304):
  a lower-bound problem for rank-two correlation matrices, not the duplicated
  block inequality for arbitrary signed real matrices.
- Vehbi E. Paksoy, *A permanent inequality for positive semidefinite
  matrices*, DOI
  [10.13001/ela.2023.7701](https://doi.org/10.13001/ela.2023.7701): an
  inequality involving a positive-semidefinite matrix and its leading
  submatrices, not the target.
- Yang Yu, *The Permanent Rank of a Matrix (Part Two)*, DOI
  [10.20944/preprints202603.0035.v1](https://doi.org/10.20944/preprints202603.0035.v1):
  `perrank` is defined as the largest size of a square submatrix having
  nonzero permanent; this is a different invariant.
- *Rank-Two Cases of the Order-Four Soules Permanent-on-Top Problem*, DOI
  [10.2139/ssrn.7362322](https://doi.org/10.2139/ssrn.7362322): a theorem on
  Schur-power matrices of positive-semidefinite matrices, not Marcus's
  duplicated-block conjecture.

## Forward-citation cross-check

The Crossref source record and publisher page displayed zero Crossref
citations.  A supplemental OpenAlex DOI lookup (work
`W3191609791`, updated 2026-08-15) and Semantic Scholar DOI lookup each
reported one clustered citing work:

- Tran Hoang Anh, [arXiv:2101.03428v5](https://arxiv.org/abs/2101.03428v5),
  *A simple counterexample for the permanent-on-top conjecture*, journal DOI
  [10.7153/mia-2022-25-01](https://doi.org/10.7153/mia-2022-25-01).

The v5 full text was inspected, not merely its title.  It treats Soules's
permanent-on-top conjecture for positive-semidefinite Hermitian matrices and
constructs an order-five complex rank-two counterexample.  It cites Marcus's
older 2016 author-hosted determinantal-identity draft and proves a Gram/product
identity for permanents.  It does **not** state Conjecture 10, the duplicated
block inequality, the real `3 x 3` coefficient 20 result, or the frozen
equality classification.  Thus the only forward citation located in these
supplemental databases is not a prior occurrence of the target theorem.  The
Crossref/OpenAlex discrepancy also shows why citation counts are used only as
diagnostics here.

## Equivalent binary-cubic/apolar searches

The following additional general-web queries were issued verbatim:

1. `"[f^2,g^2]" binary forms inequality`
2. `"binary cubic" "apolar inner product" inequality`
3. `"split real cubic" apolar inequality`
4. `"Bombieri inner product" "real-rooted" polynomial inequality`
5. `site:arxiv.org apolar binary forms product real linear factors inequality`
6. `site:arxiv.org "binary forms" "apolar inner product" inequality`
7. `site:arxiv.org "split real" cubic "apolar"`
8. `site:arxiv.org Bombieri norm product linear forms equality`
9. `"complete contraction" "binary cubic" inequality`
10. `"symmetric tensor" contraction "real-rooted" cubic inequality`
11. `"squares of binary forms" apolar pairing inequality`
12. `"products of real linear forms" "apolar" inequality`
13. `"reverse Cauchy-Schwarz" "apolar" polynomial`
14. `"reverse Cauchy Schwarz" "binary forms"`
15. `"real-rooted polynomials" "Bombieri" inner product inequality`
16. `"real-rooted" "apolar product" inequality`
17. `"Bombieri inner product" "f^2" "g^2"`
18. `"apolar inner product" "f^2" "g^2"`
19. `"real-rooted" "Bombieri inner product" binary forms`
20. `"real rooted" "Bombieri-Weyl inner product" inequality`
21. `"f²" "g²" "Bombieri" polynomial`
22. `"f squared" "g squared" "apolar inner product"`
23. `"apolar pairing" squares "real-rooted" polynomial`
24. `"Weyl inner product" real-rooted polynomial inequality`

Nearby primary works were opened and their statements compared with the
frozen endpoint:

- Bruce Reznick, *An Inequality for Products of Polynomials*, *Proc. Amer.
  Math. Soc.* 117 (1993), 1063--1073, publisher DOI
  [10.1090/S0002-9939-1993-1119265-2](https://doi.org/10.1090/S0002-9939-1993-1119265-2).
  It proves a Bombieri norm lower bound for a product and classifies equality
  by unitary separation of variables.  It does not compare the bilinear
  quantities `[f^2,g^2]_6` and `[f,g]_3^2` on the cone of split real cubics.
- J. M. Aldaz, A. Bravo, and H. Render,
  [arXiv:2403.10584](https://arxiv.org/abs/2403.10584), *The apolar inner
  product and a Bombieri type inequality for polynomials* (journal reference:
  *J. Inequal. Appl.* 2025, paper 90).  It studies apolar **norms** of products,
  principally for nonhomogeneous polynomials.  Full-text searches found no
  Marcus reference, permanent theorem, binary-cubic split cone, or frozen
  contraction inequality.
- J. M. Aldaz, [arXiv:2607.07482](https://arxiv.org/abs/2607.07482), *There
  is no degree independent Bombieri type inequality for non-homogeneous
  polynomials*.  This is a negative result for nonhomogeneous norm-product
  inequalities and is not an equivalent formulation of the target.
- Ujué Etayo, Haakan Hedenmalm, and Joaquim Ortega-Cerdà,
  [arXiv:2507.20303](https://arxiv.org/abs/2507.20303), *A Bombieri-type
  inequality and equidistribution of points*.  Its inequalities concern
  polynomial zeros, Green functions, and packing numbers, not the frozen
  coefficient contraction.
- Petter Brändén, James Haglund, Mirkó Visontai, and David G. Wagner,
  [arXiv:1010.2565v2](https://arxiv.org/abs/1010.2565v2), *Proof of the
  monotone column permanent conjecture*.  Although it uses real stability,
  Grace apolarity, and derives permanental inequalities, its hypotheses are
  monotone columns/stable polynomials and its statements do not give the
  frozen arbitrary-signed rank-two duplicated-block result or equality set.
- Sinclair's 2026 apolar-kernel paper, discussed above, was also screened
  because it is both recent and connected to finite free convolution.  No
  equivalent theorem was found there.

No queried source stated the degree-three split-real inequality
`[f^2,g^2]_6 <= [f,g]_3^2`, its matrix translation with constant 20, or the
matrix-level iff equality classification.

## Bounded finding and limitations

**Bounded finding.**  In the named primary records, arXiv API results,
Crossref top-ten responses, MathDB page, forward-citation checks, and exact or
equivalent-formulation queries recorded above, this audit found no earlier
statement or proof of the frozen real order-three theorem and no earlier iff
equality classification.  This supports the manuscript's deliberately
limited sentence that a dated search found no prior occurrence in the
recorded sources.

**This is not proof of global novelty.**  In particular:

- general-web indexing and formula recognition are incomplete;
- arXiv `all:` queries search metadata rather than every PDF formula;
- only the top ten fuzzy Crossref results per recorded query were screened;
- Crossref reference matching missed the one citation clustered by OpenAlex
  and Semantic Scholar;
- MathDB had never generated a progress summary and is not an exhaustive
  literature database;
- no subscription search of MathSciNet or the full zbMATH corpus was
  available;
- older books, theses, non-digitized papers, non-English terminology, and an
  unindexed theorem stated only in an equivalent invariant-theoretic language
  may have been missed; and
- a classical apolar or real-stability theorem might imply the frozen result
  without advertising the Marcus matrix formulation or its equality cases.

Accordingly, the defensible wording is: **"No prior occurrence was found in
the dated databases and queries recorded here."**  The stronger phrases
"globally new", "first proof", or "previously unknown" are not certified by
this audit alone.
