# Search log

## Protocol

- Search date/time: 2026-08-29, approximately 10:55–11:17 CST (UTC+08:00).
- Cutoff: material posted/published no later than 2026-08-29.
- Priority: original/publisher DOI record; published article or author/institutional final PDF; arXiv primary preprint; Crossref/zbMATH Open/OpenAlex metadata; secondary pages only for discovery.
- Negative-search language is bounded: “not found in these queries/databases,” never “does not exist.”

## Query-by-query record

| ID | Query / endpoint | Date | Result used | Evidence / limitation |
|---|---|---|---|---|
| S01 | Web: <code>Kusner conjecture equilateral sets l1^n 2n original paper</code> | 2026-08-29 | Located Alon–Pudlák, Swanepoel survey, Ge–Xu–Zhou 2026, Guy reference chain | Broad discovery query; not itself evidence. |
| S02 | Web: <code>"e(l_1^n)" "2n" equilateral</code> | 2026-08-29 | Located modern statements of $e(\ell_1^n)=2n$ and $O(n\log n)$ | Broad discovery query. |
| S03 | Web: <code>equilateral sets normed spaces l1 dimension 4 Kusner</code> | 2026-08-29 | Located Koolen–Laurent–Schrijver and Swanepoel survey | Followed to CWI final paper and DOI. |
| S04 | Web: <code>2026 equilateral sets l_p n p=1 n&lt;=4</code> | 2026-08-29 | Located arXiv:2606.03987 | Current-status primary preprint. |
| S05 | Web: <code>Richard Guy Unsolved problems come of age Amer Math Monthly 90 1983 196 199 Kusner</code> and title variants | 2026-08-29 | Disambiguated the relevant article as “An Olla-Podrida of Open Problems, Often Oddly Posed,” vol. 90(3), 196–200 | Avoided confusing it with Guy’s other 1983/1989 update articles. |
| S06 | Publisher/Crossref: DOI 10.1080/00029890.1983.11971188 and JSTOR DOI 10.2307/2975549 | 2026-08-29 | Verified Guy title, author, year, journal, vol./issue, pp. 196–200 | Direct PDF returned 403/paywall; exact original Problem 0 text not inspected. |
| S07 | Web: <code>"Embedding into rectilinear spaces" Bandelt Chepoi Laurent DOI</code> | 2026-08-29 | Found DOI 10.1007/PL00009370 and author-hosted published PDF | Primary published paper inspected. |
| S08 | Direct PDF: [Bandelt–Chepoi–Laurent](https://pageperso.lis-lab.fr/~victor.chepoi/rectilinear.pdf) | 2026-08-29 | Read abstract p. 595, §4 pp. 600–604, Proposition 4.1 p. 601, Corollary 4.2 p. 603 | Direct support for $e(\ell_1^3)=6$ and elementary $n=2$. |
| S09 | Web: <code>Koolen Laurent Schrijver equilateral dimension rectilinear pdf</code> plus CWI repository search | 2026-08-29 | Found CWI record and final PDF | Institutional repository is authoritative. |
| S10 | Direct PDF: [Koolen–Laurent–Schrijver](https://ir.cwi.nl/pub/1171/1171D.pdf) | 2026-08-29 | Read Conjecture 1 p. 149, Proposition 8 and Theorem 9 p. 154, proof pp. 159–162 | Direct support for $e(\ell_1^4)=8$. |
| S11 | Crossref DOI lookup 10.1023/A:1008391712305 | 2026-08-29 | Verified KLS metadata: *Designs, Codes and Cryptography* 21(1–3), 149–164 (2000) | DOI record. |
| S12 | Direct PDF: [Alon–Pudlák](https://web.math.princeton.edu/~nalon/PDFS/l12.pdf) and author mirror | 2026-08-29 | Read intro and Theorem 1.3, p. 468; references and open-problem remarks | Published paper / author copy. |
| S13 | Crossref DOI lookup 10.1007/s00039-003-0418-7 | 2026-08-29 | Verified AP metadata: *GAFA* 13(3), 467–482 (2003) | DOI record; confirms peer-reviewed publication. |
| S14 | Crossref DOI lookup 10.1090/S0002-9939-1971-0275294-8 | 2026-08-29 | Verified Petty metadata | AMS PDF endpoint was access-blocked; theorem cross-checked in AP and Ge–Xu–Zhou. |
| S15 | Direct arXiv PDF/HTML: [arXiv:2606.03987](https://arxiv.org/abs/2606.03987) | 2026-08-29 | Read §1.1 pp. 1–3, Theorems 1.2/1.3, conclusion p. 45, references pp. 46–47 | v1, submitted 2026-06-02; no journal publication located. It explicitly says $p=1$ is known only for $n\le4$. |
| S16 | arXiv API: <code>all:equilateral AND submittedDate:[202501010000 TO 202608292359]</code>, 100 newest results | 2026-08-29 11:12 CST | Relevant hits: arXiv:2606.03987 and arXiv:2608.14013; no $p=1,\ell_1^5$ solution found in the returned set | Broad query capped at 100 newest hits; many unrelated uses of “equilateral.” |
| S17 | arXiv API: <code>all:Kusner</code>, 100 newest results | 2026-08-29 11:12 CST | Relevant 2026 hits were arXiv:2606.03987 and 2608.14013 | Name collisions create many unrelated geometry/ML hits. No taxicab resolution found. |
| S18 | Direct arXiv HTML: [arXiv:2608.14013](https://arxiv.org/abs/2608.14013) | 2026-08-29 | Read abstract, Theorem 1, Introduction, conclusion | Establishes 58 points in $\ell_5^{56}$; expressly about $2&lt;p&lt;\infty$, not $p=1$. v1 submitted 2026-08-14. |
| S19 | zbMATH Open API: <code>ti:"Equilateral sets" &amp; any:Kusner</code>, 100 results | 2026-08-29 11:14 CST | 3 hits: Chalmers 2026; Swanepoel 2004; Smyth 2013 | Database timestamp 2026-08-29T03:14:54Z. No $p=1,n=5$ resolution in this exact query. |
| S20 | zbMATH Open API: <code>ti:equilateral &amp; any:l_1</code> | 2026-08-29 | 4 hits, all concerning other Banach-space questions (2014–2022) | Search-token limitations make this a weak negative query; retained only as supplementary evidence. |
| S21 | OpenAlex API: search <code>"Kusner" equilateral</code>, date filter 2025-01-01 through 2026-08-29 | 2026-08-29 | Relevant hits were Ge–Xu–Zhou and Chalmers; other hits were name collisions or adjacent work | OpenAlex contained a duplicate record for arXiv:2606.03987. |
| S22 | Web: exact phrases for <code>e(ℓ_1^n)</code>, <code>rectilinear space</code>, <code>n=5</code>, and <code>Kusner</code>, restricted to 2025–2026/arXiv where possible | 2026-08-29 | No additional $p=1$ theorem located; returned Ge–Xu–Zhou, Chalmers, older surveys, and unrelated works | Bounded negative evidence only. |
| S23 | [Supplied SciNet URL](https://api.scinet.pub/p/74491319-9bc4-4067-8f7a-ba824d8dc6c4) | 2026-08-29 | Page reports open status and cites arXiv:2606.03987 | Secondary source; its own vetting date is 2026-07-06. |
| S24 | Crossref DOI batch for Guy, BCL, KLS, AP, Petty, Swanepoel | 2026-08-29 | Verified titles/authors/journals/years/volumes/pages/DOIs | Endpoint form: <code>https://api.crossref.org/works/{DOI}</code>. |
| S25 | Direct survey PDF [arXiv:math/0406264](https://arxiv.org/abs/math/0406264) | 2026-08-29 | Read §1.2 and Problem 1: prove/disprove $e(\ell_1^n)=2n$ for $n\ge5$ | Historical survey; not sufficient by itself for 2026 novelty. |
| S26 | Direct paper [arXiv:math/0309317](https://arxiv.org/abs/math/0309317) and Crossref DOI 10.1007/s00013-003-4840-8 | 2026-08-29 | Checked Swanepoel’s $p&gt;1$ results and bibliographic chain to Guy | Adjacent branch only; prevents conflation with the taxicab claim. |

## Source inventory and exact locations

1. R. K. Guy, “An Olla-Podrida of Open Problems, Often Oddly Posed,” *Amer. Math. Monthly* 90(3) (1983), 196–200. DOI: [10.1080/00029890.1983.11971188](https://doi.org/10.1080/00029890.1983.11971188); JSTOR DOI: [10.2307/2975549](https://doi.org/10.2307/2975549). Original scan was not accessible in this run.
2. H.-J. Bandelt, V. Chepoi, M. Laurent, “Embedding into Rectilinear Spaces,” *Discrete Comput. Geom.* 19(4) (1998), 595–604. DOI: [10.1007/PL00009370](https://doi.org/10.1007/PL00009370). Relevant: p. 600; Prop. 4.1 p. 601; Cor. 4.2 p. 603.
3. J. Koolen, M. Laurent, A. Schrijver, “Equilateral Dimension of the Rectilinear Space,” *Designs Codes Cryptogr.* 21(1–3) (2000), 149–164. DOI: [10.1023/A:1008391712305](https://doi.org/10.1023/A:1008391712305). Relevant: Conj. 1 p. 149; Prop. 8 and Thm. 9 p. 154; proof pp. 159–162.
4. N. Alon, P. Pudlák, “Equilateral Sets in $l_p^n$,” *Geom. Funct. Anal.* 13(3) (2003), 467–482. DOI: [10.1007/s00039-003-0418-7](https://doi.org/10.1007/s00039-003-0418-7). Relevant: Conjs. 1.1/1.2 and Thm. 1.3, p. 468.
5. C. M. Petty, “Equilateral sets in Minkowski spaces,” *Proc. Amer. Math. Soc.* 29(2) (1971), 369–374. DOI: [10.1090/S0002-9939-1971-0275294-8](https://doi.org/10.1090/S0002-9939-1971-0275294-8). Universal $2^n$ bound is cross-quoted in current primary sources.
6. H.-J. Ge, Z. Xu, Y. Zhou, “Kusner’s conjecture: Exact values and linear bounds,” [arXiv:2606.03987v1](https://arxiv.org/abs/2606.03987), 2026-06-02. Relevant: §1.1 pp. 1–3; Thms. 1.2/1.3; conclusion p. 45.
7. L. R. Chalmers, “A counterexample to Kusner’s conjecture on equilateral sets,” [arXiv:2608.14013v1](https://arxiv.org/abs/2608.14013), 2026-08-14. Relevant: abstract and Thm. 1; this is $p=5$, not $p=1$.

## Search limitations

- MathSciNet full access and the full Guy/JSTOR scan were unavailable.
- arXiv, zbMATH Open, OpenAlex, Crossref, publisher/author repositories, and general web indexing do not cover unpublished/private work.
- The novelty conclusion is therefore a dated, reproducible literature lock, not a logical proof of global nonexistence of a solution.

## Second novelty sweep after the candidate strict structural bound

- Search time: 2026-08-29 11:50--11:56 CST (UTC+08:00).
- Candidate claim searched: every eleven-point equilateral realization in
  \(\ell_1^5\), if one exists, uses at least sixteen positive consecutive
  coordinate gaps; equivalently, every 5-nested positive weighted cut
  decomposition of the discrete metric on eleven labels has support at least
  sixteen when cut copies from different chains are counted separately.
- Disposition at search time: no matching prior theorem was found in the
  queries below.  This is a bounded absence result, not proof of novelty.

| ID | Query / endpoint | Result used | Evidence / limitation |
|---|---|---|---|
| S27 | Web exact/structural phrases: "e(l_1^5)" equilateral; equilateral rectilinear "positive gaps" cut frame; equilateral sets l1 singleton cut decomposition Parseval; Kusner equilateral five chains l1 11 points | Returned Ge--Xu--Zhou 2026, Chalmers 2026, KLS 2000, Swanepoel 2003/2004, and unrelated hits; no support-size \(16\) theorem or singleton-compression lemma found | Search-engine coverage is not exhaustive; exact phrases may miss differently worded work. |
| S28 | arXiv API: all:Kusner, 100 newest results, sorted by submitted date | The only equilateral-set hits through the cutoff were arXiv:2606.03987 and arXiv:2608.14013 | The former still reports the \(\ell_1\) conjecture known only through dimension 4; the latter is the \(p=5,n=56\) branch. |
| S29 | arXiv API: all:equilateral AND all:rectilinear and all:"l_1" AND all:equilateral | Zero relevant taxicab-equilateral records | Tokenization of mathematical notation is weak, so this is supplementary only. |
| S30 | OpenAlex works search: exact "e(l_1^5)" equilateral | Zero records | Exact notation search; bounded negative evidence. |
| S31 | OpenAlex works search: Kusner equilateral l1 and equilateral rectilinear cut decomposition | The first returned four name-collision records; the second was noisy and returned no relevant support-size theorem among the first 100 | OpenAlex full-text relevance for notation is weak. |
| S32 | OpenAlex forward-citation query for KLS 2000, work W1578625182, through 2026-08-29 | 25 records; the inspected list included the known surveys/adjacent distance-set papers and no \(n=5\) solution or positive-gap support bound | OpenAlex missed at least the 2026 Ge--Xu--Zhou reference link, so absence is only supplementary. |
| S33 | Direct full-text reinspection of the authoritative CWI final PDF of KLS 2000, especially Proposition 2, Lemmas 4--5, Proposition 8, Theorem 9, and Conclusions | KLS gives the weighted cut-family / \(k\)-nested equivalence and proves the \(k=4\) case, but no lower bound of sixteen cuts for a hypothetical 5-nested family on eleven labels was located | This is the closest prior structural framework and must be cited if the candidate theorem survives audit. |
| S34 | zbMATH Open API rerun of ti:"Equilateral sets" & any:Kusner and phrase variants | The rerun endpoint timed out; the successful same-day Gate-1 result S19 remains the available formal-database record | Explicit failed-query record; not counted as fresh negative evidence. |
| S35 | Crossref bibliographic queries for Kusner equilateral l1, equilateral rectilinear space, and equilateral cut family | Results were dominated by token collisions and supplied no candidate prior theorem | Crossref is used here as DOI metadata discovery, not a reliable full-text absence test. |
| S36 | Fresh exact/structural web queries after the audited \(t=17\) exclusion: "at least eighteen" equilateral rectilinear cut family; "positive gaps" equilateral set l1; "singleton compression" equilateral cut; "5-nested" equilateral cut family eleven | Returned unrelated material or the already logged general equilateral-set literature; no support-\(18\), rank-nine singleton-compression, or equivalent five-chain theorem was found | Search completed 2026-08-29 12:20 CST. This upgrades only the bounded no-match record; web indexing may miss differently phrased or unpublished work. |

The closest prior-art statement remains KLS Proposition 2: existence is
equivalent to a positive weighted \(k\)-nested equilateral cut family.  The
internal support-\(18\) obstruction uses that framework but adds a Parseval
spectral-deficit argument and a low-rank singleton-compression lemma not found
in the inspected sources.  The proof passed independent mathematical audits
through \(t=17\); the novelty conclusion remains bounded.

After the independent \(t=16\) and \(t=17\) audits, the candidate internal
claim is now the stronger support-\(18\) bound.  S27--S35 remain relevant to
its ingredients, and S36 is the additional exact-phrase sweep.  No claim of
absolute novelty is made.

## Final secondary sweep for the frozen support-\(19\) theorem

- Search time: 2026-08-29 12:46--12:53 CST (UTC+08:00).
- Frozen claim searched: a hypothetical eleven-point equilateral set in
  \(\ell_1^5\) uses at least nineteen positive consecutive coordinate gaps,
  equivalently at least twenty-four coordinate levels in total.
- Disposition: no matching theorem was found in the following bounded
  queries.  This is a reproducible absence report, not a proof of absolute
  novelty.

| ID | Query / endpoint | Result used | Evidence / limitation |
|---|---|---|---|
| S37 | Web exact and structural queries for “nineteen positive” equilateral rectilinear cut family; “support 19” Kusner equilateral l1; “ten-block” antichain equilateral cut decomposition; “Sherman-Morrison” equilateral cut family; arXiv equilateral l1 dimension five Kusner; and positive weighted 5-nested equilateral | Returned the already logged KLS framework, Ge--Xu--Zhou status report, adjacent equilateral-set papers, or unrelated uses of the phrases.  No support-\(19\), ten-block antichain, or equivalent five-chain theorem was located. | Exact phrases can miss different terminology; web and arXiv indexing do not cover private or unindexed work. |

The closest inspected prior theorem remains KLS Proposition 2, which gives
the positive weighted nested-cut equivalence but not the support-\(19\)
obstruction.  The new rank-ten step uses the exact identity
\(D+c_pJ=BGB^T\) and its Sherman--Morrison consequence to make the ten
oriented blocks pairwise intersecting and incomparable.  That step passed
the independent Round 5 proof and checker audit.  The original
\(e(\ell_1^5)=10\) question remains open.
