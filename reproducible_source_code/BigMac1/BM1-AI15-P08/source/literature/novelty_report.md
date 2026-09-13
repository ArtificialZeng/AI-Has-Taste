# Gate 1 novelty report: Sheil-Small self-inversive covering problem

**Audit date:** 2026-08-29 (Asia/Shanghai)  
**Scope:** the exact covering question attributed to T. Sheil-Small, including the unrestricted-degree problem and the proposed first cases \(n=2,3,4,5\).  
**Result:** no proof, counterexample, or published resolution of any of the four requested low-degree cases was located. This is a reproducible **not-found result**, not proof that no such publication exists.

## Proposed NOVELTY_LOCK

> **NOVELTY_LOCK (2026-08-29): PROVISIONAL OPEN / NOT FOUND.** No full solution, counterexample, or degree-\(2,3,4,5\) resolution of the standard self-inversive formulation was found in the primary-source and formal-database searches recorded below. Any such new result remains prima facie novel, subject to a second search after the mathematical claim is fixed and to resolution of the statement discrepancy below.

The lock should freeze the following claims and qualifications.

| ID | Claim that may be used | Evidence level | Qualification |
|---|---|---|---|
| N1 | Hayman--Lingham Problem 4.24 asks whether \(P(\mathbb D)\) contains an unspecified-center disc of radius \(A=\max_k\lvert a_k\rvert\), and attributes it to T. Sheil-Small. | Exact source text in arXiv v2 source, lines 2375--2384 of the extracted TeX; PDF physical p. 80 (printed p. 79). | The source's root symmetry is literally \(\zeta\mapsto1/\zeta\), not \(1/\bar\zeta\). |
| N2 | The problem was already published in the 1974 Canterbury problem collection. | Hayman--Lingham Appendix Table 2 maps Problems 4.22--4.24 to source B; Table 1 identifies source B as the 1974 Canterbury volume. Cambridge chapter metadata independently confirms the source. | The paywalled 1974 chapter text was not inspected, so its exact wording was not verified. |
| N3 | The 2018 source update says, “No progress on this problem has been reported to us.” | Exact source text, Update 4.24. | This establishes the editors' report through 2018, not present-day openness by itself. |
| N4 | No later complete solution or counterexample was located through 2026-08-29. | arXiv, Crossref, OpenAlex and source-citation searches; supplemental web and publisher searches. | Negative search evidence only; Google Scholar, MathSciNet and zbMATH were not exhaustively accessible. |
| N5 | No published exact result for \(n=2,3,4,\) or \(5\) was located. | Degree-specific phrase/topic searches in the same sources. | Negative search evidence only. Papers on zero location of quadratic/cubic/quartic/quintic self-inversive polynomials are not covering results. |
| N6 | Solyanik's 2014 coefficient covering theorem does not settle Problem 4.24. | Theorem/corollary checked in the arXiv source of arXiv:1410.6772. | Its guaranteed radius is binomially weighted and its covered disc is centered at the normalized constant term, whereas Problem 4.24 asks for the unweighted maximum coefficient and permits an arbitrary center. |

Recommended wording for any prospective paper is therefore **“the standard self-inversive interpretation of Hayman--Lingham Problem 4.24”**, followed by an explicit definition. Do not claim that the literature itself has already corrected the missing conjugation.

## 1. Source, wording, and provenance

### 1.1 Verifiable source of record

Walter K. Hayman and Eleanor F. Lingham, *Research Problems in Function Theory (New Edition)*, arXiv:1809.07200v2, submitted 2018-09-19 and revised 2018-09-21, DOI [10.48550/arXiv.1809.07200](https://doi.org/10.48550/arXiv.1809.07200), is the accessible source used for exact textual checking.

- Abstract/metadata: [arXiv:1809.07200](https://arxiv.org/abs/1809.07200).
- Problem location: source TeX lines 2375--2384 in v2; PDF physical p. 80, printed p. 79.
- The displayed polynomial is \(P(z)=\sum_{0}^{n}a_kz^k\), and the radius is \(A=\max_{0\le k\le n}|a_k|\).
- The requested disc has no prescribed center. Thus this is an image-inradius assertion, not necessarily a disc about \(P(0)\) or about \(0\).
- The problem is attributed parenthetically to T. Sheil-Small.
- The source's short update is quoted in N3 above; there is no proof or partial case in the update.

Local reproducibility facts from the fetched v2 PDF/source during this audit:

```text
PDF SHA-256: 8e28fd4403a07e4e19a9816b7efaafddf9f475d59cf8c34a8255cb03833ed4f0
source archive name: 1809.07200v2-src.tar
```

The 2019 final edition is Walter K. Hayman and Eleanor F. Lingham, *Research Problems in Function Theory: Fiftieth Anniversary Edition*, Springer Cham, DOI [10.1007/978-3-030-25165-9](https://doi.org/10.1007/978-3-030-25165-9), online ISBN 978-3-030-25165-9, print ISBN 978-3-030-25164-2. The relevant chapter is “Polynomials,” pp. 81--95, DOI [10.1007/978-3-030-25165-9_4](https://doi.org/10.1007/978-3-030-25165-9_4). The Springer chapter is paywalled; therefore the exact statement above was checked against the accessible arXiv v2 source, not inferred from the Springer snippet.

### 1.2 Statement discrepancy that must remain visible

The Hayman--Lingham v2 TeX literally says that a zero \(\zeta\) is accompanied by \(1/\zeta\). The supplied SciNet page and the standard definition instead use \(1/\bar\zeta\), equivalently

\[
P(z)=\omega z^n\overline{P(1/\bar z)},\qquad |\omega|=1,
\]

or a conjugate-reversal relation on the coefficients. These define different classes unless additional reality assumptions are imposed. Standard sources use conjugate reciprocal symmetry; for example:

- Matilde N. Lalin and Chris J. Smyth, “Unimodularity of zeros of self-inversive polynomials,” *Acta Mathematica Hungarica* **138** (2013), 85--101, DOI [10.1007/s10474-012-0225-4](https://doi.org/10.1007/s10474-012-0225-4), arXiv:[1201.0774](https://arxiv.org/abs/1201.0774).
- Ricardo S. Vieira, “Polynomials with symmetric zeros,” arXiv:[1904.01940](https://arxiv.org/abs/1904.01940), which explicitly treats self-inversive and self-reciprocal symmetry as distinct notions.

Because the source labels the polynomial “self-inversive,” omission of the conjugation is plausibly a typographical error, but no author erratum or correction was found. A proof for the \(1/\bar\zeta\) class must not be advertised as a literal proof of the \(1/\zeta\) formulation without this caveat.

### 1.3 The problem is from 1974, not approximately 35 years old

Appendix Table 2 of arXiv:1809.07200v2 assigns Problems 4.22--4.24 to source B. Table 1 identifies B as J. G. Clunie and W. K. Hayman (eds.), *Symposium on Complex Analysis, Canterbury, 1973*, London Mathematical Society Lecture Note Series 12, Cambridge University Press, 1974, pp. 143--180.

Cambridge's official metadata gives the specific chapter “New problems,” pp. 155--180, DOI [10.1017/CBO9780511662263.034](https://doi.org/10.1017/CBO9780511662263.034), in the book DOI [10.1017/CBO9780511662263](https://doi.org/10.1017/CBO9780511662263). Official publisher page: [Cambridge Core, “New problems”](https://www.cambridge.org/core/books/abs/proceedings-of-the-symposium-on-complex-analysis-canterbury-1973/new-problems/448E4822E4E02F1F8A73D101B4BECEA2). The available publisher preview contains front matter and the table of contents, not the full chapter; it confirms “New problems” at p. 155 and T. B. Sheil-Small as a contributor, but does not permit checking the original 1974 phrasing.

Consequently, the conservative age statement is: **publicly recorded since 1974, hence about 52 years old in 2026**. The SciNet page's “~35-year-old” characterization is inconsistent with the edition's own source table.

## 2. Current problem page

The supplied page, [SciNet ID 11ff995d-348a-4fda-93d6-a23c6cee26aa](https://api.scinet.pub/p/11ff995d-348a-4fda-93d6-a23c6cee26aa), was inspected on 2026-08-29.

It states the standard conjugate-inversion formulation, records the 2018 update, labels the problem open as of 2026-07-06, and displayed zero investigations at the time of inspection. It is a useful live claim-graph page, but not a primary publication or proof of present-day openness. Its status was therefore treated as a search lead only.

## 3. Primary-source and formal-database query ledger

All queries below were run on 2026-08-29. “No relevant hit” means that titles/abstracts or available text of the returned candidates did not state the exact image-disc result; it does not mean the database proves absence.

### 3.1 Exact and phrase searches

The following exact query strings were used in general scholarly web search, with publisher/arXiv/author-copy pages preferred over aggregators:

```text
"Problem 4.24" "self-inversive" polynomial
"self-inversive polynomial" "covering theorem"
"self-inversive polynomial" "disc of radius"
"self-inversive polynomial" image unit disk
"self-inversive polynomial" quadratic covering disk
"self-inversive polynomial" cubic covering disk
"self-inversive polynomial" quartic covering disk
"self-inversive polynomial" quintic covering disk
"Sheil-Small" polynomial covering
"Research Problems in Function Theory" self-inversive
```

Outcome: the exact problem page/source, general covering theorems for arbitrary complex polynomials, and papers about the *locations of zeros* of self-inversive polynomials were found. No exact solution or degree-\(2,3,4,5\) case was found.

### 3.2 arXiv

API/search queries included:

```text
all:"self-inversive"
all:"self-inversive" AND all:covering
all:"self-inversive" AND all:image
all:"self-inversive" AND all:range
all:"Sheil-Small" AND all:covering
```

The broad first query returned 67 records, including false positives containing “self-inverse.” The covering conjunction returned no exact matching item; the image/range and Sheil-Small conjunctions produced only unrelated results. Relevant inspected self-inversive-polynomial papers included arXiv:1201.0774, 1504.00615, 1511.01340, 1606.03159, 1704.00463, 1902.04231, 1904.01940, 1908.03208, and 1909.12548. Their stated results concern zero location, unimodularity, root geometry, orthogonality, curves, or codes—not the inradius of \(P(\mathbb D)\).

### 3.3 Crossref

Crossref REST API bibliographic searches, filtered where supported to 1989-01-01 through 2026-08-29 and inspected in relevance order (up to the first 100 records per broad query), used:

```text
self-inversive polynomial
self inversive polynomial covering disc
Sheil-Small polynomial covering
Problem 4.24 polynomial
polynomial maps unit disc domain containing disc coefficient
```

The broad queries were noisy because Crossref token-matches metadata. Relevant family records were checked, including DOI [10.1112/blms/bdp104](https://doi.org/10.1112/blms/bdp104), [10.1007/s10474-012-0225-4](https://doi.org/10.1007/s10474-012-0225-4), [10.1016/j.amc.2022.127547](https://doi.org/10.1016/j.amc.2022.127547), [10.1080/00029890.2019.1568151](https://doi.org/10.1080/00029890.2019.1568151), and the Sheil-Small book chapter DOI [10.1017/CBO9780511543074.009](https://doi.org/10.1017/CBO9780511543074.009). None states the target covering result. This was a metadata search, not full-text exhaustive screening.

A current false lead was Mayanglambam Singhajit Singh, Madhav Prasad Poudel, and Barchand Chanam, “Some Inequalities on Polynomials in the Complex Plane Concerning a Linear Differential Operator,” *Journal of Mathematics* (first published 2026-01-14), DOI [10.1155/jom/9930559](https://doi.org/10.1155/jom/9930559). Its Section 2.2, Theorem 10 and Corollaries 9--10, gives operator/norm inequalities for self-inversive polynomials; it does not give a disc contained in the image of the unit disc.

### 3.4 OpenAlex and citation tracing

OpenAlex searches used:

```text
self-inversive polynomial covering disc
self-inversive polynomial image unit disk
Sheil-Small covering problem
Problem 4.24 self-inversive
Research Problems in Function Theory self-inversive
```

The exact 1974 chapter DOI resolves to OpenAlex work W150365607, “New problems.” Its cited-by list contained three works at audit time: DOI [10.1007/s11511-015-0122-0](https://doi.org/10.1007/s11511-015-0122-0), [10.1007/BF01140018](https://doi.org/10.1007/BF01140018), and [10.1007/BF00969939](https://doi.org/10.1007/BF00969939). Their titles/abstracts concern entire functions and asymptotic-value sets, not self-inversive image covering. Crossref reported two references-to-this-item, also with no relevant title surfaced. A solution could omit the chapter citation, so this small citation graph is only strong corroborating negative evidence.

The OpenAlex record associated with the 2019 book appeared metadata-merged/polluted by pre-publication references and was not used as a reliable direct citation list.

### 3.5 zbMATH Open, MathSciNet, Semantic Scholar, Google Scholar, OEIS

- Exact web-index searches `site:zbmath.org "self-inversive" covering polynomial` and related variants surfaced only zero-location/derivative entries. Direct zbMATH UI access was blocked by Cloudflare in this session; REST attempts returned gateway/terms-access failures. Hence there was no exhaustive zbMATH query.
- MathSciNet was not available through an authenticated interface. The MathNet record for Dubinin's survey supplies MR 3013845 and Zbl 1267.30012, but this is not a substitute for full MathSciNet searching.
- Semantic Scholar query `Sheil-Small covering problem` returned unrelated harmonic-mapping items; subsequent API calls were rate-limited (HTTP 429).
- Direct Google Scholar access timed out/unavailable. OpenAlex, Crossref, arXiv, and publisher searches were used as Google-Scholar-equivalent discovery routes, but are not identical in coverage.
- OEIS API queries `self-inversive polynomial`, `Sheil-Small polynomial`, and `self reciprocal polynomial covering disk` were rejected with HTTP 403. Search-engine `site:oeis.org` variants returned no relevant sequence. The problem is geometric rather than sequence-based, so this is a weak auxiliary check only.

These access limitations are the principal reason the lock is **provisional**, not a declaration that absence has been proved.

## 4. The nearest genuine covering theorem is different

Alexey Solyanik, “Note on the covering theorem for complex polynomials,” arXiv:[1410.6772](https://arxiv.org/abs/1410.6772), submitted 2014-10-24, answers a question of V. N. Dubinin. In the source, for

\[
q(z)=\sum_{k=1}^{n}\widehat q(k)z^k,
\qquad
n(q)=\max_{0\le k\le n}\frac{|\widehat q(k)|}{\binom nk},
\]

Corollary 1 guarantees a disc of radius \(n(q)\) in \(q(\mathbb D)\). This does not imply a disc of radius \(\max_k|a_k|\): the binomial divisor can reduce the guaranteed radius, and subtracting \(a_0\) fixes the covered disc's center at the translated origin. Problem 4.24 allows the center to vary but asks for the substantially larger unweighted coefficient maximum.

V. N. Dubinin's survey “Methods of geometric function theory in classical and modern problems for polynomials,” *Russian Mathematical Surveys* **67** (2012), 599--684, DOI [10.1070/RM2012v067n04ABEH004803](https://doi.org/10.1070/RM2012v067n04ABEH004803), MR 3013845, Zbl 1267.30012, has a section on polynomial covering theorems. The relevant results concern expressions such as \(P(z)+P(1/z)\), restricted critical values, or coefficient-normalized guarantees. Its occurrences of self-inversive polynomials concern equality cases for other inequalities, not the Sheil-Small image-inradius assertion.

Therefore neither source should be cited as a solution or partial low-degree solution without an additional argument.

## 5. Low-degree \(n=2,3,4,5\) audit

Degree-name variants (“quadratic,” “cubic,” “quartic,” “quintic”) and numeral variants were combined with `self-inversive`, `covering`, `image`, `unit disk/disc`, and `inradius`. Returned cubic/quartic papers included root-envelope and Blaschke-product geometry, not the image \(P(\mathbb D)\) containing a coefficient-sized disc. No source found stated:

1. a theorem proving the target assertion for any one of \(n=2,3,4,5\);
2. a counterexample of any one of those degrees; or
3. an equality/extremal classification for the target image inradius.

The strongest source-level evidence before 2019 is the editors' Update 4.24 reporting no progress. The post-2018 database sweep did not reveal a later low-degree paper. Thus an exact result for even \(n=2\) should still undergo a claim-specific second search; it should not be called “the first solution” solely from this audit.

## 6. Reproducibility commands and URLs

Representative commands used or sufficient to reproduce the core checks:

```bash
curl -L 'https://arxiv.org/pdf/1809.07200v2' -o /tmp/1809.07200v2.pdf
curl -L 'https://arxiv.org/e-print/1809.07200v2' -o /tmp/1809.07200v2-src.tar
shasum -a 256 /tmp/1809.07200v2.pdf
pdftotext -layout /tmp/1809.07200v2.pdf /tmp/1809.07200v2.txt
rg -n 'Problem 4\.24|Update 4\.24|No progress' /tmp/1809.07200v2.txt

mkdir /tmp/hayman-lingham-v2-source
tar -xf /tmp/1809.07200v2-src.tar -C /tmp/hayman-lingham-v2-source
rg -n 'Problem 4\.24|Update 4\.24|No progress' /tmp/hayman-lingham-v2-source

curl -L 'https://export.arxiv.org/api/query?search_query=all:%22self-inversive%22&start=0&max_results=100' \
  -o /tmp/arxiv_self_inversive.xml

curl -L 'https://api.openalex.org/works/https://doi.org/10.1017/CBO9780511662263.034' \
  -o /tmp/openalex_problem_source.json

curl -L 'https://api.crossref.org/works/10.1017/CBO9780511662263.034' \
  -o /tmp/crossref_problem_source.json

curl -L 'https://api.crossref.org/works?query.bibliographic=self-inversive%20polynomial&filter=from-pub-date:1989-01-01,until-pub-date:2026-08-29&rows=100' \
  -o /tmp/crossref_self_inversive.json

curl -L 'https://api.openalex.org/works?search=self-inversive%20polynomial%20covering%20disc&per-page=100' \
  -o /tmp/openalex_covering_search.json
```

Stable source URLs used:

- [Hayman--Lingham arXiv record](https://arxiv.org/abs/1809.07200)
- [Springer book](https://link.springer.com/book/10.1007/978-3-030-25165-9)
- [Springer “Polynomials” chapter](https://link.springer.com/chapter/10.1007/978-3-030-25165-9_4)
- [Cambridge 1974 “New problems” chapter](https://www.cambridge.org/core/books/abs/proceedings-of-the-symposium-on-complex-analysis-canterbury-1973/new-problems/448E4822E4E02F1F8A73D101B4BECEA2)
- [SciNet current problem page](https://api.scinet.pub/p/11ff995d-348a-4fda-93d6-a23c6cee26aa)
- [Solyanik arXiv record](https://arxiv.org/abs/1410.6772)
- [Dubinin survey at MathNet](https://www.mathnet.ru/eng/rm9488)

## 7. Publication gate arising from this audit

Before asserting novelty for a mathematical result, run a second search using the exact theorem language, any extremal polynomial discovered, its coefficient pattern, and its algebraic inradius value. Also re-check forward citations to the 1974 chapter, the 2018 arXiv edition, Solyanik's paper, and Dubinin's survey. If feasible, obtain the full 1974 “New problems” chapter or an author/editor clarification about \(1/\zeta\) versus \(1/\bar\zeta\).

On present evidence the correct terminal novelty assessment is **not `ALREADY_SOLVED_STOP`**. It is a provisional green light to investigate the standard conjugate-inversion formulation, with explicit warning that novelty and even the exact historical statement must be re-audited once a decisive claim exists.
