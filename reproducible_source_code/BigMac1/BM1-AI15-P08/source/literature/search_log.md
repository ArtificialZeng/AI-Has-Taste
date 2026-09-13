# Search log

## 2026-08-29 — first-pass NOVELTY_LOCK

Frozen claims: exact source wording and attribution; present open status; known
degree-\(2,3,4,5\) cases; standard definition; nearest covering theorem.

Primary records inspected:

- Hayman--Lingham, arXiv:1809.07200v2 and extracted source TeX, Problem 4.24,
  lines 2375--2384; Springer book DOI 10.1007/978-3-030-25165-9.
- Cambridge “New problems,” DOI 10.1017/CBO9780511662263.034 (metadata and
  preview only; full 1974 problem text unavailable).
- Solyanik, arXiv:1410.6772, source proof of the binomial-weighted covering
  radius.
- Lalin--Smyth, DOI 10.1007/s10474-012-0225-4, for the standard
  conjugate-reciprocal definition.
- Supplied SciNet page, inspected as a secondary live record.

Exact phrase queries included:

```text
"Problem 4.24" "self-inversive" polynomial
"self-inversive polynomial" "covering theorem"
"self-inversive polynomial" "disc of radius"
"self-inversive polynomial" image unit disk
"self-inversive polynomial" quadratic/cubic/quartic/quintic covering disk
"Sheil-Small" polynomial covering
```

Formal-database routes: arXiv (67 broad self-inversive records screened),
Crossref (up to 100 relevance-ranked records per broad query), OpenAlex plus
forward citations to the 1974 chapter, Springer/Cambridge/DOI metadata, and
supplemental publisher/web searches.  Direct exhaustive MathSciNet, zbMATH,
Google Scholar, Semantic Scholar, and OEIS access was incomplete or blocked;
these limitations are recorded in `literature/novelty_report.md` §3.5.

Outcome: `PROVISIONAL OPEN / NOT FOUND`, not a proof of absence.  No complete
solution/counterexample and no degree-\(2,3,4,5\) covering theorem was located.
A result-specific second pass is mandatory after the exact theorem endpoint
is frozen.

Material source correction: arXiv v2 literally uses \(1/\zeta\), whereas the
user and SciNet use the standard \(1/\bar\zeta\).  No erratum was found.
The work here follows the user's explicit standard convention.

Full reproducible URLs, queries, hashes, and access limitations:
`literature/novelty_report.md`.

## 2026-08-29 — Gate 6 claim-specific second NOVELTY_LOCK

Definition frozen for this pass: exact degree \(n\ge1\), with the zero multiset
invariant under \(z\mapsto1/\bar z\).  Claims searched, without broadening, were:

1. \(\mathsf C_n\) for every \(1\le n\le3\);
2. \(\mathsf C_n\) for \(n=4,5\) when (a) an endpoint coefficient realizes
   \(A\), (b) a zero is off the unit circle, or (c) all roots are unimodular and
   \(2|a_n|\ge A\);
3. the even support class \(\{0,n/2,n\}\) and odd endpoint binomials.

Exact general-web/publisher queries included:

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

The arXiv API was queried with these exact Boolean strings (maximum 20 records
per narrow query), in addition to re-screening the broad `all:"self-inversive"`
family from Gate 1:

```text
all:"self-inversive" AND (all:quadratic OR all:cubic) AND (all:covering OR all:image OR all:inradius)
all:"self-inversive" AND (all:quartic OR all:quintic) AND (all:covering OR all:image OR all:inradius)
all:"self-inversive" AND (all:trinomial OR all:binomial) AND (all:covering OR all:image)
all:"self-inversive" AND all:"unit disk" AND all:"coefficient"
```

The first three narrow queries returned no papers; the fourth returned only an
unrelated 2025 random-polynomial paper.  No claim match was found.

Crossref REST `query.bibliographic` searches (filtered through 2026-08-29;
top five relevance-ranked records inspected for each exact narrow query) were:

```text
self-inversive quadratic covering unit disk
self-inversive cubic image unit disk radius coefficient
self-inversive quartic zero off unit circle image
self-inversive quintic zero off unit circle image
self-inversive polynomial all roots unimodular 2 leading coefficient
self-inversive trinomial image unit disk
self-inversive endpoint binomial image disk
```

They returned zero-location papers, the two cubic-geometry papers, and
Sheil-Small's chapter, but no exact covering statement.  The same seven strings
were run in OpenAlex through 2026-08-29 (top five screened); its results were
mostly semantically unrelated and contained no exact match.  The OpenAlex
record for Solyanik's arXiv:1410.6772 was also checked: W260159835 reported
zero citing works at the audit time, so forward-citation screening there added
no candidates.

zbMATH Open's live search interface was accessible on this pass.  The following
queries each returned `No Documents Found`:

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

`ti:self-inversive & cubic` returned exactly two mathematical candidates:
Zbl 1420.30001 (Holland--Smyth, DOI
10.1080/00029890.2019.1568151) and Calbeck, arXiv:1511.01340.  The former's
official abstract concerns cardioid tangent geometry; the latter's full arXiv
source, Theorem 2.1, concerns conics tangent to triangles formed by roots.
Neither concerns the image \(P(\mathbb D)\).

Primary/official items inspected for exclusion or overlap:

- Alexey Solyanik, arXiv:1410.6772, source TeX, Lemma 3 and Corollary 1.
  Corollary 1 says that a zero-constant-term polynomial \(q\) covers the
  origin-centered disk of radius
  \(\max_k|\widehat q(k)|/\binom nk\).  The \(k=n\) term proves
  \(B(a_0,|a_n|)\subset P(\mathbb D)\) for every polynomial.  Therefore the
  endpoint-max branch is already known, although this does not solve the
  unweighted interior-coefficient problem.
- William Calbeck, arXiv:1511.01340, full source, Theorem 2.1: root-triangle
  conic tangency only.
- Finbarr Holland and Roger Smyth, DOI
  10.1080/00029890.2019.1568151, official abstract: cardioid tangent geometry
  only.
- Piroska Lakatos and László Losonczi, DOI 10.5486/PMD.2004.3250,
  official publisher PDF, Theorem 1: coefficient conditions for roots to be
  unimodular, not image covering.
- Matilde N. Lalin and Chris J. Smyth, arXiv:1201.0774 / DOI
  10.1007/s10474-012-0225-4, Theorem 1 and its corollaries: zero
  unimodularity, not image covering.
- T. Sheil-Small, *Complex Polynomials*, Chapter 7, DOI
  10.1017/CBO9780511543074.009.  The official/public 45-page preview exposes
  the chapter contents and preface description (interspersion, maximum-modulus
  inequalities, univalent polynomials, Suffridge theory), but not the chapter
  body; an unadvertised statement in the inaccessible body cannot be excluded.

Access limitations: direct Google Scholar timed out; Semantic Scholar's API
returned HTTP 429; MathSciNet was not authenticated.  Crossref, OpenAlex,
arXiv, zbMATH Open, DOI/publisher pages, author/arXiv full texts, and forward
citation data were used as the available formal routes.  A database not-found
result is not proof of nonexistence.

Outcome: **PARTIAL NOVELTY CLEARANCE, CLAIMS DISAGGREGATED.**  No exact prior
match was found for the positive-degree \(n\le3\) theorem, the off-unit-zero
quartic/quintic branch, the all-unimodular quartic/quintic condition
\(2|a_n|\ge A\), or the even three-term pullback class.  The endpoint-max
branch is known for arbitrary polynomials, and endpoint binomials are an
elementary special case (indeed in every degree), so neither may be advertised
as new.  Full details and stable URLs are in
`literature/second_novelty_lock.md`.
