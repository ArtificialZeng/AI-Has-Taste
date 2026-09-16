# Citation and bibliography audit (pass 2)

## Result

**PASS.**  The frozen pass-1 ledger in `audit/citation-claim-ledger.md` contains
seven claim/citation pairs (eight distinct keys) and four bibliography-coverage
claims.  All eleven claims are supported.  No citation is missing, misquoted,
decorative, or used to strengthen the accepted theorem.  Search verification was
performed on 2026-09-07 using the mandatory author/title/venue/DOI queries and,
where applicable, arXiv-identifier queries.  The job explicitly prohibited
sub-agents, so the required key-by-key checks were performed serially in this
release context.

## Claim-to-source verification

| Claim | Key | Primary record and exact support | Metadata check | Status |
|---|---|---|---|---|
| C01 | `Williams1973` | Annals of Mathematics article, pp. 120--153; the source's matrix formulation is also stated in the first page of Baker (1983) and Jeandel (2026), PDF p. 1, which attributes the rephrasing and SSE relation to Williams. | Author, title, 1973, volume 98(1), pp. 120--153, DOI `10.2307/1970908` agree with the official Annals record. | Verified (paraphrase) |
| C01 | `Williams1974` | Official two-page erratum to the 1973 article, retained with the original because it corrects the foundational source's erroneous converse between SE and SSE; Jeandel, PDF p. 3, identifies this correction explicitly. | Author, erratum title, 1974, volume 99(2), pp. 380--381, DOI `10.2307/1970903` agree with the official Annals record. | Verified (exact companion record) |
| C02 | `Baker1983` | Official Cambridge PDF, abstract and Theorem 1.1, pp. 501--502: the theorem concerns positive 2-by-2 integral matrices of nonnegative determinant.  It cannot cover determinant -131. | Author, title, journal, volume 3(4), pp. 501--508, 1983, DOI `10.1017/S0143385700002091` agree with Cambridge. | Verified (exact) |
| C03 | `Baker1987` | Official Elsevier abstract: the paper presents a sufficient condition via connected components of a directed graph, strengthens earlier 2-by-2 results, and studies shear adjacency.  Jeandel's Theorem 1, PDF p. 3, records the applicable determinant bound `det A >= -tr(A)`; here `-131 < -2`. | Author, title, journal, volume 93, pp. 131--147, 1987, DOI `10.1016/S0024-3795(87)90319-3` agree with Elsevier. | Verified (paraphrase) |
| C04 | `ChoeShin1997` | Official Cambridge abstract: the negative-determinant extension requires `-2 tr A <= det A < -tr A` and nonprime absolute determinant.  Here the determinant is -131, outside the interval and prime in absolute value. | Authors, title, Mathematika 44(2), pp. 302--312, 1997, DOI `10.1112/S0025579300012614` agree with Cambridge. | Verified (exact) |
| C05 | `Jeandel2026` | arXiv:2609.03567v1, Problem 3 and Theorem 2, PDF pp. 4--5: the family is stated and chains are proved for `k <= 10` and `k=12`; the following paragraph says no SSE was found for any `k >= 11`.  The same page calls the lag-4 observation “Preliminary work” that “does not prove” the suggestion. | Emmanuel Jeandel, title, math.DS, v1 dated 3 September 2026, DOI `10.48550/arXiv.2609.03567` agree with arXiv. | Verified (exact) |
| C06 | `Neukirch1999` | Chapter I, Section 7, “Dirichlet's Unit Theorem,” beginning p. 39.  The theorem gives the unit-group rank; for a real quadratic field the free part is cyclic.  The manuscript itself proves which positive generator is least, so the citation is not asked to support that computation. | Jürgen Neukirch, *Algebraic Number Theory*, Springer, 1999, DOI `10.1007/978-3-662-03983-0`; the official Springer contents put Chapter I at pp. 1--97. | Verified (paraphrase) |
| C07 | `ZengLiuRatnavelu2026` | Official Preprints.org v1 abstract and Reproducibility and Disclosure section: an explicit real 2-by-2 rank-one matrix counterexample is certified by seven positive rational differences in equations (11)--(18), without numerical linear algebra. | Authors, title, version/date, venue and DOI `10.20944/preprints202608.1067.v1` agree with Preprints.org and arXiv:2608.15558v1. | Verified (exact) |

Primary URLs inspected:

- Williams (1973): <https://annals.math.princeton.edu/1973/98-1/p04>
- Williams (1974): <https://annals.math.princeton.edu/1974/99-2/p06>
- Baker (1983): <https://doi.org/10.1017/S0143385700002091>
- Baker (1987): <https://doi.org/10.1016/S0024-3795(87)90319-3>
- Choe--Shin (1997): <https://doi.org/10.1112/S0025579300012614>
- Jeandel (2026): <https://arxiv.org/abs/2609.03567v1>
- Neukirch (1999): <https://doi.org/10.1007/978-3-662-03983-0>
- Zeng--Liu--Ratnavelu (2026): <https://www.preprints.org/manuscript/202608.1067>

The local Jeandel PDF was inspected directly and is byte-identical to the frozen
primary-source artifact.  Live Crossref access from WSL failed at the network
boundary; before relying on publisher records I enumerated `literature/crossref-*`
and found no supervisor capture in this project.  This operational limitation does
not affect the records above because all were independently verified at their
publisher, arXiv, or official preprint pages.

## Bibliography coverage and novelty scope

Coverage is appropriate and not library-only: Williams supplies the foundational
relation; Baker and Choe--Shin are the natural closest older sufficient results;
Jeandel supplies the exact problem origin and closest same-family results;
Neukirch supplies the nontrivial unit theorem used by the proof.  The one selected
active-library item supports a narrowly stated methodological comparison.  A
second library item would not support a comparably natural nearby claim and was
therefore not added.

Focused searches for the exact `k=11` pair, determinant -131, minimum lag, and
lag 22 returned no primary result equivalent to the manuscript's fixed-instance
minimum-lag theorem.  This is only a bounded literature comparison.  The
manuscript correctly makes no priority claim and leaves unrestricted SSE
unresolved.

## Mechanical consistency

The bibliography checker extracted eight keys; all eight occur exactly once in
`manuscript/references.bib`, all appear in the final `.aux`, and there are no unused
entries or custom citation macros.  No BibTeX or citation-key edits were needed.
