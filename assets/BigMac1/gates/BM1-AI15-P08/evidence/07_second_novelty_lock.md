# Gate 6 second NOVELTY_LOCK: frozen low-degree and subclass claims

**Audit date:** 2026-08-29 (Asia/Shanghai)  
**Literature cutoff:** 2026-08-29  
**Definition:** exact degree \(n\ge1\), with the zero multiset invariant under
\(\zeta\mapsto1/\overline\zeta\), equivalently
\(a_k=\omega\overline{a_{n-k}}\) for some \(|\omega|=1\).  This is the
standard definition fixed by the project, not the literal unconjugated map
printed in the accessible Hayman--Lingham source.

## 1. Verdict

> **SECOND NOVELTY_LOCK (2026-08-29): PARTIAL NOVELTY CLEARANCE; CLAIMS
> DISAGGREGATED.**  No exact prior match was located for the positive-degree
> theorem \(n\le3\), for the degree-4/5 off-unit-zero branch, for the
> degree-4/5 all-unimodular branch under \(2|a_n|\ge A\), or for the even
> three-term pullback class.  These are prima-facie novel only: the search does
> not prove absence.  By contrast, the endpoint-max branch is already a special
> case of a covering theorem for arbitrary polynomials, and endpoint binomials
> are an elementary instance of the same fact.  Those two branches are not new.

The exact frozen claims and defensible novelty labels are:

| Frozen claim | Second-pass result | Permitted novelty wording |
|---|---|---|
| Every standard self-inversive polynomial of degree \(1\le n\le3\) covers an open disk of radius \(A\). | No exact prior match found. | “Prima-facie new resolution through degree three,” subject to proof/referee audit and the access limitations in §5. |
| For \(n=4,5\), an endpoint coefficient realizing \(A\) suffices. | Already known for arbitrary polynomials; see §2.1. | Background only; do not call this branch new. |
| For \(n=4,5\), a zero off the unit circle suffices. | No exact prior match found. | “Prima-facie new partial degree-four/five result.” |
| For \(n=4,5\), all roots unimodular and \(2\lvert a_n\rvert\ge A\) suffices. | No exact prior match found. | “Prima-facie new partial degree-four/five result.” |
| For even \(n=2m\), support \(\{0,m,2m\}\) suffices. | No exact published formulation found.  The reduction to degree two is immediate. | “Apparently unrecorded infinite corollary of the quadratic theorem,” not a major independent novelty claim. |
| For odd \(n\), endpoint support \(\{0,n\}\) suffices and the image is exactly a disk of radius \(A\). | Elementary and subsumed by the known endpoint theorem; true for every positive degree. | No novelty claim. |

The labels above concern literature priority only.  They do not certify the
project's proofs, whose independent mathematical audit is a separate gate.

## 2. Claim-level overlap analysis

### 2.1 Endpoint-max branch is already known

Alexey Solyanik, “Note on the covering theorem for complex polynomials,”
[arXiv:1410.6772](https://arxiv.org/abs/1410.6772), DOI
[10.48550/arXiv.1410.6772](https://doi.org/10.48550/arXiv.1410.6772), is a
primary source.  In its source TeX, Lemma 3 bounds every coefficient of a
polynomial omitting a point, and Corollary 1 states the resulting disk
containment.  For

\[
q(z)=\sum_{k=1}^n \widehat q(k)z^k,
\qquad
n(q)=\max_{1\le k\le n}
  \frac{|\widehat q(k)|}{\binom nk},
\]

Corollary 1 gives \(B(0,n(q))\subset q(\mathbb D)\).  Apply it to
\(q=P-a_0\).  The term \(k=n\) has \(\binom nn=1\), so

\[
             B(a_0,|a_n|)\subset P(\mathbb D)                     \tag{2.1}
\]

for **every** complex polynomial, without self-inversivity.  The same inclusion
also follows immediately from the product of the roots of \(P-w\).  Since a
self-inversive polynomial has \(|a_0|=|a_n|\), either endpoint realizing \(A\)
means \(A=|a_n|\), and (2.1) proves that branch.

Thus the degree-4/5 statements may contain new branches, but the disjunction
“endpoint maximal, or ...” is not wholly novel.  This is a refinement of the
first-pass ledger entry C09: Solyanik does not solve the unweighted general
problem, but it does solve exactly the endpoint-max subcase.

The OpenAlex primary record
[W260159835](https://api.openalex.org/works/W260159835) listed zero citing works at the
audit time.  That forward-citation count is corroborating metadata, not evidence
that the theorem is unknown elsewhere.

### 2.2 Degree \(1\le n\le3\)

The second search combined each of `quadratic`, `cubic`, `degree two`, and
`degree three` with `self-inversive`, `image`, `unit disk/disc`, `covering`,
`contains a disk`, `inradius`, and `maximum coefficient`.  arXiv's narrow
Boolean query returned no candidate.  Crossref returned only root-location or
root-geometry papers.  zbMATH Open returned no title containing both
`self-inversive` and `quadratic`; its cubic query returned the two candidates
excluded in §3.2.

No inspected source states that all standard self-inversive quadratics or
cubics have an image disk of radius \(\max_k|a_k|\).  The 2018
Hayman--Lingham update also reported no progress on the parent problem, but
that statement alone would not exclude an uncited elementary low-degree fact.
The second-pass verdict is therefore **no exact prior match found**, with 82%
novelty confidence rather than a claim of exhaustive absence.

Here and throughout, “\(n\le3\)” means \(1\le n\le3\) as in the frozen formal
statement.  Nonzero constant polynomials would make the assertion false and
are outside scope.

### 2.3 Degree four and five root-type branches

The exact searches separately used the phrases `zero off the unit circle`,
`all roots unimodular`, `quartic`, `quintic`, and `2|a_n|`, together with image
and disk-covering language.  No paper was found asserting either:

1. the radius-\(A\) image covering for a self-inversive quartic or quintic
   having a reciprocal pair off the circle; or
2. the radius-\(A\) image covering for an all-unimodular quartic or quintic
   under \(2|a_n|\ge A\).

The many papers returned for `all zeros on the unit circle` establish
conditions for *root location*.  They do not establish a disk inside the range
of the polynomial.  In particular, a coefficient hypothesis sufficient to make
roots unimodular is not prior art for an image-covering theorem conditional on
unimodularity.

The claim-specific verdict for both branches is **no exact prior match found**,
with 80% novelty confidence.  The shared residual risk is that an image theorem
appears inside a source whose title and abstract advertise only zero location
or geometric function theory.

### 2.4 Sparse subclasses

For even \(n=2m\), a polynomial supported on \(\{0,m,2m\}\) has the form
\(P(z)=Q(z^m)\), where \(Q\) is a self-inversive quadratic.  Because
\(z^m(\mathbb D)=\mathbb D\), the images of \(P\) and \(Q\) agree.  No exact
published statement of this support-class corollary was found under
`self-inversive trinomial`, `three-term`, `Q(z^m)`, or
`self-reciprocal trinomial` searches.  The likely novelty resides entirely in
the quadratic covering theorem; the pullback itself is elementary.

If \(P(z)=a_0+a_nz^n\), then \(z^n(\mathbb D)=\mathbb D\), and
self-inversivity gives \(|a_0|=|a_n|=A\).  Hence
\(P(\mathbb D)=B(a_0,A)\).  This observation holds for even as well as odd
positive degrees and is also contained in (2.1).  The frozen odd-degree
endpoint-binomial claim is therefore not a defensible standalone novelty.

## 3. Primary candidates inspected and excluded

### 3.1 Source book and problem records

- T. Sheil-Small, *Complex Polynomials*, Chapter 7, “Self-inversive
  polynomials,” pp. 228--262, DOI
  [10.1017/CBO9780511543074.009](https://doi.org/10.1017/CBO9780511543074.009),
  official [Cambridge chapter page](https://www.cambridge.org/core/books/abs/complex-polynomials/selfinversive-polynomials/30F52A8B228317A486CF31A6A63293C5).
  The public
  [book preview](https://api.pageplace.de/preview/DT0400.9780511059063_A23688821/preview-9780511059063_A23688821.pdf)
  exposes the table of contents and preface but not the chapter body.  Sections
  7.1--7.6 are listed as interspersed zeros, maximum-modulus relations,
  univalent polynomials, angular separation, and Suffridge extremals.  The
  preface describes root-circle and coefficient/maximum-modulus results, not
  the frozen covering claims.  Because the body was inaccessible, this is not
  a full-text exclusion.
- W. K. Hayman and E. F. Lingham, *Research Problems in Function Theory*,
  [arXiv:1809.07200v2](https://arxiv.org/abs/1809.07200), Problem 4.24 and its
  update.  This is the exact accessible problem record already audited in Gate
  1; it gives no low-degree cases.

### 3.2 Cubic papers

- William Calbeck, “Cubic Self-inversive Polynomials whose roots envelope
  conics,” [arXiv:1511.01340](https://arxiv.org/abs/1511.01340).  The full
  arXiv source was inspected.  Its main result (Theorem 2.1 in the rendered
  paper) describes a conic tangent to the three lines joining unimodular roots
  of a parameterized cubic.  It says nothing about a disk contained in
  \(P(\mathbb D)\).
- Finbarr Holland and Roger Smyth, “Cardioids and Self-inversive Cubic
  Polynomials,” *American Mathematical Monthly* **126** (2019), 319--329,
  DOI
  [10.1080/00029890.2019.1568151](https://doi.org/10.1080/00029890.2019.1568151).
  The official abstract identifies its result as cardioid tangent geometry and
  Morley's trisector theorem.  It does not state an image-covering result.
  zbMATH Open indexes it as Zbl 1420.30001.

### 3.3 Zero-location and norm papers

- Piroska Lakatos and László Losonczi, “Self-inversive polynomials whose
  zeros are on the unit circle,” *Publ. Math. Debrecen* **65** (2004),
  409--420, DOI
  [10.5486/PMD.2004.3250](https://doi.org/10.5486/PMD.2004.3250), official
  [publisher PDF](https://publi.math.unideb.hu/paper/985/download/10_5486_PMD_2004_3250.pdf).
  Theorem 1 gives coefficient conditions for unimodular zeros and discusses
  their multiplicity; no image disk is asserted.
- Matilde N. Lalin and Chris J. Smyth, “Unimodularity of zeros of
  self-inversive polynomials,” *Acta Math. Hungar.* **138** (2013), 85--101,
  DOI
  [10.1007/s10474-012-0225-4](https://doi.org/10.1007/s10474-012-0225-4),
  [arXiv:1201.0774](https://arxiv.org/abs/1201.0774).  Theorem 1 and its
  corollaries construct or characterize polynomials with all zeros on the unit
  circle; they do not control the inradius of \(P(\mathbb D)\).
- László Losonczi and Andrzej Schinzel, “Self-inversive polynomials of odd
  degree,” *Ramanujan J.* **14** (2007), 305--320, DOI
  [10.1007/s11139-007-9029-5](https://doi.org/10.1007/s11139-007-9029-5).
  Its publisher/metadata abstract gives a coefficient condition ensuring
  simple unimodular zeros, not image covering.
- Christopher D. Sinclair and Jeffrey D. Vaaler, “Self-inversive polynomials
  with all zeros on the unit circle,” in *Number Theory and Polynomials*
  (2008), 312--321, DOI
  [10.1017/CBO9780511721274.020](https://doi.org/10.1017/CBO9780511721274.020).
  The official Cambridge metadata concerns zero-location criteria.
- Artūras Dubickas and Jonas Jankauskas, “On Mahler measures of a
  self-inversive polynomial and its derivative,” *Bull. Lond. Math. Soc.*
  **42** (2010), 195--209, DOI
  [10.1112/blms/bdp104](https://doi.org/10.1112/blms/bdp104).  Its theorems
  concern Mahler measure and \(L^p\) norms, including a sharp cubic constant,
  not the range \(P(\mathbb D)\).

These exclusions are important because database relevance rankings repeatedly
returned them for the frozen queries.

## 4. Reproducible query record

All searches in this section were run on 2026-08-29.

### 4.1 Exact web/publisher strings

```text
"self-inversive polynomial" "contains a disk" quadratic cubic
"self-inversive" quartic quintic "unit disk" image covering
"self-inversive trinomial" "image" "unit disk"
"self-inversive" "leading coefficient" "unit disk" covering theorem
"self-inversive quadratic" covering polynomial disk image
"self-inversive cubic" covering polynomial disk image
"self-inversive quartic" "covering" polynomial image disk
"self-inversive quintic" "covering" polynomial image disk
"self-inversive polynomial" "zero off the unit circle" "image" disk
"self-inversive polynomial" "2|a_n|"
"self-inversive trinomial" covering disk image
"self-reciprocal trinomial" covering theorem disk
"Q(z^m)" self-inversive polynomial unit disk
"three-term" self-inversive polynomial unit disk image
"a+b z^n" maps unit disk onto disk polynomial
polynomial image unit disk contains disk radius leading coefficient Vieta covering theorem
"|a_n|" "P(D)" polynomial contains disk
"Self-inversive polynomials" Sheil-Small covering
```

No exact frozen claim was found.  Returned items were screened by official
abstracts or full primary text when accessible; representative exclusions are
in §3.

### 4.2 arXiv API

```text
all:"self-inversive" AND (all:quadratic OR all:cubic) AND (all:covering OR all:image OR all:inradius)
all:"self-inversive" AND (all:quartic OR all:quintic) AND (all:covering OR all:image OR all:inradius)
all:"self-inversive" AND (all:trinomial OR all:binomial) AND (all:covering OR all:image)
all:"self-inversive" AND all:"unit disk" AND all:"coefficient"
```

The first three returned no paper; the last returned only an unrelated work on
random-polynomial zero distributions.  The broad `all:"self-inversive"`
family screened at Gate 1 was also rechecked for low-degree titles.

Representative API endpoint:

```text
https://export.arxiv.org/api/query?search_query=all:%22self-inversive%22&start=0&max_results=100
```

### 4.3 Crossref and OpenAlex

Each database was searched through 2026-08-29 using these exact seven strings:

```text
self-inversive quadratic covering unit disk
self-inversive cubic image unit disk radius coefficient
self-inversive quartic zero off unit circle image
self-inversive quintic zero off unit circle image
self-inversive polynomial all roots unimodular 2 leading coefficient
self-inversive trinomial image unit disk
self-inversive endpoint binomial image disk
```

For Crossref, the top five `query.bibliographic` results were inspected per
string.  For OpenAlex, the top five semantic results were inspected per string.
Crossref produced the relevant-family candidates in §3 but no exact claim;
OpenAlex was much noisier and produced no additional candidate.

Reproducible endpoint examples:

```text
https://api.crossref.org/works?query.bibliographic=self-inversive%20cubic%20image%20unit%20disk%20radius%20coefficient&filter=until-pub-date:2026-08-29&rows=5
https://api.openalex.org/works?search=self-inversive%20cubic%20image%20unit%20disk%20radius%20coefficient&filter=from_publication_date:1900-01-01,to_publication_date:2026-08-29&per-page=5
```

### 4.4 zbMATH Open

The live interface returned `No Documents Found` for:

```text
ti:self-inversive & covering
ti:self-inversive & image
ti:self-inversive & inradius
ti:self-inversive & quadratic
ti:self-inversive & quartic
ti:self-inversive & quintic
ti:self-inversive & trinomial
self-inversive quadratic covering
self-inversive cubic image disk
self-inversive quartic covering
self-inversive quintic covering
self-inversive inradius
self-inversive trinomial image
self-inversive binomial image
```

The exceptional query `ti:self-inversive & cubic` returned only Calbeck and
Holland--Smyth, excluded in §3.2.  Example stable query URL:
[zbMATH Open search](https://zbmath.org/?q=ti%3Aself-inversive+%26+covering).

### 4.5 Citation tracing and secondary status page

OpenAlex forward citations of Solyanik W260159835 returned zero records.  The
Gate 1 citation tracing of the 1974 “New problems” chapter found no relevant
solution.  The supplied
[SciNet page](https://api.scinet.pub/p/11ff995d-348a-4fda-93d6-a23c6cee26aa)
still displayed the problem as open and zero investigations, but it is a
secondary live page and was not treated as priority evidence.

## 5. Negative-result limitations

This audit distinguishes **not found** from **does not exist**.

- Google Scholar timed out from this environment.  Semantic Scholar returned
  HTTP 429.  MathSciNet was not available through an authenticated interface.
- Crossref and OpenAlex search metadata, not every theorem in every full text.
- zbMATH Open title/keyword search was available, but reviews and indexing can
  omit an elementary corollary or an unadvertised theorem.
- The body of Sheil-Small's Chapter 7 was paywalled.  Only the official chapter
  record and the public book preview's contents/preface were inspected.
- An old proof could be phrased as a statement about omitted values, valency,
  boundary curves, or a normalized Hermitian trigonometric polynomial without
  the modern phrase `self-inversive covering`.  The general covering and
  self-inversive families were searched to reduce, but not eliminate, this
  vocabulary risk.
- Exact low-degree facts can circulate as exercises or folklore and remain
  invisible to DOI/arXiv databases.

These limitations support the confidence levels in the claim ledger rather
than a 100% novelty declaration.

## 6. Publication consequences

If the proof audit succeeds, a manuscript may accurately say that the searches
recorded here found no prior proof of the standard problem through degree three
and no prior versions of the two non-endpoint quartic/quintic branches.  It
should then state separately:

1. the endpoint-max branch is classical/elementary and follows from Solyanik's
   Corollary 1 (or Vieta);
2. the even three-term result is an elementary pullback corollary of the new
   quadratic case;
3. endpoint binomials are elementary and not new; and
4. the unrestricted degree-four and degree-five problems remain unresolved by
   the frozen claims.

The safe overall label is **new partial low-degree results, subject to referee
verification**, not “the first solution of Problem 4.24” and not “all listed
branches are new.”
